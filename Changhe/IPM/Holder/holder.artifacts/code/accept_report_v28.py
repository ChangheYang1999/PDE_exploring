"""Exact text and dependency audit of report version28, no numerical work."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/report_v28'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
hashes={}
for rel,ledger in [('05_team_audit/report_v27/accepted.json','V174'),('04_literature/hilbert_chordal/verification/accepted.json','V173')]:
 p=R/rel;d=json.loads(p.read_text());assert d['verdict']=='CONFIRMED' and d['ledger']==ledger;hashes[rel]=sha(p)
 for rel2,h in d['sha256'].items():assert sha(R/rel2)==h,rel2;hashes[rel2]=h
old=(R/'05_team_audit/report_v27/FINAL_REPORT.md').read_text()
a=r'''function for the angular geodesic seminorm $\sup_{0<h\le\pi}|f(x+h)-f(x)|/h^\alpha$ (corollary proved in the accompanying
   artifacts; it depends on Babenko's announced theorem, and it is not a statement for the chordal metric). This is a one-dimensional analogue only; we use it for comparison: it equals'''
b=r'''function for the angular geodesic seminorm $\sup_{0<h\le\pi}|f(x+h)-f(x)|/h^\alpha$, and also for the chordal seminorm
   $\sup|f(x)-f(y)|/|e^{ix}-e^{iy}|^\alpha$, for real and complex inputs (corollaries proved in the accompanying artifacts, from
   Theorem 1(2) with the moduli $h^\alpha$ and $(2\sin\frac h2)^\alpha$; both depend on Babenko's announced theorem, whose proof is not
   given in the source). The two seminorms differ, but the two operator constants agree. This is a one-dimensional analogue only; we use it for comparison: it equals'''
assert old.count(a)==1
expected=old.replace('Draft version 27, 2026-10-28T11:38Z.','Draft version 28, 2026-10-28T11:58Z.').replace(a,b)
assert (B/'FINAL_REPORT.md').read_text()==expected
assert sha(B/'FINAL_REPORT.md')=='81d97c09d7230c22ef14305f15f2a9607a06f8d2b06cf372168828f3afd4f403'
for p in [B/'FINAL_REPORT.md',B/'PROOF.md',B/'diff.txt',Path(__file__)]:hashes[str(p.relative_to(R))]=sha(p)
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V181',verdict='CONFIRMED',scope='Complete text-only v28 diff; chordal theorem exactly V173, with explicit announced-theorem dependency; no numerical changes',sha256=hashes)
(B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],out['ledger'],out['verdict'])
