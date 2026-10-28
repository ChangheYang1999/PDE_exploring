"""Independent closed-form audit using analytic chord maxima at 320 bits.

This does not certify the alpha-zero source integrals by itself. Their
separate replay is recorded in alpha0_replay.json. Previously accepted
positive-exponent nodes are checked against the frozen V081 inputs.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/closed_form_lead'
SRC=BASE/'source'
ctx.prec=320

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(q):return arb(str(q))
def exact(v):return Q(str(v.fmpq()))
def rec(v):
 assert v.is_finite()
 return dict(lower=str(v.lower().fmpq()),upper=str(v.upper().fmpq()),display=v.str(30,more=True))
def a3(a,N=140):
 # Positive combined series, independent of the I0-I1 subtraction.
 coeff=arb(1);total=arb(0)
 for k in range(N):
  total+=coeff*arb(4)**(-k-1)*2*(a+5+2*k)/((a+2+2*k)*(a+4+2*k))
  coeff*=arb(2*k+1)/arb(2*k+2)
 tail=3*arb(4)**(-N)/(arb.pi()*(a+2+2*N))
 return 3*total/arb.pi()+arb(0).union(tail)

def main():
 nodes=json.loads((SRC/'data/remainders.json').read_text())
 hashes={}
 for name,h in nodes['source_sha256'].items():
  assert sha(SRC/name)==h,(name,'hash');hashes[name]=h
 for name in ['uniform_result_thm35_pass3.json','uniform_result_thm37_pass3.json']:
  assert sha(SRC/'data'/name)==sha(ROOT/'09_uniform_comparison/pass3/data'/name),(name,'V081 node mismatch')
 old=json.loads((SRC/'data/uniform_result_thm35_pass3.json').read_text())
 groups={};nd={Q(row['alpha']):row for row in nodes['nodes']}
 for row in nodes['nodes']:
  assert Q(row['R'])>0
  for g in row['groups']:groups.setdefault(g,[]).append((Q(row['alpha']),Q(row['R'])))
 node_checks=[]
 for g,values in old['nodal_upper'].items():
  for text in values['C']:
   x=Q(text);a=aq(x);a2=arb(2)**(1+a/2)/(arb.pi()*(a+2))
   lc=arb(2)**(1-a)*a2/a
   ld=arb(2)**(1-a)*((a+2)/2).gamma()/(2*arb.pi().sqrt()*((a+3)/2).gamma()*a)+arb(1)/2
   target=aq(Q(nd[x]['R']))
   rc=arb(values['C'][text])-lc;rd=arb(values['D'][text])-ld
   assert target>=rc and target>=rd,(g,text,'remainder too small')
   node_checks.append(dict(group=int(g),alpha=text,margin_C=rec(target-rc),margin_D=rec(target-rd)))
 assert sorted(groups)==list(range(8))
 assert groups[0][0][0]==0 and groups[7][-1][0]==Q(199,200)
 for g,L in groups.items():
  assert L==sorted(L) and len({x for x,r in L})==len(L)
  if g:assert groups[g-1][-1][0]==L[0][0]
 kap=arb(209)/500;c=arb(72)/125
 intervals=[];worst=arb(-1000)
 for g,L in groups.items():
  for (x,rx),(y,ry) in zip(L,L[1:]):
   la=aq(rx).log();lb=aq(ry).log();s=(lb-la)/aq(y-x)
   def gap(t):
    # Negative log ratio certifies exp(chord)<kappa/(1-t)+c.
    return la+s*(t-aq(x))-(kap/(1-t)+c).log()
   vals=[gap(aq(x)),gap(aq(y))];critical=None
   if s>0:
    # Stable positive root u of c*u^2+kappa*u-kappa/s=0.
    u=2*kap/s/(kap+(kap*kap+4*c*kap/s).sqrt());t=1-u
    if not (t<aq(x) or t>aq(y)):
     assert t>0 and t<1
     vals.append(gap(t));critical=rec(t)
   elif not s<=0:raise AssertionError('undecidable chord slope')
   upper=vals[0]
   for value in vals[1:]:upper=arb.max(upper,value)
   assert upper<0,(g,x,y,upper)
   worst=arb.max(worst,upper)
   intervals.append(dict(group=g,a=str(x),b=str(y),critical=critical,log_ratio_upper=rec(upper)))
 # Entire exponent intervals, with a second expression for a3 and F_b.
 end=[];M=100
 for i in range(M):
  x=Q(199,200)+Q(i,200*M);y=Q(199,200)+Q(i+1,200*M)
  a=aq(x).union(aq(y));delta=1-a
  aa2=arb(2)**(1+a/2)/(arb.pi()*(a+2));aa3=a3(a)
  numerator=2*aa3+delta*arb(2)**(a+1)/(3*arb.pi())
  scaled=(2*aa2)**(1-a)*numerator**a/a
  lc=arb(2)**(1-a)*aa2/a
  ld=arb(2)**(1-a)*((a+2)/2).gamma()/(2*arb.pi().sqrt()*((a+3)/2).gamma()*a)
  margins={name:delta*v+kap+c*delta-scaled for name,v in [('C',lc),('D',ld)]}
  assert all(v>0 for v in margins.values()),(x,y,margins)
  end.append(dict(a=str(x),b=str(y),margins={k:rec(v) for k,v in margins.items()}))
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,
  source_hashes=hashes,node_checks=node_checks,chord_intervals=intervals,
  max_chord_log_ratio=rec(worst),endpoint_intervals=end,
  verdict='PASS for nodal subtraction, exact interval coverage, analytic chord maxima and endpoint majorization. Alpha-zero node requires separate replay.',auditor_sha256=sha(Path(__file__)))
 (BASE/'verification').mkdir(exist_ok=True)
 (BASE/'verification/independent_chord_audit.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(time_utc=result['time_utc'],nodes=len(node_checks),segments=len(intervals),worst_log_ratio=worst.str(20),endpoint_intervals=M),indent=2))
if __name__=='__main__':main()
