from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import json,time,importlib.util,sys
import numpy as np
from flint import fmpq as Q,fmpq_poly as P,arb,arb_poly,ctx
sys.set_int_max_str_digits(0);ctx.prec=768
start=time.monotonic();base=Path(__file__).resolve().parents[1]
helper=base.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('screen_fields',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
data=base/'data/candidate007_canonical.json'
c,delta,rho,stream=m.fields(json.loads(data.read_text()))
t=P([0,1]);v=P([1,-1])
def ar(x):return arb(x.numerator)/x.denominator
def prepare(source):
 ans=[]
 for (j,n),p in source.items():
  a=(j+1)*delta/2;polys=[]
  for k in range(4):
   polys.append(arb_poly([ar(x) for x in p]));p=-2*a*t*p+2*t*v*p.derivative()
  ans.append((j,n,polys))
 return ans
rr,ss=prepare(rho),prepare(stream)
print('prepared',len(rr),len(ss),'seconds',time.monotonic()-start,flush=True)
nmax=max(max(n for j,n in rho),max(n for j,n in stream));N=1024
assert 2*nmax<N//2
angles=np.arange(N)*2*np.pi/N
sines=np.sin(np.arange(nmax+1)[:,None]*angles)
cosines=np.cos(np.arange(nmax+1)[:,None]*angles)*np.arange(nmax+1)[:,None]
zn,zw=np.polynomial.legendre.leggauss(12)
edges=np.linspace(np.log(.001),np.log(100000.),25)
energy=np.zeros((2,N//2+1));cells=[]
for cell,(left,right) in enumerate(zip(edges[:-1],edges[1:])):
 for node,weight in zip(zn,zw):
  lr=(left+right)/2+(right-left)*node/2;r2=np.exp(2*lr)
  va=arb(1)/(1+arb(str(r2)));ta=1-va
  powers={j:va**ar((j+1)*delta/2) for j in range(8)}
  tables=[]
  for rows in [rr,ss]:
   out=np.zeros((4,nmax+1))
   for j,n,polys in rows:
    power=powers[j]
    for k,p in enumerate(polys):
     ball=power*p(ta)
     assert ball.is_finite()
     out[k,n]+=float(ball.mid())
   tables.append(out)
  aa,bb=tables;A=aa@sines;Ath=aa@cosines;B=bb@sines;Bth=bb@cosines
  G=[]
  for k in range(3):
   g=float(c)*(A[k]+A[k+1])-A[k]
   for l in range(k+1):g+=comb(k,l)*(-Bth[l]*(A[k-l]+A[k-l+1])+(2*B[l]+B[l+1])*Ath[k-l])
   G.append(-2*np.fft.rfft(g).imag/N)
  freq=np.arange(N//2+1)
  H=(1-freq**2)*G[0]+2*G[1]+G[2]
  ww=weight*(right-left)/2*np.pi
  for ia,a in enumerate([0,1]):energy[ia]+=ww*(1+r2)**(2-a)*H*H
 print('cell',cell,'seconds',time.monotonic()-start,flush=True)
result=[]
for ia,a in enumerate([0,1]):
 order=np.argsort(energy[ia])[::-1]
 rows=[{'mode':int(n),'norm_float':float(np.sqrt(energy[ia,n]))} for n in order[:30]]
 result.append({'a':a,'total_norm_float':float(np.sqrt(energy[ia].sum())),'ranking':rows})
 print('a',a,'total',np.sqrt(energy[ia].sum()),'top',rows[:12],flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'FLOAT screening only; no quadrature or exterior certification','input_sha256':sha256(data.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':sha256(helper.read_bytes()).hexdigest(),'seconds':time.monotonic()-start,'results':result}
p=base/'verification/mode_screen_float.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
