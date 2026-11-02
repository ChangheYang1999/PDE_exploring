"""Quick seat-0 games on the unchanged engine (development only, no logs):

    PYTHONPATH=. .venv/bin/python -B -m bot_research.experiments.lead.quick_games CAND_SPEC OPP_SPEC [OPP_SPEC ...]

prints W/D/L from the engine winner, the HP difference, the last round and the wall time per game."""
import sys, time
from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.match import resolve_spec

def play(a, b):
    engine = Engine(balanced_config(), ("A", "B"))
    bots = [type("B", (), {"decide": staticmethod(resolve_spec(s))})() for s in (a, b)]
    while engine.result is None:
        obs = [engine.observation(p) for p in (0, 1)]
        actions, errs = collect_actions(bots, obs)
        engine.play_round(actions, errs)
    hp = [engine.observation(0)["players"][p]["hp"] for p in (0, 1)]
    return engine.result["winner"], hp[0] - hp[1], engine.round

cand = sys.argv[1]
for opp in sys.argv[2:]:
    t = time.time()
    w, d, r = play(cand, opp)
    print(f"{'WDL'[0 if w == 0 else (2 if w == 1 else 1)]} {d:+5d} r{r:2d} {time.time()-t:5.1f}s  {opp.split('.')[-1]}", flush=True)
