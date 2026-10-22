"""Read-only audit of teammate inverse endpoint formulas; outputs only here."""
import os,sys,importlib.util,json,hashlib
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
BASE=Path(__file__).resolve().parents[3]
source=Path('numerics/src/inverse.py')
spec=importlib.util.spec_from_file_location('numerics_inverse_read_only',source);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
obj=object.__new__(mod.ModalInverse);obj.p=6
rows=[]
for off in (-2,-1,1,2):
    weights=obj._shifted_weights(np.array([0.]),0.,off)[0]
    actual=np.arange(6)-(6//2-1)+off
    got=float(weights@actual)
    rows.append({'offset':off,'computed_integral_of_actual_linear_data':got,'exact_integral':0.5,'predicted_wrong_result':0.5+2*off})
    assert abs(got-(.5+2*off))<1e-10 and abs(got-.5)>1
# rho=x^2*y gives rho_x=r^2 sin(2theta) exactly to leading order.
# Hence .5*integral_0^r0 f1(s)/s ds = f1(r0)/4, not f1(r0)/6.
r0=1e-4
head_wrong=r0*r0/6;head_right=r0*r0/4
out={'utc':datetime.now(timezone.utc).isoformat(),'source_path':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'shift_tests':rows,'head_formula':{'f1_power':2,'correct_full_strain_head_factor':0.25,'implemented_factor':1/6,'error_implemented_minus_correct_at_r0_1e-4':head_wrong-head_right},'verdict':'REFUTED: wrong head exponent for c and wrong sign of shifted interpolation offset. Interior recurrence and actual velocity signs are not refuted by these tests.'}
(BASE/'research/numerics_audit/evidence/inverse_endpoint_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
