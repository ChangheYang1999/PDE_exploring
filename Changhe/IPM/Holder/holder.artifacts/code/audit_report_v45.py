from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import difflib,json,re
root=Path(__file__).resolve().parents[1]
out=root/'05_team_audit/report_v45';lead=root.parent/'the lead work'
report=(lead/'FINAL_REPORT.md').read_bytes();text=report.decode()
assert 'Draft version 45' in text
old=(root/'05_team_audit/report_v44/FINAL_REPORT.md').read_text()
assert [l for l in text.splitlines() if l.startswith('|')]==[l for l in old.splitlines() if l.startswith('|')]
(out/'FINAL_REPORT.md').write_bytes(report)
(out/'changes.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile='accepted_v44',tofile='v45')))
source=root/'13_transport_duality/exponent_continuity/cost_comparison/verification/intervals.json'
rows=json.loads(source.read_text())['rows']
block=text[text.index('right side is positive for the radii'):text.index('sufficient intervals only.',text.index('right side is positive for the radii'))]
radius_text=block.split('at the ten exponents')[0]
gap_text=block.split('with lower bounds')[1]
def value(s):
 m=re.fullmatch(r'(?:(\d+)\\cdot)?10\^\{(-?\d+)\}',s)
 if m:return Q(m[1] or 1)*Q(10)**int(m[2])
 return Q(s)
radii=[value(x) for x in re.findall(r'\$([^$]+)\$',radius_text)]
gaps=[value(x) for x in re.findall(r'\$([^$]+)\$',gap_text) if re.fullmatch(r'[0-9.]+',x)]
assert radii==[Q(x['radius']) for x in rows]
assert gaps==[Q(x['rounded_down_gap']) for x in rows]
notes=(lead/'NOTES_FOR_TEAM.md').read_text();note=notes[notes.index('## Note 74'):]
if '\n## Note ' in note[1:]:note=note[:note.index('\n## Note ',1)]
(out/'lead_note74.md').write_text(note)
paths=[Path(__file__),out/'PROOF.md',out/'changes.diff',out/'lead_note74.md',source,source.parent/'independent_replay.json',source.parent.parent/'PROOF.md']
r=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED for operator statements and intervals',report_version=45,closed_ledger_entries=['V258','V259'],radii_and_gaps_checked=10,all_existing_tables_unchanged=True,report_sha256=sha256(report).hexdigest(),sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths})
(out/'accepted.json').write_text(json.dumps(r,indent=2)+'\n')
(source.parent/'accepted.json').write_text(json.dumps(dict(timestamp_utc=r['timestamp_utc'],verdict='CONFIRMED',ledger='V261',analytic_crossread='05_team_audit/report_v45/lead_note74.md',operator_comparison_and_all_ten_intervals_accepted=True,sha256=r['sha256']),indent=2)+'\n')
print(r['timestamp_utc'],r['report_sha256'])
