"""D6FP G5 (c) for the exact closure route (lead 23:08Z item 4, 23:41Z item 2 (b)): every angular table the production closure path evaluates
(first_correction, carried_patterns, closure_distance through homogeneous_velocity_exact / twisted_scalar_gradient_exact / _HomogeneousModel) is
recorded by wrapping src.bases.solid_harmonics.eval_solid during one closure_state_at call on S01 and S05 (points, modes, degree, derivative
order), then compared ENTRYWISE with the verifier's 70-digit reference (d6-ver scripts/verify_angular_tables.py: compiled, decimal_values; read
only) at exactly those points: binary64-rounded reference against the production double-double tables (values, gradients, Hessians).
Pass: every entry within one unit in the last place after normalization by the per-point table scale (the criterion of check_angular_dd.py),
exact matches counted. Output validation/g5c_closure_grid.json."""
import sys, os, json, time, hashlib
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT)
VER = "RUN_ROOT/verifier"
sys.path.insert(0, os.path.join(VER, "scripts")); sys.path.insert(0, os.path.join(VER, "independent", "src"))
import numpy as np, torch
import mpmath as _mp
_mp.mp.dps = 80                      # the verifier script sets mp.mp.dps = 80 only inside its main(): without it, compiled() builds the normalization factor at 15 digits (the cause of the spurious 1.4-ulp "errors" of the first run, 00:32Z)
torch.set_default_dtype(torch.float64)
from decimal import Decimal, getcontext
from validation.gates import Case, ROOT
import src.bases.solid_harmonics as SH
import src.far_field.correction as C
calls = []
_orig = SH.eval_solid
def recorder(y, modes, L, nderiv=2, path="auto"):
    out = _orig(y, modes, L, nderiv, path)
    try:
        calls.append(dict(points=y.detach().cpu().numpy().copy(), modes=[tuple(int(v) for v in m) for m in modes], L=int(L), nderiv=int(nderiv), path=path,
                          caller=sys._getframe(1).f_code.co_name, tables=tuple(None if t is None else t.detach().cpu().numpy().copy() for t in out)))
    except Exception as e:
        calls.append(dict(error=repr(e)))
    return out
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
SH.eval_solid = recorder; C.eval_solid = recorder if hasattr(C, "eval_solid") else None
for mod in (C,):
    for name in dir(mod):
        pass
# the closure modules import eval_solid by name in several places: patch every module attribute that is the original function
import importlib
patched = []
for modname in list(sys.modules):
    m = sys.modules[modname]
    if modname.startswith("src.") and getattr(m, "eval_solid", None) is _orig:
        setattr(m, "eval_solid", recorder); patched.append(modname)
out = dict(started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), patched_modules=patched, cases={})
for cname, fn in (("S01", "S01_nest6_cl0.45_om1.0_p0.pt"), ("S05", "S05_nest6_cl0.45_om0.3_p0.pt")):
    case = Case(cname, dev, start=os.path.join(ROOT, "starts", fn))              # the Case constructor itself calls closure_state_at through objective_at
    del calls[:]
    cl = case.prob.closure_state_at(case.z_full)                               # first_correction + carried_patterns on the exact route
    V = case.prob.closure_distance(case.z_full) if hasattr(case.prob, "closure_distance") else None
    recs = [c for c in calls if "points" in c]
    out["cases"][cname] = dict(n_calls=len(recs), calls=[dict(n_points=int(c["points"].shape[0]), n_modes=len(c["modes"]), L=c["L"], nderiv=c["nderiv"], path=c["path"], caller=c["caller"]) for c in recs])
    print(cname, "closure-path table calls:", json.dumps(out["cases"][cname]["calls"]), flush=True)
    # entrywise reference for each distinct (points, modes, L, nderiv)
    from verify_angular_tables import compiled, decimal_values, AXES
    getcontext().prec = 70
    checks = []
    seen = set()
    for c in recs:
        key = (hashlib.sha256(c["points"].tobytes()).hexdigest()[:16], tuple(c["modes"]), c["L"], c["nderiv"])
        if key in seen:
            continue
        seen.add(key)
        polys = [compiled(m) for m in c["modes"]]; powers = set(p for norm, rows in polys for row in rows for p, cc in row)
        A0, A1, A2 = c["tables"]; N = c["points"].shape[0]; Nq = len(c["modes"])
        ncol = 1 + (3 if A1 is not None else 0) + (9 if A2 is not None else 0)
        table = np.concatenate([A0[:, :, None]] + ([A1.transpose(1, 2, 0)] if A1 is not None else []) + ([A2.transpose(2, 3, 0, 1).reshape(N, Nq, 9)] if A2 is not None else []), axis=2)
        n_exact = 0; n_tot = 0; max_norm_err = 0.0; max_abs_err = 0.0; t0 = time.time()
        for i in range(N):
            vv = decimal_values(c["points"][i], polys, powers)
            scale = max(abs(float(table[i, q, k])) for q in range(Nq) for k in range(ncol)) or 1.0
            for q in range(Nq):
                for k in range(ncol):
                    ref = vv[q][k]; refd = float(ref); prod = float(table[i, q, k])
                    n_tot += 1; n_exact += (refd == prod)
                    err = abs(Decimal.from_float(prod) - ref)
                    max_abs_err = max(max_abs_err, float(err)); max_norm_err = max(max_norm_err, float(err) / scale)
        checks.append(dict(n_points=N, n_modes=Nq, L=c["L"], nderiv=c["nderiv"], entries=n_tot, exact_matches=n_exact, exact_fraction=n_exact / n_tot, max_normalized_error=max_norm_err, max_abs_error=max_abs_err,
                           pass_1ulp_normalized=bool(max_norm_err <= 2.3e-16), seconds=time.time() - t0, caller=c["caller"]))
        print(f"  {cname} {c['caller']}: {N} points x {Nq} modes (L {c['L']}, nderiv {c['nderiv']}): {n_exact}/{n_tot} exact, max normalized error {max_norm_err:.2e}, {time.time() - t0:.0f}s", flush=True)
    out["cases"][cname]["checks"] = checks
    out["cases"][cname]["all_pass"] = all(ch["pass_1ulp_normalized"] for ch in checks)
    del case; torch.cuda.empty_cache()
out["all_pass"] = all(v["all_pass"] for v in out["cases"].values())
out["reference"] = "d6-ver scripts/verify_angular_tables.py compiled/decimal_values (70-digit Decimal, rational real solid harmonics), read only"
json.dump(out, open(os.path.join(MYROOT, "validation", "g5c_closure_grid.json"), "w"), indent=1, default=str)
print("DONE all_pass", out["all_pass"])
