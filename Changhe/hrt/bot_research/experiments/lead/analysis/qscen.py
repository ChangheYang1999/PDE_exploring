"""Quick scenario games (development only): qscen.py OUTDIR CAND OPP SCEN [SCEN ...]; candidate in seat 0 and seat 1
(QSEATS=0 or QSEATS=1 in the environment: that seat only)."""
import sys, time, os
from bot_research.harness.match import play_match
out, cand, opp, scens = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
os.makedirs(out, exist_ok=True)
for s in scens:
    for seat in [int(x) for x in os.environ.get("QSEATS", "01")]:
        a, b = (cand, opp) if seat == 0 else (opp, cand)
        f = os.path.join(out, f"{s.replace(':','-')}_s{seat}_{int(time.time()*1000)%10**8}.jsonl")
        t = time.time()
        r = play_match(a, b, f, scenario=None if s == "none" else s)
        d = r["hp_diff_a"] * (1 if seat == 0 else -1)
        rej = [p["n_rejected"] for p in r["players"]]
        print(f"{s:12s} seat{seat} {d:+6d} r{r['rounds'] if 'rounds' in r else '?'} rej={rej} max={max(r['decide_max_seconds']):.2f}s {time.time()-t:.0f}s", flush=True)
