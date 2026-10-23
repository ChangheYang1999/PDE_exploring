"""Independent Gaussian whole-plane targets and positive compact quadrature."""
import json,hashlib,time,math
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp
from compact_norm_quadrature import nodes,radius_and_jacobian
from polar_derivative_norms import norm_integrand
out=Path('research/compact_derivative_quadrature/verification/manufactured.json')
rec=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',rows=[],node_checks=[])
def save():out.write_text(json.dumps(rec,indent=2)+'\n')
def polyder(p):return [j*p[j] for j in range(1,len(p))]
def nextpoly(p):
    out=[0]*(len(p)+1)
    for j,v in enumerate(polyder(p)):out[j+1]+=2*v
    for j,v in enumerate(p):out[j+1]-=2*v
    return out
def polyeval(p,x):
    val=mp.mpf(0)
    for c in p[::-1]:val=val*x+c
    return val
save()
try:
 with mp.workdps(60):
  polys={}
  for name,start in [('g',[1]),('h',[8,-4])]:
   ps=[start]
   for k in range(6):ps.append(nextpoly(ps[-1]))
   polys[name]=ps
  for order in [64,128,192]:
   ns,meta=nodes(order,50);rec['node_checks'].append(meta);save()
   for L,kappa in [(mp.mpf(1),mp.mpf(3)/2),(mp.mpf(2),mp.mpf(7)/3)]:
    totals={name:{k:mp.mpf(0) for k in range(2,7)} for name in polys}
    for s,w in ns:
     r,jac=radius_and_jacobian(s,L,kappa);x=r*r;factor=mp.exp(-x)
     for name,ps in polys.items():
      d={1:[polyeval(p,x)*factor/math.factorial(j) for j,p in enumerate(ps)]}
      for k in range(2,7):totals[name][k]+=w*jac*norm_integrand(d,r,k)
    for name in polys:
     for k in range(2,7):
      exact=mp.pi*mp.power(2,k-3 if name=='g' else k-1)*math.factorial(k+1 if name=='g' else k+3)
      error=abs(totals[name][k]/exact-1)
      rec['rows'].append(dict(order=order,L=mp.nstr(L,10),kappa=mp.nstr(kappa,20),field=name,k=k,relative_error=mp.nstr(error,35),computed=mp.nstr(totals[name][k],45),exact=mp.nstr(exact,45)))
    save();print(json.dumps(dict(order=order,L=str(L),kappa=str(kappa),rows=len(rec['rows']))),flush=True)
  for row in rec['rows']:
   if row['order']==192:assert mp.mpf(row['relative_error'])<mp.mpf('1e-10'),row
 rec['status']='PASS'
except BaseException as e:
 rec['status']='FAIL';rec['exception']=repr(e);save();raise
finally:
 rec['code_sha256']=hashlib.sha256(Path('independent_code/compact_norm_quadrature.py').read_bytes()).hexdigest()
 rec['norm_code_sha256']=hashlib.sha256(Path('independent_code/polar_derivative_norms.py').read_bytes()).hexdigest()
 rec['proof_sha256']=hashlib.sha256(Path('research/compact_derivative_quadrature/PROOF.md').read_bytes()).hexdigest()
 rec['test_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();rec['finished_utc']=datetime.now(timezone.utc).isoformat();save()
print(json.dumps(dict(status=rec['status'],rows=len(rec['rows']),finished_utc=rec['finished_utc'])),flush=True)
