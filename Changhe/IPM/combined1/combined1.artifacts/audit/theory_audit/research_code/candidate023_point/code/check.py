from pathlib import Path
from functools import lru_cache
from math import comb
from hashlib import sha256
from datetime import datetime,timezone
import json,time,sys
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1]
def sha(p):return sha256(p.read_bytes()).hexdigest()
def ar(x):return arb(x.numerator)/x.denominator
def add(x,y):return [x[k]+y[k] for k in range(5)]
def mul(x,y,n=5):return [sum((x[j]*y[k-j] for j in range(k+1) if j<len(x) and k-j<len(y)),Q(0)) for k in range(n)]
def scale(x,a):return [a*v for v in x]
@lru_cache(None)
def affine(a,b,e):
 a,b=Q(a),Q(b);out=[];cc=Q(1)
 for k in range(5):
  if k:cc*=Q(e-k+1,k)
  out.append(a**e*cc*(b/a)**k)
 return out
start=time.monotonic();ctx.prec=1024
src=B/'data/candidate023.json';ref=B/'source/N4_result.json'
assert sha(src)=='d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df'
data=json.loads(src.read_text());peer=json.loads(ref.read_text());assert peer['generator_sha256']==sha(src)
c=Q(data.get('cl_exact',data.get('cl')));delta=1-1/c
x,y=map(Q,peer['point']);r2=x*x+y*y;t=r2/(1+r2);u=1-t
@lru_cache(None)
def generator(m,spec):
 kind=spec[0]
 if kind=='mono':return affine(str(t),'1',m+spec[1])
 if kind=='leg':w,n=spec[1:];Qd=0;R=1
 else:assert kind=='legqs';w,n,Qd,R=spec[1:]
 D=Q(R*R)*u+t;out=[Q(0)]*5
 for k in range(n+1):
  v=affine(str(t),'1',m+w+k)
  if Qd:v=mul(v,affine(str(u),'-1',Qd))
  if R!=1:v=mul(v,affine(str(D),str(1-R*R),-w-Qd-k))
  out=add(out,scale(v,Q((-1)**(n+k)*comb(n,k)*comb(n+k,k)*R**(2*Qd))))
 return out
pot={}
for g in data['generators']:
 key=g['j'],g['m'];coef=Q(g['coef']);v=generator(g['m'],tuple(g['spec']))
 pot[key]=add(pot.get(key,[Q(0)]*5),scale(v,coef))
radial={}
for (j,m),v in pot.items():
 p=(3+1/c-j*delta)/2;rel=[];cc=Q(1)
 for k in range(5):
  if k:cc*=(-p-k+1)/k
  rel.append(cc*(-1/u)**k)
 f=mul(v,rel);vals=[]
 for k in range(5):
  vals.append(f[0])
  if k<4:f=mul([Q(i)*f[i] for i in range(1,len(f))],[2*t*u,2*(1-2*t),Q(-2)],len(f)-1)
 radial[j,m]=[ar(u)**ar(-p)*ar(v) for v in vals]
r=ar(r2).sqrt();C=ar(x)/r;S=ar(y)/r;C2=C*C-S*S
cs=[arb(1),C];ss=[arb(0),S]
for n in range(2,2*max(m for j,m in pot)+1):
 cs.append(cs[-1]*C-ss[-1]*S);ss.append(ss[-1]*C+cs[-2]*S)
rho=arb(0);dr=arb(0);dt=arb(0);ur=arb(0);ut=arb(0)
for (j,m),f in radial.items():
 n=2*m;sn,cn=ss[n],cs[n];b=f[2]-n*n*f[0];b1=f[3]-n*n*f[1];b2=f[4]-n*n*f[2]
 A=b1-2*b;BB=b2-5*b1+6*b
 rho-=r**(-3)*(S*A*cn-n*C*b*sn)
 dr-=r**(-3)*(S*BB*cn-n*C*(b1-3*b)*sn)
 dt-=r**(-3)*(C*(A-n*n*b)*cn+n*S*(b-A)*sn)
 E=f[2]-2*f[1]+n*n*f[0];H=f[1]-f[0]
 E2=f[3]-4*f[2]+(n*n+4)*f[1]-2*n*n*f[0];H2=f[2]-3*f[1]+2*f[0]
 ur-=r**(-3)*(C2*(E-n*n*H)*cn+n*S*C*(-E+4*H)*sn)
 ut+=r**(-3)*(S*C*E2*cn-n*C2*H2*sn)
rx=(C*dr-S*dt)/r;ry=(S*dr+C*dt)/r;u1=C*ur-S*ut;u2=S*ur+C*ut
vx=ar(c*x)+u1;vy=ar(c*y)+u2;F=vx*rx+vy*ry-rho
fields={'rho':rho,'u1':u1,'u2':u2,'rho_x':rx,'rho_y':ry,'residual':F,'velocity_norm':(vx*vx+vy*vy).sqrt(),'gradient_norm':(rx*rx+ry*ry).sqrt()}
comparisons={k:bool(v.overlaps(arb(peer['fields'][k]))) for k,v in fields.items()};assert all(comparisons.values()),comparisons
b0=ar(Q(50,651))/(arb(28248)*4*arb.pi()).sqrt();b1=ar(Q(25,217))/(8*arb.pi()).sqrt()
upper=b1*fields['velocity_norm']+b0*(1+fields['gradient_norm'])+b0*b1;gap=abs(F)-upper
assert gap>0 and upper.overlaps(arb(peer['uniform_graded_upper'])) and gap.overlaps(arb(peer['uniform_graded_gap']))
rows=[]
for old in peer['ball_exclusions']:
 s=Q(old['s']);rad=ar(Q(old['radius_squared'])).sqrt() if 'radius_squared' in old else ar(Q(old['radius']));C0=1/(4*arb.pi()*ar(1+s)).sqrt();C1=1/(8*arb.pi()*ar(s*(1+s))).sqrt()
 bound=rad*(C1*fields['velocity_norm']+C0*(1+fields['gradient_norm']))+C0*C1*rad**2
 gg=abs(F)-bound;assert gg>0 and bound.overlaps(arb(old['upper'])) and gg.overlaps(arb(old['gap']))
 root=2*abs(F)/(C1*fields['velocity_norm']+C0*(1+fields['gradient_norm'])+((C1*fields['velocity_norm']+C0*(1+fields['gradient_norm']))**2+4*C0*C1*abs(F)).sqrt())
 if 'necessary_H2s_radius_lower' in old:assert root.overlaps(arb(old['necessary_H2s_radius_lower']))
 rows.append({'framework':old['framework'],'s':str(s),'radius':old.get('radius'),'radius_squared':old.get('radius_squared'),'necessary_H2s_radius_lower':root.str(100),'upper':bound.str(100),'gap':gg.str(100),'peer_overlap':True})
theta=(fields['gradient_norm']-ry)/2;theta_gap=theta-ar(c-1)
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'candidate':peer['candidate'],'point':list(map(str,[x,y])),'c_exact':str(c),'inputs':{str(p.relative_to(B)):sha(p) for p in [src,ref,Path(__file__),B/'PROOF.md']},'fields':{k:v.str(100) for k,v in fields.items()},'field_overlaps':comparisons,'theta':theta.str(100),'theta_minus_c_minus_one':theta_gap.str(100),'uniform_graded_upper':upper.str(100),'uniform_graded_gap':gap.str(100),'ball_exclusions':rows,'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED independent polar point and necessary tests'}
p=B/'verification/results.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('F',F.str(40),'graded gap',gap.str(40),'seconds',out['elapsed_seconds'],flush=True)
