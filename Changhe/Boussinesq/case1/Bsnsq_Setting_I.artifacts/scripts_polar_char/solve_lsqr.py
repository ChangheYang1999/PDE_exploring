"""Matrix-free Levenberg-Marquardt (LSQR inner solver, autograd JVP/VJP) for large resolutions.
Same rows, weights and constraints as solve_gn.py (residuals, c = -2 row, Taylor rows T1, T2, optional gauge N2 / fixed a0),
same basis and inverse (polarlib), but the fields are assembled per mode (tensor structure) and the Jacobian is never formed.
Column equilibration by exact column norms (one JVP per unknown) recomputed every --colnorm-every iterations.
Free beta: the beta column by central differences of the full row vector (basis exponents move with beta)."""
import argparse, json, math, os, sys, time, numpy as np, torch
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *

ap = argparse.ArgumentParser()
ap.add_argument('--beta', type=float, default=3.0); ap.add_argument('--free-beta', action='store_true')
ap.add_argument('--NT', type=int, default=32); ap.add_argument('--NO', type=int, default=32); ap.add_argument('--K', type=int, default=96)
ap.add_argument('--Nr', type=int, default=500); ap.add_argument('--Nth', type=int, default=96); ap.add_argument('--qmax', type=float, default=0.99)
ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--iters', type=int, default=50); ap.add_argument('--lsqr-iters', type=int, default=300)
ap.add_argument('--lam', type=float, default=1e-4, help='initial LM damping relative to the largest column norm')
ap.add_argument('--init', type=str, required=True); ap.add_argument('--out', type=str, required=True)
ap.add_argument('--wc', type=float, default=1e3); ap.add_argument('--wcenter', type=float, default=1.0); ap.add_argument('--eps-th', type=float, default=0.05)
ap.add_argument('--floor', type=float, default=0.03); ap.add_argument('--gauge', type=str, default='none'); ap.add_argument('--fix-a0', type=float, default=None)
ap.add_argument('--colnorm-every', type=int, default=5)
args = ap.parse_args()
device = dev()
logf = open(args.out + '.log', 'a')
def log(s): print(s); logf.write(s + '\n'); logf.flush()
log('# %s args=%s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), vars(args)))
NT, NO, K = args.NT, args.NO, args.K

# ---------------- grid
P0 = Params(args.beta, L=args.L)
j = torch.arange(args.Nr, dtype=DT, device=device); q = args.qmax * 0.5 * (1 - torch.cos(math.pi * (j + 0.5) / args.Nr))
r, _ = torch.sort(P0.u_of_q(q) * P0.L)
xg, wg = np.polynomial.legendre.leggauss(args.Nth); th = torch.tensor((xg + 1) * 0.25 * math.pi, dtype=DT, device=device)
N, M = args.Nr, args.Nth
cs = torch.cos(th)[None, :]; sn = torch.sin(th)[None, :]; R = r[:, None]; X = R * cs; Y = R * sn
mT = torch.tensor([2 * n + 1 for n in range(NT)], dtype=DT, device=device); mO = torch.tensor([2 * n for n in range(1, NO + 1)], dtype=DT, device=device)
sT = torch.sin(mT[:, None] * th[None, :]); cTa = torch.cos(mT[:, None] * th[None, :]); sO = torch.sin(mO[:, None] * th[None, :]); cOa = torch.cos(mO[:, None] * th[None, :])

class Basis:
    """Per-mode radial matrices for a given beta (exponents follow beta)."""
    def __init__(self, beta):
        self.P = Params(beta, L=args.L); P = self.P
        self.HT = torch.stack([radial_basis(P, r, 2 * n + 1, P.gamma_T, K)[0] for n in range(NT)])
        self.dHT = torch.stack([radial_basis(P, r, 2 * n + 1, P.gamma_T, K)[1] for n in range(NT)])
        self.HO = torch.stack([radial_basis(P, r, 2 * n, P.gamma_O, K)[0] for n in range(1, NO + 1)])
        self.dHO = torch.stack([radial_basis(P, r, 2 * n, P.gamma_O, K)[1] for n in range(1, NO + 1)])
        self.PSI, self.DPSI, self.CROW = inverse_matrices(P, r, NO, K)
        # centre functionals
        sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=device)
        dsgn = torch.tensor([(-1.0) ** (k + 1) * k * k * 2.0 for k in range(K)], dtype=DT, device=device)
        self.va0 = sgn / P.L; self.va02 = ((P.gamma_T - 1) / 2 * sgn + P.mu / 2 * dsgn) / P.L ** 3; self.vb = sgn / P.L ** 3
        self.vG2 = sgn / P.L ** 2
        xq, wq = gl_nodes(256, device); qq = 0.5 * (xq + 1); ww = 0.5 * wq; T2, _ = cheb_T_and_dT(qq, K)
        expo = -(P.gamma_O - 4) / P.mu - 2.0 / P.mu - 1.0
        self.vM2 = (1.0 / (2 * P.L ** 2)) * (2.0 / P.mu) * torch.einsum('g,gk->k', ww * (1 - qq) ** expo, T2)
        if args.gauge == 'n2':
            r1 = torch.tensor([P.L], dtype=DT, device=device)
            self.vn2 = torch.stack([(2 * n + 1) * radial_basis(P, r1, 2 * n + 1, P.gamma_T, K)[0][0] / r1[0] for n in range(NT)])  # (NT, K)

def fields(B, cT, cO):
    f = torch.einsum('ank,ak->an', B.HT, cT); df = torch.einsum('ank,ak->an', B.dHT, cT)
    g = torch.einsum('ank,ak->an', B.HO, cO); dg = torch.einsum('ank,ak->an', B.dHO, cO)
    psi = torch.einsum('ank,ak->an', B.PSI, cO); dpsi = torch.einsum('ank,ak->an', B.DPSI, cO)
    Th = f.T @ sT; Thr = df.T @ sT; Thth_r = ((mT[:, None] * f) / r[None, :]).T @ cTa
    Om = g.T @ sO; Omr = dg.T @ sO; Omth_r = ((mO[:, None] * g) / r[None, :]).T @ cOa
    Psir = dpsi.T @ sO; Psith_r = ((mO[:, None] * psi) / r[None, :]).T @ cOa
    Thx = cs * Thr - sn * Thth_r; Thy = sn * Thr + cs * Thth_r; Omx = cs * Omr - sn * Omth_r; Omy = sn * Omr + cs * Omth_r
    U1 = -(sn * Psir + cs * Psith_r); U2 = cs * Psir - sn * Psith_r
    return dict(Th=Th, Thx=Thx, Thy=Thy, Om=Om, Omx=Omx, Omy=Omy, U1=U1, U2=U2)

def centre(B, cT, cO, beta):
    a0 = B.va0 @ cT[0]; a02 = B.va02 @ cT[0]; b = B.vb @ cT[1] if NT > 1 else 0.0 * a0
    b1 = a02 + 3 * b; b2 = a02 - b; G2 = B.vG2 @ cO[0]; M2 = B.vM2 @ cO[1] if NO > 1 else 0.0 * G2
    d1 = -G2 / 6 + M2 / 2; d2 = -G2 / 6 - M2 / 2
    return a0, b1, b2, (2 * beta + 4) * b1 + 3 * a0 * d1, 2 * (beta - 2) * b2 + a0 * d2

def rows(B, cT, cO, beta, wT, wO, a0norm):
    F = fields(B, cT, cO)
    W1 = beta * X + F['U1']; W2 = beta * Y + F['U2']
    RT = W1 * F['Thx'] + W2 * F['Thy'] - (beta - 2) * F['Th']
    RO = W1 * F['Omx'] + W2 * F['Omy'] + F['Om'] - F['Thx']
    cval = B.CROW @ cO[0]
    a0, b1, b2, T1, T2 = centre(B, cT, cO, beta)
    extra = [args.wc * (cval + 2.0), args.wcenter * T1 / a0norm, args.wcenter * T2 / a0norm]
    if args.fix_a0 is not None: extra.append(args.wc * (a0 - args.fix_a0))
    if args.gauge == 'n2': extra.append(args.wc * ((B.vn2 * cT).sum() - 0.5 * a0))
    return torch.cat([(wT * RT).reshape(-1), (wO * RO).reshape(-1), torch.stack(extra)]), F, RT, RO

def normalizers(F, beta):
    W1 = beta * X + F['U1']; W2 = beta * Y + F['U2']
    NTn = (W1 * F['Thx']).abs() + (W2 * F['Thy']).abs() + abs(beta - 2) * F['Th'].abs()
    NOn = (W1 * F['Omx']).abs() + (W2 * F['Omy']).abs() + F['Om'].abs() + F['Thx'].abs()
    return NTn, NOn

def weights(B, F, beta, a0, g0):
    u = R / B.P.L; E = 1 + u * u
    ST = max(abs(a0), 1e-12) * R * E ** (-1.0 / beta) * (sn + args.eps_th)
    SO = max(abs(g0), 1e-12) * R ** 2 * E ** (-1.0 - 0.5 / beta) * (0.5 * torch.sin(2 * th)[None, :] + args.eps_th)
    NTn, NOn = normalizers(F, beta)
    return 1.0 / torch.maximum(NTn, args.floor * ST), 1.0 / torch.maximum(NOn, args.floor * SO)

# ---------------- state
d = np.load(args.init, allow_pickle=True)
def repad(c, Nold, Kold):
    c = c.reshape(Nold, Kold); out = np.zeros((c.shape[0], K)); out[:, :min(Kold, K)] = c[:, :min(Kold, K)]; return out
cT0 = repad(d['cT'], int(d['NT']), int(d['K'])); cO0 = repad(d['cO'], int(d['NO']), int(d['K']))
cT = torch.zeros(NT, K, dtype=DT, device=device); cO = torch.zeros(NO, K, dtype=DT, device=device)
cT[:min(NT, cT0.shape[0])] = torch.tensor(cT0[:NT], dtype=DT, device=device); cO[:min(NO, cO0.shape[0])] = torch.tensor(cO0[:NO], dtype=DT, device=device)
beta = args.beta if not args.free_beta else float(d['beta']) if abs(float(d['beta']) - args.beta) < 0.5 else args.beta
B = Basis(beta)
if abs(float(d['beta']) - beta) > 1e-12:
    log('# re-projecting init from beta %.6f to %.6f' % (float(d['beta']), beta))
    Bo = Basis(float(d['beta'])); Fo = fields(Bo, cT, cO)
    # least squares per mode on radial profiles (exact angular orthogonality)
    for n in range(NT):
        fo = torch.einsum('nk,k->n', Bo.HT[n], cT[n]); cT[n] = torch.linalg.lstsq(B.HT[n], fo[:, None]).solution[:, 0]
    for n in range(NO):
        go = torch.einsum('nk,k->n', Bo.HO[n], cO[n]); cO[n] = torch.linalg.lstsq(B.HO[n], go[:, None]).solution[:, 0]

def pack(cT, cO, beta): return torch.cat([cT.reshape(-1), cO.reshape(-1), torch.tensor([beta], dtype=DT, device=device)])
def unpack(v): return v[:NT * K].reshape(NT, K), v[NT * K:NT * K + NO * K].reshape(NO, K), float(v[-1])
nunk = NT * K + NO * K + (1 if args.free_beta else 0)

def lsqr(matvec, rmatvec, b, lam, iters, ncol):
    """LSQR (Paige-Saunders) for min |A x - b|^2 + lam^2 |x|^2; A given by matvec/rmatvec on vectors of length ncol."""
    x = torch.zeros(ncol, dtype=DT, device=device)
    u = b.clone(); bnorm = u.norm(); u = u / bnorm; v = rmatvec(u); alpha = v.norm(); v = v / alpha
    w = v.clone(); phibar = bnorm; rhobar = alpha
    for it in range(iters):
        u = matvec(v) - alpha * u; bet = u.norm()
        if bet == 0: break
        u = u / bet; v = rmatvec(u) - bet * v; alpha = v.norm(); v = v / alpha
        # damping
        rhobar1 = torch.sqrt(rhobar ** 2 + lam ** 2); c1 = rhobar / rhobar1; s1 = lam / rhobar1; psi_ = s1 * phibar; phibar = c1 * phibar
        rho = torch.sqrt(rhobar1 ** 2 + bet ** 2); c = rhobar1 / rho; s = bet / rho; theta = s * alpha; rhobar = -c * alpha
        phi = c * phibar; phibar = s * phibar
        x = x + (phi / rho) * w; w = v - (theta / rho) * w
    return x

lam_rel = args.lam; hist = []; colnorm = None
for it in range(args.iters):
    t0 = time.time()
    F = fields(B, cT, cO)
    a0, b1, b2, T1v, T2v = centre(B, cT, cO, beta); a0 = float(a0); g0 = 2 * float(B.vG2 @ cO[0]) / B.P.L ** 2
    a0norm = max(abs(a0), 1e-12)
    wT, wO = weights(B, F, beta, a0, g0)
    def resid_vec(v):
        cT_, cO_, beta_ = unpack(torch.cat([v, torch.tensor([beta], dtype=DT, device=device)]) if not args.free_beta else v)
        return rows(B, cT_, cO_, beta_ if args.free_beta else beta, wT, wO, a0norm)[0]
    x0 = torch.cat([cT.reshape(-1), cO.reshape(-1)]) if not args.free_beta else pack(cT, cO, beta)
    rows0, _, RT, RO = rows(B, cT, cO, beta, wT, wO, a0norm)
    obj = float(rows0 @ rows0)
    NTn, NOn = normalizers(F, beta)
    nrmT = float((RT.abs() / (NTn + 1e-300)).max()); nrmO = float((RO.abs() / (NOn + 1e-300)).max())
    # Jacobian products by autograd (coefficients only; beta column by finite differences if free)
    def resid_coef(v):
        cT_ = v[:NT * K].reshape(NT, K); cO_ = v[NT * K:NT * K + NO * K].reshape(NO, K)
        return rows(B, cT_, cO_, beta, wT, wO, a0norm)[0]
    xc = torch.cat([cT.reshape(-1), cO.reshape(-1)])
    _, jvp_fn = torch.func.linearize(resid_coef, xc)
    _, vjp_fn = torch.func.vjp(resid_coef, xc)
    if args.free_beta:
        db = 1e-4
        Bp = Basis(beta + db); Bm = Basis(beta - db)
        bcol = (rows(Bp, cT, cO, beta + db, wT, wO, a0norm)[0] - rows(Bm, cT, cO, beta - db, wT, wO, a0norm)[0]) / (2 * db)
        del Bp, Bm
    if colnorm is None or it % args.colnorm_every == 0:
        # exact column norms via JVPs on unit vectors (batched by chunks)
        cn = torch.zeros(NT * K + NO * K, dtype=DT, device=device)
        eye_chunk = 64
        for s0 in range(0, cn.shape[0], eye_chunk):
            idx = torch.arange(s0, min(s0 + eye_chunk, cn.shape[0]), device=device)
            E_ = torch.zeros(idx.shape[0], cn.shape[0], dtype=DT, device=device); E_[torch.arange(idx.shape[0]), idx] = 1.0
            Jcols = torch.func.vmap(jvp_fn)(E_)
            cn[idx] = Jcols.norm(dim=1)
        cn = torch.where(cn > 0, cn, torch.ones_like(cn))
        if args.free_beta: cn = torch.cat([cn, bcol.norm()[None]])
        colnorm = cn
    cn = colnorm
    def matvec(v):
        out = jvp_fn(v[:NT * K + NO * K] / cn[:NT * K + NO * K])
        if args.free_beta: out = out + bcol * (v[-1] / cn[-1])
        return out
    def rmatvec(u):
        g = vjp_fn(u)[0] / cn[:NT * K + NO * K]
        if args.free_beta: g = torch.cat([g, (bcol @ u)[None] / cn[-1]])
        return g
    accepted = False
    for trial in range(8):
        lam = lam_rel * float(cn.max()) * 0 + lam_rel   # damping in column-scaled coordinates (columns have unit norm)
        delta = lsqr(matvec, rmatvec, -rows0, lam, args.lsqr_iters, nunk) / cn
        cT_n = cT + delta[:NT * K].reshape(NT, K); cO_n = cO + delta[NT * K:NT * K + NO * K].reshape(NO, K)
        beta_n = beta + float(delta[-1]) if args.free_beta else beta
        if args.free_beta and (beta_n < 2.05 or beta_n > 50): lam_rel *= 10; continue
        B_n = Basis(beta_n) if (args.free_beta and abs(beta_n - beta) > 1e-12) else B
        rows_n = rows(B_n, cT_n, cO_n, beta_n, wT, wO, a0norm)[0]; obj_n = float(rows_n @ rows_n)
        if obj_n < obj:
            accepted = True; cT, cO, beta, B = cT_n, cO_n, beta_n, B_n; lam_rel = max(lam_rel / 3, 1e-12); break
        lam_rel *= 10
    F = fields(B, cT, cO); a0p, b1p, b2p, T1p, T2p = centre(B, cT, cO, beta)
    _, _, RTp, ROp = rows(B, cT, cO, beta, wT, wO, a0norm); NTn, NOn = normalizers(F, beta)
    rec = dict(it=it, obj=obj, obj_new=obj_n if accepted else obj, beta=beta, a0=float(a0p), omxy0=2 * float(B.vG2 @ cO[0]) / B.P.L ** 2, c=float(B.CROW @ cO[0]),
               b1=float(b1p), b2=float(b2p), T1=float(T1p), T2=float(T2p), maxnormT=float((RTp.abs() / (NTn + 1e-300)).max()), maxnormO=float((ROp.abs() / (NOn + 1e-300)).max()),
               lam_rel=lam_rel, accepted=accepted, dt=time.time() - t0)
    hist.append(rec); log(json.dumps(rec))
    np.savez(args.out + '.npz', cT=cT.reshape(-1).cpu().numpy(), cO=cO.reshape(-1).cpu().numpy(), beta=beta, L=args.L, NT=NT, NO=NO, K=K, umax=0, qmax=args.qmax,
             Nr=N, Nth=M, gamma_T=B.P.gamma_T, gamma_O=B.P.gamma_O, mu=B.P.mu, hist=json.dumps(hist))
    if not accepted: log('# no decrease; stop'); break
log('# done')
