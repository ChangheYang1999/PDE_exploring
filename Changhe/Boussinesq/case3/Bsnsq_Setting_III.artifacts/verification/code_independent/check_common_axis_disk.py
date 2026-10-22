#!/usr/bin/env python3
"""Own symbolic identities and exact manufactured continuation tests."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import time,json,hashlib
import sympy as S
import check_all_order_fraction_jets as arithmetic
from check_all_order_fraction_jets import Jet
V=Path('research/326_common_axis_disk/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def ck(n,v,d=None):checks.append(dict(name=n,passed=bool(v),detail=d))
s,C,k,n=S.symbols('s C k n');B=s+k*s**2-C*k*s**13/260;b=B/s
q=(8+2*S.diff(B,s))/B;h=(5+S.diff(B,s))/B
ck('tau_regular_identity',S.cancel(q-10/s-(-6*k-4*C*k*s**11/65)/b)==0)
ck('upsilon_regular_identity',S.cancel(h-6/s-(-4*k-7*C*k*s**11/260)/b)==0)
ck('thermal_homogeneous',S.cancel(n*q-(8*n+2*n*S.diff(B,s))/B)==0)
ck('vorticity_homogeneous',S.cancel(n*q+h-((2*n+1)*(4+S.diff(B,s))+1)/B)==0)
ck('determinant',S.cancel((12*C*k/(5*(2*n+1)))*(-9*C*k/(10*n))+54*C**2*k**2/(25*n*(2*n+1)))==0)
arithmetic.WIDTH=120
for m in [0,1,6,20,26,80]:
 for power in [1,2,3]:
  # Disk |s|<1/2: b,u and the denominator of f have no zeros.
  bb=Jet({1:1,2:-F(1,4)});z=Jet({0:1,1:1})**power;z=z.shift(m)
  f=Jet({0:1})/Jet({0:1,1:-F(1,3)})+Jet({3:1})
  hh=bb*z.der()/z;g=bb*f.der()-hh*f;qj=g/(bb*z)
  key=f'm{m}_u{power}'
  ck(key+'_residue_zero',qj.at(-1)==0,str(qj.at(-1)))
  particular=z*qj.primitive();constant=(f/z).at(0);delta=f-particular-constant*z
  bad=[(e,str(delta.at(e)))for e in range(min(0,delta.val()),delta.high)if delta.at(e)]
  ck(key+'_reconstruct',not bad,dict(known_high=delta.high,first_nonzero=bad[:2]))
  neg=(g+bb*z/Jet({1:1}))/(bb*z)
  ck(key+'_negative_log_residue',neg.at(-1)==1,str(neg.at(-1)))
  ck(key+'_analytic_particular',particular.val()>=0)
# A concrete rational radius below the displayed R, tested without roots.
for cc,kk in [(F(1),F(-1)),(F(2),F(1,2)),(F(-3),F(2)),(F(10**9),F(1,10)),(F(1,10**9),F(-10**9))]:
 r=min(F(1),1/(4*abs(kk)),1/(4*(abs(cc*kk)+1)))
 ck('positive_radius_'+str((cc,kk)),r>0)
 ck('strict_uniform_bound_'+str((cc,kk)),abs(kk)*r+abs(cc*kk)*r**12/260<F(1,2))
frozen=json.loads((V/'freeze.json').read_text());ck('proof_precedes_control',frozen['utc']<start)
r=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Supplementary exact identities and manufactured scalar cases; proof supplies general continuation. No transverse convergence.')
(V/'checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='checks'},indent=2));print('FAILED',[x for x in checks if not x['passed']])
