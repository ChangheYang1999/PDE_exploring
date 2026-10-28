"""Independent all-W2/W3 point comparisons for exact candidates."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import sys,json,hashlib,time
from flint import arb,ctx
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'11_residual_norms/verification'))
from audit_norms import direct_chi,aq
sys.path.insert(0,str(BASE/'13_algebraic_repair/verification'))
from audit_points import derivative
ctx.prec=768

def polar_polys(d):
 c=arb(d['cl']);out={};gamma=1/c
 for order in range(3,8):
  for nx in range(order):
   ny=order-nx;P={}
   for (j,m,k),v in zip(d['canonical_order'],d['canonical_coefficients']):
    p=(3+gamma-j*(1-gamma))/2;T={('c',2*m,0):arb(v)}
    for di,axis in enumerate('x'*nx+'y'*ny):T=derivative(T,p,k,di,axis)
    for (kind,n,l),v in T.items():
     block=P.setdefault((j,kind,n),{});block[k+l]=block.get(k+l,arb(0))+v
   out[nx,ny]=P
 return out

def eval_polar(P,c,x,y):
 r2=x*x+y*y;r=r2.sqrt();t=r2/(1+r2);gamma=1/c
 nmax=max(n for block in P.values() for j,kind,n in block)
 co=[arb(1),x/r];si=[arb(0),y/r]
 for n in range(2,nmax+1):co.append(2*co[1]*co[-1]-co[-2]);si.append(2*co[1]*si[-1]-si[-2])
 powers={k:t**k for block in P.values() for C in block.values() for k in C}
 pref={j:(1+r2)**((3+gamma-j*(1-gamma))/2) for j in range(6)}
 ch={}
 for (nx,ny),block in P.items():
  val=arb(0)
  for (j,kind,n),C in block.items():
   pol=sum((v*powers[k] for k,v in C.items()),arb(0))
   val+=pref[j]*pol*(co[n] if kind=='c' else si[n])
  ch[nx,ny]=val/r**(nx+ny)
 return ch

def fields(ch,c,x,y):
 rho=lambda i,j:-ch[i+2,j+1]-ch[i,j+3]
 u1=lambda i,j:-ch[i+1,j+2]
 u2=lambda i,j:ch[i+2,j+1]
 q2=x*x+y*y;rad=(1+q2).sqrt()
 T={}
 for k in range(1,5):T['rho'+str(k)]=sum((comb(k,i)*rho(i,k-i)**2 for i in range(k+1)),arb(0)).sqrt()
 for k in range(1,4):T['u'+str(k)]=sum((comb(k,i)*(u1(i,k-i)**2+u2(i,k-i)**2) for i in range(k+1)),arb(0)).sqrt()
 dx,dy=rho(1,0),rho(0,1);v1=c*x+u1(0,0);v2=c*y+u2(0,0)
 A=(dy,-dx/2,arb(0));S=(u1(1,0),(u1(0,1)+u2(1,0))/2,u2(0,1))
 eig=lambda a,b,d:(a+d-((a-d)**2+4*b*b).sqrt())/2
 M=eig(2*c+1+S[0]+A[0],S[1]+A[1],2*c+1+S[2]+A[2])
 out={'F':v1*dx+v2*dy-rho(0,0),'M_min':M}
 for k,z in [(1,-(v1*x+v2*y)/(5*(1+q2))),(2,16*(v1*x+v2*y)/(5*(1+4*q2)))]:
  a=1+c+z-k*(c+S[0])+A[0];b=-k*S[1]+A[1];d=1+c+z-k*(c+S[2])+A[2]
  out['M'+str(k)+'_min']=eig(a,b,d)
 out.update({'Du':T['u1'],'Drho':T['rho1'],'r1_D2u':rad*T['u2'],'r1_D3u':rad*T['u3'],'D2rho':T['rho2'],'r1_D2rho':rad*T['rho2'],'r2_D3rho':(1+q2)*T['rho3'],'r2_D4rho':(1+q2)*T['rho4']})
 out['N_point_bound']=abs(out['F'])/(16*(q2**(arb(1)/10) if q2>1 else 1))
 return out

def run(name):
 start=time.monotonic();p=BASE/'19_nb_candidates/verification'/(name+'.audit.json');raw=p.read_bytes();d=json.loads(raw);c=Q(d['cl']);A={tuple(k):Q(v) for k,v in zip(d['canonical_order'],d['canonical_coefficients'])}
 source=Path('numerics/data')/(name+'.json')
 assert hashlib.sha256(source.read_bytes()).hexdigest()==d['source_sha256']
 P=polar_polys(d);print('POLYNOMIALS',name,time.monotonic()-start,flush=True)
 bounds={'Du':Q(14,5),'Drho':Q(16),'r1_D2u':Q(3),'r1_D3u':Q(16),'D2rho':Q(3),'r1_D2rho':Q(8),'r2_D3rho':Q(32),'r2_D4rho':Q(512)}
 rows=[]
 for xs,ys in [('0','1/10'),('0','1/5'),('0','2/5'),('0','4/5'),('0','1'),('1','1'),('3','4'),('6','8')]:
  x,y=aq(xs),aq(ys);direct=direct_chi(A,c,x,y);polar=eval_polar(P,aq(c),x,y)
  assert all(v.is_finite() and direct[key].is_finite() and v.overlaps(direct[key]) for key,v in polar.items()),(name,xs,ys,'chi')
  one=fields(direct,aq(c),x,y);two=fields(polar,aq(c),x,y)
  assert all(v.is_finite() and two[key].is_finite() and v.overlaps(two[key]) for key,v in one.items()),(name,xs,ys,'fields')
  failures=[key for key,value in bounds.items() if one[key]>aq(value)]+[key for key in ['M1_min','M2_min'] if one[key]<arb(1)/2]
  rows.append({'point':[xs,ys],'all_derivatives_and_fields_overlap':True,'cartesian':{k:v.str(65) for k,v in one.items()},'polar':{k:v.str(65) for k,v in two.items()},'refuted_global_requirements':failures})
  print(name,xs,ys,'D2rho',one['D2rho'].str(16),'r2D4rho',one['r2_D4rho'].str(16),'M1',one['M1_min'].str(16),'M2',one['M2_min'].str(16),'FAIL',failures,flush=True)
 deps=[p,HERE.parent/'PROOF.md',BASE/'11_residual_norms/verification/audit_norms.py',BASE/'11_residual_norms/verification/compact_norms.py',BASE/'02_energy/verification/compact_matrix.py',BASE/'13_algebraic_repair/verification/audit_points.py',BASE/'18_fractional_constants/PROOF.md',BASE/'16_weighted_fractional/REFERENCE_AUDIT.md']
 out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED individual point values only','candidate':name,'precision_bits':ctx.prec,'source_sha256':d['source_sha256'],'canonical_sha256':d['canonical_sha256'],'point_count':len(rows),'points':rows,'refuted_requirements':sorted(set(k for row in rows for k in row['refuted_global_requirements'])),'dependencies':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
 (HERE/(name+'.json')).write_text(json.dumps(out,indent=2)+'\n');print('DONE',name,out['seconds'],flush=True)
if __name__=='__main__':
 for name in sys.argv[1:] or ['nb_stableA4_exact','nb_stableA5_exact','nb_Mpen_exact']:run(name)
