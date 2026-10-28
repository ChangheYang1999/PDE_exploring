"""Retain the completed analytic cross-read and its primary-source dependency."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'04_literature/hilbert_chordal';V=B/'verification'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(V/'PROOF_crossread.md')=='3581c67ca5cdc1450da02d301dc172cdbd92a0a56612269b8a730f4c4b003340'
assert 'no error found' in (V/'lead_note39.md').read_text()
pdf=R/'04_literature/sources/conjugate_sharp_2014.pdf';txt=pdf.with_suffix('.txt')
assert pdf.read_bytes().startswith(b'%PDF')
assert 'Theorem 1.' in txt.read_text() and 'Remark 3.' in txt.read_text()
old=(B/'PROOF.md').read_text()
assert old==(V/'PROOF_crossread.md').read_text()
new=old.replace('An independent analytic cross-read is pending; no new accepted numerical bound depends on this note.',
 'The lead completed an independent analytic cross-read in Note39 and found no error. The final acceptance and its source dependency are recorded in verification/accepted.json. No planar numerical bound depends on this note.')
assert new!=old;(B/'PROOF.md').write_text(new)
paths=[pdf,txt,B/'PROOF.md',V/'PROOF_crossread.md',V/'lead_note39.md',V/'README.md',R/'04_literature/hilbert_periodic/PROOF.md',Path(__file__)]
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V173',verdict='CONFIRMED',
 claim='Exact periodic Hilbert operator norm for the chordal alpha seminorm equals Gamma(alpha/2) Gamma((1-alpha)/2)/pi^(3/2), 0<alpha<1, real or complex inputs',
 method='Independent analytic derivation, reread of the retained primary Theorem1(2) and Remark3, and lead Note39 cross-read',
 dependency='Babenko announces the exact maximal increment theorem in the retained source; its full proof is not provided there and is not reconstructed in this note.',
 scope='Increment seminorm only. The chordal and angular seminorms differ; their operator constants agree. No planar Riesz conclusion follows.',
 sha256={str(p.relative_to(R)):sha(p) for p in paths})
(V/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],out['ledger'],out['verdict'])
