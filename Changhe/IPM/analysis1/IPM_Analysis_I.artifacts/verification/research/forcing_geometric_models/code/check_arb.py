"""Arb512 exact-derivative geometric Taylor model and projection certificate."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time,sys,math
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_series_operands';ctx.prec=512;tic=time.monotonic();ff=lambda x:Q.from_float(float(x))
def ar(x):return arb(x.numerator)/x.denominator
def lo(x):return Q(str(x.lower().fmpq()))
def hi(x):return Q(str(x.upper().fmpq()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.loads((S/'evidence/blocks.json').read_text());part=json.loads((B/'research/middle_residual/evidence/partition_exact.json').read_text());pts=[];last=None
for z in part['spans']:
 a,b=Q(z['a_exact']),Q(z['b_exact']);n=z['count'];assert n>0 and a<b and z['first_cell']==len(pts)
 if last is not None:assert last==a
 pts.extend(a+(b-a)*i/n for i in range(n));last=b
pts.append(last);assert len(pts)==7810
raw=json.loads((B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json').read_text());p1,p2=map(ff,raw['x_star_bracket']);pp=ar(p1).union(ar(p2));th=ff(raw['theta_max']);fac=[math.factorial(i) for i in range(14)]
with np.load(S/'evidence/operands.npz',allow_pickle=False) as z:d={k:z[k].copy() for k in z.files}
records=[];fail=[];nt=ne=0;minrel=None;maxratio=Q(0)
for n,row in enumerate(rows):
 ci,q,bs,bp=[row[k] for k in ['ci','q','bs','bp']];assert tuple(d['indices'][n])==(ci,q,bs,bp)
 H,W,w,wk,c0=map(ff,[row[k] for k in ['H','W','w','wk','c0']]);T=pts[ci]+bs*H;A=th*Q(2*q+1,32)-w+(4*bp+2)*wk;M=max(abs(A-W),abs(A+W));assert 0<H<Q(1,1000) and 0<W<Q(1,1000) and M<Q(1,100)
 E=ar(T).exp();sn,cs=ar(A).sin_cos();trig=[cs,-sn,-cs,sn];ep=E*pp
 coefficients=[]
 for i in range(13):
  cc=[]
  for j in range(9):
   if i==j==0:v=(E*cs-pp)**2+(E*sn)**2
   elif j==0:v=((2**i)*E**2-2*ep*cs)/fac[i]
   else:v=(-2*ep*trig[j%4])/(fac[i]*fac[j])
   cc.append(v)
  coefficients.append(cc)
 R=E**2*ar(2*H).exp()*ar((2*H)**13/Q(fac[13]))+2*ar(p2)*E*ar(H).exp()*ar(H**13/Q(fac[13])+M*W**9/Q(fac[9]));rup=hi(R);assert lo(R)>0
 mr={}
 for model in ['q','uq']:
  total=Q(0);excess_count=0;biggest=(Q(0),None);budget=ff(d[model+'_rem'][n]);assert budget>0
  for i in range(13):
   for j in range(9):
    v=coefficients[i][j]-(ar(c0) if model=='uq' and i==j==0 else 0);vl,vu=lo(v),hi(v);m,r=ff(d[model+'_mid'][n,i,j]),ff(d[model+'_rad'][n,i,j]);assert r>=0;ex=max(Q(0),m-r-vl,vu-m-r);term=ex*H**i*W**j;total+=term;nt+=1
    if ex>0:excess_count+=1;ne+=1
    if term>biggest[0]:biggest=(term,[i,j,str(vl),str(vu),str(ex)])
  margin=budget-total-rup;ratio=(total+rup)/budget;minrel=margin/budget if minrel is None else min(minrel,margin/budget);maxratio=max(maxratio,ratio)
  if margin<0:fail.append({'index':n,'key':[ci,q,bs,bp],'model':model,'margin':str(margin),'ratio':str(ratio)})
  mr[model]={'coefficient_excess_sum':str(total),'analytic_remainder_upper':str(rup),'saved_budget':str(budget),'margin':str(margin),'relative_margin':str(margin/budget),'positive_excess_coefficients':excess_count,'largest_weighted_excess':str(biggest[0]),'largest_excess_witness':biggest[1]}
 records.append({'index':n,'key':[ci,q,bs,bp],'T_exact':str(T),'A_exact':str(A),'M_exact':str(M),'models':mr})
assert len(rows)==832 and nt==194688
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_ARB512_PHYSICAL_GEOMETRIC_MODELS' if not fail else 'OPEN_ARB_GEOMETRIC_MODEL_TESTS','blocks':832,'models':1664,'coefficient_projection_tests':nt,'positive_excess_coefficients':ne,'minimum_relative_margin':str(minrel),'maximum_budget_ratio':str(maxratio),'failures':fail,'records':records,'pins':{str(p.relative_to(B)):sha(p) for p in [S/'evidence/blocks.json',S/'evidence/operands.npz',B/'research/middle_residual/evidence/partition_exact.json',D/'PROOF.md']},'scope':'Physical geometric q and q-c0, uniform p and canonical t_i, on whole rectangles. No residual or full composed forcing claim.'}
(D/'evidence/arb.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],nt,len(fail));print('maximum_budget_ratio',float(maxratio),'minimum_relative_margin',float(minrel));assert not fail,fail[:2]
