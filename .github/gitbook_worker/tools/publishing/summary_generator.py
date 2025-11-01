"""Utilities for generating GitBook compatible ``SUMMARY.md`` files."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from enum import Enum
from itertools import chain
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)


class SummaryMode(Enum):
    """Supported summary generation modes."""

    ORDERED_BY_FILESYSTEM = "ordered-by-filesystem"
    ORDERED_BY_ALPHANUMERIC = "ordered-by-alphanumeric"
    GITBOOK_STYLE = "gitbook-style"
    MANUAL = "manual"


class SubMode(Enum):
    """Submodes for summary generation."""

    NONE = "none"
    FLIP = "flip"  # For filesystem/alphanumeric: reverse the order
    APPENDIX_LAST = "appendix-last"  # For gitbook-style: move appendices to end
    NO_CHANGE = "no-change"  # For gitbook-style: keep existing order


@dataclass
class SummaryNode:
    """Represents a node in the summary tree."""

    title: str
    path: Optional[Path]  # None for directory nodes without an index file
    level: int = 0
    children: List["SummaryNode"] = field(default_factory=list)
    is_appendix: bool = False

    def add_child(self, node: "SummaryNode") -> None:
        """Add a child node to this node."""
        node.level = self.level + 1
        self.children.append(node)

    def to_lines(self) -> List[str]:
        """Convert this node and its children to summary lines."""
        indent = "  " * self.level
        if self.path:
            line = f"{indent}* [{self.title}]({self.path.as_posix()})"
        else:
            line = f"{indent}* {self.title}" if self.title else ""

        lines: List[str] = [line] if line else []
        for child in self.children:
            lines.extend(child.to_lines())
        return lines


@dataclass
class SummaryTree:
    """Represents the complete summary tree."""

    root: SummaryNode
    mode: SummaryMode
    submode: SubMode

    def _is_appendix_path(self, path: Path) -> bool:
        """Check if a path represents an appendix entry."""
        name_lower = path.name.lower()
        stem_lower = path.stem.lower()

        # Check filename patterns
        if any(
            stem_lower.startswith(prefix)
            for prefix in ["anhang-", "appendix-", "appendices-"]
        ):
            return True

        # Check for standalone words
        if re.search(r"\b(anhang|appendix)\b", stem_lower):
            return True

        # Try to read first heading if it's a markdown file
        if path.suffix.lower() == ".md":
            try:
                content = path.read_text(encoding="utf-8")
                first_line = next(
                    (
                        line
                        for line in content.splitlines()
                        if line.strip().startswith("#")
                    ),
                    "",
                )
                if re.match(r"^#\s*(Anhang|Appendix)\b", first_line):
                    return True
            except Exception as e:
                logger.debug(f"Error reading {path}: {e}")

        return False

    def _sort_nodes(self, nodes: List[SummaryNode]) -> List[SummaryNode]:
        """Sort nodes according to the current mode and submode."""
        if self.mode == SummaryMode.ORDERED_BY_FILESYSTEM:
            # Keep filesystem order, optionally flip
            sorted_nodes = nodes

        elif self.mode == SummaryMode.ORDERED_BY_ALPHANUMERIC:
            # Sort by title, considering numeric prefixes naturally
            def natural_sort_key(node: SummaryNode):
                parts = re.split("([0-9]+)", node.title)
                return [int(part) if part.isdigit() else part.lower() for part in parts]

            sorted_nodes = sorted(nodes, key=natural_sort_key)

        elif self.mode == SummaryMode.GITBOOK_STYLE:
            if self.submode == SubMode.APPENDIX_LAST:
                # Split into regular and appendix nodes, preserve order within each group
                regular = [n for n in nodes if not n.is_appendix]
                appendices = [n for n in nodes if n.is_appendix]

                def appendix_key(node: SummaryNode) -> tuple[int, str, str]:
                    match = re.search(r"(Anhang|Appendix)\s+([A-Z])", node.title, re.IGNORECASE)
                    if match:
                        return (0, match.group(2).upper(), node.title.lower())
                    return (1, node.title.lower(), node.path.as_posix() if node.path else "")

                appendices.sort(key=appendix_key)
                sorted_nodes = regular + appendices
            elif self.submode == SubMode.NO_CHANGE:
                return nodes  # Keep existing order
            else:
                sorted_nodes = nodes  # Default gitbook ordering

        else:  # MANUAL mode
            return nodes  # Keep manual ordering

        # Apply flip if requested (for filesystem/alphanumeric modes)
        if self.submode == SubMode.FLIP:
            sorted_nodes = list(reversed(sorted_nodes))

        return sorted_nodes

    def sort_tree(self) -> None:
        """Sort the entire tree according to mode and submode."""

        def sort_recursive(node: SummaryNode):
            # Sort children first (depth-first)
            for child in node.children:
                sort_recursive(child)
            # Then sort current level
            node.children = self._sort_nodes(node.children)

        # Start recursion from root if not in manual mode
        if self.mode != SummaryMode.MANUAL:
            sort_recursive(self.root)

    def to_lines(self) -> List[str]:
        """Convert the entire tree to summary lines."""
        lines = ["# Summary", ""]
        for child in self.root.children:
            lines.extend(child.to_lines())
        return [line for line in lines if line is not None]


def build_summary_tree(
    root_dir: Path, mode: SummaryMode, submode: SubMode
) -> SummaryTree:
    """Build a summary tree from the filesystem structure."""

    def extract_title(md_path: Path) -> str:
        """Return a human readable title from ``md_path``."""

        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception as exc:  # pragma: no cover - best effort fallback
            logger.debug("Failed to read %s: %s", md_path, exc)
            text = ""

        lines = iter(text.splitlines())
        # Skip YAML front matter if present
        try:
            first = next(lines)
        except StopIteration:
            first = ""

        if first.strip() == "---":
            for line in lines:
                if line.strip() == "---":
                    break
        else:
            # put back the first line if it wasn't front matter
            lines = chain([first], lines)

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                return stripped.lstrip("#").strip()

        stem = md_path.stem.replace("-", " ").replace("_", " ").strip()
        return stem or md_path.stem

    def process_directory(path: Path, level: int = 0) -> SummaryNode:
        dir_node = SummaryNode(
            title=path.name.replace("-", " ").replace("_", " ").strip() or path.name,
            path=None,
            level=level,
            is_appendix=tree._is_appendix_path(path),
        )

        readme_names = {"readme.md", "index.md"}
        summary_names = {"summary.md"}
        md_files = sorted(path.glob("*.md"))

        children: List[SummaryNode] = []

        for md_file in md_files:
            lower_name = md_file.name.lower()
            if lower_name in summary_names:
                continue

            if lower_name in readme_names:
                dir_node.path = md_file.relative_to(root_dir)
                dir_node.title = extract_title(md_file)
                continue

            node = SummaryNode(
                title=extract_title(md_file),
                path=md_file.relative_to(root_dir),
                level=level + 1,
                is_appendix=tree._is_appendix_path(md_file),
            )
            children.append(node)

        for subdir in sorted(p for p in path.iterdir() if p.is_dir()):
            if subdir.name.startswith("."):
                continue
            subdir_node = process_directory(subdir, level + 1)
            children.append(subdir_node)

        for child in children:
            dir_node.add_child(child)

        return dir_node

    root = SummaryNode(title="", path=None)
    tree = SummaryTree(root=root, mode=mode, submode=submode)

    root_node = process_directory(root_dir)

    def shift_levels(node: SummaryNode, delta: int) -> None:
        node.level = max(0, node.level + delta)
        for child in node.children:
            shift_levels(child, delta)

    root_children: List[SummaryNode] = []
    if root_node.path:
        root_entry = SummaryNode(
            title=root_node.title,
            path=root_node.path,
            level=0,
            is_appendix=root_node.is_appendix,
        )
        root_children.append(root_entry)

    for child in root_node.children:
        shift_levels(child, -1)
        root_children.append(child)
    tree.root.children = root_children

    # Sort the tree according to mode/submode
    tree.sort_tree()

    return tree


def generate_summary(
    root_dir: Path, mode: str = "gitbook-style", submode: str = "none"
) -> List[str]:
    """Generate a SUMMARY.md content based on specified mode and submode.

    Args:
        root_dir: Root directory containing documentation files
        mode: One of 'ordered-by-filesystem', 'ordered-by-alphanumeric',
              'gitbook-style', or 'manual'
        submode: Mode-specific submode ('none', 'flip', 'appendix-last', 'no-change')

    Returns:
        List of lines for SUMMARY.md
    """
    try:
        summary_mode = SummaryMode(mode)
        sub_mode = SubMode(submode)
    except ValueError as e:
        logger.error(f"Invalid mode/submode: {e}")
        raise

    tree = build_summary_tree(root_dir, summary_mode, sub_mode)
    return tree.to_lines()


# Manual marker constant
DEFAULT_MANUAL_MARKER = "<!-- SUMMARY: MANUAL -->"
