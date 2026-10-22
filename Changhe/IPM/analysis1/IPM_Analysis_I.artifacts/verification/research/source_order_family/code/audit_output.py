"""Fresh rational formulas and Arb1536 output audit; no primary imports."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,itertools,sys
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
ctx.prec=1536;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/source_order_family';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def Q(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def end(v):
 assert v.is_finite()
 def cv(z):m,e=z.man_exp();return F(int(m))*F(2)**int(e)
 return cv(v.lower()),cv(v.upper())
x=json.loads((E/'checks.json').read_text());assert x['status']=='PASS_SOURCE_ORDER_FAMILY_CONSTANTS'
for p,h in x['files'].items():assert sha(B/p)==h,p
assert sha(D/'PROOF.md')==json.loads((E/'proof_first.json').read_text())['proof_sha256']
cnt=0
for row in x['rows']:
 s=F(row['s']);C=F(2229,625)*s+F(28551,10000);ee=F(33,2000)*C;kap=F(1301,200)-F(101,100)*s;alo=kap-ee
 target={'coefficient':F(9,2)+12*s,'C_upper':C,'E_upper':ee,'a_lower':alo,'K_upper':1/alo,'d_lower':F(101,100)*s-F(1,100)}
 for name,v in target.items():assert F(row[name])==v;cnt+=1
 assert F(row['kappa'])==kap and 1/alo<F(row['K_decimal_ceiling'])
 # beta computed from beta^2; the primary used a reciprocal square root.
 beta=(Q(1)/(Q(4*(s-1)*(s-2))*arb.pi())).sqrt();bl,bu=end(beta)
 for eng,data in row['engines'].items():
  for name,z in data.items():
   l,u=F(z['lower_exact']),F(z['upper_exact']);assert l<=u
   if name=='beta_s':assert l<bl<=bu<u
   else:assert l<=target[name]<=u
   cnt+=1
# All continuum inequalities reduce to endpoints of the specified affine forms.
for s in [F(61,20),F(31,10)]:
 cap=F(1301,200)-F(101,100)*s
 assert cap>=F(1687,500)
 C=F(2229,625)*s+F(28551,10000)
 assert 0<F(33,2000)*C<cap/2
 for A,mu,g in itertools.product([10,F(51,5)],[F(99,100),F(101,100)],[29,30]):
  assert 1+(A+mu)/2-s*mu>=cap
  assert 1+(A+mu)/2-s*A+g>=cap+F(601,1000)
  cnt+=2
assert x['counts']=={'dependency_file_pins':387,'source_box_vertices_with_s':24,'affine_endpoint_vertices_sufficient':16,'extra_order_vertices':8,'directed_interval_inequalities':78}
files={str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',Path(__file__),E/'checks.json',E/'proof_first.json']}
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FRESH_SOURCE_ORDER_AUDIT','checks':cnt,'precision_bits':1536,'primary_files_pinned':len(x['files']),'scope':'Exact real s interval uses proved multiaffine and affine reductions, not sampling. Fresh rational formulas and full high-precision beta hull containment.','files':files}
(E/'output_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj))
