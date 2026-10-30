"""Independent checks for T4-234 (forced nonintegrable tail profiles).

Exact rational Fourier arithmetic builds Psi_j and Theta_j from (1),(4) of
c1-t4 research/triangular_tail_equations/PROOF.md; mpmath Cartesian
differentiation (no polar derivative formulas) then checks the Poisson
equations, the velocity formula (5), the residual expansion (8) and the
potential endpoint formulas. Read-only inputs: none.
"""
from fractions import Fraction as Fr
import time
import mpmath as mp

t0 = time.time()
mp.mp.dps = 40
ok = True


def report(name, val, tol):
    global ok
    good = abs(val) <= tol
    ok = ok and good
    print(f"{name}: {mp.nstr(val, 5)} (tol {tol}) {'PASS' if good else 'FAIL'}")


def add(d, k, v):
    if k == 0:
        return
    if k < 0:
        k, v = -k, -v
    d[k] = d.get(k, Fr(0)) + v


def psi_from(theta, e):
    # rhs = -e cos(t) Theta + sin(t) Theta'
    rhs = {}
    for n, b in theta.items():
        add(rhs, n + 1, -e * b / 2)
        add(rhs, n - 1, -e * b / 2)
        add(rhs, n + 1, n * b / 2)
        add(rhs, n - 1, -n * b / 2)
    out = {}
    for m, v in rhs.items():
        assert m % 2 == 0
        if v != 0:
            out[m] = v / ((e + 1) ** 2 - m * m)
    return out


def bterm(psi_l, theta_m, el, em):
    # B = -e_m Psi_l' Theta_m + (e_l+1) Psi_l Theta_m'
    out = {}
    for k, p in psi_l.items():
        for n, b in theta_m.items():
            # Psi' Theta: k p cos(k t) * b sin(n t) = k p b [sin(n+k)+sin(n-k)]/2
            add(out, n + k, -em * k * p * b / 2)
            add(out, n - k, -em * k * p * b / 2)
            # Psi Theta': p sin(k t) * n b cos(n t) = n p b [sin(k+n)+sin(k-n)]/2
            add(out, k + n, (el + 1) * n * p * b / 2)
            add(out, k - n, (el + 1) * n * p * b / 2)
    return {k: v for k, v in out.items() if v != 0}


def tails(c, theta0):
    delta = 1 - 1 / c
    N = 0
    while 1 - (N + 1) * delta >= -1:
        N += 1
    e = [1 - (j + 1) * delta for j in range(2 * N)]
    th = [dict(theta0)]
    ps = [psi_from(th[0], e[0])]
    for j in range(1, N):
        s = {}
        for l in range(j):
            m = j - 1 - l
            for k, v in bterm(ps[l], th[m], e[l], e[m]).items():
                add(s, k, v)
        tj = {k: v / (j * (c - 1)) for k, v in s.items() if v != 0}
        th.append(tj)
        ps.append(psi_from(tj, e[j]))
    return N, e, th, ps


def sser(d, t):
    return mp.fsum(mp.mpf(v.numerator) / v.denominator * mp.sin(k * t) for k, v in d.items())


def cser_d(d, t):
    return mp.fsum(mp.mpf(v.numerator) / v.denominator * k * mp.cos(k * t) for k, v in d.items())


def fr(x):
    return mp.mpf(x.numerator) / x.denominator


theta0 = {1: Fr(1), 3: Fr(-2, 7), 5: Fr(1, 9)}
c007 = Fr(4076476460239181, 2 ** 51)
for label, c in (("c=9/5", Fr(9, 5)), ("c=c_007", c007)):
    N, e, th, ps = tails(c, theta0)
    print(f"{label}: N={N}, e_j+1 =", [float(e[j] + 1) for j in range(N)],
          "nonzero harmonics", [len(t) for t in th], "max", [max(t) for t in th])
    assert all(0 <= e[j] + 1 < 2 for j in range(N)) and e[N] < -1
    # exact identities c e_j - 1 = -j(c-1), e_l+e_m-1 = e_(l+m+1)
    assert all(c * e[j] - 1 == -j * (c - 1) for j in range(2 * N))
    assert all(e[l] + e[m] - 1 == e[l + m + 1] for l in range(N) for m in range(N))
    # dilation weights: Theta_0 -> z Theta_0 gives Theta_j -> z^(j+1) Theta_j
    z = Fr(5, 3)
    _, _, thz, _ = tails(c, {k: z * v for k, v in theta0.items()})
    assert all(thz[j] == {k: z ** (j + 1) * v for k, v in th[j].items()} for j in range(N))
    print(f"{label}: exact exponent identities and dilation weights z^(j+1): PASS")

    E = [fr(x) for x in e]
    cc = fr(c)

    def R(x, y, upto=N, th=th):
        r = mp.hypot(x, y)
        t = mp.atan2(y, x)
        return mp.fsum(r ** E[j] * sser(th[j], t) for j in range(upto))

    def psi(x, y, j):
        r = mp.hypot(x, y)
        t = mp.atan2(y, x)
        return r ** (E[j] + 1) * sser(ps[j], t)

    pts = [(mp.mpf('0.7'), mp.mpf('1.3')), (mp.mpf('-2.1'), mp.mpf('0.4')), (mp.mpf('3.3'), mp.mpf('-5.2'))]
    worst_p = worst_u = worst_r = mp.mpf(0)
    for (x0, y0) in pts:
        r0 = mp.hypot(x0, y0)
        t0_ = mp.atan2(y0, x0)
        for j in range(N):
            f = lambda x, y, j=j: psi(x, y, j)
            g = lambda x, y, j=j: r ** 0 if False else mp.hypot(x, y) ** E[j] * sser(th[j], mp.atan2(y, x))
            lap = mp.diff(f, (x0, y0), (2, 0)) + mp.diff(f, (x0, y0), (0, 2))
            dx = mp.diff(g, (x0, y0), (1, 0))
            worst_p = max(worst_p, abs(lap + dx) / r0 ** (E[j] - 1))
            # velocity formula (5): u = r^e[-Psi' e_r + (e+1) Psi e_theta]
            u1 = -mp.diff(f, (x0, y0), (0, 1))
            u2 = mp.diff(f, (x0, y0), (1, 0))
            P, dP = sser(ps[j], t0_), cser_d(ps[j], t0_)
            v1 = r0 ** E[j] * (-dP * mp.cos(t0_) - (E[j] + 1) * P * mp.sin(t0_))
            v2 = r0 ** E[j] * (-dP * mp.sin(t0_) + (E[j] + 1) * P * mp.cos(t0_))
            worst_u = max(worst_u, (abs(u1 - v1) + abs(u2 - v2)) / r0 ** E[j])
        # residual expansion (8) without cutoff: (cX+u).grad R - R = sum_(k>=N) r^e_k sum B
        U1 = mp.fsum(-mp.diff(lambda x, y, j=j: psi(x, y, j), (x0, y0), (0, 1)) for j in range(N))
        U2 = mp.fsum(mp.diff(lambda x, y, j=j: psi(x, y, j), (x0, y0), (1, 0)) for j in range(N))
        Rx = mp.diff(R, (x0, y0), (1, 0))
        Ry = mp.diff(R, (x0, y0), (0, 1))
        res = (cc * x0 + U1) * Rx + (cc * y0 + U2) * Ry - R(x0, y0)
        pred = mp.mpf(0)
        for l in range(N):
            for m in range(N):
                if l + m + 1 >= N:
                    pred += r0 ** E[l + m + 1] * sser(bterm(ps[l], th[m], e[l], e[m]), t0_)
        worst_r = max(worst_r, abs(res - pred) / (1 + abs(res)))
    report(f"{label}: Poisson (1) max relative defect", worst_p, 1e-25)
    report(f"{label}: velocity (5) max relative defect", worst_u, 1e-25)
    report(f"{label}: residual (8) with E_1..E_(N-1)=0, max relative defect", worst_r, 1e-25)
    # an incompatible Theta_1: residual = sum_(k>=1) r^(e_k) E_k exactly, with E_1 = -(c-1)*perturbation
    th_bad = [dict(t) for t in th]
    add(th_bad[1], 3, Fr(1, 10))
    psb = [psi_from(t, e[j]) for j, t in enumerate(th_bad)]
    Ek = []
    for k in range(1, 2 * N):
        s_ = {}
        for l in range(N):
            m = k - 1 - l
            if 0 <= m < N:
                for kk, v in bterm(psb[l], th_bad[m], e[l], e[m]).items():
                    add(s_, kk, v)
        if k < N:
            for kk, v in th_bad[k].items():
                add(s_, kk, -k * (c - 1) * v)
        Ek.append({kk: v for kk, v in s_.items() if v != 0})
    assert Ek[0] == {3: -(c - 1) / 10}
    Rb = lambda x, y: R(x, y, N, th_bad)
    def psib(x, y, j):
        return mp.hypot(x, y) ** (E[j] + 1) * sser(psb[j], mp.atan2(y, x))
    for (x0, y0) in ((mp.mpf(30), mp.mpf(41)), (mp.mpf('3e7'), mp.mpf('4.1e7'))):
        r0, t0_ = mp.hypot(x0, y0), mp.atan2(y0, x0)
        U1 = mp.fsum(-mp.diff(lambda x, y, j=j: psib(x, y, j), (x0, y0), (0, 1)) for j in range(N))
        U2 = mp.fsum(mp.diff(lambda x, y, j=j: psib(x, y, j), (x0, y0), (1, 0)) for j in range(N))
        res = ((cc * x0 + U1) * mp.diff(Rb, (x0, y0), (1, 0)) + (cc * y0 + U2) * mp.diff(Rb, (x0, y0), (0, 1))
               - Rb(x0, y0))
        pred = mp.fsum(r0 ** E[k] * sser(Ek[k - 1], t0_) for k in range(1, 2 * N))
        lead = r0 ** E[1] * sser(Ek[0], t0_)
        report(f"{label}: incompatible Theta_1, residual identity at r={mp.nstr(r0, 3)}",
               abs(res - pred) / abs(res), 1e-25)
        print(f"    residual/(r^e1 E1) = {mp.nstr(res / lead, 8)}")

# potential endpoint formulas: P = r^d cos(n t), rho = -d_y Lap P, psi = d_x d_y P
dps_ok = mp.mpf(0)
c = c007
for j in range(4):
    d = fr(1 - (j + 1) * (1 - 1 / c)) + 3
    for n in (0, 2, 4, 6):
        Pf = lambda x, y, n=n, d=d: mp.hypot(x, y) ** d * mp.cos(n * mp.atan2(y, x))
        for (x0, y0) in ((mp.mpf('1.1'), mp.mpf('0.6')), (mp.mpf('-0.8'), mp.mpf('2.3'))):
            r0, t = mp.hypot(x0, y0), mp.atan2(y0, x0)
            rho = -(mp.diff(Pf, (x0, y0), (2, 1)) + mp.diff(Pf, (x0, y0), (0, 3)))
            ps_ = mp.diff(Pf, (x0, y0), (1, 1))
            rho_f = r0 ** (d - 3) * (-(d * d - n * n) * (d - 2 - n) / 2 * mp.sin((n + 1) * t)
                                     + (d * d - n * n) * (d - 2 + n) / 2 * mp.sin((n - 1) * t))
            ps_f = r0 ** (d - 2) * ((d - n) * (d - n - 2) / 4 * mp.sin((n + 2) * t)
                                    - (d + n) * (d + n - 2) / 4 * mp.sin((n - 2) * t))
            dps_ok = max(dps_ok, abs(rho - rho_f) / r0 ** (d - 3), abs(ps_ - ps_f) / r0 ** (d - 2))
report("potential endpoint formulas (rho, psi), c_007, j=0..3, n=0,2,4,6", dps_ok, 1e-20)
print(f"runtime {time.time() - t0:.1f} s")
print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
