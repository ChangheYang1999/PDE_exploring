"""Compare the independently derived Q9 obstruction with the lead's polar code."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
import json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import sympy as sp
ROOT=Path('research/267_period_nine_tuning')
start=time.monotonic()
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
p=ROOT/'verification/obstruction_checks.json';d=json.loads(p.read_text())
assert d['all_checks_pass'] and d['independent_exact']
source=Path('../a4-lead/code/tuned/tq_cert_Q9.log')
lines=source.read_text().splitlines()
end=next(i+1 for i,s in enumerate(lines) if s.startswith('number of real roots:'))
header='\n'.join(lines[:end])+'\n'
frozen=ROOT/'sources/lead_obstruction_output.txt';frozen.write_text(header)
b=sp.Symbol('b')
P=sp.Poly(sp.sympify(next(s.split(' P = ',1)[1] for s in lines[:end] if s.startswith('Q = 9 '))),b,domain=sp.QQ)
scale=F(next(s.split('O_2Q = P * ',1)[1] for s in lines[:end] if s.startswith('O_2Q = P * ')))
assert P.degree()==18
assert [str(P.nth(j)) for j in range(19)]==d['primitive_coefficients']
assert scale==F(d['obstruction_scale'])
root_count=int(lines[end-1].split(':')[-1])
assert root_count==len(d['real_roots'])
printed=[F(s.split('~',1)[1].strip()) for s in lines[:end] if '~' in s]
assert len(printed)==root_count
for a,row in zip(printed,d['real_roots']):
    lo,hi=map(F,row['interval'])
    assert abs(a-lo)<F(1,10**24) and abs(a-hi)<F(1,10**24)
programs=[]
for name in ['tq_cert.py','tq_sym.py']:
    src=Path('../a4-lead/code/tuned')/name
    dest=ROOT/'sources'/('lead_'+name)
    dest.write_bytes(src.read_bytes());programs.append(ref(dest))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,independent_implementations='signed Cartesian Laurent derivatives and positive-frequency polar trigonometric recurrence',polynomial_degree=18,exact_coefficient_comparisons=19,obstruction_scale=str(scale),real_roots=root_count,printed_root_error_strict_upper_bound='1/1000000000000000000000000',own_obstruction=ref(p),lead_frozen_initial_output=ref(frozen),lead_programs=programs,actual_elapsed_s=time.monotonic()-start)
q=ROOT/'verification/lead_comparison.json';q.write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'sources/period_nine_lead_comparison.py').write_bytes(Path('code/period_nine_lead_comparison.py').read_bytes())
print(json.dumps(result))
