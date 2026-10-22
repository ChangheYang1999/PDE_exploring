#!/usr/bin/env python3
"""Dynamic rescaling for 2D Boussinesq, A1 parity (Theta even in x, odd in y; Omega odd-odd), whole plane.

Physical: omega_t + u.grad omega = theta_x, theta_t + u.grad theta = 0, u = (-psi_y, psi_x), -Lap psi = omega.
Rescaled: omega = C_w Om(x/C_l, tau), theta = C_l C_w^2 Th(x/C_l, tau), dtau/dt = C_w, c_l = (C_l)_tau/C_l,
c_w = (C_w)_tau/C_w:
    Om_tau + (-c_l X + U).grad Om = -c_w Om + Th_x
    Th_tau + (-c_l X + U).grad Th = -(c_l + 2 c_w) Th
Steady state = profile (P) with beta = -c_l/c_w after amplitude scaling (c -> -2).
Normalisation: c_w = -c/2 (c = Psi_xy(0)) keeps a0 = Th_y(0) exactly constant; c_l = c_w/2 - b1/g keeps
g = Om_xy(0) constant (b1 = Th_xxy(0)/2).

Grid: s = log r uniform on [smin, smax], phi cell-centred on (0, pi/2). Hat variables
    Oh = Om / r^2 = sum_m a_m(s) sin(2 m phi),   Hh = Th / r = sum_m b_m(s) sin((2m-1) phi).
Inverse: modal Green formula psi_m = (1/(4m)) int exp(-2m|s-s'|) exp(4 s') a_m(s') ds' (+ tails).
s-derivatives: 3rd-order upwind-biased; phi-derivatives: spectral (collocation matrices); RK4; exponential filter.

usage: python3 dr.py out_prefix T_end [smin smax ds Nphi] [restart.npz]
"""
import sys, time
import numpy as np

out = sys.argv[1]
T_end = float(sys.argv[2])
smin = float(sys.argv[3]) if len(sys.argv) > 3 else -6.0
smax = float(sys.argv[4]) if len(sys.argv) > 4 else 16.0
ds = float(sys.argv[5]) if len(sys.argv) > 5 else 0.04
Nph = int(sys.argv[6]) if len(sys.argv) > 6 else 64
restart = sys.argv[7] if len(sys.argv) > 7 else None

Ns = int(round((smax - smin) / ds)) + 1
s = smin + ds * np.arange(Ns)
dph = 0.5 * np.pi / Nph
ph = (np.arange(Nph) + 0.5) * dph
m = np.arange(1, Nph + 1)
S = np.sin(2 * np.outer(ph, m)); Sinv = np.linalg.inv(S); C2 = np.cos(2 * np.outer(ph, m))
T = np.sin(np.outer(ph, 2 * m - 1)); Tinv = np.linalg.inv(T); Tc = np.cos(np.outer(ph, 2 * m - 1))
sig = np.exp(-36.0 * (m / Nph) ** 36)
cph, sph = np.cos(ph), np.sin(ph)
es = np.exp(s)[:, None]
e2s = np.exp(2 * s)[:, None]
em2s = np.exp(-2 * s)[:, None]


def to_modes_O(F):  # F (Ns, Nph) -> a (Ns, Nph)
    return F @ Sinv.T


def to_modes_T(F):
    return F @ Tinv.T


def Jk(lam):
    """J0, J1, J2 = int_0^1 e^{lam t} t^k dt, vectorised."""
    lam = np.asarray(lam, float)
    J = np.empty((3,) + lam.shape)
    small = np.abs(lam) < 2e-2
    l = np.where(small, 1.0, lam)
    el = np.exp(l)
    J[0] = (el - 1) / l
    J[1] = (el * (l - 1) + 1) / l ** 2
    J[2] = (el * (l * l - 2 * l + 2) - 2) / l ** 3
    if small.any():
        ls = lam[small]
        for k in range(3):
            acc = np.zeros_like(ls); term = np.ones_like(ls)
            for i in range(12):
                acc += term / (i + k + 1)
                term = term * ls / (i + 1)
            J[k][small] = acc
    return J


# quadrature weights for the left (L) and right (R) recursions, per mode
JL = Jk((2 * m + 4) * ds)  # t-dependence exp((2m+4) ds t) times exp(-2m ds)
JR = Jk((4 - 2 * m) * ds)
decay = np.exp(-2 * m * ds)


def cell_ints(a, J):
    """int_0^1 e^{lam t} p(t) dt with p the quadratic through (j-1, j, j+1) (t=-1,0,1); at j=0 through (0,1,2).
    a: (Ns, M). returns (Ns-1, M) for cells [j, j+1]."""
    I = np.empty((Ns - 1, a.shape[1]))
    aj, ap, am = a[1:-1], a[2:], a[:-2]
    I[1:] = J[0] * aj + J[1] * (ap - am) / 2 + J[2] * (ap - 2 * aj + am) / 2
    # cell 0: quadratic through t=0,1,2 on points 0,1,2: p(t) = a0 + t(-3a0+4a1-a2)/2 + t^2 (a0-2a1+a2)/2
    a0, a1, a2 = a[0], a[1], a[2]
    I[0] = J[0] * a0 + J[1] * (-3 * a0 + 4 * a1 - a2) / 2 + J[2] * (a0 - 2 * a1 + a2) / 2
    return I


def velocity(Oh, beta_e):
    """returns A = U_r/r, B = U_phi/r on grid, and c = Psi_xy(0)."""
    a = to_modes_O(Oh)  # (Ns, M)
    e4 = np.exp(4 * s)[:-1, None]
    incL = e4 * ds * decay[None, :] * cell_ints(a, JL)
    incR = e4 * ds * cell_ints(a, JR)
    L = np.empty_like(a); R = np.empty_like(a)
    L[0] = a[0] * np.exp(4 * s[0]) / (4 * m + 2)
    for j in range(Ns - 1):
        L[j + 1] = decay * L[j] + incL[j]
    kap = 2 + 1.0 / beta_e
    R[-1] = a[-1] * np.exp(4 * s[-1]) / (2 * m + kap - 4)
    for j in range(Ns - 2, -1, -1):
        R[j] = decay * R[j + 1] + incR[j]
    psih = em2s * (L + R) / (4 * m)       # e^{-2s} psi_m
    dpsih = em2s * (R - L) / 2            # e^{-2s} psi_m'
    A = -(psih * (2 * m)) @ C2.T
    B = dpsih @ S.T
    # c = (1/2) int e^{2s} a_1 ds (Simpson) + tails
    G = np.exp(2 * s) * a[:, 0]
    w = np.ones(Ns); w[1:-1:2] = 4; w[2:-1:2] = 2
    if Ns % 2 == 0:
        raise ValueError("Ns must be odd")
    c = 0.5 * (ds / 3 * np.dot(w, G) + G[0] / 4 * 2 + G[-1] / (kap - 2))
    return A, B, c


def ghost_left(F, to_modes, basis):
    """two ghost rows left of s0 from per-mode fit q_m = t^{m-1}(alpha + beta t), t = exp(2(s-s0))."""
    q = to_modes(F[:2])
    t1 = np.exp(2 * ds)
    y0 = q[0]; y1 = q[1] * np.exp(-2 * (m - 1) * ds)
    bb = (y1 - y0) / (t1 - 1); aa = y0 - bb
    G = []
    for k in (2, 1):
        tg = np.exp(-2 * k * ds)
        G.append((tg ** (m - 1) * (aa + bb * tg)) @ basis.T)
    return np.array(G), aa, bb


def ext(F, to_modes, basis):
    gl, aa, bb = ghost_left(F, to_modes, basis)
    r1 = 3 * F[-1] - 3 * F[-2] + F[-3]
    r2 = 3 * r1 - 3 * F[-1] + F[-2]
    return np.vstack([gl, F, r1[None], r2[None]]), aa, bb


def ds_upwind(Fe, A):
    """3rd-order upwind-biased d/ds; Fe has 2 ghosts each side; A sign selects."""
    f = Fe
    j = slice(2, 2 + Ns)
    fm2, fm1, f0, fp1, fp2 = f[0:Ns], f[1:Ns + 1], f[2:Ns + 2], f[3:Ns + 3], f[4:Ns + 4]
    dplus = (2 * fp1 + 3 * f0 - 6 * fm1 + fm2) / (6 * ds)    # for A > 0
    dminus = (-fp2 + 6 * fp1 - 3 * f0 - 2 * fm1) / (6 * ds)  # for A < 0
    return np.where(A > 0, dplus, dminus)


def dphi_O(F):
    return (to_modes_O(F) * (2 * m)) @ C2.T


def dphi_T(F):
    return (to_modes_T(F) * (2 * m - 1)) @ Tc.T


state = {}


def rhs(Oh, Hh, beta_e):
    A_u, B, c = velocity(Oh, beta_e)
    Oe, aO, bO = ext(Oh, to_modes_O, S)
    He, aT, bT = ext(Hh, to_modes_T, T)
    g = 2 * aO[0]
    a0 = aT[0]
    b1 = (bT[0] + 3 * aT[1]) * np.exp(-2 * s[0])  # B1 + 3 B2 (B2 = leading coefficient of mode 2)
    cw = -c / 2
    cl = cw / 2 - b1 / g
    A = -cl + A_u
    Os = ds_upwind(Oe, A); Hs = ds_upwind(He, A)
    Oph = dphi_O(Oh); Hph = dphi_T(Hh)
    src = em2s * (cph * (Hs + Hh) - sph * Hph)
    dO = -A * (Os + 2 * Oh) - B * Oph - cw * Oh + src
    dH = -A * (Hs + Hh) - B * Hph - (cl + 2 * cw) * Hh
    state.update(c=c, cw=cw, cl=cl, g=g, a0=a0, b1=b1, Amin=A.min(), Amax=np.abs(A).max(), Bmax=np.abs(B).max())
    return dO, dH


def filt(Oh, Hh):
    return (to_modes_O(Oh) * sig) @ S.T, (to_modes_T(Hh) * sig) @ T.T


if restart:
    d = np.load(restart)
    Oh = d["Oh"]; Hh = d["Hh"]; tau = float(d["tau"]); beta_e = float(d["beta_e"])
    assert Oh.shape == (Ns, Nph)
else:
    r2 = np.exp(2 * s)[:, None]
    # Theta = AT y exp(-r^2), Omega = -AO x y exp(-r^2)  (AO = 16 gives c = -2)
    import os
    AT = float(os.environ.get("AT", "55")); AO = float(os.environ.get("AO", "16"))
    Hh = AT * sph[None, :] * np.exp(-r2) * np.ones((Ns, Nph))
    Oh = -AO * (0.5 * np.sin(2 * ph))[None, :] * np.exp(-r2)
    tau = 0.0; beta_e = 3.0

log = open(out + ".log", "a")
t0 = time.time()
rhs(Oh, Hh, beta_e)
print(f"# Ns {Ns} Nph {Nph} smin {smin} smax {smax} ds {ds}  init c {state['c']:.6f} g {state['g']:.6f} "
      f"a0 {state['a0']:.6f} b1 {state['b1']:.6f}", file=log, flush=True)
hist = []
nextout = tau
nextsave = tau + 5.0
step = 0
while tau < T_end:
    dO1, dH1 = rhs(Oh, Hh, beta_e)
    dt = 0.4 * min(ds / max(state["Amax"], 1e-3), 1.0 / (max(state["Bmax"], 1e-3) * 2 * Nph))
    dt = min(dt, 0.05)
    k1 = (dO1, dH1)
    k2 = rhs(Oh + 0.5 * dt * k1[0], Hh + 0.5 * dt * k1[1], beta_e)
    k3 = rhs(Oh + 0.5 * dt * k2[0], Hh + 0.5 * dt * k2[1], beta_e)
    k4 = rhs(Oh + dt * k3[0], Hh + dt * k3[1], beta_e)
    Oh = Oh + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
    Hh = Hh + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    Oh, Hh = filt(Oh, Hh)
    tau += dt; step += 1
    st = dict(state)
    beta_e = min(max(-st["cl"] / st["cw"], 1.2), 20.0) if st["cw"] > 0 else 3.0
    if tau >= nextout:
        # steadiness: relative max |d/dtau| of hat fields for s <= 8
        jj = s <= 8.0
        rO = np.abs(dO1[jj]).max() / np.abs(Oh[jj]).max()
        rH = np.abs(dH1[jj]).max() / np.abs(Hh[jj]).max()
        inv = st["a0"] / st["c"] ** 2
        line = (f"tau {tau:9.4f} step {step:7d} dt {dt:.2e} c {st['c']:+.6e} cw {st['cw']:+.6e} cl {st['cl']:+.6e} "
                f"beta {(-st['cl']/st['cw']):.6f} a0 {st['a0']:.8f} g {st['g']:.6f} b1 {st['b1']:+.6e} "
                f"a0/c2 {inv:.5e} Amin {st['Amin']:+.3f} rO {rO:.2e} rH {rH:.2e} maxOh {np.abs(Oh).max():.3e} "
                f"wall {time.time()-t0:.0f}s")
        print(line, file=log, flush=True)
        hist.append([tau, st["c"], st["cw"], st["cl"], -st["cl"] / st["cw"], st["a0"], st["g"], st["b1"], inv, rO, rH])
        nextout = tau + 0.25
        if not np.isfinite(Oh).all() or not np.isfinite(Hh).all():
            print("NONFINITE, stop", file=log, flush=True)
            break
    if tau >= nextsave:
        np.savez(out + ".npz", Oh=Oh, Hh=Hh, tau=tau, beta_e=beta_e, s=s, ph=ph, hist=np.array(hist))
        nextsave = tau + 5.0
np.savez(out + ".npz", Oh=Oh, Hh=Hh, tau=tau, beta_e=beta_e, s=s, ph=ph, hist=np.array(hist))
print("done", file=log, flush=True)
