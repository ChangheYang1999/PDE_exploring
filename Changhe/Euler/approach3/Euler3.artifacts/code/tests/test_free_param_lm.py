"""Verifier request (21:29Z): the actual free-parameter worker combination (free c_l, omega; fine-grid Sigma_Z scalar row; tail
constraints; far nodes) must give a consistent LM step: (1) the complete rebuilt residual has exactly the Jacobian's row count;
(2) a MIXED coefficient-and-parameter directional difference of the complete rebuilt residual, taken at a base whose parameters differ
from the originally stored pressure, matches the assembled Jacobian (AD coefficient columns at the exact base + rebuilt FD columns)."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.seeds import make_seed
from src.optimization.tail_constraints import TailConstraints
from src.optimization.lm import jacobian_fwd
torch.set_default_dtype(torch.float64)
dev = "cuda:0" if torch.cuda.is_available() else "cpu"

def run():
    model = Model(L=4, Nk=8, Nr=20, m_parity="even", R0=1.0, c_l=0.45, omega=1.0, device=dev, free_params=True, extra_r=[4096., 16384.])
    prob = Problem(model, formulation="mom", nl_weighting=True, sigmaZ=1.0, far_radii=None, sigmaZ_fine=4)
    tc = TailConstraints(model)
    z, _ = make_seed(prob, "random", np.random.default_rng(2), 0.45, 1.0); prob.pivot = prob.choose_pivot(z); prob.update_nl_weights(z)
    zr = tc.reduce(z)
    # move the base parameters away from the stored pressure (stored at 0.45, 1.0) and rebuild at the exact base (as the worker callback does)
    zr = zr.clone(); zr[-2] = 0.452; zr[-1] = 1.03
    prob.maybe_rebuild_pressure(tc.expand(zr))
    main = lambda q: prob.residual_vector_main(tc.expand(q)); srow = lambda q: prob.sigmaZ_row(tc.expand(q)); full_rebuilt = lambda q: prob.residual_vector_rebuild(tc.expand(q))
    r_full = full_rebuilt(zr); Jm = jacobian_fwd(main, zr, chunk=64)
    q_ = zr.detach().clone().requires_grad_(True); gr, = torch.autograd.grad(srow(q_), q_)
    J = torch.cat([Jm, gr[None]], 0)
    print(f"rows: Jacobian {J.shape[0]}, complete rebuilt residual {r_full.numel()}")
    assert J.shape[0] == r_full.numel()
    n = zr.numel()
    for k in [n - 2, n - 1]:
        e = torch.zeros_like(zr); h = 1e-5; e[k] = h
        J[:, k] = (full_rebuilt(zr + e) - full_rebuilt(zr - e)) / (2 * h)
    # mixed direction: coefficients + both parameters
    rng = np.random.default_rng(5); d = torch.tensor(rng.normal(size=n), device=dev); d = d / d.norm(); d[-2] = 0.3; d[-1] = 0.3
    jd = J @ d
    errs = {}
    for h in [1e-4, 1e-5, 1e-6]:
        fd = (full_rebuilt(zr + h * d) - full_rebuilt(zr - h * d)) / (2 * h)
        errs[h] = ((jd - fd).norm() / fd.norm()).item()
    print("mixed coefficient+parameter directional check at a shifted base (c_l 0.452, omega 1.03): |J d - FD| / |FD| = " + ", ".join(f"h={h:.0e}: {e:.2e}" for h, e in errs.items()))
    assert min(errs.values()) < 1e-6 and errs[1e-4] < 1e-4
    print("FREE-PARAMETER LM CONSISTENCY TEST PASSED")

if __name__ == "__main__":
    run()
