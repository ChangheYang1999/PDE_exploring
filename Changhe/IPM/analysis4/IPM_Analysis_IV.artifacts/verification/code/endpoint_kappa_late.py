"""Further exact endpoint diagnostics, restricted to the sin(3 theta) profile."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import argparse, json, time, sys
sys.dont_write_bytecode = True
from flint import arb, fmpq, ctx
from rational_scan_audit import compute

ap=argparse.ArgumentParser()
ap.add_argument('--primes',default='37,41,43')
ap.add_argument('--seconds',type=float,default=420)
a=ap.parse_args()
root=Path('research/80_compatibility_size_criterion')
ctx.prec=640
started=time.monotonic()
source=Path(__file__).read_bytes()
(root/'sources/endpoint_kappa_late.py.txt').write_bytes(source)
for p in map(int,a.primes.split(',')):
    if time.monotonic()-started>a.seconds:
        print(json.dumps(dict(stopped=True,elapsed_s=time.monotonic()-started)),flush=True)
        break
    out=root/'verification/endpoint'/f'sin3_p{p}.json'
    if out.exists():
        continue
    r=compute(Fraction(4,p),{3:'1'},p)
    v=abs(arb(fmpq(r['kappa_exact'])))
    lg=v.log()/p if v>0 else None
    r.update(profile='sin3',checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
      source_sha256=sha256(source).hexdigest(),
      log_abs_kappa_over_p=None if lg is None else lg.str(35,radius=True),
      log_abs_kappa_over_p_log_p=None if lg is None else (lg/arb(p).log()).str(35,radius=True))
    out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ['profile','n0','kappa_nonzero','log_abs_kappa_over_p','log_abs_kappa_over_p_log_p','elapsed_s']}),flush=True)
print(json.dumps(dict(complete=True,elapsed_s=time.monotonic()-started)),flush=True)
