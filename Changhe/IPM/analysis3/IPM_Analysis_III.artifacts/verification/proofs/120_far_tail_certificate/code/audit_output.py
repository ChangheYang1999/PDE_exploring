from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];p=R/'evidence/check.json';d=json.loads(p.read_text())
assert d['status']=='PASS' and d['proof_sha256']==hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest()
assert d['code_sha256']==hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest()
rows={r['T']:r for r in d['rows']}
for t,upper in [('40','3175'),('45','.666'),('60','.000114033')]:assert F(rows[t]['full_Y']['energy_upper']['upper_exact'])<F(upper)
assert F(rows['60']['full_Y']['energy_lower']['lower_exact'])>F('.0001140317')
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','full_Y_tail_energy_upper':{'40':'3175','45':'.666','60':'.000114033'},'full_Y_tail_energy_lower_at60':'.0001140317','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(R/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
