from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import ast, hashlib, json, math
from flint import arb, ctx
ctx.prec = 256
P = Path(__file__).resolve().parents[1]
S = P / 'code_snapshot'
ns = {'arb': arb, 'math': math}
tree = ast.parse((S/'outward.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef)], type_ignores=[]), 'outward.py', 'exec'), ns)
fup, flo, mx = ns['fup'], ns['flo'], ns['max_upper']
examples = [arb(0), arb(1), arb(-1), arb(1)+arb(2)**-54,
            arb(1)/2+arb(2)**-55, arb(2)**-1200, -arb(2)**-1200,
            arb(2)**1023, arb(0,1), arb('0.1 +/- 0.001')]
for a in examples:
    assert arb(fup(a)) >= a.upper()
    assert arb(flo(a)) <= a.lower()
a = arb(1)/2
b = a + arb(2)**-55
assert mx([a,b]).upper() == b.upper()
assert mx([b,a]).upper() == b.upper()
assert fup(arb(2)**-1200) == math.ldexp(1., -1074)
assert flo(-arb(2)**-1200) == -math.ldexp(1., -1074)
for v in [math.nan, math.inf, -math.inf]:
    try:
        ns['finite_or_raise'](v, 'test')
    except ValueError:
        pass
    else:
        raise AssertionError('nonfinite not rejected')
# Isolate the actual nested t_of: no driver import or pipeline work.
otree = ast.parse((S/'offbasis.py').read_text())
fun = next(n for n in ast.walk(otree) if isinstance(n,ast.FunctionDef) and n.name=='t_of')
ons = {'arb':arb}
exec(compile(ast.Module(body=[fun],type_ignores=[]),'offbasis.t_of','exec'),ons)
small = arb(2)**-1200
bad = ons['t_of'](small,arb(0),arb(0))
assert bad == 0 and small > 0
# Repaired gradient bound encloses the maximum of a unit interval square.
r = arb(0,1)
R, T = arb(r.abs_upper()), arb(r.abs_upper())
good = (R*R + T*T).sqrt()
assert str(good) != 'nan' and arb(good.upper()) >= arb(arb(2).sqrt().upper())
# Exact trigonometric quotient identity encoded in Laurent polynomials.
# sin(2n theta)=cos(theta)*2 sum_{k=1}^n (-1)^(n-k)sin((2k-1)theta).
# Remove the common 1/(2i) and convolve with cos=(z+z^-1)/2.
for n in range(1,33):
    out = {}
    for k in range(1,n+1):
        a = (-1)**(n-k)
        for freq,sign in [(2*k-1,1),(-(2*k-1),-1)]:
            for shift in [-1,1]:
                out[freq+shift] = out.get(freq+shift,0)+a*sign
    out = {k:v for k,v in out.items() if v}
    assert out == {2*n:1,-2*n:-1}
# General multiplicative-fudge counterexample survives the repaired scalar conversions.
z = math.ldexp(1.,-600)
assert z*z*(1+1e-8) == 0 and z > 0
out = {
 'date':datetime.now(timezone.utc).isoformat(), 'result':'PASS',
 'scope':'directed scalar conversions; exact row maximum; repaired gradient and quotient algebra; surviving underflow counterexamples',
 't_of_input':'2^-1200', 't_of_actual_output':str(bad),
 't_of_required_positive_square_root':'2^-600',
 'gradient_upper_ball':str(good),
 'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),
 'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(S.glob('*.py'))}
}
(P/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
