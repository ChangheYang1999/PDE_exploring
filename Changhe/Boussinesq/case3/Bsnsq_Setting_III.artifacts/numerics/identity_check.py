"""Check c = Lambda + NL with Lambda = (1/pi) int xy Theta_x / r^4, NL = (1/pi) int Omega U.grad(xy/r^4) on eps=0 fields."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from bq3core import Basis, Geometry, DT
torch.set_default_dtype(DT)
dev = 'cuda'
for f in sys.argv[1:]:
    d = np.load(f)
    b = Basis(32, 5, 12, 12, ng_coll=7, m_reg=2, device=dev, grade=1.5)
    g = Geometry(b, 3.0, 1.5)
    x, y, r = g.x, g.y, g.rr
    W = (b.w_coll_t * g.drdt)[:, None].expand(b.Nc, b.Nphi).reshape(-1) * (np.pi / b.Nphi) * r      # area element, half plane
    cF = torch.tensor(d['cF'], dtype=DT, device=dev); cGext = torch.tensor(d['cG_ext'], dtype=DT, device=dev)
    Gch = torch.tensor(d['G'], dtype=DT, device=dev)
    Om = x * Gch
    F1 = g.Phi1F @ cF
    Thx = 2 * x * F1
    U1 = g.M_U1 @ cGext; U2 = g.M_U2 @ cGext
    phi = x * y / r ** 4
    dphix = y / r ** 4 - 4 * x ** 2 * y / r ** 6
    dphiy = x / r ** 4 - 4 * x * y ** 2 / r ** 6
    c_quad = 2 * (phi * Om * W).sum().item() / np.pi
    Lam = 2 * (phi * Thx * W).sum().item() / np.pi
    NL = 2 * (Om * (U1 * dphix + U2 * dphiy) * W).sum().item() / np.pi
    print(f"{f}: c_out(fit)={float(d['c_out']):+.5f} c_quad={c_quad:+.5f}  Lambda={Lam:+.5f}  NL={NL:+.5f}  Lambda+NL={Lam+NL:+.5f}  (identity residual {c_quad-Lam-NL:+.2e})")
