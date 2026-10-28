"""Bind independent proof review and exact disk-containment certificates."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/supplemental_disks'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 hashes={}
 def bind(p):hashes[str(p.relative_to(R))]=sha(p)
 for p,v in [(B.parent/'verification/accepted.json','V230'),(B.parent.parent/'larger_disks/optimal_axis_disks/numerical_values/accepted.json','V226')]:
  d=json.loads(p.read_text());assert d['ledger']==v and d['verdict']=='CONFIRMED';bind(p)
  for n,h in d['sha256'].items():assert sha(R/n)==h;bind(R/n)
 g=json.loads((B/'geometry.json').read_text());assert g['result']=='EXACT_GEOMETRY_PASSED';bind(B/'geometry.json')
 for n,h in g['sha256'].items():assert sha(R/n)==h;bind(R/n)
 note=B/'verification/lead_note63.md';text=note.read_text();assert 'Verdict: CORRECT as stated' in text and 'sympy Sturm counts give no real' in text
 for p in [note,B/'verification/lead_sturm_check.py',B/'verification/lead_sturm_check.out',B/'PROOF.md',Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V234',verdict='CONFIRMED',supersedes_open='V232',sha256=hashes,scope='Additive phase-uniform reflection savings on disjoint disk pairs, including retained cutoff; four rational supplemental pairs have exact Bernstein and independent Sturm containment checks; no new numerical endpoint by this record',independent_review='Actual lead Note63, configured us.anthropic.claude-opus-5-5; provider attestation unavailable')
 (B/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],'V234 CONFIRMED')
if __name__=='__main__':main()
