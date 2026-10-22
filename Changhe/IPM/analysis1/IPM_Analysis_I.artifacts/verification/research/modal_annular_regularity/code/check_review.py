"""Exact independent check of the count and rate review corrections."""
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q,ctx
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/modal_annular_regularity';E=D/'evidence'
now=lambda:datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def manual(s):
 sign=-1 if s.startswith('-') else 1;s=s.lstrip('+-');a,b=s.split('p');x,y=a[2:].split('.')
 return Q(sign*int(x+y,16))*Q(2)**(int(b)-4*len(y))
p=B/'data_exact/modal_v2.json';x=json.loads(p.read_text());ar=x['arrays'];s=x['scalars_hex']
k=F.from_float(float.fromhex(s['k']));bo=F.from_float(float.fromhex(s['bo']));qk=manual(s['k']);qbo=manual(s['bo'])
assert Q(k.numerator,k.denominator)==qk and Q(bo.numerator,bo.denominator)==qbo
M,nb=ar['S']['shape'];assert (M,nb)==(260,1565) and len(ar['S']['hex'])==M*nb
T=[F.from_float(float.fromhex(t)) for t in ar['knots']['hex']];K=[manual(t) for t in ar['knots']['hex']]
assert len(T)==len(K)==1573 and len(set(T))-1==len(set(K))-1==1558
assert len(set(T))-2==len(set(K))-2==1557 and len(T)-x['degree']-1==nb
for n in range(1,262):
 m=2*n
 assert m-4+bo>m-2*k>=2-2*k>0
 assert Q(m-4)+qbo>Q(m)-2*qk>=2-2*qk>0
 assert m+k+1>0 and m-k-1>0 and Q(m)+qk+1>0 and Q(m)-qk-1>0
 assert -bo<k-3 and -qbo<qk-3
for j,l in x['outer_jl']:
 assert k-3-j*(1-k)-2*l<=k-3 and qk-3-j*(1-qk)-2*l<=qk-3
ck,cb=F(1,4),F(15,4);dk,db=Q(1,4),Q(15,4)
assert cb>4-2*ck and 2-4+cb<3-2*ck and db>4-2*dk and 2-4+db<3-2*dk
assert 2-4+bo>3-2*k and Q(-2)+qbo>3-2*qk # actual data satisfy stronger bound, generic inference does not
files={str(p.relative_to(B)):sha(p),str(Path(__file__).relative_to(B)):sha(__file__),str((D/'REVIEW_RESOLUTION.md').relative_to(B)):sha(D/'REVIEW_RESOLUTION.md')}
for n in ['checks.json','green_factor_checks.json']:
 z=json.loads((E/n).read_text())
 for a,h in z['files'].items():
  pp=Path(a);pp=pp if pp.is_absolute() else B/pp
  assert sha(pp)==h,a
 files[str((E/n).relative_to(B))]=sha(E/n)
out={'utc':now(),'status':'PASS_EXACT_REVIEW_CORRECTIONS','spline_coefficients_per_factor_mode':1565,'positive_spans':1558,'simple_interior_knots':1557,'all_modes_qualitative_rates':261,'outer_exponents':10,'generic_stronger_bound_counterexample':{'k':str(ck),'bo':str(cb),'m':2,'rate':str(2-4+cb),'rejected_lower_bound':str(3-2*ck)},'actual_data_satisfy_stronger_bound':True,'numerical_moment_input_used':False,'files':files}
with (E/'review_checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out),flush=True)
