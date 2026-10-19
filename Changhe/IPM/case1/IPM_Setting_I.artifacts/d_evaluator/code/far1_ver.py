"""Verifier (verifier), 2026-10-18 shift 6: independent far-field first correction of a formula-global shape (G81 OPEN item,
lead NOTES 18:04:24Z item 2). Written from the definitions only (no code of the lead or numerics lane):
  rho -> r^k Theta_0(t) (1 + r^(k-1) Theta_1(t) + ...),  Theta_0 = L^(3-k) cos^2 t sin t exp(H_inf(t)),
  Theta_1 (stored) = -L^(1-k) dH/dq(q = 1, t)   (from 1 - q = (1 + rr^2)^(-(1-k)/2) ~ rr^(k-1); s, chi, the log term
  only give O(rr^-2)),
  psi_0 = r^(k+1) F(t), F'' + (k+1)^2 F = -g, g = k cos t Theta_0 - sin t Theta_0'  (homogeneous full-plane inverse of
  d_x(r^k Theta_0); F = sum_n F_n sin(n t), n even, F_n = G_n / (n^2 - (k+1)^2)),
  U_0 = r^k (V_r, V_t), V_r = -F', V_t = (k+1) F,
  forced: (c_l - 1) Theta_0 Theta_1 = k V_r Theta_0 + V_t Theta_0', on the y-axis Theta_1 -> -(k+2) V_r(pi/2)/(c_l - 1).
Then C(t) = (c_l - 1)(Theta_1 forced - Theta_1 stored) and R/N_v -> C r^(k-1)/(1+k) (N_v ~ (1+k)|rho| at leading order).
Theta_0' and the sine coefficients are computed spectrally on the full circle (FFT, nt points), with the derivative of
the |cos t|^(p3-2) factor taken analytically as a cross-check (two routes).
Usage: python3 far1_ver.py shape.npz [nt] [out.json]
"""
import sys, json
import numpy as np
from scipy.interpolate import BSpline
from numpy.polynomial.chebyshev import chebval, chebder


def far_profiles(d, t):
    z = d['z']
    k = float(z[0]); coef = z[1:]; L = float(d['L'])
    deg, ang, sing = int(d['degree']), int(d['angular']), int(d['singular'])
    order = int(d['spline_order'])
    knots = np.asarray(d['spline_knots'], float)
    p3 = 6 + 2 * k / (2 - k)
    Hinf = np.zeros_like(t); dHq = np.zeros_like(t); dHt = np.zeros_like(t)
    for m in range(ang + 1):
        c = np.r_[0.0, coef[m * deg:(m + 1) * deg]]            # first B-spline omitted (coefficient 0)
        sp = BSpline(knots, c, order, extrapolate=True)
        b1, db1 = float(sp(1.0)), float(sp.derivative()(1.0))
        Hinf += b1 * np.cos(2 * m * t)
        dHt += -2 * m * b1 * np.sin(2 * m * t)
        dHq += db1 * np.cos(2 * m * t)
    ac, st, ct = np.abs(np.cos(t)), np.sin(t), np.cos(t)
    angs = ac ** (p3 - 2) * st ** 2
    # d/dt of |cos t|^(p3-2) sin^2 t = -(p3-2)|cos|^(p3-3) sgn(cos) sin^3 + 2 |cos|^(p3-2) sin cos
    dangs = -(p3 - 2) * ac ** (p3 - 3) * np.sign(ct) * st ** 3 + 2 * ac ** (p3 - 2) * st * ct
    for j in range(sing):
        e = np.zeros(j + 1); e[j] = 1
        cj = coef[(ang + 1) * deg + j]
        Tj1 = chebval(1.0, e)                                 # T_j(1) = 1
        dTj1 = chebval(1.0, chebder(e)) * 2                    # d/dq T_j(2q - 1) at q = 1 (= 2 j^2)
        Hinf += cj * Tj1 * angs                                # s^(p3/2) -> 1
        dHt += cj * Tj1 * dangs
        dHq += cj * dTj1 * angs
    base = ct ** 2 * st
    dbase = -2 * ct * st ** 2 + ct ** 3
    T0 = L ** (3 - k) * base * np.exp(Hinf)
    dT0 = L ** (3 - k) * np.exp(Hinf) * (dbase + base * dHt)
    T1s = -L ** (1 - k) * dHq
    return dict(k=k, L=L, cl=1 / k, p3=p3, T0=T0, dT0=dT0, T1s=T1s, Hinf=Hinf)


def main(path, nt=2 ** 15):
    d = np.load(path, allow_pickle=True)
    t = 2 * np.pi * np.arange(nt) / nt
    P = far_profiles(d, t)
    k, cl, T0 = P['k'], P['cl'], P['T0']
    n = np.fft.rfftfreq(nt, 1.0 / nt)
    T0h = np.fft.rfft(T0)
    dT0_spec = np.fft.irfft(1j * n * T0h, nt)
    g = k * np.cos(t) * T0 - np.sin(t) * P['dT0']
    gh = np.fft.rfft(g)
    # parity checks: T0 odd sine series in odd n; g sine series in even n
    par = dict(T0_even_n=float(np.abs(T0h[0::2]).max() / np.abs(T0h).max()),
               T0_cos=float(np.abs(T0h.real).max() / np.abs(T0h).max()),
               g_odd_n=float(np.abs(gh[1::2]).max() / np.abs(gh).max()),
               dT0_routes=float(np.abs(dT0_spec - P['dT0']).max() / np.abs(P['dT0']).max()))
    den = n ** 2 - (k + 1) ** 2
    Fh = gh / den                                           # F'' + (k+1)^2 F = -g  ->  (n^2 - (k+1)^2) F_n = g_n
    F = np.fft.irfft(Fh, nt)
    dF = np.fft.irfft(1j * n * Fh, nt)
    # check the ODE residual spectrally
    ddF = np.fft.irfft(-n ** 2 * Fh, nt)
    ode = float(np.abs(ddF + (k + 1) ** 2 * F + g).max() / np.abs(g).max())
    Vr, Vt = -dF, (k + 1) * F
    with np.errstate(divide='ignore', invalid='ignore'):
        T1f = (k * Vr * T0 + Vt * P['dT0']) / ((cl - 1) * T0)
    i_half = nt // 4                                        # t = pi/2
    Vr_axis = float(Vr[i_half])
    T1f_axis = -(k + 2) * Vr_axis / (cl - 1)
    T1s_axis = float(P['T1s'][i_half])
    C = (cl - 1) * (T1f - P['T1s'])
    C_axis = (cl - 1) * (T1f_axis - T1s_axis)
    want = [0.1001, 0.3001, 0.6, 0.818, 1.0, 1.2, 1.3999, 1.5, 1.5501, 1.565]
    tab = []
    for tw in want:
        i = int(round(tw / (2 * np.pi) * nt))
        # evaluate exactly at tw by trigonometric interpolation of the smooth pieces
        tab.append(dict(theta=float(t[i]), T1_forced=float(T1f[i]), T1_stored=float(P['T1s'][i]), C=float(C[i]),
                        C_over_1pk=float(C[i] / (1 + k))))
    sel = (t > 0.05) & (t < 1.4)
    out = dict(file=path, nt=nt, k=k, c_l=cl, parity=par, ode_rel=ode, Vr_axis=Vr_axis, T1_forced_axis=T1f_axis,
               T1_stored_axis=T1s_axis, C_axis=C_axis, C_axis_over_1pk=C_axis / (1 + k),
               max_abs_diff_005_14=float(np.abs(T1f - P['T1s'])[sel].max()),
               argmax_diff_005_14=float(t[sel][np.argmax(np.abs(T1f - P['T1s'])[sel])]), table=tab)
    return out, dict(t=t, T0=T0, T1f=T1f, T1s=P['T1s'], C=C, Vr=Vr, Vt=Vt)


if __name__ == '__main__':
    nt = int(sys.argv[2]) if len(sys.argv) > 2 else 2 ** 15
    out, prof = main(sys.argv[1], nt)
    s = json.dumps(out, indent=1)
    print(s)
    if len(sys.argv) > 3:
        open(sys.argv[3], 'w').write(s)
        np.savez(sys.argv[3].replace('.json', '_prof.npz'), **prof)
