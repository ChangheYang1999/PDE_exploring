"""GPU port (2026-10-21) of scripts_genfn_cpu/gsolve.py (v2 of 01:40Z with --core patches and --n2/--nmin normalizer modes) (Levenberg-Marquardt solve of the vorticity
equation in the generating-function basis, beta = 2m/(m-1), default m = 3). Same rows, weights, constraints and LM logic as
the original (the CPU gsolve.py at that time, sha256 25dc3dcf...); differences: all tensors live on the CUDA device (torch float64), the
Jacobian and the SVD are formed with torch on the GPU, the basis matrix is built in point chunks, and a few options were
added (--print-every, --save-every, --chunk, --maxsec). Validation against the CPU original: test_port.sh / the numerical report 2c.
Unknowns: c (basis coefficients of G), a0. Rows: R/N (prompt normalizer, lagged) at collocation points of a (t, sigma) grid
in the compact mixed domain; H(0,0) = 1 (heavy, weight 1e4); optional scale gauge A(xg, 0) = A_init(xg, 0) (weight 1e2).
Usage: python3 gsolve_gpu.py init.npz out.npz [J Kw Nt Ns iters tmin gauge(0/1) alpha] [--se v] [--gam v] [--m v] [--fixa0 v]
       [--inner nri nti rmin rmax] [--sedge] [--atarget A --maxda d] [--worig W R0] [--fdcheck] [--print-every n] [--save-every n] [--chunk n] [--maxsec s] [--cpu]"""
import sys, math, time, json, numpy as np, torch
torch.set_num_threads(1)
import jets
if '--cpu' in sys.argv: jets.DEV = torch.device('cpu')
DEV = jets.DEV
from jets import Jet, monos, DT
from model import Model, fields, ts_to_xeta
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
gam = opt('--gam', float(d['gam']) if 'gam' in d.files else 0.0)
m_ = opt('--m', int(d['m']) if 'm' in d.files else 3, int)
print_every = opt('--print-every', 10, int); save_every = opt('--save-every', 1, int)
chunk = opt('--chunk', 2048, int); maxsec = opt('--maxsec', 1e12)
bm_cpu = '--bm-cpu' in sys.argv
infrow = int(sys.argv[sys.argv.index('--infrow') + 1]) if '--infrow' in sys.argv else 0   # number of far-field rows C(v_i)/N20(v_i) (external review; farfield_rows.py)
w_inf = opt('--winf', 1.0)    # keep the basis matrix in pinned CPU memory and stream point chunks to the GPU (for J96K48: 11.9 GB)
svd_driver = opt('--svd-driver', None, str) if '--svd-driver' in sys.argv else None
step_mode = opt('--step', 'svd', str)   # 'svd' (original: one SVD, steps for all lam) or 'qr' (per trial: QR least squares of [Je; sqrt(lam) I] d = [-r; 0], the same damped step)   # None (cusolver default) or 'gesvda' (fast, tall-skinny; validated against the default on the real Jacobian, the numerical report 2c)
if '--irls' in sys.argv: sys.exit('--irls of the original is not implemented in the port')
if m_ != (int(d['m']) if 'm' in d.files else 3): print('WARNING: m differs from the initial state; coefficients are reinterpreted', flush=True)
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam)
core = None     # core patches (model_core.ModelCore): --core Jc Kc Rc Lc (repeatable), or continued from the init key 'core'
from model_core import as_patches, ModelCore
if '--core' in sys.argv:
    core = [(int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3]), float(sys.argv[i_ + 4])) for i_, a_ in enumerate(sys.argv) if a_ == '--core']
elif 'core' in d.files: core = as_patches(d['core'])
if core is not None:
    mod = ModelCore(J, Kw, core, m=m_, alpha=alpha, se=se, gam=gam)
beta_fixed = opt('--beta', None) if '--beta' in sys.argv else None   # fixed exponent != 3: authors' free-exponent basis (model_fb / model_core_fb; M = 3), = the m = 3 basis at beta 3 to rounding
if beta_fixed is not None:
    from model_fb import ModelFB
    from model_core_fb import ModelCoreFB
    mod = ModelCoreFB(J, Kw, core, beta=beta_fixed, M=3, alpha=alpha, se=se, gam=gam) if core is not None else ModelFB(J, Kw, beta=beta_fixed, M=3, alpha=alpha, se=se, gam=gam)
    print('fixed beta %.6f (free-exponent basis, M 3; the (t, s) collocation grid stays the beta-3 grid)' % beta_fixed, flush=True)
NMIN = '--nmin' in sys.argv     # rows R/min(N, N2): targets the larger of the two normalized residuals
N2MODE = '--n2' in sys.argv or NMIN
if N2MODE: print('rows: R/N2 (non-cancelling normalizer)' if not NMIN else 'rows: R/min(N, N2)', flush=True)
if alpha != (float(d['alpha']) if 'alpha' in d.files else 0.0) or se != (float(d['se']) if 'se' in d.files else 1.0) or gam != (float(d['gam']) if 'gam' in d.files else 0.0):
    print('WARNING: alpha/se/gam differ from the initial state; coefficients are reinterpreted', flush=True)
J0, K0 = int(d['J']), int(d['Kw'])
c = np.zeros((J + 1, Kw + 1)); c0 = d['c'].reshape(J0 + 1, K0 + 1)
c[:min(J, J0) + 1, :min(Kw, K0) + 1] = c0[:min(J, J0) + 1, :min(Kw, K0) + 1]
c = c.ravel()
nbo = (J + 1) * (Kw + 1)
if core is not None:
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
c = torch.tensor(c, dtype=DT, device=DEV); a0 = float(d['a0'])
fixa0 = None
if '--fixa0' in sys.argv:
    fixa0 = float(sys.argv[sys.argv.index('--fixa0') + 1]); a0 = fixa0
ATARGET = opt('--atarget', None) if '--atarget' in sys.argv else None; maxda = opt('--maxda', 10.0)   # a0 transport: move a0 toward ATARGET by <= maxda per iteration, re-solving the coefficient step for the fixed a0 increment (09:38Z); then hold a0 there

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
    if '--sedge' in sys.argv:    # extra s columns next to both axes (s -> 1: the y-axis, s -> 0: the x-axis); 07:06Z: the dense R/N2 maximum sits within 0.1 deg of the y-axis at r ~ 0.6, between the Chebyshev nodes
        se_ = np.array([1e-6, 1e-5, 1e-4, 3e-4, 1e-3]); s = np.concatenate([s, se_, 1 - se_])
    T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
    S = S if gam <= 0 else (np.exp(gam * S) - 1) / (np.exp(gam) - 1)
    x, eta = ts_to_xeta(T, S, m_, se)
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
    """basis matrix kept as a list of CONTIGUOUS pinned CPU chunks (15, chunk, nb) so that .to(DEV) is a single DMA per chunk
    (a slice of one big pinned tensor along dim 1 is non-contiguous and forces a slow host-side copy first)"""
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
            pinned = torch.empty(blk.shape, dtype=DT, device='cpu', pin_memory=True); pinned.copy_(blk)   # no unpinned intermediate
            blocks.append(pinned); del blk
        torch.cuda.empty_cache()
        return BmCPU(blocks)
    B = torch.empty(nmon, x.shape[0], mod.nb, dtype=DT, device=DEV)
    for i in range(0, x.shape[0], chunk):
        B[:, i:i + chunk, :] = mod.basis_matrix(x[i:i + chunk], e[i:i + chunk], p)
    return B

def bm_matvec(c):
    """Gc = Bm @ c  (15, N); streamed from CPU if --bm-cpu"""
    if not bm_cpu: return Bm @ c
    out = torch.empty(Bm.shape[0], Bm.shape[1], dtype=DT, device=DEV)
    for b, i in zip(Bm.blocks, Bm.offsets):
        out[:, i:i + b.shape[1]] = b.to(DEV, non_blocking=True) @ c
    return out

def bm_jac(gG):
    """Jc[i, n] = sum_m gG[m, i] Bm[m, i, n]  (N, nb); streamed from CPU if --bm-cpu"""
    if not bm_cpu: return torch.einsum('mi,min->in', gG, Bm)
    out = torch.empty(Bm.shape[1], Bm.shape[2], dtype=DT, device=DEV)
    for b, i in zip(Bm.blocks, Bm.offsets):
        out[i:i + b.shape[1]] = torch.einsum('mi,min->in', gG[:, i:i + b.shape[1]], b.to(DEV, non_blocking=True))
    return out

if '--worig' in sys.argv:      # extra weight W on rows with physical radius < R0 (radius from the initial state)
    Wo, Ro = float(sys.argv[sys.argv.index('--worig') + 1]), float(sys.argv[sys.argv.index('--worig') + 2])
    Gx0 = (basis_matrix_chunked(x0, e0, p=1)[monos(1)[1][(1, 0)]] @ c)
    wts = torch.where(torch.hypot(x0, Gx0) < Ro, torch.full_like(x0, Wo), wts)
    print('worig: weight %g on %d rows with r < %g' % (Wo, int((wts > 1).sum()), Ro), flush=True)
t00 = time.time()
if bm_cpu and '--chunk' not in sys.argv:
    # PyTorch's caching host allocator rounds pinned blocks up to a power of two: choose the chunk so that a block is just under 512 MB
    chunk = int((2 ** 29) // (15 * mod.nb * 8)); print('bm-cpu: chunk %d points (%.1f MB pinned blocks)' % (chunk, 15 * chunk * mod.nb * 8 / 1e6), flush=True)
Bm = basis_matrix_chunked(x0, e0, cpu=bm_cpu)            # (15, N, nb)
print('points', N, 'unknowns', mod.nb + 1, 'device', str(DEV), 'Bm GB %.2f' % (Bm.numel() * 8 / 1e9), 'Bm on', str(Bm.device), 'basis time %.1fs' % (time.time() - t00), flush=True)
FF = None
if infrow > 0 and beta_fixed is not None and abs(beta_fixed - 3.0) > 1e-12:
    print('infinity rows (farfield_rows.py) are beta = 3 only: skipped; use --desrows for the far constraint at beta != 3', flush=True); infrow = 0
if infrow > 0:
    from farfield_rows import FarField
    FF = FarField(J, Kw, alpha, se, infrow, DEV); print('infinity rows: %d angular points v in (0, 1), weight %g' % (infrow, w_inf), flush=True)
DES = None
if '--desrows' in sys.argv:
    # gap rows (authors' gsolve_fbd.py): Ntd x Nsd rows Wd R/N2 (lagged N2) in 0 < t < tmin, evaluated with desing.Desing (scaled variables,
    # no large-radius cancellation; CPU torch, the rows and their Jacobian are moved to the GPU); core patches are dropped there (superexponentially small)
    import jets3; jets3.DEV3 = DEV      # desingularized jets on the GPU (06:45Z: Bd build 0.2 s instead of 42 s; CPU/GPU agree to 2e-9 on R/N2)
    from desing import Desing
    i_ = sys.argv.index('--desrows'); Ntd, Nsd, Wd = int(sys.argv[i_ + 1]), int(sys.argv[i_ + 2]), float(sys.argv[i_ + 3])
    DES = Desing(J, Kw, c[:nbo].cpu().numpy(), a0, beta=mod.beta, M=3, alpha=alpha, se=se, gam=gam)
    td = tmin * 0.5 * (1 - np.cos(np.pi * (np.arange(Ntd) + 0.5) / Ntd)); sd = 0.5 * (1 - np.cos(np.pi * (np.arange(Nsd) + 0.5) / Nsd))
    TD, SD = [a.ravel() for a in np.meshgrid(td, sd, indexing='ij')]
    xhd, ehd, sgd, _ = DES.points(TD, SD)
    if core is not None:
        lamd = sgd ** (-mod.beta); rrd = (xhd * lamd) ** 2 + (ehd * se * lamd ** (1 / DES.m)) ** 2
        if (rrd / max(q[3] for q in core) ** 2 < 700).any(): raise SystemExit('desrows too close to the core')
    tB = time.time(); Bd = DES.basis_matrix(xhd, ehd, sgd).contiguous().to(DEV)       # (n3, Nd, nbo) on the GPU (the CPU einsum of the Jacobian cost 10.6 s/it, 06:27Z)
    print('desrows: %d points, t %.3e .. %.3e, weight %g (Bd %.2f GB on %s, %.1fs)' % (len(TD), td[0], td[-1], Wd, Bd.numel() * 8 / 1e9, str(Bd.device), time.time() - tB), flush=True)
h00 = torch.tensor(mod.h00_row(), dtype=DT, device=DEV)
xg = torch.tensor([1.0], dtype=DT, device=DEV); eg = torch.tensor([0.0], dtype=DT, device=DEV)
Bg = mod.basis_matrix(xg, eg, p=2)[monos(2)[1][(1, 1)], 0]   # A(xg, 0) row
Ag_target = float(Bg @ c)
WH, WG = 1e4, 1e2

def svd_robust(A, driver=None):
    """thin SVD; cusolver's default gesvd occasionally fails to converge on the rank-deficient Jacobian (s_ratio 1e-17):
    try the requested driver, then gesvdj, then the CPU LAPACK gesdd (what the original solver uses)."""
    tried = []
    for drv in ([driver] if driver is not None else [None]) + ['gesvdj']:
        try:
            return torch.linalg.svd(A, full_matrices=False, driver=drv) + (str(drv),)
        except Exception as e:
            tried.append('%s: %s' % (drv, str(e)[:60]))
    U, s, Vh = torch.linalg.svd(A.cpu(), full_matrices=False)
    print('svd fallback to CPU after', tried, flush=True)
    return U.to(A.device), s.to(A.device), Vh.to(A.device), 'cpu'

def lm_step_qr(Je, r, lam):
    """d = -(Je^T Je + lam I)^-1 Je^T r via QR of the augmented matrix (identical to the SVD formula V s/(s^2+lam) U^T r)"""
    nb1 = Je.shape[1]
    A = torch.cat([Je, math.sqrt(lam) * torch.eye(nb1, dtype=DT, device=Je.device)], 0)
    b = torch.cat([-r, torch.zeros(nb1, dtype=DT, device=Je.device)])
    return torch.linalg.lstsq(A, b[:, None], driver='gels' if Je.is_cuda else 'gelsd').solution[:, 0]

def evaluate(c, a0, need_jac=True, Nlag=None):
    Gc = bm_matvec(c).detach().requires_grad_(need_jac)
    a0t = torch.tensor(a0, dtype=DT, device=DEV, requires_grad=need_jac)
    F = fields(Gc, x0, e0, a0t, mod.beta)
    Nlag_grid = Nlag['grid'] if isinstance(Nlag, dict) else Nlag
    if N2MODE:
        # non-cancelling normalizer (lead): |U1 Om_x| + |U2 Om_y| + |beta X.grad Om + Om| + |Theta_x|
        Fd = {k: v.detach() for k, v in F.items()}
        N2 = (Fd['U1'] * Fd['Ox']).abs() + (Fd['U2'] * Fd['Oy']).abs() + (mod.beta * (x0 * Fd['Ox'] + Fd['y'] * Fd['Oy']) + Fd['Om']).abs() + Fd['Thx'].abs()
        if NMIN: N2 = torch.minimum(N2, Fd['N'])
        Nn = N2 if Nlag_grid is None else Nlag_grid
    else:
        Nn = F['N'].detach() if Nlag_grid is None else Nlag_grid
    res = F['R'] / Nn * wts
    out = dict(res=res.detach(), N=Nn, A=F['A'].detach(), y=F['y'].detach(), RN=(F['R'] / F['N']).detach() if N2MODE else None)
    if need_jac:
        gG, ga = torch.autograd.grad(res.sum(), [Gc, a0t])
        # res_i depends on Gc[:, i] only (pointwise), except through a0 (scalar): d res/d a0 = B0/(A N)
        Jc = bm_jac(gG)
        Ja = (-(F['Thx'].detach()) / a0t.detach() / Nn)      # dR/da0 = B0/A = -Thx/a0  (times wts below)
        out['J'] = torch.cat([Jc, (Ja * wts)[:, None]], 1)
    if FF is not None:
        # far-field rows: C(v_i)/N20_lag(v_i); the normalizer N20 is lagged like N (Ninf_lag passed through Nlag as a tuple)
        Ninf_lag = Nlag['inf'] if isinstance(Nlag, dict) else None
        def rows_inf(cvec, a0s):
            Cf, Nf = FF.CN(cvec[:nbo], a0s)
            return w_inf * Cf / (Nf.detach() if Ninf_lag is None else Ninf_lag), Nf
        if need_jac:
            cv = c.detach().clone().requires_grad_(True); av = torch.tensor(a0, dtype=DT, device=DEV, requires_grad=True)
            ri, Nf = rows_inf(cv, av)
            Ji = torch.zeros(ri.shape[0], c.shape[0] + 1, dtype=DT, device=DEV)
            for i in range(ri.shape[0]):
                gc, ga_ = torch.autograd.grad(ri[i], [cv, av], retain_graph=True)
                Ji[i, :-1] = gc; Ji[i, -1] = ga_
            out['J_inf'] = Ji
        else:
            with torch.no_grad(): ri, Nf = rows_inf(c, torch.tensor(a0, dtype=DT, device=DEV))
        out['res_inf'] = ri.detach(); out['Ninf'] = Nf.detach()
        with torch.no_grad(): Cf0, Nf0 = FF.CN(c[:nbo].detach(), torch.tensor(a0, dtype=DT, device=DEV)); out['maxinf'] = float((Cf0 / Nf0).abs().max())
        out['N'] = dict(grid=Nn, inf=(Nf.detach() if Ninf_lag is None else Ninf_lag))
    if DES is not None:
        N2d_lag = Nlag['des'] if isinstance(Nlag, dict) and 'des' in Nlag else None
        Gd = (Bd @ c[:nbo].detach()).detach().requires_grad_(need_jac); ad = torch.tensor(a0, dtype=DT, device=DEV, requires_grad=need_jac)
        E3 = DES.fields3(Gd, xhd, sgd, ad)
        N2d = E3['N2b'].detach() if N2d_lag is None else N2d_lag
        qd = Wd * E3['Rb'] / N2d
        out['res_des'] = qd.detach(); out['maxdes'] = float(E3['rN2'].detach().abs().max()); out['maxdesRN'] = float(E3['rN'].detach().abs().max()); out['Ades_min'] = float(E3['A'].detach().min())
        if need_jac:
            gG, ga_ = torch.autograd.grad(qd.sum(), [Gd, ad])
            Jd = torch.zeros(len(qd), c.shape[0] + 1, dtype=DT, device=DEV)
            Jd[:, :nbo] = torch.einsum('mi,min->in', gG, Bd)
            Jd[:, -1] = Wd * ((E3['terms'][2].detach() / ad.detach()) / N2d)     # a0 enters Rb linearly (a0 se ghat)
            out['J_des'] = Jd
        if not isinstance(out['N'], dict): out['N'] = dict(grid=out['N'])
        out['N']['des'] = N2d
    return out

def full_res(c, a0, ev):
    parts = [ev['res'], (WH * (h00 @ c - 1)).reshape(1)]
    if 'res_inf' in ev: parts.append(ev['res_inf'])
    if 'res_des' in ev: parts.append(ev['res_des'])
    if gauge: parts.append((WG * (Bg @ c - Ag_target)).reshape(1))
    return torch.cat(parts)

def full_jac(ev):
    rows = [ev['J'], WH * torch.cat([h00, torch.zeros(1, dtype=DT, device=DEV)])[None, :]]
    if 'J_inf' in ev: rows.append(ev['J_inf'])
    if 'J_des' in ev: rows.append(ev['J_des'])
    if gauge: rows.append(WG * torch.cat([Bg, torch.zeros(1, dtype=DT, device=DEV)])[None, :])
    return torch.cat(rows, 0)

def save(c, a0, hist):
    cn_ = c.cpu().numpy()
    np.savez(out, c=cn_[:nbo], a0=a0, J=J, Kw=Kw, m=m_, **({} if core is None else dict(cc=cn_[nbo:], core=np.array(core, dtype=float).reshape(-1, 4))),
             beta=mod.beta, hist=json.dumps(hist), Nt=Nt, Ns=Ns, tmin=tmin, gauge=gauge,
             alpha=alpha, se=se, gam=gam, l=float(d['l']) if 'l' in d else 1.0, gpu_port=1, init=ini, nmin=int(NMIN), n2=int(N2MODE), infrow=infrow, winf=w_inf, desrows=np.array([Ntd, Nsd, Wd]) if DES is not None else np.zeros(0), M=3, fb=int(beta_fixed is not None))

lam = opt('--lam0', 1e-3)   # initial damping (use a small value, e.g. 1e-10, when continuing a state that already sits at an LM floor: the x4 growth on rejection cannot recover otherwise)
hist = []
t0 = time.time()
ev = evaluate(c, a0)
r = full_res(c, a0, ev)
print('init obj %.4e maxres %.3e rms %.3e minA %.3e a0 %.4f%s' % (float(r @ r), float(ev['res'].abs().max()), float(torch.sqrt(torch.mean(ev['res']**2))), float(ev['A'].min()), a0, (' max|C/N20| %.3e' % ev['maxinf']) if 'maxinf' in ev else '') + ((' desrows max R/N2 %.3e R/N %.3e' % (ev['maxdes'], ev['maxdesRN'])) if 'maxdes' in ev else ''), flush=True)
if '--fdcheck' in sys.argv:
    Jm = full_jac(ev); rng = np.random.default_rng(0); v = torch.tensor(rng.standard_normal(Jm.shape[1]) * 1e-7, dtype=DT, device=DEV)
    rp = full_res(c + v[:-1], a0 + float(v[-1]), evaluate(c + v[:-1], a0 + float(v[-1]), False, ev['N'])); rm = full_res(c - v[:-1], a0 - float(v[-1]), evaluate(c - v[:-1], a0 - float(v[-1]), False, ev['N']))
    fd = (rp - rm) / 2; an = Jm @ v; print('FD check rel', float((fd - an).abs().max() / an.abs().max()), flush=True)
if '--stalltest' in sys.argv:
    # at the loaded state: for a range of lam, the damped (QR) step, its predicted linear objective and the actual lagged objective
    r = full_res(c, a0, ev); Jm = full_jac(ev); obj0 = float(r @ r)
    if fixa0 is not None: Jm = Jm.clone(); Jm[:, -1] = 0.0
    D = torch.linalg.norm(Jm, dim=0); D = torch.where(D == 0, torch.ones_like(D), D); Je = Jm / D
    g = Jm.T @ r
    print('stalltest: obj %.6e  |J^T r| %.3e  max row |r| %.3e' % (obj0, float(g.norm()), float(r.abs().max())))
    print('   lam        |step|      predicted obj   actual lagged obj   actual/obj0 - 1   minA')
    for lam in [1e-12, 1e-9, 1e-6, 1e-3, 1.0, 1e3, 1e6, 1e9]:
        step = lm_step_qr(Je, r, lam) / D
        cn = c + step[:-1]; an = a0 + (0.0 if fixa0 is not None else float(step[-1]))
        evn = evaluate(cn, an, need_jac=False, Nlag=ev['N']); rn = full_res(cn, an, evn)
        pred = float((r + Jm @ step).norm() ** 2)
        print('   %.0e  %.3e  %.6e  %.6e  %+.3e  %.6f' % (lam, float(step.norm()), pred, float(rn @ rn), float(rn @ rn) / obj0 - 1, float(evn['A'].min())))
    # FD check of the Jacobian along the lam = 1 step direction (lagged N)
    v0 = lm_step_qr(Je, r, 1.0) / D; v0 = v0 / v0.norm()
    torch.manual_seed(1); vr = torch.randn_like(v0); vr[-1] = 0.0 if fixa0 is not None else vr[-1]; vr = vr / vr.norm()
    for name, vv in [('lam=1 step direction', v0), ('random direction', vr)]:
        for h in [1e-4, 1e-5, 1e-6, 1e-7, 1e-8]:
            v = vv * h
            rp = full_res(c + v[:-1], a0 + float(v[-1]), evaluate(c + v[:-1], a0 + float(v[-1]), False, ev['N'])); rm = full_res(c - v[:-1], a0 - float(v[-1]), evaluate(c - v[:-1], a0 - float(v[-1]), False, ev['N']))
            fd = (rp - rm) / 2; an_ = Jm @ v
            print('   FD check, %s, h %.0e: |J v| %.3e  rel err %.3e  (max row |fd - Jv| %.2e at row %d of %d)' % (name, h, float(an_.norm()), float((fd - an_).norm() / an_.norm()), float((fd - an_).abs().max()), int((fd - an_).abs().argmax()), len(fd)))
    sys.exit(0)
if '--svdcheck' in sys.argv:
    # compare LM steps from the default SVD and the gesvda driver on the real equilibrated Jacobian, then exit
    r = full_res(c, a0, ev); Jm = full_jac(ev)
    D = torch.linalg.norm(Jm, dim=0); D = torch.where(D == 0, torch.ones_like(D), D); Je = Jm / D
    res = {}
    for drv in [None, 'gesvda']:
        torch.cuda.synchronize(); tA = time.time()
        U_, s_, Vh, used = svd_robust(Je, drv); torch.cuda.synchronize(); dt = time.time() - tA; print('driver requested', drv, 'used', used)
        g = U_.T @ r
        steps = {lam: -(Vh.T @ (s_ * g / (s_ ** 2 + lam))) / D for lam in [1e-3, 1e-6, 1e-9, 1e-12]}
        res[drv] = (s_, steps, dt, float((U_ * s_ @ Vh - Je).abs().max()))
    s0, st0, dt0, rec0 = res[None]; s1, st1, dt1, rec1 = res['gesvda']
    print('svdcheck: default %.1fs recon %.1e | gesvda %.1fs recon %.1e' % (dt0, rec0, dt1, rec1))
    print('  singular values: s_max %.4e %.4e; number with s > 1e-8 s_max: %d %d; max rel diff over s > 1e-8 s_max: %.2e' % (
        float(s0[0]), float(s1[0]), int((s0 > 1e-8 * s0[0]).sum()), int((s1 > 1e-8 * s1[0]).sum()),
        float(((s0 - s1).abs() / s0)[s0 > 1e-8 * s0[0]].max())))
    # truncated least squares: how much of the residual is reducible with directions above a singular-value threshold
    U0, s0_, Vh0 = svd_robust(Je, None)[:3]; g0 = U0.T @ r
    print('  truncated LS on the equilibrated Jacobian (s_max %.4e, %d columns): threshold s/s_max -> k, |r + J d_k|/|r|, |d_k| (coefficient units), max|d_k|' % (float(s0_[0]), Je.shape[1]))
    for th in [1e-2, 1e-3, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14, 0.0]:
        k = int((s0_ > th * s0_[0]).sum())
        dk = -(Vh0[:k].T @ (g0[:k] / s0_[:k])) / D
        print('    %.0e -> k %5d  resid %.6f  |d| %.3e  max|d| %.3e' % (th, k, float((r + Jm @ dk).norm() / r.norm()), float(dk.norm()), float(dk.abs().max())))
    # projection residual without inverse singular values, and NONLINEAR test of the truncated-SVD steps (lagged normalizer, as the LM)
    print('  nonlinear check of truncated-SVD steps t d_k (lagged N as in the LM trials): columns = t, |r_nonlin|/|r|, predicted |r + t J d_k|/|r|, min A, refreshed-N grid max')
    for th in [1e-8, 1e-10, 1e-12]:
        k = int((s0_ > th * s0_[0]).sum())
        pk = r - U0[:, :k] @ (U0[:, :k].T @ r)
        dk = -(Vh0[:k].T @ (g0[:k] / s0_[:k])) / D
        print('    th %.0e k %d: |p_k|/|r| = %.6f (should equal the LS residual above); d a0 = %.4e, |d c| = %.4e, max|d c| = %.4e' % (th, k, float(pk.norm() / r.norm()), float(dk[-1]), float(dk[:-1].norm()), float(dk[:-1].abs().max())))
        for t in [1.0, 0.3, 0.1, 0.03, 0.01]:
            cn = c + t * dk[:-1]; an = a0 + t * float(dk[-1])
            evn = evaluate(cn, an, need_jac=False, Nlag=ev['N']); rn = full_res(cn, an, evn)
            evf = evaluate(cn, an, need_jac=False); gm = float(evf['res'].abs().max()) if bool(torch.all(torch.isfinite(evf['res']))) else float('nan')
            print('      t %.2f: nonlinear %.6f  linear %.6f  minA %.4f  refreshed grid max %.3e' % (t, float(rn.norm() / r.norm()), float((r + t * (Jm @ dk)).norm() / r.norm()), float(evn['A'].min()), gm))
    for lam in st0:
        d0, d1 = st0[lam], st1[lam]
        torch.cuda.synchronize(); tA = time.time(); dq = lm_step_qr(Je, r, lam) / D; torch.cuda.synchronize(); tq = time.time() - tA
        print('  lam %.0e: |step| %.4e  rel diff of steps %.2e  predicted |r + J d| %.6e %.6e | qr step: rel diff %.2e, |r + J d| %.6e, %.2fs' % (lam, float(d0.norm()), float((d0 - d1).norm() / d0.norm()),
              float((r + Jm @ d0).norm()), float((r + Jm @ d1).norm()), float((dq - d0).norm() / d0.norm()), float((r + Jm @ dq).norm()), tq))
    sys.exit(0)
if '--nullcheck' in sys.argv:
    # near-kernel item (lead 08:43Z (4)): the 10 smallest singular values of the column-scaled Jacobian (all rows; a0 column zeroed if --fixa0) and the
    # projections of the corresponding right singular vectors (mapped back to coefficient space) onto (a) the dilation generator
    # delta G = 2 G - x G_x - eta G_eta (least-squares fit of its value jet by the basis on the collocation points) and (b) the a0 unit vector.
    r = full_res(c, a0, ev); Jm = full_jac(ev)
    if fixa0 is not None: Jm = Jm.clone(); Jm[:, -1] = 0.0
    D = torch.linalg.norm(Jm, dim=0); D = torch.where(D == 0, torch.ones_like(D), D); Je = Jm / D
    U_, s_, Vh = svd_robust(Je, None)[:3]
    L4, ix4 = monos(4); Gc = bm_matvec(c)
    f_dil = 2 * Gc[ix4[(0, 0)]] - x0 * Gc[ix4[(1, 0)]] - e0 * Gc[ix4[(0, 1)]]
    B0 = torch.stack([bm_matvec(torch.eye(c.shape[0], dtype=DT, device=DEV)[k])[ix4[(0, 0)]] for k in range(0)], 0) if False else None
    # value-jet basis matrix (N, nb) by chunks from Bm
    Bv = (Bm[ix4[(0, 0)]] if not bm_cpu else torch.cat([b[ix4[(0, 0)]].to(DEV) for b in Bm.blocks], 0))
    dc = torch.linalg.lstsq(Bv, f_dil[:, None], driver='gels').solution[:, 0]
    fit_err = float((Bv @ dc - f_dil).norm() / f_dil.norm())
    dcu = torch.cat([dc, torch.zeros(1, dtype=DT, device=DEV)]); dcu = dcu / dcu.norm()
    ea = torch.zeros(c.shape[0] + 1, dtype=DT, device=DEV); ea[-1] = 1.0
    print('nullcheck: rows %d, columns %d, s_max %.4e; dilation generator fitted by the basis to rel %.2e (|delta c| %.3e); a0 %s' % (Jm.shape[0], Jm.shape[1], float(s_[0]), fit_err, float(dc.norm()), 'held (column zeroed)' if fixa0 is not None else 'free'))
    print('   k   s_k/s_max     |cos(v_k, dilation)|   |v_k[a0]|   predicted |r + J d|/|r| using the k smallest removed (truncated LS)')
    g0 = U_.T @ r; n = s_.shape[0]
    for k in range(1, 11):
        v = Vh[n - k] / D; v = v / v.norm()
        kk = n - k
        dk = -(Vh[:kk].T @ (g0[:kk] / s_[:kk])) / D
        print('  %2d   %.3e      %.3e             %.3e     %.6f' % (k, float(s_[n - k] / s_[0]), float((v @ dcu).abs()), float(v[-1].abs()), float((r + Jm @ dk).norm() / r.norm())))
    # projection of the dilation generator onto the span of the m smallest right singular vectors (coefficient space, D^-1 metric)
    Vc = (Vh / D[None, :]); Vc = Vc / Vc.norm(dim=1, keepdim=True)
    for m_ in (1, 3, 10, 30, 100):
        W = Vc[n - m_:]; Q, _ = torch.linalg.qr(W.T); print('   dilation generator: fraction of norm inside the span of the %d smallest right singular directions: %.4f' % (m_, float((Q.T @ dcu).norm())))
    print('   10 largest singular values / s_max:', ' '.join('%.3e' % float(s_[k] / s_[0]) for k in range(10)))
    sys.exit(0)
for itn in range(iters):
    r = full_res(c, a0, ev); Jm = full_jac(ev)
    obj = float(r @ r)
    if fixa0 is not None and not (ATARGET is not None and abs(ATARGET - a0) > 1e-12): Jm = Jm.clone(); Jm[:, -1] = 0.0
    D = torch.linalg.norm(Jm, dim=0); D = torch.where(D == 0, torch.ones_like(D), D)
    tA = time.time()
    Je = Jm / D
    if step_mode == 'svd':
        U_, s_, Vh, svd_used = svd_robust(Je, svd_driver)
        g = U_.T @ r
    else:
        svd_used = 'qr'
        if itn % 50 == 0:   # singular spectrum occasionally for the record (s_ratio in the history refers to the last such iteration)
            try: s_ = torch.linalg.svdvals(Je)
            except Exception as e: print('svdvals failed:', str(e)[:80], flush=True)
    torch.cuda.synchronize() if DEV.type == 'cuda' else None; t_svd = time.time() - tA; tA = time.time()
    acc = False
    da_forced = None
    if ATARGET is not None and abs(ATARGET - a0) > 1e-12:
        da_forced = max(-maxda, min(maxda, ATARGET - a0))
    for trial in range(12):
        if da_forced is not None:
            step_c = lm_step_qr(Je[:, :-1], r + Jm[:, -1] * da_forced, lam) / D[:-1]; step = torch.cat([step_c, torch.tensor([da_forced], dtype=DT, device=DEV)])
        else:
            step = (-(Vh.T @ (s_ * g / (s_ ** 2 + lam))) / D) if step_mode == 'svd' else (lm_step_qr(Je, r, lam) / D)
        cn = c + step[:-1]; an = a0 + (0.0 if (fixa0 is not None and da_forced is None) else float(step[-1]))
        evn = evaluate(cn, an, need_jac=False, Nlag=ev['N'])
        rn = full_res(cn, an, evn)
        ok_ = bool(torch.all(torch.isfinite(rn))) and float(evn['A'].min()) > 0 and evn.get('Ades_min', 1.0) > 0   # chart positivity on the grid AND on the gap rows (external review fbg_review)
        if ok_ and (float(rn @ rn) < obj or da_forced is not None):   # a forced a0 step may raise the objective: accept the re-solved coefficient step
            acc = True; break
        lam *= 4
    if not acc:
        print('it %d: no decrease, stop' % itn, flush=True); break
    c, a0 = cn, an
    lam = max(lam / 3, 1e-12)
    t_trial = time.time() - tA; tA = time.time()
    ev = evaluate(c, a0)
    torch.cuda.synchronize() if DEV.type == 'cuda' else None; t_eval = time.time() - tA
    rr = ev['res'] / wts
    fr = full_res(c, a0, ev)
    rec = dict(it=itn, obj=float(fr @ fr), maxres=float(rr.abs().max()), maxRN=(float(ev['RN'].abs().max()) if N2MODE else None), maxinf=ev.get('maxinf'), maxdes=ev.get('maxdes'), maxdesRN=ev.get('maxdesRN'),
               rms=float(torch.sqrt(torch.mean(rr ** 2))), a0=a0, minA=float(ev['A'].min()), lam=lam, H00=float(h00 @ c),
               s_ratio=float(s_[-1] / s_[0]), sec=time.time() - t0, t_svd=round(t_svd, 2), t_trial=round(t_trial, 2), ntrial=trial + 1, t_eval=round(t_eval, 2), svd=svd_used)
    hist.append(rec)
    if itn % print_every == 0 or itn == iters - 1: print(json.dumps(rec), flush=True)
    if itn % save_every == 0 or itn == iters - 1: save(c, a0, hist)
    if time.time() - t0 > maxsec:
        print('maxsec reached at it %d' % itn, flush=True); save(c, a0, hist); break
save(c, a0, hist)
print('done', flush=True)
