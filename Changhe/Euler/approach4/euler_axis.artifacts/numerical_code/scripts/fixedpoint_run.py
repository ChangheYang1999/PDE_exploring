"""Run the Newton-Krylov fixed point from an S1 seed.  Usage: python3 scripts/fixedpoint_run.py cl q0 D nmax maxiter [tag]"""
import os, sys, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from axi.problem import Problem, Config
from axi.init import make_init
from axi.fixedpoint import FixedPoint
torch.set_default_dtype(torch.float64)
cl = float(sys.argv[1]); q0 = float(sys.argv[2]); D = int(sys.argv[3]); nmax = int(sys.argv[4]); maxiter = int(sys.argv[5]); tag = sys.argv[6] if len(sys.argv) > 6 else "fp"
unknown = sys.argv[7] if len(sys.argv) > 7 else "q0"
cfg = Config(cl=cl, D=D, nmax=nmax, shells=[(10.0, max(8, int(D * 2 / 3)))], R1=2.0, gauge="full", s1_constraint=True, ball_radial="jacobi", emax=4.0, w_int=100.0)
prob = Problem(cfg, device="cpu")
x = make_init(prob, "s1_sym_v2", 1, extra={"q0": q0, "L": 1.0}).cpu()
cphi, cq, _ = prob.split(x); cphi0 = [c.numpy().copy() for c in cphi]
fp = FixedPoint(prob, z0_init=0.0, unknown=unknown, q0_fixed=q0)
t0 = time.time()
F0 = fp.F(fp.pack(cphi0, q0 if unknown == "q0" else cl)); print(f"seed: |F| {np.linalg.norm(F0):.3e} q-eig rel {fp.last['q_rel']:.2e} eta rel {fp.last['eta_rel']:.2e} Phi_z {fp.last['Phi_z']:+.4f} ({time.time()-t0:.1f}s per F)", flush=True)
res = fp.solve(cphi0, q0 if unknown == "q0" else cl, maxiter=maxiter)
print("status", res["status"], "|F|", res["Fnorm"], "q0", res["y"][-1], "z0", fp.last.get("z0"), "q_rel", fp.last.get("q_rel"), "eta_rel", fp.last.get("eta_rel"))
out = os.path.join(ROOT, "scratch", f"{tag}_cl{cl}_q{q0}_D{D}.pt")
cphi_f, last_f = fp.unpack(res["y"]); q0_f = last_f if unknown == "q0" else q0
xf = x.clone()
for i in range(prob.nel):
    xf[prob.off_phi[i]:prob.off_phi[i + 1]] = torch.tensor(cphi_f[i])
xf[prob.nphi:prob.nphi + prob.nq] = torch.tensor(q0_f * fp.last["cq"])
if prob.ix_z0 is not None: xf[prob.ix_z0] = fp.last.get("z0", 0.0)
cfg.cl = fp.cl
torch.save(dict(x=xf, cfg=cfg.to_json(), hist=res["hist"], status=res["status"], q0=q0_f, cl=fp.cl, unknown=unknown, method="newton_krylov_fixed_point"), out)
json.dump(res["hist"], open(out.replace(".pt", "_hist.json"), "w"), indent=1)
print("saved", out)
