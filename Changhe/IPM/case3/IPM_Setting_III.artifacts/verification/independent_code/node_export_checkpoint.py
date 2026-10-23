"""Validated atomic phase snapshots shared by production and restart manufactures."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np

now=lambda:datetime.now(timezone.utc).isoformat()
SHAPES={'velocity':(2,),'Phi':(),'dV2dy':(),'tail_velocity':(2,),'metadata':(10,),'residual':(5,),'decomposition':(2,8)}

class PhaseStore:
 def __init__(self,path,label,indices,rule,bindings,columns):
  self.path=Path(path);self.label=label;self.indices=np.asarray(indices,dtype=np.int64);self.n=len(indices);self.rule=rule;self.bindings=bindings;self.columns=columns;self.done=0;self.started=now();self.arr={'indices':self.indices.copy(),**{k:np.full((self.n,)+shape,np.nan)for k,shape in SHAPES.items()}}
  if self.path.exists():
   with np.load(self.path,allow_pickle=False)as f:
    if set(f.files)!=set(self.arr)|{'manifest'}:raise ValueError('wrong snapshot members')
    meta=json.loads(str(f['manifest']));old={k:f[k]for k in self.arr}
   if meta['bindings']!=bindings or meta['rule']!=rule or meta['phase']!=label or meta['columns']!=columns:raise ValueError('snapshot binding/rule/phase/schema mismatch')
   if old['indices'].dtype!=np.dtype('int64')or not np.array_equal(old['indices'],self.indices):raise ValueError('snapshot index mismatch')
   if type(meta['completed'])is not int or not 0<=meta['completed']<=self.n:raise ValueError('invalid completed count')
   self.done=meta['completed'];self.started=meta['phase_started_utc']
   if meta['total']!=self.n or meta['exact_identity_count']!=4*self.done or meta['status']!=('COMPLETE'if self.done==self.n else'RUNNING'):raise ValueError('snapshot count/status mismatch')
   for k,shape in SHAPES.items():
    z=old[k]
    if z.dtype!=np.dtype('float64')or z.shape!=(self.n,)+shape:raise ValueError('snapshot array shape/dtype '+k)
    prefix=z[:self.done]
    if k=='residual':
     if not np.isfinite(prefix[:,:3]).all():raise ValueError('nonfinite residual prefix')
     for j,den in [(3,1),(4,2)]:
      if not np.array_equal(np.isnan(prefix[:,j]),prefix[:,den]==0)or np.isinf(prefix[:,j]).any():raise ValueError('invalid residual ratio prefix')
    elif not np.isfinite(prefix).all():raise ValueError('nonfinite prefix '+k)
    if not np.isnan(z[self.done:]).all():raise ValueError('nonempty suffix '+k)
   self.arr=old
 def save(self):
  meta=dict(status='COMPLETE'if self.done==self.n else'RUNNING',phase=self.label,phase_started_utc=self.started,updated_utc=now(),completed=self.done,total=self.n,rule=self.rule,bindings=self.bindings,columns=self.columns,exact_identity_count=4*self.done,scope='Finite auxiliary inverse snapshot, not certified.')
  tmp=self.path.with_suffix(self.path.suffix+'.tmp')
  with tmp.open('wb')as f:np.savez_compressed(f,manifest=json.dumps(meta),**self.arr)
  tmp.replace(self.path)
 def run(self,compute,after_checkpoint=None):
  if self.done:
   i=int(self.indices[self.done-1]);z=compute(i)
   for k in SHAPES:
    if not np.array_equal(self.arr[k][self.done-1],np.asarray(z[k]),equal_nan=True):raise ValueError('replayed boundary row differs '+k)
  if self.done==self.n:return self.arr
  for pos in range(self.done,self.n):
   i=int(self.indices[pos]);z=compute(i)
   if set(z)!=set(SHAPES):raise ValueError('wrong compute row schema')
   for k in SHAPES:self.arr[k][pos]=z[k]
   self.done=pos+1
   if self.done%32==0 or self.done==self.n:
    self.save()
    if after_checkpoint is not None:after_checkpoint(self.done,i)
  return self.arr

def write_or_validate_selection(path,data):
 path=Path(path)
 if path.exists():
  old=json.loads(path.read_text());drop=lambda d:{k:v for k,v in d.items()if k!='generated_utc'}
  if drop(old)!=drop(data):raise ValueError('selection changed, including baseline hash')
 else:
  tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n');tmp.replace(path)
