from __future__ import annotations

import argparse
import json

from td_game.logs import ReplayLog, load_log


def summarize(log: ReplayLog) -> dict:
    final = log.frames[-1]
    players = []
    for p in (0, 1):
        snap = final.records[p]["snapshot"]
        totals = {"base_damage": 0, "damage_dealt": 0, "outgoing_hits": 0, "rejected_actions": 0,
                  "income_path": 0, "income_factories": 0, "income_hits": 0}
        for frame in log.frames:
            for event in frame.records[p]["event"]:
                if event["kind"] == "combat":
                    for key in ("base_damage", "damage_dealt", "outgoing_hits"):
                        totals[key] += event.get(key, 0)
                elif event["kind"] == "income":
                    for key in ("path", "factories", "hits"):
                        totals[f"income_{key}"] += event.get(key, 0)
                elif event["kind"] == "action" and event.get("accepted") is False:
                    totals["rejected_actions"] += 1
        result = log.result
        outcome = "unfinished" if result is None else ("draw" if result["winner"] is None else "win" if result["winner"] == p else "loss")
        players.append({"player": p, "name": snap["name"], "outcome": outcome,
                        "hp": snap["hp"], "gold": snap["gold"], **totals})
    return {"rounds": final.round, "result": log.result, "players": players}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Minimal match summary from JSONL snapshots and events")
    parser.add_argument("log")
    parser.add_argument("--json", action="store_true", help="machine-readable summary on stdout")
    args = parser.parse_args(argv)
    try:
        summary = summarize(load_log(args.log))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"td_stats: {exc}\n")
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        players = summary["players"]
        print(f"{players[0]['name']} vs {players[1]['name']}: {summary['rounds']} rounds")
        for p in players:
            print(f"P{p['player']}: {p['outcome']}; HP {p['hp']}, gold {p['gold']}; hits {p['outgoing_hits']}, rejected {p['rejected_actions']}")
        print(f"Reason: {summary['result']['reason'] if summary['result'] else 'unfinished log'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
