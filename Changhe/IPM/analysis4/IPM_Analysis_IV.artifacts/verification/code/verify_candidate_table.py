"""Audit the newly printed exact Candidate 007 table against the independent extraction."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
from math import gcd
import json,re
root=Path('research/02_candidate007');theory=Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md')
raw=theory.read_bytes();section=raw.decode().split("### 8.5 Candidate 007's exact leading data",1)[1].split('\n## 9.',1)[0]
source=root/'data/leading_exact.json';original=source.read_bytes();data=json.loads(original)
authority=Path(data['input']);assert sha256(authority.read_bytes()).hexdigest()==data['input_sha256']
rows=re.findall(r'\$a_\{(\d+)\}\$: \$u=(-?\d+)\$, \$v=(\d+)\$',section)
assert [int(m) for m,u,v in rows]==list(range(1,20,2))
for m,u,v in rows:
 assert gcd(int(u),int(v))==1 and int(v)>0
 assert F(int(u),int(v))==F(data['density'][m])
assert F(4076476460239181,2**51)==F(data['c'])
assert 1-1/F(data['c'])==F(1824676646553933,4076476460239181)==F(data['delta'])
values={int(m):F(v) for m,v in data['density'].items()}
rounded=[('first',values[1],F('18.567822'),F(1,2000000)),('ratio',values[3]/values[1],F('0.113493'),F(1,2000000)),('l1',sum(map(abs,values.values())),F('21.58623'),F(1,200000))]
for name,value,display,tolerance in rounded:assert abs(value-display)<tolerance,(name,str(value))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,exact_fraction_matches=len(rows),all_fractions_reduced=True,authority_hash_unchanged=True,parameter_checks=2,rounded_values_checked=3,
 theory=dict(path=str(theory),sha256=sha256(raw).hexdigest()),extraction=dict(path=str(source),sha256=sha256(original).hexdigest()),authority=dict(path=str(authority),sha256=data['input_sha256']))
(root/'verification/printed_table_check.json').write_text(json.dumps(out,indent=2)+'\n')
(root/'verification/printed_table_snapshot.md').write_text("### 8.5 Candidate 007's exact leading data"+section+'\n')
(root/'verification/verify_candidate_table.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(out))
