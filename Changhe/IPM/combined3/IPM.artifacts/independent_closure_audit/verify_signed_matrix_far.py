#!/usr/bin/env python3
"""Independent scalar/binding audit of the signed-K exterior matrix price.

This consumes, but never changes, the main-campaign files. The uniform
meaning of each input is justified in INDEPENDENT_ANALYTIC_AUDIT.md.
"""
import json
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ART = HERE.parent
ctx.prec = 512

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def rational(value):
    value = Fraction(value)
    return arb(value.numerator) / arb(value.denominator)

price_path = ART / 'operator_theory/signed_matrix_far_price_v01.json'
price = json.loads(price_path.read_text())
assert price['status'] == 'SIGNED_MATRIX_FAR_PRICE_COMPLETE'
assert price['q'] == '21/10' and price['weight_a'] == '2'
for name, expected in price['bindings'].items():
    assert digest(ART / name) == expected, name
l2_path = ART / 'coercivity_residual/L2_signed_far_v05/result.json'
l2 = json.loads(l2_path.read_text())
assert l2['status'] == 'CERTIFIED_DIRECT_L2'
assert price['signed_theta_origin'] == l2['far_theta']
assert price['source_hashes'] == l2['source_configuration']['source_hashes']
c = rational('4076476460239181/2251799813685248')
q = rational('21/10')
assert Fraction(price['fixed_c']) == Fraction(4076476460239181, 2251799813685248)
p = Fraction(l2['far_theta']['common_gradient_power'])
assert p < 0
nt = arb(l2['far_theta']['normalized_theta_upper']).abs_upper()
rows = []
for row in price['rows']:
    r = arb(row['radius'])
    assert r > arb(l2['far_theta']['endpoint'])
    theta = nt * r ** rational(p)
    assert theta.overlaps(arb(row['signed_K_loss_upper']))
    lower = 1 + (2-q)*c - c/(1+4*r*r)
    lower -= arb(row['u_over_r_upper'])
    lower -= q*arb(row['strain_upper']) + theta
    assert lower.overlaps(arb(row['matrix_lower']))
    assert bool(lower >= rational('7/10')) == row['passes_beta_7_over_10']
    rows.append({'radius': row['radius'], 'independent_lower': lower.str(80),
                 'passes': bool(lower >= rational('7/10'))})
selected = next(row for row in rows if row['radius'] == 30000)
assert selected['passes']
out = {'status': 'INDEPENDENT_SIGNED_MATRIX_FAR_AUDIT_PASS',
       'finished_utc': datetime.now(timezone.utc).isoformat(),
       'auditor_code_sha256': digest(Path(__file__)),
       'price_sha256': digest(price_path), 'L2_sha256': digest(l2_path),
       'binding_checks': True, 'rows': rows,
       'conclusion': 'M(X)>=0.7 I uniformly for |X|>=30000, subject to the independently reviewed actual expansion and signed-theta proofs; no core or stationary existence assertion.'}
(HERE / 'signed_matrix_far_audit.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
