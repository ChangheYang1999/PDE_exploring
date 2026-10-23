"""Independent larger-grid auxiliary node arithmetic and atomic snapshots.
Derivation: research/hydrostatic_larger_node_audit/PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json
import numpy as np

SHAPES={'velocity':(2,),'Phi':(),'dV2dy':(),'tail_velocity':(2,),'metadata':(10,),'residual':(5,)}
REGIONS=['r<.1','.1<=r<1','1<=r<100','r>=100']
now=lambda:datetime.now(timezone.utc).isoformat()
f=lambda x:F.from_float(float(x))

def coordinates(q):
 t=q.tk[1:];r=q.L*np.sqrt((1+t)/2)/(1-t)**q.kappa
 theta=(np.arange(q.M)+.5)*np.pi/(2*q.M)
 return np.column_stack([(r[:,None]*np.cos(theta)).ravel(),(r[:,None]*np.sin(theta)).ravel()])

def exact_fields(x,y,j,v,c=2):
 x,y,c=map(f,(x,y,c));g,gx,gy=map(f,j[:3]);v1,v2=map(f,v)
 a=(c*x+v1)*gx;b=(c*y+v2)*gy;r=a+b-g;nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(v1*gx+v2*gy)
 return [r,nf,nv,abs(r)/nf if nf else None,abs(r)/nv if nv else None]

def rounded_fields(x,y,j,v,c=2):
 exact=exact_fields(x,y,j,v,c)
 try: out=np.array([float(z)if z is not None else np.nan for z in exact])
 except OverflowError as e:raise ValueError('binary64 diagnostic overflow')from e
 if not np.isfinite(out[:3]).all()or any(exact[k]>0 and out[k]==0 for k in [1,2])or any(exact[k]is not None and not np.isfinite(out[k])for k in [3,4]):raise ValueError('binary64 diagnostic representation failure')
 return out

def coordinate_diagnostics(q,xy):
 t=q.tk[1:];radial=q.L*np.sqrt((1+t)/2)/(1-t)**q.kappa
 nominal=np.repeat(radial,q.M);actual=np.hypot(xy[:,0],xy[:,1]);boundaries=[.1,1.,100.]
 return dict(boundaries=boundaries,minimum_nominal_distance=[float(np.min(abs(nominal-b)))for b in boundaries],classification_disagreement_count=int(np.count_nonzero(np.searchsorted(boundaries,nominal,side='right')!=np.searchsorted(boundaries,actual,side='right'))),max_hypot_radial_difference=float(np.max(abs(actual-nominal))),radial_min=float(radial.min()),radial_max=float(radial.max()))

def region_masks(xy):
 r=np.hypot(xy[:,0],xy[:,1]);return [r<.1,(r>=.1)&(r<1),(r>=1)&(r<100),r>=100]

def summaries(xy,rr):
 out=[]
 for name,mask in zip(REGIONS,region_masks(xy)):
  ids=np.flatnonzero(mask);row=dict(region=name,count=len(ids),metrics={})
  for metric,k in [('absR',0),('Rf',3),('Rv',4)]:
   valid=ids[np.isfinite(rr[ids,k])];i=int(valid[np.argmax(abs(rr[valid,k]))])if len(valid)else None
   row['metrics'][metric]=dict(index=i,value=float(abs(rr[i,k]))if i is not None else None,defined_count=len(valid),undefined_count=len(ids)-len(valid))
   if i is not None:row['metrics'][metric].update(x=float(xy[i,0]),y=float(xy[i,1]),fields=[float(v)if np.isfinite(v)else None for v in rr[i]])
  out.append(row)
 return out

def selection(xy,jets,data,fdproxy):
 reasons={}
 def add(i,s):
  if i is not None:reasons.setdefault(int(i),[]).append(s)
 def arg(v,s):
  ids=np.flatnonzero(np.isfinite(v))
  if len(ids):add(ids[np.argmax(v[ids])],s)
 for r in summaries(xy,data['residual']):
  for k,z in r['metrics'].items():add(z['index'],'B '+r['region']+' '+k)
 for k in range(2):arg(abs(data['velocity'][:,k]),'absolute V'+str(k+1))
 arg(abs(jets[:,3]),'absolute gxx');arg(fdproxy,'five-point gxx proxy')
 for k in [1,2,6]:
  arg(data['metadata'][:,k],'metadata maximum '+str(k));arg(-data['metadata'][:,k],'metadata minimum '+str(k))
 for i in [0,len(xy)//2,len(xy)-1]:add(i,'deterministic endpoint/middle')
 return dict(indices=sorted(reasons),reasons={str(i):reasons[i]for i in sorted(reasons)})

def pair_spreads(xy,j,vrows):
 rs=[exact_fields(*xy,j,v)[0]for v in vrows];nf=exact_fields(*xy,j,vrows[1])[1];S=max(rs)-min(rs);base=abs(rs[1]);pairs=[]
 for k in [0,1]:
  for a,b in [(0,1),(2,1),(2,0)]:
   u,v=f(vrows[a][k]),f(vrows[b][k]);d=abs(u-v);den=max(abs(u),abs(v));pairs.append(dict(component=k+1,pair=[a,b],absolute=str(d),pure_relative=str(d/den)if den else None,both_zero=not bool(den)))
 return dict(rule_order=['A','B','C'],R=[str(r)for r in rs],spread=str(S),B_Nf=str(nf),spread_over_abs_B_R=str(S/base)if base else None,spread_over_B_Nf=str(S/nf)if nf else None,zero_B_R=not bool(base),zero_B_Nf=not bool(nf),empirical_pass=bool(S<=base/100 and S<=nf/10**8)if base and nf else None,components=pairs)

class NodeStore:
 def __init__(self,path,label,indices,xy,jets,rule,bindings):
  self.path=Path(path);self.label=label;self.indices=np.asarray(indices,dtype=np.int64);self.n=len(self.indices);self.xy=np.asarray(xy,float)[self.indices];self.jets=np.asarray(jets,float)[self.indices];self.rule=rule;self.bindings=bindings;self.done=0;self.started=now()
  self.arr={k:np.full((self.n,)+sh,np.nan)for k,sh in SHAPES.items()}
  if self.indices.ndim!=1 or len(np.unique(self.indices))!=self.n or np.any(self.indices<0)or not np.isfinite(self.xy).all()or not np.isfinite(self.jets).all():raise ValueError('invalid static targets')
  if self.path.exists():
   with np.load(self.path,allow_pickle=False)as z:
    if set(z.files)!=set(SHAPES)|{'indices','xy','jets','manifest'}:raise ValueError('snapshot members')
    m=json.loads(str(z['manifest']));data={k:z[k]for k in SHAPES}
    if z['indices'].dtype!=np.dtype('int64')or not np.array_equal(z['indices'],self.indices)or not np.array_equal(z['xy'],self.xy)or not np.array_equal(z['jets'],self.jets):raise ValueError('static target mismatch')
   if m['label']!=label or m['rule']!=rule or m['bindings']!=bindings or m['schema']!='LARGER_NODE_V1' or m['total']!=self.n:raise ValueError('manifest mismatch')
   done=m['completed']
   if type(done)is not int or not 0<=done<=self.n or m['status']!=('COMPLETE'if done==self.n else'RUNNING'):raise ValueError('completion metadata')
   for k,sh in SHAPES.items():
    a=data[k]
    if a.dtype!=np.dtype('float64')or a.shape!=(self.n,)+sh:raise ValueError('shape/type '+k)
    self.validate_prefix(k,a[:done])
    if not np.isnan(a[done:]).all():raise ValueError('nonempty suffix '+k)
   self.done=done;self.started=m['started_utc'];self.arr=data
 @staticmethod
 def validate_prefix(k,a):
  if k!='residual':
   if not np.isfinite(a).all():raise ValueError('nonfinite '+k)
  else:
   if not np.isfinite(a[:,:3]).all()or np.any(a[:,1:3]<0):raise ValueError('nonfinite/negative residual operands')
   for ratio,den in [(3,1),(4,2)]:
    if not np.array_equal(np.isnan(a[:,ratio]),a[:,den]==0)or np.isinf(a[:,ratio]).any()or np.any(a[:,ratio]<0):raise ValueError('invalid ratios')
 def save(self):
  self.path.parent.mkdir(parents=True,exist_ok=True);tmp=self.path.with_suffix('.tmp')
  m=dict(schema='LARGER_NODE_V1',label=self.label,total=self.n,completed=self.done,status='COMPLETE'if self.done==self.n else'RUNNING',started_utc=self.started,updated_utc=now(),rule=self.rule,bindings=self.bindings)
  with tmp.open('wb')as h:np.savez_compressed(h,indices=self.indices,xy=self.xy,jets=self.jets,manifest=json.dumps(m),**self.arr)
  tmp.replace(self.path)
 def run(self,compute,callback=None):
  if self.done:
   z=compute(int(self.indices[self.done-1]))
   for k in SHAPES:
    if not np.array_equal(np.asarray(z[k]),self.arr[k][self.done-1],equal_nan=True):raise ValueError('boundary replay '+k)
  for pos in range(self.done,self.n):
   z=compute(int(self.indices[pos]))
   if set(z)!=set(SHAPES):raise ValueError('computed members')
   for k,sh in SHAPES.items():
    a=np.asarray(z[k],dtype=float)
    if a.shape!=sh:raise ValueError('computed shape '+k)
    self.validate_prefix(k,a.reshape((1,)+sh));self.arr[k][pos]=a
   self.done=pos+1
   if self.done%64==0 or self.done==self.n:
    self.save()
    if callback:callback(self.done,int(self.indices[pos]))
  return self.arr
