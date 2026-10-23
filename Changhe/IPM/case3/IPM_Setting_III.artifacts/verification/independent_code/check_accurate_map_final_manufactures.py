"""Synthetic complete artifact and adversarial tests for result320 final checker."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os,sys,json,traceback,copy,hashlib
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
import numpy as np
import accurate_map_stage as s
import check_accurate_map_final as f
from larger_node_stage import NodeStore
V=s.V;D=V/'final_manufactures'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');O=D/'candidate';O.mkdir(parents=True)
checks=[];bindings={};beg=s.now()
def ck(name,b,e=None):
 checks.append(dict(name=name,passed=bool(b),evidence=e))
 if not b:raise AssertionError((name,e))
def bind(p):bindings[str(p)]=s.sha(p)
def fail(name,fun):
 try:fun()
 except (AssertionError,ArithmeticError,ValueError,KeyError)as e:ck(name,True,str(e)[:300])
 else:raise AssertionError('unrejected '+name)
def fakephase(tag,label,ids,xy,j,bb):
 fac={'A':1-1e-10,'B':1.,'C':1+1e-10}[label]
 def at(i):
  x,y=xy[i];r=np.hypot(x,y);vel=np.array([.01*x/(1+r),.02*y/(1+r)])*fac
  return dict(velocity=vel,Phi=np.array(0.),dV2dy=np.array(0.),tail_velocity=np.zeros(2),metadata=np.zeros(10),residual=s.rounded_fields(x,y,j[i],vel))
 p=O/(tag+'_'+label+'.npz');a=NodeStore(p,tag+'_'+label,ids,xy,j,s.RULES[label],bb).run(at);return p,a
try:
 for p in [__file__,'independent_code/check_accurate_map_final.py','independent_code/accurate_map_stage.py','independent_code/larger_node_stage.py','independent_code/check_larger_node_final.py','independent_code/larger_node_independent_arithmetic.py','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/scalar_mp_hydrostatic_density.py',s.R/'FINAL_CHECKER_PROOF.md',s.R/'FINAL_GRID_REPRESENTATION_PROOF.md',s.R/'FINAL_COVERAGE_AND_LAUNCH_PROOF.md',s.R/'FINAL_PROVENANCE_AND_COVERAGE_PROOF.md']:bind(p)
 x,r=f.grids();ck('independently constructed probe grid exact',np.array_equal(x,s.probe_grid())and np.array_equal(r,s.probe_nominal_radius()))
 for shift in [False,True]:
  a,b=f.common(shift);c,d=s.common_grid(shift);ck('independent common grid '+str(shift),np.array_equal(a,c)and np.array_equal(b,d))
 states=[];models={};sources={};source_bindings={}
 for tag,cc in [('T',[0.,0.,1.,.5,.25]),('S',[1.,0.,0.,0.,0.])]:
  p=D/(tag+'.npz');np.savez_compressed(p,N=2,M=2,u=np.array(cc),basis=np.array('local'),tk=np.array([-1.,-.5,.5]),cl=2.,L=1.,p=2.);q=f.reader(p);models[tag]=q;sources[p.name]=str(p);source_bindings[str(p)]=s.sha(p)
  ex=f.power_center(q);ce=s.exact_center(q);ck('independent center matches Chebyshev '+tag,ex=={k:F(v)for k,v in ce['exact'].items()})
  want=dict(a=F(1),b=F(-428,3),e=F(-436,3),cH=F(17,12),delta=F(29,12),K=F(1,8))if tag=='T'else dict(a=F(1),b=F(-16),e=F(-16),cH=F(-1),delta=F(0),K=F(1,2))
  ck('hand rational center '+tag,all(ex[k]==v for k,v in want.items()))
  if tag=='S':ck('exact zero center limit',ex['delta']==ex['axis_limit']==0)
 cfg=dict(states=[['T','T.npz',2,2]],standards=[['S','S.npz',2,2]],sources=sources,pairs=[['T','S']],angular_tags=['T']);s.put(D/'FIXTURE.json',cfg)
 c=dict(status='COMPLETE_FINITE_ACCURATE_MAP_REQUIRES_FINAL_AUDIT',count=1,checks=[dict(name='synthetic only',passed=True)],bindings=source_bindings,artifacts={},states=[],angular=[],function_comparisons=[],versions=dict(python=sys.version,numpy=np.__version__,torch='synthetic'))
 def art(p):c['artifacts'][str(p)]=s.sha(p)
 tag='T';q=models[tag];j=f.CartesianQJet(q).jet(x[:,0],x[:,1]);tp=O/(tag+'_targets.npz');s.save_array(tp,dict(xy=x,jets=j));bb=dict(source_bindings);bb[str(tp)]=s.sha(tp);art(tp)
 bp,B=fakephase(tag,'B',list(range(len(x))),x,j,bb);art(bp);sel=s.select(x,j,B);sp=O/(tag+'_SELECTION.json');s.put(sp,sel);art(sp);ids=sel['indices'];ab=dict(bb);ab[str(sp)]=s.sha(sp);ap,A=fakephase(tag,'A',ids,x,j,ab);cp,C=fakephase(tag,'C',ids,x,j,ab);art(ap);art(cp)
 comps=[]
 for pos,i in enumerate(ids):
  d=s.pair_spreads(x[i],j[i],[A['velocity'][pos],B['velocity'][i],C['velocity'][pos]]);d.update(index=i,x=float(x[i,0]),y=float(x[i,1]));comps.append(d)
 ce=s.exact_center(q);ce['bindings']=bb;cep=O/(tag+'_CENTER.json');s.put(cep,ce);art(cep)
 mp=dict(bindings=bb,results=s.local_mp(q,x,j,ids));mpp=O/(tag+'_LOCAL_MP.json');s.put(mpp,mp);art(mpp)
 failed=[dict(index=z['index'],component=k,diagnostic=d)for z in mp['results']for k,d in enumerate(z['diagnostics'])if not d['precision_pass']]
 record=dict(tag=tag,N=2,M=2,source_path=str(q.path),source_sha256=s.sha(q.path),points=len(x),regions=s.regional(x,B['residual']),extents={str(e):s.regional(x,B['residual'],e)for e in s.EXTENTS},selected=sel,comparisons=comps,center=ce['rounded'],mp_precision_all_pass=not failed,mp_precision_failures=failed,arithmetic_counts=dict(B=5*len(x),A=5*len(ids),C=5*len(ids)),extent_rounding=s.extent_rounding(x,s.probe_nominal_radius()),center_inverse=s.center_inverse_diagnostics(x,B,ce));rp=O/(tag+'_COMPLETE.json');s.put(rp,record);art(rp);c['states'].append(record)
 ax,dense,coll,blocks=s.angular_grid(2);aj=f.CartesianQJet(q).jet(ax[:,0],ax[:,1]);at=O/'T_angular_targets.npz';s.save_array(at,dict(xy=ax,jets=aj,dense=dense,collocation=coll));art(at);bb=dict(source_bindings);bb[str(at)]=s.sha(at);bp,Ba=fakephase('T_angular','B',list(range(len(ax))),ax,aj,bb);art(bp)
 aa=s.angular_summary(dense,coll,blocks,Ba['residual'],2);ii=sorted({z[k]for z in aa for k in ['dense_argmax','collocation_argmax']});sp2=O/'T_angular_SELECTION.json';s.put(sp2,dict(indices=ii,reason='dense and direct collocation Rf maxima on each of four rings'));art(sp2);ab=dict(bb);ab[str(sp2)]=s.sha(sp2);ap,Aa=fakephase('T_angular','A',ii,ax,aj,ab);cp,Ca=fakephase('T_angular','C',ii,ax,aj,ab);art(ap);art(cp);co=[]
 for k,i in enumerate(ii):d=s.pair_spreads(ax[i],aj[i],[Aa['velocity'][k],Ba['velocity'][i],Ca['velocity'][k]]);d['index']=i;co.append(d)
 z=dict(tag='T',rows=len(ax),summary=aa,comparisons=co);p=O/'T_ANGULAR.json';s.put(p,z);art(p);c['angular'].append(z)
 for shift in [False,True]:
  name='shifted'if shift else'common';fx,rr=s.common_grid(shift);vals={tag:f.CartesianQJet(q).jet(fx[:,0],fx[:,1])[:,:3]for tag,q in models.items()};p=O/(name+'_fields.npz');s.save_array(p,dict(xy=fx,nominal_radius=rr,**vals));art(p)
  z=dict(grid=name,points=len(fx),records=[dict(pair=['T','S'],legacy_denominator_state='S',orientation_scope='Verifier-chosen ordered pair; producer comparison orientation is not asserted here.',regions=s.function_difference(vals['T'],vals['S'],rr))],radius_scope='nominal grid radius, half-open masks; final radius1e7 excluded from far_high');p=O/(name+'_COMPARISONS.json');s.put(p,z);art(p);c['function_comparisons'].append(z)
 s.put(O/'COMPLETE.json',c);a=f.Audit(D,True);a.run();ck('integrated all artifact path',len(a.checks)>200 and a.scalars>5000,dict(checks=len(a.checks),scalars=a.scalars));s.put(D/'INTEGRATED_CHECKS.json',dict(status='PASS_SYNTHETIC_INTEGRATED',count=len(a.checks),checks=a.checks,scalar_assertion_count=a.scalars,bindings=a.bindings,outputs=a.outputs))
 fail('extra comparison row refused',lambda:f.Audit(D,True).checked_spreads(x,j,ids,A,B,C,comps+[comps[-1]]))
 # Exact arithmetic and metadata perturbations are presented with freshly bound corrupted artifacts, so checksum checks cannot mask them.
 audit=f.Audit(D,True);audit.candidate=c
 bp=O/'T_B.npz';orig=bp.read_bytes();base=f.arrays(bp);bb=json.loads(str(base['manifest']))['bindings']
 def mutation(name,change):
  z={k:v.copy()for k,v in base.items()};change(z);s.save_array(bp,z);audit.candidate['artifacts'][str(bp)]=s.sha(bp);audit.bindings={};audit.aliases={};fail(name,lambda:audit.phase(bp,'T','B',list(range(len(x))),x,j,bb));bp.write_bytes(orig);audit.candidate['artifacts'][str(bp)]=s.sha(bp)
 mutation('one ulp residual refused',lambda z:z['residual'].__setitem__((13,0),np.nextafter(z['residual'][13,0],np.inf)))
 mutation('wrong snapshot index refused',lambda z:z['indices'].__setitem__(0,1))
 mutation('wrong target coordinate refused',lambda z:z['xy'].__setitem__((13,0),np.nextafter(z['xy'][13,0],np.inf)))
 def wrongmanifest(z):
  m=json.loads(str(z['manifest']));m['rule']['order']=65;z['manifest']=np.array(json.dumps(m))
 mutation('wrong quadrature rule refused',wrongmanifest)
 wrong=copy.deepcopy(sel);wrong['indices']=wrong['indices'][1:];ck('changed selection detected',wrong!=f.selector(x,j,B))
 z=copy.deepcopy(mp['results'][0]);z['decimal']['108'][0]='NaN';fail('nonfinite MP decimal refused',lambda:f.mp_diagnostics(z,j[z['index']]))
 z=copy.deepcopy(mp['results'][0]);z['diagnostics'][0]['precision_pass']=not z['diagnostics'][0]['precision_pass'];ck('corrupted MP flag detected',f.mp_diagnostics(z,j[z['index']])!=z['diagnostics'])
 toyx=np.array([[.05,0],[.05,0],[.1,0],[1,0],[100,0],[1e4,0],[1e7,0]],float);toyr=np.tile([1.,0.,0.,np.nan,np.nan],(7,1));sums=f.regional(toyx,toyr);ck('half-open and first tie and undefined oracle',[z['count']for z in sums]==[2,1,1,3]and sums[0]['metrics']['absR']['index']==0 and sum(z['metrics']['Rf']['undefined_count']for z in sums)==7);ck('empty regions',all(z['count']==0 for z in f.regional(np.empty((0,2)),np.empty((0,5)))))
 aa=np.array([[0.,0.,0.],[1.,2.,3.],[3.,1.,2.]]);bb0=np.array([[0.,0.,0.],[2.,4.,6.],[4.,1.,2.]]);rr=np.array([.01,2.,3.]);dif=f.differences(aa,bb0,rr);ck('independent function hand oracle',dif[2]['metrics']['pure_relative']['value']==.5 and dif[2]['metrics']['weighted_density']['value']==1/np.sqrt(3)and dif[0]['both_zero_count']==1)
 # Exercise semantic refusals with outer checksums and serialized records freshly updated.
 original_c=copy.deepcopy(c);all_original={Path(p):Path(p).read_bytes()for p in c['artifacts']};complete_original=(O/'COMPLETE.json').read_bytes()
 def whole(name,change,expected):
  cc=copy.deepcopy(original_c)
  try:
   change(cc)
   for pp in list(cc['artifacts']):cc['artifacts'][pp]=s.sha(pp)
   s.put(O/'COMPLETE.json',cc)
   try:f.Audit(D,True).run()
   except(AssertionError,ValueError,KeyError)as e:ck(name,expected in str(e),str(e)[:320])
   else:raise AssertionError('not refused '+name)
  finally:
   for pp,data in all_original.items():pp.write_bytes(data)
   (O/'COMPLETE.json').write_bytes(complete_original)
 def jsonchange(filename,fn,section=None,index=0):
  def apply(cc):
   pp=O/filename;dd=json.loads(pp.read_text());fn(dd);s.put(pp,dd)
   if section:cc[section][index]=dd
  return apply
 def arraychange(filename,fn):
  def apply(cc):pp=O/filename;dd=f.arrays(pp);fn(dd);s.save_array(pp,dd)
  return apply
 def firstrow(d):d['indices']=d['indices'][1:]
 whole('run rejects changed selection',jsonchange('T_SELECTION.json',firstrow),'independent selection')
 for field,value in [('label','other'),('status','PARTIAL'),('completed',1),('total',1)]:
  def edit(z,field=field,value=value):m=json.loads(str(z['manifest']));m[field]=value;z['manifest']=np.array(json.dumps(m))
  whole('run rejects manifest '+field,arraychange('T_B.npz',edit),'snapshot complete')
 def changed_binding(z):m=json.loads(str(z['manifest']));m['bindings']={};z['manifest']=np.array(json.dumps(m))
 whole('run rejects phase bindings',arraychange('T_B.npz',changed_binding),'exact phase binding')
 whole('run rejects MP failure counter',jsonchange('T_COMPLETE.json',lambda d:d.__setitem__('mp_precision_all_pass',not d['mp_precision_all_pass']),'states'),'MP failure coverage')
 whole('run rejects MP failure list',jsonchange('T_COMPLETE.json',lambda d:d.__setitem__('mp_precision_failures',[{}]),'states'),'MP failure coverage')
 whole('run rejects missing MP index',jsonchange('T_LOCAL_MP.json',lambda d:d['results'].pop()),'MP binding/coverage')
 for field in ['x','double']:
  def edit(d,field=field):
   z=d['results'][0]
   if field=='x':z['x']=float(np.nextafter(z['x'],np.inf))
   else:z['double'][0]=float(np.nextafter(z['double'][0],np.inf))
  whole('run rejects MP '+field,jsonchange('T_LOCAL_MP.json',edit),'MP target')
 for field,value in [('sign_changes',999),('dominant_k',999),('collocation_interpolated_max',999.),('condition_number',999.)]:
  def edit(d,field=field,value=value):d['summary'][0][field]=value
  whole('run rejects angular '+field,jsonchange('T_ANGULAR.json',edit,'angular'),'independent angular QR'if field=='condition_number'else'angular finite summaries')
 def fitwrong(d):d['summary'][0]['fit_coefficients'][0]+=1.
 whole('run rejects angular coefficient',jsonchange('T_ANGULAR.json',fitwrong,'angular'),'independent angular QR')
 whole('run rejects angular selection',jsonchange('T_angular_SELECTION.json',firstrow),'angular selected rows')
 def badmetric(d):d['records'][0]['regions'][0]['metrics']['weighted_density']['value']+=1
 whole('run rejects function metric',jsonchange('common_COMPARISONS.json',badmetric,'function_comparisons'),'independent function metrics')
 whole('run rejects function denominator',jsonchange('common_COMPARISONS.json',lambda d:d['records'][0].__setitem__('legacy_denominator_state','T'),'function_comparisons'),'independent function metrics')
 whole('run rejects function pair order',jsonchange('common_COMPARISONS.json',lambda d:d['records'][0].__setitem__('pair',['S','T']),'function_comparisons'),'function serialized record')
 whole('run rejects common field',arraychange('common_fields.npz',lambda d:d['T'].__setitem__((1,0),float(np.nextafter(d['T'][1,0],np.inf)))),'common jet reconstruction')
 whole('run rejects exact center',jsonchange('T_CENTER.json',lambda d:d['exact'].__setitem__('cH','0')),'independent exact power center')
 whole('run rejects center rounding',jsonchange('T_CENTER.json',lambda d:d['rounded'].__setitem__('cH',float(np.nextafter(d['rounded']['cH'],np.inf)))),'center rounding and bindings')
 whole('run rejects center inverse diagnostic',jsonchange('T_COMPLETE.json',lambda d:d['center_inverse'][0]['comparisons']['Rf'].__setitem__('observed',999.),'states'),'center inverse diagnostics')
 whole('run rejects extent rounding',jsonchange('T_COMPLETE.json',lambda d:d['extent_rounding'][0].__setitem__('physical_count',0),'states'),'regional and extent maxima')
 extra=O/'extra.txt';extra.write_text('unused')
 whole('run rejects unused artifact',lambda cc:cc['artifacts'].__setitem__(str(extra),s.sha(extra)),'all candidate artifacts used');extra.unlink()
 extra=D/'outside.txt';extra.write_text('outside')
 whole('run rejects outside artifact',lambda cc:cc['artifacts'].__setitem__(str(extra),s.sha(extra)),'artifact inside candidate')
 whole('run rejects source hash',lambda cc:cc['bindings'].__setitem__(str(models['T'].path),'0'*64),'binding ')
 ck('integrated common grid both-zero density case',a.outputs['function_comparisons'][0]['records'][0]['regions'][0]['both_zero_count']>0)
 for p,h in list(bindings.items()):ck('stable '+p,s.sha(p)==h)
 s.put(V/'FINAL_MANUFACTURES.json',dict(status='PASS_INDEPENDENT_ACCURATE_MAP_FINAL_MANUFACTURES',started_utc=beg,finished_utc=s.now(),count=len(checks),checks=checks,bindings=bindings,fixture=str(D),scope='Synthetic algebraic fields and corrupted artifacts. Fake velocities are deliberately not claimed to approximate an inverse. No320candidate execution.'))
 print('PASS_INDEPENDENT_ACCURATE_MAP_FINAL_MANUFACTURES',len(checks),flush=True)
except Exception:
 s.put(D/'FAILURE.json',dict(utc=s.now(),checks=checks,bindings=bindings,error=traceback.format_exc()));raise
