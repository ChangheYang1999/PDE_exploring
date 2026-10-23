"""Exact supporting checks for result99. No numerical profile claim."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
start=time.perf_counter();checks=[]
def clean(p):return {key:v for key,v in p.items()if v}
def add(*ps):
 out={}
 for p in ps:
  for key,v in p.items():out[key]=out.get(key,F(0))+v
 return clean(out)
def scale(p,c):return clean({key:v*c for key,v in p.items()})
def mul(p,q):
 out={}
 for(i,j),v in p.items():
  for(k,l),w in q.items():out[i+k,j+l]=out.get((i+k,j+l),F(0))+v*w
 return clean(out)
def d(p,axis):
 out={}
 for(i,j),v in p.items():
  ex=(i,j)[axis]
  if ex:out[i-(axis==0),j-(axis==1)]=ex*v
 return out
def lap(p):return add(d(d(p,0),0),d(d(p,1),1))
def record(name,passed):
 checks.append(dict(name=name,passed=bool(passed)));assert passed,name

def sine_laurent(poly):
 # Evaluate x=(z+z^-1)/2, y=(z-z^-1)/(2i). Odd-y polynomials
 # have imaginary Laurent coefficients; store coefficient divided by i.
 out={}
 for(i,j),v in poly.items():
  assert j%2==1
  factor=F((-1)**((j+1)//2),2**(i+j))*v
  for h in range(i+1):
   for k in range(j+1):
    power=i+j-2*h-2*k
    out[power]=out.get(power,F(0))+factor*comb(i,h)*comb(j,k)*(-1)**k
 return {k:-2*v for k,v in out.items()if k>0 and v}

for n in range(2,13):
 base={(2*n,1):F(1)};phi=d(base,0);rho=scale(lap(base),-1)
 record(f'core_density_n{n}',rho=={(2*n-2,1):F(-2*n*(2*n-1))})
 record(f'core_stream_n{n}',phi=={(2*n-1,1):F(2*n)})
 spectrum=sine_laurent(phi)
 record(f'highest_stream_sine_n{n}',spectrum[2*n]==n*F(2)**(2-2*n))
 record(f'moment_coefficient_n{n}',4*n*spectrum[2*n]==n*n*F(2)**(4-2*n))
 record(f'no_core_source_frequency_n{n}',2*n not in sine_laurent(d(rho,0)))
 record(f'unchanged_slope_n{n}',d(rho,1).get((0,0),F(0))==0)
 record(f'unchanged_strain_n{n}',d(d(phi,0),1).get((0,0),F(0))==0)
 for k in range(1,15):
  # Harmonic center coefficient must have its own radial degree.
  value=spectrum.get(2*k,F(0))if k==n else F(0)
  record(f'selected_moment_n{n}_k{k}',value==(n*F(2)**(2-2*n)if k==n else 0))
 for cut in [[1],[1,-3,2],[2,0,-4,7]]:
  poly={}
  for h,c in enumerate(cut):
   for j in range(h+1):poly[2*j,2*(h-j)]=F(c*comb(h,j))
  pot=mul(base,poly);psi=d(pot,0);sig=scale(lap(pot),-1)
  record(f'commutation_n{n}_cut{cut}',scale(lap(psi),-1)==d(sig,0))
  u1=scale(d(psi,1),-1);u2=d(psi,0)
  record(f'divergence_n{n}_cut{cut}',not add(d(u1,0),d(u2,1)))
  record(f'curl_n{n}_cut{cut}',add(d(u2,0),scale(d(u1,1),-1))==scale(d(sig,0),-1))

for h in range(1,41):
 ell=1+F(h,7);D=ell-1;a=4*D;A=2*ell-1
 r0={(0,1):a,(2,1):-a,(0,3):-a}
 p0={(1,1):-D,(3,1):a/6,(1,3):a/6}
 perturb_r={(2,1):F(-12)};perturb_p={(3,1):F(4)}
 def residual(rho,psi):
  u1=scale(d(psi,1),-1);u2=d(psi,0)
  out=add(mul(add({(1,0):ell},u1),d(rho,0)),mul(add({(0,1):ell},u2),d(rho,1)),scale(rho,-1))
  return {key:v for key,v in out.items()if sum(key)<=3}
 base=residual(r0,p0);new=residual(add(r0,perturb_r),add(p0,perturb_p));diff=add(new,scale(base,-1))
 record(f'residual_change_ell{ell}',diff=={(2,1):F(-24)})
 record(f'background_not_profile_ell{ell}',base[(2,1)]==-2*a*ell)
 record(f'T1_change_ell{ell}',-(a-2*A)*F(-12)==-24)
 record(f'T2_change_ell{ell}',4-(a-4*A)*F(-12)/(3*a)==-4/D)

out=dict(utc=datetime.now(timezone.utc).isoformat(),verdict='PASS',count=len(checks),seconds=time.perf_counter()-start,checks=checks,scope='Exact polynomial differential identities, core jets, Laurent Fourier coefficients and normalized residual changes. Compact support and norm estimates are proved in PROOF.md, not inferred from these algebra tests.')
paths=['independent_code/check_compact_moment_concentration.py','research/compact_canonical_moment_concentration/PROOF.md'];out['sha256']={p:hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in paths}
Path('research/compact_canonical_moment_concentration/verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='checks'}))
