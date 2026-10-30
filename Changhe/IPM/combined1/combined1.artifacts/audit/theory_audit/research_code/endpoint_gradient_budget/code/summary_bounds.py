from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
from flint import arb, ctx
ctx.prec=768
B=Path(__file__).resolve().parents[1]
p=B/'verification/result.json'
j=json.loads(p.read_text())
assert j['all_assertions_passed']
checks={}
for r in j['rows']:
 checks[r['candidate']]={
  'H_above_328627':arb(r['H_lower_bound'])>328627,
  'radius_above_149800000':arb(r['r_grad_lower_bound'])>149800000,
  'CI_cap_below_3752_over_10pow19':arb(r['CI_cap_upper_bound'])<arb(3752)/10**19,
  'hypothetical_E1_cap_below_15411_over_10pow8':arb(r['hypothetical_E_equal_1_cap'])<arb(15411)/10**8,
  'Ecrit_sharpw_below_20746_over_10000':arb(r['necessary_Ecrit']['sharpw_rounded_ceiling'])<arb(20746)/10000,
  'Ecrit_TB_below_196887_over_100000':arb(r['necessary_Ecrit']['TB_sharp_rounded_ceiling'])<arb(196887)/100000,
  'Ecrit_graded_below_81966_over_100000':arb(r['necessary_Ecrit']['original_graded_ceiling'])<arb(81966)/100000,
 }
 assert all(checks[r['candidate']].values())
res={'utc':datetime.now(timezone.utc).isoformat(),'result_sha256':sha256(p.read_bytes()).hexdigest(),'checks':checks,'all_assertions_passed':True}
with (B/'verification/summary_bounds.json').open('x') as f:json.dump(res,f,indent=2);f.write('\n')
print(res['utc'],res['result_sha256'])
