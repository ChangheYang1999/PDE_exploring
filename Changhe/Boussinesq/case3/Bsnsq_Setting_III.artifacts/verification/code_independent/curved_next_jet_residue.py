"""P306 exact Laurent coefficient, own symbolic polynomial arithmetic."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json,time,hashlib
start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();s,k,C,H=S.symbols('s k C H',nonzero=True)
# Compute only coefficients capable of affecting the residue.
J=sum((-1)**j*S.binomial(j+2,2)*k**j*s**(j+4)/(j+4)for j in range(8))
P=S.expand((10+4*k*s)*(1+k*s)**4)
Icurv=sum(12*k/C*P.coeff(s,j)*s**(j-11)/(j-11)for j in range(6))
I_H=-S.Rational(36,5)*H/C*s**-5-4*k*H/C*s**-4
# D contribution uses only the curvature and homogeneous eta terms of I.
Dres=-C*C*S.residue(s**3*(Icurv+I_H)/(1+k*s)**3,s,0)
# 6k eta' part: the rational second term has zero residue by degree.
linear_eta=-6*k*C*S.expand((6+2*k*s)*(1+k*s)**4*J).coeff(s,11)
# 2 eta eta' part, computed without discarding its particular terms.
prod=S.expand(2*(6+2*k*s)*(H-C*J)**2)
product_eta=prod.coeff(s,5)-2*C*S.residue((H-C*J)/(s*s*(1+k*s)**2),s,0)
quadratic=S.factor(Dres+linear_eta+product_eta)
a=-C*k/260;correction=1092*a*H;total=S.factor(quadratic+correction)
v=Path('research/306_curved_endpoint_next_jet/verification')
r=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,D_residue=str(S.factor(Dres)),linear_eta_residue=str(S.factor(linear_eta)),product_eta_residue=str(S.factor(product_eta)),quadratic_residue=str(quadratic),degree13_correction=str(correction),total_residue=str(total),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(v/'symbolic_residue.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
