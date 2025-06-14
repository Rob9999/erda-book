import ast
import json
import logging
import os
import random
import re
import time
from typing import Any, Dict, List, Tuple

import requests

from .source_extract import extract_sources_of_a_md_file_to_dict


def extract_json_from_ai_output(generated_text: str) -> Tuple[bool, Any]:
    text = generated_text.strip()
    if text.startswith("```json"):
        text = text[7:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    text = text.strip().strip("'").strip('"')
    try:
        return True, json.loads(text)
    except json.JSONDecodeError:
        pass
    try:
        unescaped = ast.literal_eval(text)
        unescaped = ast.literal_eval(unescaped)
        return True, json.loads(unescaped)
    except Exception:
        logging.warning("JSON parsing failed for AI response. Returning raw text.")
    return False, generated_text


def ask_ai(prompt: str, ai_url: str, ai_api_key: str, ai_provider: str, retry_count: int = 0, max_retries: int = 3) -> Tuple[bool, str]:
    headers = {"Authorization": f"Bearer {ai_api_key}", "Content-Type": "application/json"}
    if ai_provider.lower() == "openai":
        payload = {"model": "gpt-4", "messages": [{"role": "user", "content": prompt}], "temperature": 0.7}
        try:
            response = requests.post(ai_url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return True, result["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return False, f"[OpenAI] Fehler: {e}"
    elif ai_provider.lower() == "genai":
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        url_with_key = f"{ai_url}?key={ai_api_key}"
        try:
            response = requests.post(url_with_key, headers={"Content-Type": "application/json"}, json=payload)
            response.raise_for_status()
            result = response.json()
            generated_text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
            return extract_json_from_ai_output(generated_text)
        except requests.exceptions.RequestException as e:
            if getattr(e.response, 'status_code', None) == 429 and retry_count < max_retries:
                wait_time = random.randint(1, 8)
                logging.warning("[GenAI] Zu viele Anfragen. Warte %s Sekunden", wait_time)
                time.sleep(wait_time)
                return ask_ai(prompt, ai_url, ai_api_key, ai_provider, retry_count + 1)
            return False, f"[GenAI] Fehler: {e}"
        except Exception as e:
            return False, f"[GenAI] Fehler: {e}"
    else:
        return False, f"Unbekannter AI-Provider: '{ai_provider}'"


def proof_and_repair_internal_references(md_files: List[str], summary_md: str) -> List[Dict[str, Any]]:
    summary_map = {}
    link_re = re.compile(r"\*+\s*\[(?P<title>[^\]]+)\]\((?P<link>[^)]+\.md)\)")
    with open(summary_md, encoding="utf-8") as sf:
        for line in sf:
            m = link_re.search(line)
            if m:
                summary_map[m.group("title")] = m.group("link")

    report = []
    for file in md_files:
        sources = extract_sources_of_a_md_file_to_dict(file).get(str(file), [])
        if not sources:
            continue
        with open(file, encoding="utf-8") as f:
            lines = f.read().splitlines()
        for entry in sources:
            for name, ref in entry.items():
                idx = ref.get("lineno", 1) - 1
                if idx < len(lines):
                    lines.append(name)
        with open(file, "w", encoding="utf-8") as wf:
            wf.write("\n".join(lines) + "\n")
        report.append({"action": "footnote_added", "file": file})
    return report


def proof_and_repair_external_reference(
    reference_as_line: str,
    footnote_index: int,
    prompt: str,
    ai_url: str,
    ai_api_key: str,
    ai_provider: str,
) -> Tuple[bool, str]:
    """Send a prompt for a single reference to the chosen AI service.

    The AI should validate and, if necessary, correct the citation.  The
    response is expected to be a JSON string matching ``json_hint`` below.
    """

    structured_schema = """
    {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Zitationspr\u00fcfungsergebnis",
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Ob die Zitation erfolgreich validiert und ggf. korrigiert wurde"
    },
    "org": {
      "type": "string",
      "description": "Die original eingegebene (ungepr\u00fcfte) Quellenangabe"
    },
    "new": {
      "type": "string",
      "description": "Die neue, wissenschaftlich korrekte Zitationszeile im gew\u00fcnschten Format (optional)",
      "nullable": true
    },
    "error": {
      "type": "string",
      "description": "Fehlermeldung, falls die Zitation nicht erstellt werden konnte (optional)",
      "nullable": true
    },
    "hint": {
      "type": "string",
      "description": "Hilfestellung zur Verbesserung oder Vervollst\u00e4ndigung der Quelle (optional)",
      "nullable": true
    },
    "validation_date": {
      "type": "string",
      "format": "date",
      "description": "Das Datum der Pr\u00fcfung und ggf. der URL-Validierung (today)"
    },
    "type": {
      "type": "string",
      "description": "Kategorisierung der Quelle: 'internal reference', 'external url', 'external reference' oder '?'",
      "enum": ["internal reference", "external url", "external reference", "?"]
    }
  },
  "required": ["success", "org", "validation_date", "type"]
}
    """

    json_hint = """
    {
        "success": true|false,
        "org": "<Originalquelle>",
        "new": "<neue Zitationszeile oder null>",
        "error": "<Fehlermeldung oder null>",
        "hint": "<Hinweis oder null>",
        "validation_date": "YYYY-MM-DD",
        "type": "internal reference" | "external url" | "external reference" | "?"
    }
    """

    full_prompt = (
        f"{prompt}\n\nQuelle [{footnote_index}]: {reference_as_line}\n\n\n\n"
        f"Generate a structured JSON according:\n{json_hint}"
    )

    return ask_ai(full_prompt, ai_url, ai_api_key, ai_provider)


def proof_and_repair_external_references(md_files: List[str], prompt: str, ai_url: str, ai_api_key: str, ai_provider: str) -> List[Dict[str, Any]]:
    report = []
    for file in md_files:
        src = extract_sources_of_a_md_file_to_dict(file).get(str(file), [])
        if not src:
            continue
        lines = open(file, encoding="utf-8").read().splitlines()
        for entry in src:
            for name, info in entry.items():
                idx = info.get("lineno", 1) - 1
                success, result = proof_and_repair_external_reference(
                    reference_as_line=lines[idx],
                    footnote_index=1,
                    prompt=prompt,
                    ai_url=ai_url,
                    ai_api_key=ai_api_key,
                    ai_provider=ai_provider,
                )
                if success:
                    parsed_success, data = (
                        extract_json_from_ai_output(result)
                        if isinstance(result, str)
                        else (True, result)
                    )
                    if parsed_success and isinstance(data, dict) and data.get("new"):
                        lines[idx] = data["new"]
        with open(file, "w", encoding="utf-8") as wf:
            wf.write("\n".join(lines) + "\n")
    return report
