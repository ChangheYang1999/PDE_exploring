"""Bind the independent analytic cross-read; no numerical operator claims."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'08_improved_upper_bounds/local_projection/strict_increment';P=B/'phase_uniform_density';hashes={}
def bind(p):hashes[str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 for rel,v in [('all_even_moments/verification/accepted.json','V223'),('larger_disks/optimal_axis_disks/verification/accepted.json','V224'),('larger_disks/exact_radial_density/verification/accepted.json','V206'),('larger_disks/radial_density/verification/accepted.json','V195')]:
  p=B/rel;d=json.loads(p.read_text());assert d['verdict']=='CONFIRMED' and d['ledger']==v;bind(p)
  for name,h in d['sha256'].items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==h;bind(R/name)
 note=P/'verification/lead_note60.md';text=note.read_text();assert 'cross-read: CORRECT' in text and 'All correct.' in text
 for p in [P/'PROOF.md',note,P/'symbolic_check.txt',Path(__file__)]:bind(p)
 d=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V230',verdict='CONFIRMED',supersedes_open='V228',sha256=hashes,scope='Phase-uniform reflected-density moments on the accepted disks, including retained cutoff; no new numerical endpoint',independent_review='Actual lead Note60, configured us.anthropic.claude-opus-5-5; provider attestation unavailable')
 (P/'verification/accepted.json').write_text(json.dumps(d,indent=2)+'\n');print(d['time_utc'],'V230 CONFIRMED')
if __name__=='__main__':main()
