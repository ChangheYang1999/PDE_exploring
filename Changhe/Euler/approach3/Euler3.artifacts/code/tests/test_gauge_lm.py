"""Lead's request (2026-10-24T18:59Z): LM from a random start with the nonlinear-balance reweighting must not collapse
to U = 0 and must keep the F-gauge: report |int |F|^2 - 1| after the run (soft gauge row with weight 100)."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.lm import lm_solve
from src.optimization.seeds import make_seed
torch.set_default_dtype(torch.float64)

def run(formulation, nlw, seed=5, iters=40):
    dev = "cuda:0" if torch.cuda.is_available() else "cpu"
    model = Model(L=4, Nk=8, m_parity="even", R0=1.0, Nr=20, c_l=0.45, omega=1.0, device=dev)
    prob = Problem(model, formulation=formulation, nl_weighting=nlw)
    z, meta = make_seed(prob, "random", np.random.default_rng(seed), 0.45, 1.0)
    prob.pivot = prob.choose_pivot(z); prob.update_nl_weights(z)
    def cb(it, zc, cost, rec):
        if nlw and rec.get("accepted", True):
            prob.update_nl_weights(zc); return True
        return False
    out = lm_solve(prob.residual_vector, z, max_iter=iters, verbose=False, chunk=64, callback=cb, project=prob.phase_align, scale_rows=prob.n_pde_residuals())
    g, pd = prob.gauge_defects(out["z"])
    U = model.fields_grid(out["z"], need_vort=False)["U"]
    z = out["z"].clone(); aT, aS, c_l, om = model.unpack(z); nF = prob.tail_norm2(aT, aS, c_l, om).sqrt(); z[: model.n_coef] /= nF
    g2, _ = prob.gauge_defects(z)
    print(f"[{formulation} nlw={nlw}] {len(out['history'])} its, status {out['status']}: max|U| = {U.abs().max().item():.3e}, gauge defect |int|F|^2-1| = {g:.2e} (optimizer, soft row weight {prob.gauge_weight:g}), {g2:.1e} after the exact projection; pivot defect = {pd}")
    assert U.abs().max().item() > 1e-2, "collapse to zero"
    assert g < 1e-3 and g2 < 1e-8, "gauge defect too large"   # soft row (weight 100) leaves <= 1e-3 in 40 its; the exact final projection removes it
    return g

if __name__ == "__main__":
    for f, w in [("mom", True), ("vort", True), ("mom", False)]:
        run(f, w)
    print("GAUGE/COLLAPSE TEST PASSED")
