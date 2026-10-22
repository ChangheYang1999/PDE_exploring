"""Levenberg-Marquardt solve of the vorticity equation in the free-exponent generating basis (model_fb.ModelFB):
unknowns c (coefficients), a0 and beta (unless --fixbeta). Rows as in gsolve.py: R/N (prompt normalizer, lagged), or
R/N2 (--n2), or R/min(N, N2) (--nmin); H(0,0) = 1 (heavy); scale gauge A(1, 0) = initial value.
The beta column is a central finite difference (step hb) through the basis (E, t, w, prefactor) and the field formulas.
Usage: python3 gsolve_fb.py init.npz out.npz J Kw Nt Ns iters tmin gauge alpha [--M M] [--beta b0] [--fixbeta] [--n2|--nmin]
       [--fixa0 a] [--se s] [--hb h] [--maxdb d]
init.npz: a model.py state (m = 3, i.e. beta 3, M 3) or a gsolve_fb state (keys beta, M)."""
import sys, math, time, json, numpy as np, torch
torch.set_num_threads(1)
from jets import Jet, monos, DT
from model import fields
from model_fb import ModelFB, ts_to_xeta_fb
ini, out = sys.argv[1], sys.argv[2]
d = np.load(ini)
J, Kw, Nt, Ns, iters = [int(v) for v in sys.argv[3:8]]
tmin = float(sys.argv[8]); gauge = int(sys.argv[9]); alpha = float(sys.argv[10])
opt = lambda k, dflt, f=float: f(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else dflt
se = opt('--se', float(d['se']) if 'se' in d.files else 1.0)
gam = float(d['gam']) if 'gam' in d.files else 0.0
M = opt('--M', int(d['M']) if 'M' in d.files else 3, int)
beta = opt('--beta', float(d['beta']) if 'beta' in d.files else 3.0)
if 'm' in d.files and 'M' not in d.files and int(d['m']) != 3: raise SystemExit('init is a model.py state with m != 3: its t variable differs')
FIXB = '--fixbeta' in sys.argv
fixa0 = opt('--fixa0', None)
hb = opt('--hb', 1e-5); maxdb = opt('--maxdb', 0.02)
NMIN = '--nmin' in sys.argv; N2MODE = '--n2' in sys.argv or NMIN
print('rows:', 'R/min(N,N2)' if NMIN else ('R/N2' if N2MODE else 'R/N'), ' beta', beta, 'fixed' if FIXB else 'free', ' M', M, flush=True)
mod = ModelFB(J, Kw, beta=beta, M=M, alpha=alpha, se=se, gam=gam)
J0, K0 = int(d['J']), int(d['Kw'])
c = np.zeros((J + 1, Kw + 1)); c0 = d['c'].reshape(J0 + 1, K0 + 1)
c[:min(J, J0) + 1, :min(Kw, K0) + 1] = c0[:min(J, J0) + 1, :min(Kw, K0) + 1]
c = c.ravel(); a0 = float(d['a0']) if fixa0 is None else fixa0

def t_of_tau(tau, alpha):
    if alpha <= 0: return tau
    z = (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1)
    return 1 - z

def grid(Nt, Ns, tmin, beta0):
    it = (np.arange(Nt) + 0.5) / Nt; is_ = (np.arange(Ns) + 0.5) / Ns
    tau = 0.5 * (1 - np.cos(np.pi * it))
    t = tmin + (1 - tmin) * t_of_tau(tau, alpha)
    s = 0.5 * (1 - np.cos(np.pi * is_))
    T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
    x, eta = ts_to_xeta_fb(T, S, beta0, M, se)
    keep = (x > 1e-12) & (eta > 1e-12)
    return torch.tensor(x[keep]), torch.tensor(eta[keep])

x0, e0 = grid(Nt, Ns, tmin, beta)          # fixed collocation points in (x, eta), valid for every beta
xg = torch.tensor([1.0], dtype=DT); eg = torch.tensor([0.0], dtype=DT)
ia11 = monos(2)[1][(1, 1)]
def bg_row(b):
    mod.set_beta(b); return mod.basis_matrix(xg, eg, p=2)[ia11, 0].numpy()
def gjet(c, b):
    mod.set_beta(b); return mod.g_jet(c, x0, e0)
Bg = bg_row(beta); Bm = mod.basis_matrix(x0, e0)
print('points', x0.shape[0], 'unknowns', mod.nb + 2, flush=True)
h00 = mod.h00_row()
Ag_target = float(Bg @ c)
WH, WG = 1e4, 1e2

def resid(c, a0, b, Bm_=None, Nlag=None, need_jac=False, Gc=None):
    if Gc is None: Gc = Bm_ @ torch.tensor(c)
    Gc = Gc.detach().requires_grad_(need_jac)
    a0t = torch.tensor(a0, dtype=DT, requires_grad=need_jac)
    F = fields(Gc, x0, e0, a0t, b)
    Fd = {k: v.detach() for k, v in F.items()}
    N2 = (Fd['U1'] * Fd['Ox']).abs() + (Fd['U2'] * Fd['Oy']).abs() + (b * (x0 * Fd['Ox'] + Fd['y'] * Fd['Oy']) + Fd['Om']).abs() + Fd['Thx'].abs()
    if Nlag is not None: Nn = Nlag
    elif NMIN: Nn = torch.minimum(N2, Fd['N'])
    elif N2MODE: Nn = N2
    else: Nn = Fd['N']
    res = F['R'] / Nn
    out = dict(res=res.detach().numpy(), N=Nn, A=Fd['A'].numpy(), rN=(Fd['R'] / Fd['N']).numpy(), rN2=(Fd['R'] / N2).numpy())
    if need_jac:
        gG, ga = torch.autograd.grad(res.sum(), [Gc, a0t])
        out['Jc'] = torch.einsum('mi,min->in', gG, Bm_).numpy()
        out['Ja'] = (-(Fd['Thx']) / a0 / Nn).numpy()
    return out

def full_res(c, a0, Bg_, ev):
    return np.concatenate([ev['res'], [WH * (h00 @ c - 1)], [WG * (Bg_ @ c - Ag_target)] if gauge else []])

def jacobian(c, a0, b, ev):
    cols = [ev['Jc'], ev['Ja'][:, None]]
    if not FIXB:
        rp = resid(c, a0, b + hb, Nlag=ev['N'], Gc=gjet(c, b + hb))['res']; Bgp = bg_row(b + hb)
        rm = resid(c, a0, b - hb, Nlag=ev['N'], Gc=gjet(c, b - hb))['res']; Bgm = bg_row(b - hb)
        mod.set_beta(b)
        jb = (rp - rm) / (2 * hb); jg = (Bgp @ c - Bgm @ c) / (2 * hb)
        cols.append(jb[:, None])
    J_ = np.hstack(cols)
    nz = J_.shape[1]
    rows = [J_, WH * np.concatenate([h00, np.zeros(nz - len(h00))])[None, :]]
    if gauge:
        g = np.concatenate([Bg, [0.0]] + ([[jg]] if not FIXB else [])); rows.append(WG * g[None, :])
    return np.vstack(rows)

lam = 1e-3; hist = []; t0 = time.time()
ev = resid(c, a0, beta, Bm, need_jac=True)
r = full_res(c, a0, Bg, ev)
print('init obj %.4e maxres %.3e R/N %.3e R/N2 %.3e minA %.3e a0 %.4f beta %.6f' % (r @ r, np.abs(ev['res']).max(), np.abs(ev['rN']).max(),
      np.abs(ev['rN2']).max(), ev['A'].min(), a0, beta), flush=True)
for itn in range(iters):
    r = full_res(c, a0, Bg, ev); Jm = jacobian(c, a0, beta, ev); obj = float(r @ r)
    if fixa0 is not None: Jm[:, len(c)] = 0.0
    D = np.linalg.norm(Jm, axis=0); D[D == 0] = 1
    U_, s_, Vt = np.linalg.svd(Jm / D, full_matrices=False)
    g = U_.T @ r; acc = False
    for trial in range(12):
        step = -(Vt.T @ (s_ * g / (s_ ** 2 + lam))) / D
        cn = c + step[:len(c)]; an = a0 + (0.0 if fixa0 is not None else step[len(c)])
        bn = beta if FIXB else beta + float(np.clip(step[len(c) + 1], -maxdb, maxdb))
        if bn != beta:
            Bgn = bg_row(bn); evn = resid(cn, an, bn, Nlag=ev['N'], Gc=gjet(cn, bn))
        else:
            Bgn = Bg; evn = resid(cn, an, bn, Bm, Nlag=ev['N'])
        rn = full_res(cn, an, Bgn, evn)
        if np.all(np.isfinite(rn)) and evn['A'].min() > 0 and float(rn @ rn) < obj:
            acc = True; break
        lam *= 4
    if not acc:
        mod.set_beta(beta); print('it %d: no decrease, stop' % itn, flush=True); break
    if bn != beta:
        mod.set_beta(bn); del Bm; Bm = mod.basis_matrix(x0, e0)
    c, a0, beta, Bg = cn, an, bn, Bgn
    mod.set_beta(beta)
    lam = max(lam / 3, 1e-12)
    ev = resid(c, a0, beta, Bm, need_jac=True)
    rec = dict(it=itn, obj=float(full_res(c, a0, Bg, ev) @ full_res(c, a0, Bg, ev)), maxres=float(np.abs(ev['res']).max()),
               maxRN=float(np.abs(ev['rN']).max()), maxRN2=float(np.abs(ev['rN2']).max()), rms=float(np.sqrt(np.mean(ev['res'] ** 2))),
               a0=a0, beta=beta, minA=float(ev['A'].min()), lam=lam, H00=float(h00 @ c), s_ratio=float(s_[-1] / s_[0]), sec=time.time() - t0)
    hist.append(rec)
    if itn % 5 == 0 or itn == iters - 1: print(json.dumps(rec), flush=True)
    np.savez(out, c=c, a0=a0, J=J, Kw=Kw, beta=beta, M=M, hist=json.dumps(hist), Nt=Nt, Ns=Ns, tmin=tmin, gauge=gauge, alpha=alpha,
             se=se, gam=gam, l=float(d['l']) if 'l' in d.files else 1.0, family='fb')
