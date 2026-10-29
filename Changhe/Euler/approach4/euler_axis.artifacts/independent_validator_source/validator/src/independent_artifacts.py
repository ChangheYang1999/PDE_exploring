"""Atomic local artifacts and source identity for independent validation."""
from pathlib import Path
import hashlib,json,os
import numpy as np


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source_identity(root,entrypoint):
    root=Path(root)
    paths=sorted((root/'src').glob('independent_*.py'))+[Path(entrypoint)]
    return {str(p.relative_to(root)):sha256(p) for p in paths}


def verify_source_identity(root,identity):
    changed=[name for name,value in identity.items() if sha256(Path(root)/name)!=value]
    if changed:raise RuntimeError('source changed during validation: '+', '.join(changed))


def atomic_json(path,data):
    path=Path(path);tmp=path.with_suffix(path.suffix+'.tmp')
    with tmp.open('w') as f:
        json.dump(data,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
    tmp.replace(path)


def atomic_npz(path,arrays):
    path=Path(path);tmp=path.with_suffix(path.suffix+'.tmp')
    with tmp.open('wb') as f:
        np.savez_compressed(f,**arrays);f.flush();os.fsync(f.fileno())
    tmp.replace(path)
