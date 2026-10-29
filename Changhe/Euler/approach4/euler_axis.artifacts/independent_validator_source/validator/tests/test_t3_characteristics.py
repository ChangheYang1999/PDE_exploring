from pathlib import Path
import datetime, json, time, shutil
import numpy as np
import sympy as sp
from t3_characteristics import jets,profile,transport_points,axis_reference
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();rows=[]
def check(name,error,tol):
    ok=bool(float(error)<=tol);rows.append({'name':name,'error':float(error),'tolerance':tol,'passed':ok})
    print(name,float(error),'PASS' if ok else 'FAIL',flush=True)
    if not ok:raise AssertionError(name)
u,c,m=sp.symbols('u c m');F=(-(c+m)/2+(-2-3*c+m)*u+(2-(c+m)/2)*u*u)/(1+u)**3
P=c*u**4+(7*c-m+4)*u**3/2+(-c+11*m-32)*u**2/2+(21*c-11*m+12)*u/2+(3*c+m)/2
check('radial_numerator',int(sp.simplify((c-F-2*u*sp.diff(F,u))*(1+u)**4-P)!=0),0)
check('axis_factor',int(sp.simplify((c+2*F)*(1+u)**3-(u-1)*(c*u*u+(4+3*c-m)*u+m))!=0),0)
expected=[[sp.Rational(13,10),sp.Rational(13,15),sp.Rational(3,5)],
          [sp.Rational(7,5),sp.Rational(8,5),sp.Rational(3,5)],
          [sp.Rational(309,200),sp.Rational(96,25),sp.Rational(37,50)],
          [sp.Rational(99,50),sp.Rational(96,25),sp.Rational(37,50)]]
x=sp.symbols('x');i=0
for cc in [sp.Rational(3,5),sp.Rational(37,50)]:
 for t in [sp.Rational(1,2),sp.Integer(1)]:
  pp=P.subs({c:cc,m:t*(1+cc)})
  mins=[]
  for lo,hi in [(0,1),(1,2)]:
   polynomial=sp.Poly(pp.subs(u,lo+(hi-lo)*x),x)
   b=[sum(polynomial.nth(j)*sp.binomial(v,j)/sp.binomial(4,j) for j in range(v+1)) for v in range(5)]
   mins.append(min(b))
  mins.append(min(sp.Poly(pp.subs(u,2+x),x).all_coeffs()))
  check(f'exact_portrait_corner_{i}',int(mins!=expected[i]),0);i+=1
r,z=sp.symbols('r z');ff=F.subs({u:r*r+z*z,c:sp.Rational(37,50),m:sp.Rational(174,175)})
phi=z*ff
exprs={'phi':phi,'phi_z':sp.diff(phi,z),'br':2*sp.diff(phi,z,r),'bz':2*sp.diff(phi,z,2)}
rr=np.array([.01,.2,1.,4.]);zz=np.array([.03,.7,1.3,3.]);data=jets(rr,zz,.74,2.75)
for name,expr in exprs.items():
 exact=sp.lambdify((r,z),expr,'numpy')(rr,zz);check('symbolic_'+name,np.max(abs(exact-data[name])),2e-13)
for cc,kk in [(.6,2.25),(.68,2.5),(.74,2.75)]:
 zz=np.array([.03,.2,.8,1.,1.4,5.,30.]);rr=np.full(zz.shape,1e-6)
 numerical=transport_points(rr,zz,cc,kk,rtol=2e-11,atol=2e-13)
 ref=np.array([axis_reference(v,cc,kk) for v in zz])
 check(f'axis_h_{cc}_{kk}',np.max(abs(numerical['h']-ref[:,0])),3e-8)
 check(f'axis_e_{cc}_{kk}',np.max(abs(numerical['e']-ref[:,1])),5e-8)
rr=np.array([.1,.7,1.5,4.]);zz=np.array([.2,.8,1.3,3.]);cc=.74;kk=2.75
base=transport_points(rr,zz,cc,kk,rtol=2e-11,atol=2e-13)
step=2e-5
xp=transport_points(rr+step,zz,cc,kk,rtol=2e-11,atol=2e-13)
xm=transport_points(rr-step,zz,cc,kk,rtol=2e-11,atol=2e-13)
zp=transport_points(rr,zz+step,cc,kk,rtol=2e-11,atol=2e-13)
zm=transport_points(rr,zz-step,cc,kk,rtol=2e-11,atol=2e-13)
hr=(xp['h']-xm['h'])/(2*step);hz=(zp['h']-zm['h'])/(2*step)
er=(xp['e']-xm['e'])/(2*step);ez=(zp['e']-zm['e'])/(2*step)
d=jets(rr,zz,cc,kk)
check('h_r_finite_difference',np.max(abs(hr-base['h_r'])),2e-6)
check('h_z_finite_difference',np.max(abs(hz-base['h_z'])),2e-6)
check('q_transport_finite_difference',np.max(abs(rr*d['ar']*hr+zz*d['az']*hz-d['b']*base['h'])),3e-6)
check('eta_transport_finite_difference',np.max(abs((1+cc)*base['e']+rr*d['ar']*er+zz*d['az']*ez-2*base['h']*hz)),3e-6)
fine=transport_points(rr,zz,cc,kk,source_radius=1e-6,rtol=2e-11,atol=2e-13)
for name in ['h','h_r','h_z','e']:check('source_cutoff_'+name,np.max(abs(fine[name]-base[name])),2e-8)
out=ROOT/'results/t3_characteristic_tests.json'
atomic_json(out,{'checks':rows,'all_passed':all(r['passed'] for r in rows),'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_seconds':time.perf_counter()-start,'source_sha256':{str(p.relative_to(ROOT)):sha256(p) for p in [Path(__file__),ROOT/'src/t3_characteristics.py']}})
shutil.copyfile(out,ROOT.parent/'research/t3_rational_transport/verification/tests.json')
print(json.dumps({'all_passed':True,'checks':len(rows),'wall_seconds':time.perf_counter()-start}))
