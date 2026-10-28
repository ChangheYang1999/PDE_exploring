"""Second exact recombination of the six middle-arc residual replacements."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'08_improved_upper_bounds/middle_circle_transport/balanced_residual/table37'
RAD=ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/radial_refinement'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ctx.prec=384;hashes={}
 def bind(p):hashes[str(p.relative_to(ROOT))]=sha(p)
 p=B/'verification/independent_audit.json';d=load(p);bind(p)
 for name,h in d['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
 for line in (B/'verification/prelaunch_hashes.txt').read_text().splitlines():
  h,name=line.split(maxsplit=1);assert sha(ROOT/name)==h
 bind(B/'verification/prelaunch_hashes.txt');bind(B/'verification/prelaunch_time.txt')
 proof=B/'numerical_values/PROOF.md';bind(proof)
 printed=dict(re.findall(r'^\| ([0-9]+/[0-9]+) \| ([0-9]+\.[0-9]+) \|$',proof.read_text(),re.M))
 assert len(d['residual_checks'])==16*6*17 and all(z['old_intervals_overlap'] for z in d['residual_checks'])
 assert len(d['details'])==512 and [r['row'] for r in d['details']]==list(range(512))
 radial={r['alpha']:r for r in load(RAD/'verification/independent_audit.json')['rows']}
 small={r['alpha']:Q(r['small_upper']) for r in load(RAD.parent/'existing_certificates/verification/independent_audit.json')['rows']}
 rows=[];sec=1/(arb.pi()/64).cos()
 for r in d['rows']:
  a=r['alpha'];assert printed[a]==r['safe_upper_C']
  sums=[Q(0)]*17
  for rr in d['details']:
   assert [v['phase'] for v in rr['phases']]==list(range(17))
   for j,z in enumerate(rr['phases']):sums[j]+=Q(z['new_upper'][a])
  assert sums==list(map(Q,r['new_residual_upper']))
  gains=[max(Q(0),Q(l)-u) for l,u in zip(r['old_source_lower'],sums)]
  assert gains==list(map(Q,r['accepted_gains']))
  phases=[Q(v)-g for v,g in zip(radial[a]['phase_upper'],gains)]
  assert phases==list(map(Q,r['phase_upper']))
  assert r['worst_phase']==max(range(17),key=lambda j:phases[j])
  value=arb(str(small[a]))+sec*arb(str(max(phases)))
  lo=Q(str(value.lower().fmpq()));hi=Q(str(value.upper().fmpq()))
  assert max(lo,Q(r['upper']['lower']))<=min(hi,Q(r['upper']['upper']))
  endpoint=Q(r['safe_upper_C']);assert hi<=endpoint<hi+Q(1,10**10)
  assert endpoint<=Q(radial[a]['safe_upper_C'])
  rows.append(dict(alpha=a,safe_upper_C=r['safe_upper_C'],worst_phase=r['worst_phase']))
 bind(Path(__file__))
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V171',verdict='CONFIRMED',rows=rows,sha256=hashes,
  scope='Complete C upper bounds at six exponents, original middle extraction and plans, all512 residual rows, second exact phase recombination',
  limitation='The alpha1/1000 value is valid but weaker than the existing selected bound.')
 (B/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],'V171 CONFIRMED',rows)
if __name__=='__main__':main()
