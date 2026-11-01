"""Numerical proposals, followed by exact rational supersolution certificates."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
import sympy as sp
import mpmath as mp
from general_component_radius import Majorant, certificate, stringify
root=Path('research/140_sharper_period_five_radii');start=time.monotonic();mp.mp.dps=60
z=sp.Symbol('z');Y=sp.symbols('W V1 V2 V3 V4 E');U=sp.symbols('u0:6')

def rat(v):return sp.Rational(v.numerator,v.denominator)
def mpf(v):return mp.mpf(v.numerator)/v.denominator

def put(name,d): (root/'verification'/name).write_text(json.dumps(stringify(d),indent=2)+'\n')
try:
 inputs=json.loads(Path('research/139_period_five_response_minima/verification/checks.json').read_text())['rows']
 alist=[F(149,100),F(1049,1000),F(563,500),F(1213,1000),F(329,250),F(39,25)];rows=[]
 for inp,a in zip(inputs,alist):
  index=inp['root_index'];lo,hi=map(F,inp['root_interval']);s=F(inp['simple_uniform_lower_bound'])
  assert 1+max(abs(lo),abs(hi))<a and 0<s<F(inp['minimum_interval'][0])
  m=Majorant(5,a,F(156,5),s);base=certificate('base',5,a,F(156,5),s)
  phi=sp.Matrix(m.phi(z,list(Y)));T=sp.Matrix([[rat(v) for v in row] for row in m.T]);J=sp.Matrix([[rat(v) for v in row] for row in m.J]);c=sp.Matrix([rat(v) for v in m.constant]);Y0=sp.Matrix([rat(v) for v in m.Y0])
  G=Y0+T*(phi-c-J*sp.Matrix(Y));normalized=[sp.expand(G[j].subs(dict(zip(Y,[Y0[q]*U[q] for q in range(6)])))/Y0[j]) for j in range(6)]
  fn=sp.lambdify((z,*U),normalized,'mpmath')
  def solve(zz,tol=mp.mpf('1e-40'),steps=2500):
   u=[mp.mpf(0)]*6
   for it in range(steps):
    v=fn(zz,*u)
    if max(v)>mp.mpf('1e8'):return None,it+1
    err=max(abs(v[j]-u[j])/max(1,abs(v[j])) for j in range(6));u=v
    if err<tol:return u,it+1
   return None,steps
  low=mpf(base['z0']);sol,it=solve(low);assert sol is not None
  high=2*low;trials=[]
  while True:
   sol,it=solve(high,tol=mp.mpf('1e-22'),steps=1800);trials.append(dict(z_approx=mp.nstr(high,24),iterations=it,settled=sol is not None))
   if sol is None:break
   low=high;high*=2
  for _ in range(26):
   middle=(low+high)/2;sol,it=solve(middle,tol=mp.mpf('1e-22'),steps=1800)
   if sol is None:high=middle
   else:low=middle
  z0=F(mp.nstr(low*mp.mpf('0.99'),40));proposal=mpf(z0)*mp.mpf('1.001');u,it=solve(proposal);assert u is not None
  box=[F(mp.nstr(u[j]*mpf(m.Y0[j]),45)) for j in range(6)]
  values=m.phi(z0,box);margins=[box[j]-values[j] for j in range(6)];assert all(v>0 for v in margins)
  r_approx=mpf(z0)**(-mp.mpf(5)/2);exponent=int(mp.floor(mp.log10(r_approx)));unit=10**max(0,exponent-2);display=int(mp.ceil(r_approx/unit))*unit
  radius_test=F(display)**2*z0**5;assert radius_test>1
  row=dict(root_index=index,a=a,response_lower=s,z0=z0,box=box,Phi_on_box=values,positive_margins=margins,relative_margins=[margins[j]/box[j] for j in range(6)],radius_approx=mp.nstr(r_approx,40),display_radius=display,radius_test=radius_test,proposal_iterations=it,base_dyadic_radius_power=base['exterior_radius_power'],doubling_trials=trials)
  rows.append(row);put('checks.partial.json',dict(rows=rows));print(json.dumps(dict(root=index,radius=row['radius_approx'],display=display,iterations=it,elapsed_s=time.monotonic()-start)),flush=True)
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start);put('checks.json',result)
 for name in ['sharper_period_five_radii.py','general_component_radius.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};put('MANIFEST.json',dict(files=files))
 print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
 import traceback
 fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start);put('FAILURE.json',fail);print(json.dumps(fail),flush=True);raise SystemExit(1)
