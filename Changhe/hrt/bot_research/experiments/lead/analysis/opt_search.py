"""Search for short scenarios in which behind_mode, robust_k and the passive rule change best_v9f's actions.
Usage (from hrt-project): BEST_MODULE=... python -B -m bot_research.tmp.opt_search  (or PYTHONPATH=. python tmp/opt_search.py)"""
import sys, time
sys.path.insert(0, "bot_research/tmp")
import test_best_v9f_V33C as T
from bot_research.experiments.lead import pools

B = T.BEST
fac = lambda acts: sum(1 for r in acts for x in r if x["op"] == "buy_factory")
mins = lambda acts, k: sum(1 for r in acts[k:] for x in r if x["op"] == "buy_minion")


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i + 1
    return None


print("passive rule", flush=True)
for name, opp in (("GROWER", T.GROWER), ("GUARDED", T.GUARDED)):
    v = {}
    for tag, q in (("best", ""), ("pu_null", "?passive_until=null"),
                   ("pure_passive", "?passive_cheap_from=null&passive_mid_from=null")):
        v[tag] = T.play(B + q, opp, max_rounds=6)[3]
    print(name, {k: fac(a) for k, a in v.items()}, "diff best/pu_null r", first_diff(v["best"], v["pu_null"]),
          "pure/pu_null r", first_diff(v["pure_passive"], v["pu_null"]), flush=True)

which = sys.argv[1] if len(sys.argv) > 1 else "handoff"
opps = pools.POOLS[which] if hasattr(pools, "POOLS") else getattr(pools, which.upper())
for opp in opps:
    t = time.time()
    R = 22
    a = T.play(B, opp, max_rounds=R)
    b = T.play(B + "?behind_mode=null", opp, max_rounds=R)
    c = T.play(B + "?behind_mode=null&robust_k=2", opp, max_rounds=R)
    print(opp.split(":@make?")[-1][:120], "| behind r", first_diff(a[3], b[3]), "robust r", first_diff(b[3], c[3]),
          "| minions after r10 a/b/c", mins(a[3], 10), mins(b[3], 10), mins(c[3], 10),
          "| rounds", len(a[3]), len(b[3]), len(c[3]), "| result", a[0].result and a[0].result.get("winner"),
          f"| {time.time()-t:.0f}s", flush=True)
