from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,shutil,sys
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1]; R=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
raw=B/'source/N4_raw_point.json'
if not raw.exists():(B/'source/N4_result.json').rename(raw)
p=json.loads(raw.read_text());u=json.loads((B/'source/N4_uniform_point.json').read_text());e=json.loads((B/'source/N4_point_extensions.json').read_text())
assert sha(raw)==u['point_record_sha256']==e['point_record_sha256']
peer_path=B/'source/N4_canonical.json'; peer_can=json.loads(peer_path.read_text());own_path=R/'new_successor_weak/data/014/canonical.json';own=json.loads(own_path.read_text())
assert sha(peer_path)==p['canonical_sha256']==u['canonical_sha256']==e['canonical_sha256']
assert F(peer_can['cl'])==F(own['cl'])
convert=lambda d:{tuple(k):F(v) for k,v in zip(d['order'],d['coefficients'],strict=True)}
assert convert(peer_can)==convert(own)
assert own['source_sha256']==sha(B/'data/candidate014.json')
params=[('1/262144','1/65536'),('1/65536','3/32768'),('1/8192','43/50000'),('1/131072','1/16384'),('1/50000',None)]
rows=[]
for old,(s,r) in zip(p['ball_exclusions'],params,strict=True):
 row={'framework':old['framework'],'s':s,'upper':old['necessary_upper'],'gap':old['gap'],'necessary_H2s_radius_lower':old['necessary_H2s_radius_lower']}
 if r is None:row['radius_squared']=str(F(1,5000)**2+2*F(1,3000000)**2+F(1,50000000)**2)
 else:row['radius']=r
 rows.append(row)
for old in u['sharp_boxes']:rows.append({'framework':old['framework'],'s':old['s'],'radius':old['radius'],'upper':old['point_upper'],'gap':old['gap']})
out={'candidate':p['candidate'],'point':p['point'],'generator_sha256':sha(B/'data/candidate014.json'),'fields':p['fields'],'uniform_graded_upper':u['uniform_graded_upper'],'uniform_graded_gap':u['uniform_graded_gap'],'ball_exclusions':rows}
with (B/'source/N4_result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
report={'utc':datetime.now(timezone.utc).isoformat(),'exact_canonical_maps_equal':True,'nonzero_canonical_coordinates':len(convert(own)),'source_binding_verified':True,'inputs':{str(p):sha(p) for p in [raw,B/'source/N4_uniform_point.json',B/'source/N4_point_extensions.json',peer_path,own_path,B/'data/candidate014.json',Path(__file__)]},'output_sha256':sha(B/'source/N4_result.json'),'note':'Initial check.py run failed on the unaggregated N4 schema before field evaluation; raw input preserved and normalization explicit here.'}
with (B/'verification/preparation.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print('Exact canonical maps agree:',report['nonzero_canonical_coordinates'])
