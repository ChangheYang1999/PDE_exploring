"""Two-node integrated final checker manufacture; no real candidate writes."""
from pathlib import Path
from datetime import datetime,timezone
import os,sys,json,hashlib,time,subprocess,shutil,traceback,copy,gzip
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import numpy as np
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from larger_node_stage import coordinates,NodeStore,rounded_fields,summaries,selection,pair_spreads,coordinate_diagnostics
from node_export_inverse_stage import evaluate,RULES,META
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';D=V/'mp_driver_manufactures'/('final_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));D.mkdir(parents=True);v=D/'full';c=v/'candidate';c.mkdir(parents=True)
now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];bindings={};start=now();tick=time.monotonic()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def put(p,d):p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def load(p):
 with np.load(p,allow_pickle=False)as z:return {k:z[k]for k in z.files}
def npz(p,d):
 with p.open('wb')as f:np.savez_compressed(f,**d)
def run(args,log,expected=None):
 z=subprocess.run([sys.executable]+args,capture_output=True,text=True,timeout=240);log.write_text(z.stdout+z.stderr);ck('subprocess '+log.name,z.returncode==0 if expected is None else z.returncode!=0 and expected in z.stdout+z.stderr,dict(returncode=z.returncode,expected=expected,log=str(log)))
try:
 for p in [__file__,'independent_code/check_larger_node_final.py','independent_code/larger_node_independent_arithmetic.py',R/'FINAL_CHECKER_ASSEMBLY_PROOF.md',R/'FINAL_CHECKER_SCHEMA_NOTE.md',R/'FINAL_CHECKER_TAMPER_SUPPLEMENT_PROOF.md',V/'FINAL_ARITHMETIC_MANUFACTURES.json']:
  bindings[str(p)]=sha(p)
 source=v/'synthetic.npz';np.savez_compressed(source,N=2,M=1,u=np.array([1.,0.,0.]),basis=np.array('local'),tk=np.array([-1.,-.5,.5]),cl=2.,L=1.,p=2.)
 q=QLocalCheckpoint(source);xy=coordinates(q);jet=CartesianQJet(q).jet;jets=jet(xy[:,0],xy[:,1]);npz(c/'N2_targets.npz',dict(xy=xy,jets=jets));arr={}
 for label in ['B','A','C']:
  def compute(i):
   z=evaluate(jet,*xy[i],q.p,RULES[label]);return dict(velocity=z['V'],Phi=z['Phi'],dV2dy=z['dV2_dy'],tail_velocity=z['tail_V'],metadata=z['meta'],residual=rounded_fields(*xy[i],jets[i],z['V']))
  arr[label]=NodeStore(c/('N2_'+label+'.npz'),'N2_'+label,[0,1],xy,jets,RULES[label],{}).run(compute)
 src=dict(N=2,M=1,path=str(source),sha256=sha(source));put(v/'INPUTS.json',dict(states=[src]));shutil.copyfile(V/'MP_STAGE_MANUFACTURES.json',v/'MP_STAGE_MANUFACTURES.json');put(v/'MP_DESIGN_ACCEPTANCE.json',dict(status='SYNTHETIC_TEST_ONLY',bindings={str(Path(__file__)):sha(__file__)}))
 sel=selection(xy,jets,arr['B'],np.array([.1,.2]));rr=np.hypot(xy[:,0],xy[:,1]);sel.update(B_sha256=sha(c/'N2_B.npz'),target_sha256=sha(c/'N2_targets.npz'),proxy_step='2^-10 max(1,r)',scope='Synthetic selector only',selected_h_over_r={str(i):float(max(1,rr[i])*2**-10/rr[i])for i in sel['indices']});put(c/'N2_SELECTION.json',sel)
 comp=[]
 for i in sel['indices']:
  d=pair_spreads(xy[i],jets[i],[arr[k]['velocity'][i]for k in ['A','B','C']]);d.update(index=i,x=float(xy[i,0]),y=float(xy[i,1]));comp.append(d)
 state=dict(N=2,M=1,points=2,source=src,selected=sel,local_mp_indices=[0,1],integrand_mp_indices=[int(np.argmax(arr['B']['residual'][:,3]))],region_summaries=summaries(xy,arr['B']['residual']),comparisons=comp,metadata_columns=META,coordinate_diagnostics=coordinate_diagnostics(q,xy));put(c/'N2_COMPLETE.json',state)
 files=[c/('N2_'+s)for s in ['targets.npz','A.npz','B.npz','C.npz','SELECTION.json','COMPLETE.json']];complete=dict(status='COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW',count=1,checks=[dict(name='synthetic_only',passed=True)],bindings={},artifacts={str(p):sha(p)for p in files},results=[state]);put(c/'COMPLETE.json',complete)
 run(['independent_code/launch_larger_node_mp.py','--fixture',str(v)],v/'mp_wrapper.log')
 run(['independent_code/check_larger_node_final.py','--fixture',str(v)],v/'final_checker.log')
 result=json.loads((v/'FINAL_ARITHMETIC_CHECKS.json').read_text());ck('integrated synthetic success',result['status']=='PASS_SYNTHETIC_FINAL_ARITHMETIC'and result['synthetic_only']and result['scalar_assertion_count']>40 and all(z['passed']for z in result['checks']))
 # Mutating only a bound artifact tests fail-closed input admission. Exact arithmetic corruptions are checked below without reusing candidate summaries.
 p=c/'N2_B.npz';raw=p.read_bytes();d=load(p);d['residual'][0,0]=np.nextafter(d['residual'][0,0],np.inf);npz(p,d);run(['independent_code/check_larger_node_final.py','--fixture',str(v)],v/'bound_mutation.log','binding ');p.write_bytes(raw)
 # Exercise independent arithmetic/selection rejection directly on isolated temporary snapshot bytes, with a fresh declared digest.
 from check_larger_node_final import Audit
 local=Audit(v,True);d=load(p);d['residual'][0,0]=np.nextafter(d['residual'][0,0],np.inf);bad=v/'one_ulp_B.npz';npz(bad,d)
 try:local.load_snapshot(bad,'N2','B',[0,1],xy,jets,{str(bad):sha(bad)})
 except ArithmeticError as e:ck('one-ulp arithmetic rejection independent of digest','rounded arithmetic'in str(e))
 else:raise AssertionError('one-ulp residual accepted')
 d=load(c/'N2_C.npz');d['indices']=d['indices'][::-1];bad=v/'wrong_C_order.npz';npz(bad,d)
 try:Audit(v,True).load_snapshot(bad,'N2','C',[0,1],xy,jets,{str(bad):sha(bad)})
 except AssertionError as e:ck('changed selection rejected','snapshot indices and targets'in str(e))
 else:raise AssertionError('reversed C accepted')
 # Deliberately self-consistent record/digest corruptions must fail independently reconstructed arithmetic.
 mpfile=v/'mp'/'COMPLETE.json';mpristine=mpfile.read_bytes();mo=json.loads(mpristine);wi=mo['results'][0]['witnesses'][0]['index'];wp=v/'mp'/('N2_witness_'+str(wi)+'.json');wpristine=wp.read_bytes()
 for typ,expected in [('ledger','independent signed moment/component ledgers'),('component','six exact component decompositions')]:
  mw=json.loads(wpristine)
  if typ=='ledger':mw['ledgers']['D']['components']['V1']['total']='123'
  else:mw['components'][0]['total']='123'
  put(wp,mw);mc=copy.deepcopy(mo);mc['results'][0]['witnesses'][0]=mw;mc['artifacts'][str(wp)]=sha(wp);put(mpfile,mc)
  run(['independent_code/check_larger_node_final.py','--fixture',str(v)],v/(typ+'_mutation.log'),expected)
  wp.write_bytes(wpristine);mpfile.write_bytes(mpristine)
 chunk=next((v/'mp'/'N2_local_72').glob('chunk_*.json.gz'));cp=chunk.read_bytes();cj=json.loads(gzip.decompress(cp));cj['rows'][0][0]='NaN';cj['rows_sha256']=hashlib.sha256(json.dumps(cj['rows'],separators=(',',':'),ensure_ascii=True).encode()).hexdigest();chunk.write_bytes(gzip.compress(json.dumps(cj).encode(),mtime=0));mc=copy.deepcopy(mo);mc['artifacts'][str(chunk)]=sha(chunk);put(mpfile,mc)
 run(['independent_code/check_larger_node_final.py','--fixture',str(v)],v/'malformed_decimal.log','finite decimal syntax');chunk.write_bytes(cp);mpfile.write_bytes(mpristine)
 ck('restored exact MP inputs',mpfile.read_bytes()==mpristine and wp.read_bytes()==wpristine and chunk.read_bytes()==cp)
 # Restore a final passing file after the deliberate bound-artifact failure.
 run(['independent_code/check_larger_node_final.py','--fixture',str(v)],v/'final_restored.log')
 for p,h in bindings.items():ck('stable '+p,sha(p)==h)
 out=dict(status='PASS_SYNTHETIC_INTEGRATED_LARGER_NODE_FINAL_CHECKER',synthetic_only=True,started_utc=start,finished_utc=now(),elapsed_seconds=time.monotonic()-tick,count=len(checks),checks=checks,bindings=bindings,fixture=str(v),artifacts={str(p):sha(p)for p in D.rglob('*')if p.is_file()},scope='Synthetic two-node complete driver and final checker integration; no candidate evidence.')
 put(V/'FINAL_CHECKER_MANUFACTURES.json',out);print(out['status'],len(checks),out['elapsed_seconds'])
except Exception:
 put(D/'FAILURE.json',dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()));print(traceback.format_exc());raise
