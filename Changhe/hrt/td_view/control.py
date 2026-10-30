from __future__ import annotations

import time
from enum import Enum, auto

from .scene import ViewScene

SPEEDS = (0.25, 0.5, 1.0, 2.0, 4.0)


class ACTION(Enum):
    NONE = auto()
    REDRAW = auto()
    QUIT = auto()


def handle_key(vs: ViewScene, key: str, now: float) -> ACTION:
    if key == "q":
        return ACTION.QUIT
    if key == " ":
        vs.paused = not vs.paused if vs.index < len(vs.log.frames) - 1 else True
    elif key in ("LEFT", "k", "RIGHT", "j", "HOME", "0", "END", "G"):
        if key in ("LEFT", "k"):
            vs.index = max(0, vs.index - 1)
        elif key in ("RIGHT", "j"):
            vs.index = min(len(vs.log.frames) - 1, vs.index + 1)
        elif key in ("HOME", "0"):
            vs.index = 0
        else:
            vs.index = len(vs.log.frames) - 1
        vs.paused = True
    elif key == "v":
        vs.verbose = not vs.verbose
    elif key in ("+", "=", "-"):
        vs.speed_index = max(0, min(len(SPEEDS) - 1, vs.speed_index + (-1 if key == "-" else 1)))
    elif key == "RESIZE":
        return ACTION.REDRAW
    else:
        return ACTION.NONE
    if key != "v":
        vs.next_due = now + 1 / SPEEDS[vs.speed_index]
    return ACTION.REDRAW


def advance(vs: ViewScene, now: float) -> ACTION:
    if vs.paused or now < vs.next_due:
        return ACTION.NONE
    interval = 1 / SPEEDS[vs.speed_index]
    steps = 1 + int((now - vs.next_due) / interval)
    vs.index = min(len(vs.log.frames) - 1, vs.index + steps)
    vs.next_due += steps * interval
    if vs.index == len(vs.log.frames) - 1:
        vs.paused = True
    return ACTION.REDRAW


def run_replay(log, redraw):
    """Run terminal playback, dispatching redraws to the supplied callback."""
    import locale
    import curses

    # Python UTF-8 mode alone does not make the C curses library Unicode-aware.
    # Some macOS environments inherit an unsupported Linux C.UTF-8 locale.
    for candidate in ("", "C.UTF-8", "en_US.UTF-8", "UTF-8"):
        try:
            locale.setlocale(locale.LC_CTYPE, candidate)
        except locale.Error:
            continue
        if locale.getencoding().lower().replace("-", "") == "utf8":
            break
    else:
        raise ValueError("replay needs an available UTF-8 locale (for example en_US.UTF-8)")

    def loop(screen):
        try:
            curses.curs_set(0)
        except curses.error:
            pass
        screen.keypad(True)
        screen.timeout(25)
        vs = ViewScene(log, paused=len(log.frames) == 1, next_due=time.monotonic() + 1)
        redraw(screen, vs)
        keys = {curses.KEY_LEFT: "LEFT", curses.KEY_RIGHT: "RIGHT", curses.KEY_HOME: "HOME",
                curses.KEY_END: "END", curses.KEY_RESIZE: "RESIZE"}
        while True:
            key = screen.getch()
            now = time.monotonic()
            command = handle_key(vs, keys.get(key, chr(key) if 0 <= key < 256 else ""), now)
            if command is ACTION.QUIT:
                return
            playback = advance(vs, now)
            if command is ACTION.REDRAW or playback is ACTION.REDRAW:
                redraw(screen, vs)

    curses.wrapper(loop)
