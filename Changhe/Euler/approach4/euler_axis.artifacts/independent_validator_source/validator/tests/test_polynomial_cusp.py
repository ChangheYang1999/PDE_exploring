#!/usr/bin/env python3
"""Independent cusp coefficient and derivative-aware approximation checks."""
from pathlib import Path
from datetime import datetime,timezone
import time
import numpy as np
from numpy.polynomial import Chebyshev
import mpmath as mp
from independent_artifacts import atomic_json,sha256
R=Path(__file__).resolve().parents[1]

def coefficients(p,N):
    c=np.zeros(N+1);a=float(2**(1-p)*mp.gamma(p+1)/mp.gamma(p/2+1)**2);c[0]=a/2
    for n in range(N//2):
        a*= (p/2-n)/(p/2+n+1);c[2*n+2]=a
    return c

def main():
 start=time.perf_counter();rows=[];mp.mp.dps=65
 def check(name,error,tol):
  err=float(np.max(abs(np.asarray(error))))
  if not np.isfinite(err) or err>tol:raise AssertionError((name,err,tol))
  rows.append(dict(name=name,error=err,tolerance=tol))
 for p in [.5,2.5,3.5]:
  c=coefficients(p,12)
  for n in range(7):
   exact=4/mp.pi*mp.quad(lambda t:mp.cos(t)**mp.mpf(str(p))*mp.cos(2*n*t),[0,mp.pi/2])
   test=2*c[0] if n==0 else c[2*n]
   check(f'coefficient p{p} n{n}',float(exact)-test,3e-15)
 records=[];points=np.r_[np.linspace(-1,1,4097),0.]
 p=2.5
 for N in [16,32,64,128,256,512]:
  S=Chebyshev(coefficients(p,N));g=Chebyshev(p*(p-1)*coefficients(p-2,N));V=g.integ(2,lbnd=0)
  P=Chebyshev((p+1)*p*(p-1)*coefficients(p-2,N)).integ(3,lbnd=0)
  value=abs(S(0));second=abs(g(0));actual_value=np.max(abs(S(points)-abs(points)**p))
  # For these exponents the absolute coefficient-tail bound is attained at zero.
  check(f'value max N{N}',actual_value-value,2e-13)
  err2=np.max(abs(g(points)-p*(p-1)*abs(points)**(p-2)))
  check(f'second derivative max N{N}',err2-second,2e-12)
  check(f'integrated derivative N{N}',V.deriv(2)(points)-g(points),2e-12)
  check(f'potential third derivative N{N}',P.deriv(3)(points)-(p+1)*g(points),5e-11)
  check(f'zero matching N{N}',[V(0),V.deriv()(0),P(0),P.deriv()(0),P.deriv(2)(0)],2e-12)
  raw=float(S.deriv(2)(1));previous=float(Chebyshev(coefficients(p,N-2)).deriv(2)(1))
  expected=S.coef[-1]*N*N*(N*N-1)/3
  check(f'endpoint increment N{N}',(raw-previous-expected)/(1+abs(expected)),2e-12)
  records.append(dict(degree=N,value_error=value,integrated_C2_dominant_error=second,raw_endpoint_second_derivative=raw,true_endpoint_second_derivative=p*(p-1),raw_endpoint_increment=raw-previous))
 for previous,current in zip(records,records[1:]):
  current['value_rate']=float(np.log2(previous['value_error']/current['value_error']))
  current['C2_rate']=float(np.log2(previous['integrated_C2_dominant_error']/current['integrated_C2_dominant_error']))
 check('asymptotic value rate',records[-1]['value_rate']-2.5,.02)
 check('asymptotic C2 rate',records[-1]['C2_rate']-.5,.005)
 if abs(records[-1]['raw_endpoint_increment'])<abs(records[-2]['raw_endpoint_increment']):raise AssertionError('endpoint increment did not grow')
 record=dict(completed_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,case_count=len(rows),checks=rows,records=records,wall_seconds=time.perf_counter()-start,source_sha256=sha256(Path(__file__)),proof_sha256=sha256(R.parent/'research/polynomial_cusp/PROOF.md'))
 atomic_json(R/'results/polynomial_cusp_tests.json',record)
 print({k:record[k] for k in ['all_passed','case_count','wall_seconds']})
if __name__=='__main__':main()
