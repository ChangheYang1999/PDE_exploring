#!/usr/bin/env python
"""Deliverable C measurement (lead 11:09:15Z item 2): cost of the chunked coefficient Jacobian (lm.jacobian_fwd of residual_vector_wd, chunk as in
production) at S01_own with FREE parameters (the parameter coordinates are live inputs: the parameter-dependent construction of the fields and
rows is differentiated in every chunk, with zero tangents in all but two directions) against the same build on a model with FIXED parameters
(free_params False, same coefficients and parameter values), plus the two parameter columns (param_columns with differentiable pressure) of the
FREE model. Two repetitions each, GPU-synchronized timings; no production change. Usage: python validation/jac_cost.py [device]"""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation.gates import Case, ROOT, PROD
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.lm import jacobian_fwd, param_columns


def sync():
    if torch.cuda.is_available():
        torch.cuda.synchronize()


def timed(f, reps=2):
    out = []
    for _ in range(reps):
        sync(); t0 = time.time(); r = f(); sync(); out.append(time.time() - t0)
    return out


def main():
    dev = sys.argv[1] if len(sys.argv) > 1 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    case = Case("S01_own", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob, model = case.prob, case.model
    zo = case.z_opt.detach().clone(); n = zo.numel(); chunk = 128
    fun_free = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
    pfun_free = lambda q: prob.residual_vector_wd(case.to_full_opt(q), differentiable_pressure=True)
    with torch.no_grad():
        zf = case.to_full_opt(zo)
    t_free = timed(lambda: jacobian_fwd(fun_free, zo, chunk=chunk))
    t_par = timed(lambda: param_columns(pfun_free, zo, [n - 2, n - 1]))
    # fixed-parameter model at the same point: free_params False, same channels, same coefficients
    mf = Model(L=model.L, Nk=model.Nk, Nr=model.Nr, m_parity=model.m_parity, R0=model.R0, c_l=float(zf[-2]), omega=float(zf[-1]), free_params=False, channels=model.channels, device=dev, extra_r=model.extra_r)
    pf = Problem(mf, **PROD)
    from src.optimization.tail_constraints import TailConstraints
    tcf = TailConstraints(mf)
    z_coef_full = zf[: mf.n_coef] if hasattr(mf, "n_coef") else zf[:-2]
    zr_fixed = tcf.reduce(z_coef_full)
    pf.pivot = prob.pivot; pf.ensure_geometry(z_coef_full)
    with torch.no_grad():
        r0, aux0 = pf.objective_at(z_coef_full); pf.commit_aux(aux0)
    fun_fixed = lambda q: pf.residual_vector_wd(tcf.expand(q))
    t_fixed = timed(lambda: jacobian_fwd(fun_fixed, zr_fixed, chunk=chunk))
    rec = dict(case="S01_own", device=dev, chunk=chunk, n_free=int(n), n_fixed=int(zr_fixed.numel()), jacobian_free_s=t_free, jacobian_fixed_s=t_fixed, param_columns_free_s=t_par,
               ratio_free_over_fixed=(sum(t_free) / len(t_free)) / (sum(t_fixed) / len(t_fixed)), gpu_shared_with=("other jobs on this GPU: see nvidia-smi at run time"),
               note="FREE: residual_vector_wd(to_full_opt(q)) over all N coordinates (parameters live, tables held); FIXED: the same function on a free_params=False model with the same coefficients and parameter values; the difference is the differentiated parameter-dependent construction (basis and twist tables, tail reduction, parameter map, scale_mom, closure patterns) carried in every chunk of the FREE build",
               ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    print(json.dumps(rec, indent=1))
    json.dump(rec, open(os.path.join(ROOT, "validation", "jac_cost_S01_own.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
