#!/usr/bin/env python
"""Benchmark the extended-channel model (memory and Jacobian time) before enqueueing: bench_extended.py L Nk LB LD [NkB] [--device]"""
import sys, os, time, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.tail_constraints import TailConstraints
L, Nk, LB, LD = [int(v) for v in sys.argv[1:5]]; NkB = int(sys.argv[5]) if len(sys.argv) > 5 else 4
dev = "cuda:0"
ch = dict(NkB=NkB, NkD=NkB, NkE=NkB, core_damp=2, LB=LB, LD=LD, LE=L)
model = Model(L=L, Nk=Nk, R0=0.3, Nr=3 * Nk, c_l=0.45, omega=0.3, channels=ch, device=dev, extra_r=[4096.0, 16384.0, 65536.0])
prob = Problem(model, formulation="mom", nl_weighting=True, far_radii=None)
tc = TailConstraints(model)
print(f"L {L} Nk {Nk} LB {LB} LD {LD}: Nq {model.Nq} n_z {model.n_z} n_red {tc.n_red} grid {model.ntheta}x{model.nphi} Nr {model.Nr} Lf {model.Lf} residual rows {3 * model.Nr * model.Na}", flush=True)
z = torch.randn(tc.n_red, device=dev) * 0.1
fun = lambda zr: prob.residual_vector(tc.expand(zr))
t0 = time.time(); r = fun(z); torch.cuda.synchronize(); t_res = time.time() - t0
print(f"residual: {r.numel()} rows, {t_res:.2f}s, mem {torch.cuda.max_memory_allocated()/2**30:.1f} GB", flush=True)
from src.optimization.lm import jacobian_fwd as jacobian_chunked
for chunk in (int(os.environ.get("BENCH_CHUNK", "256")),):
    torch.cuda.reset_peak_memory_stats(); t0 = time.time()
    J = jacobian_chunked(fun, z, chunk=chunk); torch.cuda.synchronize(); tj = time.time() - t0
    print(f"jacobian chunk {chunk}: {tuple(J.shape)} {tj:.1f}s, peak mem {torch.cuda.max_memory_allocated()/2**30:.1f} GB", flush=True)
    JtJ = J.T @ J; torch.cuda.synchronize()
    print(f"normal matrix {tuple(JtJ.shape)}; peak mem {torch.cuda.max_memory_allocated()/2**30:.1f} GB; cond estimate {torch.linalg.cond(JtJ).item():.2e}", flush=True)
