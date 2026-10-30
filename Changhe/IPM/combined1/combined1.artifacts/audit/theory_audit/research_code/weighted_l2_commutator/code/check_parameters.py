from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json,hashlib
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[1]
def A(x):
 x=Q(x);return arb(x.numerator)/x.denominator
p=ROOT.parent/'background_norm_reproduction/verification/reproduction.json'
z=json.loads(p.read_text())
v=next(v for v in z.values() if isinstance(v,dict) and 'D_rho_x' in v)
qx=A(v['D_rho_x']['rational_energy_over_pi_half'])
qy=A(v['D_rho_y']['rational_energy_over_pi_half'])
log2=arb(2).log()
kappa=(((log2-A(Q(1,2)))*qx+(3*log2-2)*qy)/32).sqrt()
c=A(Q(4076476460239181,2251799813685248));theta=A(Q(1,20))
beta0=c+1-theta-kappa
a=A(Q(221,200));d=A(Q(4,9));R=arb(2)**29
assert a>2/c and a<1+1/c and a+d<2
Md=d/2*((2-d)/d)**(1-d/2)
C=a*Md/arb(2).sqrt()*((2-a-d)**(-2)+(2+d)**(-2)).sqrt()
loss=(186*C+a*22*Md)*R**(-d)
beta=beta0-c*a-loss
riesz=(1+arb(2)**(abs(1-a)/2)*(2+a)/(2-a))/2
assert beta>arb(1)/50
D=arb(1)/250
rate=beta-a*D
contraction=riesz*D/rate
assert rate>0 and contraction<1
result={'date_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
 'a':'221/200','d':'4/9','R':'536870912','C_rho':'186','C_u':'22',
 'Md':str(Md),'velocity_commutator_constant':str(C),
 'unweighted_beta0':str(beta0),'dilation_penalty':str(c*a),'finite_radius_penalty':str(loss),
 'weighted_beta':str(beta),'weighted_Riesz_constant':str(riesz),
 'illustrative_gradient_bound':'1/250','rough_low_decay':str(rate),
 'conditional_low_contraction':str(contraction),
 'background_input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'scope':'Low weighted inverse only. The low energy margin uses independently reproduced exact state131 seminorms; team acceptance of this numeric input is pending the coordinator convention. The contraction display presupposes a compatible high inverse and complete normalized high ball, neither proved here.'}
(ROOT/'verification/parameters.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
