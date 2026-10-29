"""Check reference masking and reject nonfinite independent reconstruction."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from finite_pressure_reference import compare_pressure_reference
checks=[]
def check(name,value):
 checks.append(dict(name=name,passed=bool(value)))
 if not value:raise AssertionError(name)
def rejects(name,fn):
 try:fn()
 except ValueError:check(name,True);return
 raise AssertionError(name)
s={k:np.arange(4,dtype=float)for k in ['r','z','R','mu']};s['P']=np.array([1.,np.nan,3.,np.inf]);p=np.array([2.,7.,1.,8.]);g=np.zeros((4,2))
a=compare_pressure_reference(p,g,s)
check('two finite and two unavailable',a['count']==4 and a['finite_reference_count']==2 and a['unavailable_reference_count']==2)
check('no imputation in maximum',a['max_abs_error']==2 and a['worst_index']==2)
check('no imputation in RMS',a['rms_error']==float(np.sqrt(2.5)))
check('explicit missing indices',a['unavailable_reference_indices']==[1,3])
check('explicit nonfinite kinds',a['reference_nan_count']==1 and a['reference_positive_infinity_count']==1 and a['reference_negative_infinity_count']==0)
check('JSON output finite',json.loads(json.dumps(a,allow_nan=False))==a)
rejects('nonfinite reconstruction rejected',lambda:compare_pressure_reference(np.array([2.,np.nan,1.,8.]),g,s))
rejects('nonfinite gradient rejected',lambda:compare_pressure_reference(p,np.full((4,2),np.inf),s))
rejects('no finite reference rejected',lambda:compare_pressure_reference(p,g,dict(s,P=np.full(4,np.nan))))
rejects('shape mismatch rejected',lambda:compare_pressure_reference(p,g[:3],s))
record=dict(completed_utc=datetime.now(timezone.utc).isoformat(),checks=checks,check_count=len(checks),all_passed=all(x['passed']for x in checks),source_sha256={str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest()for x in [Path(__file__),ROOT/'finite_pressure_reference.py']},scope='Reference comparison bookkeeping; no pressure integral or field residual is computed.')
out=ROOT/'results'/('finite_pressure_reference_tests_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')+'.json');out.write_text(json.dumps(record,indent=2)+'\n');print(out,record['check_count'],record['all_passed'])
