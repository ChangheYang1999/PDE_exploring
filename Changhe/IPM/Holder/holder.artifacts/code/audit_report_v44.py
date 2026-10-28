from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import difflib,json,re
root=Path(__file__).resolve().parents[1]
out=root/'05_team_audit/report_v44';lead=root.parent/'the lead work'
report=(lead/'FINAL_REPORT.md').read_bytes()
assert b'Draft version 44' in report
text=report.decode();old=(root/'05_team_audit/report_v43/FINAL_REPORT.md').read_text()
(out/'FINAL_REPORT.md').write_bytes(report)
(out/'changes.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile='accepted_v43',tofile='v44')))
source=root/'13_transport_duality/exponent_continuity/certified_neighborhoods/verification/intervals.json'
expected=json.loads(source.read_text())['rows']
block=text[text.index('| $\\alpha_0$ | $r$ |'):]
lines=[s for s in block.splitlines()[2:] if s.startswith('|')][:10]
assert len(lines)==10
for line,r in zip(lines,expected):
    c=[t.strip().strip('$') for t in line.split('|')[1:-1]]
    assert Q(c[0])==Q(r['alpha'])
    exp=int(re.fullmatch(r'10\^\{(-?\d+)\}',c[1])[1])
    assert exp==r['radius_decimal_exponent']
    assert [int(c[2]),int(c[3])]==[r['cutoff_N'],r['cutoff_M']]
    assert Q(c[4])==Q(r['rounded_down_gap'])
notes=(lead/'NOTES_FOR_TEAM.md').read_text()
note=notes[notes.index('## Note 73'):]
if '\n## Note ' in note[1:]: note=note[:note.index('\n## Note ',1)]
(out/'lead_note73.md').write_text(note)
rec=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',report_version=44,table_rows_checked=10,report_sha256=sha256(report).hexdigest(),sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),out/'PROOF.md',out/'changes.diff',out/'lead_note73.md',source]})
(out/'accepted.json').write_text(json.dumps(rec,indent=2)+'\n')
print(rec['timestamp_utc'],rec['report_sha256'])
