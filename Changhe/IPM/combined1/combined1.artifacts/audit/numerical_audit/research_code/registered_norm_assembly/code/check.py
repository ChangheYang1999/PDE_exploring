"""Independent monotone norm comparisons with verified rational endpoints."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, time
from fractions import Fraction
from flint import arb, fmpq as Q, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/registered_norm_assembly'

def H(p):
    return sha256(Path(p).read_bytes()).hexdigest()

def R(q):
    if isinstance(q, str):
        f = Fraction(q)
        return Q(f.numerator, f.denominator)
    return Q(q)

def A(q):
    q = R(q)
    return arb(q.numerator)/arb(q.denominator)

def interval(row, low='norm_lower_ball', high='norm_upper_ball'):
    return arb(row[low]).union(arb(row[high]))

def bounds(value, digits=7):
    scale = 10**digits
    center = int(float(value)*scale)
    for padding in [2, 4, 16, 256, 65536, 16777216]:
        lo, hi = Q(center-padding, scale), Q(center+padding, scale)
        if value > A(lo) and value < A(hi):
            return {'ball': value.str(90), 'strict_lower_exact': str(lo),
                    'strict_upper_exact': str(hi), 'strict_bounds_verified': True}
    raise ArithmeticError('No outward rational endpoints at the requested scale')

def derive(comp, s, w1, w2, cw):
    s, cw = Q(s), Q(cw)
    assert 0 < s < 1 and 1-Q(48,25)*s > 0
    E = (comp['P2']**2+w1*comp['G1']**2+w2*comp['G0']**2).sqrt()
    lower = (1-A(Q(48,25)*s))*E
    upper = E**A(1-s)*(2*comp['Q3']**2+A(cw)*E**2)**A(s/2)+A(Q(48,25)*s)*E
    return E, lower, upper

start = time.monotonic()
ctx.prec = 512
manifest = json.loads((BASE/'source/MANIFEST.json').read_text())
for name, row in manifest['files'].items():
    assert H(BASE/'source'/name) == row['sha256']
read = lambda name: json.loads((BASE/'source'/name).read_text())
g0, der, q3 = read('N4_G0.json'), read('N4_derivatives.json'), read('N4_Q3.json')
na, peer, old = read('N4_candidate_audit.json'), read('N3_components.json'), read('N3_registered.json')
assert der['complete'] and q3['complete'] and g0['status'] == 'FINITE'
assert na['generator_sha256'] == peer['source_sha256'] == old['source_sha256']
assert na['canonical_sha256'] == g0['source_sha256']
comp = {'G0': interval(g0), 'G1': interval(der['norms']['G1']),
        'P2': interval(der['norms']['P2']), 'Q3': interval(q3)}
pc = {k: interval(peer['norms'][k], 'norm_lower', 'norm_upper') for k in comp}
component_checks = {k: comp[k].overlaps(pc[k]) for k in comp}
assert all(component_checks.values())
instances = [
    ('sharp', Q(1,7744), 2**14, 2**18, Q(409657,25), Q(76219,10**9), 'FW-T-T4L2-sharp-v1 ('),
    ('sharpw', Q(1,5184), 2**15, 2**20, Q(819257,25), Q(4207,2*10**7), 'FW-T-T4L2-sharpw-v1 ('),
    ('bL7_5', Q(1,5476), 2**15, 2**20, Q(819257,25), Q(423,2500000), 'FW-T-T4L2-bL-v1[7/5] ('),
    ('bL1', Q(1,6561), 2**15, 2**20, Q(819257,25), Q(533,5000000), 'FW-T-T4L2-bL-v1[1] ('),
    ('trans', Q(1,2**17), 2**14, 2**18, Q(409657,25), Q(1989873,250000000000), 'FW-T-T4L2-trans-v1 (')
]
rows = []
for label, s, w1, w2, cw, threshold, prefix in instances:
    E, lower, upper = derive(comp, s, w1, w2, cw)
    pe, pl, pu = derive(pc, s, w1, w2, cw)
    matches = [v for k,v in old['thresholds'].items() if k.startswith(prefix)]
    assert len(matches) == 1
    rec = matches[0]
    assert Fraction(rec['threshold']) == Fraction(str(threshold))
    # Printed peer endpoints can be rounded. Check own full interval directly.
    old_lo, old_hi = A(R(rec['LB'])), A(R(rec['UB']))
    nesting = {'own_lower_greater_than_printed_peer_lower': bool(lower > old_lo),
               'own_upper_less_than_printed_peer_upper': bool(upper < old_hi)}
    assert all(nesting.values()), (label, nesting)
    # The peer arithmetic path encloses each exact endpoint expression from its
    # original component records, irrespective of display formatting.
    assert lower.union(upper).overlaps(pl.union(pu))
    full_bound = lower.union(upper)
    ratio = lower/A(threshold)
    row = {'label':label, 's_exact':str(s), 'w1':w1, 'w2':w2,
           'Cw_exact':str(cw), 'threshold_exact':str(threshold),
           'E_w':bounds(E), 'lower_comparison':bounds(lower),
           'upper_comparison':bounds(upper), 'whole_norm_enclosure':bounds(full_bound,2),
           'lower_threshold_ratio':bounds(ratio,2), 'peer_printed_nesting':nesting,
           'peer_lower_comparison_ball':pl.str(90),
           'peer_upper_comparison_ball':pu.str(90),
           'sufficient_threshold_strictly_failed':bool(lower>A(threshold))}
    assert row['sufficient_threshold_strictly_failed']
    rows.append(row)

star = (comp['P2']**2+2**14*comp['G1']**2+2**18*comp['G0']**2).sqrt()
shares = {'P2': comp['P2']**2/star**2,
          'G1': 2**14*comp['G1']**2/star**2,
          'G0': 2**18*comp['G0']**2/star**2}
# Concrete failure of the frozen nearest-decimal formatting rule.
x = arb(1)/7
printed = x.upper().str(25, radius=False)
assert R(printed) < Q(1,7)
fixture = {'exact': '1/7', 'displayed_upper':printed,
           'exact_shortfall':str(Q(1,7)-R(printed)),
           'display_is_strictly_below_true_value':True}
rF = interval(der['norms']['rF'])
proxy = 2**18*A(Q(20,21))*rF**2
proxy_print = old['derived']['weighted squares UB']['2^18 (20/21) H^2']
proxy_gap = proxy-A(R(proxy_print))
assert proxy_gap > 0
rounding = {'generic_fixture':fixture, 'peer_proxy_display':proxy_print,
            'proxy_exact_containing_ball':proxy.str(100),
            'proxy_minus_display_ball':proxy_gap.str(100),
            'display_not_an_upper_bound_for_proxy_square':True,
            'scope':'The labeled Hardy-proxy square is rounded downward. This does not refute the wide E2 or X norm enclosure, and it does not identify the true H norm with its Hardy proxy.'}
result = {'utc':datetime.now(timezone.utc).isoformat(), 'bits':ctx.prec,
          'candidate':g0['candidate'], 'generator_sha256':na['generator_sha256'],
          'canonical_sha256':na['canonical_sha256'],
          'inputs':{'source/MANIFEST.json':H(BASE/'source/MANIFEST.json'),
                    'PROOF.md':H(BASE/'PROOF.md'), 'code/check.py':H(__file__)},
          'component_overlaps':component_checks, 'E_star':bounds(star),
          'E_star_energy_shares':{k:bounds(v,10) for k,v in shares.items()},
          'instances':rows, 'decimal_format_audit':rounding,
          'elapsed_seconds':time.monotonic()-start,
          'status':'Independent reproduction of registered norm comparisons; source components already independently confirmed; no closure'}
with (BASE/'verification/result.json').open('x') as f:
    json.dump(result,f,indent=2);f.write('\n')
print('completed',result['utc'],'seconds',result['elapsed_seconds'],flush=True)
for row in rows:
    print(row['label'],row['lower_comparison']['ball'][:42],row['upper_comparison']['ball'][:42],row['lower_threshold_ratio']['strict_lower_exact'],flush=True)
print('E_star',star.str(24),'shares',{k:v.str(12) for k,v in shares.items()},flush=True)
print('nearest endpoint failure',fixture,'proxy shortfall',proxy_gap.str(20),flush=True)
