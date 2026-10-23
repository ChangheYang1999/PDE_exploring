"""Representation of the similarity profile.

Unknowns: smooth vector potential A(y) and pressure P(y) on R^3 (FP64).
    U = curl A                      (exactly divergence free)
    U(Qy) = Q U(y), P(Qy) = P(y)    (hard m=2 symmetry by projection, Q = diag(-1,-1,1))
Tail handling (EQUATIONS.md 5.4, R-tail + R-seed): network outputs are multiplied by algebraic envelopes at the
potential level, with one term per expected far-field degree,
    A = A_seed + sum_k rho^(d+1+k(d-1)) S[N_A^k](features),   rho = (1+R^2/l_env^2)^(1/2),  d = 1 - 1/c_l,
    P = P_seed + sum_k rho^(2d+k(d-1))   S[N_P^k](features),
k = 0 (leading, U ~ R^d, P ~ R^(2d)) and k = 1 (subleading, U ~ R^(2d-1), P ~ R^(3d-1)); the number of terms is
model.n_tail (1 or 2). Features ('dir_tau', default): xi = y/sqrt(l_in^2+R^2) (bounded, -> direction at infinity)
and tau = |xi|^2; these are analytic in y and bounded, so each N^k tends to a smooth angular function at infinity
(the non-integer subleading power is supplied by the second envelope, not by the network). Legacy feature sets
'dir_log', 'asinh', 'both' use the unbounded radial input log(1+R^2/l^2)/xi_scale; with them the learned leading tail
degenerates to an angular constant (verifier lane, research/radial-feature-tails/PROOF.md), so they are kept only
for the v1 baseline. P -> 0 at infinity is the pressure gauge (no free additive constant).
The seed family of PROMPT.md section 9 is used as a base field with learned corrections (scale 1; scaling M is not
the exact affine family because the skew part of tM+t^2M^2 is (t-t^2) skew M).
"""
import math
import torch
import torch.nn as nn

QDIAG = (-1.0, -1.0, 1.0)


def qmat(dtype, device):
    return torch.tensor(QDIAG, dtype=dtype, device=device)


def apply_Q(y):
    """Rotation by pi about the z axis applied to points or vectors of shape (...,3)."""
    return y * qmat(y.dtype, y.device)


class MLP(nn.Module):
    def __init__(self, n_in, n_out, width, depth, zero_last=True, gain=1.0):
        super().__init__()
        dims = [n_in] + [width] * depth + [n_out]
        self.lins = nn.ModuleList([nn.Linear(dims[i], dims[i + 1]) for i in range(len(dims) - 1)])
        for lin in self.lins[:-1]:
            nn.init.xavier_normal_(lin.weight, gain=gain)
            nn.init.zeros_(lin.bias)
        last = self.lins[-1]
        if zero_last:
            nn.init.zeros_(last.weight)
        else:
            nn.init.xavier_normal_(last.weight, gain=0.1)
        nn.init.zeros_(last.bias)

    def forward(self, x):
        for lin in self.lins[:-1]:
            x = torch.tanh(lin(x))
        return self.lins[-1](x)


def seed_matrix(a, b, c):
    """M = [[a,b,0],[c,-1-a,0],[0,0,1]] as a 3x3 tensor built from (possibly learnable) a,b,c."""
    z = torch.zeros_like(a)
    one = torch.ones_like(a)
    return torch.stack([torch.stack([a, b, z]), torch.stack([c, -one - a, z]), torch.stack([z, z, one])])


def seed_fields(y, M, cl):
    """Seed family of PROMPT.md section 9 (NOT an exact profile):
        chi = (1+|y|^2)^(-1/(2 c_l)),  A_seed = -(chi/3) y x (M y),  P_seed = -(chi^2/2) y.(M+M^2)y."""
    R2 = (y * y).sum(-1, keepdim=True)
    chi = (1.0 + R2) ** (-1.0 / (2.0 * cl))
    My = torch.matmul(y, M.transpose(0, 1))
    A = -(chi / 3.0) * torch.cross(y, My, dim=-1)
    MM = M + torch.matmul(M, M)
    P = -(chi[..., 0] ** 2 / 2.0) * (y * torch.matmul(y, MM.transpose(0, 1))).sum(-1)
    return A, P


def blob_potential(y, centers, moments, sigmas):
    """Q-paired localized vector-potential blobs: A_blob(y) = sum_j g_j(|y - y_j|) m_j + g_j(|y - Q y_j|) Q m_j,
    g_j = exp(-|.|^2 / (2 sigma_j^2)). Q-equivariant by construction; U = curl A_blob is a pair of localized vortex
    structures (smooth, exponentially localized; the algebraic tail is carried by the envelope terms)."""
    out = torch.zeros_like(y)
    for j in range(centers.shape[0]):
        c, m, sg = centers[j], moments[j], sigmas[j]
        for cc, mm in ((c, m), (apply_Q(c), apply_Q(m))):
            d2 = ((y - cc) ** 2).sum(-1, keepdim=True)
            out = out + torch.exp(-d2 / (2.0 * sg * sg)) * mm
    return out


class ProfileModel(nn.Module):
    """A(y), P(y) with hard symmetry, envelopes and seed base. Works on inputs of shape (...,3)."""

    def __init__(self, cfg):
        super().__init__()
        mcfg = cfg["model"]
        scfg = cfg.get("seed", {})
        self.cfg = cfg
        self.cl_trainable = bool(cfg.get("cl_trainable", False))
        lo, hi = cfg.get("cl_bounds", [0.4, 0.5])
        self.cl_lo, self.cl_hi = float(lo), float(hi)
        cl0 = float(cfg["cl"])
        if self.cl_trainable:
            # bounded parameterization cl = lo + (hi-lo) sigmoid(theta)
            t = (cl0 - lo) / (hi - lo)
            t = min(max(t, 1e-6), 1 - 1e-6)
            self.cl_theta = nn.Parameter(torch.tensor(math.log(t / (1 - t)), dtype=torch.float64))
        else:
            self.register_buffer("cl_fixed", torch.tensor(cl0, dtype=torch.float64))
        self.C = float(cfg.get("C", 0.0))
        self.l_in = float(mcfg.get("l_in", 1.0))
        self.xi_scale = float(mcfg.get("xi_scale", 3.0))
        self.l_env = float(mcfg.get("l_env", 1.0))
        self.feature_set = str(mcfg.get("feature_set", "dir_log"))
        self.p_env_shift = float(mcfg.get("p_env_shift", 0.0))  # pressure envelope degree 2d + shift
        self.a_env_shift = float(mcfg.get("a_env_shift", 0.0))  # potential envelope degree d+1 + shift
        n_in = {"dir_tau": 4, "dir_log": 4, "asinh": 4, "both": 7}[self.feature_set]
        self.n_tail = int(mcfg.get("n_tail", 2 if self.feature_set == "dir_tau" else 1))
        width, depth = int(mcfg.get("width", 64)), int(mcfg.get("depth", 4))
        self.netA = MLP(n_in, 3 * self.n_tail, width, depth, zero_last=mcfg.get("zero_last", True))
        self.netP = MLP(n_in, self.n_tail, width, depth, zero_last=mcfg.get("zero_last", True))
        self.out_scale = float(mcfg.get("out_scale", 1.0))
        # optional small random last layer (releases the seed's extra parities from the start; EQUATIONS.md 3.5)
        li = float(mcfg.get("last_init_std", 0.0))
        if li > 0:
            with torch.no_grad():
                for net in (self.netA, self.netP):
                    net.lins[-1].weight.normal_(0.0, li)
        # seed
        self.use_seed = bool(scfg.get("use", True))
        abc = torch.tensor([scfg.get("a", 0.2), scfg.get("b", -0.4), scfg.get("c", 0.7)], dtype=torch.float64)
        if scfg.get("trainable", False):
            self.seed_abc = nn.Parameter(abc)
        else:
            self.register_buffer("seed_abc", abc)

        # optional blob core (list of {"y0":[x,y,z], "m":[mx,my,mz], "sigma":s}); trainable flag shared
        bl = cfg.get("blobs", None)
        self.use_blobs = bool(bl) and len(bl.get("list", [])) > 0
        if self.use_blobs:
            cen = torch.tensor([b["y0"] for b in bl["list"]], dtype=torch.float64)
            mom = torch.tensor([b["m"] for b in bl["list"]], dtype=torch.float64)
            sig = torch.tensor([b["sigma"] for b in bl["list"]], dtype=torch.float64)
            if bl.get("trainable", True):
                self.blob_centers = nn.Parameter(cen); self.blob_moments = nn.Parameter(mom); self.blob_logsig = nn.Parameter(sig.log())
            else:
                self.register_buffer("blob_centers", cen); self.register_buffer("blob_moments", mom); self.register_buffer("blob_logsig", sig.log())

    # ---- scalar parameters -------------------------------------------------------------------
    def cl(self):
        if self.cl_trainable:
            return self.cl_lo + (self.cl_hi - self.cl_lo) * torch.sigmoid(self.cl_theta)
        return self.cl_fixed

    def seed_M(self):
        a, b, c = self.seed_abc[0], self.seed_abc[1], self.seed_abc[2]
        return seed_matrix(a, b, c)

    # ---- fields ------------------------------------------------------------------------------
    def features(self, y):
        """Smooth input features. 'dir_log' (default): y/sqrt(l^2+R^2) (bounded, -> direction at infinity)
        and log(1+R^2/l^2)/xi_scale (smooth at the origin, unbounded radial coordinate so that the network
        can represent non-integer subleading powers through saturation rates). 'asinh': asinh(y_i/l)/xi_scale
        plus the same radial feature. 'both': all seven. Under Q the horizontal features flip sign, the
        vertical and radial ones are invariant, so the symmetry projection is consistent."""
        R2 = (y * y).sum(-1, keepdim=True)
        if self.feature_set == "dir_tau":
            xi = y / torch.sqrt(self.l_in ** 2 + R2)
            return torch.cat([xi, (xi * xi).sum(-1, keepdim=True)], dim=-1)
        rad = torch.log1p(R2 / self.l_in ** 2) / self.xi_scale
        feats = []
        if self.feature_set in ("dir_log", "both"):
            feats.append(y / torch.sqrt(self.l_in ** 2 + R2))
        if self.feature_set in ("asinh", "both"):
            feats.append(torch.asinh(y / self.l_in) / self.xi_scale)
        feats.append(rad)
        return torch.cat(feats, dim=-1)

    def raw(self, y):
        """Network outputs: A terms (..., n_tail, 3) and P terms (..., n_tail)."""
        x = self.features(y)
        a = self.netA(x) * self.out_scale
        p = self.netP(x) * self.out_scale
        return a.reshape(a.shape[:-1] + (self.n_tail, 3)), p

    def corrections(self, y):
        """Symmetry-projected network outputs S[N_A^k](y) (..., n_tail, 3), S[N_P^k](y) (..., n_tail), no envelope."""
        Qy = apply_Q(y)
        NA, NP = self.raw(y)
        NAq, NPq = self.raw(Qy)
        SA = 0.5 * (NA + apply_Q(NAq))
        SP = 0.5 * (NP + NPq)
        return SA, SP

    def envelopes(self, y, cl):
        """Return envA (..., n_tail, 1) and envP (..., n_tail): rho^(d+1+k(d-1)) and rho^(2d+k(d-1))."""
        d = 1.0 - 1.0 / cl
        R2 = (y * y).sum(-1, keepdim=True)
        base = 1.0 + R2 / (self.l_env ** 2)
        ea, ep = [], []
        for k in range(self.n_tail):
            ea.append(base ** (0.5 * (d + 1.0 + k * (d - 1.0) + self.a_env_shift)))
            ep.append(base ** (d + 0.5 * k * (d - 1.0) + 0.5 * self.p_env_shift))
        return torch.stack(ea, dim=-2), torch.cat(ep, dim=-1)

    def fields(self, y):
        """Return F = (A_1,A_2,A_3,P) of shape (...,4)."""
        cl = self.cl()
        envA, envP = self.envelopes(y, cl)
        SA, SP = self.corrections(y)
        A = (envA * SA).sum(-2)
        P = (envP * SP).sum(-1)
        if self.use_seed:
            As, Ps = seed_fields(y, self.seed_M(), cl)
            A = A + As
            P = P + Ps
        if self.use_blobs:
            A = A + blob_potential(y, self.blob_centers, self.blob_moments, self.blob_logsig.exp())
        return torch.cat([A, P.unsqueeze(-1)], dim=-1)

    def forward(self, y):
        return self.fields(y)
