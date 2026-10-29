"""Lead note 29 item 3 (cheap decisive test, no new solver).  With phi frozen at a state's phi, let q* be the frozen-phi slaved swirl
(hard-pinned least squares of the PDE q rows, scripts/q_eigen_floor.py) and q_t = (1 - t) q_state + t q*.
  1. For t = 0, 0.1, ..., 1: the coupled weighted cost (all rows), its breakdown, and the holdout relative residuals rel R_q, rel R_eta
     (inner holdout grid) plus the shell of the maximum relative eta residual.
  2. At t = 0.5 and t = 1: re-optimize phi only (q frozen at q_t, scalars free) with Levenberg-Marquardt for --iters iterations; report
     the cost history, the final breakdown, rel R_q / rel R_eta on the holdout grid and (optionally, --validate) the SPEC 6.1 rho_max.
Usage: CUDA_VISIBLE_DEVICES= python3 scripts/homotopy_q_test.py <run_dir> [--iters 1000] [--validate]   -> runs/<id>/homotopy_q_test.json"""
import os, sys, json, math, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from axi.problem import Problem
from axi import diagnostics, lm, validate
torch.set_default_dtype(torch.float64); torch.set_num_threads(1)
DT = torch.float64


class FrozenQProblem:
    """phi (and the scalar unknowns) free, q frozen: residual/jacobian restricted to the non-q columns."""
    def __init__(self, prob, q):
        self.p = prob; self.cfg = prob.cfg; self.q = q.clone()
        self.outer = [i for i in range(prob.nx) if not (prob.nphi <= i < prob.nphi + prob.nq)]
        self.ix_cl = (self.outer.index(prob.ix_cl) if prob.ix_cl is not None else None)
        self.qcols = list(range(prob.nphi, prob.nphi + prob.nq))

    def cl_of(self, y):
        return float(y[self.ix_cl]) if self.ix_cl is not None else self.p.cl

    def embed(self, y):
        x = torch.zeros(self.p.nx, dtype=DT); x[self.outer] = y; x[self.qcols] = self.q
        return x

    def residual(self, y):
        return self.p.residual(self.embed(y))

    def jacobian(self, y):
        return self.p.jacobian(self.embed(y))[:, self.outer]


def holdout_rel(prob, x, cl):
    H = diagnostics.holdout_points(prob); R, mu, kind = H["R"], H["mu"], H["kind"]
    f = diagnostics.residual_fields(prob, x, R, mu, cl)
    inner = kind < 2
    sid = np.clip(np.floor(np.log2(np.maximum(R / prob.cfg.R1, 1e-300))).astype(int), -6, None)
    per_eta = {}
    for sh in np.unique(sid[inner]):
        m = (sid == sh) & inner
        per_eta[int(sh)] = float(np.sqrt(np.mean(f["Reta"][m] ** 2)) / max(np.sqrt(np.mean(f["terms_eta"][m] ** 2)), 1e-300))
    return dict(rel_Rq=float(np.sqrt(np.mean(f["Rq"][inner] ** 2)) / np.sqrt(np.mean(f["terms_q"][inner] ** 2))),
                rel_Reta=float(np.sqrt(np.mean(f["Reta"][inner] ** 2)) / np.sqrt(np.mean(f["terms_eta"][inner] ** 2))),
                worst_eta_shell=max(per_eta.items(), key=lambda t: t[1]), per_shell_eta=per_eta)


def main():
    run_dir = sys.argv[1].rstrip("/")
    iters = int(sys.argv[sys.argv.index("--iters") + 1]) if "--iters" in sys.argv else 1000
    do_val = "--validate" in sys.argv
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    prob, x = Problem.from_state(d, device="cpu")
    cl = prob.cl_of(x); z0 = prob.z0_of(x) or 0.0; q0 = prob.cfg.q0_pin
    qcols = list(range(prob.nphi, prob.nphi + prob.nq))
    # q*: hard-pinned least squares of ALL rows linear homogeneous in q at fixed phi (PDE q rows, q interface-continuity rows, q Tikhonov
    # rows, q-correction slave rows: lm.VarProProblem.inner), so that q* is continuous across the elements (the PDE-only solve of
    # scripts/q_eigen_floor.py gives q* = 0 outside the ball and is not a global swirl)
    vp = lm.VarProProblem(prob, full=False, trunc_rel=0.0); vp.x_full = x.clone()
    q_eig = vp.solve_q(x[vp.outer].clone()).clone()
    q_state = x[qcols].clone()
    out = dict(run=os.path.basename(run_dir), cl=cl, q0=q0, z0=z0, D=prob.cfg.D, nmax=prob.cfg.nmax, path=[], refits={})
    log = lambda m: print(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + " " + m, flush=True)
    for t in np.linspace(0, 1, 11):
        xt = x.clone(); xt[qcols] = (1 - t) * q_state + t * q_eig
        r = prob.residual(xt); cost = 0.5 * float(r @ r); cb = prob.cost_breakdown(xt); hr = holdout_rel(prob, xt, cl)
        rec = dict(t=float(t), cost=cost, eta_rows=sum(v for k, v in cb.items() if k.startswith("pde_eta")), q_rows=sum(v for k, v in cb.items() if k.startswith("pde_q")),
                   interface=cb["interface"], gauge=cb["gauge"], s1=cb.get("s1"), slave=cb.get("slave"), **{k: v for k, v in hr.items() if k != "per_shell_eta"})
        out["path"].append(rec)
        log(f"t {t:.1f}: cost {cost:.3e} (eta rows {rec['eta_rows']:.3e}, q rows {rec['q_rows']:.3e}, interface {cb['interface']:.2e}, gauge {cb['gauge']:.2e}) rel R_q {hr['rel_Rq']:.3e} rel R_eta {hr['rel_Reta']:.3e} worst eta shell {hr['worst_eta_shell']}")
    gauge_target0 = prob.cfg.gauge_target
    for t in (0.5, 1.0):
        xt = x.clone(); xt[qcols] = (1 - t) * q_state + t * q_eig
        # the dilation-gauge row int |F|^2 dS = target cannot be met with q frozen at q* (its swirl tail alone exceeds the target), and
        # the gauge is only a normalization: hold the gauge integral at its value for (phi, q_t) during the refit (reported separately)
        cphi, cq, _ = prob.split(xt)
        gI = float(prob.gauge_integral(cphi[-1], cq[-1], prob.alpha))
        prob.cfg.gauge_target = gI
        fp = FrozenQProblem(prob, xt[qcols]); y0 = xt[fp.outer].clone()
        hist = []
        def cb_(yc, rec, h):
            if rec["it"] % 100 == 0:
                log(f"   refit t {t}: it {rec['it']} cost {rec['cost']:.4e} lam {rec['lam']:.1e}")
        t0 = time.time()
        res = lm.lm_solve(fp, y0, max_iter=iters, lam0=1e-2, ftol=1e-13, time_limit=5400, callback=cb_, log=None, cl_bounds=prob.cfg.cl_bounds)
        xf = fp.embed(res["x"]); cb = prob.cost_breakdown(xf); hr = holdout_rel(prob, xf, cl)
        r_start = prob.residual(xt); cost_start = 0.5 * float(r_start @ r_start)
        rec = dict(t=t, status=res["status"], it=res["it"], gauge_target_used=gI, gauge_target_original=gauge_target0, cost_start=cost_start, cost_end=res["cost"], elapsed_s=time.time() - t0,
                   eta_rows=sum(v for k, v in cb.items() if k.startswith("pde_eta")), q_rows=sum(v for k, v in cb.items() if k.startswith("pde_q")), interface=cb["interface"],
                   gauge=cb["gauge"], s1=cb.get("s1"), slave=cb.get("slave"), cost_history=[h["cost"] for h in res["history"]][::10], **{k: v for k, v in hr.items() if k != "per_shell_eta"},
                   per_shell_eta=hr["per_shell_eta"], z0=prob.z0_of(xf), cl=prob.cl_of(xf))
        log(f"refit t {t}: {res['status']} after {res['it']} its, cost {rec['cost_start']:.3e} -> {res['cost']:.3e}; eta rows {rec['eta_rows']:.3e}, q rows {rec['q_rows']:.3e}; rel R_q {hr['rel_Rq']:.3e} rel R_eta {hr['rel_Reta']:.3e} worst eta shell {hr['worst_eta_shell']}; z0 {rec['z0']}")
        torch.save(dict(x=xf, cfg=prob.cfg.to_json(), gauge_target=prob.cfg.gauge_target, row_scale=[prob.cfg.w_q, prob.cfg.w_eta], note=f"homotopy refit t={t}"),
                   os.path.join(run_dir, f"homotopy_refit_t{t:.1f}.pt"))
        if do_val:
            v = validate.validate(prob, xf)
            rec["validation"] = dict(rho_max=v["rho_max"], m_max=v["m_max"], rho_max_by_eq=v.get("rho_max_by_eq"), s_core=v["s_core"], s_far=v["s_far"])
            log(f"   validation t {t}: rho_max {v['rho_max']:.3e} by eq {v.get('rho_max_by_eq')} s_core {v['s_core']:.3f}")
        out["refits"][str(t)] = rec
        json.dump(out, open(os.path.join(run_dir, "homotopy_q_test.json"), "w"), indent=1, default=float)
    prob.cfg.gauge_target = gauge_target0
    json.dump(out, open(os.path.join(run_dir, "homotopy_q_test.json"), "w"), indent=1, default=float)
    log("done")


if __name__ == "__main__":
    main()
