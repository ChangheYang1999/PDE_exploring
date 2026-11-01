"""Bind the exact pre-repair report to a compact reversible text delta."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import difflib,json
from reconstruct_text_delta import reconstruct
from certificate_admission import ref
base=Path('research/301_final_claim_audit')
current=base/'verification/post_freeze_20261031T233028Z/report.json'
raw=reconstruct(current);s=raw.decode()
for a,b in [('2026-10-31T23:29Z','2026-10-31T23:19Z'),('$5.224$ to $5.286$','$5.224$ to $5.285$'),('$1.341$ to $1.348$','$1.341$ to $1.347$'),('$0.9218$ to $0.9265$','$0.9219$ to $0.9265$')]:
    assert s.count(a)==1;s=s.replace(a,b)
a='  polynomial and its circle certificate), the corresponding computations for Theorems T_Q, T_{Q,h} and Corollaries T_4\n  to T_10 (compatibility polynomials, exact response bounds, certified prefixes and radius boxes, necessary radii) and the\n  double-precision tuned runs with their fits, with a README (directory code/tuned);'
b='  polynomial and its circle certificate), with a README (directory code/tuned);'
assert s.count(a)==1;s=s.replace(a,b)
old=s.encode();receipt=base/'verification/admission_V632.json'
expected=json.loads(receipt.read_text())['source_report']['sha256']
assert sha256(old).hexdigest()==expected
before=raw.decode().splitlines(keepends=True);after=s.splitlines(keepends=True)
changes=[]
for tag,a,b,c,e in difflib.SequenceMatcher(a=before,b=after,autojunk=False).get_opcodes():
    if tag!='equal':changes.append(dict(start=a,stop=b,replacement=after[c:e],removed=before[a:b]))
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
out=base/'sources/report_at_V632_delta.json'
assert not out.exists()
out.write_text(json.dumps(dict(format='line-replacement-delta-v1',recorded_at=now,base_delta=ref(current),base_sha256=sha256(raw).hexdigest(),result_sha256=expected,changes=changes,scope='Exact historical report bytes, reconstructed and checked against the original V632 receipt.'),indent=2)+'\n')
assert reconstruct(out)==old
binding=base/'verification/historical_reference_bindings.json'
assert not binding.exists()
binding.write_text(json.dumps(dict(at=now,scope='Additional historical bindings; original admission receipts are unchanged.',bindings=[dict(admission=str(receipt),field='/source_report',original_path='../a4-lead/FINAL_REPORT.md',sha256=expected,delta=ref(out))]),indent=2)+'\n')
print(json.dumps(dict(at=now,delta=str(out),reconstructed_sha256=expected,blocks=len(changes))))
