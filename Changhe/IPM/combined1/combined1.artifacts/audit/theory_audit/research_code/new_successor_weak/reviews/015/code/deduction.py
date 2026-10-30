from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
B=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
s=B/'source/N4_result.json';d=json.loads(s.read_text())
assert d['leading_density_equal_state131'] and d['all_forbidden_zero']
checks={str(j):next(row['exact_zero'] for row in d['sectors'] if row['h']==j and row['q']==0) for j in [1,2,3]}
assert all(checks.values())
m=B/'verification/result.json';r=json.loads(m.read_text());assert r['termwise_rational_map_equal'] and r['exact_c_origin_strain_slope_equal']
out={'utc':datetime.now(timezone.utc).isoformat(),'E1_E2_E3_zero':checks,'same_leading_density':True,'conclusion':'CONFIRMED all T4-297 structure claims by independent canonical identity and unique triangular recurrence','inputs':{str(p):sha(p) for p in [s,m,B/'PROOF.md',Path(__file__)]}}
with (B/'verification/deduction.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['conclusion'])
