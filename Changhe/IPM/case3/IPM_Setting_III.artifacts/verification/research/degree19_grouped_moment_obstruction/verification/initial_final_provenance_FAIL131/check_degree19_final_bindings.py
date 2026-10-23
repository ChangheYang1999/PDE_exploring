from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('research/degree19_grouped_moment_obstruction');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
for name,count,proof,driver,cert,lib in [('TYPES12_CHECKS.json',1258,'TYPES12_PROOF.md','check_degree19_types12.py','types_I_II_certificate.json','exact_polynomial_275.py'),('TYPES34_CHECKS.json',674,'TYPES34_PROOF.md','check_degree19_types34.py','types_III_IV_certificate.json','exact_rational_282.py'),('PARTITION_CHECKS.json',128,'PARTITION_PROOF.md','check_degree19_partitions.py',None,None)]:
 g=json.loads((V/name).read_text());ck(name+' all checks',g['status']=='PASS' and g['count']==count==len(g['checks'])and all(x['passed']for x in g['checks']));ck(name+' proof',g['proof_sha256']==sha(R/proof));ck(name+' driver',g['driver_sha256']==sha(Path('independent_code')/driver))
 if cert:ck(name+' certificate',g['certificate_sha256']==sha(V/cert));c=json.loads((V/cert).read_text());ck(name+' initial proof',c['initial_proof_sha256']==sha(R/'INITIAL_REDUCTION.md'))
 if lib:ck(name+' arithmetic library',g['polynomial_library_sha256'if '12'in name else'rational_library_sha256']==sha(Path('independent_code')/lib))
 if name.startswith('PARTITION'):
  for x in g['algebra_gates']:ck('partition binds '+x['path'],sha(x['path'])==x['sha256'])
for x in json.loads((V/'DEPENDENCIES.json').read_text()):ck('dependency '+x['source'],sha(x['source'])==sha(x['frozen'])==x['sha256'])
for x in json.loads((V/'TYPES34_BINDINGS.json').read_text())['files']:ck('type34 preexecution binding '+x['path'],sha(x['path'])==x['sha256'])
for name in ['dep_1_CHECKS.json','dep_3_LEMMA_CHECKS.json']:
 g=json.loads((V/name).read_text());ck('prior complete '+name,g['status']=='PASS'and len(g['checks'])==g['count']and all(x['passed']for x in g['checks']))
ck('prior275 proof',json.loads((V/'dep_1_CHECKS.json').read_text())['proof_sha256']==sha(V/'dep_0_PROOF.md'));ck('prior278 proof',json.loads((V/'dep_3_LEMMA_CHECKS.json').read_text())['proof_sha256']==sha(V/'dep_2_PROOF.md'))
for name,count in [('initial_types34_FAIL40/TYPES34_CHECKS.json',40),('initial_partition_FAIL108/PARTITION_CHECKS.json',108)]:
 g=json.loads((V/name).read_text());ck('preserved failure '+name,g['status']=='FAIL'and g['count']==count and any(not x['passed']for x in g['checks']))
g=json.loads((V/'PIVOT_REPAIR_COMPARISON.json').read_text());ck('pivot comparison',g['status']=='PASS'and g['count']==2 and all(x['passed']for x in g['checks']))
rows=json.loads((V/'PARTITIONS.json').read_text());ck('all67 rows',len(rows)==67);ck('retained16',sum(x['reason']=='retained'for x in rows)==16)
for x in rows:ck('partition degree '+str((x['A0'],x['multiplicities'])),x['A0']+2*sum(x['multiplicities'])==19)
for name in ['opus_focused','opus_pivot','opus_final','opus_closure']:
 m=json.loads((V/name/'metadata.json').read_text());answer=(V/name/'answer.md').read_text();ck('requested model '+name,m['requested_model']=='us.anthropic.claude-opus-5-5');ck('actual model '+name,m['returned_model']=='claude-opus-5-5');ck('answered '+name,m['answer_nonempty']and bool(answer.strip())and m['stop_reason']=='end_turn');p=json.loads((V/name/'response.json').read_text());ck('response model '+name,p['model']==m['returned_model'])
 if name in ['opus_final','opus_closure']:ck('current proof reviewed '+name,m['proof_sha256']==sha(R/'PROOF.md'));ck('correct verdict '+name,'CORRECT'in answer)
ck('withdrawal recorded','withdraw my earlier restriction'in(V/'opus_final/answer.md').read_text());ck('explanation repairs acknowledged','All four points are valid slips'in(V/'opus_closure/answer.md').read_text())
m=json.loads((V/'opus_review/metadata.json').read_text());ck('initial attempt not a review',not m['answer_nonempty']and m['stop_reason']=='max_tokens')
m=json.loads((V/'opus_initial_retry/metadata.json').read_text());ck('disabled thinking retry rejected',m['status']=='unavailable'and m['error_type']=='ValidationException')
proof=(R/'PROOF.md').read_text();ck('complete conclusion','every possible d=19 partition is excluded'in proof and'd>=21'in proof and'P=n+d/2>=23/2'in proof);ck('primary unresolved','The primary endpoint remains UNRESOLVED'in proof);ck('both failures recorded','FAIL40'in proof and'FAIL108'in proof)
out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),provenance_proof_sha256=sha(R/'FINAL_PROVENANCE_PROOF.md'),driver_sha256=sha(__file__),scope='Evidence binding for the exact degree19 finite auxiliary exclusion; no full-plane endpoint.')
(V/'FINAL_PROVENANCE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([x for x in checks if not x['passed']]);raise SystemExit(out['status']!='PASS')
