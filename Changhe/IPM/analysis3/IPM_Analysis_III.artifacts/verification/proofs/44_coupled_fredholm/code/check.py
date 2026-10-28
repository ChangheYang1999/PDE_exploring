"""Independent Arb enclosures of the two angular constants in Theorem C'."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import hashlib, json
from flint import arb, ctx
P = Path(__file__).resolve().parents[1]
ctx.threads = 1

def compute(bits):
    ctx.prec = bits
    a = arb(17)/4
    def beta(x, y):
        return x.gamma()*y.gamma()/(x+y).gamma()
    ia = 2*beta(arb(1)/4, arb(3)/2)
    istr = 2*(16*beta(arb(3)/2, a+arb(5)/2)
              -8*beta(arb(3)/2, a+arb(3)/2)
              +beta(arb(3)/2, a+arb(1)/2))
    cr = (istr*arb(58)/99).sqrt()/arb.pi()
    return {'I_a': ia, 'I_strain': istr, 'c_R': cr}

r = compute(384)
s = compute(768)
for key in r:
    assert r[key].overlaps(s[key])
assert s['c_R'] < arb('0.207570')
intervals = {
    'I_a': ('6.99215347811231949457290557304298510315401320381766176750',
            '6.99215347811231949457290557304298510315401320381766176753'),
    'c_R': ('0.20756986610668143480705395943043232139891409606278751321',
            '0.20756986610668143480705395943043232139891409606278751324')}
for key, (lo, hi) in intervals.items():
    assert arb(lo) < s[key] and s[key] < arb(hi)

def exact(x):
    m, e = x.man_exp()
    return str(Fraction(int(m))*Fraction(2)**int(e))

def record(x):
    return {'ball': x.str(90), 'lower_exact': exact(x.lower()),
            'upper_exact': exact(x.upper())}

out = {'date': datetime.now(timezone.utc).isoformat(), 'result': 'PASS',
       'precision_bits': [384, 768], 'method': 'exact beta-integral formula and Arb gamma functions',
       'results': {key: record(value) for key, value in s.items()},
       'decimal_enclosures': intervals,
       'proof_sha256': hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),
       'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'evidence/check.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
