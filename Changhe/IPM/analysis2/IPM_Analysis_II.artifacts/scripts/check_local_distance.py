"""Independent recomputation of the necessary point-distance tests of the local-distance theorem and of the seven-branch point values.

For an exact reference potential chi = sum a_(j,m,k) Re(x+iy)^(2m) (x^2+y^2)^(k-m) (1+x^2+y^2)^(p_j-k),
p_j = (3+gamma-j delta)/2, the fields rho = -chi_xxy - chi_yyy, u = (-chi_xyy, chi_xxy), V = cX + u and the residual
F = V.D rho - rho are evaluated by mpmath numerical differentiation of chi (a method different from both Taylor jets
and polar polynomial differentiation), at two working precisions whose difference is recorded. The normalization
c + chi_xxyy(0) = 1 and the slope a0 = rho_y(0) are recomputed the same way.

For s = 3*2^-31, kappa = s^(-1/2), a = 4 kappa, g = max(1,r)^(1/5), H = min(a|y|, 16 g), B = min(a r, 104 g),
D_t = B + t kappa r, A_t = a|V| + H + D_t |D rho|, Q_t = a D_t, the largest dyadic radius q = 2^-k with
(t = 0 or a q < a0) and |F| > A_t q + Q_t q^2 is found for t = 0, 1, 4 and compared with the shipped record.

Usage: python3 check_local_distance.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, time, hashlib
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mpm
from mpmath import mp, mpf
sys.set_int_max_str_digits(0)

ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
NAMES = ['state131', 'nb_stableA2_exact', 'nb_stableA3_exact', 'nb_stableA4_exact', 'nb_stableA5_exact',
         'nb_Mpen_exact', 'nb_A6dpen_exact', 'nb_Mpen2_exact', 'nb_b6_exact']
POINTS = [('0', '1/10'), ('0', '1/5'), ('0', '2/5'), ('0', '4/5'), ('0', '1'), ('0', '2'), ('1', '1'), ('3', '4'), ('6', '8')]
PARTIALS = [(2, 1), (0, 3), (3, 1), (1, 3), (2, 2), (0, 4), (1, 2)]


def source(name):
    if name == 'state131':
        p = ROOT / 'source_audit/state131_exact.json'
    elif name == 'nb_b6_exact':
        p = ROOT / '36_b6_candidates/verification/nb_b6_exact.audit.json'
    else:
        p = ROOT / f'19_nb_candidates/verification/{name}.audit.json'
    raw = p.read_bytes(); d = json.loads(raw)
    if name == 'state131':
        cl, a0 = d['exact_parameters']['cl'], d['exact_parameters']['a0']
    else:
        cl, a0 = d['cl'], d['origin_slope']
    terms = [(tuple(k), Q(v)) for k, v in zip(d['canonical_order'], d['canonical_coefficients'])]
    return p, hashlib.sha256(raw).hexdigest(), Q(cl), Q(a0), terms


def make_chi(terms, c):
    g = 1 / c; dl = 1 - g
    js = sorted({j for (j, m, k), _ in terms}); mmax = max(m for (j, m, k), _ in terms)
    kmax = max(k for (j, m, k), _ in terms)
    pj = {j: (3 + g - j * dl) / 2 for j in js}
    coef = [(j, m, k, mpf(v.numerator) / v.denominator) for (j, m, k), v in terms]
    def chi(x, y):
        z = mpm.mpc(x, y); r2 = x * x + y * y; w = 1 + r2
        zp = [mpm.mpc(1)]
        for _ in range(2 * mmax): zp.append(zp[-1] * z)
        rp = [mpf(1)]
        for _ in range(kmax): rp.append(rp[-1] * r2)
        wp = [mpf(1)]
        for _ in range(kmax): wp.append(wp[-1] / w)
        base = {j: w ** (mpf(pj[j].numerator) / pj[j].denominator) for j in js}
        return mpm.fsum(v * zp[2 * m].real * rp[k - m] * base[j] * wp[k] for j, m, k, v in coef)
    return chi


def fields(chi, c, x, y):
    d = {p: mpm.diff(chi, (x, y), p) for p in PARTIALS}
    rho = -d[2, 1] - d[0, 3]; rx = -d[3, 1] - d[1, 3]; ry = -d[2, 2] - d[0, 4]
    vx = c * x - d[1, 2]; vy = c * y + d[2, 1]
    return {'rho': rho, 'rho_x': rx, 'rho_y': ry, 'V_norm': mpm.sqrt(vx * vx + vy * vy),
            'Drho_norm': mpm.sqrt(rx * rx + ry * ry), 'F': vx * rx + vy * ry - rho}


def run(name):
    t0 = time.monotonic()
    p, sha, cl, a0q, terms = source(name)
    res = {}
    for dps in (40, 60):
        mp.dps = dps
        c = mpf(cl.numerator) / cl.denominator
        chi = make_chi(terms, cl)
        center = {pp: mpm.diff(chi, (mpf(0), mpf(0)), pp) for pp in [(2, 2), (0, 4)]}
        pts = {}
        for xs, ys in POINTS:
            x, y = mpf(Q(xs).numerator) / Q(xs).denominator, mpf(Q(ys).numerator) / Q(ys).denominator
            pts[xs, ys] = fields(chi, c, x, y)
        res[dps] = (c, center, pts)
    mp.dps = 60
    c, center, pts = res[60]
    norm_defect = c + center[2, 2]                       # should be 1
    a0 = -center[2, 2] - center[0, 4]
    a0_exact = mpf(a0q.numerator) / a0q.denominator
    rel = lambda u, v: abs(u - v) / max(abs(v), mpf(10) ** -30)
    acc = max(rel(res[40][2][k][f], pts[k][f]) for k in pts for f in pts[k])
    kappa = mpm.sqrt(mpf(2) ** 31 / 3); a = 4 * kappa
    rows = []
    for (xs, ys), f in pts.items():
        x, y = mpf(Q(xs).numerator) / Q(xs).denominator, mpf(Q(ys).numerator) / Q(ys).denominator
        r = mpm.sqrt(x * x + y * y); g = r ** (mpf(1) / 5) if r > 1 else mpf(1)
        Hc = min(a * abs(y), 16 * g); Bc = min(a * r, 104 * g); out = []
        for t in (0, 1, 4):
            Dt = Bc + t * kappa * r; A = a * f['V_norm'] + Hc + Dt * f['Drho_norm']; Qt = a * Dt
            power = None
            for k in range(80):
                q = mpf(2) ** -k
                if (t == 0 or a * q < a0_exact) and abs(f['F']) > A * q + Qt * q * q:
                    power = k; break
            out.append(power)
        rows.append({'point': [xs, ys], 'F': mpm.nstr(f['F'], 20), 'V_norm': mpm.nstr(f['V_norm'], 20),
                     'Drho_norm': mpm.nstr(f['Drho_norm'], 20), 'dyadic_power_t0_t1_t4': out})
        print(name, xs, ys, mpm.nstr(f['F'], 12), out, flush=True)
    extra = {}
    if name == 'nb_b6_exact':
        # second and fourth density derivatives in the ordered tensor norm (multiplicity binom(k, i))
        chi = make_chi(terms, cl)
        x, y = mpf(0), mpf(1) / 5
        d2 = [-mpm.diff(chi, (x, y), (i + 2, 3 - i)) - mpm.diff(chi, (x, y), (i, 5 - i)) for i in range(3)]
        extra['D2rho_norm_at_0_1/5'] = mpm.nstr(mpm.sqrt(d2[0]**2 + 2 * d2[1]**2 + d2[2]**2), 15)
        x, y = mpf(3), mpf(4)
        d4 = [-mpm.diff(chi, (x, y), (i + 2, 5 - i)) - mpm.diff(chi, (x, y), (i, 7 - i)) for i in range(5)]
        extra['r2_D4rho_norm_at_3_4'] = mpm.nstr(26 * mpm.sqrt(sum(mpm.binomial(4, i) * d4[i]**2 for i in range(5))), 15)
        print(name, extra, flush=True)
    return {'source': str(p.relative_to(ROOT)), 'source_sha256': sha, 'terms': len(terms), 'extra': extra,
            'normalization_c_plus_chi_xxyy0': mpm.nstr(norm_defect, 25), 'slope_numeric': mpm.nstr(a0, 25),
            'slope_record': mpm.nstr(a0_exact, 25), 'max_rel_diff_dps40_vs_dps60': mpm.nstr(acc, 3), 'points': rows,
            'seconds': round(time.monotonic() - t0, 1)}


if __name__ == '__main__':
    out = {'method': 'mpmath numerical differentiation of the exact potential at 40 and 60 digits', 'candidates': {}}
    for name in (sys.argv[3:] or NAMES):
        out['candidates'][name] = run(name)
    out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
