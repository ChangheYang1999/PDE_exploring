"""Exact JSON certificate interface for finite binary nodal fields."""
from pathlib import Path
import hashlib,json,math
import numpy as np

def export(source,target):
 source=Path(source).resolve();target=Path(target)
 with np.load(source) as z:
  N=int(z['N']);M=int(z['M']);b=z['b'];assert b.shape==(N+1,M)
  params={k:float(z[k]).hex() for k in ('L','c_l','beta')}
  obj={'schema':'ipm-exact-nodal-binary64-v1','source':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'N':N,'M':M,'parameters':params,'b':[[float(x).hex() for x in row] for row in b]}
  assert all(math.isfinite(float.fromhex(x)) for row in obj['b'] for x in row)
  assert np.array_equal(np.array([[float.fromhex(x) for x in row] for row in obj['b']]),b)
 target.write_text(json.dumps(obj,indent=2)+'\n');return obj

def load(target):
 target=Path(target);raw=target.read_bytes();o=json.loads(raw);assert o['schema']=='ipm-exact-nodal-binary64-v1'
 source=Path(o['source']);assert hashlib.sha256(source.read_bytes()).hexdigest()==o['source_sha256']
 b=np.array([[float.fromhex(x) for x in row] for row in o['b']]);assert b.shape==(o['N']+1,o['M']) and np.isfinite(b).all()
 params={k:float.fromhex(x) for k,x in o['parameters'].items()};assert all(math.isfinite(x) for x in params.values())
 with np.load(source) as z:
  assert np.array_equal(z['b'],b) and all(float(z[k]).hex()==o['parameters'][k] for k in params)
 return o,b,params,hashlib.sha256(raw).hexdigest()
