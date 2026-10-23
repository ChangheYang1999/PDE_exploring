from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('research/single_exceptional_multiplicity');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):checks.append(dict(name=n,passed=bool(b)))
for name,count,proofkey,proof in [('CHECKS.json',824,'proof_sha256','PROOF.md'),('REVIEW_CHECKS.json',26,'factor_proof_sha256','COUNTERCONFIGURATION_FACTOR_PROOF.md')]:
 j=json.loads((V/name).read_text());ck(name+' PASS',j['status']=='PASS'and j['count']==count and all(c['passed']for c in j['checks']));ck(name+' proof binding',j[proofkey]==sha(R/proof))
for folder,proof in [('opus_review','PROOF.md'),('opus_followup','COUNTERCONFIGURATION_FACTOR_PROOF.md')]:
 m=json.loads((V/folder/'metadata.json').read_text());q=json.loads((V/folder/'response.json').read_text());a=(V/folder/'answer.md').read_text()
 ck(folder+' actual model',m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==q['model']=='claude-opus-5-5');ck(folder+' completed',m['stop_reason']==q['stop_reason']=='end_turn'and m['answer_nonempty']);ck(folder+' proof',m['proof_sha256']==sha(R/proof));ck(folder+' dates',m['started_utc']<m['finished_utc']);ck(folder+' text matches payload',a.strip()=='\n\n'.join(x.get('text','')for x in q['content']if x.get('type')=='text').strip());ck(folder+' correct verdict','CORRECT'in a.splitlines()[0])
a=(V/'opus_followup/answer.md').read_text();ck('quartic recovered exactly','749η⁴ + 88168η³ + 2994312η² + 22061260η − 25153453'in a);ck('moment factor recovered','9/352'in a);ck('correction accepted','one common node suffices'in a);ck('context limitation disclosed','definitions'in a and 'Condition:'in a)
conf=json.loads((V/'noninteger_configuration.json').read_text());ck('JSON matches recovered f',conf['polynomial_ascending']==['-25153453','22061260','2994312','88168','749']);ck('original definition matches','M_3=1+18a^3+88(b^3-3b c2)'in(R/'COUNTERCONFIGURATION_FACTOR_PROOF.md').read_text())
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),addendum_sha256=sha(R/'REVIEW_ADDENDUM.md'),driver_sha256=sha(Path(__file__)),review_manifest={folder:{q.name:sha(q)for q in(V/folder).iterdir()if q.is_file()}for folder in ['opus_review','opus_followup']})
(V/'FOLLOWUP_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([c for c in checks if not c['passed']]);raise SystemExit(out['status']!='PASS')
