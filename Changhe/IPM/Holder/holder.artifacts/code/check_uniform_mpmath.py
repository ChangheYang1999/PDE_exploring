"""Independent 90-decimal recombination using stored rational split points."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'09_uniform_comparison/lead_certificate/data';mp.mp.dps=90;ctx.prec=256

def q(x):
 f=Fraction(x);return mp.mpf(f.numerator)/f.denominator

def hi(text):
 v=arb(text).upper().fmpq();return mp.mpf(str(v.numerator))/mp.mpf(str(v.denominator))

def load(name):return json.loads((BASE/name).read_text())

def main():
 checked=json.loads((ROOT/'data/uniform_comparison_independent.json').read_text());nodes=load('nodes2.json')
 up={r['alpha']:r for name in ['upper_n384.json','upper_n384_b.json'] for r in load(name)['rows']};up={Fraction(k):v for k,v in up.items()}
 lows={g:load(f'lower2_g{g}.json') for g in range(8)};fars={g:load(f'far2_g{g}.json') for g in range(8)}
 sec=1/mp.cos(mp.pi/64);totals={};rows=[]
 for rec in checked['rows']:
  gi=rec['group'];kind=rec['kind'];mode=rec['mode'];group=nodes['groups'][gi]
  lower={Fraction(r['alpha']):r for r in lows[gi]['rows']};far={Fraction(r['alpha']):r for r in fars[gi]['rows']};X=list(map(Fraction,group['nodes']))
  av,bv=map(Fraction,rec['upper_segment']);end=[]
  for x in [av,bv]:
   r=up[x];a=q(x)
   if mode=='thm34':value=mp.mpf(r['safe_upper_'+kind])
   else:
    regular=sec*max(hi(u)+hi(v) for u,v in zip(r['regular_grid'],far[x]['far_phase_intervals']))
    if kind=='C':value=4*2**(-a/2)/(mp.pi*a*(a+2))+regular
    else:value=2**(-a)*mp.gamma((a+2)/2)/(mp.sqrt(mp.pi)*mp.gamma((a+3)/2)*a)+mp.mpf('.5')+regular
   end.append(mp.log(value))
  def E(t):return (q(bv-t)*end[0]+q(t-av)*end[1])/q(bv-av)
  def lo(t):return mp.log(mp.mpf(lower[t]['safe_decimal_lower_10_places'])/q(t))
  def upp(t):return mp.log(mp.mpf(lower[t]['safe_decimal_upper_10_places'])/q(t))
  vals=[]
  for xs,cs,ys in rec['splits']:
   x,c,y=map(Fraction,[xs,cs,ys]);i=X.index(x);p=X[i-1];z=X[i+2]
   sl=(lo(x)-upp(p))/q(x-p);sr=(lo(y)-upp(z))/q(z-y)
   vals.extend([E(x)-mp.log(q(x))-lo(x),E(c)-mp.log(q(c))-lo(x)-q(c-x)*sl,E(c)-mp.log(q(c))-lo(y)-q(y-c)*sr,E(y)-mp.log(q(y))-lo(y)])
  result=mp.exp(max(vals));assert result<mp.mpf(rec['ratio_upper'])
  key=(mode,kind);totals[key]=max(totals.get(key,mp.mpf(0)),result)
  rows.append(dict(mode=mode,group=gi,kind=kind,upper_segment=rec['upper_segment'],ratio=mp.nstr(result,80),checked_upper=rec['ratio_upper']))
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),decimal_precision=90,all_segment_bounds_passed=True,summary={mode:{kind:mp.nstr(totals[(mode,kind)],80) for kind in ['C','D']} for mode in ['thm35','thm34']},rows=rows,source_hashes={s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in ['code/check_uniform_mpmath.py','data/uniform_comparison_independent.json']})
 (ROOT/'data/uniform_comparison_mpmath.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['summary'],indent=2))
if __name__=='__main__':main()
