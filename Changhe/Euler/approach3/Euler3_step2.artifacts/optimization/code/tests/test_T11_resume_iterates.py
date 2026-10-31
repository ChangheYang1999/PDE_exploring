"""SPEC T11 (restart determinism): kill/resume from a checkpoint reproduces the next 10 iterations to 1e-10 (lead 2026-10-25T05:42Z asks for
the ten post-resume iterates with damping, pivot, optimizer state and metric definitions). This test exercises the worker's resume path at the
API level with the same ingredients the worker checkpoints and restores (reduced coefficient vector z, LM damping lam, pivot; on resume the
nonlinear weights are recomputed from z as the worker does): run A = 13 LM iterations uninterrupted, run B = 3 iterations, snapshot (z, lam,
pivot), a fresh Problem object, 10 more iterations from the snapshot; iterates 4..13 of A and 1..10 of B are compared (coefficients, damping,
cost, acceptance flag). The LM state is exactly (z, lam) plus the frozen per-iteration weights, so the agreement should be at roundoff."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
# GEMM determinism: cuBLAS may choose split-K kernels with atomic reductions whose summation order varies between calls; the worker runs
# without this setting, so the test reports both the default and the deterministic-mode agreement (set DETERMINISTIC=0 to skip the latter)
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")      # needed before the first CUDA call if deterministic mode is switched on later
DET = False                                                       # set per run below (both modes are run and logged: verifier 2026-10-25T06:31Z)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.tail_constraints import TailConstraints
from src.optimization.lm import lm_solve

def make(device):
    model = Model(L=2, Nk=8, m_parity="even", R0=0.5, Nr=24, c_l=0.45, omega=0.7, device=device)
    prob = Problem(model, formulation="mom", nl_weighting=True, nl_denominator="all5")
    tc = TailConstraints(model)
    return model, prob, tc

def run_lm(prob, tc, z0, lam0, n_iter, pivot=None):
    model = prob.model
    if pivot is not None:
        prob.pivot = pivot
    elif prob.pivot is None:
        prob.pivot = prob.choose_pivot(tc.expand(z0))
    prob.update_nl_weights(tc.expand(z0))
    fun = lambda zr: prob.residual_vector(tc.expand(zr))
    proj = lambda zr: tc.reduce(prob.phase_align(tc.expand(zr)))
    rows = []
    def cb(it, zc, cost, rec):
        rows.append(dict(z=zc.detach().clone(), lam=rec["lam"], cost=cost, accepted=rec["accepted"]))
        if rec.get("accepted", True):
            prob.update_nl_weights(tc.expand(zc)); return True
        return False
    out = lm_solve(fun, z0.clone(), max_iter=n_iter, lam0=lam0, chunk=64, callback=cb, project=proj, verbose=False, ftol=0.0, xtol=0.0)
    return rows, out

def run(device=None, deterministic=False):
    global DET
    DET = deterministic
    torch.use_deterministic_algorithms(bool(deterministic), warn_only=True)
    device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    torch.manual_seed(21)
    model, probA, tc = make(device)
    z0 = torch.randn(tc.n_red, device=device) * 0.2
    rowsA, _ = run_lm(probA, tc, z0, 1e-2, 13)
    # run B: 3 iterations, checkpoint (z, lam, pivot), fresh Problem, 10 more iterations
    model2, probB, tc2 = make(device)
    rowsB1, _ = run_lm(probB, tc2, z0, 1e-2, 3)
    ck = dict(z=rowsB1[-1]["z"].clone(), lam=rowsB1[-1]["lam"], pivot=dict(probB.pivot))
    model3, probC, tc3 = make(device)
    rowsB2, _ = run_lm(probC, tc3, ck["z"], ck["lam"], 10, pivot=ck["pivot"])
    worst_z = 0.0; worst_lam = 0.0; worst_cost = 0.0; acc_ok = True
    for k in range(10):
        a, b = rowsA[3 + k], rowsB2[k]
        worst_z = max(worst_z, float((a["z"] - b["z"]).abs().max() / a["z"].abs().max()))
        worst_lam = max(worst_lam, abs(a["lam"] - b["lam"]) / a["lam"]); worst_cost = max(worst_cost, abs(a["cost"] - b["cost"]) / a["cost"])
        acc_ok = acc_ok and (a["accepted"] == b["accepted"])
    print(f"T11 ten post-resume iterates (4..13) vs the uninterrupted run ({'deterministic cuBLAS' if DET else 'default cuBLAS'}): coefficients {worst_z:.1e}, damping {worst_lam:.1e}, cost {worst_cost:.1e}, acceptance flags equal: {acc_ok}; first-three agreement {float((rowsA[2]['z'] - rowsB1[2]['z']).abs().max()):.1e}")
    ok = worst_z < 1e-10 and worst_lam < 1e-10 and acc_ok          # SPEC T11: the next 10 iterations (coefficient vectors and damping) to 1e-10; the cost is reported
    print("T11 PASS" if ok else "T11 FAIL")
    return ok

if __name__ == "__main__":
    ok1 = run(deterministic=False); ok2 = run(deterministic=True)
    sys.exit(0 if (ok1 and ok2) else 1)
