"""Free-beta GPU solver v2 (2026-10-21; v1 06:17Z (not published), external review fbg_review):
gsolve_gpu.py (authors' generating-function LM, GPU port) with the authors' free-exponent basis (model_fb / model_core_fb, M = 3) and the
exponent beta as an unknown (authors' gsolve_fbc.py design). The beta column of the Jacobian is a finite difference of the FULL residual
vector (grid rows, centre row, gap rows, gauge row) through the basis (outer + core patches), the field formulas, the gap rows
(desing.Desing at the perturbed beta) and the gauge row, at fixed coefficients, fixed a0, fixed collocation points (x, eta) (the beta-3
grid map) and fixed gap-row points (xh, eh, sigma), with the normalizers frozen (the Jacobian is the frozen-weight surrogate of the
adaptive normalized objective, as in all genfn solvers). Default: central difference with step hb; --rich: Richardson extrapolation
(4 D_hb - D_2hb)/3 (truncation O(hb^4)); the two underlying differences are kept for the stability check of the PROJECTED column in
--betacurv (|P(D_hb - D_2hb)| / p). After an accepted step that changes beta the basis matrices (GPU Bm, GPU Bd) and the gauge row are
rebuilt. Infinity rows (farfield_rows, beta = 3 only) are not available: use a collocation edge tmin and --desrows covering (0, tmin)
so that the far region is carried by the desingularized rows (whose binary64 evaluation noise is ~1e-9 instead of ~1e-7 for direct rows
at r > 1e6). Changes v2 (review items): gap-row chart positivity (min A over the gap rows) required at the start and in the acceptance
test; beta lower bound --bmin (default 2.2); if the beta increment is clipped to +-maxdb the (c, a0) step is re-solved with the clipped
beta increment fixed; hist 'dbeta' is the accepted change; the core-exclusion test of the gap rows is rechecked at every new beta;
F* = |P r + P J_b db*|^2 (no cancellation); p = 0 reported as non-identifiable.
Usage: python3 gsolve_fbg.py init.npz out.npz J Kw Nt Ns iters tmin gauge alpha [--beta b0] [--freebeta] [--fixa0 v] [--core Jc Kc Rc Lc]*
       [--inner nri nti rmin rmax] [--sedge] [--desrows Ntd Nsd Wd] [--nmin|--n2] [--lam0 l] [--lammin l] [--hb h] [--rich] [--maxdb d] [--bmin b] [--betacurv]
       [--a0curv] [--btarget b] [--fdcheck] [--print-every n] [--save-every n] [--chunk n] [--maxsec s] [--bm-cpu]"""
import sys, math, time, json, numpy as np, torch
torch.set_num_threads(1)
import jets
if '--cpu' in sys.argv: jets.DEV = torch.device('cpu')
DEV = jets.DEV
import jets3; jets3.DEV3 = DEV
from jets import Jet, monos, DT
from model import fields, ts_to_xeta
from model_fb import ModelFB
from model_core import as_patches
from model_core_fb import ModelCoreFB
ini, out = sys.argv[1], sys.argv[2]
d = np.load(ini)
def opt(name, default, typ=float):
    return typ(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default
J = int(sys.argv[3]) if len(sys.argv) > 3 else int(d['J'])
Kw = int(sys.argv[4]) if len(sys.argv) > 4 else int(d['Kw'])
Nt = int(sys.argv[5]) if len(sys.argv) > 5 else 2 * J + 8
Ns = int(sys.argv[6]) if len(sys.argv) > 6 else 2 * Kw + 8
iters = int(sys.argv[7]) if len(sys.argv) > 7 else 30
tmin = float(sys.argv[8]) if len(sys.argv) > 8 else 0.01
gauge = int(sys.argv[9]) if len(sys.argv) > 9 else 1
alpha = float(sys.argv[10]) if len(sys.argv) > 10 and not sys.argv[10].startswith('--') else (float(d['alpha']) if 'alpha' in d.files else 0.0)
se = opt('--se', float(d['se']) if 'se' in d.files else 1.0)
gam = float(d['gam']) if 'gam' in d.files else 0.0
if gam != 0.0: raise SystemExit('gam != 0 is not supported by the free-exponent basis')
if 'M' in d.files and int(d['M']) != 3: raise SystemExit('init has M != 3')
m_ = int(d['m']) if 'm' in d.files else 3
if m_ != 3 and 'beta' not in d.files: raise SystemExit('init is a model.py state with m != 3: its t variable differs')
print_every = opt('--print-every', 10, int); save_every = opt('--save-every', 1, int)
chunk = opt('--chunk', 2048, int); maxsec = opt('--maxsec', 1e12)
bm_cpu = '--bm-cpu' in sys.argv
beta = opt('--beta', float(d['beta']) if 'beta' in d.files else 3.0)
FREEB = '--freebeta' in sys.argv and '--fixbeta' not in sys.argv
hb = opt('--hb', 1e-5); maxdb = opt('--maxdb', 0.02); bmin = opt('--bmin', 2.2); RICH = '--rich' in sys.argv; lammin = opt('--lammin', 1e-12)
BT = opt('--btarget', None) if '--btarget' in sys.argv else None   # transport mode: move beta toward BT by at most maxdb per iteration, re-solving the (c, a0) step with that beta increment fixed (continuation without the reinterpretation shock); beta column needed while beta != BT   # damping floor (referee: 1e-12 exceeds the projected beta curvature ~1e-13)
BCURV = '--betacurv' in sys.argv
NMIN = '--nmin' in sys.argv; N2MODE = '--n2' in sys.argv or NMIN
print('rows:', 'R/min(N,N2)' if NMIN else ('R/N2' if N2MODE else 'R/N'), ' beta %.6f' % beta, ('FREE (hb %g%s, maxdb %g, bmin %g)' % (hb, ', Richardson' if RICH else '', maxdb, bmin)) if FREEB else ('transport to %.6f (steps <= %g)' % (BT, maxdb) if BT is not None else 'fixed'), ' M 3  (free-exponent basis)', flush=True)
if '--core' in sys.argv:
    core = [(int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3]), float(sys.argv[i_ + 4])) for i_, a_ in enumerate(sys.argv) if a_ == '--core']
elif 'core' in d.files: core = as_patches(d['core'])
else: core = []
mod = ModelCoreFB(J, Kw, core, beta=beta, M=3, alpha=alpha, se=se, gam=gam) if core else ModelFB(J, Kw, beta=beta, M=3, alpha=alpha, se=se, gam=gam)
nbo = (J + 1) * (Kw + 1)
if core: print('core patches', core, ': %d extra unknowns' % mod.nbc, flush=True)
J0, K0 = int(d['J']), int(d['Kw'])
c = np.zeros((J + 1, Kw + 1)); c0 = d['c'][:(J0 + 1) * (K0 + 1)].reshape(J0 + 1, K0 + 1)
c[:min(J, J0) + 1, :min(Kw, K0) + 1] = c0[:min(J, J0) + 1, :min(Kw, K0) + 1]
c = c.ravel()
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
c = torch.tensor(c, dtype=DT, device=DEV); a0 = float(d['a0'])
fixa0 = None
if '--fixa0' in sys.argv:
    fixa0 = float(sys.argv[sys.argv.index('--fixa0') + 1]); a0 = fixa0
if a0 == 0.0: raise SystemExit('a0 = 0 is not admissible (the a0 columns divide by a0)')

def t_of_tau(tau, alpha):
    if alpha <= 0: return tau
    z = (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1)
    return 1 - z

def grid(Nt, Ns, tmin, shift=0.0):
    """the beta-3 (t, s) collocation grid of gsolve_gpu.py (m = 3 map), kept for every beta (same rows as the fixed-beta runs)"""
    it = (np.arange(Nt) + 0.5 + shift) / Nt; is_ = (np.arange(Ns) + 0.5 + shift) / Ns
    tau = 0.5 * (1 - np.cos(np.pi * it))
    t = t_of_tau(tau, alpha)
    t = tmin + (1 - tmin) * t
    s = 0.5 * (1 - np.cos(np.pi * is_))
    if '--sedge' in sys.argv:    # near-axis edge columns as in gsolve_gpu.py
        se_ = np.array([1e-6, 1e-5, 1e-4, 3e-4, 1e-3]); s = np.concatenate([s, se_, 1 - se_])
    T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
    x, eta = ts_to_xeta(T, S, 3, se)
    keep = (x > 1e-12) & (eta > 1e-12)
    return torch.tensor(x[keep], dtype=DT, device=DEV), torch.tensor(eta[keep], dtype=DT, device=DEV)

x0, e0 = grid(Nt, Ns, tmin)
if '--inner' in sys.argv:
    i_ = sys.argv.index('--inner'); nri, nti, rmi, rma = int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3]), float(sys.argv[i_ + 4])
    rho = np.logspace(np.log10(rmi), np.log10(rma), nri); th = 0.5 * np.pi * (0.5 * (1 - np.cos(np.pi * (np.arange(nti) + 0.5) / nti)))
    Rr, Th = np.meshgrid(rho, th, indexing='ij')
    x0 = torch.cat([x0, torch.tensor((Rr * np.cos(Th)).ravel(), dtype=DT, device=DEV)]); e0 = torch.cat([e0, torch.tensor((Rr * np.sin(Th)).ravel(), dtype=DT, device=DEV)])
    print('inner: %d extra points, rho %g .. %g' % (nri * nti, rmi, rma), flush=True)
N = x0.shape[0]
wts = torch.ones_like(x0)

class BmCPU:
    def __init__(self, blocks):
        self.blocks = blocks; self.shape = (blocks[0].shape[0], sum(b.shape[1] for b in blocks), blocks[0].shape[2]); self.device = torch.device('cpu')
        self.offsets = [0]
        for b in blocks: self.offsets.append(self.offsets[-1] + b.shape[1])
    def numel(self): return self.shape[0] * self.shape[1] * self.shape[2]

def basis_matrix_chunked(x, e, p=4, cpu=False):
    nmon = (p + 1) * (p + 2) // 2
    if cpu:
        blocks = []
        for i in range(0, x.shape[0], chunk):
            blk = mod.basis_matrix(x[i:i + chunk], e[i:i + chunk], p)
            pinned = torch.empty(blk.shape, dtype=DT, device='cpu', pin_memory=True); pinned.copy_(blk)
            blocks.append(pinned); del blk
        torch.cuda.empty_cache()
        return BmCPU(blocks)
    B = torch.empty(nmon, x.shape[0], mod.nb, dtype=DT, device=DEV)
    for i in range(0, x.shape[0], chunk):
        B[:, i:i + chunk, :] = mod.basis_matrix(x[i:i + chunk], e[i:i + chunk], p)
    return B

def bm_matvec(c):
    if not bm_cpu: return Bm @ c
    out = torch.empty(Bm.shape[0], Bm.shape[1], dtype=DT, device=DEV)
    for b, i in zip(Bm.blocks, Bm.offsets):
        out[:, i:i + b.shape[1]] = b.to(DEV, non_blocking=True) @ c
    return out

def bm_jac(gG):
    if not bm_cpu: return torch.einsum('mi,min->in', gG, Bm)
    out = torch.empty(Bm.shape[1], Bm.shape[2], dtype=DT, device=DEV)
    for b, i in zip(Bm.blocks, Bm.offsets):
        out[i:i + b.shape[1]] = torch.einsum('mi,min->in', gG[:, i:i + b.shape[1]], b.to(DEV, non_blocking=True))
    return out

def gjet(cvec, b):
    """Taylor jets (15, N) of G at the collocation points for coefficients cvec and exponent b, without the basis matrix
    (device-safe version of ModelCoreFB.g_jet: outer part by ModelFB.g_jet, core part by the patch jets); leaves mod at beta b"""
    mod.set_beta(b)
    with torch.no_grad():
        G = ModelFB.g_jet(mod, cvec[:nbo], x0, e0)
        if core:
            for i in range(0, N, chunk):
                Bc = torch.stack([B.c for B in mod.core_jets(x0[i:i + chunk], e0[i:i + chunk], 4)], -1)
                G[:, i:i + chunk] = G[:, i:i + chunk] + Bc @ cvec[nbo:]
                del Bc
    return G

def bg_row(b):
    mod.set_beta(b); return mod.basis_matrix(xg, eg, p=2)[monos(2)[1][(1, 1)], 0]

t00 = time.time()
if bm_cpu and '--chunk' not in sys.argv:
    chunk = int((2 ** 29) // (15 * mod.nb * 8)); print('bm-cpu: chunk %d points (%.1f MB pinned blocks)' % (chunk, 15 * chunk * mod.nb * 8 / 1e6), flush=True)
Bm = basis_matrix_chunked(x0, e0, cpu=bm_cpu)
print('points', N, 'unknowns', mod.nb + 1 + (1 if FREEB else 0), 'device', str(DEV), 'Bm GB %.2f' % (Bm.numel() * 8 / 1e9), 'Bm on', str(Bm.device), 'basis time %.1fs' % (time.time() - t00), flush=True)
DES = None
def core_margin(b):
    """min over the gap rows of (x^2 + eta^2)/max Lc^2 in unscaled coordinates at exponent b (the patches are dropped there: need > 700)"""
    if not core: return float('inf')
    mb = b / (b - 2); lamd = sgd ** (-b); rrd = (xhd * lamd) ** 2 + (ehd * se * lamd ** (1 / mb)) ** 2
    return float((rrd / max(q[3] for q in core) ** 2).min())
if '--desrows' in sys.argv:
    from desing import Desing
    i_ = sys.argv.index('--desrows'); Ntd, Nsd, Wd = int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3])
    DES = Desing(J, Kw, c[:nbo].cpu().numpy(), a0, beta=beta, M=3, alpha=alpha, se=se, gam=gam)
    td = tmin * 0.5 * (1 - np.cos(np.pi * (np.arange(Ntd) + 0.5) / Ntd)); sd = 0.5 * (1 - np.cos(np.pi * (np.arange(Nsd) + 0.5) / Nsd))
    TD, SD = [a.ravel() for a in np.meshgrid(td, sd, indexing='ij')]
    xhd, ehd, sgd, _ = DES.points(TD, SD)       # fixed for every beta
    if core_margin(beta) < 700 or core_margin(max(bmin, beta - 0.3)) < 700: raise SystemExit('desrows too close to the core (margin %.3g at beta, %.3g at beta - 0.3)' % (core_margin(beta), core_margin(max(bmin, beta - 0.3))))
    tB = time.time(); Bd = DES.basis_matrix(xhd, ehd, sgd).contiguous()
    print('desrows: %d points, t %.3e .. %.3e, weight %g (Bd %.2f GB on %s, %.1fs; core margin %.2e)' % (len(TD), td[0], td[-1], Wd, Bd.numel() * 8 / 1e9, str(Bd.device), time.time() - tB, core_margin(beta)), flush=True)
h00 = torch.tensor(mod.h00_row(), dtype=DT, device=DEV)
xg = torch.tensor([1.0], dtype=DT, device=DEV); eg = torch.tensor([0.0], dtype=DT, device=DEV)
Bg = bg_row(beta)
Ag_target = float(Bg @ c)
WH, WG = 1e4, 1e2

def lm_step_qr(Je, r, lam):
    nb1 = Je.shape[1]
    A = torch.cat([Je, math.sqrt(lam) * torch.eye(nb1, dtype=DT, device=Je.device)], 0)
    b = torch.cat([-r, torch.zeros(nb1, dtype=DT, device=Je.device)])
    return torch.linalg.lstsq(A, b[:, None], driver='gels' if Je.is_cuda else 'gelsd').solution[:, 0]

def evaluate(c, a0, b, need_jac=True, Nlag=None, Gc=None, Gd=None):
    """rows at exponent b; Gc / Gd: precomputed jets (for evaluations at a changed beta where the basis matrices are not rebuilt)"""
    Gc = (bm_matvec(c) if Gc is None else Gc).detach().requires_grad_(need_jac)
    a0t = torch.tensor(a0, dtype=DT, device=DEV, requires_grad=need_jac)
    F = fields(Gc, x0, e0, a0t, b)
    Nlag_grid = Nlag['grid'] if isinstance(Nlag, dict) else Nlag
    Fd = {k: v.detach() for k, v in F.items()}
    N2 = (Fd['U1'] * Fd['Ox']).abs() + (Fd['U2'] * Fd['Oy']).abs() + (b * (x0 * Fd['Ox'] + Fd['y'] * Fd['Oy']) + Fd['Om']).abs() + Fd['Thx'].abs()
    if Nlag_grid is not None: Nn = Nlag_grid
    elif NMIN: Nn = torch.minimum(N2, Fd['N'])
    elif N2MODE: Nn = N2
    else: Nn = Fd['N']
    res = F['R'] / Nn * wts
    out = dict(res=res.detach(), N=dict(grid=Nn), A=Fd['A'], y=Fd['y'], RN=(Fd['R'] / Fd['N']), RN2=(Fd['R'] / N2))
    if need_jac:
        gG, ga = torch.autograd.grad(res.sum(), [Gc, a0t])
        Jc = bm_jac(gG)
        Ja = (-(Fd['Thx']) / a0t.detach() / Nn)
        out['J'] = torch.cat([Jc, (Ja * wts)[:, None]], 1)
    if DES is not None:
        N2d_lag = Nlag['des'] if isinstance(Nlag, dict) and 'des' in Nlag else None
        Gd = ((Bd @ c[:nbo].detach()) if Gd is None else Gd).detach().requires_grad_(need_jac); ad = torch.tensor(a0, dtype=DT, device=DEV, requires_grad=need_jac)
        E3 = DES.fields3(Gd, xhd, sgd, ad)       # DES must be at exponent b (caller's responsibility)
        N2d = E3['N2b'].detach() if N2d_lag is None else N2d_lag
        qd = Wd * E3['Rb'] / N2d
        out['res_des'] = qd.detach(); out['maxdes'] = float(E3['rN2'].detach().abs().max()); out['maxdesRN'] = float(E3['rN'].detach().abs().max()); out['Ades_min'] = float(E3['A'].detach().min())
        if need_jac:
            gG, ga_ = torch.autograd.grad(qd.sum(), [Gd, ad])
            Jd = torch.zeros(len(qd), mod.nb + 1, dtype=DT, device=DEV)
            Jd[:, :nbo] = torch.einsum('mi,min->in', gG, Bd)
            Jd[:, -1] = Wd * ((E3['terms'][2].detach() / ad.detach()) / N2d)
            out['J_des'] = Jd
        out['N']['des'] = N2d
    return out

def full_res(c, a0, ev, Bg_=None):
    Bg_ = Bg if Bg_ is None else Bg_
    parts = [ev['res'], (WH * (h00 @ c - 1)).reshape(1)]
    if 'res_des' in ev: parts.append(ev['res_des'])
    if gauge: parts.append((WG * (Bg_ @ c - Ag_target)).reshape(1))
    return torch.cat(parts)
BLOCKS = [('grid', 0, N), ('centre', N, N + 1)] + ([('gap', N + 1, N + 1 + len(TD))] if DES is not None else []) + ([('gauge', -1, None)] if gauge else [])

def full_jac_fixed(ev):
    """Jacobian with respect to (c, a0) (the beta column is appended by jacobian())"""
    rows = [ev['J'], WH * torch.cat([h00, torch.zeros(1, dtype=DT, device=DEV)])[None, :]]
    if 'J_des' in ev: rows.append(ev['J_des'])
    if gauge: rows.append(WG * torch.cat([Bg, torch.zeros(1, dtype=DT, device=DEV)])[None, :])
    return torch.cat(rows, 0)

def res_at_beta(c, a0, bb, Nlag):
    """full residual vector at exponent bb with the normalizers Nlag frozen (basis via jets, no matrix rebuild); the caller restores the exponent"""
    Gc = gjet(c, bb)
    Gd = None
    if DES is not None:
        DES.set_beta(bb); Gd = DES.g_jet(xhd, ehd, sgd, c=c[:nbo].detach().cpu().numpy()).c
    ev = evaluate(c, a0, bb, need_jac=False, Nlag=Nlag, Gc=Gc, Gd=Gd)
    return full_res(c, a0, ev, Bg_=bg_row(bb)), ev

def restore(b):
    mod.set_beta(b)
    if DES is not None: DES.set_beta(b)

def beta_diffs(c, a0, b, ev):
    """central differences D_h (and D_2h when --rich) of the full residual in beta"""
    rp, _ = res_at_beta(c, a0, b + hb, ev['N']); rm, _ = res_at_beta(c, a0, b - hb, ev['N'])
    Dh = (rp - rm) / (2 * hb); D2 = None
    if RICH:
        rp2, _ = res_at_beta(c, a0, b + 2 * hb, ev['N']); rm2, _ = res_at_beta(c, a0, b - 2 * hb, ev['N'])
        D2 = (rp2 - rm2) / (4 * hb)
    restore(b)
    return Dh, D2

def beta_col(c, a0, b, ev):
    Dh, D2 = beta_diffs(c, a0, b, ev)
    return ((4 * Dh - D2) / 3 if RICH else Dh), Dh, D2

def jacobian(c, a0, b, ev, with_beta):
    Jm = full_jac_fixed(ev); extra = None
    if with_beta:
        jb, Dh, D2 = beta_col(c, a0, b, ev); Jm = torch.cat([Jm, jb[:, None]], 1); extra = (Dh, D2)
    return Jm, extra

def rebuild(b):
    """basis matrices and gauge row at a new exponent"""
    global Bm, Bd, Bg
    restore(b)
    del Bm; torch.cuda.empty_cache(); Bm = basis_matrix_chunked(x0, e0, cpu=bm_cpu)
    if DES is not None: del Bd; torch.cuda.empty_cache(); Bd = DES.basis_matrix(xhd, ehd, sgd).contiguous()
    Bg = bg_row(b)

def block_norms(v):
    return ' '.join('%s %.3e' % (nm, float(v[a:bq].norm()) if bq is not None else float(v[a:].norm())) for nm, a, bq in BLOCKS)

def betacurv(c, a0, b, ev, tag):
    r = full_res(c, a0, ev); Jm, extra = jacobian(c, a0, b, ev, True)
    if fixa0 is not None: Jm[:, mod.nb] = 0.0
    A_ = Jm[:, :-1]; jb = Jm[:, -1]
    D = torch.linalg.norm(A_, dim=0); D = torch.where(D == 0, torch.ones_like(D), D)
    try: U_, s_, _ = torch.linalg.svd(A_ / D, full_matrices=False)
    except Exception as e:
        print('betacurv: GPU svd failed (%s), CPU fallback' % str(e)[:50], flush=True); U_, s_, _ = torch.linalg.svd((A_ / D).cpu(), full_matrices=False); U_ = U_.to(DEV); s_ = s_.to(DEV)
    print('betacurv %s: |J_b| %.4e by block: %s' % (tag, float(jb.norm()), block_norms(jb)), flush=True)
    # gradient of the (frozen-normalizer) objective with respect to (c, a0) and the directional derivative in beta at fixed shape (lead 11:03Z):
    gA = A_.T @ r
    rp_, _ = res_at_beta(c, a0, b + hb, None); rm_, _ = res_at_beta(c, a0, b - hb, None); restore(b)      # FRESH normalizers at beta +- hb
    print('betacurv %s: obj %.6e  |grad_(c,a0) obj| (frozen N) %.4e  dObj/dbeta at fixed shape: frozen N (2 J_b.r) %+.4e, fresh N (central FD, h %g) %+.4e' % (
          tag, float(r @ r), float(2 * gA.norm()), float(2 * (jb @ r)), hb, (float(rp_ @ rp_) - float(rm_ @ rm_)) / (2 * hb)), flush=True)
    if extra is not None and extra[1] is not None:
        Dh, D2 = extra; print('betacurv %s: |D_h - D_2h| %.4e by block: %s (unprojected FD stability)' % (tag, float((Dh - D2).norm()), block_norms(Dh - D2)), flush=True)
    for rc in (1e-10, 1e-12, 1e-14):
        Uk = U_[:, s_ > rc * s_[0]]
        P = lambda v: v - Uk @ (Uk.T @ v)
        pj = P(jb); pr = P(r); p = float(pj.norm())
        if p == 0.0:
            print('betacurv %s rcond %.0e: p = 0: beta not identifiable in the linearization' % (tag, rc), flush=True); continue
        dbs = -float(pj @ pr) / p ** 2
        Fs = float((pr + pj * dbs).norm() ** 2)
        line = 'betacurv %s rcond %.0e: obj %.4e |J_b| %.4e |P J_b| %.4e db* %+.4e dB1=sqrt(obj)/p %.4e |P r|^2 %.4e F* %.4e dB2=sqrt(F*)/p %.4e (k %d)' % (tag, rc, float(r @ r),
              float(jb.norm()), p, dbs, math.sqrt(float(r @ r)) / p, float(pr @ pr), Fs, math.sqrt(Fs) / p, int(Uk.shape[1]))
        if extra is not None and extra[1] is not None:
            Dh, D2 = extra; pDh = P(Dh); pD2 = P(D2)
            line += ' | projected FD stability: |P D_h| %.4e |P D_2h| %.4e |P(D_h - D_2h)|/p %.3e' % (float(pDh.norm()), float(pD2.norm()), float((pDh - pD2).norm()) / p)
        print(line, flush=True)
    del U_

def a0curv(c, a0, b, ev, tag):
    """authors' a0curv: the a0 column against the span of the c columns (beta held): p_a = |P J_a|, da* = -(P J_a . P r)/p^2, widths"""
    r = full_res(c, a0, ev); Jm, _ = jacobian(c, a0, b, ev, False)
    A_ = Jm[:, :mod.nb]; ja = Jm[:, mod.nb]
    D = torch.linalg.norm(A_, dim=0); D = torch.where(D == 0, torch.ones_like(D), D)
    try: U_, s_, _ = torch.linalg.svd(A_ / D, full_matrices=False)
    except Exception as e:
        print('a0curv: GPU svd failed (%s), CPU fallback' % str(e)[:50], flush=True); U_, s_, _ = torch.linalg.svd((A_ / D).cpu(), full_matrices=False); U_ = U_.to(DEV); s_ = s_.to(DEV)
    for rc in (1e-10, 1e-12, 1e-14):
        Uk = U_[:, s_ > rc * s_[0]]
        pj = ja - Uk @ (Uk.T @ ja); pr = r - Uk @ (Uk.T @ r); p = float(pj.norm())
        if p == 0.0: print('a0curv %s rcond %.0e: p = 0' % (tag, rc), flush=True); continue
        das = -float(pj @ pr) / p ** 2; Fs = float((pr + pj * das).norm() ** 2)
        print('a0curv %s rcond %.0e: obj %.4e a0 %.4f |J_a| %.4e |P J_a| %.4e da* %+.4e dA1=sqrt(obj)/p %.4e |P r|^2 %.4e F* %.4e dA2=sqrt(F*)/p %.4e (k %d)' % (tag, rc, float(r @ r), a0,
              float(ja.norm()), p, das, math.sqrt(float(r @ r)) / p, float(pr @ pr), Fs, math.sqrt(Fs) / p, int(Uk.shape[1])), flush=True)
    del U_

def reduced2(pb, pa, pr, obj, tag, extra_txt=''):
    """2 x 2 reduced (Schur-complement) Gauss-Newton model q(t) = |P(r + B t)|^2, B = [P J_b, P J_la], t = (dbeta, dlog a0), solved through the thin SVD of
    M = [pb, pa] (external review review 12:16Z: avoid forming G^-1; guard rank deficiency). Prints G, rho, the joint Newton step t* = -M^+ pr, F* = |pr + M t*|^2,
    and three kinds of width (external review): 'alone' sqrt(Q/G_ii) (one coordinate moved, the other held at the joint minimum), 'profile' sqrt(Q (G^-1)_ii)
    (the other coordinate re-optimized), 'eigen' sqrt(Q/lambda) along the unit eigenvectors; each is the displacement from the joint minimum of the
    quadratic model that raises the model objective by Q; Q = obj (current objective) and Q = F* (model minimum) are both printed. rho = cos(pb, pa);
    along the valley dlog a0 / dbeta = -G01 / G11, so rho < 0 means same-sign compensation (beta up, a0 up). All widths are frozen-weight linearized
    quantities, not confidence intervals."""
    M = torch.stack([pb, pa], 1).double(); pr = pr.double()
    nb_, na_ = float(pb.norm()), float(pa.norm())
    if nb_ == 0.0 or na_ == 0.0:
        print('abcurv %s: zero projected column (|P J_b| %.3e, |P J_la| %.3e): parameter not identifiable in the linearization' % (tag, nb_, na_), flush=True); return
    G = (M.T @ M).cpu(); g = (M.T @ pr).cpu(); rho = float(G[0, 1]) / math.sqrt(float(G[0, 0]) * float(G[1, 1]))
    Um, sm, Vm = torch.linalg.svd(M, full_matrices=False); s1, s2 = float(sm[0]), float(sm[1])
    F0 = float(pr @ pr)
    print('abcurv %s: |P J_b| %.4e |P J_la| %.4e rho %+.6f (valley slope dlog a0/dbeta = -G01/G11 %+.4e; -G01/G00 = dbeta/dlog a0 %+.4e)  sing. values of [pb, pa] %.4e %.4e (ratio %.2e)  F0 = |P r|^2 %.4e (obj %.4e)%s' % (
        tag, nb_, na_, rho, -float(G[0, 1]) / float(G[1, 1]), -float(G[0, 1]) / float(G[0, 0]), s1, s2, s2 / s1, F0, obj, extra_txt), flush=True)
    if s2 / s1 < 1e-7:
        print('abcurv %s: [pb, pa] numerically rank 1 (ratio %.2e): soft direction (%+.5f, %+.5f) unresolved (width not finite in the linearization); hard direction (%+.5f, %+.5f) width sqrt(obj)/s1 %.3e' % (
            tag, s2 / s1, float(Vm[1, 0]), float(Vm[1, 1]), float(Vm[0, 0]), float(Vm[0, 1]), math.sqrt(obj) / s1), flush=True); return
    ts = -(Vm.T @ ((Um.T @ pr) / sm)).cpu(); Fs = float((pr + M @ ts.to(M.device)).norm() ** 2)
    Ginv = torch.linalg.inv(G)
    print('abcurv %s: S11 = G00 %.6e S22 = G11 %.6e S12 = G01 %+.6e; projected gradient (pb.pr, pa.pr) %+.6e %+.6e (half-objective gradient; full = 2x)' % (tag, float(G[0, 0]), float(G[1, 1]), float(G[0, 1]), float(g[0]), float(g[1])), flush=True)
    print('abcurv %s: joint Newton step (dbeta*, dlog a0*) %+.4e %+.4e (1-D steps: dbeta %+.4e, dlog a0 %+.4e), model minimum F* %.4e (F0 %.4e)' % (
        tag, float(ts[0]), float(ts[1]), -float(g[0]) / float(G[0, 0]), -float(g[1]) / float(G[1, 1]), Fs, F0), flush=True)
    for Q, nm in ((obj, 'Q = obj'), (Fs, 'Q = F*')):
        if Q <= 0: continue
        print('abcurv %s widths (%s %.4e): alone beta %.3e, log a0 %.3e; profile (other re-optimized) beta %.3e, log a0 %.3e (= alone / sqrt(1 - rho^2) = x %.3f); eigen: lambda %.4e dir (dbeta, dlog a0) (%+.5f, %+.5f) width %.3e [soft]; lambda %.4e dir (%+.5f, %+.5f) width %.3e [hard]' % (
            tag, nm, Q, math.sqrt(Q / float(G[0, 0])), math.sqrt(Q / float(G[1, 1])), math.sqrt(Q * float(Ginv[0, 0])), math.sqrt(Q * float(Ginv[1, 1])), 1 / math.sqrt(1 - rho ** 2),
            s2 ** 2, float(Vm[1, 0]), float(Vm[1, 1]), math.sqrt(Q) / s2, s1 ** 2, float(Vm[0, 0]), float(Vm[0, 1]), math.sqrt(Q) / s1), flush=True)

def abcurv(c, a0, b, ev, tag):
    """lead 2026-10-21T12:04Z (optional item): 2 x 2 frozen-weight linearized curvature of the objective in (beta, log a0) with the shape coefficients
    eliminated (Schur complement of the Gauss-Newton Hessian w.r.t. the c block, restricted to the retained singular directions): P = projector onto the
    complement of the span of the equilibrated c columns with singular value > rcond s_max; pb = P J_b (Richardson FD beta column, --rich), pa = P (a0 J_a)
    (a0 column scaled by a0 so that the coordinate is dlog a0; a0 is NOT zeroed here even if held in the fit). FD sensitivity: the analysis is repeated
    with the plain central difference D_h (no Richardson) and with D_2h in place of the beta column. Formulas reviewed by external review (review abcurv_review,
    2026-10-21T12:16Z): algebra confirmed on a manufactured example; their recommendations (SVD solve, rank guard, F0 / F* / both Q, rho sign) applied."""
    r = full_res(c, a0, ev); Jm, extra = jacobian(c, a0, b, ev, True)
    A_ = Jm[:, :mod.nb]; ja = Jm[:, mod.nb] * a0; jb = Jm[:, -1]
    D = torch.linalg.norm(A_, dim=0); D = torch.where(D == 0, torch.ones_like(D), D)
    try: U_, s_, _ = torch.linalg.svd(A_ / D, full_matrices=False)
    except Exception as e:
        print('abcurv: GPU svd failed (%s), CPU fallback' % str(e)[:50], flush=True); U_, s_, _ = torch.linalg.svd((A_ / D).cpu(), full_matrices=False); U_ = U_.to(DEV); s_ = s_.to(DEV)
    obj = float(r @ r)
    print('abcurv %s: obj %.6e a0 %.4f beta %.6f |J_b| %.4e |J_la| %.4e cos(J_b, J_la) %+.6f  (unprojected)' % (tag, obj, a0, b, float(jb.norm()), float(ja.norm()), float(jb @ ja) / (float(jb.norm()) * float(ja.norm()))), flush=True)
    for rc in (1e-10, 1e-12, 1e-14):
        Uk = U_[:, s_ > rc * s_[0]]
        P = lambda v: v - Uk @ (Uk.T @ v)
        pb = P(jb); pa = P(ja); pr = P(r)
        reduced2(pb, pa, pr, obj, '%s rcond %.0e (k %d, Richardson column)' % (tag, rc, int(Uk.shape[1])))
        if extra is not None and extra[1] is not None and rc == 1e-12:
            Dh, D2 = extra
            for col, nm in ((Dh, 'plain D_h'), (D2, 'D_2h')):
                pbh = P(col); print('abcurv %s rcond %.0e FD sensitivity (%s): |P(col) - P(Richardson)| / |P(Richardson)| %.3e' % (tag, rc, nm, float((pbh - pb).norm()) / float(pb.norm())), flush=True)
                reduced2(pbh, pa, pr, obj, '%s rcond %.0e (k %d, %s)' % (tag, rc, int(Uk.shape[1]), nm))
    del U_

def save(c, a0, b, hist):
    cn_ = c.cpu().numpy()
    np.savez(out, c=cn_[:nbo], a0=a0, J=J, Kw=Kw, m=3, **({} if not core else dict(cc=cn_[nbo:], core=np.array(core, dtype=float).reshape(-1, 4))),
             beta=b, hist=json.dumps(hist), Nt=Nt, Ns=Ns, tmin=tmin, gauge=gauge, alpha=alpha, se=se, gam=gam, l=float(d['l']) if 'l' in d else 1.0,
             gpu_port=1, nmin=int(NMIN), n2=int(N2MODE), infrow=0, desrows=np.array([Ntd, Nsd, Wd]) if DES is not None else np.zeros(0), M=3, fb=1, freebeta=int(FREEB), hb=hb, rich=int(RICH), init=ini)

lam = opt('--lam0', 1e-3)
hist = []
t0 = time.time()
ev = evaluate(c, a0, beta)
r = full_res(c, a0, ev)
if ev.get('Ades_min', 1.0) <= 0: raise SystemExit('initial state: chart not positive on the gap rows (min A %.3e)' % ev['Ades_min'])
print('init obj %.4e maxres %.3e R/N %.3e R/N2 %.3e rms %.3e minA %.3e a0 %.4f beta %.6f%s' % (float(r @ r), float(ev['res'].abs().max()), float(ev['RN'].abs().max()), float(ev['RN2'].abs().max()),
      float(torch.sqrt(torch.mean(ev['res']**2))), float(ev['A'].min()), a0, beta, ((' desrows max R/N2 %.3e R/N %.3e minA %.3e' % (ev['maxdes'], ev['maxdesRN'], ev['Ades_min'])) if 'maxdes' in ev else '')), flush=True)
if '--fdcheck' in sys.argv:
    Jm, extra = jacobian(c, a0, beta, ev, FREEB); rng = np.random.default_rng(0); v = torch.tensor(rng.standard_normal(Jm.shape[1]) * 1e-7, dtype=DT, device=DEV)
    for scale in (1.0, 0.1):
        vv = v * scale
        def rs(sgn):
            cn = c + sgn * vv[:mod.nb]; an = a0 + sgn * float(vv[mod.nb]); bn = beta + (sgn * float(vv[-1]) if FREEB else 0.0)
            rr_, _ = res_at_beta(cn, an, bn, ev['N']); return rr_
        fd = (rs(1) - rs(-1)) / 2; an_ = Jm @ vv; restore(beta)
        bad = int((fd - an_).abs().argmax())
        print('FD check (h scale %g): rel %.3e  (|Jv| %.3e, worst row %d of %d: fd %.3e an %.3e)' % (scale, float((fd - an_).abs().max() / an_.abs().max()), float(an_.norm()), bad, len(fd), float(fd[bad]), float(an_[bad])), flush=True)
    # cached (matrix) residual path vs the jet path at the same beta (external review fbg_review item 2)
    rj, _ = res_at_beta(c, a0, beta, ev['N']); restore(beta); r0 = full_res(c, a0, ev)
    print('matrix path vs jet path at the same beta: max |diff| %.3e, by block: %s (row values: max %.3e)' % (float((rj - r0).abs().max()), block_norms(rj - r0), float(r0.abs().max())), flush=True)
    if FREEB:
        for h_ in (10 * hb, hb, hb / 10):
            rp, _ = res_at_beta(c, a0, beta + h_, ev['N']); rm, _ = res_at_beta(c, a0, beta - h_, ev['N']); restore(beta)
            Dh_ = (rp - rm) / (2 * h_); print('beta column, central difference h %.1e: |D_h| %.6e by block: %s' % (h_, float(Dh_.norm()), block_norms(Dh_)), flush=True)
if BCURV: betacurv(c, a0, beta, ev, 'start')
if '--a0curv' in sys.argv: a0curv(c, a0, beta, ev, 'start')
if '--abcurv' in sys.argv: abcurv(c, a0, beta, ev, 'start')
for itn in range(iters):
    r = full_res(c, a0, ev); obj = float(r @ r)
    moving = FREEB or (BT is not None and abs(BT - beta) > 1e-14)
    tA = time.time(); Jm, extra = jacobian(c, a0, beta, ev, moving); t_jac = time.time() - tA
    if fixa0 is not None: Jm[:, mod.nb] = 0.0
    D = torch.linalg.norm(Jm, dim=0); D = torch.where(D == 0, torch.ones_like(D), D)
    Je = Jm / D
    if itn % 50 == 0:
        try: s_ = torch.linalg.svdvals(Je)
        except Exception as e: print('svdvals failed:', str(e)[:80], flush=True); s_ = torch.tensor([1.0, 0.0], dtype=DT, device=DEV)
    tA = time.time(); acc = False; clipped = False
    for trial in range(12):
        step = lm_step_qr(Je, r, lam) / D
        dbeta = 0.0
        if BT is not None and moving:
            dbeta = max(-maxdb, min(maxdb, BT - beta)); clipped = True
            step2 = lm_step_qr(Je[:, :-1], r + Jm[:, -1] * dbeta, lam) / D[:-1]
            step = torch.cat([step2, torch.tensor([dbeta], dtype=DT, device=DEV)])
        elif FREEB:
            dbeta = float(step[-1]); clipped = abs(dbeta) > maxdb or beta + dbeta < bmin
            if clipped:
                # re-solve the (c, a0) step with the clipped beta increment fixed (external review fbg_review item 6)
                dbeta = max(bmin - beta, min(maxdb, max(-maxdb, dbeta)))
                step2 = lm_step_qr(Je[:, :-1], r + Jm[:, -1] * dbeta, lam) / D[:-1]
                step = torch.cat([step2, torch.tensor([dbeta], dtype=DT, device=DEV)])
        cn = c + step[:mod.nb]; an = a0 + (0.0 if fixa0 is not None else float(step[mod.nb])); bn = beta + dbeta
        if bn != beta:
            rn, evn = res_at_beta(cn, an, bn, ev['N']); restore(beta)
        else:
            evn = evaluate(cn, an, beta, need_jac=False, Nlag=ev['N']); rn = full_res(cn, an, evn)
        ok_ = bool(torch.all(torch.isfinite(rn))) and float(evn['A'].min()) > 0 and evn.get('Ades_min', 1.0) > 0
        if ok_ and (float(rn @ rn) < obj or (BT is not None and moving and dbeta != 0.0)):   # transport mode: a forced beta step may raise the objective; accept the re-solved (c, a0) step
            acc = True; break
        lam *= 4
    if not acc:
        print('it %d: no decrease, stop' % itn, flush=True); break
    t_trial = time.time() - tA; tA = time.time()
    if bn != beta:
        if core_margin(bn) < 700: print('it %d: gap rows would be too close to the core at beta %.6f (margin %.3g): stop' % (itn, bn, core_margin(bn)), flush=True); break
        rebuild(bn)
    c, a0, beta = cn, an, bn
    lam = max(lam / 3, lammin)
    ev = evaluate(c, a0, beta)
    torch.cuda.synchronize() if DEV.type == 'cuda' else None; t_eval = time.time() - tA
    rr = ev['res'] / wts
    fr = full_res(c, a0, ev)
    rec = dict(it=itn, obj=float(fr @ fr), maxres=float(rr.abs().max()), maxRN=float(ev['RN'].abs().max()), maxRN2=float(ev['RN2'].abs().max()), maxdes=ev.get('maxdes'), maxdesRN=ev.get('maxdesRN'), Ades_min=ev.get('Ades_min'),
               rms=float(torch.sqrt(torch.mean(rr ** 2))), a0=a0, beta=beta, dbeta=dbeta, clipped=int(clipped), minA=float(ev['A'].min()), lam=lam, H00=float(h00 @ c),
               s_ratio=float(s_[-1] / s_[0]), sec=time.time() - t0, t_jac=round(t_jac, 2), t_trial=round(t_trial, 2), ntrial=trial + 1, t_eval=round(t_eval, 2))
    hist.append(rec)
    if itn % print_every == 0 or itn == iters - 1: print(json.dumps(rec), flush=True)
    if itn % save_every == 0 or itn == iters - 1: save(c, a0, beta, hist)
    if time.time() - t0 > maxsec:
        print('maxsec reached at it %d' % itn, flush=True); break
save(c, a0, beta, hist)
if BCURV: betacurv(c, a0, beta, ev, 'end')
if '--a0curv' in sys.argv: a0curv(c, a0, beta, ev, 'end')
if BT is not None: print('transport end: beta %.6f (target %.6f) grid max %.3e R/N %.3e R/N2 %.3e%s' % (beta, BT, float(ev['res'].abs().max()), float(ev['RN'].abs().max()), float(ev['RN2'].abs().max()), (' gap %.3e' % ev['maxdes']) if 'maxdes' in ev else ''), flush=True)
print('done', flush=True)
