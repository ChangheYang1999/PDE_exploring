"""Directed constants for the elementary short-window fit comparison."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import dyadic
ROOT=Path('research/219_local_fit_ambiguity')
ctx.prec=1024
h=arb(11)/359
B=(arb(557)/1000)*h*h/(2*arb(10).log()*(1-h)**2)
assert B<arb(1)/8000
p=Path('research/215_shifted_multiplier_growth/verification/drift_fit_checks.json')
r=json.loads(p.read_text())
v=r['fits']['F']['logarithmic']['slope_ball']
beta=arb(dyadic(v[0],v[1]),dyadic(v[2],v[3]))
assert abs(beta)<arb(557)/1000
tangent_c1=-359*beta/arb(10).log()
print(json.dumps(dict(bound=B.str(40,radius=True),tangent_c1=tangent_c1.str(40,radius=True))))
# The bound holds for any beta in the stated exact rational interval.
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),status='PASS',n0=359,h='11/359',absolute_beta_bound='557/1000',uniform_log10_bound=B.str(40,radius=True),bound_below_one_over_8000=True,verified_beta=beta.str(40,radius=True),tangent_inverse_coefficient=tangent_c1.str(40,radius=True),fit_reference=dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest()))
(ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'sources/local_fit_ambiguity.py').write_bytes(Path(__file__).read_bytes())
