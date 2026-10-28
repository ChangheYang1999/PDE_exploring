"""Certify unequal-node phase interpolation using already accepted arrays."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib,re
R=Path(__file__).resolve().parents[1]
B=R/'08_improved_upper_bounds/phase_interpolation'
M=R/'08_improved_upper_bounds/middle_circle_transport/balanced_residual'
L=R/'08_improved_upper_bounds/local_disk_transport/balanced_residual'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def uq(x):return Q(str(x.upper().fmpq()))
def lq(x):return Q(str(x.lower().fmpq()))
def endpoints(s):
 if not s.startswith('['):return Q(s),Q(s)
 m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',s);assert m,s
 u,v=map(Q,m.groups());return u-v,u+v
def ceil10(q):
 k=-((-q*10**10).__floor__());return f'{k//10**10}.{k%10**10:010d}'
def main():
 ctx.prec=384;hashes={}
 def bind(p):hashes[str(p.relative_to(R))]=sha(p)
 for p,ledger in [(M/'verification/accepted.json','V168'),(M/'table37/verification/accepted.json','V171')]:
  d=load(p);assert d['verdict']=='CONFIRMED' and d['ledger']==ledger;bind(p)
  for rel,h in d['sha256'].items():assert sha(R/rel)==h,rel;bind(R/rel)
 mid=load(M/'verification/independent_audit.json');extra=load(M/'table37/verification/independent_audit.json')
 small={r['alpha']:Q(r['small_upper']) for r in load(L/'existing_certificates/verification/independent_audit.json')['rows']}
 dp=R/'data/middle_composite_upper_n512.json';dnear={r['alpha']:endpoints(r['near_D'])[1] for r in load(dp)['rows']}
 for p in [M/'verification/independent_audit.json',M/'table37/verification/independent_audit.json',L/'existing_certificates/verification/independent_audit.json',dp]:bind(p)
 delta=arb.pi()/32;c=delta.cos();s=delta.sin();cl=lq(c);sec=1/(delta/2).cos()
 def bound(u,v):
  U,V=arb(str(u)),arb(str(v))
  if v<=u*cl:return u,dict(method='left endpoint',value=str(u))
  if u<=v*cl:return v,dict(method='right endpoint',value=str(v))
  amp=(U*U+V*V-2*U*V*c).sqrt()/s
  secbound=sec*arb(str(max(u,v)));a,b=uq(amp),uq(secbound)
  return min(a,b),dict(method='amplitude and secant minimum',amplitude_upper=str(a),secant_upper=str(b))
 rows=[]
 tasks=[]
 for r in mid['rows']:
  for operator in ['C','D']:
   tasks.append((r['alpha'],operator,list(map(Q,r[operator+'_phase_upper'])),small[r['alpha']] if operator=='C' else dnear[r['alpha']],r['safe_upper_'+operator]))
 for r in extra['rows']:tasks.append((r['alpha'],'C',list(map(Q,r['phase_upper'])),small[r['alpha']],r['safe_upper_C']))
 for alpha,operator,u,S,previous in tasks:
  assert len(u)==17 and all(v>=0 for v in u)
  intervals=[]
  for j in range(16):
   h,detail=bound(u[j],u[j+1]);intervals.append(dict(index=j,left=str(u[j]),right=str(u[j+1]),certified_upper=str(h),**detail))
  worst=max(range(16),key=lambda j:Q(intervals[j]['certified_upper']))
  regular=Q(intervals[worst]['certified_upper']);total=S+regular;safe=ceil10(total)
  assert Q(safe)<=Q(previous),(alpha,operator,safe,previous)
  row=dict(alpha=alpha,operator=operator,phase_upper=list(map(str,u)),uniform_part=str(S),intervals=intervals,worst_interval=worst,
   regular_upper=str(regular),complete_upper=str(total),safe_upper=safe,previous_upper=previous,decimal_improvement=str(Q(previous)-Q(safe)))
  rows.append(row);print(alpha,operator,previous,'->',safe,'interval',worst,flush=True)
 for p in [Path(__file__),B/'PROOF.md']:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),status='NUMERICAL CHECKS PASS; analytic cross-read and second acceptance pending',precision_bits=384,phase_intervals=16,rows=rows,sha256=hashes)
 (B/'verification/independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
