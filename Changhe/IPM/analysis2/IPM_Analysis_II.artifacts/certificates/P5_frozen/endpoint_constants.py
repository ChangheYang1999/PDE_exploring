"""Exact parameter and Arb checks for the frozen endpoint theorem."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
ctx.prec=512

def a(x):
 x=Q(x);return arb(x.numerator)/x.denominator

rows=[]
for state in (88,131):
 p=BASE/'source_audit'/f'state{state:03d}_exact.json';raw=p.read_bytes();dct=json.loads(raw)
 ex=dct['exact_parameters'];lam=Q(ex['lambda_origin']);dd=lam-1;sig=Q(ex['sigma']);aa=Q(ex['a0'])
 assert sig*dd==aa and 2<lam<3 and sig>=5 and 4*lam-10>0
 l,d,s=a(lam),a(dd),a(sig);pi=arb.pi()
 I=pi.sqrt()*((s-1)/2).gamma()/(s/2).gamma()
 J1=pi/(2*(1+d).gamma()*(pi*d/2).sin())
 J2=(1-d).gamma()*(pi*d/2).cos()/d
 assert J1.is_finite() and J1>0 and J2.is_finite() and J1.overlaps(J2)
 C=2**d*I*(2+d/2).gamma()/((1+d).gamma()*(pi*d/2).sin())
 Cdirect=I/(8*pi)*2**(d+4)*(2+d/2).gamma()*J2
 assert C.overlaps(Cdirect) and C>0
 endpoint=16/(3-l)+6*pi.sqrt()/(l-2)
 gap=4*l-10
 moment=endpoint/(l*(l-1))*(2*pi/gap)**a(Q(1,4))
 row={'state':state,'source_sha256':hashlib.sha256(raw).hexdigest(),'lambda':str(lam),'sigma':str(sig),
      'endpoint_holder_exponent':str(lam-2),'p4_moment_gap':str(4*lam-10),
      'constants':{'I_sigma':I.str(70),'cosine_integral':J1.str(70),'center_Holder_coefficient':C.str(70),'center_density_coefficient':(C/l).str(70),'Gaussian_endpoint_D2_upper':endpoint.str(70),'Gaussian_p4_kappa12_unit_disk_moment_upper':moment.str(70)},
      'independent_gamma_forms_overlap':True}
 rows.append(row);print(state,json.dumps(row['constants'],indent=2),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','precision_bits':ctx.prec,'rows':rows,'scope':'Constants for the proved complete frozen operator and Gaussian forcing; not a variable-coefficient inverse estimate.'}
(HERE/'endpoint_constants.json').write_text(json.dumps(out,indent=2)+'\n')
