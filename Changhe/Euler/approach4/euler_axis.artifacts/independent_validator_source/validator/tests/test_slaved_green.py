#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import os,sys,time
import numpy as np
from scipy.optimize import least_squares
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'exploration'))
from slaved_green import SlavedGreen
from eta_green_basis import EtaGreenField
from coefficient_tail import saved_powers,at_power
from independent_farfield import angular_data
from independent_artifacts import atomic_json,sha256

def main():
 start=time.perf_counter();rows=[];rng=np.random.default_rng(694941)
 def check(name,error,tol):
  e=float(np.max(abs(np.asarray(error))))
  if not np.isfinite(e) or e>tol:raise AssertionError((name,e,tol))
  rows.append(dict(name=name,error=e,tolerance=tol))
 for cl in [.6,2/3,.74]:
  for m in [2,4]:
   p=SlavedGreen(cl,2,angular=m,radial=3,correction=1,nradial=13,nangle=16)
   check(f'rank {cl} {m}',len(p.singular_values)-5,0)
   x=p.seed();x+=.02*rng.normal(size=len(x));c,J=p.coefficients(x,True)
   check(f'constraint {cl} {m}',p.C@c-p.target,2e-10)
   check(f'tangent {cl} {m}',p.C@J,2e-10)
   L=x[:p.nleading];check(f'quadratic map {cl} {m}',p.forced(L)-p.forced_direct(L),2e-10)
   check(f'homogeneity {cl} {m}',p.forced(1.7*L)-1.7**2*p.forced(L),2e-10)
   field=p.field(x);pp,qq,_=saved_powers(field,2*p.alpha+1,2*p.alpha+2)
   data=angular_data(p.alpha,at_power(pp,p.alpha),at_power(qq,p.alpha+1));nodes=np.linspace(-1,1,61)
   check(f'stream correction {cl} {m}',at_power(pp,2*p.alpha+1)(nodes)-data['A1'](nodes),2e-9)
   check(f'swirl correction {cl} {m}',at_power(qq,2*p.alpha+2)(nodes)-data['B1'](nodes),2e-9)
   rq,re=p.raw(x);other=field.reduced(p.r,p.z)
   check(f'q direct {cl} {m}',(rq-other['q'])/(1+np.max(abs(rq))),3e-11)
   check(f'eta direct {cl} {m}',(re-other['eta'])/(1+np.max(abs(re))),3e-11)
   v=rng.normal(size=len(x));v/=np.linalg.norm(v);h=1e-5
   check(f'coefficient JVP {cl} {m}',(p.coefficients(x+h*v)-p.coefficients(x-h*v))/(2*h)-J@v,3e-8)
   j=p.evaluate(x)[1]@v;fd=(p.evaluate(x+h*v)[0]-p.evaluate(x-h*v)[0])/(2*h)
   check(f'residual JVP {cl} {m}',np.linalg.norm(fd-j)/(1+np.linalg.norm(j)),3e-8)
   # Moving only fast null coordinates cannot change leading/correction coefficients.
   y=x.copy();y[p.nleading:]+=.07*rng.normal(size=p.nfree)
   cy=p.coefficients(y)
   check(f'fast tail invariance {cl} {m}',cy[np.r_[p.leading,p.correction_ids]]-c[np.r_[p.leading,p.correction_ids]],0)
   d=p.diagnostic(x);check(f'diagnostic rows {cl} {m}',d['hard_source_defect'],2e-10)
 # A nonzero known root of an offset residual verifies that the nonlinear chart
 # and its Jacobian work together in a solve, without presenting it as Euler.
 p=SlavedGreen(.68,1.,angular=2,radial=3,correction=1,nradial=17,nangle=20,regularization=1e-3)
 target=p.seed()+.01*rng.normal(size=p.nvar);f0=p.evaluate(target)[0]
 fit=least_squares(lambda x:p.evaluate(x)[0]-f0,target+.002*rng.normal(size=p.nvar),jac=lambda x:p.evaluate(x)[1],max_nfev=50,gtol=1e-12,ftol=1e-12,xtol=1e-12,x_scale='jac')
 check('forced manufactured residual recovery',np.linalg.norm(fit.fun),1e-9)
 check('forced manufactured coefficient recovery',np.linalg.norm(fit.x-target),1e-6)
 temp=R/'results/slaved_green_roundtrip.json';atomic_json(temp,p.field(target).as_dict());loaded=EtaGreenField.load(temp)
 check('saved coefficients roundtrip',loaded.q.evaluate(p.r*p.r,p.z)-p.field(target).q.evaluate(p.r*p.r,p.z),0)
 files=[Path(__file__),R/'exploration/slaved_green.py',R/'exploration/s1_green_pilot.py',R/'src/coefficient_tail.py',R/'src/independent_farfield.py']
 record=dict(completed_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start,source_sha256={str(f.relative_to(R)):sha256(f) for f in files})
 atomic_json(R/'results/slaved_green_tests.json',record);print({k:record[k] for k in ['all_passed','case_count','elapsed_seconds']})
if __name__=='__main__':main()
