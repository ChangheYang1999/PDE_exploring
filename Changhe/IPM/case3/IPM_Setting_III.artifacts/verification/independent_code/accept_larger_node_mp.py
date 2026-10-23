"""Collect the already reviewed MP design once actual B has completed. No computation launch."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,os,sys
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
if sys.flags.optimize:raise SystemExit('optimization not admitted')
import numpy as np
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';C=V/'candidate';bindings={};checks=[]
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise ValueError(n)
def bind(p,h=None):
 p=Path(p);z=hashlib.sha256(p.read_bytes()).hexdigest();ck('binding '+str(p),(h is None or h==z)and(str(p)not in bindings or bindings[str(p)]==z));bindings[str(p)]=z;return p
def read(p,h=None):return json.loads(bind(p,h).read_text())
def gate(p,status):
 d=read(p);ck('semantic '+str(p),d['status']==status and d['count']==len(d['checks'])and all(z['passed']for z in d['checks']))
 for p,h in d.get('bindings',{}).items():bind(p,h)
 return d
def load(p):
 with np.load(bind(p),allow_pickle=False)as z:return {k:z[k]for k in z.files}
try:
 ck('acceptance absent',not(V/'MP_DESIGN_ACCEPTANCE.json').exists())
 job=read(V/'JOB.json');pid=Path('/proc')/str(job['pid'])
 if pid.exists():ck('B process ceased',(pid/'stat').read_text().rsplit(') ',1)[1].split()[0]=='Z'or b'run_larger_node_audit.py'not in(pid/'cmdline').read_bytes())
 c=gate(C/'COMPLETE.json','COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW')
 for p,h in c['artifacts'].items():bind(p,h)
 inp=read(V/'INPUTS.json');ck('exact state order',[(s['N'],s['M'])for s in inp['states']]==[(224,56),(192,48)]);ck('completed source identity',[s['source']for s in c['results']]==inp['states'])
 for state in c['results']:
  tag='N'+str(state['N']);ids=state['selected']['indices'];sel=read(C/(tag+'_SELECTION.json'));A=load(C/(tag+'_C.npz'));B=load(C/(tag+'_B.npz'));manifest=json.loads(str(A['manifest']))
  ck('actual C selection '+tag,manifest['status']=='COMPLETE'and manifest['completed']==manifest['total']==len(ids)and np.array_equal(A['indices'],ids)and sel==state['selected']and ids==state['local_mp_indices'])
  valid=np.flatnonzero(np.isfinite(B['residual'][:,3]));ck('finite B Rf '+tag,len(valid)>0)
  first=int(valid[np.argmax(B['residual'][valid,3])]);ck('actual first global witness '+tag,state['integrand_mp_indices']==[first]and first in ids)
  ck('per-state completion identity '+tag,read(C/(tag+'_COMPLETE.json'))==state)
 for name,status in [('MP_STAGE_MANUFACTURES.json','PASS_MP_GEOMETRY_MOMENTS_AND_REAL_RESTART'),('MP_DRIVER_MANUFACTURES.json','PASS_SYNTHETIC_MP_DRIVER_ADMISSION_AND_TAMPER'),('MP_ADMISSION_SUPPLEMENT.json','PASS_MP_ADMISSION_SUPPLEMENT')]:gate(V/name,status)
 a=read(V/'DESIGN_ACCEPTANCE.json');ck('B design status',a['status']=='ACCEPTED_FOR_FINITE_COMPUTATION')
 for p,h in a['bindings'].items():bind(p,h)
 for label in ['mp_design','mp_followup','mp_clarification']:
  p=V/('opus_'+label);m=read(p/'metadata.json');ck('actual model completed '+label,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']=='claude-opus-5-5'and m['stop_reason']=='end_turn'and m['answer_nonempty'])
  for name in ['request.txt','response.json','answer.md']:bind(p/name)
 for p in R.glob('MP*.md'):bind(p)
 for p in ['independent_code/run_larger_node_mp.py','independent_code/launch_larger_node_mp.py','independent_code/larger_node_stage.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py',__file__]:bind(p)
 for p,h in list(bindings.items()):bind(p,h)
 out=dict(status='ACCEPTED_FOR_FINITE_MP_COMPUTATION',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,scope='Design and real B/C admission only. Candidate MP remains uncomputed; exact inverse error OPEN; primary UNRESOLVED.')
 (V/'MP_DESIGN_ACCEPTANCE.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),len(bindings))
except Exception:
 import traceback
 (V/('MP_ACCEPTANCE_FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')).write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
