"""Levenberg-Marquardt solve of the vorticity equation (2) in the generating-function basis (beta = 3).
Unknowns: c (basis coefficients of G), a0. Rows: R/N (prompt normalizer, lagged) at collocation points of a (t, sigma)
grid in the compact mixed domain; H(0,0) = 1 (heavy); optional scale gauge A(xg, 0) = A_init(xg, 0).
Usage: python3 gsolve.py init.npz out.npz [J Kw Nt Ns iters tmin gauge(0/1)]
--farrows Nw Wf: add Nw rows Wf * C/N20 (lagged N20) at Chebyshev nodes of the far section (farrows.py): the exact limit of
R/N2 at physical infinity (m = 3, gam = 0, alpha > 0 only)."""
import sys, math, time, json, numpy as np, torch
torch.set_num_threads(1)
from jets import Jet, monos, DT
from model import Model, fields, ts_to_xeta
ini, out = sys.argv[1], sys.argv[2]
d = np.load(ini)
J = int(sys.argv[3]) if len(sys.argv) > 3 else int(d['J'])
Kw = int(sys.argv[4]) if len(sys.argv) > 4 else int(d['Kw'])
Nt = int(sys.argv[5]) if len(sys.argv) > 5 else 2 * J + 8
Ns = int(sys.argv[6]) if len(sys.argv) > 6 else 2 * Kw + 8
iters = int(sys.argv[7]) if len(sys.argv) > 7 else 30
tmin = float(sys.argv[8]) if len(sys.argv) > 8 else 0.01
gauge = int(sys.argv[9]) if len(sys.argv) > 9 else 1
alpha = float(sys.argv[10]) if len(sys.argv) > 10 and not sys.argv[10].startswith('--') else (float(d['alpha']) if 'alpha' in d.files else 0.0)
se = float(sys.argv[sys.argv.index('--se') + 1]) if '--se' in sys.argv else (float(d['se']) if 'se' in d.files else 1.0)
gam = float(sys.argv[sys.argv.index('--gam') + 1]) if '--gam' in sys.argv else (float(d['gam']) if 'gam' in d.files else 0.0)
m_ = int(sys.argv[sys.argv.index('--m') + 1]) if '--m' in sys.argv else (int(d['m']) if 'm' in d.files else 3)
if m_ != (int(d['m']) if 'm' in d.files else 3): print('WARNING: m differs from the initial state; coefficients are reinterpreted', flush=True)
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam)
if alpha != (float(d['alpha']) if 'alpha' in d.files else 0.0) or se != (float(d['se']) if 'se' in d.files else 1.0) or gam != (float(d['gam']) if 'gam' in d.files else 0.0):
    print('WARNING: alpha differs from the initial state; coefficients are reinterpreted', flush=True)
J0, K0 = int(d['J']), int(d['Kw'])
c = np.zeros((J + 1, Kw + 1)); c0 = d['c'].reshape(J0 + 1, K0 + 1)
c[:min(J, J0) + 1, :min(Kw, K0) + 1] = c0[:min(J, J0) + 1, :min(Kw, K0) + 1]
c = c.ravel(); a0 = float(d['a0'])
core = None     # core patches (model_core.ModelCore): --core Jc Kc Rc Lc (repeatable), or continued from the init key 'core'
from model_core import as_patches
if '--core' in sys.argv:
    core = [(int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3]), float(sys.argv[i_ + 4])) for i_, a_ in enumerate(sys.argv) if a_ == '--core']
elif 'core' in d.files: core = as_patches(d['core'])
if core is not None:
    from model_core import ModelCore
    mod = ModelCore(J, Kw, core, m=m_, alpha=alpha, se=se, gam=gam)
    cold = as_patches(d['core']) if 'core' in d.files else []
    ccold = d['cc'] if 'core' in d.files else np.zeros(0)
    parts = []; off = 0; offs = []
    for q in cold: offs.append(off); off += (q[0] + 1) * (q[1] + 1)
    for ip, q in enumerate(core):
        cc = np.zeros((q[0] + 1, q[1] + 1))
        if ip < len(cold):
            q0 = cold[ip]
            if abs(q0[2] - q[2]) > 0 or abs(q0[3] - q[3]) > 0: print('WARNING: patch %d Rc/Lc differ from the initial state' % ip, flush=True)
            cc0 = ccold[offs[ip]:offs[ip] + (q0[0] + 1) * (q0[1] + 1)].reshape(q0[0] + 1, q0[1] + 1)
            cc[:min(q0[0], q[0]) + 1, :min(q0[1], q[1]) + 1] = cc0[:min(q0[0], q[0]) + 1, :min(q0[1], q[1]) + 1]
        parts.append(cc.ravel())
    c = np.concatenate([c] + parts)
    print('core patches', core, ': %d extra unknowns' % mod.nbc, flush=True)
nbo = (J + 1) * (Kw + 1)
fixa0 = None
NMIN = '--nmin' in sys.argv     # rows R/min(N, N2): targets the larger of the two normalized residuals
N2MODE = '--n2' in sys.argv or NMIN
if N2MODE: print('rows: R/N2 (non-cancelling normalizer)' if not NMIN else 'rows: R/min(N, N2)', flush=True)
if '--fixa0' in sys.argv:
    fixa0 = float(sys.argv[sys.argv.index('--fixa0') + 1]); a0 = fixa0

def t_of_tau(tau, alpha):
    if alpha <= 0: return tau
    z = (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1)
    return 1 - z

def grid(Nt, Ns, tmin, shift=0.0):
    it = (np.arange(Nt) + 0.5 + shift) / Nt; is_ = (np.arange(Ns) + 0.5 + shift) / Ns
    tau = 0.5 * (1 - np.cos(np.pi * it))                              # Chebyshev-clustered at both ends
    t = t_of_tau(tau, alpha)
    t = tmin + (1 - tmin) * t
    s = 0.5 * (1 - np.cos(np.pi * is_))
    T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
    S = S if gam <= 0 else (np.exp(gam * S) - 1) / (np.exp(gam) - 1)
    x, eta = ts_to_xeta(T, S, m_, se)
    keep = (x > 1e-12) & (eta > 1e-12)
    return torch.tensor(x[keep]), torch.tensor(eta[keep])

x0, e0 = grid(Nt, Ns, tmin)
if '--inner' in sys.argv:
    # extra collocation points near the origin, polar in (x, eta) (eta ~ y there): the (t, s) grid leaves the region
    # x^2 + eta^6 < 6 (1 - t_max) unsampled (x < 0.005, eta < 0.2 at Nt ~ 100), a thin strip along the y-axis
    i_ = sys.argv.index('--inner'); nri, nti, rmi, rma = int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3]), float(sys.argv[i_ + 4])
    rho = np.logspace(np.log10(rmi), np.log10(rma), nri); th = 0.5 * np.pi * (0.5 * (1 - np.cos(np.pi * (np.arange(nti) + 0.5) / nti)))
    Rr, Th = np.meshgrid(rho, th, indexing='ij')
    x0 = torch.cat([x0, torch.tensor((Rr * np.cos(Th)).ravel())]); e0 = torch.cat([e0, torch.tensor((Rr * np.sin(Th)).ravel())])
    print('inner: %d extra points, rho %g .. %g' % (nri * nti, rmi, rma), flush=True)
wts = torch.ones_like(x0)
if '--worig' in sys.argv:      # extra weight W on rows with physical radius < R0 (radius from the initial state)
    Wo, Ro = float(sys.argv[sys.argv.index('--worig') + 1]), float(sys.argv[sys.argv.index('--worig') + 2])
    Gx0 = (mod.basis_matrix(x0, e0, p=1)[monos(1)[1][(1, 0)]] @ torch.tensor(c))
    wts = torch.where(torch.hypot(x0, Gx0) < Ro, torch.full_like(x0, Wo), wts)
    print('worig: weight %g on %d rows with r < %g' % (Wo, int((wts > 1).sum()), Ro), flush=True)
Bm = mod.basis_matrix(x0, e0)            # (15, N, nb)
FAR = None
if '--farrows' in sys.argv:
    from farrows import FarRows, cheb_w
    if m_ != 3 or gam != 0.0 or alpha <= 0: raise SystemExit('--farrows needs m = 3, gam = 0, alpha > 0')
    i_ = sys.argv.index('--farrows'); Nwf, Wf = int(sys.argv[i_ + 1]), float(sys.argv[i_ + 2])
    FAR = FarRows(J, Kw, alpha, se, cheb_w(Nwf))
    print('farrows: %d section points, weight %g' % (Nwf, Wf), flush=True)
print('points', x0.shape[0], 'unknowns', mod.nb + 1, flush=True)
h00 = mod.h00_row()
Lm, ixm = monos(4)
xg = torch.tensor([1.0], dtype=DT); eg = torch.tensor([0.0], dtype=DT)
Bg = mod.basis_matrix(xg, eg, p=2)[monos(2)[1][(1, 1)], 0].numpy()   # A(xg, 0) row
Ag_target = float(Bg @ c)
WH, WG = 1e4, 1e2

def evaluate(c, a0, need_jac=True, Nlag=None):
    NlagF = Nlag
    if FAR is not None and Nlag is not None: Nlag = Nlag[0]
    ct = torch.tensor(c)
    Gc = (Bm @ ct).detach().requires_grad_(need_jac)
    a0t = torch.tensor(a0, dtype=DT, requires_grad=need_jac)
    F = fields(Gc, x0, e0, a0t, mod.beta)
    if N2MODE:
        # non-cancelling normalizer: |U1 Om_x| + |U2 Om_y| + |beta X.grad Om + Om| + |Theta_x| (far field: R/N2 -> C, the
        # next-order coefficient of the vorticity equation, while the prompt's R/N ~ r^(-1/3) C there)
        Fd = {k: v.detach() for k, v in F.items()}
        N2 = (Fd['U1'] * Fd['Ox']).abs() + (Fd['U2'] * Fd['Oy']).abs() + (mod.beta * (x0 * Fd['Ox'] + Fd['y'] * Fd['Oy']) + Fd['Om']).abs() + Fd['Thx'].abs()
        if NMIN: N2 = torch.minimum(N2, Fd['N'])
        Nn = N2 if Nlag is None else Nlag
    else:
        Nn = F['N'].detach() if Nlag is None else Nlag
    res = F['R'] / Nn * wts
    out = dict(res=res.detach().numpy(), N=Nn, A=F['A'].detach().numpy(), y=F['y'].detach().numpy())
    if need_jac:
        gG, ga = torch.autograd.grad(res.sum(), [Gc, a0t])
        # res_i depends on Gc[:, i] only (pointwise), except through a0 (scalar): d res/d a0 = B0/(A N)
        Jc = torch.einsum('mi,min->in', gG, Bm).numpy()
        Ja = (-(F['Thx'].detach()) / a0t.detach() / Nn).numpy()      # dR/da0 = B0/A = -Thx/a0
        out['J'] = np.hstack([Jc, Ja[:, None]])
    if FAR is not None:
        ctf = torch.tensor(c[:nbo]).requires_grad_(need_jac); af = torch.tensor(a0, dtype=DT, requires_grad=need_jac)
        Z = FAR.terms(ctf, af)
        N20 = Z.detach().abs().sum(0) if NlagF is None else NlagF[1]
        q = Z.sum(0) / N20
        out['far'] = Wf * q.detach().numpy(); out['N'] = (out['N'], N20)
        if need_jac:
            Jf = np.zeros((len(q), len(c) + 1))
            for i in range(len(q)):
                gc, ga_ = torch.autograd.grad(q[i], [ctf, af], retain_graph=True)
                Jf[i, :nbo] = Wf * gc.numpy(); Jf[i, -1] = Wf * float(ga_)
            out['Jfar'] = Jf
    return out

def full_res(c, a0, ev):
    return np.concatenate([ev['res']] + ([ev['far']] if FAR is not None else []) + [[WH * (h00 @ c - 1)], [WG * (Bg @ c - Ag_target)] if gauge else []])

def full_jac(ev):
    rows = [ev['J']] + ([ev['Jfar']] if FAR is not None else []) + [WH * np.append(h00, 0)[None, :]]
    if gauge: rows.append(WG * np.append(Bg, 0)[None, :])
    return np.vstack(rows)

lam = 1e-3
hist = []
t0 = time.time()
ev = evaluate(c, a0)
r = full_res(c, a0, ev)
print('init obj %.4e maxres %.3e rms %.3e minA %.3e a0 %.4f' % (r @ r, np.abs(ev['res']).max(), np.sqrt(np.mean(ev['res']**2)), ev['A'].min(), a0), flush=True)
if FAR is not None: print('init far max |C|/N20 %.4e' % (np.abs(ev['far']).max() / Wf), flush=True)
if '--fdcheck' in sys.argv:
    Jm = full_jac(ev); rng = np.random.default_rng(0); v = rng.standard_normal(Jm.shape[1]) * 1e-7
    rp = full_res(c + v[:-1], a0 + v[-1], evaluate(c + v[:-1], a0 + v[-1], False, ev['N'])); rm = full_res(c - v[:-1], a0 - v[-1], evaluate(c - v[:-1], a0 - v[-1], False, ev['N']))
    fd = (rp - rm) / 2; an = Jm @ v; print('FD check rel', np.abs(fd - an).max() / np.abs(an).max())
irls = None
if '--irls' in sys.argv:   # IRLS towards an L^p (large p: near-minimax) fit: every k its, w_i = (|r_i|/max|r| + floor)^((p - 2)/2)
    i_ = sys.argv.index('--irls'); irls = (float(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3]))
    print('irls: p %g every %d its, floor %g' % irls, flush=True)
for itn in range(iters):
    if irls is not None and itn % irls[1] == 0:
        ru = np.abs(ev['res'] / wts.numpy()); wn = (ru / ru.max() + irls[2]) ** ((irls[0] - 2) / 2)
        wn = wn / np.sqrt(np.mean(wn ** 2))
        if itn > 0: wn = np.sqrt(wn * wts.numpy())      # damped update: geometric mean with the previous weights
        wts = torch.tensor(wn / np.sqrt(np.mean(wn ** 2)), dtype=DT); ev = evaluate(c, a0)
    r = full_res(c, a0, ev); Jm = full_jac(ev)
    obj = float(r @ r)
    if fixa0 is not None: Jm = Jm.copy(); Jm[:, -1] = 0.0
    D = np.linalg.norm(Jm, axis=0); D[D == 0] = 1
    U_, s_, Vt = np.linalg.svd(Jm / D, full_matrices=False)
    g = U_.T @ r
    acc = False
    for trial in range(12):
        step = -(Vt.T @ (s_ * g / (s_ ** 2 + lam))) / D
        cn = c + step[:-1]; an = a0 + (0.0 if fixa0 is not None else step[-1])
        evn = evaluate(cn, an, need_jac=False, Nlag=ev['N'])
        rn = full_res(cn, an, evn)
        if np.all(np.isfinite(rn)) and evn['A'].min() > 0 and float(rn @ rn) < obj:
            acc = True; break
        lam *= 4
    if not acc:
        print('it %d: no decrease, stop' % itn, flush=True); break
    c, a0 = cn, an
    lam = max(lam / 3, 1e-12)
    ev = evaluate(c, a0)
    rr = ev['res'] / wts.numpy()
    if N2MODE:
        F_ = fields((Bm @ torch.tensor(c)), x0, e0, torch.tensor(a0, dtype=DT), mod.beta); rN = (F_['R'] / F_['N']).detach().numpy()
    rec = dict(it=itn, obj=float(full_res(c, a0, ev) @ full_res(c, a0, ev)), maxres=float(np.abs(rr).max()),
               rms=float(np.sqrt(np.mean(rr ** 2))), maxRN=float(np.abs(rN).max()) if N2MODE else None, a0=a0, minA=float(ev['A'].min()), lam=lam, H00=float(h00 @ c),
               s_ratio=float(s_[-1] / s_[0]), sec=time.time() - t0, maxfar=float(np.abs(ev['far']).max() / Wf) if FAR is not None else None)
    hist.append(rec)
    if itn % 10 == 0 or itn == iters - 1: print(json.dumps(rec), flush=True)
    np.savez(out, c=c[:nbo], a0=a0, J=J, Kw=Kw, m=m_, **({} if core is None else dict(cc=c[nbo:], core=np.array(core, dtype=float).reshape(-1, 4))), beta=mod.beta, hist=json.dumps(hist), Nt=Nt, Ns=Ns, tmin=tmin, gauge=gauge, alpha=alpha, se=se, gam=gam,
             l=float(d['l']) if 'l' in d else 1.0)
