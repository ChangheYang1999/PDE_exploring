"""Second arithmetic path for the e2norms records (lane c1-n3).

1. Regenerates the compactified polynomials from the exact source and compares them with the stored record.
2. Recomputes every finite norm with the variable u = 1 - t (direct monomial antiderivatives, no beta recursion,
   all ordered cross terms explicitly) at 640 bits and compares the exact rational sums with the record.
3. Compares the residual and its derivatives at rational Cartesian points with a direct Taylor-jet evaluation of
   the potential (the jet evaluator follows A2/certificates/P12_residual_norms/audit_norms.py, direct_chi/direct_F,
   which is independent of the compactified representation).
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb
from datetime import datetime, timezone
import sys, json, time, hashlib
from flint import arb, acb, fmpq, fmpq_poly, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E
U = fmpq_poly([0, 1]); T = 1 - U

def compose(p, x):
    out = fmpq_poly([])
    for a in reversed(p.coeffs()): out = out * x + a
    return out

def aq(x): return E.aq(x)

def poly_integral_u(p, exponent):
    result = fmpq(0)
    for k, coef in enumerate(p.coeffs()):
        if coef:
            assert exponent + k > -1, ('nonintegrable exact u monomial', exponent, k)
            result += coef / E.fq(exponent + k + 1)
    return result

def integrate(D, d, delta, a_shift, t_power, series, N):
    group = {}; base = Q(d - 3) + Q(a_shift); bad = False
    for nx in range(d + 1):
        harmonics = {}
        for (ell, kind, n), p in D[d, nx].items():
            pu = compose(p, T)
            first = next(k for k, a in enumerate(pu.coeffs()) if a)
            exponent = base + ell * delta + 2 * first
            if exponent <= -1: bad = True
            harmonics.setdefault((kind, n), []).append((ell, pu))
        for (kind, n), entries in harmonics.items():
            factor = comb(d, nx) * (2 if kind == 'c' and n == 0 else 1)
            for ell, p in entries:
                for ell2, q in entries:
                    group[ell + ell2] = group.get(ell + ell2, fmpq_poly([])) + factor * p * q
    if bad: return None
    tp = (1 if d % 2 else T) * (T ** t_power)
    s = fmpq(0); ss = fmpq(0); g = fmpq_poly([1]); eps = fmpq(0)
    for cc, alpha in series:
        cc = Q(cc); alpha = Q(alpha); mid = 1 + cc / 2; z0 = cc / (2 + cc)
        zu = fmpq_poly([E.fq(cc / 2 / mid), E.fq(-cc / mid)])   # z = (cc t - cc/2)/mid with t = 1-u
        gg = fmpq_poly([])
        for n in range(N + 1):
            coeff = fmpq(1)
            for j in range(n): coeff *= E.fq(alpha - j) / (j + 1)
            gg += coeff * zu ** n
        nxt = fmpq(1)
        for j in range(N + 1): nxt *= E.fq(alpha - j) / (j + 1)
        eps += abs(nxt) * E.fq(z0 ** (N + 1) / (1 - z0)); g = g * gg
    for power, p in group.items():
        exp = base + power * delta / 2
        s += poly_integral_u(p * tp, exp)
        if series: ss += poly_integral_u(p * tp * g, exp)
    if not series: ss = s
    return s, ss, eps

ORDER = 7
INDICES = [(i, j) for i in range(ORDER + 1) for j in range(ORDER + 1 - i)]
def pmul(a, b, order=ORDER):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            if i + j + k + l <= order:
                key = i + k, j + l; out[key] = out.get(key, arb(0)) + x * y
    return out

def direct_chi(A, c, x, y):
    q = x * x + y * y; oq = 1 + q; gamma = 1 / aq(c); v = q / oq
    dq = {(1, 0): 2 * x, (0, 1): 2 * y, (2, 0): arb(1), (0, 2): arb(1)}
    powers = [{(0, 0): arb(1)}]
    for _ in range(ORDER): powers.append(pmul(powers[-1], dq))
    mmax = max(m for j, m, k in A); zz = acb(x, y); zp = [acb(1)]
    for _ in range(2 * mmax): zp.append(zp[-1] * zz)
    hj = {}
    for m in range(mmax + 1):
        n = 2 * m; poly = {}
        for i, j in INDICES:
            if i + j <= n:
                z = zp[n - i - j]; val = (z.real, -z.imag, -z.real, z.imag)[j % 4]
                poly[i, j] = arb(factorial(n) // factorial(n - i - j)) * val / (factorial(i) * factorial(j))
        hj[m] = poly
    groups = {}
    for (j, m, k), a in A.items(): groups.setdefault((j, m), []).append((k - m, a))
    chi = {key: arb(0) for key in INDICES}
    for (j, m), terms in groups.items():
        p = (3 + gamma - j * (1 - gamma)) / 2; pref = oq ** (p - m); rad = [arb(0) for _ in range(ORDER + 1)]
        for l, coeff in terms:
            factor = aq(coeff) * pref * v ** l; beta = p - m - l
            binom_q = [arb(comb(l, k)) / q ** k if k <= l else arb(0) for k in range(ORDER + 1)]
            binom_o = [arb(1)]
            for k in range(1, ORDER + 1): binom_o.append(binom_o[-1] * (beta - k + 1) / (k * oq))
            for k in range(ORDER + 1): rad[k] += factor * sum((binom_q[a] * binom_o[k - a] for a in range(k + 1)), arb(0))
        rp = {key: arb(0) for key in INDICES}
        for k, val in enumerate(rad):
            for key, co in powers[k].items(): rp[key] += val * co
        prod = pmul(hj[m], rp)
        for key, val in prod.items(): chi[key] += val
    return {key: val * factorial(key[0]) * factorial(key[1]) for key, val in chi.items()}

def direct_F(A, c, x, y):
    chi = direct_chi(A, c, x, y); rho = {}; u = {0: {}, 1: {}}
    for i in range(5):
        for j in range(5 - i): rho[i, j] = (-chi[i + 2, j + 1] - chi[i, j + 3]) / (factorial(i) * factorial(j))
    for i in range(4):
        for j in range(4 - i):
            u[0][i, j] = -chi[i + 1, j + 2] / (factorial(i) * factorial(j))
            u[1][i, j] = chi[i + 2, j + 1] / (factorial(i) * factorial(j))
    u[0][0, 0] += aq(c) * x; u[1][0, 0] += aq(c) * y
    u[0][1, 0] += aq(c); u[1][0, 1] += aq(c)
    rx = {(i, j): (i + 1) * rho[i + 1, j] for i in range(4) for j in range(4 - i)}
    ry = {(i, j): (j + 1) * rho[i, j + 1] for i in range(4) for j in range(4 - i)}
    a = pmul(u[0], rx, 3); b = pmul(u[1], ry, 3)
    return {(i, j): (a.get((i, j), arb(0)) + b.get((i, j), arb(0)) - rho[i, j]) * factorial(i) * factorial(j)
            for i in range(4) for j in range(4 - i)}

def polar_eval(D, delta, xq, yq):
    r2 = xq * xq + yq * yq; tq = r2 / (1 + r2)
    t = aq(tq); r = aq(r2).sqrt(); x = aq(xq); y = aq(yq); w = (1 - t) ** (aq(delta) / 2)
    maxn = max(n for fields in D.values() for ell, kind, n in fields)
    co = [arb(1), x / r]; si = [arb(0), y / r]
    for n in range(2, maxn + 1): co.append(2 * co[1] * co[-1] - co[-2]); si.append(2 * co[1] * si[-1] - si[-2])
    values = {}
    for (d, nx), fields in D.items():
        val = arb(0)
        for (ell, kind, n), p in fields.items():
            pp = arb(0)
            for a in reversed(p.coeffs()): pp = pp * t + aq(a)
            val += w ** ell * pp * (co[n] if kind == 'c' else si[n])
        fac = (1 - t) ** aq(Q(d - 1, 2))
        if d % 2 == 0: fac *= t.sqrt()
        values[nx, d - nx] = val * fac
    return values

SPECS = {'G0': (0, Q(0), 0, ()), 'rF': (0, Q(-1), 1, ()), 'G1': (1, Q(0), 0, ()), 'P2': (2, Q(-4, 5), 0, E.OMEGA),
         'Q3': (3, Q(-4, 5), 0, E.OMEGA), 'Pw1': (1, Q(1, 5), 0, ()), 'D2': (2, Q(0), 0, ()), 'rD2': (2, Q(-1), 1, ())}

def run(name, resdir, source_path, points=None):
    ctx.prec = 640; start = time.monotonic(); resdir = Path(resdir)
    recfile = resdir / f'{name}_e2norms.json'; rec = json.loads(recfile.read_text())
    c, A, src_sha, can_sha, meta = E.load_reference(source_path)
    assert rec['canonical_sha256'] == can_sha and rec['source_sha256'] == src_sha
    delta = 1 - 1 / c
    log = lambda *a: print(*a, flush=True)
    D, fields = E.residual_polynomials(A, c, 3, log=lambda *a: None)
    fpoly = resdir / f'{name}_Fpoly.json'
    if fpoly.exists():
        raw = json.loads(fpoly.read_text()); assert raw['canonical_sha256'] == can_sha
        F_rec = {(r['ell'], r['kind'], r['mode']): fmpq_poly([fmpq(v) for v in r['coeff']]) for r in raw['polynomials']['0,0']}
        assert F_rec == D[0, 0], 'stored F polynomials differ from the regenerated ones'
        log(f'{name}: stored F polynomials identical to regenerated ones')
    log(f'{name}: polynomials regenerated ({time.monotonic()-start:.1f}s)')
    vals = {}
    for label, row in rec['norms'].items():
        d, a, tp, ser = SPECS[label]
        z = integrate(D, d, delta, a, tp, ser, rec['series_degree'])
        if z is None:
            assert row['status'] == 'INFINITE', label; vals[label] = {'status': 'INFINITE', 'agrees': True}
        else:
            S, Tt, eps = z
            ok = str(S) == row['base_beta_sum'] and str(Tt) == row['weighted_beta_sum']
            if ser: ok = ok and str(eps) == row['series'][0]['eps']
            pref = arb(1)
            for cc, alpha in ser: pref *= aq(Q(1) + Q(cc) / 2) ** aq(alpha)
            lo = arb.pi() / 2 * pref * aq(Tt - eps * S); hi = arb.pi() / 2 * pref * aq(Tt + eps * S)
            vals[label] = {'status': 'FINITE', 'agrees': ok, 'lower': str(lo.sqrt().lower()), 'upper': str(hi.sqrt().upper())}
            assert ok, ('exact sums differ', label)
        log(f'{name}: {label} u-integral {vals[label]["status"]} agrees={vals[label]["agrees"]} {vals[label].get("lower","")} {vals[label].get("upper","")}')
    checks = []
    for xs, ys in (points or [('0', '1/10'), ('1', '0'), ('1/2', '1/2'), ('1', '2'), ('3', '1'), ('60', '80'), ('0', '1000')]):
        xq, yq = Q(xs), Q(ys); v = polar_eval(D, delta, xq, yq); direct = direct_F(A, c, aq(xq), aq(yq))
        ok = {f'{i},{j}': bool(v[i, j].is_finite() and q.is_finite() and v[i, j].overlaps(q)) for (i, j), q in direct.items()}
        assert all(ok.values()), (name, xs, ys, [(k, str(v[tuple(map(int, k.split(',')))]), str(direct[tuple(map(int, k.split(',')))])) for k, a in ok.items() if not a])
        checks.append({'point': [xs, ys], 'components': ok, 'F': v[0, 0].str(30)}); log(f'{name}: Cartesian jet check ({xs},{ys}) PASS, F = {v[0,0].str(20)}')
    out = {'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'name': name, 'verdict': 'CONFIRMED', 'precision_bits': ctx.prec,
           'canonical_sha256': can_sha, 'source_sha256': src_sha,
           'record_sha256': hashlib.sha256(recfile.read_bytes()).hexdigest(), 'norms': vals, 'cartesian_checks': checks,
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'elapsed_seconds': time.monotonic() - start}
    (resdir / f'{name}_audit.json').write_text(json.dumps(out, indent=1) + '\n')
    log(f'AUDIT COMPLETE {name} {out["elapsed_seconds"]:.1f}s')
    return out

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3])
