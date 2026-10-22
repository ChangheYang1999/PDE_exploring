"""iv160 recurrence/half-angle geometric model audit, independent of Arb output."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time,sys,math
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_series_operands';iv.dps=160;tic=time.monotonic()
def rat(v):return F.from_float(float(v))
def ivq(q):return iv.mpf(q.numerator)/q.denominator
def endpoint(t):
 s,m,e,_=t;return F(-m if s else m)*F(2)**e
def lower(z):return endpoint(z._mpi_[0])
def upper(z):return endpoint(z._mpi_[1])
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
cover=B/'research/localized_forcing/evidence/coverage.json';points=list(map(F,json.loads(cover.read_text())['local_points']));assert len(points)==14 and all(x<y for x,y in zip(points,points[1:]))
raw=json.loads((B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json').read_text());p1,p2=map(rat,raw['x_star_bracket']);pbox=iv.mpf([ivq(p1),ivq(p2)]);theta=rat(raw['theta_max']);rows=json.loads((S/'evidence/blocks.json').read_text())
with np.load(S/'evidence/operands.npz',allow_pickle=False) as f:data={k:f[k].copy() for k in f.files}
records=[];fails=[];ncoeff=positive=0;minrel=None;maxratio=F(0)
for ix,row in enumerate(rows):
 ci,q,bs,bp=[row[k] for k in ['ci','q','bs','bp']];assert tuple(data['indices'][ix])==(ci,q,bs,bp)
 h,w,half,width=map(rat,[row[k] for k in ['H','W','w','wk']]);T=points[ci-4096]+bs*h;angle=theta*F(2*q+1,32)-half+(4*bp+2)*width;M=max(abs(angle-w),abs(angle+w));assert 0<h<F(1,1000) and 0<w<F(1,1000) and M<F(1,100)
 es=[iv.exp(ivq(T))];ds=[iv.exp(2*ivq(T))]
 for i in range(1,13):es.append(es[-1]/i);ds.append(2*ds[-1]/i)
 cs=[iv.cos(ivq(angle)),-iv.sin(ivq(angle))]
 for j in range(2,9):cs.append(-cs[j-2]/(j*(j-1)))
 constant=(es[0]-pbox)**2+4*es[0]*pbox*iv.sin(ivq(angle)/2)**2
 coeff=[[constant if i==j==0 else (ds[i]-2*pbox*es[i]*cs[0] if j==0 else -2*pbox*es[i]*cs[j]) for j in range(9)] for i in range(13)]
 # Evaluate the rearranged positive remainder with two direct exponentials.
 small=h**13/F(math.factorial(13));angular=M*w**9/F(math.factorial(9))
 R=iv.exp(2*ivq(T+h))*ivq((2*h)**13/F(math.factorial(13)))+ivq(2*p2)*iv.exp(ivq(T+h))*ivq(small+angular);ru=upper(R);assert lower(R)>0
 model_records={}
 for model in ['q','uq']:
  terms=[];nex=0;largest=F(0);witness=None
  for i in range(13):
   for j in range(9):
    v=coeff[i][j]
    if model=='uq' and i==j==0:v=v-ivq(rat(row['c0']))
    l,u=lower(v),upper(v);mid,rad=rat(data[model+'_mid'][ix,i,j]),rat(data[model+'_rad'][ix,i,j]);assert rad>=0;dist=max(F(0),mid-rad-l,u-mid-rad);weight=dist*h**i*w**j;terms.append(weight);ncoeff+=1
    if dist:positive+=1;nex+=1
    if weight>largest:largest=weight;witness=[i,j,str(l),str(u),str(dist)]
  total=sum(terms,F(0));e=rat(data[model+'_rem'][ix]);assert e>0;margin=e-total-ru;ratio=(total+ru)/e;maxratio=max(maxratio,ratio);minrel=margin/e if minrel is None else min(minrel,margin/e)
  if margin<0:fails.append({'index':ix,'key':[ci,q,bs,bp],'model':model,'margin':str(margin),'ratio':str(ratio)})
  model_records[model]={'coefficient_excess_sum':str(total),'analytic_remainder_upper':str(ru),'saved_budget':str(e),'margin':str(margin),'relative_margin':str(margin/e),'positive_excess_coefficients':nex,'largest_weighted_excess':str(largest),'largest_excess_witness':witness}
 records.append({'index':ix,'key':[ci,q,bs,bp],'T_exact':str(T),'A_exact':str(angle),'M_exact':str(M),'models':model_records})
assert len(rows)==832 and ncoeff==194688
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_IV160_PHYSICAL_GEOMETRIC_MODELS' if not fails else 'OPEN_IV_GEOMETRIC_MODEL_TESTS','blocks':832,'models':1664,'coefficient_projection_tests':ncoeff,'positive_excess_coefficients':positive,'minimum_relative_margin':str(minrel),'maximum_budget_ratio':str(maxratio),'failures':fails,'records':records,'pins':{str(p.relative_to(B)):sha(p) for p in [S/'evidence/blocks.json',S/'evidence/operands.npz',cover,D/'PROOF.md']},'method':'Independent recurrences for exponentials and trigonometric Taylor coefficients; half-angle constant; rearranged analytic remainder with direct exp(2(T+H)).'}
(D/'evidence/iv.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],ncoeff,len(fails));print('maximum_budget_ratio',float(maxratio),'minimum_relative_margin',float(minrel));assert not fails,fails[:2]
