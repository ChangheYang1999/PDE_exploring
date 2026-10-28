"""Ninety-digit arithmetic cross-check of every third-pass segment."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'09_uniform_comparison/pass3';OLD=ROOT/'09_uniform_comparison/lead_certificate/data';mp.mp.dps=90;ctx.prec=256

def load(p):return json.loads(p.read_text())
def q(x):x=Q(x);return mp.mpf(x.numerator)/x.denominator
def hi(s):x=arb(s).upper().fmpq();return mp.mpf(str(x.numerator))/mp.mpf(str(x.denominator))
def main():
 checked=load(BASE/'verification/independent_recombination.json');nodes=load(OLD/'nodes2.json');prior=load(ROOT/'data/uniform_comparison_mpmath.json');oldrows={(r['group'],tuple(r['upper_segment'])):mp.mpf(r['ratio']) for r in prior['rows'] if r['mode']=='thm35' and r['kind']=='C'}
 lt={};mt={};sec=1/mp.cos(mp.pi/64)
 for p in (BASE/'data/local').glob('*.json'):
  d=load(p);x=Q(d['alpha']);v=lt.setdefault(x,[mp.mpf(0) for _ in range(17)])
  for j,s in d['partial_phase_intervals'].items():v[int(j)]+=hi(s)
 for p in (BASE/'data/mid').glob('*.json'):
  for r in load(p)['rows']:
   k=(Q(r['plan_reference_alpha']),Q(r['alpha']));v=mt.setdefault(k,[mp.mpf(0) for _ in range(17)])
   for j,s in enumerate(r['middle_phase_intervals']):v[j]+=hi(s)
 rows=[];worst=mp.mpf(0)
 for rec in checked['rows']:
  gi=rec['group'];g=nodes['groups'][gi];a,b=map(Q,rec['upper_segment']);old=oldrows[(gi,tuple(rec['upper_segment']))];fresh=None
  if rec['new_log_upper'] is not None:
   ref=Q(g['far_ref']);far={Q(r['alpha']):r for r in load(OLD/f'far2_g{gi}.json')['rows']};low={Q(r['alpha']):r for r in load(OLD/f'lower2_g{gi}.json')['rows']};X=list(map(Q,g['nodes']));ends=[]
   for x in [a,b]:
    alpha=q(x);delta=mp.mpf(1)/64;small=4*2**(alpha/2)*delta**alpha/(mp.pi*alpha*(alpha+2))+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
    regular=max(l+m+hi(f) for l,m,f in zip(lt[x],mt[(ref,x)],far[x]['far_phase_intervals']));ends.append(mp.log(small+sec*regular))
   def E(t):return (q(b-t)*ends[0]+q(t-a)*ends[1])/q(b-a)
   def lo(x):return mp.log(mp.mpf(low[x]['safe_decimal_lower_10_places'])/q(x))
   def up(x):return mp.log(mp.mpf(low[x]['safe_decimal_upper_10_places'])/q(x))
   vals=[]
   for xs,cs,ys in rec['splits']:
    x,c,y=map(Q,[xs,cs,ys]);i=X.index(x);prev,nxt=X[i-1],X[i+2];sl=(lo(x)-up(prev))/q(x-prev);sr=(lo(y)-up(nxt))/q(nxt-y)
    vals.extend([E(x)-mp.log(q(x))-lo(x),E(c)-mp.log(q(c))-lo(x)-q(c-x)*sl,E(c)-mp.log(q(c))-lo(y)-q(y-c)*sr,E(y)-mp.log(q(y))-lo(y)])
   fresh=mp.exp(max(vals))
  chosen=old if fresh is None else min(old,fresh);assert chosen<mp.mpf(rec['safe_ratio']);worst=max(worst,chosen)
  rows.append(dict(group=gi,upper_segment=rec['upper_segment'],old_ratio=mp.nstr(old,80),new_ratio=None if fresh is None else mp.nstr(fresh,80),chosen_ratio=mp.nstr(chosen,80),checked_upper=rec['safe_ratio']))
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),decimal_precision=90,all_segment_checks_passed=True,uniform_ratio=mp.nstr(worst,80),rows=rows,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),BASE/'verification/independent_recombination.json',ROOT/'data/uniform_comparison_mpmath.json']})
 (BASE/'verification/mpmath_recombination.json').write_text(json.dumps(out,indent=2)+'\n');print(out['uniform_ratio'])
if __name__=='__main__':main()
