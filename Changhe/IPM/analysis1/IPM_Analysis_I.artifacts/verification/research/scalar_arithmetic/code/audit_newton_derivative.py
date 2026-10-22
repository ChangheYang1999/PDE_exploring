"""Read-only actual source function test of the Newton denominator identity."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from types import SimpleNamespace
import numpy as np
BASE=Path(__file__).resolve().parents[3];NUM=BASE.parent/'ipmA-num';E=BASE/'research/scalar_arithmetic/evidence'
sys.path.insert(0,str(NUM/'src'))
from cert_scalars2 import axis_tms,tm_eval
from cert_resid import TMArr
from midrad import MR
Q=12;zero=TMArr(MR.exact(np.zeros((1,Q+1))),np.zeros(1));ta=MR.exact(1.)
fake=SimpleNamespace(Q=Q,n=np.array([1]),M=0,c_l=MR.exact(.5))
fake._last_tms=dict(A=zero,B=zero,psi=zero,Rj=zero,Rtj=zero,hpow=np.array([.0005**i for i in range(40)]),h_up=.0005,e_ta=ta)
fake.cell=lambda ci:None
T=axis_tms(fake,0);at0=MR.exact(np.array([0.]))
F=tm_eval(T['xV1'],at0);D=tm_eval(T['xdV1'],at0)
# Exact manufactured physical functions: psi=0, V1=x/2, xV1=e^{2t}/2.
# Therefore d_t(xV1)(0)=1, but x d_tV1(0)=1/2.
assert float(D.upper()[0])<1
actual_path=NUM/'src/cert_scalars2.py';snap=E/'cert_scalars2_snapshot.py';snap.write_bytes(actual_path.read_bytes())
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'REFUTED as derivative of xV1 used in interval Newton; no actual root numerical value refuted by this test','method':'Actual read-only axis_tms on an exact zero-stream field, analytic differentiation of xV1','source_sha256':hashlib.sha256(actual_path.read_bytes()).hexdigest(),'F_xV1_at_0':[float(F.lower()[0]),float(F.upper()[0])],'supplied_derivative_at_0':[float(D.lower()[0]),float(D.upper()[0])],'true_derivative_exact':'1','identity':'d_t(xV1)=xV1+x*d_tV1; code supplies only the second term','note':'A manufactured coefficient test of an algebraic derivative claim, not a candidate satisfying all nonlinear normalization constraints. Code use is generic; the missing term identity also holds for the actual trial.'}
(E/'newton_derivative_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
