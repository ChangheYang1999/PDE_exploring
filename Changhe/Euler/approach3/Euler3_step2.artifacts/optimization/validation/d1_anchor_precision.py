"""D6FP D1 (lead 23:08Z item 2, 23:24Z item 2): precision diagnostic for the far-anchor block of the production J_cw coefficient columns on the
verifier's input d6-ver/artifacts/inputs/manufactured_geometric_even (Nk 4, R0 1.31, (c_l, omega) = (0.42, 0.3), angular 20 x 38, Nr_source 48,
anchors 4096/16384/65536 R0): columns 152, 181, 183, 185, 187, 188 (reduced physical coordinates) failed the anchor block in V045/V046 (v0).
Variants: --precision fp64 (v0, production chain), dd (v1, double-double pressure chain with exact tangents, PressureSolver.solve_dd) or dd2 (v2: v1 plus DU and tr(DU^2) accumulated in double-double, src/equations/fields_dd.py).
--src-root imports the production package from another root (the verifier's immutable snapshot, for the v0 reproduction) before the validation
code is imported. Output: validation/d1_<tag>.json and a table of the anchor-block errors per step."""
import sys, os, json, time, argparse, hashlib
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ap = argparse.ArgumentParser()
ap.add_argument("--src-root", default=None); ap.add_argument("--precision", default="fp64", choices=["fp64", "dd", "dd2", "dd2t", "dd2j"]); ap.add_argument("--columns", default="152,181,183,185,187,188")
ap.add_argument("--tag", required=True); ap.add_argument("--input", default="RUN_ROOT/verifier/artifacts/inputs/manufactured_geometric_even")
ap.add_argument("--pair", default="0.42,0.3"); ap.add_argument("--nr", type=int, default=48); ap.add_argument("--grid", default="20,38"); ap.add_argument("--steps", default="1e-3,1e-4,1e-5,1e-6,1e-7")
args = ap.parse_args()
if args.src_root:
    sys.path.insert(0, os.path.abspath(args.src_root))
    import src, src.equations.fields, src.optimization.problem, src.optimization.tail_constraints, src.optimization.param_map, src.optimization.lm   # noqa: the package 'src' now resolves to that root
    import src.optimization.seeds
sys.path.insert(0, MYROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, column_test, PROD
import src as _src
src_root_used = os.path.dirname(os.path.abspath(_src.__file__))
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
d = np.load(os.path.join(args.input, "coeffs.npz"), allow_pickle=True)
sha = {fn: hashlib.sha256(open(os.path.join(args.input, fn), "rb").read()).hexdigest() for fn in ("coeffs.npz", "meta.json")}
T = lambda a: torch.tensor(np.asarray(a, dtype=float))
arrays = dict(A=T(d["A"]), C=T(d["C"]), B=T(d["B"]), D=T(d["D"]), E=T(d["E"]), channels=json.loads(str(d["channels"])), m_parity=str(d["m_parity"]), R0=float(d["R0"]), Nk=int(d["Nk"]), Nr=args.nr,
              desc=f"d6-ver manufactured_geometric_even coeffs.npz sha256 {sha['coeffs.npz'][:16]}")
pair = tuple(float(v) for v in args.pair.split(","))
grid = tuple(int(v) for v in args.grid.split(","))
t0 = time.time()
case = Case(f"V045_input_{args.precision}", dev, arrays=arrays, pair=pair, align=False, grid=grid)
prob, model = case.prob, case.model
modes_npz = [tuple(int(v) for v in m) for m in d["modes"].tolist()]
modes_model = [tuple(int(v) for v in m) for m in model.modes]
assert modes_npz == modes_model, ("mode order differs", modes_npz[:5], modes_model[:5])
out = dict(tag=args.tag, precision=args.precision, src_root=src_root_used, input=args.input, input_sha256=sha, pair=pair, grid=grid, Nr=args.nr, n_opt=int(case.z_phys.numel()), n_rows=int(case.r.numel()),
           n_anchor_rows=int(case.anchor_mask.sum()), anchors=[float(v) for v in model.extra_r], gpu=(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"), started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           src_sha256={fn: hashlib.sha256(open(os.path.join(src_root_used, fn), "rb").read()).hexdigest() for fn in ("pressure/poisson_sh.py", "optimization/problem.py", "equations/fields.py", "far_field/correction.py") if os.path.exists(os.path.join(src_root_used, fn))})
if args.precision in ("dd", "dd2", "dd2t", "dd2j"):
    if not hasattr(prob.pressure, "solve_dd"):
        raise SystemExit("this src root has no solve_dd")
    prob.pressure.chain_precision = "dd"                                        # v1: double-double pressure chain
    if args.precision in ("dd2", "dd2t", "dd2j"):
        prob.source_precision = "dd"                                            # v2: DU and tr(DU^2) accumulated in double-double, unrounded into the chain
    if args.precision == "dd2t":
        import src.pressure.poisson_sh as _ps; _ps.TANGENT_FP64 = True           # double-double values, float64 tangents (cost option)
    if args.precision == "dd2j":
        from src.optimization.problem import apply_precision_mode; apply_precision_mode(prob, "dd_fp64jac")   # configuration M: float64 Jacobian path inside functorch, dd2 values
    r, aux = prob.objective_at(case.z_full); prob.commit_aux(aux); case.r = r; case.cost = 0.5 * float(r @ r)
out["cost"] = case.cost; out["r_norm"] = float(case.r.norm()); out["r_anchor_norm"] = float(case.r[case.anchor_mask].norm())
zp = case.z_phys; n = zp.numel()
def act(zz_full):
    ev = prob.evaluate(zz_full, tables=prob.pressure_tables_at(zz_full))
    return prob.nl_active_set(ev) | dict(geometry=prob.pressure.geometry_id)
fun_w = lambda q: prob.residual_vector_wd(case.to_full_phys(q))
hs = [float(v) for v in args.steps.split(",")]
cols = [int(v) for v in args.columns.split(",")]
res = {}
for k in cols:
    e = torch.zeros_like(zp); e[k] = 1.0
    t1 = time.time()
    col = torch.func.jvp(fun_w, (zp,), (e,))[1]
    tj = time.time() - t1
    t1 = time.time()
    tst = column_test(case, f"J_cw coefficient column {k} (physical)", col, fun_w, zp, e, hs, ref=case.r, record_active=lambda q: act(case.to_full_phys(q)), scale=1.0)
    tt = time.time() - t1
    blk = {f"{h:.0e}": dict(e2=tst["per_group"][f"{h:.0e}"]["second_order"].get("far_anchor_block"), e4=tst["per_group"][f"{h:.0e}"]["five_point"].get("far_anchor_block")) for h in hs}
    res[str(k)] = dict(column_norm=tst["column_norm"], anchor_block_column_norm=float(col[case.anchor_mask].norm()), far_anchor_block=blk, far_anchor_group_pass=tst["group_pass"].get("far_anchor_block"),
                       all_errors_second_order=tst["errors_second_order"], all_errors_five_point=tst["errors_five_point"], richardson_all=tst["richardson_error"], PASS_all_groups=tst["PASS"],
                       group_pass={g: v["PASS"] for g, v in tst["group_pass"].items()}, active_sets_identical=tst["active_sets_identical"], t_jvp=tj, t_test=tt)
    print(f"col {k}: |col| {tst['column_norm']:.3e} anchors {float(col[case.anchor_mask].norm()):.3e}; far_anchor_block e2/e4: " + " ".join(f"{h:.0e}:{blk[f'{h:.0e}']['e2']:.2e}/{blk[f'{h:.0e}']['e4']:.2e}" for h in hs)
          + f"; block PASS {tst['group_pass'].get('far_anchor_block', {}).get('PASS')} rich {tst['group_pass'].get('far_anchor_block', {}).get('richardson_error')}; column PASS {tst['PASS']} ({tj:.1f}s + {tt:.1f}s)", flush=True)
out["columns"] = res; out["elapsed_s"] = time.time() - t0
out["anchor_block_all_pass"] = all(v["far_anchor_group_pass"] and v["far_anchor_group_pass"]["PASS"] for v in res.values())
out["all_columns_pass"] = all(v["PASS_all_groups"] for v in res.values())
print("anchor block all pass:", out["anchor_block_all_pass"], "all columns pass:", out["all_columns_pass"], f"elapsed {out['elapsed_s']:.0f}s", flush=True)
json.dump(out, open(os.path.join(MYROOT, "validation", f"d1_{args.tag}.json"), "w"), indent=1)
