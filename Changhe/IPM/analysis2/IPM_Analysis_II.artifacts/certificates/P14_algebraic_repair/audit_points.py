"""Independent polar differentiation audit of Cartesian repair point values."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib
from flint import arb,ctx
HERE=Path(__file__).resolve().parent
ctx.prec=640
sys.set_int_max_str_digits(0)

def add(D,kind,n,l,v):
 if n<0:
  n=-n
  if kind=='s':v=-v
 if kind=='s' and n==0:return
 key=kind,n,l;D[key]=D.get(key,arb(0))+v

def derivative(D,p,k,d,axis):
 E={}
 for (kind,n,l),v in D.items():
  s=2*k-d+2*l;u=p-k-l
  if axis=='x':
   add(E,kind,n+1,l,v*(s-n)/2);add(E,kind,n-1,l,v*(s+n)/2)
   add(E,kind,n+1,l+1,v*u);add(E,kind,n-1,l+1,v*u)
  elif kind=='c':
   add(E,'s',n+1,l,v*(s-n)/2);add(E,'s',n-1,l,-v*(s+n)/2)
   add(E,'s',n+1,l+1,v*u);add(E,'s',n-1,l+1,-v*u)
  else:
   add(E,'c',n-1,l,v*(s+n)/2);add(E,'c',n+1,l,-v*(s-n)/2)
   add(E,'c',n-1,l+1,v*u);add(E,'c',n+1,l+1,-v*u)
 return E

def polynomials(d):
 c=arb(d['cl']);out={};gamma=1/c
 for nx,ny in [(0,3),(1,2),(2,1),(0,4),(1,3),(2,2),(3,1)]:
  polys={};degree=nx+ny
  for (j,m,k),v in zip(d['canonical_order'],d['canonical_coefficients']):
   p=(3+gamma-j*(1-gamma))/2
   T={('c',2*m,0):arb(v)}
   for di,axis in enumerate('x'*nx+'y'*ny):T=derivative(T,p,k,di,axis)
   for (kind,n,l),v in T.items():
    key=j,kind,n;co=polys.setdefault(key,{})
    co[k+l]=co.get(k+l,arb(0))+v
  out[nx,ny]=polys
 return out

def eval_fields(polys,c,x,y):
 r2=x*x+y*y;r=r2.sqrt();t=r2/(1+r2);gamma=1/c
 nmax=max(n for P in polys.values() for j,k,n in P)
 co=[arb(1),x/r];si=[arb(0),y/r]
 for n in range(2,nmax+1):co.append(2*co[1]*co[-1]-co[-2]);si.append(2*co[1]*si[-1]-si[-2])
 # Sparse powers permit very large K without constructing degree-K arrays.
 allpowers={q for P in polys.values() for C in P.values() for q in C};tp={q:t**q for q in allpowers}
 pref={j:(1+r2)**((3+gamma-j*(1-gamma))/2) for j in range(6)}
 chi={}
 for (nx,ny),P in polys.items():
  val=arb(0)
  for (j,kind,n),C in P.items():
   pp=sum((v*tp[k] for k,v in C.items()),arb(0))
   val+=pref[j]*pp*(co[n] if kind=='c' else si[n])
  chi[nx,ny]=val/r**(nx+ny)
 rho=-chi[2,1]-chi[0,3];rx=-chi[3,1]-chi[1,3];ry=-chi[2,2]-chi[0,4]
 ux=-chi[1,2];uy=chi[2,1];F=(c*x+ux)*rx+(c*y+uy)*ry-rho
 m11=2*c+1-2*chi[2,2]-chi[0,4];m22=2*c+1+chi[2,2];m12=chi[3,1]
 lm=(m11+m22-((m11-m22)**2+4*m12*m12).sqrt())/2
 return {'rho':rho,'rho_x':rx,'rho_y':ry,'u1':ux,'u2':uy,'F':F,'M_lambda_min':lm}

def run(name):
 start=time.monotonic();p=HERE/(name+'.json');pp=HERE/(name+'_points.json')
 d=json.loads(p.read_text());saved=json.loads(pp.read_text())
 assert saved['input_sha256']==hashlib.sha256(p.read_bytes()).hexdigest()
 polys=polynomials(d);c=arb(d['cl']);rows=[];badcoef=False;floor=arb(0)
 for row in saved['points']:
  x,y=map(arb,row['point']);new=eval_fields(polys,c,x,y)
  old={k:arb(v) for k,v in row['fields'].items()}
  assert all(v.is_finite() and old[k].is_finite() and v.overlaps(old[k]) for k,v in new.items())
  if new['M_lambda_min']<0:badcoef=True
  if abs(new['F'])>floor:floor=abs(new['F'])
  rows.append({'point':row['point'],'all_fields_agree':True,'F':new['F'].str(60),'M_lambda_min':new['M_lambda_min'].str(60)})
  print(name,row['point'],'PASS',flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','name':name,'canonical_sha256':d['canonical_sha256'],'points_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),'independent_method':'Polar derivative recurrence and sparse radial powers, compared to order-seven Cartesian jets.','precision_bits':ctx.prec,'points':rows,'has_negative_energy_matrix_eigenvalue':badcoef,'Ns_residual_lower_bound':str(floor.lower()),'seconds':time.monotonic()-start,'scope':'Individual point values, hence coefficient counterexamples and an N_s lower bound by the verified sup embedding. No upper norm or global coercivity claim.'}
 (HERE/(name+'_points_audit.json')).write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',name,'negativeM',badcoef,'Ns lower',floor.str(16),'seconds',out['seconds'],flush=True)
if __name__=='__main__':
 for name in sys.argv[1:] or ['algebraic_state131_k4','algebraic_n12_m10_k4','algebraic_state131_k16','algebraic_n12_m10_k16']:run(name)
