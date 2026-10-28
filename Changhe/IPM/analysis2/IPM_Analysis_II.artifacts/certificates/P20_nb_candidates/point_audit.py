"""Two-method point audit for the exactly projected N-B reference."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,sys,hashlib,time
from flint import arb,ctx
sys.set_int_max_str_digits(0)
ctx.prec=768
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'11_residual_norms/verification'))
from audit_norms import direct_chi,aq
sys.path.insert(0,str(BASE/'13_algebraic_repair/verification'))
from audit_points import polynomials,eval_fields
ctx.prec=768

def direct(A,c,x,y):
 ch=direct_chi(A,c,x,y);rho=-ch[2,1]-ch[0,3];rx=-ch[3,1]-ch[1,3];ry=-ch[2,2]-ch[0,4]
 ux=-ch[1,2];uy=ch[2,1];F=(aq(c)*x+ux)*rx+(aq(c)*y+uy)*ry-rho
 aa=2*aq(c)+1-2*ch[2,2]-ch[0,4];bb=2*aq(c)+1+ch[2,2];ab=ch[3,1]
 lm=(aa+bb-((aa-bb)**2+4*ab*ab).sqrt())/2
 return {'rho':rho,'rho_x':rx,'rho_y':ry,'u1':ux,'u2':uy,'F':F,'M_lambda_min':lm}

def run(name):
 start=time.monotonic();p=HERE/(name+'.audit.json');raw=p.read_bytes();d=json.loads(raw);c=Q(d['cl'])
 A={tuple(k):Q(v) for k,v in zip(d['canonical_order'],d['canonical_coefficients'])}
 P=polynomials(d);rows=[];bad=False
 for xs,ys in [('0','1/10'),('0','1'),('1','1'),('0','2'),('3','4'),('6','8'),('30','40'),('60','80')]:
  x,y=aq(xs),aq(ys);one=direct(A,c,x,y);two=eval_fields(P,aq(c),x,y)
  assert all(a.is_finite() and two[k].is_finite() and a.overlaps(two[k]) for k,a in one.items())
  if one['M_lambda_min']<arb(19)/5:bad=True
  row={'point':[xs,ys],'independent_overlap_all_fields':True,'cartesian':{k:v.str(60) for k,v in one.items()},'polar':{k:v.str(60) for k,v in two.items()},'violates_required_M':one['M_lambda_min']<arb(19)/5}
  rows.append(row);print(xs,ys,'F',one['F'].str(20),'M',one['M_lambda_min'].str(20),flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED individual points only','candidate':name,'input_sha256':hashlib.sha256(raw).hexdigest(),'canonical_sha256':d['canonical_sha256'],'precision_bits':ctx.prec,'independent_methods':['Cartesian Taylor jets through order7','polar differentiated finite radial polynomials'],'points':rows,'required_global_M_refuted':bad,'seconds':time.monotonic()-start,'dependencies':{str(v.relative_to(BASE)):hashlib.sha256(v.read_bytes()).hexdigest() for v in [BASE/'11_residual_norms/verification/audit_norms.py',BASE/'11_residual_norms/verification/compact_norms.py',BASE/'02_energy/verification/compact_matrix.py',BASE/'13_algebraic_repair/verification/audit_points.py',HERE.parent/'PROOF.md'] if v.exists()},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (HERE/(name+'.points.json')).write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',out['seconds'],flush=True)
if __name__=='__main__':
 for name in sys.argv[1:] or ['nb_stableA2_exact']:run(name)
