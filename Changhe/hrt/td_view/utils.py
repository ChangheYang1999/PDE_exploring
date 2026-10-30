from __future__ import annotations

import unicodedata


def get(snapshot: dict, key: str, default=0):
    return snapshot.get(key, default)


def safe_text(text: str) -> str:
    return "".join(" " if unicodedata.category(ch).startswith("C") else ch for ch in str(text))


def cell_width(ch: str) -> int:
    if unicodedata.combining(ch):
        return 0
    return 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1


def truncate(text: str, width: int) -> str:
    text = safe_text(text)
    if width <= 0:
        return ""
    if sum(map(cell_width, text)) <= width:
        return text
    suffix = "." * min(3, width)
    output, used = [], 0
    for ch in text:
        size = cell_width(ch)
        if used + size > width - len(suffix):
            break
        output.append(ch)
        used += size
    return "".join(output) + suffix


def visible_lines(lines: list[str], height: int) -> list[str]:
    """Newest content wins; an ellipsis marks every omitted older block."""
    if height <= 0:
        return []
    if len(lines) <= height:
        return lines
    return ["..."] + (lines[-(height-1):] if height > 1 else [])


def safe_write(screen, x: int, y: int, text: str, attribute: int = 0) -> None:
    """Absolute terminal (x,y) adapter for curses' (y,x) argument order."""
    height, width = screen.getmaxyx()
    if not (0 <= y < height and 0 <= x < width):
        return
    clipped = truncate(text, width - x)
    if not clipped:
        return
    # curses may raise AFTER writing the bottom-right cell; it is safe to ignore.
    import curses
    try:
        screen.addstr(y, x, clipped, attribute)
    except curses.error:
        pass
