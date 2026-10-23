from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib,uuid,os,copy,math,types
R=Path('research/hydrostatic_c2_resolved_224_audit');V=R/'verification';T=V/'manufactured_recovery';T.mkdir(exist_ok=True);checks=[];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();tag='hsG_c2.0_N224_log'
def ck(name,test,evidence=None):
 checks.append(dict(name=name,passed=bool(test),evidence=evidence))
 if not test:raise AssertionError((name,evidence))
def compile_nodes(nodes):return compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),'<actual prepared AST>','exec')
fpath=Path('independent_code/freeze_hydrostatic_224_input.py');pcode=Path('independent_code/audit_hydrostatic_c2_resolved_224.py');scode=Path('independent_code/summarize_hydrostatic_c2_resolved_224.py');ft=ast.parse(fpath.read_text());pt=ast.parse(pcode.read_text());st=ast.parse(scode.read_text());guard=next(n for n in ft.body if isinstance(n,ast.If)and 'INPUTS.json'in ast.unparse(n.test));atomic=next(n for n in ft.body if isinstance(n,ast.FunctionDef)and n.name=='atomic_json');fields=['driver_sha256','proof_sha256','review_proof_sha256','followup_proof_sha256','final_preparation_proof_sha256'];active={k:hashlib.sha256(k.encode()).hexdigest()for k in fields}
def write(p,d):Path(p).write_text(json.dumps(d,indent=2)+'\n')
def make(label):
 v=T/label;v.mkdir(exist_ok=True);source=v/'synthetic_source.bin';source.write_bytes(b'SYNTHETIC PROTOCOL TEST ONLY. Not a checkpoint.\n');(v/'producer_log_at_freeze.txt').write_text('synthetic log\n');(v/'producer_launcher_at_freeze.txt').write_text('synthetic launcher\n');inp=dict(states=[dict(tag=tag,frozen=str(source),sha256=sha(source))]);write(v/'INPUTS.json',inp);gate=dict(status='PASS',input_sha256=sha(v/'INPUTS.json'),source_sha256=sha(source),frozen=str(source),count=1,checks=[dict(passed=True)],log_sha256=sha(v/'producer_log_at_freeze.txt'),launcher_sha256=sha(v/'producer_launcher_at_freeze.txt'),modules={str(Path('independent_code',name).resolve()):sha(Path('independent_code',name))for name in ['q_local_checkpoint.py','q_checkpoint_reader.py']},**active);write(v/'SOURCE_GATE.json',gate);return v,inp,gate
labels=['valid','missing_input','missing_gate','invalid_json','source_changed','frozen_path','tag','input_hash','gate_count','failed_check','driver','proof','module_set','log_changed','publication_interrupted']
for label in labels:
 v,inp,gate=make(label)
 if label=='missing_input':(v/'INPUTS.json').unlink()
 elif label=='missing_gate':(v/'SOURCE_GATE.json').unlink()
 elif label=='invalid_json':(v/'INPUTS.json').write_text('{broken')
 elif label=='source_changed':Path(inp['states'][0]['frozen']).write_bytes(b'changed synthetic bytes')
 elif label=='log_changed':(v/'producer_log_at_freeze.txt').write_text('changed log')
 else:
  if label=='frozen_path':gate['frozen']='not-the-bound-source'
  elif label=='tag':inp['states'][0]['tag']='wrong-tag';write(v/'INPUTS.json',inp);gate['input_sha256']=sha(v/'INPUTS.json')
  elif label=='input_hash':gate['input_sha256']='0'*64
  elif label=='gate_count':gate['count']=2
  elif label=='failed_check':gate['checks'][0]['passed']=False
  elif label=='driver':gate['driver_sha256']='0'*64
  elif label=='proof':gate['proof_sha256']='0'*64
  elif label=='module_set':gate['modules']={}
  elif label=='publication_interrupted':gate['input_sha256']=hashlib.sha256(b'new unpublished INPUTS bytes').hexdigest()
  write(v/'SOURCE_GATE.json',gate)
 original={p.name:p.read_bytes()for p in [v/'INPUTS.json',v/'SOURCE_GATE.json']if p.exists()};env=dict(V=v,Path=Path,json=json,sha=sha,tag=tag,out=dict(active),uuid=uuid,print=lambda *args,**kwargs:None);exited=False
 try:exec(compile_nodes([guard]),env)
 except SystemExit as exc:exited=True;ck(label+' success exit',exc.code==0)
 ck(label+' guard behavior',exited==(label=='valid'))
 if not exited:
  archive=Path(env['out']['recovery_archive']);ck(label+' originals preserved',all((archive/name).read_bytes()==b for name,b in original.items()))
 else:ck('valid no recovery archive',not(v/'source_recovery').exists())
# Atomic replacement and injected failure before publication.
v=T/'atomic';v.mkdir(exist_ok=True);target=v/'document.json';target.write_text('{"old":true}\n');env=dict(V=v,Path=Path,json=json,uuid=uuid,os=os);exec(compile_nodes([atomic]),env);env['atomic_json'](target,dict(new=1));ck('atomic complete replacement',json.loads(target.read_text())==dict(new=1));before=target.read_bytes()
def fail_replace(*args):raise OSError('synthetic injected replace failure')
env['os']=types.SimpleNamespace(replace=fail_replace)
try:env['atomic_json'](target,dict(new=2));raise AssertionError('injection not called')
except OSError:ck('atomic interrupted old document intact',target.read_bytes()==before)
# Actual pipeline hypothesis handler, with bound synthetic files.
main=next(n for n in pt.body if isinstance(n,ast.FunctionDef)and n.name=='main');bodytry=next(n for n in main.body if isinstance(n,ast.Try));handler=next(h for h in bodytry.handlers if ast.unparse(h.type)=='Inapplicable')
for changed in [False,True]:
 v,inp,source=make('pipeline_changed'if changed else'pipeline_valid');code=v/'synthetic_code.txt';code.write_text('synthetic code');pipe=dict(status='RUNNING',input_sha256=sha(v/'INPUTS.json'),source_gate_sha256=sha(v/'SOURCE_GATE.json'),code_and_proof_sha256={str(code):sha(code)},checks=[],states=[dict(tag=tag,status='RUNNING')]);env=dict(V=v,sha=sha,pipe=pipe,inputs=inp,source=source,exc=Exception('synthetic a=0'),utc=utc,traceback=__import__('traceback'),print=lambda *args,**kwargs:None)
 def check(name,ok,evidence=None):
  pipe['checks'].append(dict(name=name,passed=bool(ok),evidence=evidence))
  if not ok:raise AssertionError(name)
 env.update(check=check,savepipe=lambda:write(v/'PIPELINE.json',pipe))
 if changed:Path(inp['states'][0]['frozen']).write_bytes(b'changed synthetic source')
 raised=False
 try:exec(compile_nodes(handler.body),env)
 except AssertionError:raised=True
 ck('pipeline label '+str(changed),pipe['status']==('FAILED'if changed else'INAPPLICABLE')and raised==changed)
# Summary shared provenance prefix must run before its applicability exception.
main=next(n for n in st.body if isinstance(n,ast.FunctionDef)and n.name=='main');prefix=[]
for n in main.body:
 if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='points'for t in n.targets):break
 prefix.append(n)
class Inapplicable(Exception):pass
for changed in [False,True]:
 v,inp,source=make('summary_changed'if changed else'summary_valid');code=v/'synthetic_code.txt';code.write_text('synthetic code');pipe=dict(status='INAPPLICABLE',reason='synthetic h1<=0',input_sha256=sha(v/'INPUTS.json'),source_gate_sha256=sha(v/'SOURCE_GATE.json'),code_and_proof_sha256={str(code):sha(code)},checks=[dict(passed=True)],states=[dict(tag=tag,status='INAPPLICABLE')]);write(v/'PIPELINE.json',pipe);local=[]
 if changed:inp['states'][0]['sha256']='0'*64;write(v/'INPUTS.json',inp)
 env=dict(V=v,json=json,sha=sha,checks=local,check=lambda n,b,e=None:local.append(dict(name=n,passed=bool(b))),Inapplicable=Inapplicable);kind=None
 try:exec(compile_nodes(prefix),env)
 except Inapplicable:kind='INAPPLICABLE'
 except AssertionError:kind='PROVENANCE_FAILED'
 ck('summary prefix '+str(changed),kind==('PROVENANCE_FAILED'if changed else'INAPPLICABLE'));ck('summary no numerical records needed '+str(changed),not(v/'POINTS.json').exists())
# Point serialization preserves exact axes; actual function, manufactured arguments.
tree=ast.parse(Path('independent_code/audit_hydrostatic_states.py').read_text());record=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='point_record');env=dict(math=math);exec(compile_nodes([record]),env)
class FakeInverse:
 def at(self,x,y):return dict(V=[0. if x==0 else x,0. if y==0 else y],Phi=0.,tail_V=[0.,0.])
for x0,y0 in [(0.,3.),(3.,0.)]:
 point=env['point_record'](lambda x,y:(y,0.,1.,0.),FakeInverse(),2.,x0,y0);roundtrip=json.loads(json.dumps(point));ck('axis serialization '+str((x0,y0)),roundtrip==point and point['gx']==0. and(point['V1']==0. if x0==0 else point['R_Nf']is None and point['R_Nv']is None))
precision=next(n for n in st.body if isinstance(n,ast.FunctionDef)and n.name=='precision_check')
class PrecisionFailure(Exception):pass
env=dict(check=lambda *args:None,PrecisionFailure=PrecisionFailure);exec(compile_nodes([precision]),env);raised=False
try:env['precision_check']('synthetic low precision',False,{})
except PrecisionFailure:raised=True
ck('dedicated precision exception',raised)
out=dict(status='PASS',utc=utc(),count=len(checks),checks=checks,proof_sha256=sha(R/'RECOVERY_MANUFACTURE_PROOF.md'),driver_sha256=sha(__file__),source_sha256={str(p):sha(p)for p in [fpath,pcode,scode,Path('independent_code/audit_hydrostatic_states.py')]},scope='Synthetic protocol tests only. No N224 coefficients, no numerical candidate result.')
(V/'RECOVERY_MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),out['utc'])
