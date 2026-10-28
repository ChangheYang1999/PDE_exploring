"""Bind actual primary files and locations for the closing statement audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path(__file__).resolve().parents[1]
B=R/'04_literature/final_statement_audit'
S=R/'04_literature/sources'
specs=[
('conjugate_sharp_2014','Theorem 1(2), printed page 2; kernel and proof note','Theorem 1.'),
('korneichuk_stechkin_2020','Lemma 8 and proof, printed pages 8-9','Lemma 8.'),
('mov','Norm definition and Main Lemma, printed page 8','Main Lemma'),
('1604.07670','Definitions 1-2, Proposition 2, Theorems 1 and 3','Proposition 2 ('),
('1201.5385','Theorems 1.1-1.2, printed pages 2-3','Theorem 1.2.'),
('1201.5403','Theorem 1.1, printed page 2','Theorem 1.1.'),
('garcia_cuerva_gatto','Definitions 3.1-3.4 and Theorem 3.6, printed pages 5-7','Theorem 3.6.'),
('holder_riesz_semigroups','Theorem A, Corollary B, Theorem 3.7, Corollary 4.4','Theorem A'),
('schauder_incomplete_1963','Theorem 2.1, printed pages 513-514; also rendered images','THEOREM 2.1.'),
('schauder_poisson','Equations 4.8, 4.9, 4.17, printed pages 22-24','(4.17)'),
('schauder_germs','Theorems 1 and 4 and non-explicit-constant footnote','Theorem 4.'),
('wang_schauder_2006','Theorem 1.1, equation 1.3 and proof, printed pages 637-639','Theorem 1.1')]
hashes={};records=[]
def bind(p):
 hashes[str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
for stem,loc,needle in specs:
 p=S/(stem+'.pdf');t=S/(stem+'.txt')
 assert p.read_bytes().startswith(b'%PDF'),p
 text=t.read_text();assert needle in text,(stem,needle)
 bind(p);bind(t)
 records.append(dict(source=stem,locations=loc,primary_pdf=str(p.relative_to(R)),text=str(t.relative_to(R))))
for rel in ['04_literature/final_statement_audit/PROOF.md','04_literature/READ_BEFORE_LITERATURE.md','05_team_audit/report_v38/FINAL_REPORT.md','04_literature/hilbert_exact/PROOF.md','04_literature/hilbert_periodic_direct/PROOF.md','code/audit_final_literature.py']:
 bind(R/rel)
for p in sorted((B/'verification').glob('*.png')):bind(p)
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V244',verdict='CONFIRMED',claim='The report38 Section2 statements have the primary-source scopes described in PROOF.md.',sources=records,sha256=hashes,limitations=['This binds statements and scope, not an independent proof of every cited theorem.','No new primary source was downloaded.','Nolder, Arsenovic-Mateljevic, Rode-Simonenko and correction, and the relevant AIM book theorem remain unverified.'])
(B/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['time_utc'],out['ledger'],len(records),'primary file pairs bound; statement audit passed')
if __name__=='__main__':pass
