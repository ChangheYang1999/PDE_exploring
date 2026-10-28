"""Accept unchanged-mass middle residual replacement with a second sum check."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,re
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/middle_circle_transport/balanced_residual'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def main():
 ctx.prec=384;hashes={}
 def bind(p):hashes[str(p.relative_to(ROOT))]=sha(p)
 src=BASE/'verification/independent_audit.json';d=load(src);bind(src)
 for name,h in d['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
 proof=BASE/'PROOF.md';assert sha(proof)=='e00bc7fb02978cb18fd32688e8fb21bfba2515eb05e1abf135e6ca9ca918fb94';bind(proof)
 note=ROOT/'05_team_audit/lead_note36/NOTE.md';assert sha(proof) in note.read_text();bind(note)
 statement=BASE/'numerical_values/PROOF.md';bind(statement)
 printed={a:(c,e) for a,c,e in re.findall(r'^\| ([0-9]+/[0-9]+) \| ([0-9]+\.[0-9]+) \| ([0-9]+\.[0-9]+) \|$',statement.read_text(),re.M)}
 mid=ROOT/'data/middle_circle_certificate_n512.json';mh=sha(mid)
 for suffix in ('a30','a50','a75','a90'):
  p=ROOT/('data/local_circle_composite_'+suffix+'.json');assert load(p)['input_hashes']['data/middle_circle_certificate_n512.json']==mh;bind(p)
 assert load(ROOT/'data/middle_composite_upper_n512.json')['input_sha256']['data/middle_circle_certificate_n512.json']==mh
 radial=load(ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/radial_refinement/verification/independent_audit.json')
 crows={r['alpha']:r for r in radial['rows']}
 small=load(ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/existing_certificates/verification/independent_audit.json');small={r['alpha']:Q(r['small_upper']) for r in small['rows']}
 rows=[];sec=1/(arb.pi()/64).cos()
 for r in d['rows']:
  a=r['alpha'];assert printed[a]==(r['safe_upper_C'],r['safe_upper_D'])
  totals=[Q(0)]*17
  for k in range(512):
   p=BASE/'verification/mass_replay'/f'row_{k:03d}.json';v=load(p)
   assert v['row']==k and v['subdivisions']==8 and len(v['phases'])==17
   for j,z in enumerate(v['phases']):totals[j]+=Q(z['new'][a]['upper'])
  for j,z in enumerate(r['residual_checks']):
   assert z['phase']==j and totals[j]==Q(z['new_residual_upper'])
   gain=max(Q(0),Q(z['old_source_lower'])-totals[j]);assert gain==Q(z['accepted_gain'])
   assert Q(r['C_phase_upper'][j])==Q(crows[a]['phase_upper'][j])-gain
  cphase=list(map(Q,r['C_phase_upper']));dphase=list(map(Q,r['D_phase_upper']))
  assert r['worst_C_phase']==max(range(17),key=lambda j:cphase[j]);assert r['worst_D_phase']==max(range(17),key=lambda j:dphase[j])
  independent_c=arb(str(small[a]))+sec*arb(str(max(cphase)))
  assert Q(str(independent_c.upper().fmpq()))<=Q(r['safe_upper_C'])
  for op in ('C','D'):
   up=Q(r['upper_'+op]['upper']);s=Q(r['safe_upper_'+op]);assert up<=s<up+Q(1,10**10)
   assert s<=Q(r['old_upper_'+op])
  rows.append({k:r[k] for k in ('alpha','safe_upper_C','safe_upper_D','worst_C_phase','worst_D_phase')})
 bind(Path(__file__))
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V168',verdict='CONFIRMED',rows=rows,sha256=hashes,
  scope='Complete C and D upper bounds, unchanged extracted masses, full 512-row replay and exact phase recombination',
  cross_read_note='The parenthetical i-to-i assertion in lead Note36 is a harmless typo and is not used; the Mobius map preserves the upper half-plane.')
 (BASE/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],'V168 CONFIRMED',rows)
if __name__=='__main__':main()
