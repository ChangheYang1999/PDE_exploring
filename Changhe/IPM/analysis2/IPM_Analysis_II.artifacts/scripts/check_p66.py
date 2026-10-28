"""Third computation for verification topic 66 (Gaussian finite differences and the frozen ordinary C^(1/2) constants
97 for checkpoint 88 and 96 for checkpoint 131).

Written from the statement of topic 66 only; no verifier code is imported. The evaluation routes differ from the
verifier's primary (Arb) and audit (alternating series) routes:

1. Frozen parameters. From the exact source records, check lambda = 2c - 1, c + strain = 1 and sigma = a0/(lambda - 1)
   exactly. For both checkpoints the center jets of rho and V = cX + u are also enclosed directly from the canonical
   potential coefficients (bivariate interval jets of check_jet_distance.py at X = 0): rho_y(0) must enclose a0,
   (V1)_x(0) must enclose lambda and (V2)_y(0) must enclose 1.
2. Kernel moments I_j, 0 <= j <= 7, by the squared forms obtained by integrating by parts, I_(2i) = int r (Delta^i m)^2 dr
   and I_(2i+1) = int r ((Delta^i m)')^2 dr, m = r^sigma exp(-r^2). Delta^i m = exp(-r^2) sum_n q_n r^(sigma + 2n) is
   formed by differentiating r^p exp(-r^2) twice with exact rational exponents, and
   int_0^inf r^beta exp(-2 r^2) dr = Gamma((beta + 1)/2)/(2 2^((beta + 1)/2)). This route is manifestly positive.
3. erf(z) and gamma_lower(1/4, z^2) by the positive Kummer series
   erf(z) = (2/sqrt(pi)) exp(-z^2) sum 2^n z^(2n+1)/(2n+1)!!,  gamma_lower(s, x) = x^s exp(-x) sum x^n/(s (s+1) ... (s+n)),
   summed exactly in rationals with a geometric tail bound (term ratio below x/(s + N + 1) < 1/2 beyond N).
4. B_(theta,z) of (1), A_P^2 of (5) (binomial weights, recorded mu) and (6) (two-term weights; any mu > 0 is valid, the
   enclosure of the recorded optimal mu is used), and the ordinary bound sqrt(A_P^2) B/(1 - alpha), alpha = 1/2, in
   mpmath interval arithmetic at 500 bits. Every recorded safe integer must exceed the upper end, the recorded balls
   must overlap mine, and the headline constants 97 (checkpoint 88) and 96 (checkpoint 131) must hold for the degree 5
   binomial choice.

Usage: python3 check_p66.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib, time, re
from fractions import Fraction as Q
from decimal import Decimal
from math import comb
from pathlib import Path
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
sys.argv = [sys.argv[0], str(ROOT)]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_jet_distance as cj
from mpmath import iv
sys.set_int_max_str_digits(0)
iv.prec = 500
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
I, lo, hi = cj.I, cj.lo, cj.hi
t_start = time.monotonic()
out = {'inputs': {}}


def ball(s):
    m = re.fullmatch(r'\[(.*?) \+/- (.*?)\]', s.strip()); assert m, s
    mid, rad = Q(Decimal(m.group(1))), Q(Decimal(m.group(2)))
    return mid - rad, mid + rad


overlap = lambda x, b: max(lo(x), b[0]) <= min(hi(x), b[1])

rec_dir = ROOT / '66_gaussian_holder/verification'
rec = json.loads((rec_dir / 'compute.json').read_text()); out['inputs']['66_gaussian_holder/verification/compute.json'] = sha(rec_dir / 'compute.json')
rec_states = {r['state']: r for r in rec['states']}

# ---------- 1. frozen parameters ----------
par = {}
for st in (88, 131):
    p = ROOT / f'source_audit/state{st:03d}_exact.json'; out['inputs'][str(p.relative_to(ROOT))] = sha(p)
    d = json.loads(p.read_text()); ep = {k: Q(v) for k, v in d['exact_parameters'].items()}
    c, a0, lam, sg = ep['cl'], ep['a0'], ep['lambda_origin'], ep['sigma']
    folder = 'state088_handoff' if st == 88 else 'state131_last_unverified'
    src = ROOT.parent.parent / f'source/case4/IPM_case4.artifacts/checkpoints/{folder}/accepted_{st:08d}.json'
    chk = {'lambda=2c-1': lam == 2 * c - 1, 'c+strain=1': c + ep['strain'] == 1, 'sigma=a0/(lambda-1)': sg == a0 / (lam - 1),
           'sigma_equals_topic66_record': str(sg) == rec_states[st]['sigma'],
           'checkpoint_sha256_equals_record': sha(src) == rec_states[st]['source_sha256'] == d['source_json_sha256'],
           'sigma>6': sg > 6}
    terms = [(tuple(k), Q(v)) for k, v in zip(d['canonical_order'], d['canonical_coefficients'])]
    J = cj.Jets(5); z0 = I(0)
    f = cj.fields(J, cj.chi_jet(J, terms, c, z0, z0), c, z0, z0); JM = f['J']
    ry, v1x, v2y = f['rho'][JM.pos[0, 1]], f['V1'][JM.pos[1, 0]], f['V2'][JM.pos[0, 1]]
    chk.update({'jet_rho_y(0)_encloses_a0': lo(ry) <= a0 <= hi(ry), 'jet_V1_x(0)_encloses_lambda': lo(v1x) <= lam <= hi(v1x),
                'jet_V2_y(0)_encloses_1': lo(v2y) <= 1 <= hi(v2y)})
    par[st] = (c, a0, lam, sg)
    out[f'state{st}_parameters'] = {'c': str(c), 'a0': str(a0), 'lambda': str(lam), 'sigma': str(sg), 'sigma_float': float(sg),
                                    'jet_widths': [float(hi(x) - lo(x)) for x in (ry, v1x, v2y)], 'checks': chk}
    print(st, chk, flush=True)
    assert all(chk.values())


# ---------- 2. moments by squared forms ----------
def lap(poly, sg):
    """Delta_rad of exp(-r^2) sum_n q_n r^(sg + 2n) via f'' + f'/r of each r^p exp(-r^2)."""
    res = {}
    for n, q in poly.items():
        p = sg + 2 * n
        # (r^p e)' = p r^(p-1) e - 2 r^(p+1) e;  (r^p e)'' = p(p-1) r^(p-2) e - 2p r^p e - 2(p+1) r^p e + 4 r^(p+2) e
        for dn, cf in ((-1, p * (p - 1) + p), (0, -2 * p - 2 * (p + 1) - 2), (1, Q(4))):
            res[n + dn] = res.get(n + dn, Q(0)) + cf * q
    return {k: v for k, v in res.items() if v != 0}


def deriv(poly, sg):
    """(exp(-r^2) sum q_n r^(sg + 2n))' = exp(-r^2) sum [(sg + 2n) q_n r^(sg + 2n - 1) - 2 q_n r^(sg + 2n + 1)];
    returned as a dict exponent -> coefficient (exponents exact rationals)."""
    res = {}
    for n, q in poly.items():
        p = sg + 2 * n
        res[p - 1] = res.get(p - 1, Q(0)) + p * q
        res[p + 1] = res.get(p + 1, Q(0)) - 2 * q
    return res


def gint(beta):
    """int_0^inf r^beta exp(-2 r^2) dr for rational beta > -1."""
    e = I((beta + 1) / 2)
    return iv.gamma(e) / (2 * iv.mpf(2) ** e)


moments = {}
for st in (88, 131):
    sg = par[st][3]; polys = [{0: Q(1)}]
    for i in range(3): polys.append(lap(polys[-1], sg))
    Ij = []
    for j in range(8):
        i = j // 2
        if j % 2 == 0:
            P = {sg + 2 * n: q for n, q in polys[i].items()}
        else:
            P = deriv(polys[i], sg)
        tot = iv.mpf(0)
        for e1, q1 in P.items():
            for e2, q2 in P.items():
                b = 1 + e1 + e2
                assert b > -1
                tot += I(q1 * q2) * gint(b)
        Ij.append(tot)
    moments[st] = Ij
    cmpm = [overlap(x, ball(s)) for x, s in zip(Ij, rec_states[st]['moments'])]
    out[f'state{st}_moments'] = {'values': [float(lo(x)) for x in Ij], 'positive': all(lo(x) > 0 for x in Ij),
                                 'overlap_record': cmpm}
    print(st, 'moments', [float(lo(x)) for x in Ij], cmpm, flush=True)
    assert all(cmpm) and all(lo(x) > 0 for x in Ij)


# ---------- 3. erf and gamma_lower by Kummer series ----------
def kummer(x, s, N=120):
    """sum_(n>=0) x^n/(s (s+1) ... (s+n)) for rational 0 < x < 1, s > 0: exact partial sum and tail bound."""
    tot, term = Q(0), 1 / s
    for n in range(N):
        tot += term; term = term * x / (s + n + 1)
    ratio = x / (s + N + 1); assert ratio < Q(1, 2)
    return iv.mpf([I(tot).a, I(tot + term / (1 - ratio)).b])


sp_ = {}
for st in (88, 131):
    r = rec_states[st]; z = Q(r['z']); th = Q(r['theta']); x = z * z; assert 0 < z < 1 and th == Q(143, 1024)
    assert z == (Q(167, 256) if st == 88 else Q(669, 1024))
    erf = iv.exp(-I(x)) * I(z) * kummer(x, Q(1, 2)) / iv.sqrt(iv.pi)           # erf(z) = gamma_lower(1/2, z^2)/sqrt(pi)
    t2, term = Q(0), z
    for n in range(120):
        t2 += term; term = term * 2 * x / (2 * n + 3)
    erf2 = 2 / iv.sqrt(iv.pi) * iv.exp(-I(x)) * iv.mpf([I(t2).a, I(t2 + 2 * term).b])
    s = Q(1, 4)
    gl = iv.exp(I(s) * iv.log(I(x))) * iv.exp(-I(x)) * kummer(x, s)
    sg = par[st][3]; S = I(sg); al = I(Q(1, 2)); b = S - al
    A = iv.exp(-b / 2 * iv.log(1 - I(th))); k = 1 / (4 * iv.sqrt(I(th)))
    Bv = 4 * iv.exp(al * iv.log(k)) / (al * iv.gamma(S / 2)) * (iv.exp(-al * iv.log(I(z))) * (1 - A * erf2) + A * gl / iv.sqrt(iv.pi))
    cmp_ = {key: overlap(v, ball(r[key])) for key, v in [('erf_z', erf2), ('gamma_lower', gl), ('A_theta', A), ('k_theta', k), ('B', Bv)]}
    cmp_['erf_two_series_overlap'] = max(lo(erf), lo(erf2)) <= min(hi(erf), hi(erf2))
    cmp_['B_positive'] = lo(Bv) > 0
    sp_[st] = Bv
    out[f'state{st}_B'] = {'erf': float(lo(erf2)), 'gamma_lower': float(lo(gl)), 'B': float(lo(Bv)), 'checks': cmp_}
    print(st, 'B', float(lo(Bv)), cmp_, flush=True)
    assert all(cmp_.values())

# ---------- 4. A_P and the ordinary bounds ----------
rows = []
for r in rec['records']:
    st, d, fam = r['state'], r['degree'], r['family']; Ij = moments[st]; S = I(par[st][3]); al = I(Q(1, 2)); a1 = al + 1
    assert Q(3, 2) < d < par[st][3] + 1
    if fam == 'binomial':
        mu = Q(r['mu']); assert mu > 0; M = I(mu)
        Asq = iv.exp(-a1 * iv.log(M)) * iv.gamma(a1) * iv.gamma(d - a1) / (2 * iv.gamma(iv.mpf(d))) * \
            sum((comb(d, j) * M ** j * Ij[j] for j in range(d + 1)), iv.mpf(0))
    else:
        mb = ball(r['optimal_mu']); assert mb[0] > 0
        M = iv.mpf([I(mb[0]).a, I(mb[1]).b])
        Asq = iv.pi / (2 * d * iv.sin(iv.pi * a1 / d)) * iv.exp(-a1 / d * iv.log(M)) * (Ij[0] + M * Ij[d])
    bound = iv.sqrt(Asq) * sp_[st] / (1 - al)
    rr = {'state': st, 'degree': d, 'family': fam, 'bound_upper': float(hi(bound)), 'record_safe_integer': r['safe_integer'],
          'below_record_integer': hi(bound) < r['safe_integer'], 'A_squared_overlap': overlap(Asq, ball(r['A_squared'])),
          'bound_overlap': overlap(bound, ball(r['ordinary_bound']))}
    rows.append(rr); print(rr, flush=True)
out['rows'] = rows
assert all(r['below_record_integer'] and r['A_squared_overlap'] and r['bound_overlap'] for r in rows)
head = {st: next(r for r in rows if r['state'] == st and r['degree'] == 5 and r['family'] == 'binomial')['bound_upper'] for st in (88, 131)}
out['headline'] = {'state88_deg5_binomial_upper': head[88], 'below_97': head[88] < 97, 'below_96.092': head[88] < 96.092,
                   'state131_deg5_binomial_upper': head[131], 'below_96': head[131] < 96, 'below_95.907': head[131] < 95.907,
                   'best_over_all_rows': {st: min(r['bound_upper'] for r in rows if r['state'] == st) for st in (88, 131)}}
print(out['headline'], flush=True)
assert all(v for k, v in out['headline'].items() if isinstance(v, bool))
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t_start, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
