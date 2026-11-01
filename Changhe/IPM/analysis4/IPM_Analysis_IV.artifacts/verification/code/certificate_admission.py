"""Small helpers for auditable, sequential certificate admission."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import gzip,json,re,sys
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
def read(p):
 p=Path(p);r=p.read_bytes();return json.loads(gzip.decompress(r) if p.suffix=='.gz' else r)
def ref(p):
 p=Path(p);return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def checkref(r):
 assert ref(r['path'])['sha256']==r['sha256'],r['path']
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def next_entry(i):
 p=Path('VERIFY_REPORT.md');s=p.read_text();assert max(map(int,re.findall(r'^## V(\d+) \|',s,re.M)))==i-1;return p,s
def reviewed(base,review):
 p=Path(review);assert p.exists() and len(p.read_text())>100
 q=Path(base)/'sources'/p.name
 if p!=q:q.write_bytes(p.read_bytes())
 return q
def admit(base,i,title,claim,method,result,verdict,evidence,review,extra=None):
 base=Path(base);ledger,s=next_entry(i);assert not (base/'verification/admission.json').exists()
 now=stamp();p=base/'PROOF.md';(base/'sources'/f'PROOF_before_V{i}.md').write_bytes(p.read_bytes())
 text=p.read_text();a=text.index('Status:');b=text.index('\n',a)
 text=text[:a]+f'Status: PROVED in V{i}, admitted {now}, within the exact scope below.'+text[b:]
 text+=f'\n## Completed verification\n\n{result}\n\n{verdict}\n';p.write_text(text)
 snapshot=base/'sources'/f'PROOF_at_V{i}.md';snapshot.write_bytes(p.read_bytes())
 receipt=dict(admitted_at_utc=now,ledger=f'V{i}',verdict='PROVED',all_checks_pass=True,evidence=ref(evidence),proof=ref(snapshot),independent_review=ref(review),scope=verdict)
 if extra:receipt.update(extra)
 out=base/'verification/admission.json';out.write_text(json.dumps(receipt,indent=2)+'\n')
 ledger.write_text(s+f'\n## V{i} | {now} | {title}\n\n**Claim.** {claim}\n\n**Method.** {method}\n\n**Result.** {result}\n\n**Verdict: CONFIRMED.** {verdict} Evidence: {out}.\n')
 notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD: V{i}, {title}\n\n{result}\n\n{verdict} Evidence: {out}.\n\n'+notes.read_text())
 for name,line in [('WORKLOG.md',f'{now}: V{i} admitted {title}.'),('VERIFY_SUMMARY.md',f'V{i}: {result} {verdict}'),('research/INDEX.md',f'Update {now}: {base.name} is PROVED in V{i} within its stated scope.')]:
  with Path(name).open('a') as f:f.write('\n'+line+'\n')
 print(json.dumps(dict(at=now,entry=i,title=title)))
