"""Actual SIGTERM/resume and corrupt-snapshot manufactures, entirely lane-local."""
from pathlib import Path
from datetime import datetime,timezone
import os,sys,json,hashlib,signal,subprocess,time
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';D=V/'restart_manufactures';D.mkdir(exist_ok=True)
import numpy as np
from node_export_checkpoint import PhaseStore,SHAPES,write_or_validate_selection
from node_export_inverse_stage import finite_arithmetic
rule={'order':4,'tail_order':8,'split':2.,'inner':.125,'partition':'dyadic'};indices=np.arange(70,dtype=np.int64);bound={'synthetic_source':'fixed-before-both-runs'};cols={'schema':'same production shapes, synthetic values'}
def compute(i):
 x=float(i)/8;y=float(i%7)/16;j=np.array([1.,2.,3.]);jp=np.array([.5,1.,2.]);v=np.array([i/4.,1.-i/8.]);vm=np.array([.25,.5]);vp=np.array([1.,-.75]);rr,dd=finite_arithmetic(j,jp,v,vm,vp,2.,x,y)
 return dict(velocity=v,Phi=float(i*i),dV2dy=float(i)/3,tail_velocity=v/8,metadata=np.arange(1,11,dtype=float)+i,residual=rr,decomposition=dd)
if len(sys.argv)>1 and sys.argv[1]=='--child':
 path=Path(sys.argv[2]);store=PhaseStore(path,'A',indices,rule,bound,cols)
 def stop(done,index):
  if sys.argv[3]=='stop'and done==32:os.kill(os.getpid(),signal.SIGTERM)
 store.run(compute,stop);raise SystemExit(0)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter();checks=[];bindings={str(p):sha(p)for p in [Path(__file__),Path('independent_code/node_export_checkpoint.py'),Path('independent_code/node_export_inverse_stage.py'),Path('independent_code/node_export_arithmetic_strict.py'),Path('independent_code/node_export_arithmetic.py'),R/'INVERSE_RESTART_AND_REVIEW_PROOF.md']}
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def rejected(name,fun):
 try:fun()
 except (ValueError,ArithmeticError,KeyError,TypeError)as e:ck(name,True,str(e));return
 ck(name,False)
def load(p):
 with np.load(p,allow_pickle=False)as f:return {k:f[k]for k in f.files}
def save(p,d):
 with p.open('wb')as f:np.savez_compressed(f,**d)
# Refuse reuse so a rerun cannot silently read prior completed snapshots.
for p in [D/'uninterrupted.npz',D/'resumed.npz',D/'partial32.npz']:
 if p.exists():raise FileExistsError('use a separately named/reviewed test directory: '+str(p))
full=PhaseStore(D/'uninterrupted.npz','A',indices,rule,bound,cols).run(compute)
child=subprocess.run([sys.executable,__file__,'--child',str(D/'resumed.npz'),'stop'],timeout=30,capture_output=True,text=True)
ck('real child terminated bySIGTERM after checkpoint',child.returncode==-signal.SIGTERM,dict(returncode=child.returncode,stdout=child.stdout,stderr=child.stderr))
partial=load(D/'resumed.npz');ck('exact32 retained',json.loads(str(partial['manifest']))['completed']==32);save(D/'partial32.npz',partial)
child=subprocess.run([sys.executable,__file__,'--child',str(D/'resumed.npz'),'continue'],timeout=30,capture_output=True,text=True)
ck('new process resumes and exits',child.returncode==0,dict(returncode=child.returncode,stdout=child.stdout,stderr=child.stderr));got=load(D/'resumed.npz')
for k in full:ck('bitwise same arrays '+k,got[k].dtype==full[k].dtype and got[k].shape==full[k].shape and got[k].tobytes()==full[k].tobytes())
# COMPLETE return must not mutate the archive, preserving downstream source hashes.
h=sha(D/'resumed.npz');PhaseStore(D/'resumed.npz','A',indices,rule,bound,cols).run(compute);ck('completed resume file unchanged',sha(D/'resumed.npz')==h)
rejected('wrong binding rejected',lambda:PhaseStore(D/'partial32.npz','A',indices,rule,{'synthetic_source':'tampered'},cols))
rejected('wrong indices rejected',lambda:PhaseStore(D/'partial32.npz','A',indices[::-1],rule,bound,cols))
rejected('wrong rule rejected',lambda:PhaseStore(D/'partial32.npz','A',indices,{**rule,'split':4.},bound,cols))
rejected('wrong phase rejected',lambda:PhaseStore(D/'partial32.npz','C',indices,rule,bound,cols))
for name in ['status','completed','dtype','prefix','suffix','ratio']:
 d={k:v.copy()for k,v in partial.items()};m=json.loads(str(d['manifest']))
 if name=='status':m['status']='COMPLETE';d['manifest']=np.array(json.dumps(m))
 elif name=='completed':m['completed']=71;d['manifest']=np.array(json.dumps(m))
 elif name=='dtype':d['velocity']=d['velocity'].astype('float32')
 elif name=='prefix':d['velocity'][3,0]=np.nan
 elif name=='suffix':d['velocity'][50,0]=0.
 elif name=='ratio':d['residual'][3,3]=np.nan
 p=D/('tampered_'+name+'.npz');save(p,d);rejected('tampered '+name+' rejected',lambda p=p:PhaseStore(p,'A',indices,rule,bound,cols))
d={k:v.copy()for k,v in partial.items()};d['velocity'][31,0]+=1.;p=D/'tampered_boundary.npz';save(p,d);rejected('finite corrupted replay row rejected',lambda:PhaseStore(p,'A',indices,rule,bound,cols).run(compute))
selpath=D/'SELECTION.json';selection={'generated_utc':start,'indices':[0,17,31],'bindings':{'A.npz':sha(D/'uninterrupted.npz'),'B.npz':'synthetic'}};write_or_validate_selection(selpath,selection);h=sha(selpath);write_or_validate_selection(selpath,{**selection,'generated_utc':'changed-clock-only'});ck('selection same content preserves hash',sha(selpath)==h)
altered={**selection,'bindings':{**selection['bindings'],'A.npz':sha(D/'tampered_boundary.npz')}};rejected('changed A archive selection rejected',lambda:write_or_validate_selection(selpath,altered))
# C checkpoint shares the real frozen selection digest and exercises complete resume.
cids=np.array([0,17,31],np.int64);cb={**bound,str(selpath):sha(selpath)};cpath=D/'C.npz';one=PhaseStore(cpath,'C',cids,rule,cb,cols).run(compute);h=sha(cpath);two=PhaseStore(cpath,'C',cids,rule,cb,cols).run(compute)
ck('C resume after selection identical',sha(cpath)==h and all(one[k].tobytes()==two[k].tobytes()for k in one))
for p,h in bindings.items():ck('stable '+p,sha(p)==h)
out=dict(status='PASS_PHASE_RESTART_AND_TAMPER_REJECTION',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_monotonic_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=bindings,artifact_bindings={str(p):sha(p)for p in D.iterdir()if p.is_file()},scope='Synthetic70-point actual kill/resume plus corruption tests. No actual candidate inverse run.')
(V/'INVERSE_RESTART_MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),out['elapsed_monotonic_seconds'])
