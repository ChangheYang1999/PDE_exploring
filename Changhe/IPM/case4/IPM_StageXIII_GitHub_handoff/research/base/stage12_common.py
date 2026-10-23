"""Stage XII shared utilities. All numerical imports require the supervisor."""
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
sys.dont_write_bytecode = True
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Stage XII numerical work requires the verified resource supervisor')
os.environ['IPM_WORK_DIR'] = str(ROOT)
sys.path.insert(0, str(ROOT/'engine'))
import numpy as np
import stage10 as e
from c5_chart import hp_report, constraints
from coefficient_normal_chart import CoefficientNormalChart


def read(path):
    return json.loads(Path(path).read_text())


def atomic(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+'.partial')
    with tmp.open('w') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
    tmp.replace(path)


def append(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a') as stream:
        stream.write(json.dumps(value, allow_nan=False)+'\n')
        stream.flush(); os.fsync(stream.fileno())


def npz(path, **arrays):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+'.partial')
    with tmp.open('wb') as stream:
        np.savez_compressed(stream, **arrays)
        stream.flush(); os.fsync(stream.fileno())
    tmp.replace(path)


def digest(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''): value.update(block)
    return value.hexdigest()


def array_hash(value):
    return hashlib.sha256(np.ascontiguousarray(value, dtype='<f8').tobytes()).hexdigest()


def initial_parameters():
    saved = read(ROOT/'inputs/stage11_endpoint.json')
    return np.r_[saved['cl'], saved['coefficients'][1:]]


def chart(p):
    return CoefficientNormalChart(read(OUT/'chart_coefficient_normal.json'), base=np.asarray(p))


def source_identity():
    names = ['stage12_common.py','stage12_model.py','spectral_basis.py',
             'c5_chart.py','continuation_chart.py','coefficient_normal_chart.py']
    paths = [ROOT/name for name in names]+list((ROOT/'engine').glob('*.py'))
    return {str(path.relative_to(ROOT)):digest(path) for path in sorted(paths)}


def provenance():
    import platform, psutil, scipy
    from threadpoolctl import threadpool_info
    return {'epoch':time.time(), 'python':platform.python_version(), 'numpy':np.__version__,
            'scipy':scipy.__version__, 'machine':platform.machine(), 'host':platform.node(),
            'pid':os.getpid(), 'nice':psutil.Process().nice(), 'threadpools':threadpool_info(),
            'resource_session':os.environ['IPM_RESOURCE_SESSION'],
            'resource_run':os.environ.get('IPM_RESOURCE_RUN')}


def objectives(r, n=97):
    ji = float(r[:n*n]@r[:n*n]/2)
    jf = float(r[n*n:]@r[n*n:]/.2)
    return {'J_inner':ji, 'J_far':jf, 'J_joint':ji+.1*jf,
            'RMS_inner':float(np.sqrt(2*ji)), 'RMS_far':float(np.sqrt(2*jf))}


def make_candidate(p, extra, modes, label, result=None):
    p = np.asarray(p)
    prob = e.GridProblem(97)
    case = e.make(p, prob, label)
    case.update(stage='XII', core_parameters=p.tolist(), extra_coefficients=np.asarray(extra).tolist(),
                modes=modes, independent_parameters=24+len(modes), feasible_variables=19+len(modes),
                core_HP=hp_report(p), source_sha256=source_identity())
    if result is not None: case['objectives'] = result
    return case
