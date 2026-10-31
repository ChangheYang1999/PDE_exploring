"""Project an arbitrary velocity field onto the divergence-free spectral basis (linear least squares on the training
grid, weighted by the fixed-gauge scaling), and SPEC 11 v1.5 (iv) affine-core seeds.

fit_field: U_target(y) given on the model grid (3,Nr,Na) -> coefficients z (A, C channels; extra channels zero) minimizing
sum_j w_j |U(z) - U_target|^2 with w = node weights x (1+r^2/R0^2)^alpha. Because U is linear in z (fixed c_l, omega),
the Jacobian of the field map is assembled by forward-mode AD and the normal equations solved with a small Tikhonov
term relative to the largest eigenvalue (reported). Used for: transferring states of other routes (labelled 'transfer'),
affine-core seeds, and the SPEC 10 exchange.

Affine core (SPEC 11 (iv)): M = [[-1/2 + a, b - g, 0], [b + g, -1/2 - a, 0], [0, 0, 1]] (tr M = 0, g != 0, (a,b) != 0) is an
exact non-decaying profile for every c_l (Omega = 2 g e_3, eta = Omega.S Omega/|Omega|^2 = 1), two-fold symmetric;
-eps |y|^2 J y (g eps > 0) makes 0 a strict local maximum of |Omega|^2. Seed: U = chi(r) (M y - eps |y|^2 J y) + (1 - chi) U_tail
with chi = exp(-(r/R_c)^2) and U_tail the leading tail of a random (sigma, tau) seed, then projected onto the basis."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import alpha_of
from ..optimization.lm import jacobian_fwd

DT = torch.float64


def fit_field(model, U_target, tikhonov=1e-10, chunk=256, expand=None, n_red=None, rcond=1e-12):
    """U_target: (3, Nr, Na) on model grid. Returns (z, info). With expand (linear map reduced -> full coefficients, e.g.
    TailConstraints.expand) and n_red, the fit is done in the reduced (tail-constrained) coordinates and z is the full vector."""
    dev = model.r.device
    n = model.n_coef if expand is None else n_red
    def to_full(zc):
        zc = expand(zc) if expand is not None else zc
        return torch.cat([zc, torch.tensor([model.c_l0, model.omega0], dtype=DT, device=dev)]) if model.free_params else zc
    def field_flat(zc):
        return model.fields_grid(to_full(zc), need_vort=False)['U'].reshape(-1)
    z0 = torch.zeros(n, dtype=DT, device=dev)
    J = jacobian_fwd(field_flat, z0, chunk=chunk)                      # (3*Nr*Na, n): linear map (no constant term)
    alpha = alpha_of(model.c_l0)
    w = ((1 + model.rho / model.R0 ** 2) ** alpha)[:, None] * (model.grid.w / (4 * math.pi))[None, :]   # (Nr, Na)
    wv = w.expand(3, -1, -1).reshape(-1).sqrt()
    Jw = J * wv[:, None]; bw = U_target.reshape(-1) * wv
    # column scaling (the basis columns differ by many orders of magnitude: r^l R0^(alpha+l) factors) and a truncated-SVD least squares;
    # before 2026-10-24T23:40Z the fit used normal equations with a relative Tikhonov term 1e-10 lambda_max, which at condition numbers
    # 1e300 regularized away genuine directions (fit errors 1e-2 growing with Nk); the Tikhonov path is kept as an option (tikhonov > 0 and
    # lstsq=False)
    cs = Jw.norm(dim=0).clamp_min(1e-300)
    Js = Jw / cs[None, :]
    svals = torch.linalg.svdvals(Js.cpu())          # CPU: cusolver gesvd failed on the L 10 fit matrix (buffer-size error)
    sol = torch.linalg.lstsq(Js.cpu(), bw.cpu()[:, None], rcond=rcond, driver="gelsd")
    zc = (sol.solution[:, 0].to(dev)) / cs
    rank = int(sol.rank.item()) if sol.rank is not None and sol.rank.numel() else None
    resid = (Jw @ zc - bw).norm() / bw.norm().clamp_min(1e-300)
    z = to_full(zc)
    return z, dict(rel_fit_residual=resid.item(), cond_est=(svals[0] / svals[-1].clamp_min(1e-300)).item(), rank=rank, n_columns=int(n), rcond=rcond,
                   method="column-scaled truncated-SVD least squares (gelsd)")


def affine_profile_check(M, omega):
    """skew(M + M^2 + omega [J, M]) should vanish for an exact affine profile."""
    J = torch.tensor([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=DT)
    X = M + M @ M + omega * (J @ M - M @ J)
    return (X - X.T).abs().max().item(), M.trace().item()


def affine_core_seed(prob, rng, c_l, omega, a=None, b=None, g=None, eps=None, Rc=None, tail_amp=1.0):
    """Build the SPEC affine-core seed, project onto the basis, normalize to the F-gauge. Returns (z, meta)."""
    model = prob.model
    dev = model.r.device
    a = rng.uniform(-0.5, 0.5) if a is None else a
    b = rng.uniform(-0.5, 0.5) if b is None else b
    g = rng.choice([-1.0, 1.0]) * rng.uniform(0.5, 2.0) if g is None else g
    eps = (0.3 if g > 0 else -0.3) * rng.uniform(0.5, 2.0) if eps is None else eps
    Rc = rng.uniform(0.5, 2.0) * model.R0 if Rc is None else Rc
    M = torch.tensor([[-0.5 + a, b - g, 0.0], [b + g, -0.5 - a, 0.0], [0.0, 0.0, 1.0]], dtype=DT, device=dev)
    skew_def, tr = affine_profile_check(M.cpu(), omega)
    y = model.y                                                        # (Nr, Na, 3)
    My = torch.einsum('ij,rakj->raki', M, y[..., None, :]).squeeze(-2) if False else torch.einsum('ij,raj->rai', M, y)
    Jy = torch.stack([-y[..., 1], y[..., 0], torch.zeros_like(y[..., 0])], -1)
    core = My - eps * (y ** 2).sum(-1, keepdim=True) * Jy
    chi = torch.exp(-(model.r / Rc) ** 2)[:, None, None]
    # tail: leading tail of a random seed (A, C channels, Phi_0 only), scaled to the F-gauge
    from .seeds import make_seed
    ztail, mtail = make_seed(prob, "random", rng, c_l, omega, params=dict(core_ratio=0.0))
    Utail = model.fields_grid(ztail, need_vort=False)['U']            # (3, Nr, Na)
    U_target = (chi * core).permute(2, 0, 1) + (1 - chi.permute(2, 0, 1)) * tail_amp * Utail
    z, info = fit_field(model, U_target)
    aT, aS, c_lt, omt = model.unpack(z)
    n2 = prob.tail_norm2(aT, aS, c_lt, omt).item()
    z = z.clone(); z[: model.n_coef] = z[: model.n_coef] / math.sqrt(max(n2, 1e-300))
    meta = dict(family="affine_core", a=a, b=b, g=g, eps=eps, Rc=Rc, skew_defect=skew_def, trace=tr, fit_rel_residual=info["rel_fit_residual"],
                tail_norm2_before=n2, note="projected affine core + random tail; amplitude rescaled to the F-gauge (changes the core strain by the same factor)")
    return z, meta


def embed_state(z_src, model_src, model_dst):
    """Exact embedding of a state into a larger basis with the same R0 and parity: modes (l, m, t) of model_src are a
    subset of model_dst's, Chebyshev indices k < Nk_src a subset of k < Nk_dst; extra channels likewise. Coefficients are
    copied, the rest zero (the fields are identical). c_l, omega copied when free."""
    import torch
    ds = model_src.unpack_all(z_src)
    idx = {mode: i for i, mode in enumerate(model_dst.modes)}
    cols = torch.tensor([idx[mode] for mode in model_src.modes], dtype=torch.long, device=z_src.device)
    def emb(a, n_dst):
        out = torch.zeros(n_dst, model_dst.Nq, dtype=a.dtype, device=a.device)
        if a.numel():
            out[: a.shape[0], cols] = a
        return out
    A = emb(ds["A"], model_dst.Nk); C = emb(ds["C"], model_dst.Nk)
    extra = {k: emb(ds[k], dict(model_dst.layout)[k]) for k in ("B", "D", "E") if dict(model_dst.layout)[k] > 0}
    return model_dst.pack(A, C, ds["c_l"], ds["omega"], extra=extra)
