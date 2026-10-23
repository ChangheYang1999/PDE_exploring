"""Manufactures for the complete axis inverse, independent of candidate data."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
from hydrostatic_axis_tail_series import coordinate,velocity,axis_jet,moment
mp.mp.dps=115
R=Path('research/hydrostatic_cusp_row_audit');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
C=mp.mpf(3)/7;P=mp.mpf('1.5')
for j in [1,2,3]:
 k=[mp.mpf(0)]*j+[mp.mpf(1)]
 for tt in [mp.mpf(2),mp.mpf(7),mp.mpf(25),mp.mpf(100)]:
  y=C*tt*(1+tt*tt);w=1/(1+tt*tt);label='j'+str(j)+' tau'+str(tt)
  target={1:3*tt-2*mp.atan(tt),2:2*mp.atan(tt)-tt/(1+tt*tt),3:3*tt/(4*(1+tt*tt))-tt/(2*(1+tt*tt)**2)+3*mp.atan(tt)/4}[j]*C
  check(label+' independent coordinate',abs(coordinate(P,C,y)-w)<mp.mpf('1e-100'))
  for N in [24,64,128]:
   result=velocity(P,C,k,y,N);error=abs(result['V2']-target)
   check(label+' explicit primitive N'+str(N),error<=result['remainder_bound']+mp.mpf('1e-100'),dict(error=mp.nstr(error,12),bound=mp.nstr(result['remainder_bound'],12)))
 expected={1:-mp.pi*C,2:mp.pi*C,3:3*mp.pi*C/8}[j];check('j'+str(j)+' independent moment',abs(moment(k,P,C)-expected)<mp.mpf('1e-100'))
for P in [mp.mpf('1.25'),mp.mpf('1.5'),mp.mpf('1.75')]:
 k=[mp.mpf(0),mp.mpf(3),mp.mpf(-2),mp.mpf(5)/7];H=[mp.mpf(0),mp.mpf(1),mp.mpf(-3)/2,mp.mpf(2)/3]
 for w in [mp.mpf('.01'),mp.mpf('.04'),mp.mpf('.1'),mp.mpf('.25')]:
  y=C*mp.sqrt(1-w)/w**P;label='P'+str(P)+' w'+str(w);mm=moment(k,P,C)
  derivative=mp.diff(lambda t:velocity(P,C,k,t,192,mm)['V2'],y);target=mp.fsum(k[j]*w**j for j in range(len(k)))
  check(label+' velocity derivative',abs(derivative-target)<mp.mpf('1e-95'),mp.nstr(abs(derivative-target),12))
  g,gy=axis_jet(P,C,H,y);direct=mp.diff(lambda t:axis_jet(P,C,H,t)[0],y)
  check(label+' density derivative',abs(gy-direct)<mp.mpf('1e-100'),mp.nstr(abs(gy-direct),12))
  r32=velocity(P,C,k,y,32,mm);r64=velocity(P,C,k,y,64,mm)
  check(label+' series remainder difference',abs(r64['V2']-r32['V2'])<=r32['remainder_bound']+r64['remainder_bound']+mp.mpf('1e-100'))
# Independent symbolic expansion of the normalized residual through its constant term.
import sympy as S
e,K,c2,r2,p,m0=S.symbols('e K c2 r2 p m0');den=2+e
coef1=r2/(K*den)-e*(r2+2*c2)/(K*den**2);coef0=p*m0/den-e*p*m0/den**2
check('binary exponent y^p coefficient',S.simplify(coef1-2*(r2-e*c2)/(K*den**2))==0)
check('binary exponent constant coefficient',S.simplify(coef0-2*p*m0/den**2)==0)
result=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,module_sha256=sha('independent_code/hydrostatic_axis_tail_series.py'),driver_sha256=sha(__file__),proof_sha256=sha(R/'AXIS_TAIL_PROOF.md'))
(V/'AXIS_SERIES_GATE.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count']);print([c for c in checks if not c['passed']])
if result['status']!='PASS':raise SystemExit(1)
