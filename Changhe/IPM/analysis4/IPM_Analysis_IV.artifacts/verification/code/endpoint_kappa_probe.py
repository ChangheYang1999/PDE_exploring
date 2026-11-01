"""Finite exact diagnostic for the missing endpoint bound."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import argparse, json, time
from flint import arb, fmpq, ctx
from rational_scan_audit import compute

ap = argparse.ArgumentParser()
ap.add_argument('--primes', default='7,11,13,17,19,23,29,31')
ap.add_argument('--seconds', type=float, default=450)
a = ap.parse_args()
root = Path('research/80_compatibility_size_criterion/verification/endpoint')
root.mkdir(exist_ok=True)
ctx.prec = 640
started = time.monotonic()
for profile, initial in [('sin1', {1:'1'}), ('sin3', {3:'1'}), ('three_modes', {1:'1',3:'1',5:'1'})]:
    for p in map(int,a.primes.split(',')):
        if time.monotonic()-started > a.seconds:
            print(json.dumps(dict(stopped=True,elapsed_s=time.monotonic()-started)),flush=True)
            raise SystemExit(0)
        out = root/f'{profile}_p{p}.json'
        if out.exists():
            continue
        r = compute(Fraction(4,p), initial, p)
        v = abs(arb(fmpq(r['kappa_exact'])))
        lg = v.log()/p if v > 0 else None
        r.update(profile=profile,checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                 log_abs_kappa_over_p=None if lg is None else lg.str(30,radius=True),
                 log_abs_kappa_over_p_log_p=None if lg is None else (lg/arb(p).log()).str(30,radius=True))
        out.write_text(json.dumps(r,indent=2)+'\n')
        print(json.dumps({k:r[k] for k in ['profile','n0','kappa_nonzero','log_abs_kappa_over_p','log_abs_kappa_over_p_log_p','elapsed_s']}),flush=True)
print(json.dumps(dict(complete=True,elapsed_s=time.monotonic()-started)),flush=True)
