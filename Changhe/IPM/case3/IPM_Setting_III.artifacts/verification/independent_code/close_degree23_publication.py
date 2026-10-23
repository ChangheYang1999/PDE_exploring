"""Final immutable publication bindings for finite results292/293."""
from pathlib import Path
from datetime import datetime,timezone
import json,gzip,hashlib,traceback,sys,ast,flint
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)
mode=sys.argv[1];assert mode in ['292','293']
R=Path('research')/('degree23_grouped_moment_obstruction'if mode=='292'else'degree23_real_parameter_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
checks=[];bindings={};started=utc();evidence={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=str(p);s=sha(p);ck('bind '+p,h is None or s==h);ck('consistent binding '+p,p not in bindings or bindings[p]==s);bindings[p]=s
 raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw)if p.endswith('.gz')else raw)
def gate(p,n,status):
 d=bind(p);ck('complete gate '+str(p),d['status']==status and d['count']==len(d['checks'])==n and all(z['passed']for z in d['checks']))
 for p,h in d.get('bindings',{}).items():ck('gate dependency '+p,sha(p)==h);bindings[p]=h
 return d
def reviews():
 ids=[]
 for label in ['final','final_followup']:
  q=V/('opus_'+label)
  for name in ['request.txt','response.json','answer.md','metadata.json']:bindings[str(q/name)]=sha(q/name)
  meta=json.loads((q/'metadata.json').read_text());response=json.loads((q/'response.json').read_text());answer='\n\n'.join(z.get('text','')for z in response['content']if z.get('type')=='text')+'\n'
  ck(label+' actual model',meta['requested_model']=='us.anthropic.claude-opus-5-5'and meta['returned_model']==response['model']=='claude-opus-5-5')
  ck(label+' completed response',meta['stop_reason']==response['stop_reason']=='end_turn'and meta['answer_nonempty']and answer.strip()!='')
  ck(label+' response text exact',answer==(q/'answer.md').read_text())
  ck(label+' request binding',meta['request_sha256']==sha(q/'request.txt'))
  ck(label+' chronology',meta['started_utc']<meta['finished_utc']<utc());ids.append(dict(request_id=meta['request_id'],model=meta['returned_model'],finished_utc=meta['finished_utc']))
 return ids
try:
 for p in [Path(__file__),R/'FINAL_CLOSURE_PROOF.md']:bindings[str(p)]=sha(p)
 ck('assertions enabled',sys.flags.optimize==0)
 ck('runtime contracts identified',flint.__version__=='0.9.0'and flint.__FLINT_VERSION__=='3.6.0'and flint.ctx.threads==1)
 if mode=='292':
  d=gate(V/'CLOSURE_NATIVE_CHECKS.json',86928,'PASS_PENDING_FINAL_MODEL_REVIEW')
  supplement=gate(V/'FINAL_SUPPLEMENT_CHECKS.json',2893,'PASS_PENDING_FOCUSED_FINAL_REVIEW')
  gate(V/'native/TARGET_LINKAGE_PREFLIGHT.json',241,'PASS_TARGET_LINKAGE_PREFLIGHT_ONLY')
  gate(V/'native/OUTER_SMOKE_CLOSURE.json',317,'PASS_ACTUAL_NATIVE_RECORD_AND_SMOKE_INDEX')
  source=Path('independent_code/check_degree23_closure_native.py').read_text();tree=ast.parse(source)
  args=sorted(ast.unparse(n.args[1])for n in ast.walk(tree)if isinstance(n,ast.Call)and isinstance(n.func,ast.Name)and n.func.id=='restore')
  ck('all three restore ledgers covered',args==sorted(["d['resultant_removed']","d['gcd_removed']","br['removed']"]))
  cf=V/'cases/1_6_2_2_1.json.gz';case=bind(cf);o=bind(V/'outer_native/1_6_2_2_1__0.json.gz')
  ck('supplemental constant job name linked',o['name']==case['jobs'][0]['name']=='1_6_2_2_1 final')
  ck('supplemental outer case bytes linked',o['bindings'][str(cf)]==sha(cf))
  expected=dict(cases=49,reconstruction_assertions=6433,outer_jobs=82,positive_real_patterns=47,gcd_certificates=33,outer_assertions=43573,exact_samples=41031,zero_branches=20,integer_exceptions=2)
  ck('native statistics exact',d['statistics']==expected)
  ck('82sample bounds sum41031',len(d['outer_identities'])==82 and sum(z['bound']+1 for z in d['outer_identities'])==41031 and all(z['samples']==z['bound']+1 for z in d['outer_identities']))
  ck('supplement factor count136',supplement['evidence']['factor_records']==136)
  evidence=dict(statistics=expected,restore_ledger_expressions=args,primary_endpoint='UNRESOLVED',scope='Exact finite degree23 node exclusion for integer n>=1; finite auxiliary d>=25,P>=27/2 with prior reductions only.')
  status='CONFIRMED_FINITE_INTEGER_NODE_EXCLUSION'
 else:
  consequence=gate(V/'FINAL_EVIDENCE_CHECKS.json',236,'PASS_EXACT_EVIDENCE_SUMMARY_PENDING_MODEL_REVIEW')
  deps=gate(V/'FINAL_DEPENDENCY_CHECKS.json',287,'PASS_PENDING_DEPENDENCY_FOLLOWUP_REVIEW')
  original=bind(V/'REAL_INDEX.json');fresh=bind(V/'forced_replay/REAL_INDEX.json')
  ck('both original and fresh461',original['count']==fresh['count']==461 and len(original['cases'])==len(fresh['cases'])==2)
  manifest='research/degree23_grouped_moment_obstruction/verification/INPUTS.json';mh=sha(manifest)
  ck('original index manifest anchor',original['bindings'][manifest]==mh)
  for row in original['cases']:
   a=bind(row['path'],row['sha256']);brow=next(z for z in fresh['cases']if z['name']==row['name']);b=bind(brow['path'],brow['sha256'])
   ck(row['name']+' original arithmetic PASS',a['status']=='PASS'and a['count']==len(a['checks'])and all(z['passed']for z in a['checks']))
   ck(row['name']+' original manifest anchor',a['bindings'][manifest]==mh)
   for key in ['name','status','count','checks','evidence','bindings']:ck(row['name']+' replay '+key,a[key]==b[key])
   for p,h in a['bindings'].items():ck('candidate dependency '+p,sha(p)==h);bindings[p]=h
  for p in [R/'FINAL_DEPENDENCY_AND_REPLAY_PROOF.md',V/'initial_replay_path_failure/FINAL_DEPENDENCY_CHECKS.json',V/'initial_replay_path_failure/FINAL_DEPENDENCY_TRACEBACK.txt',V/'initial_replay_path_failure/checker.py.txt']:bindings[str(p)]=sha(p)
  evidence=dict(original_assertions=461,replayed_assertions=461,consequence_assertions=236,dependency_assertions=287,manifest_anchor=mh,primary_endpoint='UNRESOLVED',scope='Two exact finite-node configurations A0=1 at real noninteger n in(1,3/2), with16 simple root disks. No finite polynomial profile or IPM existence claim.')
  status='CONFIRMED_FINITE_REAL_NONINTEGER_CONFIGURATIONS'
 evidence['actual_final_reviews']=reviews();evidence['runtime']=dict(python=sys.version,python_flint=flint.__version__,flint=flint.__FLINT_VERSION__,threads=flint.ctx.threads,optimize=sys.flags.optimize)
 for p,h in bindings.items():ck('final unchanged '+p,sha(p)==h)
except BaseException:
 status='FAIL';(V/'FINAL_PUBLICATION_TRACEBACK.txt').write_text(traceback.format_exc());raise
finally:
 out=dict(status=status,started_utc=started,finished_utc=utc(),count=len(checks),checks=checks,bindings=bindings,evidence=evidence)
 (V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(mode,status,len(checks),len(bindings),sha(V/'FINAL_BINDINGS.json'),out['finished_utc'],flush=True)
