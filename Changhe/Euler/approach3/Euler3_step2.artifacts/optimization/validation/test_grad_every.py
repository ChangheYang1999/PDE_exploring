"""D6FP 2026-10-29: synthetic regression of the R5 complete-gradient spacing in lm_solve_free (grad_every): with lag_jacobian on and grad_every 4,
the complete gradient must be present at every accepted step taken with a fresh J and at every accepted step whose running accepted count is a
multiple of 4, and marked skipped (with the policy text) at the other reused-J steps; with grad_every 1 it is present at every accepted step.
The gradient values at evaluated steps must equal those of the grad_every 1 run at the same iterates. Writes validation/test_grad_every.json."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.optimization.lm import lm_solve_free
torch.manual_seed(0)
n, m = 12, 60
A = torch.randn(m, n); b = torch.randn(m) * 0.1
def resid(z):
    return A @ z + 0.3 * (z ** 2).sum() * torch.ones(m) * 0.05 + 0.2 * torch.sin(z[:1]) * torch.ones(m) - b
def objective(z):
    r = resid(z); return r, dict(r=r)
def commit(aux): pass
calls = {"n": 0}
def grad_fun(z):
    calls["n"] += 1
    zz = z.detach().clone().requires_grad_(True); r = resid(zz); c = 0.5 * (r @ r); g, = torch.autograd.grad(c, zz); return g.detach()
z0 = torch.ones(n) * 2.0
out = {}
for ge in (1, 4):
    calls["n"] = 0
    res = lm_solve_free(resid, z0.clone(), param_idx=(n - 2, n - 1), objective=objective, commit=commit, max_iter=60, lam0=1e-2, chunk=16, verbose=False, log=None,
                        ftol=1e-16, xtol=1e-16, lag_jacobian=dict(max_reuse=8, rho_min=0.25), grad_fun=grad_fun, grad_every=ge)
    h = [r for r in res["history"] if r["accepted"]]
    n_acc = 0; ok = True; detail = []
    for r in h:
        n_acc += 1
        cg = r.get("complete_gradient") or {}
        evaluated = ("g_2" in cg); skipped = bool(cg.get("skipped"))
        due = r["J_fresh"] or ge <= 1 or (n_acc % ge == 0)
        ok &= (evaluated == due) and (skipped == (not due))
        detail.append(dict(it=r["it"], n_acc=n_acc, J_fresh=r["J_fresh"], J_age=r["J_age"], evaluated=evaluated, skipped=skipped, due=due, g_2=cg.get("g_2")))
    out[f"grad_every_{ge}"] = dict(n_accepted=len(h), grad_calls=calls["n"], n_evaluated=sum(d["evaluated"] for d in detail), n_skipped=sum(d["skipped"] for d in detail), rule_ok=ok, status=res["status"], cost=res["cost"], detail=detail)
# values at common evaluated iterates agree (same trajectory: the gradient does not influence the steps)
d1 = {d["it"]: d["g_2"] for d in out["grad_every_1"]["detail"]}; d4 = {d["it"]: d["g_2"] for d in out["grad_every_4"]["detail"] if d["evaluated"]}
same_traj = abs(out["grad_every_1"]["cost"] - out["grad_every_4"]["cost"]) <= 1e-14 * max(1.0, out["grad_every_1"]["cost"])
agree = all(abs(d1[k] - v) <= 1e-12 * max(1.0, abs(v)) for k, v in d4.items() if k in d1)
out["checks"] = dict(rule_ok_1=out["grad_every_1"]["rule_ok"], rule_ok_4=out["grad_every_4"]["rule_ok"], same_trajectory=same_traj, gradients_agree_at_common_iterates=agree,
                     fewer_calls_with_4=out["grad_every_4"]["grad_calls"] < out["grad_every_1"]["grad_calls"], skipped_present=out["grad_every_4"]["n_skipped"] > 0)
out["all_pass"] = all(out["checks"].values())
json.dump(out, open(os.path.join(os.path.dirname(__file__), "test_grad_every.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "grad_every_1" and k != "grad_every_4"}), {k: {kk: vv for kk, vv in v.items() if kk != "detail"} for k, v in out.items() if k.startswith("grad_every")})
print("ALL_PASS", out["all_pass"])
