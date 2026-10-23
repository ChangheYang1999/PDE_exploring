from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,resource,os
R=Path('verification');assert Path.cwd().resolve()==R
V=Path('research/e2_integer_divisor_audit/verification');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,8*1024**3))
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
inputs=json.loads((V/'INPUTS.json').read_text());gate=json.loads((V/'ALGEBRA_CHECKS.json').read_text());assert gate['status']=='PASS';assert sha(V/'polynomial_terms.tsv')==gate['terms_sha256'];assert inputs['n_min']==1 and inputs['n_max']==1000
expected=json.loads((V/'EXPECTED_LOOPS.json').read_text());assert expected['nmax']==1000
hashes={str(p):sha(p)for p in [Path(__file__),Path('independent_code/e2_divisor_enumerator.cpp'),V/'enumerator',V/'polynomial_terms.tsv',V/'original_polynomial.json',V/'INPUTS.json',V/'EXPECTED_LOOPS.json',V/'ALGEBRA_CHECKS.json',V/'BUILD.json',Path('independent_code/check_e2_enumeration.py'),V.parent/'PROOF.md']}
meta=dict(status='RUNNING',started_utc=now(),cwd=str(Path.cwd()),pid=os.getpid(),expected_gh=expected['gh'],hashes=hashes)
(V/'RUN.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta['started_utc'],'START expected_gh',meta['expected_gh'],flush=True)
r=subprocess.run([str(V/'enumerator'),str(inputs['n_max']),str(V/'polynomial_terms.tsv'),str(V/'full1000')],timeout=2400)
meta.update(finished_utc=now(),returncode=r.returncode,unchanged_inputs=all(sha(p)==h for p,h in hashes.items()))
if r.returncode==0:
 j=json.loads((V/'full1000.result.json').read_text());meta.update(result=j,result_sha256=sha(V/'full1000.result.json'));rows=[json.loads(x)for x in(V/'full1000.counts.jsonl').read_text().splitlines()]
 good=j['status']=='DONE'and j['nmax']==1000 and j['gh']==expected['gh']and len(rows)==1000 and all(x['n']==i+1 and x['status']=='PER_N_DONE'and x['gh']==expected['per_n'][i]['gh']for i,x in enumerate(rows))and meta['unchanged_inputs']
 meta['status']='DONE'if good else'FAIL'
else:meta['status']='FAIL'
(V/'RUN.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta['finished_utc'],meta['status'],meta.get('result'),flush=True)
if meta['status']=='DONE':
 r2=subprocess.run(['python3','independent_code/check_e2_enumeration.py'],timeout=600);meta['checker_returncode']=r2.returncode;meta['checked_utc']=now();meta['status']='VERIFIED'if r2.returncode==0 else'CHECK_FAILED';(V/'RUN.json').write_text(json.dumps(meta,indent=2)+'\n')
raise SystemExit(meta['status']!='VERIFIED')
