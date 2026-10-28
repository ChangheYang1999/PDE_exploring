from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from flint import arb, ctx
import json
ctx.prec=384
base=Path(__file__).resolve().parents[2]
def A(q):
    q=Q(q); return arb(q.numerator)/arb(q.denominator)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'), 'states':{}}
for state in (88,131):
 p=json.loads((base/'source_audit'/f'state{state:03d}_exact.json').read_text())['exact_parameters']
 lam=A(p['lambda_origin']); sigma=A(p['sigma']); a=A(p['a0']); d=lam-1
 assert lam>arb(5)/2 and lam<3 and sigma>lam+2
 vals={
  'lambda_minus_two':lam-2,
  'lambda_minus_five_halves':lam-arb(5)/2,
  'sigma_minus_lambda_minus_two':sigma-lam-2,
  'sup_norm_F0_coefficient':1/(2*arb.pi()*lam),
  'gradient_F1_coefficient':1/(2*arb.pi()*(lam-1)),
  'Hessian_F2_coefficient':1/(2*arb.pi()*(lam-2)),
  'Hessian_Holder_half_F2_5_coefficient':arb(2).sqrt()/(2*arb.pi()*(lam-arb(5)/2)),
  'strain_from_forcing_yjet_coefficient':1/a,
  'Gaussian_derivative_lower_constant_K': (1/(40*arb.pi()))*((arb(221)/100)**(-sigma/2))*(-arb(221)/400).exp()*(1-arb(1).cos())*(1-(arb(11)/10)**(-d))/d,
 }
 assert vals['Gaussian_derivative_lower_constant_K']>0
 out['states'][str(state)]={k:v.str(60) for k,v in vals.items()}
 print(state,{k:float(v.mid()) for k,v in vals.items()})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
