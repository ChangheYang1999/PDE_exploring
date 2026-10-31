import sys, os, time, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.lm import jacobian_fwd
torch.set_default_dtype(torch.float64)
dev = "cuda:0"
for (L, Nk) in [(6, 16), (10, 24)]:
    model = Model(L=L, Nk=Nk, m_parity="even", R0=1.0, c_l=0.45, omega=1.0, device=dev, free_params=False)
    prob = Problem(model, formulation="vort")
    z = torch.randn(model.n_z, device=dev) * 0.1
    prob.pivot = prob.choose_pivot(z)
    fun = prob.residual_vector
    fun(z); torch.cuda.synchronize()
    t0 = time.time(); [fun(z) for _ in range(10)]; torch.cuda.synchronize(); print(f"L={L} residual {((time.time()-t0)/10)*1e3:.1f} ms", flush=True)
    # sequential jvp cost
    e = torch.zeros_like(z); e[0] = 1
    torch.func.jvp(fun, (z,), (e,)); torch.cuda.synchronize()
    t0 = time.time(); [torch.func.jvp(fun, (z,), (e,)) for _ in range(5)]; torch.cuda.synchronize(); print(f"  single jvp {((time.time()-t0)/5)*1e3:.1f} ms", flush=True)
    for chunk in [32, 128, 512, 1024]:
        torch.cuda.reset_peak_memory_stats(); torch.cuda.synchronize(); t0 = time.time()
        J = jacobian_fwd(fun, z, chunk=chunk); torch.cuda.synchronize()
        print(f"  chunk {chunk}: jacobian {time.time()-t0:.2f}s  peak mem {torch.cuda.max_memory_allocated()/2**30:.1f} GB", flush=True)
