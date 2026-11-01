"""Compare independent two-continuation responses to exact symbolic polynomials."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys
sys.dont_write_bytecode=True
import sympy as sp
from flint import arb,ctx
from pure_cartesian_ball import ball,refine_root
ctx.prec=1536
root=Path('research/148_independent_tuned_prefixes')
rootdata=json.loads(Path('research/142_period_four_tuning/verification/root_response_certificates.json').read_text())
responses=json.loads(Path('research/142_period_four_tuning/verification/small_responses.json').read_text())
polys={r['k']:sp.Poly(sp.sympify(r['sigma']),sp.Symbol('b'),domain=sp.QQ) for r in responses['rows']}
rows=[]
for folder in sorted((root/'verification').glob('Q4_root*')):
    d=json.loads((folder/'checks.json').read_text());b,I=refine_root(rootdata['primitive_coefficients_ascending'],rootdata['real_roots'][d['root_index']-1]['interval'],1600)
    counts=0
    for h in d['harmonics']:
        p=polys[h['k']];value=arb(0)
        for c in p.all_coeffs():value=value*b+ball(str(c))
        assert value.overlaps(arb(h['sigma'])),(folder.name,h['k'])
        counts+=1
    row=dict(folder=folder.name,root_index=d['root_index'],exact_polynomial_comparisons=counts,all_overlap=True,source_checks_sha256=sha256((folder/'checks.json').read_bytes()).hexdigest())
    rows.append(row)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows)
(root/'verification/response_comparisons.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/check_tuned_prefix_responses.py').write_bytes(Path('code/check_tuned_prefix_responses.py').read_bytes())
print(json.dumps(result))
