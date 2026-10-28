"""Register only completed, independently rechecked derivative groups."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
import json,re,sys
p=Path(__file__).resolve().parent;root=p.parents[2];now=datetime.now(timezone.utc).isoformat();groups=sys.argv[1:] or ['fourth','D2u','D2rho','u'];rows={};files={}
claims={'fourth':'|Du|<=14/5, |D rho|<=16, sup r^(4/9)|Du|<=22 and sup r^(4/9)|D rho|<=93','D2u':'<r>|D2u|<=3 and sup r^(13/9)|D2u|<=56','D2rho':'|D2rho|<=3, <r>|D2rho|<=8 and sup r^(13/9)|D2rho|<=93','u':'sup r^(-5/9)|u|<=22'}
for kind in groups:
 assert kind in claims
 a=p/f'nb_d2_exact.{kind}.correlated.json';b=a.with_name(a.stem+'.recheck.json');x=json.loads(a.read_text());y=json.loads(b.read_text());assert x['status']=='COMPLETE' and not x['pending_paths'] and not x['failed'];assert y['all_pass'] and len(x['accepted'])==y['leaves'];assert y['primary_sha256']==sha256(a.read_bytes()).hexdigest();rows[kind]=y['leaves']
 for f in [a,b]:files[f.name]=sha256(f.read_bytes()).hexdigest()
for name in ['nb_d2_exact.algebra.base.json','nb_d2_exact.algebra.higher.json','check_taylor_identity.json']:
 f=p/name;assert json.loads(f.read_text())['all_pass'];files[name]=sha256(f.read_bytes()).hexdigest()
for name in ['build.py','build_derivatives.py','audit_algebra.py','norms_correlated.py','correlated.py','recheck_norms.py','recheck_norms_chunked.py','recheck_fast.py']:
 files[name]=sha256((p/name).read_bytes()).hexdigest()
text='For the exact nb_d2 reference, the following full-plane bounds are independently confirmed: '+ '; '.join(claims[g] for g in groups)+'. The primary and independent covers contain '+', '.join(f'{k}:{n}' for k,n in rows.items())+' leaves. All derivative norms are full ordered Euclidean tensor norms. The two density decay halves combine to the cap186 when both groups pass. No residual smallness or existence follows.'
record={'utc':now,'all_pass':True,'groups':groups,'claims':{g:claims[g] for g in groups},'leaves':rows,'files':files,'proof_sha256':sha256((p.parent/'PROOF.md').read_bytes()).hexdigest(),'method':'512-bit primary correlated Bernstein cover;640-bit independent direct power restriction; complete exact source reconstruction'}
name='audit_norms_'+('_'.join(groups))+'.json';(p/name).write_text(json.dumps(record,indent=2)+'\n')
ledger=root/'VERIFY_REPORT.md';n=max(map(int,re.findall(r'^## V(\d+)\s*\|',ledger.read_text(),re.M)))+1;tag=f'V{n:03d}'
def app(path,s):
 with path.open('a') as f:f.write(s)
app(ledger,f'\n## {tag} | {now} | d2 derivative and decay groups\n\nClaim: The specified d2 derivative and decay caps hold everywhere.\nMethod: Exact independent source algebra, complete512-bit correlated Bernstein covers,640-bit independent direct restrictions and complete-tree checks.\nResult: {text}\nVerdict: CONFIRMED. Evidence:research/95_refit_global_hypotheses/verification/{name}.\n')
app(p/'AUDIT.md',f'\n## {now}: derivative and decay extension\n\n{text}\nAll current source and program hashes are in {name}.\n')
app(p.parent/'RESULTS.md',f'\n## {tag}, {now}: derivative/decay groups\n\n{text}\nVerdict: CONFIRMED. Opus5.5 follow-up pending.\n')
app(root/'NOTES_FOR_TEAM.md',f'\n## {now} | {tag}/topic95: derivative and decay extension\n\n{text}\n\nOpus5.5: please review the exact norm contractions and radial factors in the final sections of PROOF.md, and {name}. The whole reference contract will be consolidated only after all four groups pass. No JavaScript/TypeScript, servers/listeners, RLScience/cluster or remote compute.\n')
for fn in ['S1_THEORY_18H_REPORT.md','S1_PROOFS.md','S1_NUMERICAL_CERTIFICATES.md','S1_CLOSURE.md','S1_RESTART.md']:
 app(root/'research'/fn,f'\n## {tag}: d2 derivative/decay bounds ({now})\n\n{text}\n\nEvidence:95_refit_global_hypotheses/verification/{name}.\n')
app(root/'WORKLOG.md',f'\n## {now}\n{tag}: registered d2 derivative and decay groups '+','.join(groups)+'.\n');print(now,tag)
