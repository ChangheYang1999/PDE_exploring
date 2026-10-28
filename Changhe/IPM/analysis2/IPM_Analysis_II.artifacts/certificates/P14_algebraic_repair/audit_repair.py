"""Independent moment, Fourier derivative, residual and center audit.
No construction code is imported. Exact arithmetic uses FLINT rationals.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,hashlib,time,re
from flint import fmpq as Q,fmpq_poly,arb,ctx
ctx.prec=384
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]

def clean(a):return {m:v for m,v in a.items() if v}
def add(*terms):
 a={}
 for c,d in terms:
  for m,v in d.items():a[m]=a.get(m,Q(0))+c*v
 return clean(a)
def derivative(a,s,axis):
 out={}
 for m,v in a.items():
  out[m-1]=out.get(m-1,Q(0))+(s+m)*v/2
  out[m+1]=out.get(m+1,Q(0))+(s-m)*v/2*(1 if axis=='x' else -1)
 return clean(out)
def derivatives(a,s,axes):
 for axis in axes:a=derivative(a,s,axis);s-=1
 return a
def conv(a,b):
 if not a or not b:return {}
 la,lb=min(a),min(b);ha,hb=max(a),max(b)
 p=fmpq_poly([a.get(m,Q(0)) for m in range(la,ha+1)])
 q=fmpq_poly([b.get(m,Q(0)) for m in range(lb,hb+1)])
 z=p*q
 return {m+la+lb:z[m] for m in range(len(z)) if z[m]}
def cosine(a):
 out={}
 for m,v in a.items():
  if m:out[2*m]=v/2;out[-2*m]=v/2
  else:out[0]=v
 return clean(out)
def moments(A,c):
 out={}
 for (j,m,k),v in A.items():
  a=(3+1/c-j*(1-1/c))/2
  for q,b in [(0,Q(1)),(1,a-k)]:
   key=j,q;d=out.setdefault(key,{})
   d[m]=d.get(m,Q(0))+b*v
 return {k:clean(v) for k,v in out.items()}
def readbase(name):
 p=BASE/'source_audit/state131_exact.json' if name=='state131' else BASE/'08_refits/verification'/f'{name}_audit.json'
 d=json.loads(p.read_text());A={tuple(k):Q(v) for k,v in zip(d['canonical_order'],d['canonical_coefficients'])}
 return p,A

def audit_sectors(M,c):
 gamma=1/c;delta=1-gamma;rho={};psi={};vel={};grad={};out=[]
 for (j,q),a in M.items():
  H=cosine(a);s=3+gamma-j*delta-2*q
  rho[j,q]=add((-1,derivatives(H,s,'xxy')),(1,derivatives(H,s,'yyy')))
  psi[j,q]=derivatives(H,s,'xy')
  p=s-3
  vel[j,q]=(derivative(psi[j,q],p+1,'y'),derivative(psi[j,q],p+1,'x'))
  grad[j,q]=(derivative(rho[j,q],p,'x'),derivative(rho[j,q],p,'y'))
 for h,q in [(h,0) for h in range(7)]+[(0,1),(1,1)]:
  p=gamma-h*delta-2*q
  terms=[(c*p-1,rho.get((h,q),{}))]
  for i in range(6):
   j=h-1-i
   if not 0<=j<6:continue
   for u in range(q+1):
    v=q-u
    if (i,u) not in vel or (j,v) not in grad:continue
    ux,uy=vel[i,u];dx,dy=grad[j,v]
    terms.extend([(1,conv(ux,dx)),(-1,conv(uy,dy))])
  E=add(*terms)
  if h<6 or q:assert not E,(h,q)
  if E:
   # Real sine coefficient is -2 times the coefficient of i exp(i m theta).
   sq=sum((4*v*v for m,v in E.items() if m>0),Q(0))
   n=(arb.pi()*arb(str(sq))).sqrt()
  else:n=arb(0)
  out.append({'h':h,'q':q,'exponent':str(p),'zero':not bool(E),'full_angular_L2':n.str(50),'max_harmonic':max(E,default=0)})
  print('sector',h,q,'zero',not bool(E),'norm',n.str(16),flush=True)
 return out

def main():
 t=time.monotonic();tail=HERE.parents[1]/'10_tail_splice/verification/state131_splice.json';target=json.loads(tail.read_text())
 C={int(n)-1:{int(m)//2:Q(v) for m,v in x['cosine_coefficients'].items()} for n,x in target['homogeneous_potential_orders'].items()}
 rows=[];common=None;c=None
 for p in sorted(HERE.glob('algebraic_*_k*.json')):
  if not re.fullmatch(r'algebraic_.+_k[0-9]+',p.stem):continue
  d=json.loads(p.read_text());A={tuple(k):Q(v) for k,v in zip(d['canonical_order'],d['canonical_coefficients'])};c=Q(d['cl']);K=d['K']
  assert c==Q(target['c'])
  bp,B=readbase(d['base_name']);assert hashlib.sha256(bp.read_bytes()).hexdigest()==d['base_record_sha256']
  assert hashlib.sha256(tail.read_bytes()).hexdigest()==d['stationary_tail_record_sha256']
  serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(A.items()))+'\n'
  assert hashlib.sha256(serial.encode()).hexdigest()==d['canonical_sha256']
  diff=clean({k:A.get(k,Q(0))-B.get(k,Q(0)) for k in A.keys()|B.keys()})
  given={tuple(k):Q(v) for k,v in zip(d['additions_order'],d['additions_coefficients'])}
  assert diff==given and all(k>=m+K for j,m,k in diff)
  assert all(2*k>=2*K and k>=m for j,m,k in diff)
  M=moments(A,c)
  for j in range(6):
   assert M[j,0]==clean(C[j])
   if j<=1:assert not M[j,1]
  prim={k:v for k,v in M.items() if k[1]==0 or k[0]<=1}
  if common is None:common=prim
  else:assert prim==common
  rows.append({'name':d['name'],'canonical_sha256':d['canonical_sha256'],'exact_difference_checked':True,'leading_potential_orders':[1,2,3,4,5,6], 'vanishing_descendant_potential_branches':[0,1],'minimum_changed_potential_degree':min(2*k for j,m,k in diff),'unchanged_origin_density_slope_and_strain':2*K>4})
  print('moments, reconstruction and jets PASS',d['name'],flush=True)
 sectors=audit_sectors(common,c)
 result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','variants':rows,'independent_derivative_method':'Laurent Fourier coefficients, Cartesian x/y derivative shifts, polynomial convolution; imaginary phases retained explicitly','residual_sectors':sectors,'all_exponents_ge_minus2_vanish':True,'residual_big_O_exponent':str(1-7*(1-1/c)),'seconds':time.monotonic()-t,'scope':'Exact reference construction and residual-space membership. No residual-size or background-coefficient certificate.'}
 (HERE/'repair_audit.json').write_text(json.dumps(result,indent=2)+'\n')
 print('ALL CHECKS PASS seconds',result['seconds'],flush=True)
if __name__=='__main__':main()
