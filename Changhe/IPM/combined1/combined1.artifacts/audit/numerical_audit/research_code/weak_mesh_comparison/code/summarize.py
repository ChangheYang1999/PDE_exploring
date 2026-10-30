from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
R=Path(__file__).resolve().parents[3];D=R/'research/weak_mesh_comparison';ctx.prec=512
p=D/'verification/candidate007.json';d=json.loads(p.read_text())
assert len(d['rows'])==9 and [r['k'] for r in d['rows']]==list(range(9))
assert all(all(abs(arb(v))<arb('1e-6') for v in r['peer_relative_difference'].values()) for r in d['rows'])
assert all(abs(arb(r['peer_relative_difference']['m']))<arb('3.578e-7') for r in d['rows'])
assert all(arb(d['rows'][i+1]['exact_balls']['m'])>arb(d['rows'][i]['exact_balls']['m']) for i in range(8))
assert all(d['rows'][0]['previous_exact_overlap'].values())
out={'utc':datetime.now(timezone.utc).isoformat(),'input_sha256':sha256(p.read_bytes()).hexdigest(),'summary_code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'all_component_relative_errors_below':'1e-6','all_m_relative_errors_below':'3.578e-7','best_tested_k':8,'best_exact_ball':d['best_exact_ball'],'k0_previous_overlap':True,'new_k_values_peer_status':'OPEN'}
with (D/'verification/comparison_summary.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
