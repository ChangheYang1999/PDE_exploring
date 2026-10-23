"""Record-only node audit, with separately implemented selected Cartesian jets."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import os,sys,json,hashlib,math,re,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
import numpy as np
import new_node_export_record as core
ROOT=Path('research/new_node_export_record_audit');V=ROOT/'verification';checks=[];bindings={}
now=lambda:datetime.now(timezone.utc).isoformat()
def ck(name,b,e=None):
 checks.append(dict(name=name,passed=bool(b),evidence=e))
 if not b:raise AssertionError((name,e))
def bind(p,h=None):
 p=Path(p);b=p.read_bytes();x=hashlib.sha256(b).hexdigest();ck('binding '+str(p),h is None or h==x);bindings[str(p)]=x;return p

def fake(operands):
 args=np.asarray(operands,float);x,y,g,gx,gy,v,w=args.T;a=2*x+v;b=2*y+w;px=a*gx;py=b*gy
 return dict(zip(['x','y','g','g_xi','g_y','V1','V2','R_h','N_f'],[x,y,g,gx,gy,v,w,px+py-g,np.abs(px)+np.abs(py)+np.abs(g)]))
def rejects(n,fn):
 try:fn()
 except(ValueError,AssertionError,KeyError)as e:ck(n,True,str(e)[:160])
 else:raise AssertionError('not rejected '+n)
def manufactures():
 d=fake([(1,2,3,4,5,6,7),(-1,.01,-2,-3,4,5,-6),(0,0,0,1,2,0,0),(1,0,0,1,0,-2,0),(2**-100,2**100,2**-50,2**-40,2**-60,2**-100,2**-90)])
 f,e=core.check_rows(d);ck('all5 varied finite rows',f.shape==(5,5));ck('Nf and Nv allzero undefined',np.isnan(f[2,3])and np.isnan(f[2,4]));ck('Nfzero Nvpositive',np.isnan(f[3,3])and f[3,4]==0 and f[3,2]>0);ck('explicit distributed residual',Q(f[0,0])==67)
 for key,value in [('R_h',1.),('N_f',1.)]:
  z={k:a.copy()for k,a in d.items()};z[key][0]+=value;rejects('edited '+key,lambda z=z:core.check_rows(z))
 for key,value in [('x',math.nan),('g',math.inf)]:
  z={k:a.copy()for k,a in d.items()};z[key][0]=value;rejects('nonfinite '+key,lambda z=z:core.check_rows(z))
 z={k:a.copy()for k,a in d.items()};z['x']=z['x'].astype('float32');rejects('wrong dtype',lambda:core.check_rows(z))
 z=fake([(1e-310,1,1,1,0,0,0)]);rejects('subnormal intermediate',lambda:core.check_rows(z))
 x=np.array([0,.1,1,100,101.]);y=np.zeros(5);ff=np.ones((5,5));ff[4,3]=math.nan;reg=core.regions(x,y,ff);ck('halfopen counts',[z['count']for z in reg]==[1,1,1,2]);ck('first tie',reg[3]['metrics']['absR']['index']==3);ck('undefined excluded',reg[3]['metrics']['Rf']['undefined_count']==1)
 for p in [__file__,core.__file__,ROOT/'PROOF.md']:bind(p)
 return dict(status='PASS_NEW_EXPORT_RECORD_MANUFACTURES',utc=now(),count=len(checks),checks=checks,bindings=bindings)

def run():
 import torch
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 mf=json.loads(bind(V/'MANUFACTURES.json').read_text());ck('manufacture gate',mf['status']=='PASS_NEW_EXPORT_RECORD_MANUFACTURES'and mf['count']==len(mf['checks'])and all(x['passed']for x in mf['checks']))
 for p,h in mf['bindings'].items():bind(p,h)
 cfg=json.loads(bind(V/'EXPORT_INPUTS.json').read_text());out=[]
 for z in cfg['states']:
  with np.load(bind(z['export'],z['export_sha256']),allow_pickle=False)as f:d={k:f[k].copy()for k in f}
  source=bind(z['state'],z['state_sha256'])
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(source)
  N,M,fine=z['N'],z['M'],z['fine'];tag=z['tag'];n=N*M*(3 if fine else 1)
  ck('metadata '+tag,int(d['N'])==q.N==N and int(d['M'])==q.M==M and bool(d['fine'])==fine and float(d['c'])==q.cl==2 and q.L==1 and q.kappa==2 and q.p==.5 and q.meta['basis_nodes_source']=='stored'and q.basis=='local')
  ck('source hash '+tag,str(d['state_sha256'])==z['state_sha256']);ck('rule '+tag,str(d['rule'])=='resolved evaluator (32, 10x16, 400, q=2); rows: '+('3M oversampled angles (fine)'if fine else'M collocation angles'));ck('size '+tag,len(d['x'])==n)
  m=M*(3 if fine else 1);rr=np.sqrt((1+q.tk[1:])/2)/(1-q.tk[1:])**2;th=(np.arange(m)+.5)*np.pi/(2*m);xx=(rr[:,None]*np.cos(th)).ravel();yy=(rr[:,None]*np.sin(th)).ravel();delta=np.stack([d['x']-xx,d['y']-yy],1);scale=np.stack([abs(xx),abs(yy)],1);relative=float(np.max(abs(delta)/scale));ck('own coordinates '+tag,relative<=32*float(core.U),relative)
  vals,errors=core.check_rows(d);ck('allnode finite arithmetic '+tag,True,errors);reg=core.regions(d['x'],d['y'],vals)
  exportvals=vals.copy();exportvals[:,0]=d['R_h'];exportvals[:,1]=d['N_f'];exportvals[:,3]=np.divide(abs(d['R_h']),d['N_f'],out=np.full(n,np.nan),where=d['N_f']!=0);exportreg=core.regions(d['x'],d['y'],exportvals)
  ids={0,n//2,n-1}
  for r in reg:
   for a in r['metrics'].values():
    if a['index']is not None:ids.add(a['index'])
  ids=sorted(ids);own=CartesianQJet(q).jet(d['x'][ids],d['y'][ids])[:,:3];prod=np.stack([d['g'][ids],d['g_xi'][ids],d['g_y'][ids]],1);err=abs(own-prod)/(1+abs(own));ck('selected own jets '+tag,np.isfinite(own).all()and np.all(err<=1e-10),float(err.max()))
  table=bind(z['record'],z['record_sha256']).read_text();rows=re.findall(r'r in \[([^,]+), ([^\)]+)\): max \|R_h\| (\S+)\s+max \|R_h\|/N_f (\S+)',table);ck('four printed regions '+tag,len(rows)==4)
  for k,row in enumerate(rows):
   for metric,value in [('absR',row[2]),('Rf',row[3])]:
    mant,exp=value.lower().split('e');places=len(mant.split('.')[1]);half=Q(10)**(int(exp)-places)/2;center=Q(value);v=Q(exportreg[k]['metrics'][metric]['value']);ck('printed interval '+tag+str(k)+metric,center-half<=v<=center+half)
  out.append(dict(tag=tag,points=n,arithmetic=errors,coordinate_relative_error=relative,exact_operand_regions=reg,export_arithmetic_regions=exportreg,selected_jet_indices=ids,selected_jet_scaled_max=float(err.max()),scope='Producer velocities on all nodes; exact finite-operand arithmetic; independent density jets only at selected indices. Full-node inverse not independently recomputed.'))
 for p in [__file__,core.__file__,ROOT/'PROOF.md','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/independent_hydrostatic.py']:bind(p)
 return dict(status='PASS_NEW_NODE_EXPORT_RECORDS_REQUIRES_FINAL_REVIEW',utc=now(),count=len(checks),checks=checks,bindings=bindings,states=out,scope='Producer-record consistency only for all-node velocities. No canonical inverse error bound or primary endpoint.')
if __name__=='__main__':
 try:
  if sys.argv[1:]==['--manufactures']:out=manufactures();name='MANUFACTURES.json'
  elif not sys.argv[1:]:out=run();name='CHECKS.json'
  else:raise ValueError('unsupported argument')
  (V/name).write_text(json.dumps(out,indent=2,allow_nan=True)+'\n');print(out['status'],out['count'])
 except Exception:
  (V/('FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')).write_text(json.dumps(dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
