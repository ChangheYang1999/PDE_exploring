#!/usr/bin/env python3
"""Independent exact rational ball arithmetic from this auditor's scalar join."""
import json
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ART = HERE.parent
ctx.prec = 512

def read(path):
    return json.loads(path.read_text())

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def aa(value):
    value = F(value)
    return arb(value.numerator)/arb(value.denominator)

joined_path = HERE/'final_join_audit.json'
joined = read(joined_path)
assert joined['status'] == 'INDEPENDENT_FINAL_SCALAR_JOIN_PASS'
assert joined['auditor_code_sha256'] == digest(HERE/'verify_final_join.py')
published_path = ART/'RATIONAL_FINAL_BALL.json'
published = read(published_path)
assert published['status'] == 'EXACT_RATIONAL_FIXED_PARAMETER_BALL_PASS'
assert published['program_sha256'] == digest(ART/'certify_rational_final_ball.py')
for name, expected in published['input_sha256'].items():
    assert digest(ART/name) == expected
R,M,beta2,f2,n,beta,epsilon,C,L = map(F,[
    '381377/1000000000000','3/10','2087491/1000000','7961207/10000000000000',
    '759/100000','7/10','3491/31250','28427625600','57/250'])
r = aa(R/M)
exponents = {'local_gradient':F(20,21),'local_scalar':F(40,21),
             'lower_source_near':F(20,21),'transport_second':F(10,21),
             'transport_third':F(11,21),'source_principal':F(10,21),
             'source_second':F(20,21),'source_fractional':F(1)}
assert set(joined['rates']) == set(exponents)
eps = arb(joined['far_rate'])
weak = arb(0)
for name, power in exponents.items():
    rate = arb(joined['rates'][name])
    eps += (1-aa(power)/2)*rate
    weak += aa(power)/2*rate/(r*r)
assert eps < aa(epsilon) and weak < aa(C)
assert arb(joined['nonlinear_loss']) < aa(L)
assert arb(joined['inherited_N_upper']) < aa('355363/1000000')
b0,bprime = beta-epsilon,beta-epsilon-L
radius_margin = R*beta2-f2
margin = bprime*M*M-n*M-C*R*R
assert b0 == F(9192,15625) and bprime == F(11259,31250)
assert radius_margin == F(355107,10**18) > 0
assert margin == F(8129427150678683343,312500000000000000000) > F(260141,10**7)
assert F(published['exact_L2_radius_margin']) == radius_margin
assert F(published['exact_selfmap_margin']) == margin
pi_lower = F(157,50)
assert arb.pi() > aa(pi_lower)
assert F(25)*M*M/(F(11)*pi_lower*beta2*beta2) < F(123,1000)**2
out = {'status':'INDEPENDENT_EXACT_RATIONAL_BALL_AUDIT_PASS',
       'finished_utc':datetime.now(timezone.utc).isoformat(),
       'bindings':{str(p.relative_to(ART)):digest(p) for p in
                   [Path(__file__),joined_path,published_path,ART/'certify_rational_final_ball.py']},
       'background_epsilon_rebuilt':eps.str(80),'background_C_rebuilt':weak.str(80),
       'R':str(R),'M':str(M),'background_strong_decay':str(b0),
       'nonlinear_loss_upper':str(L),'frozen_strong_decay':str(bprime),
       'exact_L2_radius_margin':str(radius_margin),'exact_selfmap_margin':str(margin),
       'selfmap_margin_decimal':aa(margin).str(80),'contraction_upper':'123/1000',
       'inherited_N_upper':'355363/1000000',
       'scope':'Independent exact final ball inequalities and conservative comparison with this auditor own raw-source scalar reconstruction. Analytic proof chain is separately audited.'}
(HERE/'rational_ball_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
