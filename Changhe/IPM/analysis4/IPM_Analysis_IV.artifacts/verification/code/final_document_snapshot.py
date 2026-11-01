"""Freeze final documents and inventory their claims without admitting them."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, re, time

started = time.monotonic()
now = datetime.now(timezone.utc)
base = Path('research/301_final_claim_audit')
out = base / 'verification' / now.strftime('%Y%m%dT%H%M%SZ')
out.mkdir(parents=True)
inputs = {
    'lead_summary.md': Path('../a4-lead/FINAL_SUMMARY.md'),
    'lead_theory.md': Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md'),
    'lead_report.md': Path('../a4-lead/FINAL_REPORT.md'),
    'lead_numerics.md': Path('../a4-lead/report_parts/numerics.md'),
    'lead_appendix.md': Path('../a4-lead/report_parts/appendix.md'),
    'numerics_report.md': Path('../a4-num/FARFIELD_NUMERICAL_EXPERIMENTS.md'),
    'numerics_summary.md': Path('../a4-num/NUM_REPORT.md'),
    'verifier_claim_map.md': Path('FINAL_CLAIM_MAP.md'),
    'verifier_radii.md': Path('CERTIFIED_RADII.md'),
    'verifier_radii.json': Path('artifacts/current_certified_radii.json'),
    'verifier_readings.json': base / 'verification/pre_freeze_reading_record.json',
}
manifest=[]
headings=[]
for name, source in inputs.items():
    before=source.stat()
    raw=source.read_bytes()
    after=source.stat()
    assert (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns),str(source)
    (out/name).write_bytes(raw)
    manifest.append(dict(source=str(source),snapshot=str(out/name),sha256=sha256(raw).hexdigest(),bytes=len(raw)))
    if name.endswith('.md'):
        for n,line in enumerate(raw.decode().splitlines(),1):
            cleaned=line.lstrip('* ')
            if line.startswith('#') or re.match(r'(?:Theorem|Lemma|Proposition|Corollary)\s+[A-Z0-9]',cleaned):
                headings.append(dict(document=name,line=n,text=line))
links=[]
text=inputs['verifier_claim_map.md'].read_text()
for target in dict.fromkeys(re.findall(r'\]\(([^)]+)\)',text)):
    target=target.split('#')[0]
    p=Path(target)
    assert not p.is_absolute(),target
    assert p.is_file(),target
    links.append(dict(path=target,sha256=sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
readings=json.loads(inputs['verifier_readings.json'].read_text())
reading_checks=[]
for row in readings['items']:
    p=Path(row['path']);actual=sha256(p.read_bytes()).hexdigest()
    reading_checks.append(dict(path=str(p),expected=row['sha256'],actual=actual,unchanged=actual==row['sha256']))
assert all(r['unchanged'] for r in reading_checks)
result=dict(frozen_at_utc=now.isoformat(timespec='seconds'),scope='Snapshot, heading inventory and linked-proof identity only. No automatic admission of mathematical claims or later edits.',manual_review_pending=True,documents=manifest,heading_count=len(headings),linked_proof_count=len(links),reading_checks=reading_checks,elapsed_s=time.monotonic()-started)
(out/'snapshot_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'claim_headings.json').write_text(json.dumps(headings,indent=2)+'\n')
(out/'linked_proofs.json').write_text(json.dumps(links,indent=2)+'\n')
(base/'sources/final_document_snapshot.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(dict(folder=str(out),documents=len(manifest),headings=len(headings),links=len(links),readings=len(reading_checks),manual_review_pending=True)))
