"""Verifier (verifier), 2026-10-18 shift 6: independent far-field expansion of a formula-global shape to the order of the
lead's far2 (NOTES 18:19:06Z item 2). Written from the definitions and code/gen_shape.py only (no code of the lead or of the
numerics lane).
Physical r, delta = r^(k-1), eps = r^(-2). Terms are indexed (n, p) with exponent a(n, p) = k + n (k - 1) - 2 p, kept for
n (1 - k) + 2 p <= 2.5 (that is (0,0), (1,0), (2,0), (0,1), (3,0)).
Density: with u = 1 - q = (1 + rr^2)^(-(1-k)/2) = rr^(k-1) (1 + O(rr^-2)), chi^(m-1) = 1 - (m-1) r0^2 rr^-2, s^(p3/2) =
1 - (p3/2) rr^-2, (1 + rr^2)^((k-3)/2) = rr^(k-3) (1 + (k-3)/2 rr^-2):
  log rho = log Theta_0 + k log r + lam1 delta + lam2 delta^2 + lam3 delta^3 + lamh eps + O(delta eps),
  lam_j = (-1)^j d^j H/dq^j (q = 1) / j! L^(j(1-k)),  lamh = L^2 [(k-3)/2 - r0^2 sum_{m>1} (m-1) b_m(1) cos 2mt - (p3/2) T(1) v].
Velocity: each density term r^a A gives psi = r^(a+1) F, F'' + (a+1)^2 F = -(a cos t A - sin t A'), (sine series, even n;
no resonance since a+1 is not an even integer), U_r = -r^a F', U_t = (a+1) r^a F. Core multipoles enter at relative r^-4.
Residual R = c_l r d_r rho + U.grad rho - rho with c_l = 1/k; U^(n1,p1).grad rho^(n2,p2) is of order (n1+n2+1, p1+p2).
N_v = |rho| + |X.grad rho| + |U.grad rho|, each absolute value expanded with the sign of its leading coefficient.
R/N_v = q1 delta + q2 delta^2 + qh eps + q3 delta^3 + O(r^(-2.82)), by series division.
Usage: python3 far2_ver.py shape.npz [nt] [theta,theta,...] [out.json]
"""
import sys, json
import numpy as np
from scipy.interpolate import BSpline
from numpy.polynomial.chebyshev import chebval, chebder


def jets(d, t, nder=3):
    z = d['z']
    k = float(z[0]); coef = z[1:]; L = float(d['L'])
    deg, ang, sing = int(d['degree']), int(d['angular']), int(d['singular'])
    order, r0 = int(d['spline_order']), float(d['origin_radius'])
    knots = np.asarray(d['spline_knots'], float)
    p3 = 6 + 2 * k / (2 - k)
    Hq = [np.zeros_like(t) for _ in range(nder + 1)]           # d^j H / dq^j at q = 1 (rr -> infinity limits)
    eta = np.full_like(t, (k - 3) / 2)
    for m in range(ang + 1):
        sp = BSpline(knots, np.r_[0.0, coef[m * deg:(m + 1) * deg]], order, extrapolate=True)
        c2 = np.cos(2 * m * t)
        for j in range(nder + 1):
            Hq[j] += float(sp.derivative(j)(1.0) if j else sp(1.0)) * c2
        if m > 1 and r0 > 0:
            eta += -(m - 1) * r0 ** 2 * float(sp(1.0)) * c2
    v = np.abs(np.cos(t)) ** (p3 - 2) * np.sin(t) ** 2
    T1 = 0.0
    for j in range(sing):
        e = np.zeros(j + 1); e[j] = 1
        cj = coef[(ang + 1) * deg + j]
        T1 += cj * chebval(1.0, e)
        ej = e.copy()
        for i in range(nder + 1):
            Hq[i] += cj * chebval(1.0, ej) * 2 ** i * v
            ej = chebder(ej)
    eta += -(p3 / 2) * T1 * v
    T0 = L ** (3 - k) * np.cos(t) ** 2 * np.sin(t) * np.exp(Hq[0])
    lam = [None] + [(-1) ** j * Hq[j] / [1, 1, 2, 6][j] * L ** (j * (1 - k)) for j in (1, 2, 3)]
    return dict(k=k, L=L, r0=r0, p3=p3, T0=T0, lam=lam, lamh=L ** 2 * eta, h_eta=L ** 2 * eta)


def main(path, nt=2 ** 15, want=(1.56811, 1.56265, 1.54625, 0.81819)):
    d = np.load(path, allow_pickle=True)
    t = 2 * np.pi * np.arange(nt) / nt
    J = jets(d, t)
    k, L = J['k'], J['L']
    cl = 1 / k
    n = np.fft.rfftfreq(nt, 1.0 / nt)
    D = lambda f: np.fft.irfft(1j * n * np.fft.rfft(f), nt)
    l1, l2, l3 = J['lam'][1:]
    lh = J['lamh']
    T0 = J['T0']
    orders = [(0, 0), (1, 0), (2, 0), (0, 1), (3, 0)]
    a = {o: k + o[0] * (k - 1) - 2 * o[1] for o in orders}
    A = {(0, 0): T0, (1, 0): T0 * l1, (2, 0): T0 * (l2 + l1 ** 2 / 2), (0, 1): T0 * lh,
         (3, 0): T0 * (l3 + l1 * l2 + l1 ** 3 / 6)}
    dA = {o: D(A[o]) for o in orders}
    V = {}
    chk = {}
    for o in [(0, 0), (1, 0), (2, 0)]:
        g = a[o] * np.cos(t) * A[o] - np.sin(t) * dA[o]
        gh = np.fft.rfft(g)
        chk[str(o)] = float(np.abs(gh[1::2]).max() / np.abs(gh).max())   # parity: sine series in even n only
        Fh = gh / (n ** 2 - (a[o] + 1) ** 2)
        F = np.fft.irfft(Fh, nt)
        V[o] = (-np.fft.irfft(1j * n * Fh, nt), (a[o] + 1) * F)
    def add(x, y):
        return (x[0] + y[0], x[1] + y[1])
    # U.grad rho by order
    UG = {o: np.zeros(nt) for o in orders}
    for o1 in V:
        for o2 in orders:
            o = (o1[0] + o2[0] + 1, o1[1] + o2[1])
            if o in UG:
                UG[o] = UG[o] + a[o2] * V[o1][0] * A[o2] + V[o1][1] * dA[o2]
    R = {o: (cl * a[o] - 1) * A[o] + UG[o] for o in orders}
    s0 = np.sign(A[(0, 0)]); s1 = np.sign(k * A[(0, 0)]); s2 = np.sign(UG[(1, 0)])
    N = {o: s0 * A[o] + s1 * a[o] * A[o] + s2 * UG[o] for o in orders}
    N0, N1, N2 = N[(0, 0)], N[(1, 0)], N[(2, 0)]
    R1, R2, R3, Rh = R[(1, 0)], R[(2, 0)], R[(3, 0)], R[(0, 1)]
    q1 = R1 / N0
    q2 = R2 / N0 - R1 * N1 / N0 ** 2
    qh = Rh / N0
    q3 = R3 / N0 - (R2 * N1 + R1 * N2) / N0 ** 2 + R1 * N1 ** 2 / N0 ** 3
    out = dict(file=path, nt=nt, k=k, L=L, c_l=cl, parity=chk, R00_max=float(np.abs(R[(0, 0)] / T0)[np.abs(T0) > 1e-3 * np.abs(T0).max()].max()),
               rows=[])
    for tw in want:
        i = int(round(tw / (2 * np.pi) * nt))
        out['rows'].append(dict(theta=float(t[i]), q1=float(q1[i]), q2=float(q2[i]), qh=float(qh[i]), q3=float(q3[i]),
                                R1=float(R1[i] / A[(0, 0)][i]), R2=float(R2[i] / A[(0, 0)][i]), R3=float(R3[i] / A[(0, 0)][i]),
                                h=float(lh[i]), lam1=float(l1[i]), Theta1f_over=float(UG[(1, 0)][i] / ((cl - 1) * A[(0, 0)][i]))))
    return out, dict(t=t, q1=q1, q2=q2, qh=qh, q3=q3)


if __name__ == '__main__':
    nt = int(sys.argv[2]) if len(sys.argv) > 2 else 2 ** 15
    want = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else (1.56811, 1.56265, 1.54625, 0.81819)
    out, prof = main(sys.argv[1], nt, want)
    s = json.dumps(out, indent=1)
    print(s)
    if len(sys.argv) > 4:
        open(sys.argv[4], 'w').write(s)
        np.savez(sys.argv[4].replace('.json', '_prof.npz'), **prof)
