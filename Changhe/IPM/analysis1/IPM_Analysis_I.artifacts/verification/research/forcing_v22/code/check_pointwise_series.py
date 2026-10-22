"""Exact dyadic products, independently grouped Arb bounds and three tail tests."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from flint import arb, ctx
from mpmath import iv
import json, hashlib, math, time
D=Path(__file__).resolve().parents[1];ctx.prec=384;iv.dps=120;start=time.monotonic()
p=D/'source/runs/forcing/v22_p9_merged.json';raw=json.loads(p.read_text());rows=raw['cells']
assert hashlib.sha256(p.read_bytes()).hexdigest()=='b5f597c90a0928dd9a5ea87af12953bcc33f46321ef60c3d5b014d9bef3a7201'
def f(x):
 assert isinstance(x,(float,int)) and math.isfinite(x)
 return Q.from_float(float(x))
def a(x):return arb(x.numerator)/x.denominator
def v(x):return iv.mpf(x.numerator)/x.denominator
def ah(x):return Q(str(x.upper().fmpq()))
def mpf(x):
 s,m,e,bc=x
 assert s in (0,1) and m>=0 and bc>=0 and ((m==0 and e==0 and bc==0) or (m>0 and m.bit_length()==bc)),x
 return (-1 if s else 1)*Q(m)*Q(2)**e
def vh(x):return mpf(x._mpi_[1])
G=['G0','G1','G2F','GL','GL1','GL2'];T=['T0','T1','T2F','TL','TL1','TL2'];F=['F0','F1','FL','FL1','FL2']
# Each coefficient vector indexes pair products (tau component, g component).
terms=[[(1,0,0)],[(1,0,1),(1,1,0)],[(1,0,3),(2,1,1),(1,3,0)],
 [(1,1,3),(1,0,4),(2,2,1),(2,1,2),(1,3,1),(1,4,0)],
 [(1,0,5),(1,5,0),(2,3,3),(4,1,4),(4,4,1),(4,2,2)]]
counts={k:0 for k in ('inside','straddle','transition')};checks=0;eq=0;minrel=None;blocks={};fallback=set();nseries=0
for r in rows:
 reg=r['regime'];counts[reg]+=1;gs=[f(r[k]) for k in G];ts=[f(r[k]) for k in T];fs=[f(r[k]) for k in F]
 assert min(gs+ts+fs)>=0
 if reg=='inside':
  qs=[gs[j] for j in (0,1,3,4,5)]
  bs=[a(gs[j]) for j in (0,1,3,4,5)]
 elif reg=='straddle':
  qs=[sum((n*ts[t]*gs[g] for n,t,g in row),Q(0)) for row in terms]
  g0,g1,g2,gl,gl1,gl2=map(a,gs);t0,t1,t2,tl,tl1,tl2=map(a,ts)
  # Different grouping: collect by the common residual factor.
  bs=[g0*t0, g0*t1+g1*t0, g0*tl+g1*(2*t1)+gl*t0,
      g0*tl1+g1*(2*t2+tl)+g2*(2*t1)+gl*t1+gl1*t0,
      g0*tl2+g1*(4*tl1)+g2*(4*t2)+gl*(2*tl)+gl1*(4*t1)+gl2*t0]
 else:qs=bs=[]
 for key,q,b,saved in zip(F,qs,bs,fs):
  assert q<=saved,(reg,key,q,saved)
  assert ah(b)<=saved,(reg,key,str(b),saved)
  checks+=1;eq+=q==saved
  if saved and q<saved:
   z=(saved-q)/saved;minrel=z if minrel is None else min(minrel,z)
 bkey=tuple(r[k] for k in ('ci','q','bs','bp'))
 if r['series'] is None:
  fallback.add(bkey);assert reg=='inside';continue
 tri=tuple(f(x) for x in r['series']);assert blocks.setdefault(bkey,tri)==tri;nseries+=1
assert not(set(blocks)&fallback)
min_tail=None;maxtail=Q(0);maxratio=Q(0)
for key,(c,x,tail) in blocks.items():
 assert c>0 and 0<=x<Q(3,5) and tail>=0
 # Squared rational inequality, direct Arb root, and iv log/exp.
 q=tail*tail*c*(1-x)**2;rhs=x**34;assert q>=rhs,(key,q,rhs)
 target=(a(x)**17)/(a(c).sqrt()*(1-a(x)))
 assert ah(target)<=tail,(key,str(target),tail)
 target2=iv.exp(17*iv.ln(v(x))-iv.ln(v(c))/2-iv.ln(1-v(x))) if x else iv.mpf(0)
 assert vh(target2)<=tail,(key,str(target2),tail)
 if rhs:
  z=(q-rhs)/rhs;min_tail=z if min_tail is None else min(min_tail,z)
 maxratio=max(maxratio,x);maxtail=max(maxtail,tail)
assert len(rows)==43949 and counts=={'inside':26079,'straddle':1368,'transition':16502}
assert checks==137235 and len(blocks)==331 and len(fallback)==43 and nseries==38445
# Published extrema range over all832 blocks; saved row triples cover only374.
assert maxratio<=f(raw['worst_series']['x_series']) and maxtail<=f(raw['worst_series']['tail'])
out=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-start,status='PASS_V22_POINTWISE_ROWS_AND_SAVED_SERIES_TAILS',rows=len(rows),classifications=counts,pointwise_checks_per_engine=checks,exact_equalities=eq,strict_relative_slack_min=str(minrel),series_blocks=len(blocks),fallback_blocks=len(fallback),series_occurrences=nseries,tail_checks_per_engine=len(blocks),tail_squared_relative_slack_min=str(min_tail),largest_saved_ratio=str(maxratio),largest_saved_tail=str(maxtail),data_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),methods=['exact dyadic weighted products','Arb384 regrouped expressions and direct square root','exact squared tail inequality','mpmath.iv120 log/exp tail with finite endpoint guards'],scope='Pointwise rows conditional on their six G factors; cutoff factors separately checked. The tail formula is checked on each saved triple, without proving physical q/c0 linkage or missing composed arrays. No bound is asserted for transition rows by the fallback formula.')
(D/'evidence/pointwise_series.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],'seconds',out['seconds'],'checks',checks,'series',len(blocks))
