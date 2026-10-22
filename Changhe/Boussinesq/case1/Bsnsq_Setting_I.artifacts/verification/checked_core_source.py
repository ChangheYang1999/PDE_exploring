"""Bind exact JSON to one NPZ byte string, with a source-text-backed schema.

No fitter is imported. This checker supplements the archived original importer.
"""
from pathlib import Path
from fractions import Fraction as F
from io import BytesIO
import hashlib,json
import numpy as np
from core_generating_mp import ALLOWED

# These keys occur only in archived fit/grid/save code, not Model.basis_jets.
METADATA=set('hist Nt Ns tmin gauge l gpu_port init nmin n2'.split())
REQUIRED=set('c a0 J Kw m beta alpha se gam'.split())
ACCEPTED=REQUIRED|METADATA|{'cc','core'}

def digest(b):return hashlib.sha256(b).hexdigest()
def exact(x):return str(F(float(x)))

def bind(path,certificate=True):
    path=Path(path);raw=path.read_bytes();data=json.loads(raw);source=Path(data['source']);b=source.read_bytes()
    if digest(b)!=data['source_sha256']:raise ValueError('source bytes mismatch')
    with np.load(BytesIO(b),allow_pickle=False) as z:
        if set(z.files)-ACCEPTED or REQUIRED-set(z.files):raise ValueError('unreviewed schema keys')
        for k in ('J','Kw','m'):
            if z[k].shape!=() or z[k].dtype!=np.dtype('int64'):raise ValueError(('integer scalar',k))
        for k in ('a0','beta','alpha','se','gam'):
            if z[k].shape!=() or z[k].dtype!=np.dtype('float64') or not np.isfinite(z[k]):raise ValueError(('real scalar',k))
        if z['m']!=3 or z['beta']!=3 or z['gam']!=0 or z['alpha']<=0 or z['se']<=0 or z['a0']==0:raise ValueError('unsupported or degenerate source')
        J,K=int(z['J']),int(z['Kw'])
        def array(k):
            v=z[k]
            if v.dtype!=np.dtype('float64') or not np.isfinite(v).all():raise ValueError(('coefficient dtype',k))
            return v
        c=array('c')
        if J<0 or K<0 or c.shape!=((J+1)*(K+1),):raise ValueError('outer shape')
        rebuilt={'source':data['source'],'source_sha256':digest(b),'schema':'beta3 alpha-positive gam0 exact dyadic generating function; n/k outer; patch/i/j core',
            's':exact(z['se']),'alpha':exact(z['alpha']),'a':exact(z['a0']),'outer':[[exact(v) for v in row] for row in c.reshape(J+1,K+1)],'patches':[]}
        if ('cc' in z.files)!=('core' in z.files):raise ValueError('missing patch metadata')
        if 'core' in z.files:
            cc,core=array('cc'),array('core')
            if cc.ndim!=1 or core.ndim!=2 or core.shape[1]!=4:raise ValueError('patch layout')
            offset=0
            for n,m,R,L in core:
                if n<0 or m<0 or n!=int(n) or m!=int(m) or R<=0 or L<=0:raise ValueError('patch parameters')
                n,m=int(n),int(m);size=(n+1)*(m+1)
                if offset+size>len(cc):raise ValueError('patch length')
                v=cc[offset:offset+size].reshape(n+1,m+1);offset+=size
                rebuilt['patches'].append({'R':exact(R),'L':exact(L),'coefficients':[[exact(q) for q in row] for row in v]})
            if offset!=len(cc):raise ValueError('extra patch coefficients')
        keys=sorted(z.files)
    if rebuilt!=data:raise ValueError('JSON does not represent the pinned NPZ bytes')
    certpath=path.with_name('certificate.json')
    if certificate:
        cert=json.loads(certpath.read_text())
        if cert['input_sha256']!=digest(raw):raise ValueError('center certificate input binding')
    return data,{'source_sha256':digest(b),'input_sha256':digest(raw),'keys':keys,'metadata_keys':sorted(set(keys)&METADATA),'source_read':'loaded and hashed the identical byte string','checker_file':str(Path(__file__).resolve()),'checker_sha256':digest(Path(__file__).read_bytes())}
