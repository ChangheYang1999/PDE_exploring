#!/usr/bin/env python3
"""Independent exact algebra supporting result159; no producer code imported."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import hashlib,json,time,resource
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
start=time.monotonic();out=Path('research/weighted_transport_fibres/verification');counts={}
assert(out/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
def ck(b,g):
 counts[g]=counts.get(g,0)+1
 if not b:raise AssertionError(g)
def clean(a):return {k:v for k,v in a.items() if v}
def add(*aa):
 r={}
 for a in aa:
  for k,v in a.items():r[k]=r.get(k,F())+v
 return clean(r)
def scl(a,s):return clean({k:v*s for k,v in a.items()})
def mul(a,b):
 r={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():r[i+k,j+l]=r.get((i+k,j+l),F())+v*w
 return clean(r)
def derivative(a,axis):
 r={}
 for k,v in a.items():
  if k[axis]:
   kk=list(k);kk[axis]-=1;r[tuple(kk)]=v*k[axis]
 return clean(r)
def ev(a,x,y):return sum(v*x**i*y**j for (i,j),v in a.items())
def rpow(k):return {(2*j,2*(k-j)):F(comb(k,j)) for j in range(k+1)}
def fields(coeff):
 rho={};psi={}
 for k,v in enumerate(coeff):
  rho=add(rho,scl(mul({(0,1):F(1)},rpow(k)),v))
  psi=add(psi,scl(mul({(1,1):F(1)},rpow(k)),-v/F(2*k+4)))
 return rho,psi
for row in json.loads((out/'manifest.json').read_text())['files']:
 ck(hashlib.sha256(Path(row['frozen']).read_bytes()).hexdigest()==row['sha256'],'frozen_source_hash')
cases=[]
for trial in range(1,8):
 coeff=[F((-1)**(j+trial)*(trial+j+1),2*j+trial+1) for j in range(trial)]
 rho,psi=fields(coeff);px=derivative(psi,0);py=derivative(psi,1);rx=derivative(rho,0);ry=derivative(rho,1)
 ck(add(scl(derivative(px,0),-1),scl(derivative(py,1),-1))==rx,'Cartesian_Poisson_identity')
 Ux=scl(py,-1);Uy=px;ck(add(derivative(Ux,0),derivative(Uy,1))=={},'Cartesian_divergence_zero')
 ck(all(i%2==0 and j%2==1 for i,j in rho),'density_parity')
 ck(all(i%2==1 and j%2==1 for i,j in psi),'stream_parity')
 angular=add(scl(mul({(0,1):F(1)},rx),-1),mul({(1,0):F(1)},ry));ck(all(i>=1 for i,j in angular),'angular_x_factor')
 for ell in (F(3,2),F(5,2),F(3),F(7,2)):
  wx=add({(1,0):ell},Ux);wy=add({(0,1):ell},Uy);E=add(mul(wx,rx),mul(wy,ry),scl(rho,-1))
  ck(all(i%2==0 and j%2==1 for i,j in E),'residual_parity')
  for t in (F(1,7),F(2,3),F(3,2)):
   for cc,ss in ((F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(-8,17),F(15,17))):
    x,y=t*cc,t*ss;A=sum(v*t**(2*k+1) for k,v in enumerate(coeff));Ap=sum((2*k+1)*v*t**(2*k) for k,v in enumerate(coeff));I=sum(v*t**(2*k+4)/(2*k+4) for k,v in enumerate(coeff));B=-I/(2*t*t);Bp=I/t**3-A/2
    ur=ev(Ux,x,y)*cc+ev(Uy,x,y)*ss;ut=-ev(Ux,x,y)*ss+ev(Uy,x,y)*cc
    ck(ur==I/t**3*(cc*cc-ss*ss),'independent_radial_velocity')
    ck(ut==Bp*2*ss*cc,'independent_angular_velocity')
    polar=ss*(ell*t*Ap-A+A*Bp/t+(A*Bp-2*B*Ap)/t*(cc*cc-ss*ss))
    ck(polar==ev(E,x,y),'Cartesian_vs_polar_residual')
    ck(ev(psi,x,y)==B*2*ss*cc,'Cartesian_vs_radial_stream')
for ell in (F(11,10),F(3,2),F(5,2),F(3),F(7,2),F(9),F(12)):
 p=1/ell;a=4*(ell-1);b=a*(p-1)/2;rho,psi=fields([a,b]);rx=derivative(rho,0);ry=derivative(rho,1);ux=scl(derivative(psi,1),-1);uy=derivative(psi,0)
 E=add(mul(add({(1,0):ell},ux),rx),mul(add({(0,1):ell},uy),ry),scl(rho,-1))
 c=derivative(derivative(psi,0),1).get((0,0),F());ck(c==1-ell,'canonical_strain_from_Cartesian_stream');ck(E.get((0,1),F())==0,'linear_transport_cancel')
 cubic_sin3=(E.get((2,1),F())-E.get((0,3),F()))/4
 cubic_sin1=(E.get((2,1),F())+3*E.get((0,3),F()))/4
 ck(cubic_sin1==a*(p-1),'complete_cubic_sin1')
 ck(cubic_sin3==a*a*(p-1)/12!=0,'nonzero_cubic_sin3');ck(cubic_sin3==a*b/6,'radial_vs_Cartesian_cubic')
 cases.append(dict(ell=str(ell),p=str(p),a=str(a),b=str(b),c=str(c),residual_sin3_r3=str(cubic_sin3),residual_sin1_r3=str(cubic_sin1)))
 for beta in (F(1,10),F(1,2),F(1),F(7,3),F(4),F(21,2)):
  alow=-2-beta;ahigh=-2-beta*p
  ck(alow<ahigh<0,'nonempty_strip')
  for q in (F(1,10),F(1,2),F(9,10)):
   alpha=alow+q*(ahigh-alow);M_origin=alpha+beta+1;M_infty=alpha+beta*p+1;V_infty=alpha+beta*p+p
   ck(M_origin>-1 and M_infty<-1 and V_infty<-1,'absolute_integrability_exponents')
   ck(((2+alpha)*ell+beta)/(-alpha)<0,'weighted_identity_negative_ratio')
  ck((2+ahigh)*ell+beta==0,'endpoint_mass_coefficient_zero')
  ck(ahigh+beta+1>-1 and ahigh+beta*p+1==-1 and ahigh+beta*p+p==p-2<-1,'endpoint_exponents')
  # Polynomial antiderivative identity underlying the angular integration by parts.
  ck((beta+1)-(beta+2)*((beta+1)/(beta+2))==0,'angular_recurrence_algebra')
  ck(1-2*(beta+1)/(beta+2)==-beta/(beta+2),'angular_cos2_ratio')
for k in range(1,41):
 S=F(2*comb(2*k,k),4**k);Sn=F(2*comb(2*k+2,k+1),4**(k+1))
 ck(Sn==F(2*k+1,2*k+2)*S,'independent_even_beta_integral')
 ck(S-2*Sn==-F(k,k+1)*S,'independent_even_beta_cos2_integral')
# Direct compact monomial test of the chain rule before integration: Phi=r^(2i) rho^j.
rho,psi=fields([F(4),F(-2),F(1,3)]);ell=F(2);wx=add({(1,0):ell},scl(derivative(psi,1),-1));wy=add({(0,1):ell},derivative(psi,0));E=add(mul(wx,derivative(rho,0)),mul(wy,derivative(rho,1)),scl(rho,-1))
def powp(a,n):
 b={(0,0):F(1)}
 for _ in range(n):b=mul(b,a)
 return b
for i in range(1,4):
 for j in range(1,4):
  Phi=mul(rpow(i),powp(rho,j));div=add(derivative(mul(wx,Phi),0),derivative(mul(wy,Phi),1));rad=mul(scl(rpow(i-1),2*i),powp(rho,j));sder=mul(rpow(i),scl(powp(rho,j-1),j));rhs=add(scl(Phi,2*ell),mul(add(mul(wx,{(1,0):F(1)}),mul(wy,{(0,1):F(1)})),rad),mul(add(rho,E),sder))
  ck(div==rhs,'full_Cartesian_composite_chain_rule')
res=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=sum(counts.values()),counts=counts,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,proof_sha256=hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),center_cases=cases,scope='Finite exact identities support the standalone integral proof; polynomial test fields are local manufactures and are not claimed to satisfy sublinear growth')
(out/'EXACT_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
