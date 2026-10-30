"""Validation of legqs_norms (lane c1-n3). Usage: legqs_tests.py <test letters, e.g. ACDE or B>"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json, sys, time, tempfile
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from flint import fmpq, fmpq_poly, arb, ctx
import e2norms as E, legqs_e2norms as LS, legqs_norms as LN, legqs_integrals as LI
from e2norms import fq, Z, OM, ONE
C131 = Q(4076476460239181, 2251799813685248)
which = sys.argv[1] if len(sys.argv) > 1 else 'ACDE'

def write_cand(gens, c=C131):
    f = Path(tempfile.mkdtemp()) / 'g.json'; f.write_text(json.dumps({'cl': str(c), 'generators': gens})); return f

def expand_legqs_to_ordinary(gens):
    """Rewrite legqs generators with R0 = 1 as ordinary (j, m, k) terms (exact), for the identity test."""
    out = []
    for g in gens:
        s = g['spec']
        if s[0] != 'legqs': out.append(g); continue
        w, n, qpow, R0 = s[1:]; assert Q(R0) == 1
        poly = {}
        for h, b in E.legendre_monomials(n).items():
            for q in range(qpow + 1):
                e = w + h + q; poly[e] = poly.get(e, Q(0)) + b * comb(qpow, q) * (-1) ** q
        for e, b in poly.items():
            if b: out.append({'m': g['m'], 'j': g['j'], 'spec': ['mono', e], 'coef': str(Q(g['coef']) * b)})
    return out

if 'A' in which:
    print('--- A: J tables (exact recurrences) against 2F1 balls')
    tabs = LN.ScaleTables(); ok = True; worst = 0
    for a in (Q(624), Q(99), Q(2499)):
        for b0 in (Q(-37, 100), Q(0), Q(1824676646553933, 4076476460239181) / 2 - 1):   # third class: b0 = delta/2 - 1 in (-1, 0) (N4-300: the first version used -1/2 + delta - 1 < -1, inadmissible)
            I0 = tabs.I0(a, b0)
            for i in range(0, 15):
                for m in range(0, 41, 7):
                    R1, R2 = tabs.entry(a, b0, m, i); mine = LN.fq2arb(R1) + LN.fq2arb(R2) * I0
                    ref = LI.J(b0 + m, 0, a, i, 1024)
                    if not mine.overlaps(ref): ok = False; print('MISMATCH', a, b0, m, i, mine, ref)
                    worst = max(worst, float(mine.rad()) / max(float(abs(mine.mid())), 1e-300))
    print('J table entries overlap the 2F1 balls for 3 scales x 3 classes x 15 i x 6 m:', ok, 'worst relative radius', worst)
    # large m (probe-type) entries against 2F1 at 1024 bits
    ok2 = True
    for m in (600, 1800, 2400):
        R1, R2 = tabs.entry(Q(624), Q(-37, 100), m, 23); mine = LN.fq2arb(R1) + LN.fq2arb(R2) * tabs.I0(Q(624), Q(-37, 100)); ref = LI.J(Q(-37, 100) + m, 0, Q(624), 23, 1024)
        ok2 = ok2 and mine.overlaps(ref)
    print('large-m entries (m = 600, 1800, 2400; i = 23) overlap 2F1:', ok2, 'digits of the m = 2400 entry:', len(str(R1.q)))
    # I0 against mpmath
    import mpmath; mpmath.mp.dps = 50
    for a, b0 in ((Q(624), Q(-37, 100)), (Q(2499), Q(0))):
        ref = mpmath.quad(lambda v: v ** (mpmath.mpf(b0.numerator) / b0.denominator) / (1 + int(a) * v), [0, mpmath.mpf(1) / 1000, mpmath.mpf(1) / 30, 1])
        print('I0', a, b0, tabs.I0(a, b0).str(25), 'mpmath', mpmath.nstr(ref, 25))

if 'C' in which:
    print('--- C: legqs generators with R0 = 1 reproduce the ordinary expansion exactly (fields, F, D1, D2, norms)')
    gens = [{'m': 2, 'j': 1, 'spec': ['legqs', 1, 2, 4, 1], 'coef': '3/7'}, {'m': 3, 'j': 0, 'spec': ['legqs', 0, 1, 4, 1], 'coef': '-2/5'},
            {'m': 1, 'j': 2, 'spec': ['legqs', 0, 3, 4, 1], 'coef': '5/11'}, {'m': 0, 'j': 0, 'spec': ['legqs', 2, 2, 4, 1], 'coef': '1/3'},
            {'m': 1, 'j': 3, 'spec': ['legqs', 0, 0, 4, 1], 'coef': '7/2'}]
    f1 = write_cand(gens); f2 = write_cand(expand_legqs_to_ordinary(gens))
    c, A1, A1s, _, m1 = LS.load_reference_legqs(f1); c2, A2, A2s, _, m2 = LS.load_reference_legqs(f2); assert not A2s
    D1, f1d = LN.residual_t(A1, A1s, c, 2, log=lambda *a: None); D2, f2d = LN.residual_t(A2, {}, c, 2, log=lambda *a: None)
    cc, A3, _, _, _ = E.load_reference(f2); D3, _ = E.residual_polynomials(A3, cc, 2, log=lambda *a: None)
    ok = all(LN.equal_t(D1[k], D2[k]) for k in D1) and all(LN.to_plain(D2[k]) == D3[k] for k in D3)
    print('R0 = 1 residual components identical to the ordinary expansion and to e2norms (d <= 2):', ok, m1)
    delta = 1 - 1 / c
    for label, d, a, tp, ser in LN.STANDARD[:4]:
        r1 = LN.norm_t(D1, d, delta, a, tp, ser, 56, label); r3 = E.norm(D3, d, delta, a, tp, ser, 56, label)
        sameS = r1['status'] == r3['status'] and (r1['status'] != 'FINITE' or 2 * fmpq(r1['S_exact_rational']) == fmpq(r3['base_beta_sum']))
        close = r1['status'] != 'FINITE' or (abs(arb(r1['norm_lower']) - arb(r3['norm_lower'])) < 1e-100 and abs(arb(r1['norm_upper']) - arb(r3['norm_upper'])) < 1e-100)
        print(f"  {label}: {r1['status']} legqs {r1.get('norm_lower_ball','')[:30]} e2norms {r3.get('norm_lower_ball','')[:30]} S identical: {sameS}; bounds within 1e-100: {close}")

if 'D' in which or 'E' in which:
    import mpmath; mpmath.mp.dps = 60
    gens = [{'m': 2, 'j': 1, 'spec': ['legqs', 0, 2, 4, 25], 'coef': '3/7'}, {'m': 3, 'j': 0, 'spec': ['legqs', 0, 1, 4, 25], 'coef': '-2/5'},
            {'m': 1, 'j': 2, 'spec': ['legqs', 0, 1, 4, 25], 'coef': '5/11'}, {'m': 0, 'j': 0, 'spec': ['legqs', 1, 2, 4, 25], 'coef': '1/3'},
            {'m': 1, 'j': 3, 'spec': ['legqs', 0, 0, 4, 25], 'coef': '7/2'}, {'m': 2, 'j': 3, 'spec': ['legqs', 1, 0, 4, 10], 'coef': '-1/9'}]
    f = write_cand(gens); c, A, A_s, _, meta = LS.load_reference_legqs(f); delta = 1 - 1 / c; gamma = 1 / c
    D, fields = LN.residual_t(A, A_s, c, 2, log=lambda *a: None)
    def mpq(x): x = Q(x); return mpmath.mpf(x.numerator) / x.denominator
    cm = mpq(c); dm = mpq(delta)
    def chi(x, y):
        r2 = x * x + y * y; th = mpmath.atan2(y, x); tot = mpmath.mpf(0)
        for g in gens:
            j, m, v = g['j'], g['m'], mpq(g['coef']); s = g['spec']; p = (3 + mpq(gamma) - j * mpq(delta)) / 2
            base = v * r2 ** m * mpmath.cos(2 * m * th) * (1 + r2) ** (p - m)
            if s[0] == 'mono': rad = (r2 / (1 + r2)) ** s[1]
            elif s[0] == 'leg': t = r2 / (1 + r2); rad = t ** s[1] * mpmath.legendre(s[2], 2 * t - 1)
            else:
                w, n, qp, R0 = s[1:]; tR = r2 / (R0 * R0 + r2); rad = tR ** w * (1 - tR) ** qp * mpmath.legendre(n, 2 * tR - 1)
            tot += base * rad
        return tot
    def dchi(x, y, nx, ny): return mpmath.diff(lambda u, v: chi(u, v), (x, y), (nx, ny))
    def F_direct(x, y):
        rho = -(dchi(x, y, 2, 1) + dchi(x, y, 0, 3)); u1 = -dchi(x, y, 1, 2); u2 = dchi(x, y, 2, 1)
        rx = -(dchi(x, y, 3, 1) + dchi(x, y, 1, 3)); ry = -(dchi(x, y, 2, 2) + dchi(x, y, 0, 4))
        return (cm * x + u1) * rx + (cm * y + u2) * ry - rho
    _cache = {}
    def eval_t(Dc, d, x, y):
        """Evaluate a degree-d tuple-key component at (x, y) (coefficients converted once per component)."""
        key = id(Dc)
        if key not in _cache:
            _cache[key] = [(ell, kind, n, [(mpq(a), N) for a, N in sc], [mpq(str(cf)) for cf in p.coeffs()]) for (ell, kind, n, sc), p in Dc.items()]
        r2 = x * x + y * y; t = r2 / (1 + r2); v = 1 - t; th = mpmath.atan2(y, x); tot = mpmath.mpf(0)
        for ell, kind, n, sc, cf in _cache[key]:
            pv = mpmath.mpf(0)
            for ck in reversed(cf): pv = pv * t + ck
            trig = mpmath.cos(n * th) if kind == 'c' else mpmath.sin(n * th)
            K = mpmath.mpf(1)
            for a, N in sc: K *= (1 + a * v) ** (-N)
            tot += v ** (ell * dm / 2) * pv * trig * K
        pre = mpmath.sqrt(r2) * v ** (d // 2) if d % 2 == 0 else v ** ((d - 1) // 2)
        return pre * tot
    if 'D' in which:
        print('--- D: point values of F and D F (tuple-key representation) against direct mpmath differentiation of chi')
        for (x, y) in ((mpmath.mpf(3) / 7, mpmath.mpf(-2) / 5), (mpmath.mpf(21), mpmath.mpf(-9)), (mpmath.mpf(0.3), mpmath.mpf(70))):
            Fr = eval_t(D[0, 0], 0, x, y); Fd = F_direct(x, y)
            Fx_r = eval_t(D[1, 1], 1, x, y); Fy_r = eval_t(D[1, 0], 1, x, y)
            Fx_d = mpmath.diff(lambda u: eval_t(D[0, 0], 0, u, y), x); Fy_d = mpmath.diff(lambda u: eval_t(D[0, 0], 0, x, u), y)
            Fxx_r = eval_t(D[2, 2], 2, x, y); Fxx_d = mpmath.diff(lambda u: eval_t(D[1, 1], 1, u, y), x)
            print(f'  ({mpmath.nstr(x,3)},{mpmath.nstr(y,3)}): F rep {mpmath.nstr(Fr, 18)} direct {mpmath.nstr(Fd, 18)} |diff| {mpmath.nstr(abs(Fr-Fd), 3)}; '
                  f'Fx rel {mpmath.nstr(abs(Fx_r-Fx_d)/abs(Fx_d), 3)} Fy rel {mpmath.nstr(abs(Fy_r-Fy_d)/abs(Fy_d), 3)} Fxx rel {mpmath.nstr(abs(Fxx_r-Fxx_d)/abs(Fxx_d), 3)}')
    if 'E' in which:
        print('--- E: G0 and rF with scales (exact R1 + R2 I0 route) against mpmath 2D quadrature of the point evaluator')
        tables = LN.ScaleTables(); t0 = time.time()
        rG0 = LN.norm_t(D, 0, delta, Q(0), 0, (), 56, 'G0', tables); rrF = LN.norm_t(D, 0, delta, Q(-1), 1, (), 56, 'rF', tables)
        rG1 = LN.norm_t(D, 1, delta, Q(0), 0, (), 56, 'G1', tables); rP2 = LN.norm_t(D, 2, delta, Q(-4, 5), 0, E.OMEGA, 56, 'P2', tables); print('  P2', rP2['status'], rP2.get('norm_lower_ball','')[:40], rP2.get('norm_upper_ball','')[:40])
        print(f"  norm_t: G0 {rG0['status']} {rG0.get('norm_lower_ball','')[:40]} rF {rrF['status']} {rrF.get('norm_lower_ball','')[:40]} G1 {rG1['status']} {rG1.get('norm_lower_ball','')[:40]} ({time.time()-t0:.0f}s)")
        pass  # 2D quadrature cross-check: certification/legqs_quadcheck.py (detached)

if 'B' in which:
    print('--- B: state 131 (no scales): residual and norms identical to e2norms (record C1-BASE-S131_e2norms.json)')
    c, A, src, can, meta = E.load_reference('source_copy/exact_refs/state131_exact.json') if Path('source_copy/exact_refs/state131_exact.json').exists() else (None,) * 5
    if c is None:
        import glob; cands = glob.glob('source_copy/**/*131*.json', recursive=True); print('state 131 candidates:', cands); c, A, src, can, meta = E.load_reference(cands[0])
    delta = 1 - 1 / c; t0 = time.time()
    D, fields = LN.residual_t(A, {}, c, 2, log=print)
    Dref, _ = E.residual_polynomials(A, c, 2, log=print)
    print('residual components identical (d <= 2):', all(LN.to_plain(D[k]) == Dref[k] for k in Dref), f'{time.time()-t0:.0f}s')
    rec = json.load(open('certification/results/C1-BASE-S131_e2norms.json'))
    for label, d, a, tp, ser in LN.STANDARD[:4]:
        r = LN.norm_t(D, d, delta, a, tp, ser, 56, label); ref = rec['norms'][label]
        print(f"  {label}: S identical {r.get('S_exact_rational') == ref.get('base_beta_sum')}; bounds identical {r.get('norm_lower') == ref.get('norm_lower') and r.get('norm_upper') == ref.get('norm_upper')}; {r.get('norm_lower_ball','')[:36]} ({r.get('elapsed_seconds',0):.0f}s)")
