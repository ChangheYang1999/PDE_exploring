"""Continuation diagnostics requested by the lead (team notes 2026-10-18T09:48Z item 2(b), 10:10Z item 2(a)-(c); specification M27(g), M28(j)).
full_diag(SB, g, p, coef) on a forward state g [Nr, Nth] (rho = r^p g, datum A = cos^2 exp(sum coef_j phi_j) on the outer ring):
  m1 (core-corrected moment), c (strain moment), axis law in both forms with the local h (fd1): D_div, D_dir, drifts, q_+-(lr) ;
  G_+- = exp(q_+-) at lr -11 (axis_D q_sel);  a_* = max_th g(r_max, th) = max A (rho(r_max, th)/r_max^p);  Q = log G_+ + log(a_*)/(1 - p);
  c_<R = core term + (1/pi) int_{r_min}^R r^-2 int rho sin 3th dth dr at R = e^-10, e^-8 and the curve c_<r / c at lr = -13..0 ;
  E_R = (1/pi) int_{r<R} |rho - G_+- x^2| r^-3 |sin 3th| dX per half-plane (upper: G_+, lower: G_-), R = e^-10, e^-8, inner part below r_min
        from rho/r^2 frozen at the first ring (same convention as the core term);
  sigma(lr) = d log rho(r, 0)/d log r = p + d log g(:, 0)/d lr (central differences): lr ranges with |sigma - 2| <= 0.05 and |sigma - p| <= 0.05,
        crossing radii sigma = 1.9, 1.0, 0.6 (lead M28(k)), plateau search (longest interval of length >= 1 in lr with range <= 0.05 outside the 2 / p ranges);
  min |V|/r and min V_r/r with locations (lr, deg).
"""
import math, json
import numpy as np
import torch
from pfwd_diag import axis_D


def datum_fun(coef, qj=2.0):
    coef = np.asarray(coef, float)
    def Afun(t):
        F = torch.zeros_like(t)
        for j in range(len(coef)):
            n = j + 1; F = F + float(coef[j]) * (torch.sin(n * t) if n % 2 == 1 else torch.cos(n * t))
        return torch.cos(t).abs() ** float(qj) * torch.exp(F)
    return Afun


def _crossings(lr, sig, level):
    out = []
    for i in range(len(lr) - 1):
        if (sig[i] - level) * (sig[i + 1] - level) < 0:
            out.append(float(lr[i] + (level - sig[i]) / (sig[i + 1] - sig[i]) * (lr[i + 1] - lr[i])))
    return out


def _ranges(lr, msk):
    out = []; i = 0
    while i < len(lr):
        if msk[i]:
            j = i
            while j + 1 < len(lr) and msk[j + 1]: j += 1
            out.append((round(float(lr[i]), 2), round(float(lr[j]), 2))); i = j + 1
        else:
            i += 1
    return out


def full_diag(SB, g, p, coef, Rs_lr=(-10.0, -8.0), curve_lr=tuple(range(-13, 1)), qj=2.0, Afun=None):
    qj = float(qj)
    S = SB.S; dev = g.device
    pB = torch.tensor([float(p)], device=dev)
    A = (Afun if Afun is not None else datum_fun(coef, qj))(S.th[None, :])     # [1, Nth]; Afun = the full datum (with window bumps) when given
    rho = S.r[None, :, None] ** float(p) * g[None]
    Wr, Wt = SB.velocity(rho, pB)
    cm, core = SB.c_moment(rho, pB, A, qj=qj); m1 = 1.0 / float(p) - float(cm[0]); c = float(cm[0])
    axd = axis_D(S, g, Wr[0], float(p), m1, A=A[0], hmode='fd1', qj=qj)
    axr = axis_D(S, g, Wr[0], float(p), m1, A=A[0], Wt=Wt[0], hmode='fd1', qj=qj)
    qsel = lambda ax, side, L: ax['q_%s' % side].get('%g' % L)
    q_up11, q_dn11 = qsel(axd, 'up', -11), qsel(axd, 'down', -11)
    # COEFFICIENT convention (referee audit, item 7, 2026-10-18T11:17Z): at q = 2 axis_D's h is rho_xx = 2 x (coefficient of x^2); for q != 2 it is the
    # coefficient itself.  G_+- below are the coefficients of |x|^q (rho ~ G_+- |x|^q on the two half-axes).
    hfac = 2.0 if abs(qj - 2.0) < 1e-12 else 1.0
    G_plus, G_minus = math.exp(q_up11) / hfac, math.exp(q_dn11) / hfac
    a_star = float(g[-1].max())
    Q = math.log(G_plus) + (qj - 1.0) * math.log(a_star) / (1.0 - float(p))     # scale-invariant under rho_a(X) = a rho(X/a): G -> a^(1-q) G, a_* -> a^(1-p) a_* (referee audit, item 9)
    lr = S.lr.cpu().numpy(); r = np.exp(lr); th = S.th.cpu().numpy(); dth = float(S.dth)
    rh = rho[0].cpu().numpy()
    s3 = np.sin(3 * th)
    # c_<r curve (per unit lr integrand: (1/pi) r^-1 int rho sin3th dth)
    integ = (rh * s3[None, :]).sum(1) * dth / math.pi / r
    cum = float(core[0]) + np.concatenate([[0.0], np.cumsum(0.5 * (integ[1:] + integ[:-1]) * np.diff(lr))])
    cfun = lambda L: float(np.interp(L, lr, cum))
    c_lt = {('%g' % L): cfun(L) for L in Rs_lr}
    c_curve = {('%g' % L): round(cfun(L) / c, 5) if c != 0 else float('nan') for L in curve_lr}
    # E_R per half-plane (upper th in (0, pi): G_+; lower: G_-)
    x2 = np.abs(r[:, None] * np.cos(th)[None, :]) ** qj                 # |x|^q (x^2 at q = 2)
    up = (np.sin(th) > 0)[None, :]
    Gfield = np.where(up, G_plus, G_minus)
    dev_ = np.abs(rh - Gfield * x2) * np.abs(s3)[None, :]
    E = {}
    for side, msk in (('up', up[0]), ('down', ~up[0])):
        ie = (dev_[:, msk]).sum(1) * dth / math.pi / r                   # per unit lr
        inner = r[0] / math.pi / (qj - 1.0) * ((np.abs(rh[0, msk] / r[0] ** qj - Gfield[0, msk] * np.abs(np.cos(th[msk])) ** qj) * r[0] ** (qj - 2) * np.abs(s3[msk])).sum()) * dth
        cumE = inner + np.concatenate([[0.0], np.cumsum(0.5 * (ie[1:] + ie[:-1]) * np.diff(lr))])
        for L in Rs_lr:
            E['%s_%g' % (side, L)] = float(np.interp(L, lr, cumE))
    # sigma on th = 0
    g0 = g[:, 0].cpu().numpy()
    sig = float(p) + np.gradient(np.log(np.clip(g0, 1e-300, None)), lr)
    near2 = _ranges(lr, np.abs(sig - qj) <= 0.05); nearp = _ranges(lr, np.abs(sig - float(p)) <= 0.05)
    cross = {('%g' % L): [round(v, 2) for v in _crossings(lr, sig, L)] for L in (1.9, 1.0, 0.6)}
    if abs(qj - 2.0) > 1e-12: cross['%g' % (qj - 0.1)] = [round(v, 2) for v in _crossings(lr, sig, qj - 0.1)]
    # plateau: longest window of length >= 1 with range <= 0.05, outside the 2 and p bands
    plateau = None
    excl = (np.abs(sig - qj) <= 0.1) | (np.abs(sig - float(p)) <= 0.1)
    n1 = int(round(1.0 / float(S.d)))
    best = 0
    for i in range(len(lr) - n1):
        w = sig[i:i + n1 + 1]
        if excl[i:i + n1 + 1].any(): continue
        if w.max() - w.min() <= 0.05:
            j = i + n1
            while j + 1 < len(lr) and not excl[j + 1] and sig[i:j + 2].max() - sig[i:j + 2].min() <= 0.05: j += 1
            if j - i > best:
                best = j - i; plateau = dict(lr=(round(float(lr[i]), 2), round(float(lr[j]), 2)), value=round(float(sig[i:j + 1].mean()), 3))
    sig_sel = {('%g' % L): round(float(np.interp(L, lr, sig)), 3) for L in range(-13, 1)}
    # velocity minima
    Vr_r = (1.0 / float(p)) + Wr[0] / S.r[:, None]; Vt_r = Wt[0] / S.r[:, None]; Vabs = torch.sqrt(Vr_r ** 2 + Vt_r ** 2)
    thd = np.degrees(th)
    i, j = np.unravel_index(int(Vabs.argmin()), Vabs.shape); i2, j2 = np.unravel_index(int(Vr_r.argmin()), Vr_r.shape)
    out = dict(qj=qj, p=float(p), m1=m1, c=c, core=float(core[0]), D_div=axd['D_ax_k'], D_dir=axr['D_ax_k'], drift_up_div=axd['drift_up'], drift_down_div=axd['drift_down'],
               drift_up_dir=axr['drift_up'], drift_down_dir=axr['drift_down'], q_up=axd['q_up'], q_down=axd['q_down'], G_plus=G_plus, G_minus=G_minus,
               logG_ratio_m11=q_dn11 - q_up11, a_star=a_star, Q=Q, G_convention='coefficient of |x|^q (rho ~ G |x|^q)', c_lt=c_lt, c_curve_frac=c_curve, E_R=E, sigma_sel=sig_sel, sigma_near2=near2, sigma_nearp=nearp,
               sigma_cross=cross, sigma_plateau=plateau, minVabs_r=float(Vabs.min()), minVabs_at=[float(lr[i]), float(thd[j])], minVr_r=float(Vr_r.min()),
               minVr_at=[float(lr[i2]), float(thd[j2])])
    return out


def summary_line(d, label=''):
    return ("%-26s p %.4f m1 %.5f D_div %.4f D_dir %.4f drU %.3f/%.3f Q %.3f G+ %.3g c %.4f c<-10 %.4f c<-8 %.4f E_up(-10,-8) %.2e/%.2e E_dn %.2e/%.2e "
            "min|V|/r %.3f@(%.1f,%.0f) minVr/r %.3f@(%.1f,%.0f) sig1.9 %s sig1.0 %s sig0.6 %s plateau %s" % (
            label[:26], d['p'], d['m1'], d['D_div'], d['D_dir'], d['drift_up_div'], d['drift_up_dir'], d['Q'], d['G_plus'], d['c'], d['c_lt']['-10'], d['c_lt']['-8'],
            d['E_R']['up_-10'], d['E_R']['up_-8'], d['E_R']['down_-10'], d['E_R']['down_-8'], d['minVabs_r'], d['minVabs_at'][0], d['minVabs_at'][1],
            d['minVr_r'], d['minVr_at'][0], d['minVr_at'][1], d['sigma_cross']['1.9'], d['sigma_cross']['1'], d['sigma_cross']['0.6'], d['sigma_plateau']))
