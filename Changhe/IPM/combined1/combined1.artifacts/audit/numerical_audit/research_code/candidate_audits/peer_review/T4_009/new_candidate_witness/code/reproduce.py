from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from math import comb
import json,hashlib,time,sys
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=1024
ROOT=Path(__file__).resolve().parents[1]
T=P([0,1]);U=P([1,-1]);Z=P([])
def q(x):
 f=Fraction(str(x));return Q(f.numerator,f.denominator)
def ar(x):return arb(x.numerator)/x.denominator
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(A,j,n,V):
 if n==0 or not V:return
 if n<0:n,V=-n,-V
 A[j,n]=A.get((j,n),Z)+V
 if not A[j,n]:del A[j,n]
def divide(V):
 assert V[0]==0 and V[1]==0
 return P(list(V)[2:])
def rad(V,p):return 2*p*T*V+2*T*U*V.derivative()
def td(V,a,k=1):return (k-2*a*T)*V+2*T*U*V.derivative()
def run(name):
 start=time.monotonic();folder=ROOT/'data'/name
 manifest=json.loads((folder/'MANIFEST.json').read_text())
 src=folder/manifest['coefficient_files'][0]['name'];d=json.loads(src.read_text())
 c=q(d.get('cl_exact',d.get('cl')));delta=1-1/c;pot={}
 for g in d['generators']:
  j,m=g['j'],g['m'];sp=g['spec'];coef=q(g['coef'])
  if sp[0]=='mono':V=T**(m+sp[1])
  else:
   assert sp[0]=='leg';w,n=sp[1:]
   V=T**(m+w)*P([(-1)**(n+k)*comb(n,k)*comb(n+k,k) for k in range(n+1)])
  pot[j,2*m]=pot.get((j,2*m),Z)+coef*V
 canpath=ROOT/'source'/f'{name}_canonical.json';can=json.loads(canpath.read_text())
 expected={(j,2*m,k):q(x) for (j,m,k),x in zip(can['order'],can['coefficients']) if q(x)}
 actual={(j,n,k):coef for (j,n),V in pot.items() for k,coef in enumerate(V) if coef}
 assert expected==actual
 rho={};stream={}
 for (j,n),V in pot.items():
  p=(3+1/c-j*delta)/2
  B=rad(rad(V,p),p)-n*n*V;E=rad(B,p)-2*B
  put(rho,j,n-1,(E+n*B)/2);put(rho,j,n+1,-(E-n*B)/2)
  plus=rad(V,p)-n*V;plus=rad(plus,p)-(n+2)*plus
  minus=rad(V,p)+n*V;minus=rad(minus,p)+(n-2)*minus
  put(stream,j,n+2,plus/4);put(stream,j,n-2,-minus/4)
 rho={key:divide(V) for key,V in rho.items()};stream={key:divide(V) for key,V in stream.items()}
 targetpath=ROOT/'source'/f'{name}_point.json';target=json.loads(targetpath.read_text())
 x,y=map(q,target['point']);r2=x*x+y*y;r=ar(r2).sqrt();t=r2/(1+r2);u=1/(1+r2)
 ct=ar(x)/r;st=ar(y)/r;sn=[arb(0),st];cn=[arb(1),ct]
 for n in range(2,max([key[1] for key in rho]+[key[1] for key in stream])+1):
  sn.append(sn[-1]*ct+cn[-1]*st);cn.append(cn[-1]*ct-sn[-2]*st)
 powers={j:ar(u)**ar((j+1)*delta/2) for j,n in pot}
 density=arb(0);rr=arb(0);rt=arb(0);ur=arb(0);ut=arb(0)
 for (j,n),V in rho.items():
  a=(j+1)*delta/2;value=ar(V(t));power=powers[j]
  density+=r*power*value*sn[n]
  rr+=power*ar(td(V,a)(t))*sn[n];rt+=power*n*value*cn[n]
 for (j,n),V in stream.items():
  a=(j+1)*delta/2;power=powers[j]
  ur-=r*power*n*ar(V(t))*cn[n];ut+=r*power*ar(td(V,a,2)(t))*sn[n]
 rx=ct*rr-st*rt;ry=st*rr+ct*rt;u1=ct*ur-st*ut;u2=st*ur+ct*ut
 vx=ar(c*x)+u1;vy=ar(c*y)+u2;F=vx*rx+vy*ry-density
 fields={'rho':density,'u1':u1,'u2':u2,'rho_x':rx,'rho_y':ry,'residual':F,'velocity_norm':(vx*vx+vy*vy).sqrt(),'gradient_norm':(rx*rx+ry*ry).sqrt()}
 overlaps={k:v.overlaps(arb(target['fields'][k])) for k,v in fields.items()};assert all(overlaps.values()),overlaps
 boxes=[('A2-Db',Q(1,2**18),ar(Q(1,2**16))),('FW-T-TB-rebal-v1',Q(1,2**16),ar(Q(3,2**15))),('FW-T-TB-sharp-v1',Q(1,2**13),ar(Q(43,50000))),('T4-019-no-H',Q(1,2**17),ar(Q(1,2**14))),('T4-graded-rational-box-1',Q(1,50000),(ar(Q(1,5000))**2+2*ar(Q(1,3000000))**2+ar(Q(1,50000000))**2).sqrt())]
 gaps=[];old={v['framework']:v for v in target['ball_exclusions']}
 for fw,sv,radius in boxes:
  s=ar(sv);C0=1/(4*arb.pi()*(1+s)).sqrt();C1=1/(8*arb.pi()*s*(1+s)).sqrt()
  A=C1*fields['velocity_norm']+C0*(1+fields['gradient_norm']);B=C0*C1
  upper=A*radius+B*radius**2;gap=abs(F)-upper;necessary=2*abs(F)/(A+(A*A+4*B*abs(F)).sqrt())
  assert gap>0
  if fw in old:
   for val,key in [(upper,'necessary_upper'),(gap,'gap'),(necessary,'necessary_H2s_radius_lower')]:assert val.overlaps(arb(old[fw][key])),(fw,key)
  gaps.append({'framework':fw,'s_exact':str(sv),'H2s_radius_upper':radius.str(80),'necessary_upper':upper.str(80),'gap':gap.str(80),'necessary_H2s_radius_lower':necessary.str(80),'N4_overlap':True if fw in old else 'new point-box combination'})
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'method':'Independent exact Rodrigues conversion and polar Laplacian/stream differentiation','point':list(map(str,[x,y])),'precision_bits':ctx.prec,'snapshot_sha256':sha(src),'canonical_sha256':sha(canpath),'canonical_coefficients_agree_exactly':True,'target_sha256':sha(targetpath),'code_sha256':sha(Path(__file__)),'fields':{k:v.str(100) for k,v in fields.items()},'field_overlaps':overlaps,'ball_exclusions':gaps,'elapsed_seconds':time.monotonic()-start}
 (ROOT/'verification'/f'{name}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(name,'F',F.str(30),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run(sys.argv[1])
