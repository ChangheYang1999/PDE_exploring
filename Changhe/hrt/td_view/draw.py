"""Fixed three-column display. No pathfinding or path rendering belongs here."""
from __future__ import annotations

import json

from .scene import PlayScene, ViewScene, buildscene, visible_events
from .utils import safe_write, truncate, visible_lines

PLAYER_1_X = 0
PLAYER_2_X = 30
EVENT_X = 60
PLAYER_WIDTH = 28
CELL_WIDTH = 2
MAP_Y = 5
MIN_WIDTH = 92
MIN_HEIGHT = 24
P_border = 0
MINION_LABELS = {
    "tier1": "1", "tier2": "2", "tier3": "3", "tier4": "4", "tier5": "5",
    "scout": "1", "brute": "2", "titan": "3",
}


class Canvas:
    def __init__(self, screen):
        self.screen = screen

    def _add_str(self, x: int, y: int, ch: str, attribute: int = P_border):
        safe_write(self.screen, x, y, ch, attribute)


def _draw_player(ps: PlayScene, x: int, canvas: Canvas, height: int):
    canvas._add_str(x, 2, truncate(ps.name, PLAYER_WIDTH))
    canvas._add_str(x, 3, truncate(f"HP: {ps.hp}  gold: {ps.gold}", PLAYER_WIDTH))
    canvas._add_str(x, MAP_Y, "┌" + "─" * (12 * CELL_WIDTH) + "┐", P_border)
    for y, row in enumerate(ps.grid):
        canvas._add_str(x, MAP_Y + 1 + y, "│", P_border)
        for column, symbol in enumerate(row):
            canvas._add_str(x + 1 + column * CELL_WIDTH, MAP_Y + 1 + y, symbol + " ")
        canvas._add_str(x + 1 + 12 * CELL_WIDTH, MAP_Y + 1 + y, "│", P_border)
    canvas._add_str(x, MAP_Y + 13, "└" + "─" * (12 * CELL_WIDTH) + "┘", P_border)
    canvas._add_str(x, MAP_Y + 14, truncate(f"T: {ps.n_turrets}  F: {ps.n_factories}", PLAYER_WIDTH))
    tokens = [MINION_LABELS.get(entry["type"], "?") for entry in ps.roster]
    roster = f"Roster({len(tokens)}):" + ("".join(tokens) if tokens else "-")
    lines = [roster[start:start + PLAYER_WIDTH] for start in range(0, len(roster), PLAYER_WIDTH)]
    roster_y = MAP_Y + 15
    available_lines = max(0, height - roster_y - 2)
    # Leave the last two rows for the outcome and playback controls.
    for index, line in enumerate(lines[:available_lines]):
        if index == available_lines - 1 and len(lines) > available_lines:
            line = truncate(line + "...", PLAYER_WIDTH)
        canvas._add_str(x, roster_y + index, line)


def event_lines(vs: ViewScene) -> list[str]:
    lines = []
    for round_number, player, event in visible_events(vs):
        prefix = f"R{round_number} P{player} "
        kind = event["kind"]
        if vs.verbose:
            lines.append(prefix + kind)
            details = {k: v for k, v in event.items() if k != "kind"}
            # Round events only: no tick traces or state reenactment.
            for key, value in details.items():
                label = f"{key} income (gold)" if kind == "income" and key in ("path", "factories", "hits") else key
                lines.append(f"  {label}: {json.dumps(value, ensure_ascii=False, sort_keys=True)}")
        elif kind == "action":
            action = event.get("action")
            label = action.get("op", "invalid") if isinstance(action, dict) else "invalid"
            status = "ok" if event.get("accepted") else f"rejected: {event.get('reason', '?')}"
            lines.append(prefix + f"{label} {status}")
        elif kind == "combat":
            lines.append(prefix + f"hits {event.get('outgoing_hits', 0)}, damage taken {event.get('base_damage', 0)}")
        elif kind == "income":
            lines.append(prefix + f"income +{event.get('total', 0)}")
        elif kind == "expiration":
            lines.append(prefix + f"expired {len(event.get('roster_ids', []))}")
        elif kind == "bot_error":
            lines.append(prefix + f"bot_error: {event.get('reason', '?')}")
        else:
            lines.append(prefix + kind)
    return lines


def _draw_events(vs: ViewScene, canvas: Canvas, height: int, width: int):
    canvas._add_str(EVENT_X, 2, "EVENT (detailed)" if vs.verbose else "EVENT (brief)")
    for index, line in enumerate(visible_lines(event_lines(vs), height - 4)):
        canvas._add_str(EVENT_X, 3 + index, truncate(line, width - EVENT_X))


def draw(screen, state: dict[str, ViewScene]):
    vs = state["vs"]
    screen.erase()
    height, width = screen.getmaxyx()
    canvas = Canvas(screen)
    if height < MIN_HEIGHT or width < MIN_WIDTH:
        canvas._add_str(0, 0, f"Enlarge terminal to {MIN_WIDTH}x{MIN_HEIGHT}; q quits.")
        screen.refresh()
        return
    from .control import SPEEDS
    frame = vs.log.frames[vs.index]
    status = "paused" if vs.paused else "playing"
    canvas._add_str(0, 0, f"Round {frame.round}/{vs.log.frames[-1].round}  {status}  {SPEEDS[vs.speed_index]}x")
    players = buildscene(frame, vs.log.match)
    _draw_player(players[0], PLAYER_1_X, canvas, height)
    _draw_player(players[1], PLAYER_2_X, canvas, height)
    _draw_events(vs, canvas, height, width)
    if vs.index == len(vs.log.frames) - 1 and vs.log.result:
        result = vs.log.result
        outcome = "Draw" if result["winner"] is None else f"P{result['winner']} wins"
        canvas._add_str(0, height - 2, truncate(f"{outcome}: {result['reason']}", EVENT_X - 2))
    canvas._add_str(0, height - 1, "Space pause | k/j prev/next | 0/G first/last | +/- speed | v details | q quit")
    screen.refresh()
