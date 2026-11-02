"""Reproductions of rule facts recorded in bot_research/reports/RULES.md.

Each check calls the unchanged engine (td_game.*) on fresh objects and prints
PASS/FAIL with the observed values. Run from the project root:

    PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" .venv/bin/python -B \
        -m bot_research.experiments.lead.rule_repros
"""
from __future__ import annotations

from td_bots.protocol import collect_actions
from td_game.actions import apply_action
from td_game.combat import Minion, combat_tick, simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry

CFG = balanced_config()
EMPTY = shortest_path(12, 12, [], (0, 0), (11, 11))
results = []


def check(name, ok, detail):
    results.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")


def gun_single_target():
    # Three copies inside gun3 range at different progress; only the frontmost is hit.
    d = PlayerState("D", 800, 0, buildings=[Building(5, 2, "gun3")])
    copies = [Minion(0, 1000, 5, 0, 5), Minion(1, 1000, 5, 0, 4), Minion(2, 1000, 5, 0, 3)]
    alive, _ = combat_tick(1, copies, [], EMPTY, d, CFG)
    hps = [m.hp for m in alive]
    # After moving one step: indices 6, 5, 4 -> cells (6,0), (5,0), (4,0); all within 3.5 of (5,2).
    in_range = [((EMPTY[m.path_index][0] - 5) ** 2 + (EMPTY[m.path_index][1] - 2) ** 2) <= 3.5 ** 2 for m in alive]
    check("gun hits only the frontmost copy in range", hps == [945, 1000, 1000] and all(in_range),
          f"hp after one tick {hps}, all in range {in_range}")


def gun_overkill():
    # Two gun1 cover the same frontmost tier1 (20 hp): both shoot it, the rear copy is untouched.
    d = PlayerState("D", 800, 0, buildings=[Building(2, 1, "gun1"), Building(3, 1, "gun1")])
    copies = [Minion(0, 10, 5, 0, 2), Minion(1, 20, 5, 0, 1)]
    alive, totals = combat_tick(1, copies, [], EMPTY, d, CFG)
    check("guns select before damage resolution (overkill is wasted)",
          [(m.roster_id, m.hp) for m in alive] == [(1, 20)] and totals.killed == 1,
          f"survivors {[(m.roster_id, m.hp) for m in alive]}, killed {totals.killed}")


def splash_all_copies_eight_cells():
    d = PlayerState("D", 800, 0, buildings=[Building(5, 5, "splash")])
    hit_offsets = []
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if (dx, dy) == (0, 0):
                continue
            copies = [Minion(i, 100, 5, 0) for i in range(4)]
            alive, _ = combat_tick(0, copies, [], [(5 + dx, 5 + dy), (5 + dx, 5 + dy)], d, CFG)
            if all(m.hp == 90 for m in alive) and len(alive) == 4:
                hit_offsets.append((dx, dy))
    expected = sorted((dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0))
    check("splash hits all copies on the 8 neighbours (diagonals included), nothing at distance 2",
          sorted(hit_offsets) == expected, f"offsets hit {sorted(hit_offsets)}")


def splash_per_copy_independent_of_count():
    # One splash at (1,1) beside the empty route gives every copy 3 x 10 = 30 damage at
    # indices 0,1,2, so every tier1 (20 hp) dies however many copies come, including
    # copies stacked on the same tick beyond 250 entries.
    buildings = [Building(1, 1, "splash")]
    path = shortest_path(12, 12, {(b.x, b.y) for b in buildings}, (0, 0), (11, 11))
    out = []
    for n in (1, 5, 300, 600):
        d = PlayerState("D", 800, 0, buildings=list(buildings))
        attacker = PlayerState("A", 800, 0, roster=[RosterEntry(i, "tier1", 1, 12) for i in range(n)])
        totals = simulate_map(attacker, d, path, 1, CFG)
        out.append((n, totals.killed, totals.hits, totals.cleared))
    # A copy spawning at tick 249 is attacked once (10 damage) and is then cleared at round end.
    late = {n: sum(1 for k in range(n) if k % 250 == 249) for n, *_ in out}
    check("splash damage per copy is independent of the number of copies (no target cap)",
          all(h == 0 and k == n - late[n] and c == late[n] for n, k, h, c in out),
          f"(copies, killed, hits, cleared) {out}")


def arrival_cutoff():
    # On the empty route (L=22), a copy spawning at tick 227 arrives at 249 (counts), at 228 never.
    data = CFG.to_dict()
    data["minions"]["dummy"] = {"cost": 0, "hp": 1, "damage": 0}
    from td_game.config import config_from_dict
    cfg = config_from_dict(data)
    out = {}
    for s in (227, 228):
        roster = [RosterEntry(i, "dummy", 1, 12) for i in range(s)] + [RosterEntry(s, "tier1", 1, 12)]
        d = PlayerState("D", 800, 0)
        simulate_map(PlayerState("A", 800, 0, roster=roster), d, EMPTY, 1, cfg)
        out[s] = 800 - d.hp
    check("arrival at tick 249 counts, 250 does not (L=22)", out == {227: 5, 228: 0}, f"damage by spawn tick {out}")


def income_and_lifetime():
    e = Engine(CFG, ("A", "B"))
    rec = e.play_round([[{"op": "buy_factory"}, {"op": "buy_minion", "type": "tier1"}], []])
    inc = next(x for x in rec[0]["event"] if x["kind"] == "income")
    ok = inc == {"kind": "income", "path": 22, "factories": 15, "hits": 5, "total": 42}
    for _ in range(11):
        e.play_round([[], []])
    alive_after_12 = len(e.players[0].roster)
    check("factory income in purchase round; hit bounty 5; roster removed after round 12",
          ok and alive_after_12 == 0 and e.players[1].hp == 800 - 12 * 5,
          f"income {inc}, roster after 12 rounds {alive_after_12}, B hp {e.players[1].hp}")


def construction_check_order():
    p = PlayerState("A", 800, 0)
    r = apply_action(p, {"op": "build_wall", "x": 0, "y": 0}, 1, CFG)
    r2 = apply_action(p, {"op": "build_wall", "x": 3, "y": 3}, 1, CFG)
    check("placement legality is checked before gold", r["reason"] == "cannot build at spawn or base"
          and r2["reason"] == "insufficient gold", f"{r['reason']!r}, {r2['reason']!r}")


def blocking_rejected():
    p = PlayerState("A", 800, 100)
    apply_action(p, {"op": "build_wall", "x": 1, "y": 0}, 1, CFG)
    r = apply_action(p, {"op": "build_wall", "x": 0, "y": 1}, 1, CFG)
    check("a building that removes every route is rejected", not r["accepted"] and r["reason"] == "building would block every path",
          r["reason"])


def hidden_actions_and_isolation():
    seen = []

    class Spy:
        def decide(self, obs):
            seen.append(obs["players"][1 - obs["player"]]["gold"])
            obs["players"][0]["gold"] = 10 ** 9
            return [{"op": "buy_factory"}] * 5

    e = Engine(CFG, ("A", "B"))
    obs = [e.observation(0), e.observation(1)]
    subs, errs = collect_actions([Spy(), Spy()], obs)
    check("both bots see pre-action copies; mutation does not leak", seen == [100, 100] and e.players[0].gold == 100,
          f"opponent gold seen {seen}, engine gold {e.players[0].gold}")


def both_destroyed_draw_and_negative_hp():
    e = Engine(CFG, ("A", "B"))
    e.players[0].hp = 5
    e.players[1].hp = 5
    rec = e.play_round([[{"op": "buy_minion", "type": "tier1"}], [{"op": "buy_minion", "type": "tier3"}]])
    check("both bases destroyed in one round is a draw; HP may be negative",
          rec[0]["result"] == {"winner": None, "reason": "both_bases_destroyed"} and e.players[0].hp == -21,
          f"result {rec[0]['result']}, hp {e.players[0].hp}/{e.players[1].hp}")


def main():
    for fn in (gun_single_target, gun_overkill, splash_all_copies_eight_cells, splash_per_copy_independent_of_count,
               arrival_cutoff, income_and_lifetime, construction_check_order, blocking_rejected,
               hidden_actions_and_isolation, both_destroyed_draw_and_negative_hp):
        fn()
    failed = [n for n, ok in results if not ok]
    print(f"{len(results) - len(failed)}/{len(results)} reproductions passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
