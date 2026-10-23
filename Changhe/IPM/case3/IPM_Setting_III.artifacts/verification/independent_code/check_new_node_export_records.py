"""Record-only node audit, with separately implemented selected Cartesian jets."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from types import SimpleNamespace
import os,sys,json,hashlib,math,re,traceback,copy,io
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

def read_bound(p,h=None):
 p=Path(p);b=p.read_bytes();hh=hashlib.sha256(b).hexdigest();ck('exact loaded bytes '+str(p),h is None or hh==h);ck('stable loaded bytes '+str(p),str(p)not in bindings or bindings[str(p)]==hh);bindings[str(p)]=hh;return b

def source_pin(da):
 k=str(V/'SOURCE_INPUTS.json')
 if k not in da['bindings']:raise ValueError('source inputs not pinned by design acceptance')
 return da['bindings'][k]

def fake(operands):
 args=np.asarray(operands,float);x,y,g,gx,gy,v,w=args.T;a=2*x+v;b=2*y+w;px=a*gx;py=b*gy
 return dict(zip(core.ARRAYS,[x,y,g,gx,gy,v,w,px+py-g,np.abs(px)+np.abs(py)+np.abs(g)]))
def rejects(n,fn):
 try:fn()
 except(ValueError,AssertionError,KeyError)as e:ck(n,True,str(e)[:160])
 else:raise AssertionError('not rejected '+n)

def manufactures():
 d=fake([(1,2,3,4,5,6,7),(-1,.01,-2,-3,4,5,-6),(0,0,0,1,2,0,0),(1,0,0,1,0,-2,0),(2**-100,2**100,2**-50,2**-40,2**-60,2**-100,2**-90)])
 f,e=core.check_rows(d);ck('all5 varied finite rows',f.shape==(5,5));ck('Nf and Nv allzero undefined',np.isnan(f[2,3])and np.isnan(f[2,4]));ck('Nfzero Nvpositive',np.isnan(f[3,3])and f[3,4]==0 and f[3,2]>0);ck('explicit distributed residual',Q(f[0,0])==84)
 for key in ['R_h','N_f']:
  z=copy.deepcopy(d);z[key][0]+=1.;rejects('edited '+key,lambda z=z:core.check_rows(z))
  z=copy.deepcopy(d);z[key][0]=np.nextafter(z[key][0],math.inf);core.check_rows(z);ck('one ulp allowed '+key,True)
  z=copy.deepcopy(d);target=Q(float(z[key][0]))+core.GAMMA*90;bad=float(target)
  while Q(bad)<=target:bad=np.nextafter(bad,math.inf)
  ck('smallest representable above gamma8 '+key,Q(np.nextafter(bad,-math.inf))<=target<Q(bad))
  z[key][0]=bad;rejects('near threshold refused '+key,lambda z=z:core.check_rows(z))
 for key,value in [('x',math.nan),('g',math.inf)]:
  z=copy.deepcopy(d);z[key][0]=value;rejects('nonfinite '+key,lambda z=z:core.check_rows(z))
 z=copy.deepcopy(d);z['x']=z['x'].astype('float32');rejects('wrong dtype',lambda:core.check_rows(z))
 z=fake([(1e-310,1,1,1,0,0,0)]);rejects('subnormal intermediate',lambda:core.check_rows(z))
 z=fake([(2**-600,1,1,2**-600,0,0,0)]);rejects('product rounded to zero underflow',lambda:core.check_rows(z))
 rejects('exact residual underflow rejected',lambda:core.round_values([Q(1,2**1100),Q(1),Q(1),Q(0),Q(0)],0))
 rejects('exact residual overflow rejected',lambda:core.round_values([Q(2**1100),Q(1),Q(1),Q(0),Q(0)],0))
 rr,under=core.round_values([Q(1),Q(1),Q(1),Q(1,2**1100),Q(0)],3);ck('ratio underflow explicit exact ledger',len(under)==1 and under[0]['field']=='Rf'and Q(under[0]['exact'])>0 and rr[3]==0)
 x=np.array([0,.1,1,100,101.]);y=np.zeros(5);ff=np.ones((5,5));ff[4,3]=math.nan;reg=core.regions(x,y,ff);ck('halfopen counts',[z['count']for z in reg]==[1,1,1,2]);ck('first tie',reg[3]['metrics']['absR']['index']==3);ck('undefined excluded',reg[3]['metrics']['Rf']['undefined_count']==1)
 ex=core.export_regions(d,f);ck('no export Rv',all('Rv'not in z['metrics']for z in ex));ck('export field labels',all(set(a['fields'])=={'R_h','N_f','Rf'}for z in ex for a in z['metrics'].values()if a['index']is not None))
 cp=copy.deepcopy(ex);cp[0]['metrics']['absR']['index']=1;ck('selection includes export-only maximizer',1 in core.selected([],cp,9))
 tk=np.array([-1.,-.5,.5]);xx,yy=core.expected_coordinates(tk,2,False);co=core.coordinates(xx,yy,xx,yy);ck('coordinate identity',co['relative_error']==0)
 rejects('angle-major ordering',lambda:core.coordinates(xx.reshape(2,2).T.ravel(),yy.reshape(2,2).T.ravel(),xx,yy))
 aa,bb=core.expected_coordinates(tk,2,True);rejects('wrong M versus3M',lambda:core.coordinates(aa,bb,xx,yy))
 aa=xx.copy();aa[0]*=1+64*float(core.U);rejects('64u perturbation',lambda:core.coordinates(aa,yy,xx,yy))
 aa=xx.copy();aa[0]=0;rejects('zero coordinate scale',lambda:core.coordinates(xx,yy,aa,yy))
 q=SimpleNamespace(N=2,M=2,cl=2,L=1,kappa=2,p=.5,basis='local',meta={'basis_nodes_source':'stored','c':2},data={'c':2,'p':2,'map_exponent_P':2,'result':{'nodes_Fmax':.125}})
 cfg=dict(N=2,M=2,fine=False,state_sha256='a'*64,producer_state_basename='toy.pt')
 md=fake([(1,2,3,4,5,6,7)]*4);md.update({k:np.array(v)for k,v in dict(c=2.,N=2,M=2,fine=False,rule='resolved evaluator (32, 10x16, 400, q=2); rows: M collocation angles',state_file='runs/toy.pt',state_sha256='a'*64,solver_nodes_Fmax=.125).items()})
 core.metadata(md,q,cfg);ck('complete metadata accepted',True)
 mutations=[('extra key',lambda z:z.update(extra=np.array(0))),('missing key',lambda z:z.pop('rule')),('nonscalar',lambda z:z.update(c=np.array([2.]))),('nonunicode',lambda z:z.update(rule=np.array(b'wrong'))),('noninteger N',lambda z:z.update(N=np.array(2.))),('nonbool fine',lambda z:z.update(fine=np.array(0))),('wrong c',lambda z:z.update(c=np.array(3.))),('wrong source hash',lambda z:z.update(state_sha256=np.array('b'*64))),('wrong rule',lambda z:z.update(rule=np.array('other'))),('wrong basename',lambda z:z.update(state_file=np.array('other.pt'))),('wrong residual',lambda z:z.update(solver_nodes_Fmax=np.array(.25)))]
 for name,mut in mutations:
  z=copy.deepcopy(md);mut(z);rejects(name,lambda z=z:core.metadata(z,q,cfg))
 for name,mut in [('raw c',lambda z:z.meta.update(c=3)),('raw dict c',lambda z:z.data.update(c=3)),('map exponent',lambda z:z.data.update(map_exponent_P=3)),('state fine',lambda z:z.data['result'].update(fine=True))]:
  qq=copy.deepcopy(q);mut(qq);rejects(name,lambda qq=qq:core.metadata(md,qq,cfg))
 reg=core.regions(np.array([.01,.2,2.,200.]),np.zeros(4),np.ones((4,5)))
 txt='\n'.join(f'r in [{lo}, {hi}): max |R_h| 1.000e+00   max |R_h|/N_f 1.000e+00'for lo,hi in [('0','0.1'),('0.1','1'),('1','100'),('100','1e300')])
 ck('four printed regions accepted',len(core.printed_table(txt,reg))==8)
 core.printed_value('1.000e+00',1.);ck('printed half ulp accepted',True)
 limit=Q(1)+Q(1,2000);outside=float(limit)
 while Q(outside)<=limit:outside=np.nextafter(outside,math.inf)
 rejects('just outside decimal interval',lambda:core.printed_value('1.000e+00',outside))
 rejects('fewer printed rows',lambda:core.printed_table('\n'.join(txt.splitlines()[:3]),reg));rejects('wrong printed interval label',lambda:core.printed_table(txt.replace('[1, 100)','[2, 100)'),reg))
 rejects('NaN without undefined',lambda:core.printed_value('nan',1.,0));ck('NaN propagation accepted',core.printed_value('nan',1.,1)=='NAN_PROPAGATED_IN_PRODUCER_REGION');rejects('numeric despite undefined',lambda:core.printed_value('1.000e+00',1.,1));rejects('infinite token',lambda:core.printed_value('inf',1.))
 hdr='toy.pt 2x2 c=2.0: solver node |F|max (maps) 1.250e-01;  '+str(md['rule'])+' AT THE SAME NODES (4 points):\n'
 ck('printed header accepted',core.printed_header(hdr,md,cfg))
 for old,new in [('toy.pt','bad.pt'),('2x2','2x3'),('c=2.0','c=3.0'),('(4 points)','(5 points)'),('q=2','q=3')]:rejects('header mutation '+old,lambda old=old,new=new:core.printed_header(hdr.replace(old,new),md,cfg))
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 toy=QLocalCheckpoint.__new__(QLocalCheckpoint);toy.N=2;toy.M=2;toy.L=1;toy.kappa=2;toy.p=.5;toy.basis='local';toy.tk=tk;toy.coeff=[np.array([1.,.125,.03125]),np.array([.05,.01])]
 x=np.array([.17,.83,2.1]);y=np.array([.23,.37,.9]);j=CartesianQJet(toy).jet(x,y);h=1e-4
 def derivative(dx,dy):return(-toy.rho(x+2*h*dx,y+2*h*dy)+8*toy.rho(x+h*dx,y+h*dy)-8*toy.rho(x-h*dx,y-h*dy)+toy.rho(x-2*h*dx,y-2*h*dy))/(12*h)
 target=np.stack([toy.rho(x,y),derivative(1,0),derivative(0,1)],1);err=np.max(abs(j[:,:3]-target));ck('Cartesian jet order independently differentiated nonconstant density',err<2e-10,float(err))
 qq=copy.deepcopy(q);qq.data.pop('map_exponent_P');core.metadata(md,qq,cfg);ck('raw map fallback accepted',True);qq.data['p']=3;rejects('raw map fallback refused',lambda:core.metadata(md,qq,cfg))
 for name,tt in [('wrong origin',np.array([-.9,-.5,.5])),('unsorted',np.array([-1.,.5,-.5])),('one endpoint',np.array([-1.,-.5,1.])),('wrong count',tk[:-1])]:rejects('radial '+name,lambda tt=tt:core.expected_coordinates(tt,2,False,2))
 core.finite_radius(np.array([1.]),np.array([2.]));ck('finite radius accepted',True);rejects('radius cutoff refused',lambda:core.finite_radius(np.array([1e300]),np.array([0.])))
 jets=np.array([[1.,2.,3.],[4.,5.,6.]]);ck('selected jets identity',core.jet_compare(jets,jets)==0);rejects('switched physical derivative labels',lambda:core.jet_compare(jets,jets[:,[0,2,1]]));bad=jets.copy();bad[:,1]*=2;rejects('mapped derivative refused',lambda:core.jet_compare(jets,bad))
 states=[dict(tag='S160',N=160,M=40,fine=False,state='one.pt',state_sha256='a'*64,producer_state_basename='one.pt',producer_export_basename=Path(core.EXPORT_PATHS[0]).name,export_sha256='c'*64),dict(tag='G128',N=128,M=32,fine=True,state='two.pt',state_sha256='b'*64,producer_state_basename='two.pt',producer_export_basename=Path(core.EXPORT_PATHS[1]).name,export_sha256='d'*64)]
 frozen=copy.deepcopy(states);ck('fixed frozen320 identities',core.state_identities(states,frozen));bad=copy.deepcopy(states);bad[0]['state_sha256']='e'*64;rejects('changed frozen state hash',lambda:core.state_identities(bad,frozen));rejects('empty state list',lambda:core.state_identities([],frozen));rejects('reordered state list',lambda:core.state_identities(states[::-1],frozen))
 hs=''.join(h+'  '+p+'\n'for h,p in zip(['c'*64,'d'*64],core.EXPORT_PATHS));ck('ordinary producer hash list',core.hash_list(hs,states))
 for name,text in [('hash mismatch',hs.replace('c'*64,'e'*64)),('one line',hs.splitlines()[0]),('duplicates',hs.splitlines()[0]+'\n'+hs.splitlines()[0]),('binary marker',hs.replace('  artifacts',' *artifacts')),('escaped prefix','\\'+hs),('wrong path',hs.replace('artifacts/data/','artifacts/other/'))]:rejects('hash list '+name,lambda text=text:core.hash_list(text,states))
 ck('source identity pin accepted',source_pin({'bindings':{str(V/'SOURCE_INPUTS.json'):'a'*64}})=='a'*64);rejects('missing source identity pin',lambda:source_pin({'bindings':{}}))
 for p in [__file__,core.__file__,ROOT/'PROOF.md',ROOT/'MANUFACTURE_CORRECTION_PROOF.md',ROOT/'DESIGN_REPAIR_PROOF.md',ROOT/'DESIGN_CLOSURE_PROOF.md',ROOT/'SOURCE_PIN_PROOF.md','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/independent_hydrostatic.py']:bind(p)
 return dict(status='PASS_NEW_EXPORT_RECORD_MANUFACTURES',utc=now(),count=len(checks),checks=checks,bindings=bindings)

def run():
 import torch
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 mf=json.loads(bind(V/'MANUFACTURES.json').read_text());ck('manufacture gate',mf['status']=='PASS_NEW_EXPORT_RECORD_MANUFACTURES'and mf['count']==len(mf['checks'])and all(x['passed']for x in mf['checks']))
 for p,h in mf['bindings'].items():bind(p,h)
 da=json.loads(bind(V/'DESIGN_ACCEPTANCE.json').read_text());ck('design gate',da['status']=='ACCEPTED_FOR_FINITE_RECORD_AUDIT')
 for p,h in da['bindings'].items():bind(p,h)
 sf=json.loads(read_bound(V/'SOURCE_INPUTS.json',source_pin(da)))
 for z in sf['files']:bind(z['frozen'],z['sha256'])
 cfg=json.loads(read_bound(V/'EXPORT_INPUTS.json'));sha=read_bound(cfg['producer_hash_list'],cfg['producer_hash_list_sha256']).decode();ck('exact producer hash list',core.hash_list(sha,cfg['states']));ck('frozen320 state identities',core.state_identities(cfg['states'],sf['states']));out=[]
 for z in sf['states']:
  manifest=json.loads(read_bound(z['manifest'],z['manifest_sha256']));ck('state occurs in bound320 manifest '+z['tag'],any(e.get('frozen')==z['state']and e['sha256']==z['state_sha256']for e in manifest['files']))
 for z in cfg['states']:
  raw=read_bound(z['export'],z['export_sha256'])
  with np.load(io.BytesIO(raw),allow_pickle=False)as f:d={k:f[k].copy()for k in f}
  source=bind(z['state'],z['state_sha256'])
  read_bound(source,z['state_sha256'])
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(source)
  read_bound(source,z['state_sha256']);ck('reader hash equals frozen state '+z['tag'],q.meta['sha256']==z['state_sha256'])
  tag=z['tag'];meta=core.metadata(d,q,z);ck('closed metadata '+tag,True,meta);n=len(d['x'])
  xx,yy=core.expected_coordinates(q.tk,q.M,z['fine'],q.N);relative=core.coordinates(d['x'],d['y'],xx,yy);ck('own coordinates '+tag,True,relative)
  radius=core.finite_radius(d['x'],d['y']);ck('all radii in producer final region extent '+tag,True)
  vals,errors=core.check_rows(d);ck('allnode finite arithmetic '+tag,True,errors);reg=core.regions(d['x'],d['y'],vals);exportreg=core.export_regions(d,vals)
  ids=core.selected(reg,exportreg,n);own=CartesianQJet(q).jet(d['x'][ids],d['y'][ids])[:,:3];prod=np.stack([d['g'][ids],d['g_xi'][ids],d['g_y'][ids]],1);err=core.jet_compare(own,prod);ck('selected own Cartesian jets '+tag,True,err)
  table=read_bound(z['record'],z['record_sha256']).decode();ck('printed header '+tag,core.printed_header(table,d,z));printed=core.printed_table(table,exportreg);ck('printed intervals '+tag,True,printed)
  out.append(dict(tag=tag,points=n,arithmetic=errors,coordinates=relative,exact_operand_regions=reg,export_arithmetic_regions=exportreg,selected_jet_indices=ids,selected_jet_order=['g','d_x_g','d_y_g'],selected_own_jets=own.tolist(),selected_export_jets=prod.tolist(),selected_jet_scaled_max=err,scope='Producer velocities at all nodes. Transport arithmetic assumes exported g_xi means physical d_x g at every node. Exact finite-operand arithmetic; independent Cartesian density jets only at selected indices. Full-node inverse not independently recomputed. Printed comparison is same-run internal consistency, not agreement with an earlier historical table or evidence of historical execution authenticity.'))
 for p,h in list(bindings.items()):bind(p,h)
 return dict(status='PASS_NEW_NODE_EXPORT_RECORDS_REQUIRES_FINAL_REVIEW',utc=now(),count=len(checks),checks=checks,bindings=bindings,states=out,numpy_version=np.__version__,scope='Producer-record consistency only for all-node velocities. No canonical inverse error bound or primary endpoint.')
if __name__=='__main__':
 try:
  if sys.argv[1:]==['--manufactures']:out=manufactures();name='MANUFACTURES.json'
  elif not sys.argv[1:]:out=run();name='CHECKS.json'
  else:raise ValueError('unsupported argument')
  (V/name).write_text(json.dumps(out,indent=2,allow_nan=True)+'\n');print(out['status'],out['count'])
 except Exception:
  (V/('FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')).write_text(json.dumps(dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
