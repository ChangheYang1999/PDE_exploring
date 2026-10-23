"""Bind unreviewed dependencies and force a fresh, separately archived replay."""
from pathlib import Path
from datetime import datetime,timezone
import json,gzip,hashlib,traceback,sys,flint
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)
R=Path('research/degree23_real_parameter_audit');V=R/'verification';P=Path('research/degree23_grouped_moment_obstruction/verification')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
checks=[];bindings={};evidence={};started=utc()
def ck(name,b):
 checks.append(dict(name=name,passed=bool(b)))
 if not b:raise AssertionError(name)
def bind(p,expected=None):
 p=str(p);digest=sha(p);ck('binding '+p,expected is None or digest==expected);bindings[p]=digest
 raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw)if p.endswith('.gz')else raw)
try:
 for p in [Path(__file__),R/'FINAL_DEPENDENCY_AND_REPLAY_PROOF.md',R/'FINAL_EVIDENCE_PROOF.md']:
  bindings[str(p)]=sha(p)
 manifest=bind(P/'INPUTS.json');ck('62 frozen inputs',len(manifest['files'])==62)
 for row in manifest['files']:
  p=Path(row['frozen']);raw=p.read_bytes();ck('compressed '+str(p),len(raw)==row['compressed_bytes']and hashlib.sha256(raw).hexdigest()==row['compressed_sha256']);plain=gzip.decompress(raw);ck('uncompressed '+str(p),len(plain)==row['bytes']and hashlib.sha256(plain).hexdigest()==row['sha256']);bindings[str(p)]=sha(p)
 manufactures=bind(V/'INTERVAL_MANUFACTURES.json');ck('96 manufactures',manufactures['status']=='PASS'and manufactures['count']==len(manufactures['checks'])==96 and all(z['passed']for z in manufactures['checks']))
 for p,d in manufactures['bindings'].items():ck('manufacture dependency '+p,sha(p)==d);bindings[p]=d
 newton=bind('research/degree21_grouped_moment_obstruction/verification/UNIVERSAL_NEWTON.json');ck('320 Newton checks',newton['status']=='PASS'and newton['count']==len(newton['checks'])==320 and all(z['passed']for z in newton['checks']))
 ck('Newton library binding',sha('independent_code/exact_degree21.py')==newton['library_sha256']);bindings['independent_code/exact_degree21.py']=newton['library_sha256']
 oldindex=bind(V/'REAL_INDEX.json');ck('two original cases461',len(oldindex['cases'])==2 and oldindex['count']==461 and oldindex['status']=='PASS_PENDING_FINAL_REVIEW')
 for p,d in oldindex['bindings'].items():ck('original dependency '+p,sha(p)==d);bindings[p]=d
 evidence['runtime']=dict(python=sys.version,python_flint=flint.__version__,flint=flint.__FLINT_VERSION__,flint_threads=flint.ctx.threads)
 ck('exact runtime versions and one thread',flint.__version__=='0.9.0'and flint.__FLINT_VERSION__=='3.6.0'and flint.ctx.threads==1)
 replaydir=V/'forced_replay';replaydir.mkdir(exist_ok=True)
 ck('no prior replay artifacts',not any(replaydir.iterdir()))
 sourcepath=Path('independent_code/check_degree23_real_parameters.py');source=sourcepath.read_text();original=source
 substitutions=[("if out.exists():\n  old=", "if False:\n  old="),("out=V/('INDEPENDENT_REAL_'+cid+'.json.gz')", "out=V/'forced_replay'/('INDEPENDENT_REAL_'+cid+'.json.gz')"),("(V/'REAL_INDEX.json').write_text", "(V/'forced_replay/REAL_INDEX.json').write_text")]
 for i,(a,b)in enumerate(substitutions):ck('unique source substitution'+str(i),source.count(a)==1);source=source.replace(a,b)
 evidence['replay_source']=dict(original_sha256=sha(sourcepath),executed_sha256=hashlib.sha256(source.encode()).hexdigest(),substitutions=substitutions)
 (replaydir/'EXECUTION_TRANSFORM.json').write_text(json.dumps(evidence['replay_source'],indent=2)+'\n');bindings[str(replaydir/'EXECUTION_TRANSFORM.json')]=sha(replaydir/'EXECUTION_TRANSFORM.json')
 namespace={'__file__':str(sourcepath.resolve()),'__name__':'__main__'};oldargv=sys.argv[:];sys.argv=[str(sourcepath)]
 try:exec(compile(source,str(sourcepath)+' [fresh replay output redirect]','exec'),namespace)
 finally:sys.argv=oldargv
 freshindex=bind(replaydir/'REAL_INDEX.json');ck('fresh cases461',len(freshindex['cases'])==2 and freshindex['count']==461 and freshindex['status']=='PASS_PENDING_FINAL_REVIEW')
 for oldrow in oldindex['cases']:
  old=bind(oldrow['path'],oldrow['sha256']);newrow=next(z for z in freshindex['cases']if z['name']==oldrow['name']);fresh=bind(newrow['path'],newrow['sha256'])
  ck(oldrow['name']+' fresh PASS',fresh['status']=='PASS'and fresh['count']==len(fresh['checks'])and all(z['passed']for z in fresh['checks']))
  for key in ['name','status','count','checks','evidence','bindings']:ck(oldrow['name']+' exact replay '+key,fresh[key]==old[key])
  ck(oldrow['name']+' later fresh timestamps',fresh['started_utc']>old['updated_utc'])
 finite=bind(V/'FINAL_EVIDENCE_CHECKS.json');ck('236 finite consequence checks',finite['status']=='PASS_EXACT_EVIDENCE_SUMMARY_PENDING_MODEL_REVIEW'and finite['count']==len(finite['checks'])==236 and all(z['passed']for z in finite['checks']))
 for p,d in finite['bindings'].items():ck('consequence dependency '+p,sha(p)==d);bindings[p]=d
 for name in ['request.txt','response.json','answer.md','metadata.json']:
  p=V/'opus_final'/name;bindings[str(p)]=sha(p)
 meta=json.loads((V/'opus_final/metadata.json').read_text());ck('actual final Opus5.5 endturn',meta['returned_model']=='claude-opus-5-5'and meta['stop_reason']=='end_turn'and meta['answer_nonempty'])
 for p,d in bindings.items():ck('unchanged '+p,sha(p)==d)
 status='PASS_PENDING_DEPENDENCY_FOLLOWUP_REVIEW'
except BaseException:
 status='FAIL';(V/'FINAL_DEPENDENCY_TRACEBACK.txt').write_text(traceback.format_exc());raise
finally:
 out=dict(status=status,started_utc=started,finished_utc=utc(),count=len(checks),checks=checks,bindings=bindings,evidence=evidence)
 (V/'FINAL_DEPENDENCY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(status,len(checks),out['finished_utc'],flush=True)
