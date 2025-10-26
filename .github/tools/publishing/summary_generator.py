"""GitBook summary generation module.

This module handles the generation of SUMMARY.md for GitBook documentation.
It supports different ordering modes and submodes for flexible summary organization.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import List, Optional, Union
import logging
import re

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
        lines = []
        indent = "  " * self.level
        if self.path:
            lines.append(f"{indent}* [{self.title}]({self.path.as_posix()})")
        else:
            lines.append(f"{indent}* {self.title}")

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
        # Add header
        lines = ["# Summary"]
        # Add all nodes
        lines.extend(self.root.to_lines())
        return lines


def build_summary_tree(
    root_dir: Path, mode: SummaryMode, submode: SubMode
) -> SummaryTree:
    """Build a summary tree from the filesystem structure."""

    def process_directory(path: Path, level: int = 0) -> SummaryNode:
        # Create directory node
        dir_node = SummaryNode(
            title=path.name,
            path=None,  # Will be updated if index.md exists
            level=level,
        )

        # Process markdown files in this directory
        md_files = sorted(path.glob("*.md"))
        for md_file in md_files:
            if md_file.name.lower() == "index.md":
                dir_node.path = md_file.relative_to(root_dir)
                continue

            # Create file node
            is_appendix = tree._is_appendix_path(md_file)
            node = SummaryNode(
                title=md_file.stem,
                path=md_file.relative_to(root_dir),
                level=level + 1,
                is_appendix=is_appendix,
            )
            dir_node.add_child(node)

        # Process subdirectories
        for subdir in sorted(p for p in path.iterdir() if p.is_dir()):
            if not subdir.name.startswith("."):  # Skip hidden directories
                subdir_node = process_directory(subdir, level + 1)
                dir_node.add_child(subdir_node)

        return dir_node

    # Create empty root node
    root = SummaryNode(title="", path=None)
    tree = SummaryTree(root=root, mode=mode, submode=submode)

    # Process root directory
    root_node = process_directory(root_dir)
    # Move root's children to tree root
    tree.root.children = root_node.children

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
