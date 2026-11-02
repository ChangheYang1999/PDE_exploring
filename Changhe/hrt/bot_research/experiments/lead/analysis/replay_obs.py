"""Rebuild the observations of one player from a match log and feed them to a fresh bot (development only).

    PYTHONPATH=. .venv/bin/python -B tmp/replay_obs.py LOG PLAYER SPEC MAXROUND
Prints per round whether the bot's actions equal the logged ones, and the bot's rule-trace lists at the end.
"""
import json, sys
from collections import Counter
from td_game.config import balanced_config
from bot_research.harness.match import resolve_spec

log, me, spec, mx = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
recs = {}
for line in open(log):
    r = json.loads(line)
    recs[(r["round"], r["player"])] = r
rules = balanced_config().to_dict()
bot = resolve_spec(spec)
for rnd in range(1, mx + 1):
    obs = {"round": rnd, "player": me, "players": [recs[(rnd - 1, p)]["snapshot"] for p in (0, 1)], "rules": rules}
    acts = bot(obs)
    logged = [e["action"] for e in recs[(rnd, me)]["event"] if e["kind"] == "action"]
    same = json.dumps(acts, sort_keys=True) == json.dumps(logged, sort_keys=True)
    c = Counter(a.get("type", a["op"]) for a in acts)
    print(rnd, "same" if same else "DIFF", dict(c), "gold", obs["players"][me]["gold"], "hp", obs["players"][me]["hp"],
          obs["players"][1 - me]["hp"])
obj = getattr(bot, "__self__", bot)
for name in ("catch_rounds", "level_skips", "switch_round"):
    print(name, getattr(obj, name, None))
base = getattr(obj, "base", None)
for name in ("joint_rounds", "gun_rounds", "fortress", "failed"):
    print("base." + name, getattr(base, name, None))
