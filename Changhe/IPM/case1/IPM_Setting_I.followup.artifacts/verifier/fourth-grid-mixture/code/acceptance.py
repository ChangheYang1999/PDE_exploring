"""Check runtime evidence and frozen registration after the finite mixture finishes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
BASE=Path(__file__).resolve().parents[3];ROOT=BASE/'verifier/fourth-grid-mixture';V=ROOT/'verification'
if sys.flags.optimize or not __debug__:raise RuntimeError('Acceptance requires assertions enabled')
def need(ok,msg):
 if not ok:raise RuntimeError(msg)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def stamp(text):
 d=datetime.fromisoformat(text);need(d.tzinfo is not None,'naive timestamp');return d.timestamp()
expected_plan='4005e6a6c0cc6682b49ce1619ec8c4a9d00f986efe030eeed656f4e575af099f'
expected_reg='521edaf21aab392f109cf334098e029ba568464f26479ca2be8267ed989b78f4'
expected_wrapper='d7a5bd23b32a67502cebcd0bcb23f678926b089d1590f5f2a851e00f3df6e8c0'
plan=V/'plan.json';registration=V/'registration.json';need(sha(plan)==expected_plan and sha(registration)==expected_reg,'registration bytes')
ps=json.loads(plan.read_text());result=V/'n84m35S_summary.json';out=json.loads(result.read_text())
need(out.get('complete') and out.get('verdict')=='PASS','mixture incomplete')
need(out['pins'][str(plan)]==expected_plan and out['pins'][str(registration)]==expected_reg,'mixture registration pins')
need(len(out['rows'])==15 and {(r['dimension'],r['alpha_first_sample']) for r in out['rows']}=={(k,a)for k in [4,10,14]for a in [0,.25,.5,.75,1]},'fifteen prescribed cases')
wrapper=BASE/'verifier/run-control/code/checked_python.py';need(sha(wrapper)==expected_wrapper,'wrapper changed')
resolution=json.loads((V/'import_resolution.json').read_text())
output_map={
 'fourth-grid-actions/code/summarize.py':[('verifier/fourth-grid-actions/verification/summary.json','date'),('verifier/fourth-grid-actions/verification/summary_matrices.npz',None)],
 'fourth-grid-actions/code/audit_summary.py':[('verifier/fourth-grid-actions/verification/summary_audit.json','utc')],
 'fourth-grid-gauss/code/run.py':[('verifier/fourth-grid-gauss/verification/n84m35S_actions.json','date_end')],
 'fourth-grid-gauss/code/summarize.py':[('verifier/fourth-grid-gauss/verification/n84m35S_summary.json','utc'),('verifier/fourth-grid-gauss/verification/n84m35S_matrices.npz',None)],
 'fourth-grid-gauss/code/audit_summary.py':[('verifier/fourth-grid-gauss/verification/n84m35S_audit.json','utc')],
 'fourth-grid-mixture/code/run.py':[('verifier/fourth-grid-mixture/verification/n84m35S_summary.json','utc'),('verifier/fourth-grid-mixture/verification/n84m35S_matrices.npz',None)]
}
targets=['fourth-grid-actions/code/summarize.py','fourth-grid-actions/code/audit_summary.py','fourth-grid-gauss/code/run.py','fourth-grid-gauss/code/summarize.py','fourth-grid-gauss/code/audit_summary.py','fourth-grid-mixture/code/run.py']
records=[];intervals={};pins={str(p.relative_to(BASE)):sha(p)for p in [plan,registration,result,wrapper,Path(__file__),ROOT/'ACCEPTANCE.md']}
for target in targets:
 rel='verifier/'+target;p=BASE/rel;need(sha(p)==ps['pins'][rel],'target changed '+rel)
 expected_modules=resolution['resolutions'].get(str(p.parent.relative_to(BASE)),resolution['resolutions']['verifier/fourth-grid-gauss/code'])
 expected_argv=[rel] if target.startswith('fourth-grid-actions/') else [rel,'84']
 found=[]
 for rp in (BASE/'verifier/run-control/verification').glob('*_'+p.parent.parent.name+'_'+p.stem+'.json'):
  r=json.loads(rp.read_text())
  if r.get('target')!=str(p) or not r.get('complete'):continue
  need(r['optimize']==0 and r['PYTHONOPTIMIZE'] is None and r['target_unchanged'] is True,'runtime flags or mutation '+str(rp))
  need(r['target_sha256']==ps['pins'][rel] and r['wrapper_sha256']==expected_wrapper,'runtime source pin '+str(rp))
  need(r['argv']==expected_argv,'runtime argv '+str(rp))
  start=stamp(r['start_utc']);end=stamp(r['end_utc']);need(start<=end,'runtime time order')
  intervals[target]=(start,end)
  for output_rel,time_key in output_map[target]:
   op=BASE/output_rel;need(start<=op.stat().st_mtime<=end,'output modification outside wrapper interval '+output_rel)
   if time_key:
    output_time=stamp(json.loads(op.read_text())[time_key]);need(start<=output_time<=end,'output timestamp outside wrapper interval '+output_rel)
   if target!='fourth-grid-mixture/code/run.py':need(out['pins'][str(op)]==sha(op),'consumed output differs '+output_rel)
   pins[output_rel]=sha(op)
  for name,binding in r['modules'].items():
   need(name in expected_modules,'unknown tracked binding '+name)
   expected=expected_modules[name];ep=BASE/expected['file']
   need(binding['file']==str(ep) and binding['sha256']==expected['sha256']==sha(ep),'module binding '+name)
  if target=='fourth-grid-gauss/code/run.py':
   need(set(r['modules'])==set(expected_modules),'missing Gauss direct binding')
   need(r.get('gradient_fd_source')==str(BASE/'verifier/inverse/code/density.py'),'Gauss stencil binding')
  found.append(rp)
 need(len(found)==1,'expected one successful runtime record '+rel)
 rp=found[0];pins[str(rp.relative_to(BASE))]=sha(rp);records.append({'target':rel,'record':str(rp.relative_to(BASE)),'sha256':sha(rp)})
# Every consumed pin must belong to an explicitly accepted category.
accepted_outputs={str(BASE/rel)for target,pairs in output_map.items()if target!='fourth-grid-mixture/code/run.py'for rel,_ in pairs}
static_inputs={str(BASE/rel)for rel in ps['pins']}|{str(plan),str(registration)}
unwrapped_primary={str(BASE/'verifier/fourth-grid-actions/verification/actions.json')}
for key,h in out['pins'].items():
 op=Path(key);need(op.is_absolute() and op.resolve()==op and op.is_relative_to(BASE),'noncanonical consumed pin')
 need(key in accepted_outputs|static_inputs|unwrapped_primary,'unclassified consumed input '+key)
 need(sha(op)==h,'consumed input changed '+key)
 pins[str(op.relative_to(BASE))]=h
for earlier,later in [('fourth-grid-actions/code/summarize.py','fourth-grid-actions/code/audit_summary.py'),('fourth-grid-gauss/code/run.py','fourth-grid-gauss/code/summarize.py'),('fourth-grid-gauss/code/summarize.py','fourth-grid-gauss/code/audit_summary.py')]:
 need(intervals[earlier][1]<=intervals[later][0],'producer-consumer execution order')
for target,interval in intervals.items():
 if target!='fourth-grid-mixture/code/run.py':need(interval[1]<=intervals['fourth-grid-mixture/code/run.py'][0],'upstream run after mixture start')
for rel,h in ps['pins'].items():need(sha(BASE/rel)==h,'plan source changed '+rel)
for rel,h in pins.items():need(sha(BASE/rel)==h,'acceptance input changed '+rel)
answer={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','records':records,'pins':pins,'plan_sha256':expected_plan,'registration_sha256':expected_reg,'scope':'Mechanical checks in ACCEPTANCE.md. Prior the research record/request copies and live-primary observation limitations remain a manual verifier check. Finite numerical diagnostics only.'}
(V/'acceptance.json').write_text(json.dumps(answer,indent=2)+'\n');print('ACCEPTANCE_PASS',len(records),'runtime records')
