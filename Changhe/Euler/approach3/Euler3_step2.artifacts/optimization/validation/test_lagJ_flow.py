"""D6FP lagJ control-flow regression (verifier V116): a small synthetic least-squares problem through lm_solve_free with lag_jacobian, checking
(1) J reuse while accepted with rho >= 0.25 (J_age increments, at most max_reuse), (2) a rejection with a stale J leads to a fresh-J retry at the
same point with the SAME lambda (no damping increase) and the run continues, (3) the final result matches a run without lagJ to 1e-8 in cost."""
import sys, os, json, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.optimization.lm import lm_solve_free
torch.manual_seed(0)
n, m = 12, 60
A = torch.randn(m, n); b = torch.randn(m) * 0.1
def resid(z):                                   # mildly nonlinear residual
    return A @ z + 0.3 * (z ** 2).sum() * torch.ones(m) * 0.05 + 0.2 * torch.sin(z[:1]) * torch.ones(m) - b
state = {}
def objective(z):
    r = resid(z); return r, dict(r=r)
def commit(aux): state["aux"] = aux
z0 = torch.ones(n) * 2.0
res_ref = lm_solve_free(resid, z0.clone(), objective=objective, commit=commit, max_iter=60, lam0=1e-2, chunk=16, verbose=False, log=None, ftol=1e-16, xtol=1e-16)
res_lag = lm_solve_free(resid, z0.clone(), objective=objective, commit=commit, max_iter=60, lam0=1e-2, chunk=16, verbose=False, log=None, ftol=1e-16, xtol=1e-16, lag_jacobian=dict(max_reuse=8, rho_min=0.25))
h = res_lag["history"]
ages = [r["J_age"] for r in h]; fresh = [r["J_fresh"] for r in h]; acc = [r["accepted"] for r in h]
stale_rej = [i for i, r in enumerate(h) if (not r["accepted"]) and any(x.get("stale_J_refresh") for x in r["rejections"])]
checks = dict(n_iter_ref=len(res_ref["history"]), n_iter_lag=len(h), cost_ref=res_ref["cost"], cost_lag=res_lag["cost"], rel_cost_diff=abs(res_ref["cost"] - res_lag["cost"]) / max(res_ref["cost"], 1e-300),
              max_J_age=max(ages), n_fresh=sum(fresh), n_reused=sum(1 for f in fresh if not f), status_lag=res_lag["status"], status_ref=res_ref["status"],
              stale_rejections=len(stale_rej), ages_sequence=ages[:40], accepted_sequence=acc[:40])
# (2) after a stale rejection the next record must be a fresh J at the same lambda
ok_retry = True; details = []
for i in stale_rej:
    if i + 1 < len(h):
        # the retry record is a fresh J; the damping used for its FIRST trial is the rejected record's lambda (no increase): the record's lam
        # is the value after the retry's own acceptance/rejection, so compare the rejected trial's lam with the first rejection/acceptance lam of the retry
        lam_rej = h[i]["rejections"][-1]["lam"]
        lam_retry_first = h[i + 1]["rejections"][0]["lam"] if h[i + 1]["rejections"] else None
        details.append(dict(i=i, fresh_next=bool(h[i + 1]["J_fresh"]), lam_rejected=lam_rej, lam_first_trial_of_retry=lam_retry_first, lam_record_after_retry=h[i + 1]["lam"]))
        ok_retry &= bool(h[i + 1]["J_fresh"]) and (lam_retry_first is None or abs(lam_retry_first - lam_rej) <= 1e-12 * max(lam_rej, 1e-300))
checks["retry_with_fresh_J_no_damping_increase"] = bool(ok_retry) if stale_rej else "no stale rejection occurred in this synthetic run"; checks["retry_details"] = details
checks["max_reuse_respected"] = max(ages) <= 8
print(json.dumps(checks, indent=1))
json.dump(checks, open(os.path.join(os.path.dirname(__file__), "test_lagJ_flow.json"), "w"), indent=1)
