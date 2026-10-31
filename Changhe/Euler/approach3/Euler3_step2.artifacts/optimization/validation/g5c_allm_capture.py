#!/usr/bin/env python
"""G5 (c) for the all-m class (lead 13:25:05Z item 1): capture of EVERY angular-table evaluation the production all-m residual, Jacobian path, pressure,
closure and O1 perform at S20_own (the P3 start): src.bases.solid_harmonics.eval_solid is wrapped in every src module during the case build (which
evaluates objective_at: residual, pressure, closure target, O1), one residual evaluation and one Jacobian forward-mode column (the field tables are
cached per model, so the Jacobian path uses the captured tables). For each distinct (points, modes, degree, derivative order) call the NODE LIST, the
MODE LIST (all (l, m) used, odd m included) and the PRODUCTION double-double tables (value, gradient, Hessian) are saved to validation/
g5c_allm_capture_<case>_arrays.npz (float64; sha256 in the JSON) so that the verifier can generate the 70-digit reference at exactly these nodes and
modes (lead item 1 (a)) and the entrywise comparison (item 1 (b), SPEC normalization) can be run on the two files. No comparison is made here.
Usage: python validation/g5c_allm_capture.py <case> [device]   (CPU intended; one core through the guard)"""
import sys, os, json, time, hashlib
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT, PAIRS, code_hashes
import src.bases.solid_harmonics as SH

DEFS = {"S20_own": dict(start=os.path.join(ROOT, "starts", "S20_s4allm_cl0.45_om1.0.pt")), "S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")),
        "manu_allm_c": dict(pair=PAIRS["c"], seed=8, m_parity="all")}
calls = []
_orig = SH.eval_solid


def recorder(y, modes, L, nderiv=2, path="auto"):
    out = _orig(y, modes, L, nderiv, path)
    # v2 (verifier 13:37:54Z): the metadata is recorded BEFORE any NumPy conversion, so that a conversion failure (functorch-wrapped tensors inside
    # torch.func.jvp have no accessible storage) stays attributable; for such calls the points are matched against every earlier recorded set by
    # torch.equal (an ordinary tensor op, allowed on wrapped tensors), which proves reuse of exactly the covered arguments or reports the failure.
    meta = dict(modes=np.array([[int(v) for v in m] for m in modes], dtype=np.int64), L=int(L), nderiv=int(nderiv), path=str(path), caller=sys._getframe(1).f_code.co_name,
                module=sys._getframe(1).f_globals.get("__name__"), shape=list(y.shape), tensor_type=type(y).__name__, in_jvp=bool(getattr(torch._C._functorch, "peek_interpreter_stack", lambda: None)() is not None) if hasattr(torch._C, "_functorch") else None)
    try:
        meta["points"] = y.detach().cpu().numpy().copy(); meta["tables"] = tuple(None if t is None else t.detach().cpu().numpy().copy() for t in out)
    except Exception as e:
        meta["conversion_error"] = repr(e); meta["matches_recorded_set"] = []
        for i, c in enumerate(calls):
            if "points" in c and list(c["points"].shape) == meta["shape"]:
                try:
                    eq = bool(torch.equal(y, torch.as_tensor(c["points"], dtype=y.dtype, device=y.device)))
                    same_modes = bool(np.array_equal(c["modes"], meta["modes"])) and c["L"] == meta["L"]
                    meta["matches_recorded_set"].append(dict(index=i, points_equal=eq, modes_and_L_equal=same_modes, nderiv_recorded=c["nderiv"], caller_recorded=c.get("caller")))
                except Exception as e2:
                    meta["matches_recorded_set"].append(dict(index=i, error=repr(e2)))
    calls.append(meta)
    return out


def main():
    cname = sys.argv[1]; dev = sys.argv[2] if len(sys.argv) > 2 else "cpu"
    out_json = os.path.join(ROOT, "validation", f"g5c_allm_capture_{cname}_v2.json"); out_npz = os.path.join(ROOT, "validation", f"g5c_allm_capture_{cname}_v2_arrays.npz")
    for p in (out_json, out_npz):
        if os.path.exists(p):
            raise FileExistsError(p)
    t0 = time.time()
    SH.eval_solid = recorder
    patched = []
    for modname in list(sys.modules):
        m = sys.modules[modname]
        if modname.startswith("src.") and getattr(m, "eval_solid", None) is _orig:
            setattr(m, "eval_solid", recorder); patched.append(modname)
    case = Case(cname, dev, **DEFS[cname]); prob, model = case.prob, case.model          # the constructor evaluates objective_at (residual, pressure, closure, O1)
    n_build = len(calls)
    with torch.no_grad():
        r, aux = prob.objective_at(case.z_full)                                               # one more full evaluation
    n_obj = len(calls)
    # one Jacobian forward-mode column (parameter c_l in physical coordinates): the Jacobian path's table use
    zp = case.z_phys.detach().clone(); e = torch.zeros_like(zp); e[zp.numel() - 2] = 1.0
    def fun(q):
        return prob.objective_at(case.to_full_phys(q), need_aux=False)[0]
    try:
        torch.func.jvp(fun, (zp,), (e,)); jvp_ok = True
    except Exception as ex:
        jvp_ok = repr(ex)
    n_jvp = len(calls)
    recs = [c for c in calls if "points" in c]; errs = [dict((k, v) for k, v in c.items() if k not in ("tables",)) for c in calls if "conversion_error" in c]
    for e_ in errs:
        e_["modes_count"] = int(e_["modes"].shape[0]); e_["modes_odd_m"] = int((np.abs(e_["modes"][:, 1]) % 2 == 1).sum()); e_["modes_sha256"] = hashlib.sha256(e_["modes"].tobytes()).hexdigest(); del e_["modes"]
        e_["reuses_covered_arguments"] = any(m.get("points_equal") and m.get("modes_and_L_equal") for m in e_.get("matches_recorded_set", []))
    distinct = {}; order = []
    for c in recs:
        key = hashlib.sha256(c["points"].tobytes() + c["modes"].tobytes() + bytes([c["L"], c["nderiv"]])).hexdigest()[:16]
        if key not in distinct:
            distinct[key] = c; order.append(key)
        distinct[key].setdefault("callers", set()).add(f"{c['module']}.{c['caller']}")
    arrays = {}; summary = []
    for i, key in enumerate(order):
        c = distinct[key]; tag = f"call{i:02d}"
        arrays[f"{tag}_points"] = c["points"]; arrays[f"{tag}_modes"] = c["modes"]
        for j, nm in enumerate(("A0", "A1", "A2")):
            if c["tables"][j] is not None:
                arrays[f"{tag}_{nm}"] = c["tables"][j]
        ms = c["modes"]; odd = int((np.abs(ms[:, 1]) % 2 == 1).sum()) if ms.size else 0
        summary.append(dict(tag=tag, key=key, n_points=int(c["points"].shape[0]), n_modes=int(ms.shape[0]), degrees=[int(ms[:, 0].min()), int(ms[:, 0].max())] if ms.size else None, n_odd_m_modes=odd, L=c["L"], nderiv=c["nderiv"], path=c["path"],
                            callers=sorted(c["callers"]), table_shapes=[None if t is None else list(t.shape) for t in c["tables"]], points_sha256=hashlib.sha256(c["points"].tobytes()).hexdigest(), modes_sha256=hashlib.sha256(ms.tobytes()).hexdigest()))
    np.savez(out_npz, **arrays, model_modes=np.array(model.modes, dtype=np.int64), L_ext=np.array(model.L_ext))
    rec = dict(case=cname, start=DEFS[cname].get("start"), m_parity=getattr(model, "m_parity", None), L=model.L, L_ext=model.L_ext, Nq=model.Nq, n_opt=int(case.z_opt.numel()), cost=float(case.cost), pair=[float(case.pair[0]), float(case.pair[1])],
               model_modes_count=len(model.modes), model_modes_odd_m=int(sum(1 for q in model.modes if abs(int(q[1])) % 2 == 1)), model_modes_degrees=[min(int(q[0]) for q in model.modes), max(int(q[0]) for q in model.modes)],
               calls_during_build=n_build, calls_during_objective_at=n_obj - n_build, calls_during_jvp=n_jvp - n_obj, jvp_ok=jvp_ok, unconverted_calls=errs, unconverted_calls_all_reuse_covered_arguments=bool(errs) and all(e_["reuses_covered_arguments"] for e_ in errs), distinct_calls=summary, patched_modules=patched,
               arrays_npz=out_npz, arrays_sha256=hashlib.sha256(open(out_npz, "rb").read()).hexdigest(), code_sha256=code_hashes(), script_sha256=hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
               device=dev, seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               note="capture only (no comparison): node lists, mode lists and the production double-double tables of every distinct angular-table evaluation of the all-m path at this case; the verifier's 70-digit reference at these nodes and modes and the entrywise comparison (G5 (c), <= 1e-13 relative with the floor 1e-13 x the largest entry of the same degree) follow as separate records")
    with open(out_json, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print(json.dumps({k: rec[k] for k in ("case", "m_parity", "L", "L_ext", "Nq", "model_modes_count", "model_modes_odd_m", "model_modes_degrees", "calls_during_build", "calls_during_objective_at", "calls_during_jvp", "jvp_ok")}, default=str))
    for s_ in summary:
        print(" ", s_["tag"], s_["n_points"], "points x", s_["n_modes"], "modes (odd m", s_["n_odd_m_modes"], ") L", s_["L"], "nderiv", s_["nderiv"], s_["callers"])
    print("DONE", out_json, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
