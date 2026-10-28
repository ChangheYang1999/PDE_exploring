"""Arb evaluation and independent point-pair checks for the glued witness."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,math,cmath,random
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'16_beurling_complex_norm/glued_witness/verification'
ctx.prec=192

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ball(x):
 assert x.is_finite()
 return dict(lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()),display=x.str(50,more=True))
def floor(x):
 n=(x*10**10).__floor__();return f'{n//10**10}.{n%10**10:010d}'
def evaluate(a):
 q2=2/(2-a).sqrt()*((1-a)/(2-a))**((1-a)/2)
 q3=6/(3-a)*(3*(1-a)/(4*(3-a)))**((1-a)/2)
 J=sum((arb(2)**(-a-k-1)/(a+k+1) for k in range(100)),arb(0))
 J+=arb(0).union(arb(2)**(-a-100)/(a+101))
 flower=(2**(-a)/a+J)/q2
 exterior=2**a*a*arb.pi()/(q3*(arb.pi()*a).sin())
 cubic=(a+3)/(2*(1-a)*q3)
 return q2,q3,flower,exterior,cubic

def diagnostic():
 rng=random.Random(3102812);rows=[]
 for a in [.001,.01,.1,.3,.4,.5,.75,.9,.99]:
  q2=2/math.sqrt(2-a)*((1-a)/(2-a))**((1-a)/2)
  q3=6/(3-a)*(3*(1-a)/(4*(3-a)))**((1-a)/2)
  b2=2**(a-1)/q2;b3=2**(a-1)/q3
  def flower(z):
   r=abs(z);tau=max(0,min(r,.5-r))
   return b2*tau**a*cmath.exp(-2j*cmath.phase(z)) if tau else 0j
  def f(z):
   r=abs(z)
   return flower(z-.5)-flower(z+.5)+(b3*(r-1)**a*cmath.exp(-3j*cmath.phase(z)) if r>1 else 0j)
  pts=[0j,.5+0j,-.5+0j,1+0j,-1+0j]
  for j in range(200):
   if j%3==0:z=.5+math.exp(rng.uniform(-15,math.log(.5)))*cmath.exp(2j*math.pi*rng.random())
   elif j%3==1:z=-.5+math.exp(rng.uniform(-15,math.log(.5)))*cmath.exp(2j*math.pi*rng.random())
   else:z=(1+math.exp(rng.uniform(-15,8)))*cmath.exp(2j*math.pi*rng.random())
   pts.append(z)
  worst=0;count=0
  for _ in range(800):
   z,w=rng.sample(pts,2);ratio=abs(f(z)-f(w))/abs(z-w)**a
   assert ratio<=1+2e-12,(a,z,w,ratio)
   worst=max(worst,ratio);count+=1
  # Opposite sides of the tangency to the exterior support.
  for k in range(2,14):
   e=10.**(-k);z=1-e;w=1+e
   ratio=abs(f(z)-f(w))/abs(z-w)**a
   assert ratio<=1+2e-12
   worst=max(worst,ratio);count+=1
  rows.append(dict(alpha=a,checked_pairs=count,max_ratio=worst))
 return rows

def main():
 table=json.loads((OUT/'accepted_C_snapshot.json').read_text())['rows'];rows=[]
 for row in table:
  alpha=Q(row['alpha']);a=arb(str(alpha));q2,q3,flower,exterior,cubic=evaluate(a)
  glued=flower+exterior;lower=max(Q(str(glued.lower().fmpq())),Q(str(cubic.lower().fmpq())))
  C=Q(row['selected_upper_C']['exact_safe_endpoint'])
  rows.append(dict(alpha=str(alpha),Q2=ball(q2),Q3=ball(q3),flower=ball(flower),exterior=ball(exterior),glued=ball(glued),cubic=ball(cubic),safe_M_lower=floor(lower),safe_gap_over_C=floor(lower-C),strict=lower>C))
 checks=diagnostic()
 paths=[Path(__file__),OUT/'accepted_C_snapshot.json',OUT.parent/'PROOF.md',ROOT/'16_beurling_complex_norm/exact_angular_modes/PROOF.md',ROOT/'16_beurling_complex_norm/compact_flower/PROOF.md']
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=192,J_terms=100,rows=rows,pair_diagnostics=checks,source_hashes={str(p.relative_to(ROOT)):sha(p) for p in paths})
 (OUT/'formula_checks.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps([{k:r[k] for k in ['alpha','safe_M_lower','safe_gap_over_C','strict']} for r in rows],indent=2));print('Pairs:',sum(r['checked_pairs'] for r in checks))
if __name__=='__main__':main()
