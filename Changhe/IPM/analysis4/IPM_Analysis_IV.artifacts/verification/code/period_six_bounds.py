"""Exact global Q6 response infima and component-radius certificates."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
from math import comb
import json,sys,time
sys.dont_write_bytecode=True
import sympy as sp
from general_component_radius import Majorant,stringify
root=Path('research/155_period_six_response_infima');src=Path('research/154_period_six_tuning/verification');start=time.monotonic();b,k=sp.symbols('b k')
def coeff(e):
 p=sp.Poly(e,b,domain=sp.QQ)
 return [F(str(p.nth(j))) for j in range(p.degree()+1)]
def imul(a,z):
 v=[x*y for x in a for y in z];return min(v),max(v)
def ev(a,I):
 out=(F(0),F(0))
 for c in reversed(a):lo,hi=imul(out,I);out=lo+c,hi+c
 return out
def ab(a):
 lo,hi=a;assert lo>0 or hi<0
 return (lo,hi) if lo>0 else (-hi,-lo)
def put(n,d):(root/'verification'/n).write_text(json.dumps(stringify(d),indent=2,default=str)+'\n')
try:
 data=json.loads((src/'symbolic_responses.json').read_text());N=sp.Poly(sp.sympify(data['numerator']),k,b,domain=sp.QQ);D=sp.Poly(sp.sympify(data['denominator']),k,domain=sp.QQ);nd,bd=N.degree(k),N.degree(b)
 mat=[[F(0)]*(bd+1) for _ in range(nd+1)]
 for (j,m),v in N.terms():mat[j][m]=F(str(v))
 dc=[F(str(D.nth(j))) for j in range(D.degree()+1)];assert nd==D.degree()
 if dc[-1]<0:dc=[-v for v in dc];mat=[[-v for v in row] for row in mat]
 small={r['k']:coeff(sp.sympify(r['sigma'])) for r in json.loads((src/'small_responses.json').read_text())['rows']};limit=coeff(sp.sympify(data['sigma_infinity']))
 roots=json.loads((src/'root_response_certificates.json').read_text())['real_roots'];shifts={}
 def shift(K):
  if K not in shifts:
   nm=[[sum(mat[j][m]*comb(j,t)*K**(j-t) for j in range(t,nd+1)) for m in range(bd+1)] for t in range(nd+1)]
   dd=[sum(dc[j]*comb(j,t)*K**(j-t) for j in range(t,len(dc))) for t in range(len(dc))];assert all(c>0 for c in dd);shifts[K]=nm,dd
  return shifts[K]
 def fixed(j):
  if j in small:return small[j]
  d=sum(c*j**m for m,c in enumerate(dc));assert d>0
  return [sum(mat[t][m]*j**t for t in range(nd+1))/d for m in range(bd+1)]
 rows=[];alist=list(map(F,['161/100','109/100','23/20','6/5','32/25','38/25']));slower=list(map(F,['434/25','87/500000','309/1000000','29/20000','189/10000','483/1000']));qpowers=[60,73,73,71,68,65]
 for index,(rr,targetk,a,s,q) in enumerate(zip(roots,[6,5,6,None,None,6],alist,slower,qpowers),1):
  I=tuple(map(F,rr['interval']));target=small[targetk] if targetk is not None else limit;raw=ev(target,I);sg=1 if raw[0]>0 else -1;target=[sg*c for c in target];tiv=ev(target,I);assert tiv[0]>0
  liv=ev(limit,I);ts=1 if liv[0]>0 else -1;assert (targetk is None) or ab(liv)[0]>tiv[1]
  trials=[]
  for K in [13,16,24,32,48,64,96,128,256,512,1024]:
   nm,dd=shift(K);bounds=[];zeros=[]
   for t,co in enumerate(nm):
    expr=[ts*co[m]-dd[t]*(target[m] if m<len(target) else 0) for m in range(bd+1)];zeros.append(all(v==0 for v in expr));bounds.append(ev(expr,I))
   ok=bounds[0][0]>0 and all(lo>=0 for lo,hi in bounds);trials.append(dict(K=K,negative_count=sum(lo<0 for lo,hi in bounds),zero_coefficients=[j for j,v in enumerate(zeros) if v]))
   if ok:break
  else:raise AssertionError(('no positive tail certificate',index,trials))
  finite=[]
  for j in range(2,K):
   v=ev(fixed(j),I);av=ab(v);gap=F(0) if j==targetk else av[0]-tiv[1];assert j==targetk or gap>0
   finite.append(dict(k=j,signed_interval=v,absolute_interval=av,gap_lower=gap))
  assert tiv[0]>s and 1+max(map(abs,I))<a
  scale=1
  while tiv[0]*scale<100:scale*=10
  sharper=F((tiv[0]*scale).numerator//(tiv[0]*scale).denominator,scale);assert 0<sharper<tiv[0]
  m=Majorant(6,a,F(128,3),s);box=[2*v for v in m.Y0];z0=F(1,2**q);values=m.transformed(z0,box);margins=[v-w for v,w in zip(box,values)];assert all(v>0 for v in margins)
  previous=m.transformed(2*z0,box);assert any(v>w for v,w in zip(previous,box))
  row=dict(root_index=index,root_interval=I,unique_minimizer=targetk,infimum_attained=targetk is not None,infimum_sign=sg,infimum_polynomial=target,infimum_interval=tiv,infimum_approx=float(sum(tiv)/2),uniform_response_lower=s,three_digit_lower=sharper,tail_sign=ts,tail_from_k=K,tail_trials=trials,tail_coefficient_intervals=bounds,shifted_denominator_coefficients=dd,finite_checks=finite,a=a,kappa=F(128,3),L=F(3),z0=z0,z_power=q,radius_power=3*q,J=m.J,T=m.T,Y0=m.Y0,box=box,map_on_box=values,positive_margins=margins,max_component_ratio=max(v/w for v,w in zip(values,box)),previous_dyadic_fails=True)
  rows.append(row);put('checks.partial.json',dict(rows=rows));print(json.dumps(dict(root=index,k=targetk,minimum=row['infimum_approx'],sharper=str(sharper),K=K,radius_power=3*q,max_ratio=float(row['max_component_ratio']),elapsed_s=time.monotonic()-start)),flush=True)
 m=Majorant(6,F(161,100),F(128,3),F(87,500000));box=[2*v for v in m.Y0];z0=F(1,2**77);values=m.transformed(z0,box);margins=[v-w for v,w in zip(box,values)];assert all(v>0 for v in margins);assert any(v>w for v,w in zip(m.transformed(2*z0,box),box))
 common=dict(a=m.a,s=m.lower,z0=z0,radius_power=231,J=m.J,T=m.T,Y0=m.Y0,box=box,map_on_box=values,positive_margins=margins,max_component_ratio=max(v/w for v,w in zip(values,box)),previous_dyadic_fails=True)
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,common=common,input_hashes={str(p):sha256(p.read_bytes()).hexdigest() for p in [src/'symbolic_responses.json',src/'small_responses.json',src/'root_response_certificates.json']},actual_elapsed_s=time.monotonic()-start);put('checks.json',result)
 for name in ['period_six_bounds.py','general_component_radius.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};put('MANIFEST.json',dict(files=files));print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
 import traceback
 fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start);put('FAILURE.json',fail);print(json.dumps(fail),flush=True);raise SystemExit(1)
