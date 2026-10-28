"""Finite interval proof of the central complex-versus-real separation."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from flint import arb,ctx
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'16_beurling_complex_norm/strict_separation/verification'
ctx.prec=192;N=80

def ball(x):
 assert x.is_finite();return dict(lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()))
def I(a,p):
 e=a+2+2*p;c=arb(1);total=arb(0)
 for k in range(N):
  total+=c*2**(-e-2*k)/(e+2*k);c*=arb(2*k+1)/(2*k+2)
 tail=arb(4)/3*2**(-e-2*N)/(e+2*N)
 return total+arb(0).union(tail)
def gaps(a):
 a2=2**(1+a/2)/(arb.pi()*(a+2));a3=3*2**a/arb.pi()*(3*I(a,0)-4*I(a,1));b=2**(a+1)/(3*arb.pi())
 s=(2*a3+(1-a)*b)/(2*a2)
 if not s>0:return None
 U=2*a2*s**a/(a*(1-a))
 q2=2/(2-a).sqrt()*((1-a)/(2-a))**((1-a)/2)
 q3=6/(3-a)*(3*(1-a)/(4*(3-a)))**((1-a)/2)
 J=sum((2**(-a-k-1)/(a+k+1) for k in range(N)),arb(0))
 Lg=(2**(-a)/a+J)/q2+2**a*a*arb.pi()/(q3*(arb.pi()*a).sin())
 Lc=(a+3)/(2*(1-a)*q3)
 return a*(1-a)*(Lg-U),a*(1-a)*(Lc-U)
def main():
 pending=[(Q(1,10),Q(9,10),0)];leaves=[];checked=0
 while pending:
  lo,hi,depth=pending.pop();a=arb(str(lo)).union(arb(str(hi)));g=gaps(a);checked+=1
  if g is not None and (g[0]>0 or g[1]>0):
   choice=0 if g[0]>0 else 1
   leaves.append(dict(lo=str(lo),hi=str(hi),glued_gap=ball(g[0]),cubic_gap=ball(g[1]),selected=['glued','cubic'][choice],depth=depth));continue
  assert depth<18,('uncertified',lo,hi,g)
  mid=(lo+hi)/2;pending.extend([(mid,hi,depth+1),(lo,mid,depth+1)])
 leaves.sort(key=lambda d:Q(d['lo']));cursor=Q(1,10)
 for d in leaves:assert Q(d['lo'])==cursor;cursor=Q(d['hi'])
 assert cursor==Q(9,10) and checked==2*len(leaves)-1
 paths=[Path(__file__),OUT.parent/'PROOF.md',ROOT/'16_beurling_complex_norm/glued_witness/PROOF.md',ROOT/'16_beurling_complex_norm/exact_angular_modes/PROOF.md',ROOT/'02_upper_bounds/PROOF.md']
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,series_terms=N,checked=checked,leaf_count=len(leaves),leaves=leaves,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},verdict='central cover positive; independent audit required')
 (OUT/'central_cover.json').write_text(json.dumps(result,indent=2)+'\n');print('Checked',checked,'leaves',len(leaves),'depth',max(d['depth'] for d in leaves))
if __name__=='__main__':main()
