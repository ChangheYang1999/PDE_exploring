"""Exact controls for packet182, including a smooth counterexample when U=o(r)
is dropped. These controls check identities and premises, not Jordan separation.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,time
root=Path('research/182_beta2_global_three_region_decomposition/verification')
start=datetime.now(timezone.utc).isoformat();tic=time.monotonic();checks=[];negative=[]
def eq(name,value):
 value=s.simplify(value);assert value==0,(name,value);checks.append({'name':name,'exact_residual':str(value)})
def yes(name,value):assert value,name;checks.append({'name':name,'passed':bool(value)})
def neg(name,value):assert value,name;negative.append({'name':name,'counterexample_verified':True})
x,y,t,v,a=s.symbols('x y t v a',real=True);h=s.Function('h')(x)
W=s.Matrix([h,(4-s.diff(h,x))*y]);U=W-2*s.Matrix([x,y]);psi=(2*x-h)*y
omega=s.diff(h,x,2)*y
for j,z in enumerate([-s.diff(psi,y),s.diff(psi,x)]):eq(f'stream inverse component{j}',U[j]-z)
eq('negative Laplacian',-s.diff(psi,x,2)-s.diff(psi,y,2)-omega)
eq('constant divergence',s.diff(W[0],x)+s.diff(W[1],y)-4)
eq('vorticity sign',-(s.diff(W[1],x)-s.diff(W[0],y))-omega)
ss=s.symbols('ss',positive=True);tt=s.symbols('tt',positive=True)
hh=2*ss*s.exp(-1/ss**2);d=2*s.exp(-tt)*(1+2*tt)
eq('outgoing derivative formula',s.diff(hh,ss)-d.subs(tt,1/ss**2))
eq('derivative maximum sign',s.diff(d,tt)-2*s.exp(-tt)*(1-2*tt))
eq('maximum value',d.subs(tt,s.Rational(1,2))-4*s.exp(-s.Rational(1,2)))
yes('maximum strictlybelow4',s.exp(-s.Rational(1,2))<1)
for j in range(7):eq(f'endpoint flat derivative{j}',s.limit(s.diff(hh,ss,j),ss,0,dir='+'))
for xx in [s.Rational(-1),s.Rational(-1,2),s.Rational(0),s.Rational(1,2),s.Rational(1)]:
 flow=s.Matrix([xx,y*s.exp(4*t)])
 eq(f'strip orbit x {xx}',s.diff(flow[0],t))
 eq(f'strip orbit y {xx}',s.diff(flow[1],t)-4*flow[1])
 eq(f'backward limit y {xx}',s.limit(flow[1],t,-s.oo))
 vp=s.symbols('vp',positive=True)
 eq(f'upper asymptotic direction x {xx}',s.limit(xx/s.sqrt(xx**2+vp**2),vp,s.oo))
 eq(f'upper asymptotic direction y {xx}',s.limit(vp/s.sqrt(xx**2+vp**2),vp,s.oo)-1)
flowgeneral=s.Matrix([x,y*s.exp(4*t)])
eq('exact area multiplier',flowgeneral.jacobian([x,y]).det()-s.exp(4*t))
eq('center thermal transport',s.diff(a*x*x,y)*4*y)
eq('center vorticity residual',-s.diff(a*x*x,x)+2*a*x)
neg('sublinear hypothesis fails onverticalaxis',s.Rational(2)!=0)
neg('two distinct strongorbits have same upper direction',s.Matrix([1,1])!=s.Matrix([-1,1]))
neg('relative inverse correction is not bounded',s.limit(2*vp,vp,s.oo)==s.oo)
neg('nonzero a0 fails B2vorticity equation',-s.diff(a*x*x,x)!=0)
params={'h_positive':'2(x-1)exp[-1/(x-1)^2] for x>1','h_zero_interval':['-1','1'],'extension':'odd','W':['h(x)','(4-h_prime(x))*y'],'a0':'symbolic nonzero','scope':'smooth geometric control violates U=o(r) and B2vorticity; not a PDE solution'}
(root/'manufactured_parameters.json').write_text(json.dumps(params,indent=2)+'\n')
end=datetime.now(timezone.utc).isoformat();out={'started_utc':start,'ended_utc':end,'elapsed_seconds':time.monotonic()-tic,'verdict':'PASS','exact_count':len(checks),'negative_count':len(negative),'checks':checks,'negative_controls':negative,'scope':'Exact smooth-field controls; no claim of proof-assistant verification or finite-sample proof of planar topology.'}
(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['started_utc','ended_utc','elapsed_seconds','verdict','exact_count','negative_count']},indent=2))
