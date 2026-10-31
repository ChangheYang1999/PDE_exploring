"""Benchmark residual evaluation and Jacobian assembly on one GPU vs CPU at the Stage I ladder."""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.lm import jacobian_fwd
torch.set_default_dtype(torch.float64)

def bench(L, Nk, formulation, device, reps=3, chunk=128):
    model = Model(L=L, Nk=Nk, m_parity="even", R0=1.0, c_l=0.45, omega=1.0, device=device, free_params=True)
    prob = Problem(model, formulation=formulation)
    z = torch.randn(model.n_z, device=device) * 0.1; z[-2] = 0.45; z[-1] = 1.0
    prob.pivot = prob.choose_pivot(z)
    fun = prob.residual_vector
    r = fun(z)
    if device != "cpu": torch.cuda.synchronize()
    t0 = time.time()
    for _ in range(reps): r = fun(z)
    if device != "cpu": torch.cuda.synchronize()
    t_res = (time.time() - t0) / reps
    t0 = time.time()
    J = jacobian_fwd(fun, z, chunk=chunk)
    if device != "cpu": torch.cuda.synchronize()
    t_jac = time.time() - t0
    t0 = time.time()
    A = J.T @ J; Lc = torch.linalg.cholesky(A + 1e-3 * torch.diag(torch.diagonal(A)))
    if device != "cpu": torch.cuda.synchronize()
    t_lin = time.time() - t0
    mem = torch.cuda.max_memory_allocated() / 2**30 if device != "cpu" else 0.0
    rec = dict(L=L, Nk=Nk, Nr=model.Nr, Na=model.Na, n_z=model.n_z, n_res=r.numel(), formulation=formulation, device=device,
               t_residual=t_res, t_jacobian=t_jac, t_normal_eq=t_lin, gpu_mem_GB=mem)
    print(json.dumps(rec), flush=True)
    return rec

if __name__ == "__main__":
    dev = sys.argv[1] if len(sys.argv) > 1 else "cuda:0"
    out = []
    torch.set_num_threads(2)
    out.append(bench(6, 16, "vort", "cpu", reps=1, chunk=64))
    for (L, Nk) in [(6, 16), (10, 24), (14, 36)]:
        for f in ["vort", "mom", "both"]:
            torch.cuda.reset_peak_memory_stats()
            out.append(bench(L, Nk, f, dev))
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "..", "status", "benchmark.json"), "w"), indent=1)
