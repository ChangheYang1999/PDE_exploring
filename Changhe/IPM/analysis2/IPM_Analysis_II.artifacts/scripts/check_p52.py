"""Third computation for verification topic 52 (annular residual bounds and necessary distances for nb_Mpen2_exact and
nb_d2_exact, for every R >= 2^31 and 0 < s <= 2^-12).

Written from the statement in topic 52 only; no verifier code is imported. The canonical coefficients a_(j,m,k) are read
from the audited source records (the same inputs as check_jet_distance.py, with their hashes).

1. Exact far-field sectors. For r > 1, r^(2k) (1 + r^2)^(b_j - k) = sum_q binom(b_j - k, q) r^(2 b_j - 2q), b_j =
   (3 + gamma - j delta)/2, so the potential has sectors chi_(j,q) = r^(3 + gamma - j delta - 2q) sum_n c_n e^(i n theta).
   Cartesian derivatives act exactly on r^p e^(i n theta): d_x = d_z + d_zbar, d_y = i (d_z - d_zbar), with
   d_z (r^p e^(i n theta)) = ((p + n)/2) r^(p-1) e^(i (n-1) theta) and d_zbar (...) = ((p - n)/2) r^(p-1) e^(i (n+1) theta).
   For q <= 3 the script forms rho = -d_y Delta chi, D rho, u = (-d_xyy chi, d_xxy chi), and the truncated residual
   F_t = (c X + u).D rho - rho sector by sector (c X.D multiplies a sector of exponent p by c p), with exact rational
   Laurent polynomials in e^(i theta) (python-flint fmpq_poly for the products). Checks: every sector of exponent above
   p_star = gamma - 6 delta vanishes, the (6, 0) sector is a nonzero sine series, the leading potential sector (0, 0)
   equals that of state 131. The leading sine coefficients e_m, S = sum e_m^2/d_m, S0, S1, S2, Z, C1, C2, the cross
   coefficients C_(h,q) = sum_m a_m E_(h,q,m), the branch sums A_j and the derivative bounds B_(d,j,q) (d = 3, 4, 5:
   max over the order-d Cartesian derivatives of the sum of absolute Fourier coefficients) are compared exactly with
   the verifier's exact record.
2. The inequalities (2) to (7) of topic 52 are evaluated in mpmath interval arithmetic for T = 2^8, ..., 2^31; for each
   successful annulus the lower bound N_(s,R)(F) > L_T/ell and the largest excluded dyadic radius are compared with the
   record.
3. Coding check of the sector expansion: at four points with T <= |X| <= 2T for the best T, the full residual from the
   bivariate interval jets of check_jet_distance.py is compared with F_t; the difference must be below Ctail r^p_star.

Usage: python3 check_p52.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib, time
from fractions import Fraction as Q
from math import comb
from pathlib import Path
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
sys.argv = [sys.argv[0], str(ROOT)]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_jet_distance as cj
from flint import fmpq, fmpq_poly
from mpmath import iv
sys.set_int_max_str_digits(0)
iv.prec = 400
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
I, lo, hi, mag, mig = cj.I, cj.lo, cj.hi, cj.mag, cj.mig
fq = lambda x: fmpq(Q(x).numerator, Q(x).denominator)
tq = lambda x: Q(int(x.p), int(x.q))
t_start = time.monotonic()


class S:
    """r^p * i^ip * sum_n c[n - lo] e^(i n theta), ip in {0, 1}; p is tracked by the caller."""
    def __init__(self, lo_, c, ip=0):
        self.lo, self.c, self.ip = lo_, list(c), ip

    def norm(self):
        while self.c and self.c[-1] == 0: self.c.pop()
        k = 0
        while k < len(self.c) and self.c[k] == 0: k += 1
        self.c = self.c[k:]; self.lo += k
        return self

    def scale(self, a):
        return S(self.lo, [a * x for x in self.c], self.ip).norm()

    def add(self, o):
        if not o.c: return S(self.lo, self.c, self.ip)
        if not self.c: return S(o.lo, o.c, o.ip)
        assert self.ip == o.ip
        l = min(self.lo, o.lo); h = max(self.lo + len(self.c), o.lo + len(o.c))
        r = [fmpq(0)] * (h - l)
        for i, x in enumerate(self.c): r[self.lo - l + i] += x
        for i, x in enumerate(o.c): r[o.lo - l + i] += x
        return S(l, r, self.ip).norm()

    def mul(self, o):
        if not self.c or not o.c: return S(0, [])
        pr = (fmpq_poly(self.c) * fmpq_poly(o.c)).coeffs()
        ip = self.ip + o.ip; sg = 1
        if ip == 2: ip, sg = 0, -1
        return S(self.lo + o.lo, [sg * x for x in pr], ip).norm()

    def abssum(self):
        return sum((abs(x) for x in self.c), fmpq(0))


def dxy(s, p, axis):
    """d_x (axis 0) or d_y (axis 1) of r^p s; result has exponent p - 1."""
    if not s.c: return S(0, [])
    p = fq(p); r = [fmpq(0)] * (len(s.c) + 2)
    for i, x in enumerate(s.c):
        n = s.lo + i
        r[i] += (p + n) / 2 * x                       # index n - 1  ->  i
        r[i + 2] += ((p - n) / 2 if axis == 0 else -(p - n) / 2) * x
    out = S(s.lo - 1, r, s.ip)
    if axis == 1:
        out.ip += 1
        if out.ip == 2: out.ip = 0; out.c = [-x for x in out.c]
    return out.norm()


def potential_sectors(terms, c):
    g = 1 / c; dl = 1 - g
    sec = {}
    for (j, m, k), a in terms:
        b = (3 + g - j * dl) / 2
        for q in range(4):
            bn = Q(1)
            for i in range(q): bn *= (b - k - i)
            bn /= {0: 1, 1: 1, 2: 2, 3: 6}[q]
            d = sec.setdefault((j, q), {})
            if m == 0: d[0] = d.get(0, Q(0)) + a * bn
            else:
                d[2 * m] = d.get(2 * m, Q(0)) + a * bn / 2; d[-2 * m] = d.get(-2 * m, Q(0)) + a * bn / 2
    out = {}
    for key, d in sec.items():
        l = min(d); h = max(d)
        out[key] = (3 + g - key[0] * dl - 2 * key[1], S(l, [fq(d.get(n, Q(0))) for n in range(l, h + 1)]).norm())
    return out


def derivs(s, p, order):
    """all d_x^a d_y^b of r^p s with a + b <= order, keyed by (a, b)."""
    D = {(0, 0): s}
    for n in range(1, order + 1):
        for a in range(n + 1):
            b = n - a
            D[a, b] = dxy(D[a - 1, b], p - (n - 1), 0) if a > 0 else dxy(D[a, b - 1], p - (n - 1), 1)
    return D


def analyse(name, rec_dir):
    pth, shs, c, a0, terms = cj.source(name)
    g = 1 / c; dl = 1 - g; pstar = g - 6 * dl
    pot = potential_sectors(terms, c)
    res = {'source': str(pth.relative_to(ROOT)), 'source_sha256': shs, 'canonical_count': len(terms)}
    fields, bounds = {}, {3: {}, 4: {}, 5: {}}
    for key, (p, s) in pot.items():
        D = derivs(s, p, 5)
        for d in (3, 4, 5):
            bounds[d][key] = max(D[a, d - a].abssum() for a in range(d + 1))
        rho = D[2, 1].add(D[0, 3]).scale(fmpq(-1))
        rx = D[3, 1].add(D[1, 3]).scale(fmpq(-1)); ry = D[2, 2].add(D[0, 4]).scale(fmpq(-1))
        u1 = D[1, 2].scale(fmpq(-1)); u2 = D[2, 1]
        fields[key] = (p, rho, rx, ry, u1, u2)
    Fs = {}
    def put(h, q, e, s):
        if not s.c: return
        if (h, q) in Fs:
            assert Fs[h, q][0] == e; Fs[h, q] = (e, Fs[h, q][1].add(s))
        else: Fs[h, q] = (e, s)
    for (j, q), (p, rho, rx, ry, u1, u2) in fields.items():
        put(j, q, p - 3, rho.scale(fq(c * (p - 3) - 1)))
    for (j1, q1), f1 in fields.items():
        for (j2, q2), f2 in fields.items():
            e = (f1[0] - 3) + (f2[0] - 4)
            put(j1 + j2 + 1, q1 + q2, e, f1[4].mul(f2[2]).add(f1[5].mul(f2[3])))
    for key, (e, s) in Fs.items():
        assert e == g - key[0] * dl - 2 * key[1]
    nonzero = {k: v for k, v in Fs.items() if v[1].c}
    above = sorted(k for k, (e, s) in nonzero.items() if e > pstar)
    zero_cands = sorted(k for k in Fs if not Fs[k][1].c and Fs[k][0] >= -3)
    res['sectors_above_p_star_nonzero'] = above
    res['vanishing_sectors_with_exponent_>=-3'] = [list(k) for k in zero_cands]
    for k in above:
        e, s_ = nonzero[k]
        print(name, 'nonzero sector above p_star', k, float(e), 'terms', len(s_.c), 'max', float(max(abs(x) for x in s_.c)), flush=True)
    assert not above
    e6, s6 = nonzero[6, 0]; assert e6 == pstar and s6.ip == 1
    sine = {}
    for i, x in enumerate(s6.c):
        n = s6.lo + i
        if n > 0:
            xm = s6.c[-n - s6.lo] if 0 <= -n - s6.lo < len(s6.c) else fmpq(0)
            assert xm == -x                                # pure sine series
            if x != 0: sine[n] = tq(xm - x)                # e_n = c_(-n) - c_n
    for k, (e, s) in nonzero.items():
        assert s.ip == 1
        for i, x in enumerate(s.c):
            n = s.lo + i; j = -n - s.lo
            if x != 0: assert 0 <= j < len(s.c) and s.c[j] == -x       # every sector is a real sine series
    dm = {m: Q(1, 35) + Q(m * m, 630) for m in sine}; am = {m: v / dm[m] for m, v in sine.items()}
    Sx = sum((sine[m] * am[m] for m in sine), Q(0)); Sj = [sum((m ** j * abs(v) for m, v in am.items()), Q(0)) for j in range(3)]
    Z = Sj[0] / 16; C1 = Sj[0] / 2 + Sj[1] / 16; C2 = 5 * Sj[0] / 2 + Q(27, 32) * Sj[1] + Sj[2] / 16
    cross = {}
    for k, (e, s) in nonzero.items():
        if k == (6, 0): continue
        v = Q(0)
        for m, a in am.items():
            i1, i2 = -m - s.lo, m - s.lo
            cm = tq(s.c[i1]) if 0 <= i1 < len(s.c) else Q(0); cp = tq(s.c[i2]) if 0 <= i2 < len(s.c) else Q(0)
            v += a * (cm - cp)
        cross[k] = (e, v)
    Aj = {j: sum((abs(a) for (jj, m, k), a in terms if jj == j), Q(0)) for j in range(6)}
    # leading potential moments against state 131
    _, _, c131, _, terms131 = cj.source('state131'); assert c131 == c
    p131 = potential_sectors([t for t in terms131 if t[0][0] == 0], c131)
    res['leading_potential_sector_equals_state131'] = (p131[0, 0][1].lo, p131[0, 0][1].c) == (pot[0, 0][1].lo, pot[0, 0][1].c)
    res['vanishing_potential_sectors'] = sorted([list(k) for k, (p, s) in pot.items() if not s.c])
    # comparison with the verifier's exact record
    rec = json.loads((rec_dir / f'{name}.exact.json').read_text())
    res['record_sha256'] = sha(rec_dir / f'{name}.exact.json')
    cmp_ = {'canonical_sha256_in_record': rec['canonical_sha256'],
            'leading_sine_equal': {str(m): str(v) for m, v in sine.items()} == rec['leading_sine_coefficients'],
            'S_equal': str(Sx) == rec['S'], 'S012_equal': list(map(str, Sj)) == rec['S012'],
            'Z_C1_C2_equal': list(map(str, [Z, C1, C2])) == rec['Z_C1_C2'],
            'branch_sums_equal': {str(j): str(v) for j, v in Aj.items()} == rec['absolute_branch_sums'],
            'p_star_equal': str(pstar) == rec['p_star']}
    rc = {(h, q): (Q(ep), Q(v)) for h, q, ep, v in rec['exact_cross_coefficients']}
    mine = {k: v for k, v in cross.items() if v[1] != 0}; theirs = {k: v for k, v in rc.items() if v[1] != 0}
    cmp_['cross_equal'] = mine == theirs; cmp_['cross_count_nonzero'] = len(mine)
    rb = {int(d): {(j, q): Q(v) for j, q, v in L} for d, L in rec['component_bounds'].items()}
    cmp_['component_bounds_equal'] = all({k: tq(v) for k, v in bounds[d].items()} == rb[d] for d in (3, 4, 5))
    res['comparison_with_record'] = cmp_
    print(name, 'exact part', cmp_, 'seconds', round(time.monotonic() - t_start, 1), flush=True)
    assert all(v for k, v in cmp_.items() if isinstance(v, bool))
    # ---------- part 2: inequalities (2) to (7) ----------
    ann = json.loads((rec_dir / f'{name}.annular.json').read_text()); res['annular_record_sha256'] = sha(rec_dir / f'{name}.annular.json')
    Rm = iv.mpf(2) ** 31; ell = I(Q(11, 10)) / iv.sqrt(iv.mpf(2) ** 53); kk = I(Q(11, 10)) / Rm; mm = 2 * I(c) + 1
    G, DL, PS = I(g), I(dl), I(pstar)
    rows = []
    for tp in [8, 10, 12, 14, 16, 20, 24, 31]:
        T = iv.mpf(2) ** tp; M, Td = {}, {}
        for d in (3, 4, 5):
            M[d] = sum((I(tq(v)) * T ** (-I(Q(j)) * DL - 2 * q) for (j, q), v in bounds[d].items()), iv.mpf(0))
            tau = I(Q(80, 5) * Q(140, 138) ** d) / T ** 2; assert hi(tau) < 1
            Td[d] = comb(79, 4) * iv.mpf(138) ** d * T ** (-8) * sum((I(Aj[j]) * T ** (-j * DL) for j in range(6)), iv.mpf(0)) / (1 - tau)
        Ct = (2 * iv.sqrt(2) * I(c) * Td[4] + 2 * Td[3]) * T ** (G - PS) + 4 * (Td[3] * M[4] + M[3] * Td[4] + Td[3] * Td[4]) * T ** (2 * G - 1 - PS)
        neg = sum((I(-v) * T ** (I(e) - PS) for k, (e, v) in cross.items() if v < 0), iv.mpf(0))
        b = I(Sx) - neg - 2 * Ct * I(Sj[0])
        rr = {'T_power': tp, 'Ctail_upper': float(hi(Ct)), 'b_lower': float(lo(b)), 'positive': lo(b) > 0}
        recrow = next(x for x in ann['rows'] if x['T_power'] == tp)
        if lo(b) > 0:
            Cd = {d: M[d] + Td[d] for d in (3, 4, 5)}
            W = (1 + 4 * T * T / (Rm * Rm)) ** (iv.mpf(11) / 10)
            P = iv.pi * b * T ** (PS + 2) * iv.mpf(2) ** (PS + 1) / 30
            L = P / (W * iv.sqrt(iv.pi * I(Sx))); N = L / ell
            V = 2 * I(c) * T + iv.sqrt(2) * Cd[3] * (2 * T) ** G; V1 = iv.sqrt(2) * I(c) + 2 * Cd[4] * T ** (G - 1)
            D = 2 * iv.sqrt(2) * Cd[4] * T ** (G - 1); D1 = 4 * Cd[5] * T ** (G - 2)
            s3 = iv.sqrt(3 * iv.pi)
            Ah = ell * W * s3 * (V / T * I(C2) + (V1 + mm + kk * V) * I(C1) + kk * mm * T * I(Z))
            Au = I(Q(13, 3)) * ell * W * s3 * ((D1 + kk * D) * T * I(Z) + D * I(C1))
            A = hi(Ah + Au); Qc = hi(W * W * I(C1) / (190000 * 60000 * T)); Pl = lo(P)
            ok = [qq for qq in range(-100, 150) if Pl > A * Q(2) ** qq + Qc * Q(4) ** qq]
            kx = max(ok); assert all(qq in ok for qq in range(min(ok), kx + 1))
            nl = lo(N)
            rr.update({'P_lower': float(Pl), 'L_lower': float(lo(L)), 'N_lower': float(nl), 'A_upper': float(A), 'Q_upper': float(Qc),
                       'excluded_radius_power': kx, 'record_excluded_radius_power': recrow.get('excluded_radius_power'),
                       'record_N_integer_lower': recrow.get('N_integer_lower'),
                       'record_N_below_enclosure': Q(recrow['N_integer_lower']) < nl,
                       'agrees': kx == recrow.get('excluded_radius_power') and Q(recrow['N_integer_lower']) < nl and recrow['positive_pairing']})
        else:
            rr['agrees'] = not recrow['positive_pairing']
        rows.append(rr); print(name, rr, flush=True)
    res['rows'] = rows
    assert all(r['agrees'] for r in rows)
    best = max((r for r in rows if r['positive']), key=lambda r: r['excluded_radius_power'])
    res['best_excluded_radius_power'] = best['excluded_radius_power']; res['best_N_lower'] = max(r['N_lower'] for r in rows if r['positive'])
    res['best_agrees_with_record'] = (best['excluded_radius_power'] == ann['best_excluded_radius_power'] and
                                      ann['best_N_integer_lower'] == max(r['record_N_integer_lower'] for r in rows if r['positive']))
    assert res['best_agrees_with_record']
    # ---------- part 3: coding check of the expansion at the best annulus ----------
    tp = best['T_power']; T = Q(2) ** tp; Ct = best['Ctail_upper']
    checks = []
    for xs, ys in [(Q(0), T), (Q(3, 5) * T, Q(4, 5) * T), (T, T), (Q(1, 3) * T, Q(3, 2) * T)]:
        X, Y = I(xs), I(ys); J = cj.Jets(4)
        Fj = cj.fields(J, cj.chi_jet(J, terms, c, X, Y), c, X, Y)['F'][0]
        r = iv.sqrt(X * X + Y * Y); cs, sn = X / r, Y / r
        cos_, sin_ = {0: iv.mpf(1)}, {0: iv.mpf(0)}
        nmax = max(max(abs(s.lo), abs(s.lo + len(s.c))) for e, s in nonzero.values()) + 1
        for n in range(1, nmax + 1):
            cos_[n] = cos_[n - 1] * cs - sin_[n - 1] * sn; sin_[n] = sin_[n - 1] * cs + cos_[n - 1] * sn
        Ft = iv.mpf(0)
        for k, (e, s) in nonzero.items():
            val = iv.mpf(0)
            for i, x in enumerate(s.c):
                n = s.lo + i
                if n > 0: val -= I(tq(x)) * sin_[n]
                elif n < 0: val += I(tq(x)) * sin_[-n]
            Ft += r ** I(e) * val
        err = mag(Fj - Ft) / lo(r ** PS)
        checks.append({'point_over_T': [str(xs / T), str(ys / T)], 'F_jets': float(lo(Fj)), 'F_truncated': float(lo(Ft)),
                       'normalized_difference_upper': float(err), 'below_Ctail': err < Q(Ct)})
        print(name, checks[-1], flush=True)
    res['cartesian_checks'] = checks
    assert all(ch['below_Ctail'] for ch in checks)
    return res


rec_dir = ROOT / '52_refit_annular_distance/verification'
out = {'inputs': {}}
for name in ['nb_d2_exact', 'nb_Mpen2_exact']:
    out[name] = analyse(name, rec_dir)
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t_start, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
