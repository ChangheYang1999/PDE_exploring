"""Lead note 25 item 4: for the frozen (phi, c_l) of a state, the q equation is linear and homogeneous in q.  Solve
    min || W (R_q(q)) ||   over the q coefficients, with the pin q(0, z0) = q0 as a HARD row (null-space elimination),
using the job's own row weights (the PDE q rows of Problem.residual, i.e. sqrt(w_node) scale_q R_q), and report the floor of the
holdout relative q residual per dyadic shell and the shell of the maximum, plus the relative distance between the eigen-solved q and
the state's q.  A floor of order 1e-3 means the state's q residual is a trade-off against the eta rows (variable projection is the
right solver); a floor at the percent level means the q basis cannot represent the transport eigenfunction of that phi.
Usage: CUDA_VISIBLE_DEVICES=<gpu> python3 scripts/q_eigen_floor.py <run_dir> [...]"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from axi.problem import Problem
from axi import diagnostics
torch.set_default_dtype(torch.float64)
dev = "cuda" if torch.cuda.is_available() else "cpu"
for run_dir in sys.argv[1:]:
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    prob, x = Problem.from_state(d, device=dev)
    cl = prob.cl_of(x); z0 = prob.z0_of(x) or 0.0; q0 = prob.cfg.q0_pin
    # linear operator of the weighted q rows w.r.t. the q coefficients (R_q is linear in q at fixed phi: the Jacobian block is exact)
    J = prob.jacobian(x)
    n0 = 0; rows = []
    for i in range(prob.nel):
        n = prob.n_nodes_per_el[i]; rows += list(range(n0, n0 + n)); n0 += 2 * n          # q rows of element i (eta rows skipped)
    qcols = list(range(prob.nphi, prob.nphi + prob.nq))
    A = J[rows][:, qcols].cpu().numpy()
    r_state = prob.residual(x)[rows].cpu().numpy()
    # hard pin: s . c = q0, with s the axis evaluation row of q at (0, z0); null-space elimination c = c_p + N y
    _, _, _, mu0, s_full, _ = prob.axis_phi_rows(z0, with_q=True)
    s = s_full[prob.nphi:prob.nphi + prob.nq]
    c_p = s * (q0 / float(s @ s))
    Q, _ = np.linalg.qr(s[:, None], mode="complete"); N = Q[:, 1:]                      # orthonormal basis of {s . c = 0}
    AN = A @ N; b = -(A @ c_p)
    cs = np.max(np.abs(AN), axis=0); cs[cs == 0] = 1.0
    y, *_ = np.linalg.lstsq(AN / cs, b, rcond=None); c_eig = c_p + N @ (y / cs)
    r_eig = A @ c_eig
    x_eig = x.clone(); x_eig[prob.nphi:prob.nphi + prob.nq] = torch.tensor(c_eig, device=dev)
    pin_check = float(s @ c_eig) - q0
    # holdout relative q residual per dyadic shell for the state and for the eigen-solved q
    out = {}
    for tag, xx in (("state", x), ("eigen", x_eig)):
        H = diagnostics.holdout_points(prob); R, mu, kind = H["R"], H["mu"], H["kind"]
        f = diagnostics.residual_fields(prob, xx.cpu(), R, mu, cl)
        sid = np.clip(np.floor(np.log2(np.maximum(R / prob.cfg.R1, 1e-300))).astype(int), -6, None)
        per = {}
        for sh in np.unique(sid):
            m = sid == sh
            per[int(sh)] = float(np.sqrt(np.mean(f["Rq"][m] ** 2)) / max(np.sqrt(np.mean(f["terms_q"][m] ** 2)), 1e-300))
        inner = kind < 2
        out[tag] = dict(rel_Rq_inner=float(np.sqrt(np.mean(f["Rq"][inner] ** 2)) / np.sqrt(np.mean(f["terms_q"][inner] ** 2))), per_shell=per,
                        worst_shell=max(per.items(), key=lambda t: t[1]))
    qs = x[prob.nphi:prob.nphi + prob.nq].cpu().numpy()
    out["weighted_cost_q_rows"] = dict(state=float(0.5 * r_state @ r_state), eigen=float(0.5 * r_eig @ r_eig))
    out["q_coeff_rel_diff"] = float(np.linalg.norm(c_eig - qs) / np.linalg.norm(qs)); out["pin_check"] = pin_check
    out["cl"] = cl; out["q0"] = q0; out["z0"] = z0; out["D"] = prob.cfg.D; out["nmax"] = prob.cfg.nmax
    json.dump(out, open(os.path.join(run_dir, "q_eigen_floor.json"), "w"), indent=1, default=float)
    print(os.path.basename(run_dir)[:46], f"cl {cl:.4f} q0 {q0} D{prob.cfg.D}/n{prob.cfg.nmax}")
    print(f"   state : rel R_q inner {out['state']['rel_Rq_inner']:.3e}, worst shell {out['state']['worst_shell']}, weighted q-row cost {out['weighted_cost_q_rows']['state']:.3e}")
    print(f"   eigen : rel R_q inner {out['eigen']['rel_Rq_inner']:.3e}, worst shell {out['eigen']['worst_shell']}, weighted q-row cost {out['weighted_cost_q_rows']['eigen']:.3e}; |q_eig - q|/|q| = {out['q_coeff_rel_diff']:.3e}; pin check {pin_check:.1e}")
    print("   eigen per shell:", {k: round(v, 4) for k, v in out["eigen"]["per_shell"].items()})
