"""Lead request (06:08Z): kappa_{p,a} = a_{p, a/2-2} (first-resonance compatibility coefficient) for f_1 = sin(theta), delta = a/p,
primes 67 <= p <= pmax, all even a with a/p in (0.25, 0.75), in ball arithmetic (256 bits): log10|kappa| with radius.
Time-budgeted; results appended per case to notes/kappa_scan_arb.jsonl. usage: kappa_scan_arb.py pmin pmax budget_seconds"""
import sys, os, json, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
from flint import fmpq, arb
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pmin, pmax, budget = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]); t0 = time.time()
out = open(os.path.join(LANE, 'notes', 'kappa_scan_arb.jsonl'), 'a')
primes = [p for p in range(pmin, pmax + 1) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
R = RingArb(256)
for p in primes:
    stats = []
    for a in range(4, p, 2):
        if not (0.25 < a / p < 0.75): continue
        if time.time() - t0 > budget: print('budget exhausted at p =', p, 'a =', a); sys.exit(0)
        delta = fmpq(a, p); cl = 1 / (1 - delta); j0 = a // 2 - 1
        ff = FarField(R, cl, [R.scalar(1)])
        try:
            while max(ff.f) < p: ff.step()
        except ArithmeticError as e:
            print('ERR', p, a, e); continue
        kap = ff.f[p][j0 - 1] if j0 - 1 < len(ff.f[p]) else R.zero
        res = ff.stats[p].get('resonances')
        lk = R.log10abs(kap); lr = float((kap.rad().log() / arb(10).log()).str(10, radius=False)) if kap.rad() != 0 else -float('inf')
        rec = {'p': p, 'a': a, 'delta': a / p, 'j0': j0, 'log10_abs_kappa': lk, 'log10_radius': lr, 'certified_nonzero': bool(not kap.contains(0)), 'status': res[0]['status'] if res else None, 'time': time.time() - t0}
        out.write(json.dumps(rec) + '\n'); out.flush(); stats.append(lk / p)
        print(f"p={p} a={a} log10|kappa|={lk:.4f} (radius 1e{lr:.0f}) log10|kappa|/p={lk/p:.4f} status={rec['status']}", flush=True)
    if stats: print(f"== p={p}: mean log10|kappa|/p = {sum(stats)/len(stats):.4f}, min = {min(stats):.4f}, cases {len(stats)}", flush=True)
