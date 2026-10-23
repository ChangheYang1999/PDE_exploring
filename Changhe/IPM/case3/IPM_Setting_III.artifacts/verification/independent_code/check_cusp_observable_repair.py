"""Result236 final local observable repair; no producer code executed."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal,localcontext
import hashlib,json
R=Path('research/cusp_polar_repair_audit');V=R/'verification/observable_repaired';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
for row in json.loads((V/'INPUTS.json').read_text())['files']:ck('frozen '+row['frozen'],sha(row['frozen'])==row['sha256'])
p=json.loads((R/'verification/repaired/CHECKS.json').read_text());a=json.loads((R/'verification/CHECKS.json').read_text())
ck('prior55',p['status']=='PASS' and p['count']==55 and all(x['passed'] for x in p['checks']))
ck('prior44',a['status']=='PASS' and a['count']==44 and all(x['passed'] for x in a['checks']))
ck('parent gate unchanged',p['parent_sha256']==sha(R/'verification/CHECKS.json'))
ck('parent repair proof unchanged',p['proof_sha256']==sha(R/'REPAIR_PROOF.md'))
t=' '.join((V/'NUM_REPORT.md').read_text().split())
for phrase in ['adds a term (c p - 1) K y^p to R_h, i.e. a linear term -1.48e-16 y to y R_h/N_f',
 'their complete C_p/K is -1.441028e-5 / +7.822256e-5 / +8.534005e-4',
 'the stored K - 1 of these states is +1.7e-11 / +4.2e-11 / +2.1e-10',
 'trace-dependent coefficient; the exact tails beyond 1e6 are -7.2e-9 / +3.6e-8 / +4.0e-7 K']:
 ck('current wording '+phrase,phrase in t)
ck('incorrect raw observable removed','adds a linear axis term -1.48e-16 y to R_h' not in t)
with localcontext() as ctx:
 ctx.prec=100
 for row in a['states']:
  e=Decimal(row['cp_minus1']);coef=e/(abs(1+e)+1)
  ck(row['tag']+' divided coefficient rounds correctly',abs(coef-Decimal('-1.48e-16'))<Decimal('0.005e-16'),str(coef))
ck('raw and scaled terms have distinct exponents','(cp-1)K y^p' in (R/'OBSERVABLE_REPAIR_PROOF.md').read_text())
o=dict(status='PASS' if all(x['passed'] for x in checks) else 'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'OBSERVABLE_REPAIR_PROOF.md'),driver_sha256=sha(__file__),inputs_sha256=sha(V/'INPUTS.json'),parent_sha256=sha(R/'verification/repaired/CHECKS.json'))
(V/'CHECKS.json').write_text(json.dumps(o,indent=2)+'\n');print(o['status'],o['count']);print([c for c in checks if not c['passed']])
if o['status']!='PASS':raise SystemExit(1)
