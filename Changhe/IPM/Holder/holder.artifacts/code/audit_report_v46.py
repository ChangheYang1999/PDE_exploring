from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import difflib, json, re
root = Path(__file__).resolve().parents[1]
out = root / '05_team_audit/report_v46'
lead = root.parent / 'the lead work'
report = (lead / 'FINAL_REPORT.md').read_bytes()
text = report.decode()
assert 'Draft version 46' in text
assert 'enlarges the radii to' not in text
assert 'with smaller gap bounds' not in text
assert 'diameter at most $d>0$' in text
assert '(the zero measure is immediate)' in text
old = (root / '05_team_audit/report_v45/FINAL_REPORT.md').read_text()
assert [l for l in text.splitlines() if l.startswith('|')] == [l for l in old.splitlines() if l.startswith('|')]
source = root / '13_transport_duality/exponent_continuity/cost_comparison/one_sided/verification/intervals.json'
rows = json.loads(source.read_text())['rows']
block = text[text.index('Evaluating the two sides separately'):text.index('same folder, `one_sided/`)', text.index('Evaluating the two sides separately'))]
marker = 'radii '
radius_text = block[block.index(marker) + len(marker):].split('gap bounds')[0]
radius_text = radius_text.split('with corresponding')[0]
gap_text = block.split('gap bounds')[1]
def value(s):
    m = re.fullmatch(r'(?:(\d+)\\cdot)?10\^\{(-?\d+)\}', s)
    if m:
        return Q(m[1] or 1) * Q(10) ** int(m[2])
    return Q(s)
radii = [value(x) for x in re.findall(r'\$([^$]+)\$', radius_text)]
gaps = [value(x) for x in re.findall(r'\$([^$]+)\$', gap_text)]
assert radii == [Q(x['radius']) for x in rows], radii
assert gaps == [Q(x['rounded_down_gap']) for x in rows], gaps
notes = (lead / 'NOTES_FOR_TEAM.md').read_text()
note = notes[notes.index('## Note 75'):]
if '\n## Note ' in note[1:]:
    note = note[:note.index('\n## Note ', 1)]
(out / 'FINAL_REPORT.md').write_bytes(report)
(out / 'lead_note75.md').write_text(note)
(out / 'changes.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True), text.splitlines(True), fromfile='accepted_v45', tofile='v46')))
paths = [Path(__file__), out / 'PROOF.md', out / 'changes.diff', out / 'lead_note75.md', source, source.parent / 'independent_replay.json', source.parent / 'accepted.json', source.parent.parent / 'PROOF.md']
r = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(), verdict='CONFIRMED', report_version=46, ledger='V264', radii_and_gaps_checked=10, all_existing_tables_unchanged=True, report_sha256=sha256(report).hexdigest(), sha256={str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths})
(out / 'accepted.json').write_text(json.dumps(r, indent=2) + '\n')
print(r['timestamp_utc'], r['report_sha256'])
