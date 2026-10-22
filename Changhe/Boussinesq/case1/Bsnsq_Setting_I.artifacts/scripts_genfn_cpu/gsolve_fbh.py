"""gsolve_fb.py with core patches, inner points and exact far rows, for fixed- and free-beta studies at high resolution.
Basis: model_core_fb.ModelCoreFB (free-exponent outer basis of model_fb plus the core patches of model_core); for beta = 3,
M = 3 it equals model_core.ModelCore, so the core states of gsolve.py (keys core, cc) are reused unchanged.
Unknowns c (outer, then patch coefficients), a0 and beta (unless --fixbeta). Rows as in gsolve_fb.py: R/N, R/N2 (--n2) or
R/min(N, N2) (--nmin), lagged; H(0,0) = 1 (heavy); scale gauge A(1, 0) = initial value; optionally the far rows.
The beta column is a central finite difference (step hb) through the basis, the field formulas and the far rows.
Usage: python3 gsolve_fbc.py init.npz out.npz J Kw Nt Ns iters tmin gauge alpha [--M M] [--beta b0] [--fixbeta]
       [--n2|--nmin] [--fixa0 a] [--se s] [--hb h] [--maxdb d] [--core Jc Kc Rc Lc]... [--inner nr nth rmin rmax]
       [--farrows Nw Wf] [--betacurv] [--lam0 l]
--farrows Nw Wf: Nw rows Wf C/N20 at Chebyshev nodes in w of the far section (farrows.FarRows with this beta): the exact
  limit of R/N2 at physical infinity (gam = 0, alpha > 0).
--betacurv: at the start and at the end print the beta-profile diagnostic of the linearized least-squares problem:
  p = |P J_b| (component of the beta column orthogonal to the span of the c and a0 columns), db* = -(P J_b . P r)/p^2
  (the reoptimized Gauss-Newton beta step) and dB = sqrt(obj)/p (the beta offset whose reoptimized linearized objective
  increase equals the current objective)."""
import sys, math, time, json, numpy as np, torch
torch.set_num_threads(1)
from jets import Jet, monos, DT
from model_h import fields_h as fields
from model_fb import ts_to_xeta_fb
from model_core_fb import ModelCoreFB
from model_core import as_patches
ini, out = sys.argv[1], sys.argv[2]
d = np.load(ini)
J, Kw, Nt, Ns, iters = [int(v) for v in sys.argv[3:8]]
tmin = float(sys.argv[8]); gauge = int(sys.argv[9]); alpha = float(sys.argv[10])
opt = lambda k, dflt, f=float: f(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else dflt
se = opt('--se', float(d['se']) if 'se' in d.files else 1.0)
gam = float(d['gam']) if 'gam' in d.files else 0.0
if gam != 0.0: raise SystemExit('gam != 0 is not supported')
M = opt('--M', int(d['M']) if 'M' in d.files else 3, int)
beta = opt('--beta', float(d['beta']) if 'beta' in d.files else 3.0)
if 'm' in d.files and 'M' not in d.files and int(d['m']) != 3: raise SystemExit('init is a model.py state with m != 3: its t variable differs')
FIXB = '--fixbeta' in sys.argv
fixa0 = opt('--fixa0', None)
hb = opt('--hb', 1e-5); maxdb = opt('--maxdb', 0.02)
NMIN = '--nmin' in sys.argv; N2MODE = '--n2' in sys.argv or NMIN
BCURV = '--betacurv' in sys.argv
print('rows:', 'R/min(N,N2)' if NMIN else ('R/N2' if N2MODE else 'R/N'), ' beta', beta, 'fixed' if FIXB else 'free', ' M', M, flush=True)
if '--core' in sys.argv:
    core = [(int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3]), float(sys.argv[i_ + 4])) for i_, a_ in enumerate(sys.argv) if a_ == '--core']
elif 'core' in d.files: core = as_patches(d['core'])
else: core = []
mod = ModelCoreFB(J, Kw, core, beta=beta, M=M, alpha=alpha, se=se, gam=gam)
nbo = mod.nbo
J0, K0 = int(d['J']), int(d['Kw'])
c = np.zeros((J + 1, Kw + 1)); c0 = d['c'][:(J0 + 1) * (K0 + 1)].reshape(J0 + 1, K0 + 1)
c[:min(J, J0) + 1, :min(Kw, K0) + 1] = c0[:min(J, J0) + 1, :min(Kw, K0) + 1]
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
c = np.concatenate([c.ravel()] + parts); a0 = float(d['a0']) if fixa0 is None else fixa0
if core: print('core patches', core, ': %d extra unknowns' % mod.nbc, flush=True)

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

x0, e0 = grid(Nt, Ns, tmin, beta)          # fixed collocation points in (x, eta), kept for every beta
if '--inner' in sys.argv:
    i_ = sys.argv.index('--inner'); nri, nti, rmi, rma = int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3]), float(sys.argv[i_ + 4])
    rho = np.logspace(np.log10(rmi), np.log10(rma), nri); th = 0.5 * np.pi * (0.5 * (1 - np.cos(np.pi * (np.arange(nti) + 0.5) / nti)))
    Rr, Th = np.meshgrid(rho, th, indexing='ij')
    x0 = torch.cat([x0, torch.tensor((Rr * np.cos(Th)).ravel())]); e0 = torch.cat([e0, torch.tensor((Rr * np.sin(Th)).ravel())])
    print('inner: %d extra points, rho %g .. %g' % (nri * nti, rmi, rma), flush=True)
FARW = None; FARC = {}
if '--farrows' in sys.argv:
    from farrows import FarRows, cheb_w
    if alpha <= 0: raise SystemExit('--farrows needs alpha > 0')
    i_ = sys.argv.index('--farrows'); Nwf, Wf = int(sys.argv[i_ + 1]), float(sys.argv[i_ + 2]); FARW = cheb_w(Nwf)
    print('farrows: %d section points, weight %g' % (Nwf, Wf), flush=True)
def far_obj(b):
    if b not in FARC:
        if len(FARC) > 8: FARC.clear()
        FARC[b] = FarRows(J, Kw, alpha, se, FARW, beta=b)
    return FARC[b]
xg = torch.tensor([1.0], dtype=DT); eg = torch.tensor([0.0], dtype=DT)
ia11 = monos(2)[1][(1, 1)]
def bg_row(b):
    mod.set_beta(b); return mod.basis_matrix(xg, eg, p=2)[ia11, 0].numpy()
def gjet(c, b):
    mod.set_beta(b); return mod.g_jet(c, x0, e0)
Bg = bg_row(beta); Bm = mod.basis_matrix(x0, e0)
print('points', x0.shape[0], 'unknowns', mod.nb + 1 + (0 if FIXB else 1), flush=True)
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
    if Nlag is not None: Nn = Nlag['N']
    elif NMIN: Nn = torch.minimum(N2, Fd['N'])
    elif N2MODE: Nn = N2
    else: Nn = Fd['N']
    res = F['R'] / Nn
    out = dict(res=res.detach().numpy(), N=dict(N=Nn), A=Fd['A'].numpy(), rN=(Fd['R'] / Fd['N']).numpy(), rN2=(Fd['R'] / N2).numpy())
    if need_jac:
        gG, ga = torch.autograd.grad(res.sum(), [Gc, a0t])
        out['Jc'] = torch.einsum('mi,min->in', gG, Bm_).numpy()
        out['Ja'] = (-(Fd['Thx']) / a0 / Nn).numpy()
    if FARW is not None:
        ctf = torch.tensor(c[:nbo]).requires_grad_(need_jac); af = torch.tensor(a0, dtype=DT, requires_grad=need_jac)
        Z = far_obj(b).terms(ctf, af)
        N20 = Z.detach().abs().sum(0) if Nlag is None else Nlag['N20']
        q = Z.sum(0) / N20
        out['far'] = Wf * q.detach().numpy(); out['N']['N20'] = N20; out['qfar'] = (Z.detach().sum(0) / Z.detach().abs().sum(0)).numpy()
        if need_jac:
            Jf = np.zeros((len(q), len(c) + 1))
            for i in range(len(q)):
                gc, ga_ = torch.autograd.grad(q[i], [ctf, af], retain_graph=True)
                Jf[i, :nbo] = Wf * gc.numpy(); Jf[i, len(c)] = Wf * float(ga_)
            out['Jfar'] = Jf
    return out

def full_res(c, a0, Bg_, ev):
    return np.concatenate([ev['res']] + ([ev['far']] if FARW is not None else []) + [[WH * (h00 @ c - 1)]] + ([[WG * (Bg_ @ c - Ag_target)]] if gauge else []))

def beta_cols(c, a0, b, ev):
    """central differences in beta of the data rows (lagged normalizers) and of the gauge row"""
    rp = resid(c, a0, b + hb, Nlag=ev['N'], Gc=gjet(c, b + hb)); Bgp = bg_row(b + hb)
    rm = resid(c, a0, b - hb, Nlag=ev['N'], Gc=gjet(c, b - hb)); Bgm = bg_row(b - hb)
    mod.set_beta(b)
    jb = (rp['res'] - rm['res']) / (2 * hb)
    if FARW is not None: jb = np.concatenate([jb, (rp['far'] - rm['far']) / (2 * hb)])
    return jb, (Bgp @ c - Bgm @ c) / (2 * hb)

def jacobian(c, a0, b, ev, with_beta):
    data = np.hstack([ev['Jc'], ev['Ja'][:, None]])
    if FARW is not None: data = np.vstack([data, ev['Jfar']])
    nz = data.shape[1] + (1 if with_beta else 0)
    if with_beta:
        jb, jg = beta_cols(c, a0, b, ev); data = np.hstack([data, jb[:, None]])
    rows = [data, WH * np.concatenate([h00, np.zeros(nz - len(h00))])[None, :]]
    if gauge:
        g = np.concatenate([Bg, [0.0]] + ([[jg]] if with_beta else [])); rows.append(WG * g[None, :])
    return np.vstack(rows)

def betacurv(c, a0, b, ev, tag):
    r = full_res(c, a0, Bg, ev); Jm = jacobian(c, a0, b, ev, True)
    if fixa0 is not None: Jm[:, len(c)] = 0.0
    A_ = Jm[:, :-1]; jb = Jm[:, -1]
    D = np.linalg.norm(A_, axis=0); D[D == 0] = 1
    U_, s_, _ = np.linalg.svd(A_ / D, full_matrices=False)
    for rc in (1e-10, 1e-12, 1e-14):
        Uk = U_[:, s_ > rc * s_[0]]
        pj = jb - Uk @ (Uk.T @ jb); pr = r - Uk @ (Uk.T @ r); p = float(np.linalg.norm(pj))
        print('betacurv %s rcond %.0e: obj %.4e |J_b| %.4e |P J_b| %.4e db* %+.4e dB %.4e |P r|^2 %.4e' % (tag, rc, r @ r,
              np.linalg.norm(jb), p, -(pj @ pr) / p ** 2, math.sqrt(r @ r) / p, pr @ pr), flush=True)

lam = opt('--lam0', 1e-3); hist = []; t0 = time.time()
ev = resid(c, a0, beta, Bm, need_jac=True)
r = full_res(c, a0, Bg, ev)
print('init obj %.4e maxres %.3e R/N %.3e R/N2 %.3e minA %.3e a0 %.4f beta %.6f' % (r @ r, np.abs(ev['res']).max(), np.abs(ev['rN']).max(),
      np.abs(ev['rN2']).max(), ev['A'].min(), a0, beta), flush=True)
if FARW is not None: print('init far max |C|/N20 %.4e' % np.abs(ev['qfar']).max(), flush=True)
if '--fdcheck' in sys.argv:
    Jm = jacobian(c, a0, beta, ev, not FIXB); rng = np.random.default_rng(0); v = rng.standard_normal(Jm.shape[1]) * 1e-7
    def rr(s):
        cn = c + s * v[:len(c)]; an = a0 + s * v[len(c)]; bn = beta + (0.0 if FIXB else s * v[-1])
        out_ = full_res(cn, an, bg_row(bn), resid(cn, an, bn, Nlag=ev['N'], Gc=gjet(cn, bn))); mod.set_beta(beta); return out_
    fd = (rr(1) - rr(-1)) / 2; an_ = Jm @ v; print('FD check rel', np.abs(fd - an_).max() / np.abs(an_).max(), flush=True)
if BCURV: betacurv(c, a0, beta, ev, 'start')
for itn in range(iters):
    r = full_res(c, a0, Bg, ev); Jm = jacobian(c, a0, beta, ev, not FIXB); obj = float(r @ r)
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
    fr_ = full_res(c, a0, Bg, ev)
    rec = dict(it=itn, obj=float(fr_ @ fr_), maxres=float(np.abs(ev['res']).max()),
               maxRN=float(np.abs(ev['rN']).max()), maxRN2=float(np.abs(ev['rN2']).max()), rms=float(np.sqrt(np.mean(ev['res'] ** 2))),
               a0=a0, beta=beta, minA=float(ev['A'].min()), lam=lam, H00=float(h00 @ c), s_ratio=float(s_[-1] / s_[0]), sec=time.time() - t0,
               maxfar=float(np.abs(ev['qfar']).max()) if FARW is not None else None)
    hist.append(rec)
    if itn % 5 == 0 or itn == iters - 1: print(json.dumps(rec), flush=True)
    np.savez(out, c=c[:nbo], a0=a0, J=J, Kw=Kw, beta=beta, M=M, **(dict(cc=c[nbo:], core=np.array(core, dtype=float).reshape(-1, 4)) if core else {}),
             hist=json.dumps(hist), Nt=Nt, Ns=Ns, tmin=tmin, gauge=gauge, alpha=alpha, se=se, gam=gam,
             l=float(d['l']) if 'l' in d.files else 1.0, family='fbh')
if BCURV: betacurv(c, a0, beta, ev, 'end')
