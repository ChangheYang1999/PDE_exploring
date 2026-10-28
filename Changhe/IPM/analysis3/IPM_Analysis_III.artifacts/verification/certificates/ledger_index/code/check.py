"""Check ledger IDs and complete proof-index links without executing proof code."""
from pathlib import Path
from datetime import datetime, timezone
import re, json, hashlib
ROOT=Path(__file__).resolve().parents[3]
now=datetime.now(timezone.utc)
ledger=ROOT/'VERIFY_REPORT.md';index=ROOT/'proofs/INDEX.md'
primary=[int(x) for x in re.findall(r'^## V(\d+)\b',ledger.read_text(),re.M)]
supplements=re.findall(r'^### V\d+\b[^\n]*',ledger.read_text(),re.M)
proofs=sorted(str(p.relative_to(ROOT/'proofs')) for p in (ROOT/'proofs').glob('*/PROOF.md'))
links=re.findall(r'\]\(([^)]+)\)',index.read_text())
missing=[p for p in links if not (index.parent/p).exists()]
unindexed=sorted(set(proofs)-set(links))
record={
 'actual_time_utc':now.isoformat(),
 'scope':'Ledger and proof reading-index inventory only, immediately before any subsequent ledger append. No new mathematical validity claim.',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'ledger_sha256_before_append':hashlib.sha256(ledger.read_bytes()).hexdigest(),
 'index_sha256':hashlib.sha256(index.read_bytes()).hexdigest(),
 'primary_claims':len(primary),'last_primary_id':max(primary),
 'primary_sequence_complete_ordered':primary==list(range(1,max(primary)+1)),
 'supplements':supplements,'proof_count':len(proofs),'proof_paths':proofs,
 'index_link_count':len(links),'missing_link_paths':missing,'unindexed_proofs':unindexed,
}
record['passed']=record['primary_sequence_complete_ordered'] and not missing and not unindexed
out=ROOT/'certificates/ledger_index/evidence'/f'check_{now:%H%M%S}.json'
assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='proof_paths'},indent=2))
print('Output:',out.relative_to(ROOT),'SHA256:',hashlib.sha256(out.read_bytes()).hexdigest())
