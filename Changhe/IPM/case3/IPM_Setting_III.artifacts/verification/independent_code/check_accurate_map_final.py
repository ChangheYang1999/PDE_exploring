"""Independent result320 arithmetic and artifact audit; no producer/stage imports."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,sys,json,hashlib,math,time,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
sys.set_int_max_str_digits(1000000)
import numpy as np
import gmpy2
import torch
from scipy.linalg import lstsq
from check_larger_node_final import Audit as Parent,arrays,sha,six
import larger_node_independent_arithmetic as ar
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
ROOT=Path('research/accurate_map_final_audit');BASE=ROOT/'verification'
STATES=[('B','hsQ_c2.0_N128_acc.pt',128,32),('C','hsQ_c2.0_N96_acc_fromG.pt',96,24),('A','hsQ_c2.0_N96_acc.pt',96,24),('E','hsQ_c2.0_N96_acc_fine.pt',96,24),('G80','hsQ_c2.0_N80_acc6_fine.pt',80,20),('G96','hsQ_c2.0_N96_acc6_fine.pt',96,24),('G112','hsQ_c2.0_N112_acc6_fine.pt',112,28),('G128','hsQ_c2.0_N128_acc6_fine.pt',128,32)]
STANDARDS=[('S96','standard96.pt',96,24),('S128','standard128c.pt',128,32),('S160','hsG_c2.0_N160_log.pt',160,40)]
PAIRS=[('G80','G96'),('G96','G112'),('G112','G128'),('E','G96'),('S96','A'),('S128','B'),('S96','C'),('S96','E'),('E','G128'),('S128','G128'),('G128','S160')]
REGIONS=[('core',0,.1),('sub',.1,1),('annulus',1,100),('far',100,float('inf'))]
EXTENTS=[100.,1e4,1e7]
now=lambda:datetime.now(timezone.utc).isoformat()
def put(p,d):
 t=p.with_suffix('.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');t.replace(p)
def reader(p):
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):return QLocalCheckpoint(p)
def grids():
 radii=np.unique(np.r_[np.logspace(-6,7,51),.1,1.,100.,1e4,1e7]);angles=[0.,.017,.053,.147,.31,.59,.83,1.07,1.31,1.49,1.553,1.566,np.pi/2];xy=[];rr=[]
 for r in radii:
  for k,t in enumerate(angles):xy.append([0. if k==12 else r*np.cos(t),0. if k==0 else r*np.sin(t)]);rr.append(r)
 ii=np.arange(111);ir=10.**(-6+13*(ii+.37)/111);it=np.pi/2*np.mod((ii+1)*(np.sqrt(5)-1)/2,1.)
 for r,theta in zip(ir,it):xy.append([r*np.cos(theta),r*np.sin(theta)]);rr.append(r)
 return np.asarray(xy),np.asarray(rr)
def common(shift):
 rr=10.**(-3+10*(np.arange(397)+.37)/397)if shift else np.logspace(-3,7,401)
 angles=np.pi*(np.arange(47)+.23)/(2*47)if shift else np.linspace(0,np.pi/2,49)
 # Match the declared binary64 multiplication order, while deriving the Cartesian product separately.
 return np.array([[r*np.cos(t),r*np.sin(t)]for r in rr for t in angles]),np.repeat(rr,len(angles))
def angular_grid(M):
 a=np.linspace(0,np.pi/2,8*M+1)[1:-1];b=(np.arange(M)+.5)*np.pi/(2*M);out=[];blocks=[]
 for r in [3.,30.,300.,3000.]:
  blocks.append(dict(radius=r,start=len(out),dense_count=len(a),coll_count=M,total=len(a)+M));out.extend([[r*np.cos(t),r*np.sin(t)]for t in np.r_[a,b]])
 return np.asarray(out),a,b,blocks

def power_center(q):
 Q=gmpy2.mpq
 def rat(v):
  n,d=float(v).as_integer_ratio();return Q(n,d)
 def linear(poly,alpha,beta):
  z=[Q(0)]*(len(poly)+1)
  for j,v in enumerate(poly):z[j]+=beta*v;z[j+1]+=alpha*v
  return z
 def expand(cc,tk):
  alpha=4/(1-tk);beta=-(3+tk)/(1-tk);old=[Q(1)];out=[Q(0)]*len(cc);out[0]=rat(cc[0])
  if len(cc)>1:
   cur=[beta,alpha]
   for k,v in enumerate(cur):out[k]+=rat(cc[1])*v
   for j in range(2,len(cc)):
    nxt=linear(cur,2*alpha,2*beta)
    for k,v in enumerate(old):nxt[k]-=v
    for k,v in enumerate(nxt):out[k]+=rat(cc[j])*v
    old,cur=cur,nxt
  return out
 # Independently split the original flat coefficient vector, without q.exact_coefficients or q.coeff.
 rows=[];start=0
 for k in range(q.M):
  size=q.N+1-k;rows.append(expand(q.u[start:start+size],rat(q.tk[k])));start+=size
 if start!=len(q.u)or q.basis!='local' or(q.cl,q.kappa,q.L,q.p)!=(2,2,1,.5):raise ValueError('exact center admission')
 a=rows[0][0];twod=rows[0][1]if len(rows[0])>1 else Q(0);u=rows[1][0]if len(rows)>1 else Q(0);b=16*(twod-a+u);e=16*(twod-a-u);c=-a;K=Q(0)
 for k,row in enumerate(rows):
  K+=(-1)**k*sum(row,Q(0))/2
  if k:c-=2*k*k*(-1)**k*sum((v*(Q(1,l+k)+Q(3,l+k+1))for l,v in enumerate(row)),Q(0))
 D=1+c
 if not a:raise ValueError('degenerate source outside this finite audit')
 d=dict(a=a,b=b,e=e,E=e/a,K=K,cH=c,delta=D,B_minus_6E=b-6*e/a,cubic_residual=e*(2+3*D)-a*b/3,axis_limit=abs(D)/(abs(1+D)+1))
 return {k:F(int(v.numerator),int(v.denominator))for k,v in d.items()}

def regional(xy,rr,extent=float('inf')):
 radii=np.hypot(xy[:,0],xy[:,1]);out=[]
 for name,lo,hi in REGIONS:
  ids=[i for i,r in enumerate(radii)if lo<=r<hi and r<=extent];met={}
  for key,col in [('absR',0),('Rf',3),('Rv',4)]:
   valid=[i for i in ids if math.isfinite(float(rr[i,col]))];i=max(valid,key=lambda j:abs(float(rr[j,col])))if valid else None
   met[key]=dict(index=i,value=abs(float(rr[i,col]))if i is not None else None,defined_count=len(valid),undefined_count=len(ids)-len(valid),x=float(xy[i,0])if i is not None else None,y=float(xy[i,1])if i is not None else None,R=float(rr[i,0])if i is not None else None,Nf=float(rr[i,1])if i is not None else None,Nv=float(rr[i,2])if i is not None else None)
  out.append(dict(region=name,count=len(ids),metrics=met))
 return out

def selector(xy,j,B):
 reasons={}
 def add(i,why):
  if i is not None:reasons.setdefault(str(int(i)),[]).append(why)
 for e in [float('inf')]+EXTENTS:
  for row in regional(xy,B['residual'],e):
   for key,d in row['metrics'].items():add(d['index'],str(e)+' '+row['region']+' '+key)
 for k in [0,1]:add(max(range(len(xy)),key=lambda i:abs(B['velocity'][i,k])),'absV'+str(k+1))
 add(max(range(len(xy)),key=lambda i:abs(j[i,3])),'absgxx')
 for i in [0,len(xy)//2,len(xy)-1]:add(i,'first/middle/last')
 return dict(indices=sorted(map(int,reasons)),reasons={str(i):reasons[str(i)]for i in sorted(map(int,reasons))})

def extent_rounding(xy,rr):
 r=np.hypot(xy[:,0],xy[:,1]);out=[]
 for e in EXTENTS:
  ni=[i for i,v in enumerate(rr)if v<=e];pi=[i for i,v in enumerate(r)if v<=e]
  out.append(dict(extent=e,nominal_count=len(ni),physical_count=len(pi),nominal_in_physical_out=sorted(set(ni)-set(pi)),nominal_out_physical_in=sorted(set(pi)-set(ni))))
 return out

def centers(xy,B,ex):
 ids=sorted([i for i in range(len(xy))if xy[i,0]==0 and xy[i,1]>0],key=lambda i:xy[i,1])[:2];out=[]
 for i in ids:
  y=ar.f(xy[i,1]);v=ar.f(B['velocity'][i,1])/y;r=ar.f(B['residual'][i,0])/y;rf=ar.f(B['residual'][i,3]);d={}
  for key,value,target in [('V2_over_y',v,ex['cH']),('R_over_y',r,ex['a']*ex['delta']),('Rf',rf,ex['axis_limit'])]:d[key]=dict(observed=float(value),exact_limit=str(target),difference=float(value-target))
  out.append(dict(index=i,y=float(y),comparisons=d,scope='Finite consistency diagnostic; finite-y corrections and quadrature error are not enclosed.'))
 return out

def mp_diagnostics(rec,j):
 low=list(map(ar.decimal,rec['decimal']['72']));high=list(map(ar.decimal,rec['decimal']['108']));dd=list(map(ar.f,j));out=[]
 if not len(low)==len(high)==len(dd)==4:raise ValueError('local MP width')
 for a,b,c in zip(low,high,dd):
  delta=abs(a-b);scale=max(abs(a),abs(b),F(1,10**80));den=max(abs(c),abs(b));out.append(dict(precision_abs=float(delta),precision_scaled=float(delta/scale),precision_pass=delta<=scale/F(10**48),double_abs=float(abs(c-b)),double_pure_relative=float(abs(c-b)/den)if den else None,both_zero=not bool(den)))
 return out

def differences(a,b,r):
 z0=abs(a[:,0]-b[:,0]);grad=np.hypot(a[:,1]-b[:,1],a[:,2]-b[:,2]);den=np.maximum(abs(a[:,0]),abs(b[:,0]));pure=np.array([v/d if d else 0. for v,d in zip(z0,den)]);vals=[z0/np.sqrt(1+r),grad*np.sqrt(1+r),z0/(abs(b[:,0])+1e-300),pure];keys=['weighted_density','weighted_gradient','legacy_new_denominator_relative','pure_relative'];out=[]
 for name,lo,hi in [('core',0,.1),('sub',.1,1),('annulus',1,100),('far_low',100,1e4),('far_high',1e4,1e7)]:
  ids=[i for i,x in enumerate(r)if lo<=x<hi];met={}
  for key,z in zip(keys,vals):
   i=max(ids,key=lambda k:z[k])if ids else None;met[key]=dict(index=i,value=float(z[i])if i is not None else None)
  out.append(dict(region=name,count=len(ids),both_zero_count=sum(den[i]==0 for i in ids),metrics=met))
 return out

class Audit(Parent):
 def __init__(self,V=BASE,fixture=False):super().__init__(V,fixture);self.candidate=None
 def phase(self,p,tag,label,ids,xy,j,bb):
  z=self.load_snapshot(p,tag,label,ids,xy,j,self.candidate['artifacts']);m=json.loads(str(z['manifest']));self.ck('exact phase binding '+tag+label,m['bindings']==bb);return z
 def checked_spreads(self,xy,j,ids,A,B,C,declared,angular=False):
  self.ck('exact selected comparison coverage',len(declared)==len(ids))
  enriched=[]
  for i,d in zip(ids,declared):
   self.ck('comparison index',d['index']==i)
   enriched.append(dict(d,x=float(xy[i,0]),y=float(xy[i,1])))
  return self.spreads(xy,j,ids,A,B,C,enriched)
 def chronology(self,admission,result,c):
  dt=lambda x:datetime.fromisoformat(x);self.ck('candidate completion within recorded attempt',dt(admission['started_utc'])<=dt(c['started_utc'])<=dt(c['finished_utc'])<=dt(result['finished_utc']))
 def provenance(self,V):
  job=self.json(V/'JOB.json');proc=Path('/proc')/str(job['pid'])
  if proc.exists():self.ck('320 worker ceased',((proc/'stat').read_text().rsplit(') ',1)[1].split()[0]=='Z')or(b'accurate_map'in (proc/'cmdline').read_bytes())is False)
  result=self.json(V/'EXECUTION_RESULT.json');self.ck('worker successful execution',result['returncode']==0 and result['wrapper_pid']==job['pid']and result['admission_path']==job['admission_path'])
  admission=self.json(job['admission_path'],job['admission_sha256']);policy=self.json(admission['policy_path'],admission['policy_sha256']);self.ck('wrapper process policy',policy['nice']==19 and policy['memory_limit_bytes']==14*1024**3 and policy['timeout_seconds']==10800 and policy['schema']=='IPM320_EXECUTION_V1')
  for path,h in policy['sources'].items():self.bind(path,h)
  self.ck('wrapper result admission',result['admission_sha256']==job['admission_sha256']and result['driver_sha256']==policy['sources']['independent_code/run_accurate_map_audit.py']and result['started_utc']==admission['started_utc'])
  sources={}
  for name in ['INPUTS.json','INPUTS_SUPPLEMENT.json','INPUTS_ADDITIONAL.json']:
   for d in self.json(V/name)['files']:self.bind(d['frozen'],d['sha256']);sources[Path(d['frozen']).name]=d['frozen']
  self.ck('recorded attempt policy',admission['nice']==19 and admission['memory_limit_bytes']==14*1024**3 and admission['lock_held']is True and admission['wrapper_pid']==job['pid'])
  self.execution=(admission,result)
  return sources
 def run(self):
  V=self.V;O=V/'candidate'
  for p in [__file__,ar.__file__,sys.modules['check_larger_node_final'].__file__,'independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/independent_hydrostatic.py',ROOT/'FINAL_CHECKER_PROOF.md',ROOT/'FINAL_GRID_REPRESENTATION_PROOF.md',ROOT/'FINAL_COVERAGE_AND_LAUNCH_PROOF.md',ROOT/'FINAL_PROVENANCE_AND_COVERAGE_PROOF.md']:self.bind(p)
  if self.fixture:
   cfg=self.json(V/'FIXTURE.json');states=cfg['states'];standards=cfg['standards'];pairs=cfg['pairs'];angular_tags=cfg['angular_tags'];sources=cfg['sources']
  else:
   self.gate(V/'FINAL_MANUFACTURES.json','PASS_INDEPENDENT_ACCURATE_MAP_FINAL_MANUFACTURES')
   accept=self.json(V/'FINAL_DESIGN_ACCEPTANCE.json');self.ck('accepted final checker',accept['status']=='ACCEPTED_CANDIDATE_FREE_FINAL_CHECKER_DESIGN')
   for p,h in accept['bindings'].items():self.bind(p,h)
   self.gate(V/'PROVENANCE_MANUFACTURES.json','PASS_ACCURATE_MAP_PROVENANCE_MANUFACTURES')
   sources=self.provenance(V)
   states=STATES;standards=STANDARDS;pairs=PAIRS;angular_tags=['B','G128']
  c=self.gate(O/'COMPLETE.json','COMPLETE_FINITE_ACCURATE_MAP_REQUIRES_FINAL_AUDIT');self.candidate=c
  if not self.fixture:
   admission,result=self.execution;self.chronology(admission,result,c)
  self.ck('candidate state order',[z['tag']for z in c['states']]==[s[0]for s in states]);self.ck('versions recorded',all(isinstance(c['versions'][k],str)and c['versions'][k]for k in ['python','numpy','torch']))
  for p,h in c['artifacts'].items():
   self.ck('artifact inside candidate',Path(p).resolve().is_relative_to(O.resolve()));self.bind(p,h)
  models={}
  for tag,name,N,M in list(states)+list(standards):
   q=reader(self.bind(sources[name]));self.ck('source parameters '+tag,(q.N,q.M,q.cl,q.kappa,q.L,q.p,q.basis,q.meta['basis_nodes_source'])==(N,M,2,2,1,.5,'local','stored')and np.isfinite(q.u).all());models[tag]=q
   self.ck('candidate binds source '+tag,c['bindings'][str(q.path)]==sha(q.path))
  xy,rr=grids();out=[];seen_artifacts=set()
  def artifact(p):seen_artifacts.add(str(p));return self.artifact(p,c['artifacts'])
  for state,record in zip(states,c['states']):
   tag,name,N,M=state;q=models[tag];target=O/(tag+'_targets.npz');d=arrays(artifact(target));j=CartesianQJet(q).jet(xy[:,0],xy[:,1]);self.ck('reconstructed targets '+tag,set(d)=={'xy','jets'}and np.array_equal(d['xy'],xy)and np.array_equal(d['jets'],j)and d['xy'].dtype==d['jets'].dtype==np.dtype('float64'))
   bb=dict(c['bindings']);bb[str(target)]=sha(target);B=self.phase(artifact(O/(tag+'_B.npz')),tag,'B',list(range(len(xy))),xy,j,bb)
   sp=artifact(O/(tag+'_SELECTION.json'));sel=self.json(sp);self.ck('independent selection '+tag,sel==selector(xy,j,B));ids=sel['indices'];ab=dict(bb);ab[str(sp)]=sha(sp)
   A=self.phase(artifact(O/(tag+'_A.npz')),tag,'A',ids,xy,j,ab);C=self.phase(artifact(O/(tag+'_C.npz')),tag,'C',ids,xy,j,ab)
   self.ck('state serialized record '+tag,self.json(artifact(O/(tag+'_COMPLETE.json')))==record)
   sums=regional(xy,B['residual']);ext={str(e):regional(xy,B['residual'],e)for e in EXTENTS}
   self.ck('state record geometry '+tag,(record['N'],record['M'],record['source_path'],record['source_sha256'],record['points'])==(N,M,str(q.path),sha(q.path),len(xy)))
   self.ck('regional and extent maxima '+tag,record['regions']==sums and record['extents']==ext and record['selected']==sel and record['extent_rounding']==extent_rounding(xy,rr))
   self.ck('exact arithmetic counts '+tag,record['arithmetic_counts']==dict(B=5*len(xy),A=5*len(ids),C=5*len(ids)))
   comp=self.checked_spreads(xy,j,ids,A,B,C,record['comparisons'])
   center=self.json(artifact(O/(tag+'_CENTER.json')));ex=power_center(q);self.ck('independent exact power center '+tag,{k:F(v)for k,v in center['exact'].items()}==ex)
   self.ck('center rounding and bindings '+tag,center['source_sha256']==sha(q.path)and center['bindings']==bb and center['rounded']=={k:float(v)for k,v in ex.items()}==record['center'])
   self.ck('center Gaussian descriptors '+tag,set(center['center_formula_gauss'])=={str(N+M+8),str(2*(N+M+8))}and all(math.isfinite(x)for x in center['center_formula_gauss'].values()))
   self.ck('center inverse diagnostics '+tag,record['center_inverse']==centers(xy,B,ex))
   mp=self.json(artifact(O/(tag+'_LOCAL_MP.json')));self.ck('MP binding/coverage '+tag,mp['bindings']==bb and[z['index']for z in mp['results']]==ids)
   failed=[]
   for z,i in zip(mp['results'],ids):
    self.ck('MP target '+tag+str(i),[z['x'],z['y']]==list(xy[i])and z['double']==list(j[i])and set(z['decimal'])=={'72','108'})
    diag=mp_diagnostics(z,j[i]);self.ck('MP exact decimal diagnostics '+tag+str(i),diag==z['diagnostics'])
    failed.extend(dict(index=i,component=k,diagnostic=d)for k,d in enumerate(diag)if not d['precision_pass'])
   self.ck('MP failure coverage '+tag,record['mp_precision_failures']==failed and record['mp_precision_all_pass']==(not failed))
   self.ck('reflections '+tag,np.array_equal(CartesianQJet(q).jet(-xy[ids,0],xy[ids,1]),j[ids]*[1,-1,1,1])and np.array_equal(CartesianQJet(q).jet(xy[ids,0],-xy[ids,1]),j[ids]*[-1,-1,1,-1]))
   out.append(dict(tag=tag,N=N,M=M,source_sha256=sha(q.path),points=len(xy),regions=sums,extents=ext,selected_count=len(ids),comparisons=comp,center={k:float(v)for k,v in ex.items()},center_exact_nonzero=bool(ex['delta']),center_inverse=record['center_inverse'],MP_failed=failed,gauss_minus_exact={n:float(ar.f(v)-ex['cH'])for n,v in center['center_formula_gauss'].items()}))
   print('FINAL STATE',tag,now(),flush=True)
  angular_out=[];self.ck('angular tag order',[z['tag']for z in c['angular']]==angular_tags)
  for tag,record in zip(angular_tags,c['angular']):
   q=models[tag];ax,dense,coll,blocks=angular_grid(q.M);tp=artifact(O/(tag+'_angular_targets.npz'));d=arrays(tp);j=CartesianQJet(q).jet(ax[:,0],ax[:,1]);self.ck('angular targets '+tag,set(d)=={'xy','jets','dense','collocation'}and all(np.array_equal(d[k],v)for k,v in dict(xy=ax,jets=j,dense=dense,collocation=coll).items()))
   bb=dict(c['bindings']);bb[str(tp)]=sha(tp);B=self.phase(artifact(O/(tag+'_angular_B.npz')),tag+'_angular','B',list(range(len(ax))),ax,j,bb)
   self.ck('angular serialized record '+tag,self.json(artifact(O/(tag+'_ANGULAR.json')))==record and record['rows']==len(ax)and len(record['summary'])==4)
   ids=[];qr=[]
   for block,z in zip(blocks,record['summary']):
    start=block['start'];n=block['dense_count'];u=B['residual'][start:start+n,0]/B['residual'][start:start+n,1];v=B['residual'][start+n:start+block['total'],0]/B['residual'][start+n:start+block['total'],1]
    self.ck('finite angular denominators '+tag,np.isfinite(u).all()and np.isfinite(v).all())
    a=max(range(n),key=lambda k:abs(u[k]));b=max(range(q.M),key=lambda k:abs(v[k]));coeff=np.asarray(z['fit_coefficients']);mat=np.column_stack([np.cos(2*dense*k)for k in range(3*q.M)]);fit,_,rank,_=lstsq(mat,u,lapack_driver='gelsy');sv=np.linalg.svd(mat,compute_uv=False);k=int(np.argmax(abs(coeff[1:]))+1)
    self.ck('angular finite summaries '+tag+str(block['radius']),z['radius']==block['radius']and z['dense_max']==float(abs(u[a]))and z['dense_argmax']==start+a and z['collocation_direct_max']==float(abs(v[b]))and z['collocation_argmax']==start+n+b and z['collocation_interpolated_max']==float(max(abs(np.interp(coll,dense,u))))and z['sign_changes']==sum(u[i-1]*u[i]<0 for i in range(1,n))and z['dominant_k']==k and z['dominant_coefficient']==coeff[k]and z['least_squares_rank']==rank==3*q.M)
    delta=float(max(abs(coeff-fit)));normal=float(np.linalg.norm(mat.T@(mat@coeff-u),ord=np.inf));scale=max(float(np.linalg.norm(u)),1e-300);tol=2e-11*scale
    self.ck('independent angular QR '+tag+str(block['radius']),coeff.shape==(3*q.M,)and np.isfinite(coeff).all()and delta<=tol and normal<=tol and math.isclose(z['condition_number'],float(sv[0]/sv[-1]),rel_tol=2e-12),dict(max_coefficient_difference=delta,normal_equation_max=normal,tolerance=tol))
    ids.extend([start+a,start+n+b]);qr.append(dict(radius=block['radius'],qr_dominant_k=int(np.argmax(abs(fit[1:]))+1),coefficient_difference=delta,normal_equation_max=normal))
   ids=sorted(set(ids));sp=artifact(O/(tag+'_angular_SELECTION.json'));sel=self.json(sp);self.ck('angular selected rows '+tag,sel==dict(indices=ids,reason='dense and direct collocation Rf maxima on each of four rings'));ab=dict(bb);ab[str(sp)]=sha(sp)
   A=self.phase(artifact(O/(tag+'_angular_A.npz')),tag+'_angular','A',ids,ax,j,ab);C=self.phase(artifact(O/(tag+'_angular_C.npz')),tag+'_angular','C',ids,ax,j,ab);self.checked_spreads(ax,j,ids,A,B,C,record['comparisons'],True);angular_out.append(dict(tag=tag,summary=record['summary'],QR=qr))
  foutput=[];self.ck('function grid order',[z['grid']for z in c['function_comparisons']]==['common','shifted'])
  for shift,record in zip([False,True],c['function_comparisons']):
   name='shifted'if shift else'common';fx,rr=common(shift);p=artifact(O/(name+'_fields.npz'));d=arrays(p);self.ck('common field schema '+name,set(d)=={'xy','nominal_radius'}|set(models)and np.array_equal(d['xy'],fx)and np.array_equal(d['nominal_radius'],rr))
   for tag,q in models.items():self.ck('common jet reconstruction '+name+tag,d[tag].dtype==np.dtype('float64')and np.array_equal(d[tag],CartesianQJet(q).jet(fx[:,0],fx[:,1])[:,:3]))
   self.ck('function serialized record '+name,self.json(artifact(O/(name+'_COMPARISONS.json')))==record and record['points']==len(fx)and[z['pair']for z in record['records']]==[list(p)for p in pairs])
   for pair,z in zip(pairs,record['records']):
    a,b=pair;self.ck('independent function metrics '+name+str(pair),z['regions']==differences(d[a],d[b],rr)and z['legacy_denominator_state']==b and z['orientation_scope']=='Verifier-chosen ordered pair; producer comparison orientation is not asserted here.')
   foutput.append(record)
  self.ck('all candidate artifacts used',seen_artifacts==set(c['artifacts']),dict(unused=sorted(set(c['artifacts'])-seen_artifacts)))
  for p,h in list(self.bindings.items()):self.scalar(sha(p)==h,('stable',p))
  self.outputs=dict(states=out,angular=angular_out,function_comparisons=foutput,scope='Independent exact finite-array and power-basis arithmetic; scalar MP sensitivities and quadrature outputs are empirical. Gaussian center estimates are descriptive. No quadrature enclosure, continuum convergence, historical execution authentication or primary IPM endpoint.')
  return self.outputs

def main():
 fixture=len(sys.argv)>1;V=BASE
 if fixture:
  if len(sys.argv)!=3 or sys.argv[1]!='--fixture':raise ValueError('explicit fixture invocation required')
  V=Path(sys.argv[2]);V.resolve().relative_to((BASE/'final_manufactures').resolve())
 a=Audit(V,fixture);start=now();tick=time.monotonic();p=V/'FINAL_CHECKS.json'
 if p.exists():p.rename(V/('FINAL_CHECKS_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json'))
 try:a.run();status='PASS_SYNTHETIC_ACCURATE_MAP_FINAL'if fixture else'PASS_FINITE_ACCURATE_MAP_FINAL_REQUIRES_MODEL_REVIEW'
 except Exception:status='FAIL';a.outputs['error']=traceback.format_exc();print(a.outputs['error'],flush=True)
 put(p,dict(status=status,synthetic_only=fixture,started_utc=start,finished_utc=now(),elapsed_seconds=time.monotonic()-tick,count=len(a.checks),scalar_assertion_count=a.scalars,checks=a.checks,bindings=a.bindings,outputs=a.outputs));print(status,len(a.checks),a.scalars,flush=True)
 if status=='FAIL':raise SystemExit(1)
if __name__=='__main__':main()
