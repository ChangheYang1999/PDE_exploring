"""FLOAT independent quadrature check of the Gaussian center asymptotic.
Analytically integrates the radial Gaussian first; not used as a certificate.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,math
from scipy.integrate import quad
from scipy.special import hyp1f1,gamma
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
x=json.loads((BASE/'source_audit/state131_exact.json').read_text())['exact_parameters']
d=float(Q(x['lambda_origin'])-1);sig=float(Q(x['sigma']))
I=math.sqrt(math.pi)*gamma((sig-1)/2)/gamma(sig/2)
expected=2**d*I*gamma(2+d/2)/(gamma(1+d)*math.sin(math.pi*d/2))

def oneminus(x):
 if x<1e-4:return 4*x-4*x*x+32/15*x**3-16/21*x**4
 if x>1e10:return 1-.75/x**2
 return 1-hyp1f1(2,.5,-x)

def compute(y):
 T=-math.log(y)
 def outer(s):
  eps=math.exp(-d*(T+s));e2s=math.exp(2*s)
  def inner(theta):
   co=math.cos(theta);A=1+(eps*math.tan(theta))**2
   return A**(sig/2-2)*co**(sig-2)*oneminus(e2s/A)
  v,err=quad(inner,0,math.pi/2,epsabs=1e-11,epsrel=2e-10,limit=200)
  return math.exp(-d*s)*v
 v,err=quad(outer,-T,25,points=[0],epsabs=1e-9,epsrel=2e-9,limit=200)
 return 4/math.pi*v,4/math.pi*err
rows=[]
for y in [1e-2,1e-4,1e-6,1e-8]:
 value,err=compute(y);rows.append({'y':y,'H_over_y_power':value,'quadrature_error_estimate':err,'limiting_coefficient':expected,'difference':value-expected});print(rows[-1],flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'FLOAT_DIAGNOSTIC','method':'radial Gaussian integral via confluent hypergeometric function, then two-dimensional positive quadrature','rows':rows,'scope':'Independent numerical check only; quadrature error estimates are not rigorous.'}
(HERE/'gaussian_asymptotic_probe.json').write_text(json.dumps(out,indent=2)+'\n')
