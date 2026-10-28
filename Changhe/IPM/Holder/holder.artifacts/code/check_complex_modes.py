"""Explicit Arb bounds and independent two-point diagnostics for complex modes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,random,math
import mpmath as mp
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
ctx.prec=192;mp.mp.dps=65

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ball(x):
 assert x.is_finite()
 return dict(lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()),display=x.str(50,more=True))
def floor(x):
 k=(Q(str(x))*10**10).__floor__();return f'{k//10**10}.{k%10**10:010d}'
def getq(a,n):
 if n==1:return arb(1)
 if n==2:return 2/(2-a).sqrt()*((1-a)/(2-a))**((1-a)/2)
 if n==3:return 6/(3-a)*(3*(1-a)/(4*(3-a)))**((1-a)/2)
 raise ValueError(n)

def main():
 table=json.loads((ROOT/'data/verified_table.json').read_text())['rows'];out=[]
 for row in table:
  aq=Q(row['alpha']);a=arb(str(aq));q2=getq(a,2);q3=getq(a,3)
  N=100;J=sum((arb(2)**(-a-k-1)/(a+k+1) for k in range(N)),arb(0))
  J+=arb(0).union(arb(2)**(-a-N)/(a+N+1))
  flower=(2**(-a)/a+J)/q2;cubic=(a+3)/(2*(1-a)*q3)
  b=[None,2**(a-1),2**(a-1)/q2,2**(a-1)/q3]
  cap=arb.min((b[3]+b[1])/2,2**a/arb.pi());B=2*b[3]/(1-a)+cap;s=(1-a)*B/(2*b[2]);F=2*b[2]*s**a/(a*(1-a))
  lower=max(Q(str(flower.lower().fmpq())),Q(str(cubic.lower().fmpq())))
  upperC=Q(row['selected_upper_C']['exact_safe_endpoint']);gap=lower-upperC
  out.append(dict(alpha=str(aq),Q2=ball(q2),Q3=ball(q3),J=ball(J),flower_lower=ball(flower),cubic_lower=ball(cubic),explicit_complex_upper=ball(F),safe_M_lower=floor(lower),safe_gap_over_C_upper=floor(gap),strict_separation=gap>0))
 rng=random.Random(20261028);tests=0;max_ratio=mp.mpf(0)
 for a in [mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf('0.75'),mp.mpf('0.9'),mp.mpf('0.99')]:
  for n in [1,2,3]:
   if n==1:q=mp.mpf(1)
   elif n==2:q=2/mp.sqrt(2-a)*((1-a)/(2-a))**((1-a)/2)
   else:q=6/(3-a)*(3*(1-a)/(4*(3-a)))**((1-a)/2)
   norm=2**(1-a)*q
   for j in range(120):
    x=mp.mpf(str(rng.uniform(0,25)));t=mp.mpf(str(rng.uniform(.0001,math.pi/2)))
    ratio=2**(1-a)*mp.sqrt((mp.sinh(a*x)**2+mp.sin(n*t)**2)/(mp.sinh(x)**2+mp.sin(t)**2)**a)
    assert ratio<=norm+mp.mpf('1e-60');max_ratio=max(max_ratio,ratio/norm);tests+=1
  for j in range(40):
   x=mp.mpf(str(rng.uniform(0,20)));u=mp.mpf(str(rng.random()))
   assert mp.sinh(a*x)**2+u**a<=(mp.sinh(x)**2+u)**a+mp.mpf('1e-55');tests+=1
 sources=[Path(__file__),ROOT/'16_beurling_complex_norm/exact_angular_modes/PROOF.md',ROOT/'16_beurling_complex_norm/compact_flower/PROOF.md',ROOT/'16_beurling_complex_norm/optimized_upper/PROOF.md',ROOT/'data/verified_table.json']
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=192,positive_series_terms=100,rows=out,diagnostic_pairs=tests,max_diagnostic_ratio=str(max_ratio),source_hashes={str(p.relative_to(ROOT)):sha(p) for p in sources})
 path=ROOT/'16_beurling_complex_norm/exact_angular_modes/verification/formula_checks.json';path.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps([{k:r[k] for k in ['alpha','safe_M_lower','safe_gap_over_C_upper','strict_separation']} for r in out],indent=2));print('Independent finite pair diagnostics:',tests)
if __name__=='__main__':main()
