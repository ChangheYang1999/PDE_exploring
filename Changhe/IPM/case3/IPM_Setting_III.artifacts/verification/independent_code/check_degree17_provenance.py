from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import exact_polynomial_275 as lib
R=Path('research/degree17_grouped_moment_obstruction');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[]
def ck(n,v,e=None):checks.append(dict(name=n,passed=bool(v),evidence=e))
g=json.loads((V/'CHECKS.json').read_text());ck('exact710 gate',g['status']=='PASS'and g['count']==710 and all(c['passed']for c in g['checks']));ck('proof gate',g['proof_sha256']==sha(R/'PROOF.md'));ck('certificate gate',g['certificate_sha256']==sha(V/'certificate.json'));ck('checker gate',g['driver_sha256']==sha('independent_code/check_degree17_certificate.py'));ck('library gate',g['polynomial_library_sha256']==sha('independent_code/exact_polynomial_275.py'));ck('library import path in this verifier',Path(lib.__file__).resolve()==Path('independent_code/exact_polynomial_275.py').resolve(),lib.__file__)
deps=json.loads((V/'DEPENDENCIES.json').read_text());ls=[d for d in deps if d['frozen'].endswith('exact_polynomial_275_frozen.py')];ck('library exact manifest entry',len(ls)==1 and ls[0]['sha256']==sha(ls[0]['frozen'])==g['polynomial_library_sha256'])
for folder,proof in [('opus_review',V/'PROOF_initial698.md'),('opus_followup',R/'PROOF.md')]:
 p=V/folder;meta=json.loads((p/'metadata.json').read_text());resp=json.loads((p/'response.json').read_text());ck(folder+' requested5.5',meta['requested_model']=='us.anthropic.claude-opus-5-5');ck(folder+' actual5.5',meta['returned_model']=='claude-opus-5-5'and resp['model']==meta['returned_model']);ck(folder+' completed text',meta['answer_nonempty']and meta['stop_reason']=='end_turn');ck(folder+' proof version',meta['proof_sha256']==sha(proof));ck(folder+' ordered actual times',meta['started_utc']<meta['finished_utc']);req=(p/'request.txt').read_text()
 for token in ['noJavaScript/TypeScript/Node','no servers/listeners/tunnels','noRLSciencecluster','noLean/Lake','verification']:ck(folder+' restriction '+token,token in req)
ck('followup explicit CORRECT','**Verdict: CORRECT**'in(V/'opus_followup/answer.md').read_text());ck('followup accepts counterargument','earlier "L+1 unknowns" was wrong'in(V/'opus_followup/answer.md').read_text())
# Initial and revised checks used identical exact identities and certificate.
old=json.loads((V/'CHECKS_initial698.json').read_text());ck('certificate unchanged',old['certificate_sha256']==g['certificate_sha256']);ck('initial698 no failure',old['status']=='PASS'and old['count']==698 and all(c['passed']for c in old['checks']));ck('complete42 partitions',g['partition_count']==42)
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),main_gate_sha256=sha(V/'CHECKS.json'),driver_sha256=sha(__file__))
(V/'PROVENANCE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([c for c in checks if not c['passed']]);raise SystemExit(out['status']!='PASS')
