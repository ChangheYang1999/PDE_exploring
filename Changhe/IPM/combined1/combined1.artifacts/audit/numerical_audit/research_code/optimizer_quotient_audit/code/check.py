from pathlib import Path
from datetime import datetime,timezone
import hashlib,importlib.util,json,os,signal,sys,time
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/optimizer_quotient_audit'
sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.monotonic();begin=datetime.now(timezone.utc).isoformat();stopped=[]
try:
 for pid in [286853,336903]:
  path=Path(f'/proc/{pid}/stat')
  if path.exists() and path.read_text().split()[2] not in ['T','Z','X']:os.kill(pid,signal.SIGSTOP);stopped.append(pid)
 engine=ROOT/'research/quotient_coordinates/code/reduce.py';spec=importlib.util.spec_from_file_location('n4_exact_quotient_audit',engine);Q=importlib.util.module_from_spec(spec);spec.loader.exec_module(Q)
 rows=[];inputs=[Path(__file__),BASE/'PROOF.md',engine,BASE/'source/N1_quotient_basis.py',ROOT/'research/quotient_coordinates/PROOF.md',ROOT/'research/quotient_coordinates/verification/007_legendre/result.json',ROOT/'research/quotient_coordinates/reviews/T4_230/ACCEPTANCE.json']
 for short,name in [('007','C1-N1-007-d2w-j7-e2bal'),('013','C1-N1-013-pairU-from007')]:
  tick=time.monotonic();source=BASE/f'source/N1_{short}_quot_exact.json';raw=json.loads(source.read_text())
  expected={'007':'0973c3659f5ad0b5a3b2087a9e91ea61408b4356cee11006773879c13f9bfe20','013':'c0d3536ea961908a8a4d251054192bad0b5b2534435e3c8224fe0424bda5f7fe'}[short];assert sha(source)==expected
  original=ROOT/f'research/candidate_audits/data/{name}'/Path(raw['meta']['quotient_of']).name
  prior=json.loads(original.read_text());cp=original.parent/'canonical.json';can=json.loads(cp.read_text());auditpath=ROOT/f'research/candidate_audits/verification/{name}.json';audit=json.loads(auditpath.read_text())
  assert sha(original)==audit['generator_sha256']==raw['meta']['quotient_of_sha256']
  assert sha(cp)==audit['canonical_sha256'] and can['source_sha256']==sha(original)
  assert Q.Q(raw['cl_exact'])==Q.Q(prior['cl_exact'])==Q.Q(can['cl'])==Q.Q(4076476460239181,2251799813685248)
  assert len(prior['generators'])==2982 and raw['n_free']==len(raw['generators'])==1922 and raw['n_fixed']==0
  kept=raw['meta']['kept_indices'];assert len(kept)==len(set(kept))==1922 and all(type(i) is int and 0<=i<2982 for i in kept)
  assert all(all(a[k]==prior['generators'][i][k] for k in ['j','m','spec']) for a,i in zip(raw['generators'],kept,strict=True))
  new,pivots,relations,blocks=Q.reduce(raw);assert len(pivots)==1922 and not relations and len(new)==1922
  canonical=Q.canonical(raw['generators']);oldcanon=Q.canonical(prior['generators']);expectedcan={tuple(k):Q.Q(v) for k,v in zip(can['order'],can['coefficients'],strict=True)}
  assert canonical==oldcanon==expectedcan and len(canonical)==1922
  counts={s:sum(g['spec'][0]==s for g in raw['generators']) for s in ['mono','leg']};assert counts=={'mono':262,'leg':1660}
  assert raw['meta']['removed_zero_potential_directions']==2982-1922==1060
  inputs.extend([source,original,cp,auditpath])
  row={'candidate':name,'new_source_sha256':sha(source),'original_raw_sha256':sha(original),'canonical_sha256':sha(cp),'original_columns':2982,'selected_columns':1922,'nonpivot_relations':0,'original_kernel_dimension':1060,'selected_counts':counts,'selected_original_shapes_match':True,'all_canonical_coefficients_equal':True,'canonical_coefficient_count':len(canonical),'c_exact':str(Q.Q(raw['cl_exact'])),'blocks':[{'j':r['j'],'m':r['m'],'rank':r['rank']} for r in blocks],'elapsed_seconds':time.monotonic()-tick}
  rows.append(row);print(name,'canonical_equal',len(canonical),'rank',len(pivots),'blocks',len(blocks),'seconds',row['elapsed_seconds'],flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p.relative_to(ROOT)):sha(p) for p in inputs},'rows':rows,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED exact quotient re-expression and rank only. No numerical convergence or conditioning claim.'}
 with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
finally:
 for pid in reversed(stopped):
  try:os.kill(pid,signal.SIGCONT)
  except ProcessLookupError:pass
 pause={'began_utc':begin,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'stopped_and_resumed_pids':stopped}
 with (BASE/'verification/pause.json').open('x') as f:json.dump(pause,f,indent=2);f.write('\n')
