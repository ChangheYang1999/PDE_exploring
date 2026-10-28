"""Independent positive-series replay of the finite separation cover."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from flint import arb,ctx
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];FOLDER=ROOT/'16_beurling_complex_norm/strict_separation/verification'
ctx.prec=256;N=100

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def record(v):
 assert v.is_finite();return dict(lower=str(v.lower().fmpq()),upper=str(v.upper().fmpq()))
def a3_direct(a):
 # Expand the combined positive integrand, not a difference of integrals.
 c=arb(1);s=arb(0)
 for k in range(N):
  e=a+2+2*k
  s+=c*arb(4)**(-k-1)*2*(a+5+2*k)/(e*(e+2))
  c*=arb(2*k+1)/(2*k+2)
 result=3*s/arb.pi()
 tail=3*arb(4)**(-N)/(arb.pi()*(a+2+2*N))
 return result+arb(0).union(tail)
def independent_gap(a,branch):
 A=2**(1+a/2)/(arb.pi()*(a+2));B=2*a3_direct(a)+(1-a)*2**(a+1)/(3*arb.pi())
 U=(2*A)**(1-a)*B**a/(a*(1-a))
 q3=6/(3-a)*(3*(1-a)/(4*(3-a)))**((1-a)/2)
 if branch=='cubic':L=(a+3)/(2*(1-a)*q3)
 else:
  assert branch=='glued'
  q2=2/(2-a).sqrt()*((1-a)/(2-a))**((1-a)/2)
  J=sum((2**(-a-k-1)/(a+k+1) for k in range(N)),arb(0))
  L=(2**(-a)/a+J)/q2+2**a*a*arb.pi()/(q3*(arb.pi()*a).sin())
 return a*(1-a)*(L-U)
def main():
 path=FOLDER/'central_cover.json';cert=json.loads(path.read_text())
 for p,h in cert['source_hashes'].items():assert sha(ROOT/p)==h
 leaves=cert['leaves'];assert cert['leaf_count']==len(leaves) and cert['checked']==2*len(leaves)-1
 cursor=Q(1,10);audited=[];minimum=None
 for row in leaves:
  lo,hi=Q(row['lo']),Q(row['hi']);assert lo==cursor and lo<hi;cursor=hi
  stored=row[row['selected']+'_gap'];assert Q(stored['lower'])>0 and Q(stored['upper'])>=Q(stored['lower'])
  v=independent_gap(arb(str(lo)).union(arb(str(hi))),row['selected'])
  assert v.is_finite() and v>0,(lo,hi,v)
  lower=Q(str(v.lower().fmpq()));minimum=lower if minimum is None else min(minimum,lower)
  audited.append(dict(lo=str(lo),hi=str(hi),selected=row['selected'],independent_gap=record(v)))
 assert cursor==Q(9,10)
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=256,positive_series_terms=N,leaf_count=len(leaves),minimum_scaled_central_margin=str(minimum),leaves=audited,certificate_sha256=sha(path),auditor_sha256=sha(Path(__file__)),verdict='CONFIRMED: exact once-only central coverage; all selected gaps independently positive. Combined with the analytic endpoint arguments, M_alpha > C_alpha for every 0 < alpha < 1.')
 (FOLDER/'independent_audit.json').write_text(json.dumps(result,indent=2)+'\n');print('CONFIRMED',len(leaves),'leaves; independent scaled margin >',float(minimum))
if __name__=='__main__':main()
