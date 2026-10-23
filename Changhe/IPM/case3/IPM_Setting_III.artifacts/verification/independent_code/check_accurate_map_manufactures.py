"""Manufactured arithmetic, reconstruction, grid, inverse, and resume checks."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os,sys,json,hashlib,ast,math,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
import numpy as np
import accurate_map_stage as stage
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
V=stage.V;D=V/('manufactures_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));D.mkdir(parents=True)
checks=[];bindings={}
def ck(name,b,e=None):
 checks.append(dict(name=name,passed=bool(b),evidence=e))
 if not b:raise AssertionError((name,e))
def bind(p,h=None):
 p=str(p);v=stage.sha(p);ck('binding '+p,h is None or v==h);bindings[p]=v
try:
 for p in [__file__,'independent_code/accurate_map_stage.py','independent_code/run_accurate_map_audit.py','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/node_export_inverse_stage.py','independent_code/larger_node_stage.py','independent_code/larger_node_independent_arithmetic.py','independent_code/scalar_mp_hydrostatic_density.py',stage.R/'PROOF.md',stage.R/'EXECUTION_PROOF.md']:bind(p)
 for name in ['IMPORT_AND_CACHE_CORRECTION_PROOF.md','NONCONSTANT_MANUFACTURE_PROOF.md','RECORD_AUDIT_PROOF.md','RECORD_SCHEMA_CORRECTION_PROOF.md','DESIGN_REVIEW_RESOLUTION_PROOF.md']:bind(stage.R/name)
 for p in ['independent_code/accurate_map_stage.py','independent_code/run_accurate_map_audit.py']:ast.parse(Path(p).read_text());ck('Python syntax '+p,True)
 for name,status in [('MANUFACTURES.json','PASS_LARGER_NODE_MANUFACTURES'),('MP_STAGE_MANUFACTURES.json','PASS_MP_GEOMETRY_MOMENTS_AND_REAL_RESTART'),('FINAL_ARITHMETIC_MANUFACTURES.json','PASS_INDEPENDENT_FINITE_ARITHMETIC_MANUFACTURES')]:
  p=Path('research/hydrostatic_larger_node_audit/verification')/name;bind(p);d=json.loads(p.read_text());ck('reused semantic manufacture '+name,d['status']==status and d['count']==len(d['checks'])and all(z['passed']for z in d['checks']))
  for p,h in d['bindings'].items():bind(p,h)
 xy=stage.probe_grid();rad=np.hypot(*xy.T);ck('probe count and finite',xy.shape==(826,2)and np.isfinite(xy).all(),list(xy.shape));ck('actual axes',(xy[:,0]==0).sum()==55 and(xy[:,1]==0).sum()==55);ck('probe extent coverage',rad.min()<=1e-6 and rad.max()<=1e7*(1+1e-15)and all(np.any(rad==e)for e in [100,1e4,1e7]))
 nominal=stage.probe_nominal_radius();ext=stage.extent_rounding(xy,nominal)
 ck('nominal radius count',nominal.shape==(826,))
 for z in ext:
  e=z['extent'];ii=[i for i in range(len(xy))if nominal[i]<=e and math.hypot(*xy[i])>e];oo=[i for i in range(len(xy))if nominal[i]>e and math.hypot(*xy[i])<=e]
  # numpy hypot is the declared physical classifier; independent scalar numpy calls avoid a second algorithm's rounding differences.
  ii=[i for i in range(len(xy))if nominal[i]<=e and np.hypot(float(xy[i,0]),float(xy[i,1]))>e];oo=[i for i in range(len(xy))if nominal[i]>e and np.hypot(float(xy[i,0]),float(xy[i,1]))<=e]
  ck('extent rounding count '+str(e),z['nominal_in_physical_out']==ii and z['nominal_out_physical_in']==oo and z['nominal_count']-z['physical_count']==len(ii)-len(oo),z)
 edge=stage.extent_rounding(np.array([[np.nextafter(100.,np.inf),0.],[100.,0.]]),np.array([100.,np.nextafter(100.,np.inf)]),[100.])[0]
 ck('both boundary rounding directions',edge['nominal_in_physical_out']==[0]and edge['nominal_out_physical_in']==[1])
 import torch
 source_map={}
 for name in ['INPUTS.json','INPUTS_SUPPLEMENT.json','INPUTS_ADDITIONAL.json']:
  p=V/name;bind(p)
  for z in json.loads(p.read_text())['files']:source_map[Path(z['frozen']).name]=z
 for name,N,M in [('standard96.pt',96,24),('standard128c.pt',128,32),('hsG_c2.0_N160_log.pt',160,40)]:
  z=source_map[name];bind(z['frozen'],z['sha256'])
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q0=QLocalCheckpoint(z['frozen'])
  ck('standard state explicit admission '+name,(q0.N,q0.M)==(N,M)and q0.cl==2 and q0.kappa==2 and q0.L==1 and q0.p==.5 and q0.basis=='local'and q0.meta['basis_nodes_source']=='stored'and np.isfinite(q0.u).all(),dict(N=q0.N,M=q0.M,cl=q0.cl,kappa=q0.kappa,L=q0.L,p=q0.p,basis=q0.basis))
 for shift,want in [(False,19649),(True,18659)]:
  a,r=stage.common_grid(shift);ck('common dimensions '+str(shift),a.shape==(want,2)and r.shape==(want,)and np.isfinite(a).all());ck('nominal/hypot agreement '+str(shift),np.allclose(np.hypot(*a.T),r,rtol=3e-16,atol=0))
 # Deliberate discontinuous values exercise closed extents, half-open regions, ties, and undefined axes.
 x=np.array([[.05,0],[.05,0],[.1,0],[1,0],[100,0],[1e4,0],[1e7,0]],float);j=np.zeros((7,4));v=np.zeros((7,2));rr=np.array([stage.rounded_fields(*a,b,c)for a,b,c in zip(x,j,v)]);rr[:,0]=1
 sums=stage.regional(x,rr);ck('first tied maximum',sums[0]['metrics']['absR']['index']==0);ck('undefined counts',sum(z['metrics']['Rf']['undefined_count']for z in sums)==7);ck('half-open region counts',[z['count']for z in sums]==[2,1,1,3]);ck('closed extent includes100',sum(z['count']for z in stage.regional(x,rr,100))==5)
 empty=stage.regional(np.empty((0,2)),np.empty((0,5)));ck('empty regions',all(z['count']==0 and z['metrics']['Rf']['index']is None for z in empty))
 # A hand residual oracle is evaluated independently of the stage implementation.
 qrow=stage.rounded_fields(1,2,[4,5,-3,0],[2,7]);ck('manual R/Nf/Nv',np.array_equal(qrow,np.array([-17,57,16,17/57,17/16])))
 ck('independent arithmetic accepts',stage.audit_rows(np.array([[1.,2.]]),np.array([[4.,5.,-3.,0.]]),dict(velocity=np.array([[2.,7.]]),residual=qrow[None,:]),[0])==5)
 bad=qrow.copy();bad[0]=np.nextafter(bad[0],np.inf)
 try:stage.audit_rows(np.array([[1.,2.]]),np.array([[4.,5.,-3.,0.]]),dict(velocity=np.array([[2.,7.]]),residual=bad[None,:]),[0])
 except ArithmeticError:ck('one-ulp arithmetic rejected',True)
 else:raise AssertionError('one-ulp accepted')
 # Gaussian moments have a closed, separately integrated full inverse.
 def gaussian(x,y):
  x,y=np.broadcast_arrays(x,y);a=1+x*x;f=np.exp(-y*y)
  return np.stack([y*f/a,-2*x*y*f/a**2,(1-2*y*y)*f/a,(6*x*x-2)*y*f/a**3],axis=-1)
 for label,rule in stage.RULES.items():
  for x0,y0 in [(0.,0.),(.25,.4),(1.,2.),(-.5,.8),(.3,-.7)]:
   z=stage.evaluate(gaussian,x0,y0,.5,rule);a=1+x0*x0;b=(6*x0*x0-2)/a**3;want=[x0/a**2*math.exp(-y0*y0),b*math.sqrt(math.pi)*math.erf(y0)/4]
   ck('Gaussian inverse '+str((label,x0,y0)),np.max(abs(z['V']-want))<3e-13)
 # q0=1 yields g=y*w, w+16*r^2*w^4=1. Its exact center expansion is a=1,b=e=-16,cH=-1.
 source=D/'constant_mode.npz';np.savez_compressed(source,N=2,M=1,u=np.array([1.,0.,0.]),basis=np.array('local'),tk=np.array([-1.,-.5,.5]),cl=2.,L=1.,p=2.)
 q=QLocalCheckpoint(source);c=stage.exact_center(q);ck('exact polynomial center oracle',{k:F(c['exact'][k])for k in ['a','b','e','cH','delta','K','cubic_residual']}==dict(a=F(1),b=F(-16),e=F(-16),cH=F(-1),delta=F(0),K=F(1,2),cubic_residual=F(-80,3)))
 # Nonconstant radial mode and nonzero angular mode check the derivative and affine-basis terms.
 source2=D/'nonconstant_modes.npz';np.savez_compressed(source2,N=2,M=2,u=np.array([0.,0.,1.,.5,.25]),basis=np.array('local'),tk=np.array([-1.,-.5,.5]),cl=2.,L=1.,p=2.)
 q2=QLocalCheckpoint(source2);c2=stage.exact_center(q2);got={k:F(c2['exact'][k])for k in ['a','b','e','cH','delta','K']}
 ck('nonconstant exact center and shifted mode oracle',got==dict(a=F(1),b=F(-428,3),e=F(-436,3),cH=F(17,12),delta=F(29,12),K=F(1,8)),{k:str(v)for k,v in got.items()})
 parity_points=np.array([[.03,.07],[-.03,.07],[.03,-.07],[-.03,-.07],[0.,0.],[100.,-200.],[-.125,0.],[0.,-.125]])
 jet2=CartesianQJet(q2).jet;par=jet2(*parity_points.T)
 ck('nonconstant exact x reflection',np.array_equal(jet2(-parity_points[:,0],parity_points[:,1]),par*[1,-1,1,1]))
 ck('nonconstant exact y reflection',np.array_equal(jet2(parity_points[:,0],-parity_points[:,1]),par*[-1,-1,1,-1]))
 pp=np.array([[0.,.125],[0.,.25],[.5,0.]])
 fake=dict(velocity=np.array([[0.,.125],[0.,.5],[0.,0.]]),residual=np.array([[.25,2.,3.,.125,0.],[.75,3.,4.,.25,0.],[0.,0.,0.,np.nan,np.nan]]))
 cc=dict(exact=dict(cH='1',a='2',delta='1',axis_limit='1/3'))
 cd=stage.center_inverse_diagnostics(pp,fake,cc)
 ck('center inverse diagnostic oracle',[z['index']for z in cd]==[0,1]and cd[0]['comparisons']['V2_over_y']['difference']==0 and cd[0]['comparisons']['R_over_y']['difference']==0 and cd[1]['comparisons']['R_over_y']['difference']==1 and cd[0]['comparisons']['Rf']['difference']==float(F(1,8)-F(1,3)))
 points=np.array([[.003,.007],[.4,.8],[100.,200.],[0.,.125],[.125,0.],[0.,0.]]);jet=CartesianQJet(q).jet;jj=jet(*points.T);mp=stage.local_mp(q,points,jj,list(range(len(points))));ck('scalar MP precision oracle',all(d['precision_pass']for z in mp for d in z['diagnostics']));ck('Cartesian and scalar derivatives',max(d['double_abs']/max(1.,abs(z['double'][k]))for z in mp for k,d in enumerate(z['diagnostics']))<1e-12)
 # Formula implicit derivative at r=.5: w_x=-32*x*w^4/(1+64*r^2*w^3).
 x0,y0=.3,.4;w=q.coordinates(np.hypot(x0,y0))[2];wx=-32*x0*w**4/(1+64*(x0*x0+y0*y0)*w**3);ck('implicit Cartesian gx',abs(jet(x0,y0)[1]-y0*wx)<2e-15)
 sf=D/'B.npz';p2=points[:3];j2=jj[:3];snap=stage.phase(sf,'synthetic','B',np.arange(3),p2,j2,jet,.5,{'test':'constant'});old=sf.read_bytes();again=stage.phase(sf,'synthetic','B',np.arange(3),p2,j2,jet,.5,{'test':'constant'});ck('completed replay stable bytes',sf.read_bytes()==old and np.array_equal(again['residual'],snap['residual'],equal_nan=True))
 # The sign-count and Fourier mode routine receives an exact sampled cosine, separately from transport.
 ax,dense,coll,records=stage.angular_grid(4);rows=np.zeros((len(ax),5));rows[:,1]=1
 for z in records:
  begin=z['start'];angles=np.r_[dense,coll];rows[begin:begin+z['total'],0]=np.cos(8*angles)
 angular=stage.angular_summary(dense,coll,records,rows,4);ck('known angular mode',all(z['dominant_k']==4 and z['sign_changes']==4 and z['collocation_direct_max']<2e-15 and z['dense_max']>.9 for z in angular))
 a=np.array([[0.,0.,0.],[1.,2.,3.],[3.,1.,2.]]);b=np.array([[0.,0.,0.],[2.,4.,6.],[4.,1.,2.]]);r=np.array([.01,2.,3.]);d=stage.function_difference(a,b,r);ann=d[2]['metrics'];ck('function weighted and relative oracle',ann['weighted_density']['value']==1/np.sqrt(3)and ann['pure_relative']['value']==.5 and ann['legacy_new_denominator_relative']['value']==.5 and ann['weighted_gradient']['value']==np.sqrt(13)*np.sqrt(3));ck('both-zero function handling',d[0]['both_zero_count']==1 and d[0]['metrics']['pure_relative']['value']==0)
 for p,h in bindings.items():ck('stable '+p,stage.sha(p)==h)
 stage.put(V/'MANUFACTURES.json',dict(status='PASS_ACCURATE_MAP_MANUFACTURES',utc=stage.now(),count=len(checks),checks=checks,bindings=bindings,fixture=str(D),scope='Synthetic fields, known moments, exact center and independent scalar derivatives; no accurate-map candidate evaluation.'))
 print('PASS_ACCURATE_MAP_MANUFACTURES',len(checks))
except Exception:
 stage.put(D/'FAILURE.json',dict(utc=stage.now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
