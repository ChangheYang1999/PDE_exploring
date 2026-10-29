"""Quick exploration of solver settings on small problems. Usage:
  python3 scripts/explore.py '{"cl":0.6,"D":24,"nmax":12,"shells":[[10,16]]}' gauss_core,ring_core 300 [lm|lbfgs|both] [seed]
Prints one summary line per (family) with holdout diagnostics. Saves states to scratch/.
"""
import os, sys, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np, torch
from axi.problem import Problem, Config
from axi.init import make_init
from axi import lm, diagnostics

torch.set_default_dtype(torch.float64)
over = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
fams = sys.argv[2].split(",") if len(sys.argv) > 2 else ["gauss_core"]
max_iter = int(sys.argv[3]) if len(sys.argv) > 3 else 200
opt = sys.argv[4] if len(sys.argv) > 4 else "lm"
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 1
tail = over.pop("tail", "mixed")
scale_core = over.pop("scale_core", 1.0)
cfg = Config(**{**over, "shells": [tuple(s) for s in over.get("shells", [(8.0, 16)])]})
dev = "cuda" if torch.cuda.is_available() else "cpu"
prob = Problem(cfg, device=dev)
print(f"cfg: {json.dumps(over)} nx={prob.nx} rows={prob.n_rows} gauge={cfg.gauge} phi_exps={[round(m*prob.alpha+k,3) for m,k in prob.ext_pairs_phi]} q_exps={[round(m*prob.alpha+k,3) for m,k in prob.ext_pairs_q]}")
os.makedirs("scratch", exist_ok=True)
for fam in fams:
    x0 = make_init(prob, fam, seed=seed, scale_core=scale_core, extra={"tail": tail})
    r0 = prob.residual(x0); c0 = 0.5 * float(r0 @ r0)
    for o in (["lm", "lbfgs"] if opt == "both" else [opt]):
        t0 = time.time()
        if o == "lm":
            res = lm.lm_solve(prob, x0, max_iter=max_iter, log=None, cl_bounds=cfg.cl_bounds)
        else:
            res = lm.lbfgs_solve(prob, x0, max_iter=max_iter, log=None)
        dt = time.time() - t0
        rep = diagnostics.report(prob, res["x"])
        print(f"[{o:5s} {fam:17s}] init {c0:.2e} -> cost {res['cost']:.3e} ({res['status']}, it {res['it']}, {dt:.0f}s) | {diagnostics.summarize(rep)}")
        tag = f"{fam}_{o}_" + "_".join(f"{k}{v}" for k, v in over.items() if k not in ("shells",))
        torch.save({"x": res["x"].cpu(), "cfg": cfg.to_json(), "history": res["history"], "report": rep}, f"scratch/{tag[:120]}.pt")
