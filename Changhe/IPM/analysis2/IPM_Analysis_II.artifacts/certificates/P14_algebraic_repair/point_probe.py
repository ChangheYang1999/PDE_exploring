"""Certified point values for exact repairs. No claim between sample points."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import sys,json,hashlib,time
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'11_residual_norms/verification'))
from audit_norms import direct_chi,aq
ctx.prec=640
sys.set_int_max_str_digits(0)

def run(name):
 p=HERE/(name+'.json');d=json.loads(p.read_text());c=Q(d['cl'])
 A={tuple(k):Q(v) for k,v in zip(d['canonical_order'],d['canonical_coefficients'])}
 rows=[];start=time.monotonic()
 for x,y in [('0','1/10'),('1','1'),('0','2'),('3','4'),('6','8'),('30','40'),('60','80'),('300','400')]:
  xx,yy=aq(x),aq(y);chi=direct_chi(A,c,xx,yy)
  rho=-chi[2,1]-chi[0,3];rx=-chi[3,1]-chi[1,3];ry=-chi[2,2]-chi[0,4]
  ux=-chi[1,2];uy=chi[2,1];F=(aq(c)*xx+ux)*rx+(aq(c)*yy+uy)*ry-rho
  m11=2*aq(c)+1-2*chi[2,2]-chi[0,4];m22=2*aq(c)+1+chi[2,2];m12=chi[3,1]
  lm=(m11+m22-((m11-m22)**2+4*m12*m12).sqrt())/2
  vals={'rho':rho,'rho_x':rx,'rho_y':ry,'u1':ux,'u2':uy,'F':F,'M_lambda_min':lm}
  assert all(v.is_finite() for v in vals.values())
  rows.append({'point':[x,y],'fields':{k:v.str(60) for k,v in vals.items()}})
  print(name,x,y,'F',F.str(14),'Mmin',lm.str(14),flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'points':rows,'seconds':time.monotonic()-start,'scope':'Certified individual point enclosures only; independent evaluator check pending. No whole-plane coefficient certificate or residual norm.'}
 (HERE/(name+'_points.json')).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
 for n in sys.argv[1:] or ['algebraic_state131_k4','algebraic_n12_m10_k4','algebraic_state131_k16','algebraic_n12_m10_k16']:run(n)
