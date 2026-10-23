"""Isolated absolute-loss validation utilities; numerical imports are guarded."""
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'base'
OUT=ROOT/'results'
sys.dont_write_bytecode=True
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Absolute-loss numerical work requires the verified supervisor')
sys.path.insert(1,str(BASE))
import numpy as np
import scipy
import scipy.linalg
from threadpoolctl import threadpool_info


def read(path):return json.loads(Path(path).read_text())


def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()


def atomic(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.partial')
    with tmp.open('w') as f:
        json.dump(value,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
    tmp.replace(path)


def npz(path,**arrays):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.partial')
    with tmp.open('wb') as f:
        np.savez_compressed(f,**arrays);f.flush();os.fsync(f.fileno())
    tmp.replace(path)


def array_hash(value):return hashlib.sha256(np.ascontiguousarray(value,dtype='<f8').tobytes()).hexdigest()


def provenance():
    import platform,psutil
    return {'epoch':time.time(),'host':platform.node(),'machine':platform.machine(),
            'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
            'nice':psutil.Process().nice(),'threadpools':threadpool_info(),
            'resource_session':os.environ['IPM_RESOURCE_SESSION'],
            'resource_run':os.environ.get('IPM_RESOURCE_RUN')}


def sources():
    return {'new_sources':{p.name:digest(p) for p in sorted(ROOT.glob('*.py'))},
            'base_manifest_sha256':digest(ROOT/'provenance/base_manifest.json'),
            'candidate_index_sha256':digest(ROOT/'inputs/candidates.json')}


def load_case(label):return read(ROOT/'inputs'/((label if label.endswith('.json') else label+'.json')))


A_REF=read(ROOT/'inputs/candidates.json')['a_ref']
assert A_REF>0
