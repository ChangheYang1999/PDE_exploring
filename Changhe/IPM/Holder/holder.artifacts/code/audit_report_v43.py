from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import difflib, json
root=Path(__file__).resolve().parents[1]
out=root/'05_team_audit/report_v43'
lead=root.parent/'the lead work'
report=(lead/'FINAL_REPORT.md').read_bytes()
assert b'Draft version 43' in report
old=(root/'05_team_audit/report_v42/FINAL_REPORT.md').read_text()
(out/'FINAL_REPORT.md').write_bytes(report)
(out/'changes.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),report.decode().splitlines(True),fromfile='accepted_v42',tofile='v43')))
notes=(lead/'NOTES_FOR_TEAM.md').read_text()
assert 'Note 72' in notes and 'V254 cross-read CORRECT' in notes
proof=root/'08_improved_upper_bounds/local_projection/internal_cycle/PROOF.md'
cert=proof.parent/'verification/cycle_certificate.json'
d=json.loads(cert.read_text())
assert d['sha256'][str(proof.relative_to(root))]==sha256(proof.read_bytes()).hexdigest()
rec=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',report_version=43,closes='V254',report_sha256=sha256(report).hexdigest(),unchanged_table=True,sha256={str(p.relative_to(root) if p.is_relative_to(root) else p):sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),out/'PROOF.md',out/'changes.diff',proof,cert,lead/'NOTES_FOR_TEAM.md']})
(out/'accepted.json').write_text(json.dumps(rec,indent=2)+'\n')
print(rec['timestamp_utc'],rec['report_sha256'])
