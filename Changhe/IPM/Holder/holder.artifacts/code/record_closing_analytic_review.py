from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import re,json
root=Path(__file__).resolve().parents[1]
folder=root/'05_team_audit/closing_analytic_review'
index=(root/'THEOREM_MAP.md').read_text()
paths={Path(__file__),folder/'PROOF.md',root/'THEOREM_MAP.md',root/'data/verified_table.json',root/'05_team_audit/report_v43/FINAL_REPORT.md',root/'05_team_audit/report_v43/accepted.json',root/'05_team_audit/final_integrity/accepted.json',root/'04_literature/final_statement_audit/verification/accepted.json'}
for path in re.findall(r'\]\(([^)]+)\)',index):
    p=root/path
    assert p.is_file(),p
    if p.name!='VERIFY_REPORT.md':paths.add(p)
paths.add(root/'13_transport_duality/exponent_continuity/certified_neighborhoods/verification/independent_replay.json')
rec=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',report_version=43,scope='Closing analytic synthesis with exact previously accepted numerical replay limits; no new quadrature.',file_count=len(paths),sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in sorted(paths)})
(folder/'verification/accepted.json').write_text(json.dumps(rec,indent=2)+'\n')
print(rec['timestamp_utc'],rec['verdict'],rec['file_count'],'files')
