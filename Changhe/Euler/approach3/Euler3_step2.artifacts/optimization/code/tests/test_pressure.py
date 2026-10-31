"""Pressure solver on manufactured decaying P (m = 0 modes: the solver assumes the twisted-frame structure of the
representation's sources, so untwisted m != 0 manufactured sources are outside its class; see test_pressure_twisted.py):
P = sum_q c_q (1+rho/R0^2)^(-(gamma+l)/2) P_q(y), f = -Lap P from the exact Hessian trace; compares P and grad P on the
grid; checks monopole behaviour and volume-integral weights."""
import sys, os, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model
from src.pressure.poisson_sh import PressureSolver
from src.bases.solid_harmonics import mode_list, eval_solid
torch.set_default_dtype(torch.float64)

def manufactured(model, gamma, pmodes, seed=0):
    rng = np.random.default_rng(seed)
    Nq = len(pmodes)
    l = torch.tensor([float(a) for (a, b, c) in pmodes])
    m = torch.tensor([float(b) for (a, b, c) in pmodes])
    coef = torch.tensor(rng.normal(size=Nq)) * torch.exp(-0.3 * l) * (m == 0).double()
    rho = model.rho[:, None]; R0 = model.R0
    p = (gamma + l[None, :]) / 2
    b = 1 + rho / R0**2
    h0 = coef * b ** (-p)
    h1 = coef * (-p) * b ** (-p - 1) / R0**2
    h2 = coef * p * (p + 1) * b ** (-p - 2) / R0**4
    return (h0, h1, h2), coef

def run(L=4, Nk=10, Nr=30, gamma=2.4, R0=1.0):
    model = Model(L=L, Nk=Nk, m_parity="even", R0=R0, Nr=Nr, c_l=0.45, omega=0.5)
    pm = mode_list(model.Lf, "even", l_min=0)
    A0, A1, A2 = eval_solid(model.grid.n, pm, model.Lf, 2)
    helper = Model.__new__(Model); helper.__dict__.update(model.__dict__)
    helper.modes = pm; helper.A0, helper.A1, helper.A2 = A0, A1, A2
    helper.l_arr = torch.tensor([float(a) for (a, b, c) in pm]); helper.rl = model.r[:, None] ** helper.l_arr[None, :]
    h, coef = manufactured(model, gamma, pm)
    P_ref, gP_ref, H_ref = helper.scalar_grid(h, True)
    f = -(H_ref[0, 0] + H_ref[1, 1] + H_ref[2, 2])
    for p0 in [gamma + 2, gamma + 2.5]:
        t0 = time.time()
        ps = PressureSolver(model, p0=p0)
        tb = time.time() - t0
        P, gP, Plm, dPlm = ps.solve(f)
        errP = (P - P_ref).abs().max().item() / P_ref.abs().max().item()
        errG = (gP - gP_ref).abs().max().item() / gP_ref.abs().max().item()
        wr = (1 + model.r ** 2) ** (gamma / 2)
        errPw = ((P - P_ref).abs() * wr[:, None]).max().item() / (P_ref.abs() * wr[:, None]).max().item()
        print(f"p0={p0:.2f} (true decay {gamma+2:.2f}): build {tb:.1f}s, rel err P {errP:.2e}, grad P {errG:.2e}, r^gamma-weighted P {errPw:.2e}")
        if abs(p0 - gamma - 2) < 1e-12:
            assert errP < 1e-9 and errG < 1e-8
    I = ps.volume_integral(f).item()
    g = torch.exp(-model.rho)[:, None].expand(-1, model.Na)
    Ig = ps.volume_integral(g).item()
    print(f"monopole int f = {I:.2e} (expect ~0); int exp(-r^2) = {Ig:.12f} vs pi^1.5 = {math.pi**1.5:.12f}")
    assert abs(Ig - math.pi ** 1.5) < 1e-8
    print("PRESSURE TESTS PASSED")

if __name__ == "__main__":
    run()
