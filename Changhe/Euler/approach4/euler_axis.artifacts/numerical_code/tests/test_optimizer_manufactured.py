"""Manufactured-solution test of the whole least-squares machinery (PROMPT section 3): take a smooth state x* in the basis
(the S1 seed fit at pilot resolution), force the system so that r(x*) = 0 exactly (r_offset = r_unforced(x*)), perturb x* by a
relative random amount, and check that Levenberg-Marquardt recovers x* (cost to round-off, |x - x*| small) within a bounded
number of iterations.  This separates optimizer/Jacobian defects from the hardness of the real (unforced) problem.
Run: CUDA_VISIBLE_DEVICES=<gpu> python3 tests/test_optimizer_manufactured.py"""
import os, sys, time, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np, torch
from axi.problem import Problem, Config
from axi.init import make_init
from axi import lm
torch.set_default_dtype(torch.float64)
dev = "cuda" if torch.cuda.is_available() else "cpu"
FAILS = []
def check(name, err, tol):
    ok = err <= tol; print(f"[{'PASS' if ok else 'FAIL'}] {name}: err={err:.3e} tol={tol:.1e}")
    if not ok: FAILS.append(name)

for (label, cfg, pert) in [
    ("small, S1 rows, 5% perturbation", Config(cl=0.6, D=16, nmax=8, shells=[(8.0, 12)], gauge="full", s1_constraint=True, w_int=100.0, w_s1=300.0), 0.05),
    ("pilot size, S1 rows + amplitude, 5% perturbation", Config(cl=0.6, D=24, nmax=12, shells=[(10.0, 16)], gauge="full", s1_constraint=True, amp_param=True, w_int=100.0, w_s1=300.0, ball_radial="jacobi", emax=4.0), 0.05),
    ("pilot size, free c_l, 5% perturbation + c_l off by 0.01", Config(cl=0.6, free_cl=True, D=24, nmax=12, shells=[(10.0, 16)], gauge="full", s1_constraint=True, q0_pin=1.0, w_int=100.0, w_s1=300.0, ball_radial="jacobi", emax=4.0), 0.05),
]:
    prob = Problem(cfg, device=dev)
    xs = make_init(prob, "s1_sym_v2", 1, extra={"q0": 1.0, "L": 1.0})
    cphi, cq, _ = prob.split(xs); prob.cfg.gauge_target = float(prob.gauge_integral(cphi[-1], cq[-1] * (prob.amp_of(xs)), prob.alpha))
    prob.r_offset = None
    r_star = prob.residual(xs).detach().clone()
    prob.r_offset = r_star
    r0 = prob.residual(xs); check(f"{label}: forced residual at x* is zero", float(torch.max(torch.abs(r0))), 1e-12)
    g = torch.Generator().manual_seed(5)
    x0 = xs * (1 + pert * torch.randn(xs.shape, generator=g, dtype=torch.float64).to(dev))
    if prob.ix_z0 is not None: x0[prob.ix_z0] = xs[prob.ix_z0] + 0.05
    if prob.ix_cl is not None: x0[prob.ix_cl] = xs[prob.ix_cl] + 0.01
    if prob.ix_a is not None: x0[prob.ix_a] = xs[prob.ix_a] + 0.1
    c0 = 0.5 * float(prob.residual(x0) @ prob.residual(x0))
    t0 = time.time()
    res = lm.lm_solve(prob, x0, max_iter=400, log=None, ftol=1e-16, xtol=1e-16, cl_bounds=cfg.cl_bounds)
    dt = time.time() - t0
    err_x = float(torch.norm(res["x"] - xs)) / float(torch.norm(xs))
    print(f"  {label}: nx={prob.nx} init cost {c0:.3e} -> {res['cost']:.3e} in {res['it']} iterations ({dt:.0f}s, status {res['status']}); |x-x*|/|x*| = {err_x:.2e}"
          + (f"; c_l recovered to {abs(float(res['x'][prob.ix_cl]) - cfg.cl):.2e}" if prob.ix_cl is not None else ""))
    check(f"{label}: LM converges to the manufactured solution (cost)", res["cost"], 1e-18 * max(1.0, c0))
    check(f"{label}: LM recovers x* (relative; null directions excluded by the gauge/S1 rows up to round-off)", err_x, 1e-6)
print(f"\n{len(FAILS)} failures")
if FAILS: print("FAILED:", FAILS); sys.exit(1)
