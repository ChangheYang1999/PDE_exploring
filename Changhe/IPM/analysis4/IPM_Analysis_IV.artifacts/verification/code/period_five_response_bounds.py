"""Exact rational, coefficient-positive uniform bounds for the Q=5 responses."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from math import comb
import json,sys,time
sys.dont_write_bytecode=True
import sympy as sp
root=Path('research/133_six_period_five_profiles');src=Path('research/130_period_five_tuning/verification');start=time.monotonic();b,k=sp.symbols('b k')
def frac(v):return F(int(v.p),int(v.q))
def interval_mul(a,z):
 vals=[a[i]*z[j] for i in range(2) for j in range(2)];return min(vals),max(vals)
def interval_poly(coeff,lo,hi):
 v=(F(0),F(0))
 for c in reversed(coeff):
  v=interval_mul(v,(lo,hi));v=(v[0]+c,v[1]+c)
 return v
def absolute_lower(iv):
 lo,hi=iv
 assert lo>0 or hi<0,('unresolved',str(lo),str(hi))
 return lo if lo>0 else -hi
def polycoeff(e):
 p=sp.Poly(e,b,domain=sp.QQ);return [frac(p.nth(i)) for i in range(p.degree()+1)]
def dyadic_below(x):
 q=F(1)
 while q>=x:q/=2
 return q
try:
 data=json.loads((src/'symbolic_responses.json').read_text());N=sp.Poly(sp.sympify(data['numerator']),k,b,domain=sp.QQ);D=sp.Poly(sp.sympify(data['denominator']),k,domain=sp.QQ)
 nd,bd=N.degree(k),N.degree(b);mat=[[F(0) for _ in range(bd+1)] for _ in range(nd+1)]
 for (j,m),v in N.terms():mat[j][m]=frac(v)
 dc=[frac(D.nth(j)) for j in range(D.degree()+1)]
 small={r['k']:polycoeff(sp.sympify(r['sigma'])) for r in json.loads((src/'small_responses.json').read_text())['rows']}
 limits=polycoeff(sp.sympify(data['sigma_infinity']));rootrows=json.loads((src/'irreducibility_sturm_checks.json').read_text())['real_roots'];rows=[]
 def fixed_coeff(k0):return [sum(mat[j][m]*k0**j for j in range(nd+1)) for m in range(bd+1)]
 def fixed_den(k0):return sum(c*k0**j for j,c in enumerate(dc))
 shifts={}
 def shift(K):
  if K not in shifts:
   nm=[[sum(mat[j][m]*comb(j,t)*K**(j-t) for j in range(t,nd+1)) for m in range(bd+1)] for t in range(nd+1)]
   dd=[sum(dc[j]*comb(j,t)*K**(j-t) for j in range(t,len(dc))) for t in range(len(dc))]
   assert all(c>0 for c in dd)
   shifts[K]=(nm,dd)
  return shifts[K]
 for index,rr in enumerate(rootrows,1):
  lo,hi=map(F,rr['interval']);lim=interval_poly(limits,lo,hi);sign=1 if lim[0]>0 else -1;lower=absolute_lower(lim);finite=[]
  for k0 in range(2,11):
   iv=interval_poly(small[k0],lo,hi);lb=absolute_lower(iv);lower=min(lower,lb);finite.append(dict(k=k0,lower=str(iv[0]),upper=str(iv[1])))
  s=dyadic_below(lower/10);tail=None
  for K in [11,16,24,32,48,64,96,128,256,512,1024,2048,4096]:
   nm,dd=shift(K);bounds=[]
   for t,co in enumerate(nm):
    nl,nu=interval_poly(co,lo,hi);nl,nu=(nl,nu) if sign==1 else (-nu,-nl);dv=dd[t] if t<len(dd) else F(0);bounds.append((nl-s*dv,nu-s*dv))
   if all(x[0]>=0 for x in bounds) and bounds[0][0]>0:
    tail=(K,nm,dd);break
  assert tail is not None,('no positive tail certificate',index)
  K,nm,dd=tail
  for k0 in range(11,K):
   dl=fixed_den(k0);assert dl>0;iv=interval_poly(fixed_coeff(k0),lo,hi);iv=(iv[0]/dl,iv[1]/dl);lb=absolute_lower(iv);lower=min(lower,lb);finite.append(dict(k=k0,lower=str(iv[0]),upper=str(iv[1])))
  s=min(s,dyadic_below(lower/10));tailbounds=[]
  for t,co in enumerate(nm):
   nl,nu=interval_poly(co,lo,hi);nl,nu=(nl,nu) if sign==1 else (-nu,-nl);dv=dd[t] if t<len(dd) else F(0);lb,ub=nl-s*dv,nu-s*dv;assert lb>=0
   tailbounds.append(dict(degree=t,lower=str(lb),upper=str(ub)))
  row=dict(root_index=index,root_interval=rr['interval'],root_approx=rr['approx'],sigma_infinity_interval=list(map(str,lim)),uniform_response_lower_bound=str(s),uniform_response_lower_bound_approx=float(s),tail_from_k=K,tail_sign=sign,finite_responses=finite,tail_target_coefficient_bounds=tailbounds,shifted_denominator_coefficients=list(map(str,dd)))
  rows.append(row);(root/'verification/response_bounds.partial.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n');print(json.dumps(dict(root_index=index,s=str(s),tail_from_k=K,elapsed_s=time.monotonic()-start)),flush=True)
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
 (root/'verification/response_bounds.json').write_text(json.dumps(result,indent=2)+'\n');(root/'sources/period_five_response_bounds.py').write_bytes(Path('code/period_five_response_bounds.py').read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};(root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as e:
 import traceback
 fail=dict(error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)],actual_elapsed_s=time.monotonic()-start)
 (root/'verification/BOUND_FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
