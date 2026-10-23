"""Stage XI numerical shared utilities. Numerical callers require the guard."""
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'
os.environ['IPM_WORK_DIR']=str(ROOT)
sys.dont_write_bytecode=True
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Stage XI numerical work requires the verified hardware supervisor')
sys.path.insert(0,str(ROOT/'engine'))
import numpy as np
import stage10 as e
from c5_chart import C5Chart, constraints, hp_report, hp_values, physical_metric

def read(path):return json.loads(Path(path).read_text())
def atomic(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.partial')
    with tmp.open('w') as f:
        json.dump(value,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
    tmp.replace(path)
def append(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('a') as f:
        f.write(json.dumps(value,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
def npz(path,**arrays):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_name(path.name+'.partial')
    with tmp.open('wb') as f:
        np.savez(f,**arrays);f.flush();os.fsync(f.fileno())
    tmp.replace(path)
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fingerprint(p):return e.a.fingerprint(case(p))
def reference(label):return read(ROOT/'engine/reference_results'/('five.json' if label=='c5start' else 'final.json'))
def parameters(case):return np.r_[case['cl'],case['coefficients'][1:]]
def problem():return e.GridProblem(97)
def case(p,label='state',objectives=None):
    prob=problem();v=e.make(np.asarray(p),prob,label)
    if objectives is not None:v['objectives']=objectives
    v['stage']='XI';v['constraints']='Ex=Ey=D1=D2=D3=0';return v
def objectives(r):
    ji=float(r[:97**2]@r[:97**2]/2);jf=float(r[97**2:]@r[97**2:]/.2)
    return {'J_inner':ji,'J_far':jf,'J_joint':ji+.1*jf,'RMS_inner':float(np.sqrt(2*ji)),'RMS_far':float(np.sqrt(2*jf))}

class Evaluator:
    def __init__(self,phase,state=None):
        self.phase=phase;self.prob=problem();self.state=state
    def fun(self,p,kind='residual'):
        began=time.time()
        if self.state is not None:
            self.state['residual_attempts']=self.state.get('residual_attempts',0)+1
            index=self.state['residual_attempts']
            append(OUT/'evaluation_attempts.jsonl',{'attempt':index,'phase':self.phase,'kind':kind,'event':'started','p':np.asarray(p).tolist(),'epoch':began})
        else:index=None
        r=self.prob.fun(p)
        if self.state is not None:
            self.state['residual_calls']=self.state.get('residual_calls',0)+1
            residual_path=OUT/'evaluations'/('residual_'+str(index).zfill(7)+'.npz')
            npz(residual_path,r=r,p=np.asarray(p))
            append(OUT/'fit_evaluations.jsonl',{'attempt':index,'call':self.state['residual_calls'],'phase':self.phase,'kind':kind,
                'p':np.asarray(p).tolist(),'J':float(r@r/2),'epoch':time.time(),'elapsed':time.time()-began,
                'residual_path':str(residual_path),'residual_sha256':digest(residual_path)})
        else:append(OUT/'diagnostic_evaluations.jsonl',{'phase':self.phase,'kind':kind,'p':np.asarray(p).tolist(),'J':float(r@r/2),'epoch':time.time(),'elapsed':time.time()-began})
        return r
    def jac(self,p):
        if self.state is not None:
            self.state['jacobian_attempts']=self.state.get('jacobian_attempts',0)+1
            append(OUT/'Jacobian_attempts.jsonl',{'attempt':self.state['jacobian_attempts'],'event':'started','p':np.asarray(p).tolist(),'epoch':time.time()})
        j=self.prob.hybrid(p,fun=lambda q:self.fun(q,'Jacobian_cl_probe'),cl_step=e.v.CL_STEP)
        if self.state is not None:
            self.state['jacobian_calls']=self.state.get('jacobian_calls',0)+1
            append(OUT/'Jacobian_attempts.jsonl',{'attempt':self.state['jacobian_attempts'],'event':'complete','call':self.state['jacobian_calls'],'p':np.asarray(p).tolist(),'epoch':time.time()})
        return j

def full_tangent(prob,p,T):
    B,mr,ff,D=physical_metric(prob,p)
    _,sb,vb=np.linalg.svd(B@T,full_matrices=False)
    assert len(sb)==19 and min(sb)>0
    field=T@(vb.T/sb)
    return field,B,mr,ff,D,sb

def chart_tangent(chart,p):
    _,G=constraints(p,True)
    R=np.zeros((24,22));R[chart.free22]=np.eye(22)
    R[chart.zpair]=-np.linalg.solve(G[:2,chart.zpair],G[:2,chart.free22])
    normal=G[2:]@R@chart.e
    T=R@(chart.n-chart.e@np.linalg.solve(normal,G[2:]@R@chart.n))
    return T

def derivative_identity():
    names=['c5_chart.py','stage11_common.py','preflight.py']
    return {'research_sources':{name:digest(ROOT/name) for name in names},
            'engine_sources':{p.name:digest(p) for p in (ROOT/'engine').glob('*.py')},
            'chart_sha256':digest(OUT/'chart.json'),'map_sha256':digest(OUT/'fit_map.json'),
            'preflight_arrays_sha256':digest(OUT/'preflight_arrays.npz')}

def provenance():
    import platform,psutil,scipy
    from threadpoolctl import threadpool_info
    return {'epoch':time.time(),'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
            'threadpools':threadpool_info(),'nice':psutil.Process().nice(),'pid':os.getpid(),
            'source_sha256':{p.name:digest(p) for p in ROOT.glob('*.py')},
            'resource_session':os.environ.get('IPM_RESOURCE_SESSION'),'resource_run':os.environ.get('IPM_RESOURCE_RUN')}
