"""Loss assembly and training-time diagnostics (all components logged separately)."""
import math
import torch
from . import physics as ph
from .model import apply_Q
from .fastderiv import fast_fields_derivs


def fields_derivs(model, y, fast=True):
    """(F, J, H) by the hand-derived forward propagation when supported (fast=True), else nested torch.func.jacfwd."""
    if fast:
        out = fast_fields_derivs(model, y)
        if out is not None:
            return out
    return ph.derivs(lambda p: model.fields(p), y, order=2)


def rot_z(alpha, dtype, device):
    c, s = math.cos(alpha), math.sin(alpha)
    return torch.tensor([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]], dtype=dtype, device=device)


def nonaxi_ratio(model, y, K=8):
    """Vector group average over rotations about z (PROMPT.md section 6):
    U_axi(y) = (1/K) sum_k R_{-a_k} U(R_{a_k} y). Returns (||U - U_axi||^2 sum, ||U||^2 sum, U, U_axi).
    K equally spaced angles over [0,2pi) remove cylindrical modes n not divisible by K and retain n = 0, +-K, +-2K, ...
    (so the result is the exact zero mode only if no content sits at multiples of K; check ring Fourier spectra too).
    On a finite non-rotation-invariant point set the ratio is a diagnostic, not an orthogonal energy split."""
    Us = []
    Ua = torch.zeros_like(y)
    for k in range(K):
        a = 2 * math.pi * k / K
        R = rot_z(a, y.dtype, y.device)
        yk = y @ R.T
        F, J = ph.derivs(lambda p: model.fields(p), yk, order=1)
        Uk = ph.curl_from_jac(J[:, :3, :])
        Ua = Ua + Uk @ R  # R_{-a} U = R^T U -> row-vector form U @ R
        if k == 0:
            U0 = Uk
    Ua = Ua / K
    e_non = ((U0 - Ua) ** 2).sum()
    e_tot = (U0 ** 2).sum()
    return e_non, e_tot, U0, Ua


def smooth_max_norm(U, p=8):
    """(sum_i |U_i|^(2p))^(1/(2p)): a smooth surrogate of max_i |U_i| (over-estimates by at most N^(1/2p))."""
    n2 = (U * U).sum(-1)
    m = n2.max().detach().clamp_min(1e-300)
    return m.sqrt() * (((n2 / m) ** p).sum()) ** (1.0 / (2.0 * p))


def compute_loss(model, batch, gauge_pts, cfg, cl_override=None):
    """batch: dict region -> (y, w). Returns total loss and dict of logged scalars."""
    lcfg = cfg["loss"]
    cl = model.cl()
    C = model.C
    logs = {}
    total = torch.zeros((), dtype=torch.float64, device=gauge_pts.device)
    rw = lcfg.get("region_weights", {})
    fast = bool(lcfg.get("fast_derivs", True))
    for name, (y, w) in batch.items():
        F, J, H = fields_derivs(model, y, fast)
        U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
        Rm, V, conv = ph.momentum_residual(y, U, gU, gP, cl, C)
        T = ph.term_scale(y, cl, lcfg.get("T_mode", "nonlinear"), model.l_env, lam=lcfg.get("T_lambda", None))
        r2 = (Rm * Rm).sum(-1) / (T * T)
        lm = r2.mean()  # per-region mean under the sampling distribution (documented; physical weights w are used in validation)
        logs["mom_" + name] = lm.detach()
        logs["mom_" + name + "_max"] = r2.detach().max().sqrt()
        total = total + float(rw.get(name, 1.0)) * lm
        if lcfg.get("div_weight", 0.0) > 0:  # U = curl A is exactly divergence free; this is a check only
            dv = ph.divergence(gU)
            ld = (dv * dv).mean()
            logs["div_" + name] = ld.detach()
            total = total + lcfg["div_weight"] * ld
    # amplitude gauge on fixed gauge points: smooth-max |U| = 1
    Fg, Jg = ph.derivs(lambda p: model.fields(p), gauge_pts, order=1)
    Ug = ph.curl_from_jac(Jg[:, :3, :])
    amp = smooth_max_norm(Ug, p=int(lcfg.get("amp_p", 8)))
    lam_amp = float(lcfg.get("lambda_amp", 1.0))
    l_amp = (amp - 1.0) ** 2
    logs["amp_smooth"] = amp.detach()
    logs["amp_max"] = Ug.norm(dim=-1).max().detach()
    logs["gauge_amp"] = l_amp.detach()
    total = total + lam_amp * l_amp
    # optional temporary non-axisymmetry floor (search branch only; must be relaxed before acceptance)
    lam_na = float(lcfg.get("lambda_nonaxi", 0.0))
    if lam_na > 0 or lcfg.get("log_nonaxi", False):
        e_non, e_tot, _, _ = nonaxi_ratio(model, gauge_pts[: int(lcfg.get("nonaxi_pts", 512))], K=int(lcfg.get("nonaxi_K", 8)))
        ratio = e_non / e_tot.clamp_min(1e-300)
        logs["nonaxi_ratio"] = ratio.detach()
        if lam_na > 0:
            floor = float(lcfg.get("nonaxi_floor", 0.05))
            l_na = torch.relu(floor - ratio) ** 2
            logs["pen_nonaxi"] = l_na.detach()
            total = total + lam_na * l_na
    logs["cl"] = cl.detach()
    logs["total"] = total.detach()
    return total, logs
