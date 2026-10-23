"""Hand-derived second-order forward propagation of (value, Jacobian, Hessian) w.r.t. y through the ProfileModel.

Replaces nested torch.func.jacfwd in the training loss (3-4x fewer kernels); torch.func remains the independent
cross-check (tests compare both to 1e-12). Conventions as in physics.py: J[n,i,a] = d_a F_i, H[n,i,a,b] = d_a d_b F_i.
Supports feature_set 'dir_tau', any n_tail, trainable c_l and seed matrix; falls back (returns None) for blobs or other
feature sets.
"""
import torch
from .model import seed_matrix, apply_Q, qmat

EPS = torch.tensor  # alias


def _lin(W, b, h, Jh, Hh):
    z = h @ W.T + b
    Jz = torch.einsum("oi,nia->noa", W, Jh)
    Hz = torch.einsum("oi,niab->noab", W, Hh)
    return z, Jz, Hz


def _tanh(z, Jz, Hz):
    t = torch.tanh(z)
    t1 = 1.0 - t * t
    t2 = -2.0 * t * t1
    Jt = t1.unsqueeze(-1) * Jz
    Ht = t1.unsqueeze(-1).unsqueeze(-1) * Hz + t2.unsqueeze(-1).unsqueeze(-1) * Jz.unsqueeze(-1) * Jz.unsqueeze(-2)
    return t, Jt, Ht


def _mlp(net, x, Jx, Hx):
    h, Jh, Hh = x, Jx, Hx
    lins = list(net.lins)
    for lin in lins[:-1]:
        z, Jz, Hz = _lin(lin.weight, lin.bias, h, Jh, Hh)
        h, Jh, Hh = _tanh(z, Jz, Hz)
    return _lin(lins[-1].weight, lins[-1].bias, h, Jh, Hh)


def _features_dir_tau(y, l_in):
    """xi = y/s, s = sqrt(l^2+R^2); tau = |xi|^2 = 1 - l^2/s^2. Returns x (N,4), Jx (N,4,3), Hx (N,4,3,3)."""
    N = y.shape[0]
    R2 = (y * y).sum(-1, keepdim=True)
    s = torch.sqrt(l_in ** 2 + R2)
    xi = y / s
    I3 = torch.eye(3, dtype=y.dtype, device=y.device)
    yy = y.unsqueeze(-1) * y.unsqueeze(-2)  # (N,3,3) y_i y_a
    s3 = (s ** 3).unsqueeze(-1); s5 = (s ** 5).unsqueeze(-1)
    Jxi = I3 / s.unsqueeze(-1) - yy / s3  # [n,i,a]
    # H[n,i,a,b] = -(delta_ia y_b + delta_ib y_a + delta_ab y_i)/s^3 + 3 y_i y_a y_b / s^5
    yb = y.view(N, 1, 1, 3); ya = y.view(N, 1, 3, 1); yi = y.view(N, 3, 1, 1)
    Hxi = -(I3.view(1, 3, 3, 1) * yb + I3.view(1, 3, 1, 3) * ya + I3.view(1, 1, 3, 3) * yi) / s3.unsqueeze(-1) + 3.0 * yi * ya * yb / s5.unsqueeze(-1)
    tau = (xi * xi).sum(-1, keepdim=True)
    l2 = l_in ** 2
    Jtau = (2.0 * l2 * y / s ** 4).unsqueeze(1)  # (N,1,3)
    Htau = (2.0 * l2 * I3 / (s ** 4).unsqueeze(-1) - 8.0 * l2 * yy / (s ** 6).unsqueeze(-1)).unsqueeze(1)  # (N,1,3,3)
    x = torch.cat([xi, tau], -1)
    Jx = torch.cat([Jxi, Jtau], 1)
    Hx = torch.cat([Hxi, Htau], 1)
    return x, Jx, Hx


def _power_base(y, p, l_env):
    """e = (1 + R^2/l^2)^p for tensor exponent p (scalar). Returns e (N,1), Je (N,1,3), He (N,1,3,3)."""
    l2 = l_env ** 2
    R2 = (y * y).sum(-1, keepdim=True)
    base = 1.0 + R2 / l2
    e = base ** p
    g = 2.0 * y / l2  # d_a base
    e1 = p * base ** (p - 1.0)
    e2 = p * (p - 1.0) * base ** (p - 2.0)
    I3 = torch.eye(3, dtype=y.dtype, device=y.device)
    Je = (e1 * g).unsqueeze(1)
    He = (e2.unsqueeze(-1) * g.unsqueeze(-1) * g.unsqueeze(-2) + e1.unsqueeze(-1) * (2.0 / l2) * I3).unsqueeze(1)
    return e, Je, He


def _prod_scalar_vec(e, Je, He, v, Jv, Hv):
    """(e v) with e (N,1), Je (N,1,3), He (N,1,3,3); v (N,m), Jv (N,m,3), Hv (N,m,3,3)."""
    val = e * v
    J = e.unsqueeze(-1) * Jv + v.unsqueeze(-1) * Je
    H = e.unsqueeze(-1).unsqueeze(-1) * Hv + v.unsqueeze(-1).unsqueeze(-1) * He + Je.unsqueeze(-1) * Jv.unsqueeze(-2) + Jv.unsqueeze(-1) * Je.unsqueeze(-2)
    return val, J, H


def _seed(y, M, cl):
    """A_seed = -(chi/3) y x (M y), P_seed = -(chi^2/2) y.(M+M^2) y, chi = (1+R^2)^(-1/(2cl)). Returns (F (N,4), J, H)."""
    N = y.shape[0]
    dt, dv = y.dtype, y.device
    eps = torch.zeros(3, 3, 3, dtype=dt, device=dv)
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1.0
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1.0
    m = y @ M.T  # (N,3)
    w = torch.cross(y, m, dim=-1)  # w_i = eps_ijk y_j m_k
    # d_a w_i = eps_iak m_k + eps_ijk y_j M_ka
    Jw = torch.einsum("iak,nk->nia", eps, m) + torch.einsum("ijk,nj,ka->nia", eps, y, M)
    # d_a d_b w_i = eps_iak M_kb + eps_ibk M_ka
    Hw = (torch.einsum("iak,kb->iab", eps, M) + torch.einsum("ibk,ka->iab", eps, M)).unsqueeze(0).expand(N, 3, 3, 3)
    q = -1.0 / (2.0 * cl)
    chi, Jchi, Hchi = _power_base(y, q, 1.0)
    A, JA, HA = _prod_scalar_vec(-chi / 3.0, -Jchi / 3.0, -Hchi / 3.0, w, Jw, Hw)
    MM = M + M @ M
    MMy = y @ MM.T
    Qd = (y * MMy).sum(-1, keepdim=True)
    JQd = (2.0 * MMy).unsqueeze(1)  # (N,1,3)   (MM symmetric)
    HQd = (2.0 * MM).view(1, 1, 3, 3).expand(N, 1, 3, 3)
    chi2, Jchi2, Hchi2 = _power_base(y, 2.0 * q, 1.0)
    P, JP, HP = _prod_scalar_vec(-chi2 / 2.0, -Jchi2 / 2.0, -Hchi2 / 2.0, Qd, JQd, HQd)
    return torch.cat([A, P], -1), torch.cat([JA, JP], 1), torch.cat([HA, HP], 1)


def fast_fields_derivs(model, y):
    """Return F (N,4), J (N,4,3), H (N,4,3,3) for model.fields, or None if unsupported."""
    if model.feature_set != "dir_tau" or getattr(model, "use_blobs", False):
        return None
    N = y.shape[0]
    cl = model.cl()
    d = 1.0 - 1.0 / cl
    Qy = apply_Q(y)
    yy2 = torch.cat([y, Qy], 0)
    x, Jx, Hx = _features_dir_tau(yy2, model.l_in)
    a, Ja, Ha = _mlp(model.netA, x, Jx, Hx)
    p, Jp, Hp = _mlp(model.netP, x, Jx, Hx)
    os_ = model.out_scale
    a, Ja, Ha, p, Jp, Hp = a * os_, Ja * os_, Ha * os_, p * os_, Jp * os_, Hp * os_
    # derivatives of the second half are w.r.t. Qy; convert to derivatives w.r.t. y: d/dy = Q d/d(Qy)
    qd = qmat(y.dtype, y.device)
    Ja2 = Ja[N:] * qd.view(1, 1, 3); Ha2 = Ha[N:] * qd.view(1, 1, 3, 1) * qd.view(1, 1, 1, 3)
    Jp2 = Jp[N:] * qd.view(1, 1, 3); Hp2 = Hp[N:] * qd.view(1, 1, 3, 1) * qd.view(1, 1, 1, 3)
    nt = model.n_tail
    # Q acts on the A output vector index (component signs) for each tail term
    qa = qd.repeat(nt)  # (3 nt,)
    SA = 0.5 * (a[:N] + qa * a[N:]); JSA = 0.5 * (Ja[:N] + qa.view(1, -1, 1) * Ja2); HSA = 0.5 * (Ha[:N] + qa.view(1, -1, 1, 1) * Ha2)
    SP = 0.5 * (p[:N] + p[N:]); JSP = 0.5 * (Jp[:N] + Jp2); HSP = 0.5 * (Hp[:N] + Hp2)
    A = torch.zeros(N, 3, dtype=y.dtype, device=y.device); JA = torch.zeros(N, 3, 3, dtype=y.dtype, device=y.device); HA = torch.zeros(N, 3, 3, 3, dtype=y.dtype, device=y.device)
    P = torch.zeros(N, 1, dtype=y.dtype, device=y.device); JP = torch.zeros(N, 1, 3, dtype=y.dtype, device=y.device); HP = torch.zeros(N, 1, 3, 3, dtype=y.dtype, device=y.device)
    for k in range(nt):
        pa = 0.5 * (d + 1.0 + k * (d - 1.0) + model.a_env_shift)
        pp = d + 0.5 * k * (d - 1.0) + 0.5 * model.p_env_shift
        ea, Jea, Hea = _power_base(y, pa, model.l_env)
        ep, Jep, Hep = _power_base(y, pp, model.l_env)
        v, Jv, Hv = _prod_scalar_vec(ea, Jea, Hea, SA[:, 3 * k:3 * k + 3], JSA[:, 3 * k:3 * k + 3], HSA[:, 3 * k:3 * k + 3])
        A = A + v; JA = JA + Jv; HA = HA + Hv
        v, Jv, Hv = _prod_scalar_vec(ep, Jep, Hep, SP[:, k:k + 1], JSP[:, k:k + 1], HSP[:, k:k + 1])
        P = P + v; JP = JP + Jv; HP = HP + Hv
    F = torch.cat([A, P], -1); J = torch.cat([JA, JP], 1); H = torch.cat([HA, HP], 1)
    if model.use_seed:
        Fs, Js, Hs = _seed(y, model.seed_M(), cl)
        F = F + Fs; J = J + Js; H = H + Hs
    return F, J, H
