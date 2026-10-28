"""Bind the two separate annular runs and verify all published integer bounds."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
from flint import arb, ctx
ctx.prec=768
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
records=[];rows=[]
for name in ['nb_stableA2_exact','nb_stableA3_exact']:
 p=HERE/(name+'.annular.json');d=json.loads(p.read_text())
 assert d['name']==name and d['precision_bits']==768
 assert d['retained_residual_sector_count']==73 and d['all_sectors_above_p_star_zero']
 assert hashlib.sha256((HERE/'annular_candidates.py').read_bytes()).hexdigest()==d['code_sha256']
 for rel,h in d['dependencies'].items():assert hashlib.sha256((BASE/rel).read_bytes()).hexdigest()==h,(name,rel)
 source=Path('numerics/data')/(name+'.json')
 assert hashlib.sha256(source.read_bytes()).hexdigest()==d['source_sha256']
 for w in d['witnesses']:
  low=arb(w['L_lower_witness_ball']);high=arb(w['N_lower_witness_ball'])
  assert low>w['certified_L_integer_lower'] and high>w['certified_N_integer_lower']
  assert high>arb(2)**w['certified_N_power_lower']
  assert high*arb(2)**35>arb(2)**w['certified_gap_over_eta_power_lower']
  assert len(w['independent_point_checks'])==2
  for pt in w['independent_point_checks']:
   assert pt['passes_uniform_remainder']
   assert arb(pt['normalized_error_upper_ball'])<arb(w['tail']['Ctail'])
  rows.append({'name':name,'T_power':w['T_power'],'R_power':w['R_power'],'L_integer_lower':w['certified_L_integer_lower'],'N_integer_lower':w['certified_N_integer_lower'],'N_power':w['certified_N_power_lower'],'gap_power':w['certified_gap_over_eta_power_lower']})
 records.append(d)
assert records[0]['leading_sine_coefficients']==records[1]['leading_sine_coefficients']
assert arb(records[0]['leading_residual_full_angular_L2']).overlaps(arb(records[1]['leading_residual_full_angular_L2']))
files=[HERE/(name+suffix) for name in ['nb_stableA2_exact','nb_stableA3_exact'] for suffix in ['.annular.json','.sectors.json','.annular.log']]
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','identical_exact_leading_sector':True,'rows':rows,'leading_angular_L2':records[0]['leading_residual_full_angular_L2'],'input_hashes':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
