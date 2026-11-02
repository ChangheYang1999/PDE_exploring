"""Like opt_search.py, for one pool and one seat: does behind_mode / robust_k change best_v9f's actions?
Usage (from hrt-project): BEST_MODULE=... PYTHONPATH=. python tmp/opt_search2.py POOL SEAT [MAX_ROUNDS]"""
import sys, time
sys.path.insert(0, "bot_research/tmp")
import test_best_v9f_V33C as T
from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.match import TimedBot, resolve_spec
from bot_research.experiments.lead import pools


def play(spec, opp, seat, max_rounds):
    specs = (spec, opp) if seat == 0 else (opp, spec)
    engine = Engine(balanced_config(), ("A", "B"))
    bots = [TimedBot(resolve_spec(s), None) for s in specs]
    acts = []
    while engine.result is None and engine.round < max_rounds:
        actions, errs = collect_actions(bots, [engine.observation(p) for p in (0, 1)])
        acts.append(actions[seat])
        engine.play_round(actions, errs)
    return engine, acts


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i + 1
    return None if len(a) == len(b) else min(len(a), len(b)) + 1


which, seat = sys.argv[1], int(sys.argv[2])
R = int(sys.argv[3]) if len(sys.argv) > 3 else 22
B = T.BEST
for opp in getattr(pools, which.upper()):
    t = time.time()
    a = play(B, opp, seat, R)
    b = play(B + "?behind_mode=null", opp, seat, R)
    c = play(B + "?behind_mode=null&robust_k=2", opp, seat, R)
    print(opp.split(":@make")[0].split(".")[-1], opp.split(":@make")[-1][:150], "| behind r", first_diff(a[1], b[1]),
          "robust r", first_diff(b[1], c[1]), "| rounds", len(a[1]), len(b[1]), len(c[1]),
          "| winner", a[0].result and a[0].result.get("winner"), f"| {time.time()-t:.0f}s", flush=True)
