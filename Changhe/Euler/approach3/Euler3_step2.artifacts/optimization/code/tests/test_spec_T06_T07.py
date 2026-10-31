"""SPEC T06: reflection S = diag(1,-1,1) maps a state with omega to one with -omega: residuals on mirrored points agree.
SPEC T07: L[r^-alpha F] = 0 for random smooth (sigma, tau) tails built from the spherical-harmonic basis (asymptotically,
through the Phi_0-only coefficient set), checked by the decay of the scaled linear residual with radius."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model
from src.equations import residuals as res
torch.set_default_dtype(torch.float64)

def test_T06():
    torch.manual_seed(11)
    m1 = Model(L=4, Nk=5, m_parity="even", R0=1.0, Nr=8, c_l=0.44, omega=1.7)
    m2 = Model(L=4, Nk=5, m_parity="even", R0=1.0, Nr=8, c_l=0.44, omega=-1.7)
    z1 = torch.randn(m1.n_z) * 0.4
    aT, aS, _, _ = m1.unpack(z1)
    # S y: (x, -y, z) -> phi -> -phi: cos(m phi) even, sin(m phi) odd; scalar potentials: T'(y) = T(S y)?  For U' = S U(S y):
    # curl(T y) is a pseudo-vector construction: curl(T' y) with T' = -T(S y) gives S [curl(T y)](S y); curl curl(S' y) with S' = +S(S y).
    aT2, aS2 = aT.clone(), aS.clone()
    for q, (l, m, t) in enumerate(m1.modes):
        sgn = 1.0 if t == 0 else -1.0
        aT2[:, q] = -sgn * aT[:, q]; aS2[:, q] = sgn * aS[:, q]
    z2 = m2.pack(aT2, aS2)
    pts = torch.tensor([[0.4, -0.3, 0.6], [1.5, 0.7, -0.2], [0.0, 0.0, 0.9], [2.0, 1.0, 1.0]])
    Sm = torch.diag(torch.tensor([1.0, -1.0, 1.0]))
    F1 = m1.fields_points(z1, pts); F2 = m2.fields_points(z2, (Sm @ pts.T).T)
    eU = (F2['U'] - Sm @ F1['U']).abs().max().item()
    R1 = res.momentum_terms(F1)['sum']; R2 = res.momentum_terms(F2)['sum']
    eR = (R2 - Sm @ R1).abs().max().item() / R1.abs().max().item()
    V1 = res.vorticity_terms(F1)['sum']; V2 = res.vorticity_terms(F2)['sum']
    eV = (V2 + Sm @ V1).abs().max().item() / V1.abs().max().item()     # Omega is a pseudo-vector: Omega' = -S Omega(S y)
    print(f"T06 reflection omega -> -omega: U {eU:.2e}, R_u0 {eR:.2e}, R_Omega {eV:.2e}")
    assert max(eU, eR, eV) < 1e-12

def test_T07():
    torch.manual_seed(12)
    model = Model(L=6, Nk=4, m_parity="all", R0=1.0, Nr=8, c_l=0.47, omega=2.3)
    aT = torch.zeros(model.Nk, model.Nq); aS = torch.zeros_like(aT)
    aT[0] = torch.randn(model.Nq); aS[0] = torch.randn(model.Nq)       # Phi_0 only: pure envelope times harmonics (random sigma, tau)
    z = model.pack(aT, aS)
    worst = []
    for r in [1e2, 1e3, 1e4, 1e5]:
        n = torch.randn(40, 3); n = n / n.norm(dim=1, keepdim=True)
        pts = r * n
        F = model.fields_points(z, pts, need_vort=False)
        U, GU, yv = F['U'], F['GU'], pts.T
        W = 0.47 * yv - 2.3 * res.Jvec(yv)
        Rlin = (1 - 0.47) * U + torch.einsum('m...,mi...->i...', W, GU) + 2.3 * res.Jvec(U)
        ratio = (Rlin.norm(dim=0) / U.norm(dim=0)).max().item()
        worst.append(ratio)
    print("T07 random (sigma,tau) tail: |L U|/|U| at r=1e2..1e5:", " ".join(f"{v:.2e}" for v in worst), "(expected ~ 2 R0^2/r^2 from the s vs r envelope)")
    assert worst[-1] < 1e-8 and worst[1] / worst[2] > 50

if __name__ == "__main__":
    test_T06(); test_T07(); print("T06/T07 PASSED")
