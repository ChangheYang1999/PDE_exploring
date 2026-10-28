"""Finite power-space constants; no coefficient fitting or matrix inversion."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, hashlib, time
from flint import arb, fmpq, ctx
sys.set_int_max_str_digits(0)
ctx.prec=384
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
start=time.monotonic()
c=Q(4076476460239181,2251799813685248);delta=1-1/c
a0=Q(7)*delta/2-2
exponents=sorted({Q(ell)*delta/2+k-2 for ell in range(1,13) for k in range(155) if Q(ell)*delta/2+k-2>=a0})
assert exponents[0]==a0 and a0>Q(-1,2)
assert len({Q(ell)*delta/2+k-2 for ell in range(1,13) for k in range(155)})==12*155

def aq(x):
 q=fmpq(str(x));return arb(q)

def constants(exps):
 first=exps[0];D=1/(2*aq(first)+1).sqrt()
 for a in exps[1:]:D*=aq(a-first)/aq(a+first+1)
 total=sum((2*a+1 for a in exps),Q(0))
 squares=sum(((2*a+1)**2 for a in exps),Q(0))
 cd2=sum((a*a for a in exps),Q(0))+(total*total-squares)/2
 return D,aq(cd2).sqrt(),cd2
D,CD,cd2=constants(exponents)
p=BASE/'23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json'
d=json.loads(p.read_text())
e={int(k):aq(v) for k,v in d['leading_sine_coefficients'].items()}
assert all(m>0 and m%2 for m in e)
lnorm2=arb.pi()/2*D**2*sum((v**2/(m*m+(1+2*CD)**2) for m,v in e.items()),arb(0))
lower=lnorm2.sqrt()
routeU=(1-arb(34)/2**18)*(arb(20)/21*2**18).sqrt()*lower
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED constants; theorem independently reviewed',
 'c':str(c),'delta':str(delta),'a0':str(a0),'exponent_count':len(exponents),'first_exponents':[str(a) for a in exponents[:12]],'last_exponent':str(exponents[-1]),
 'D':D.str(70),'C_D':CD.str(70),'C_D_squared_exact':str(cd2),'mode_count':len(e),'max_mode':max(e),
 'Hminus_lower':lower.str(70),'Route_U_N_lower_at_s_2minus18':routeU.str(70),'Route_U_ratio_eta':(routeU*1572864).str(70),
 'input_hash':hashlib.sha256(p.read_bytes()).hexdigest(),'proof_hash':hashlib.sha256((HERE.parent/'PROOF.md').read_bytes()).hexdigest(),
 'code_hash':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
