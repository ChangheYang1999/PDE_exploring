#!/usr/bin/env python3
"""Read-only numerical reproduction; no PDE optimizer is called.

Import only the portable copy. Historical candidate coefficients are never
re-solved for the main checks. All outputs are restricted to this migration tree.
"""
import argparse
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
import platform
import struct
import sys
import time
from decimal import Decimal

sys.dont_write_bytecode = True
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[_name] = "1"

MIGRATION = Path(__file__).resolve().parents[1]
TOL = {
    "objective_rtol": 1e-6, "objective_atol": 1e-13,
    "diagnostic_rtol": 1e-5, "diagnostic_atol": 1e-10,
    "a0_atol": 1e-8, "quadratic_atol": 1e-10, "five_atol": 1e-10,
    "inverse_atol": 1e-7, "inverse_rtol": 1e-9,
    "inverse_quadrature_atol": 1e-7,
    "archived_hybrid_reduction_atol": 5e-9,
}


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint(case):
    return hashlib.sha256(struct.pack("<25d", case["cl"], *case["coefficients"])).hexdigest()


def atomic_json(path, data):
    path = path.resolve()
    if MIGRATION not in path.parents:
        raise ValueError("Outputs must remain inside migration_preparation")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".partial")
    temporary.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def check(checks, name, actual, expected=0., atol=0., rtol=0.):
    error = abs(float(actual) - float(expected))
    limit = atol + rtol * abs(float(expected))
    checks.append({"name": name, "actual": float(actual), "expected": float(expected),
                   "absolute_difference": error, "tolerance": limit,
                   "passed": bool(math.isfinite(error) and error <= limit)})


def setup(source):
    source = source.resolve()
    if source != MIGRATION / "portable" / "stage10_completion":
        raise ValueError("Use the portable/stage10_completion source copy")
    sys.path.insert(0, str(source))
    a = importlib.import_module("stage8")
    jet = importlib.import_module("taylor_jet")
    return a, jet


def trap(np, nodes):
    nodes = np.asarray(nodes)
    delta = np.empty(len(nodes))
    delta[0] = (nodes[1]-nodes[0])/2
    delta[-1] = (nodes[-1]-nodes[-2])/2
    delta[1:-1] = (nodes[2:]-nodes[:-2])/2
    return delta/(nodes[-1]-nodes[0])


def coordinates(np, row):
    return np.array(row["x"]), np.array(row["y"])


def coordinate_hash(np, x, y):
    return hashlib.sha256(np.column_stack([x, y]).astype("<f8").tobytes()).hexdigest()


def residuals(a, case, x, y, batch=512):
    """Exact saved vector; stable original objective and separate physical PDE sums."""
    np = a.np
    n = len(x)
    values = {key: np.empty(n) for key in ("fit", "physical_fit", "Rf", "Rrho", "nf", "nr", "rho")}
    items = a.s.basis(case["cl"], 3, 5, "fractional3")
    c = np.array(case["coefficients"])
    strain = np.array([a.e.evaluate(b["ratio"], [0.], [0.])[0] for b in items])
    for lo in range(0, n, batch):
        hi = min(n, lo+batch)
        xx, yy = x[lo:hi], y[lo:hi]
        matrices = a.e.matrices(items, xx, yy)
        f = {key: a.dot(M, c) for key, M in matrices.items()}
        wx, wy = case["cl"]*xx-f["psiy"], case["cl"]*yy+f["psix"]
        tx, ty = wx*f["fx"], wy*f["fy"]
        stable_reaction = a.dot(matrices["ratio"]-strain[None, :], c)*f["f"]
        physical_reaction = (case["cl"]-1+f["ratio"])*f["f"]
        floor = 1e-8*(1+xx*xx+yy*yy)**((1/case["cl"]-1)/2)
        rf = tx+ty+physical_reaction
        # Evaluate density transport directly, independently of Rrho=y*Rf.
        rx, ry, rho = wx*yy*f["fx"], wy*(f["f"]+yy*f["fy"]), yy*f["f"]
        values["fit"][lo:hi] = (tx+ty+stable_reaction)/np.sqrt(tx*tx+ty*ty+stable_reaction**2+floor**2)
        values["physical_fit"][lo:hi] = rf/np.sqrt(tx*tx+ty*ty+physical_reaction**2+floor**2)
        values["Rf"][lo:hi] = rf
        values["Rrho"][lo:hi] = rx+ry-rho
        values["nf"][lo:hi] = abs(tx)+abs(ty)+abs(physical_reaction)
        values["nr"][lo:hi] = abs(rx)+abs(ry)+abs(rho)
        values["rho"][lo:hi] = rho
    return values


def objectives(a, case, stored, n):
    np = a.np
    xi, yi = coordinates(np, stored["inner"])
    xf, yf = coordinates(np, stored["far"])
    # Derive normalized log-radial/angular trapezoids from saved coordinates.
    ri = np.hypot(xi, yi).reshape(n, n)[:, 0]
    rf = np.hypot(xf, yf).reshape(n, n)[:, 0]
    ti = np.arctan2(yi, xi).reshape(n, n)[-1]
    tf = np.arctan2(yf, xf).reshape(n, n)[-1]
    wi = np.outer(np.r_[0., trap(np, np.log(ri[1:]))], trap(np, ti)).ravel()
    wf = np.outer(trap(np, np.log(rf)), trap(np, tf)).ravel()
    vi, vf = residuals(a, case, xi, yi), residuals(a, case, xf, yf)
    ji, jf = float(wi@(vi["fit"]**2)/2), float(wf@(vf["fit"]**2)/2)
    physical = float(wi@(vi["physical_fit"]**2)/2+.1*(wf@(vf["physical_fit"]**2)/2))
    return {"J_inner": ji, "J_far": jf, "J_joint": ji+.1*jf,
            "RMS_inner": math.sqrt(2*ji), "RMS_far": math.sqrt(2*jf),
            "physical_PDE_J_joint": physical,
            "physical_vs_stabilized_J_difference": physical-(ji+.1*jf),
            "inner_weight_sum": float(wi.sum()), "far_weight_sum": float(wf.sum()),
            "inner_coordinate_sha256": coordinate_hash(np, xi, yi),
            "far_coordinate_sha256": coordinate_hash(np, xf, yf)}


def diagnostic(a, case, row, a0):
    np = a.np
    x, y = coordinates(np, row)
    v = residuals(a, case, x, y)
    ef = 1e-10*max(1, abs(a0))
    er = 1e-10*max(1, float(max(abs(v["rho"]))))
    out = {"points": len(x), "coordinate_sha256": coordinate_hash(np, x, y),
           "epsilon_f": ef, "epsilon_rho": er,
           "Rrho_vs_y_Rf_max_abs": float(max(abs(v["Rrho"]-y*v["Rf"]))) }
    for key, values in (("Rf", abs(v["Rf"])/np.maximum(v["nf"], ef)),
                        ("Rrho", abs(v["Rrho"])/np.maximum(v["nr"], er))):
        i = int(np.argmax(values))
        out["max_normalized_"+key] = float(values[i])
        out["max_normalized_"+key+"_percent"] = float(100*values[i])
        out["location_normalized_"+key] = [float(x[i]), float(y[i])]
    return out


def inverse_check(a, case, checks):
    """Green integration of rho_x; exact incomplete-beta integral to infinity."""
    np = a.np
    points = [(0., 0.), (.3, .2), (1., .7), (2., 1.5), (0., 2.), (2., 0.),
              (8., 0.), (0., 64.), (31., 17.), (90., 70.), (230., 150.),
              (0., 512.), (512., 0.), (200., 1e-9)]
    x, y = np.array(points).T
    exact = a.s.fields(case, x, y)
    items = a.s.basis(case["cl"], 3, 5, "fractional3")
    source = [(co, ax, by+1, power) for co, ax, by, power in a.e.merged(items, case["coefficients"], "fx")]
    coarse = a.e.canonical_inverse(source, points, 80)
    fine = a.e.canonical_inverse(source, points, 120)
    orders = [80, 120]
    qerror = max(abs(u[k]-v[k]) for u, v in zip(coarse, fine) for k in ("psi", "psix", "psiy"))
    if qerror > 1e-8:
        coarse = a.e.canonical_inverse(source, points, 240)
        fine = a.e.canonical_inverse(source, points, 480)
        orders += [240, 480]
        qerror = max(abs(u[k]-v[k]) for u, v in zip(coarse, fine) for k in ("psi", "psix", "psiy"))
    rows = []
    for i, (point, computed) in enumerate(zip(points, fine)):
        row = {"point": list(point)}
        for key in ("psi", "psix", "psiy"):
            row[key+"_abs_error"] = abs(computed[key]-float(exact[key][i]))
            check(checks, "inverse {} {}".format(point, key), computed[key], exact[key][i],
                  atol=TOL["inverse_atol"], rtol=TOL["inverse_rtol"])
        rows.append(row)
    center_error = abs(fine[0]["strain"]-float(exact["ratio"][0]))
    check(checks, "canonical center strain", center_error, atol=TOL["inverse_atol"])
    check(checks, "Green quadrature convergence", qerror, atol=TOL["inverse_quadrature_atol"])
    return {"method": "polar Green modes; Gauss-Legendre interior and incomplete-beta full infinite exterior tail",
            "orders_used": orders, "last_orders_max_difference": qerror,
            "center_strain_abs_error": center_error, "points": rows,
            "exterior_center_strain": {str(r): a.e.exterior_strain(source, r) for r in (8, 64, 256, 512)}}


def saved_stationarity(a, case, reference, checks):
    np = a.np
    record = read(reference/"final_stationarity_scale4.json")
    arrays_path = reference/"final_stationarity_arrays.npz"
    with np.load(arrays_path, allow_pickle=False) as data:
        p, r, jz = data["p"], data["r"], data["JZ"]
        same = bool(np.array_equal(p, np.r_[case["cl"], case["coefficients"][1:]]))
        hybrid = float(np.linalg.norm(jz.T@r)/np.linalg.norm(r))
        rnorm = float(np.linalg.norm(r))
    fd = []
    hashes = {arrays_path.name: sha(arrays_path), "final_stationarity_scale4.json": sha(reference/"final_stationarity_scale4.json")}
    for i in range(11):
        path = reference/("final_FD_scale4_batch"+str(i)+".json")
        fd.extend(read(path)); hashes[path.name] = sha(path)
    fd.sort(key=lambda row: row["direction"])
    directions_ok = [row["direction"] for row in fd] == list(range(22))
    norms = np.linalg.norm(np.array([row["FD_gradient"] for row in fd]), axis=0)/rnorm
    check(checks, "stationarity exact physical vector", int(same), 1)
    check(checks, "stationarity fingerprint", int(record["physical_vector_sha256"] == fingerprint(case)), 1)
    check(checks, "stationarity 22 directions", int(directions_ok), 1)
    check(checks, "saved hybrid norm consistency", hybrid, record["hybrid_relative"], atol=TOL["archived_hybrid_reduction_atol"])
    for i in range(2):
        check(checks, "saved FD norm consistency "+str(i), norms[i], record["FD_relative"][i], atol=1e-12)
    check(checks, "archived stationarity threshold", max(hybrid, *norms), atol=1e-5)
    return {"scope": "archived arrays and all 22 FD components reassembled; no fresh derivatives in this default command",
            "hybrid_relative_reassembled": hybrid, "FD_relative_reassembled": norms.tolist(),
            "hybrid_relative_archived": record["hybrid_relative"],
            "hybrid_reduction_difference": hybrid-record["hybrid_relative"],
            "historical_threshold": 1e-5, "evidence_sha256": hashes}


def reproduce(args, a, jet, reference):
    checks = []
    grids = read(reference/"fitting_grids.json")
    assessments = read(reference/"assessment_grids.json")
    design = read(reference/"grid_design.json")
    cases = {}
    for label in args.labels:
        print("Recomputing "+label+": coefficients, objectives, validation and Green inverse", flush=True)
        path = args.source/"inputs/start_original.json" if label == "original" else reference/(label+".json")
        case = read(path)
        if len(case["coefficients"]) != 24 or case["family"] != "fractional3":
            raise ValueError("Unexpected saved candidate format")
        hp = jet.high_precision(case["cl"], case["coefficients"], prec=70)
        cl_from_center = float(Decimal(1)-Decimal(hp["jets"]["h"]))
        a0 = float(a.s.fields(case, [0.], [0.])["f"][0])
        check(checks, label+" cl reconstructed from center strain", cl_from_center, case["cl"], atol=1e-10)
        check(checks, label+" a0", a0, case["a0"], atol=TOL["a0_atol"])
        check(checks, label+" engine versus independent series a0", a0, float(hp["jets"]["a"]), atol=TOL["a0_atol"])
        check(checks, label+" quadratic Taylor", max(abs(float(v)) for v in hp["constraints"]), atol=TOL["quadratic_atol"])
        check(checks, label+" center identity", float(hp["center"]), atol=1e-10)
        check(checks, label+" formal Poisson jets", max(abs(float(v)) for v in hp["poisson"]), atol=1e-55)
        row = {"input_sha256": sha(path), "physical_vector_sha256": fingerprint(case),
               "cl": case["cl"], "cl_reconstructed_from_center_strain": cl_from_center,
               "coefficients": case["coefficients"], "a0": a0,
               "high_precision_independent_Taylor": hp, "objectives": {}, "validation": {},
               "role": "five-condition feasibility only; PDE objective and stationarity were not optimized" if label == "five" else ("Stage IX verified benchmark" if label == "original" else "Stage X quadratic-constrained S0 optimized profile")}
        expected = read(reference/(label+"_cross_grid.json"))
        check(checks, label+" archived objective fingerprint", int(expected["physical_vector_sha256"] == fingerprint(case)), 1)
        for n in (49, 97):
            obj = objectives(a, case, grids[str(n)], n)
            row["objectives"][str(n)] = obj
            for key in ("J_inner", "J_far", "J_joint", "RMS_inner", "RMS_far"):
                check(checks, label+" "+str(n)+" "+key, obj[key], expected["grids"][str(n)][key],
                      atol=TOL["objective_atol"], rtol=TOL["objective_rtol"])
        expected_diag = read(reference/(label+"_main_diagnostics.json"))
        for region in ("true_H65", "independent_shifted_inner", "independent_shifted_far"):
            diag = diagnostic(a, case, assessments[region], a0)
            row["validation"][region] = diag
            check(checks, label+" "+region+" coordinates", int(diag["coordinate_sha256"] == design[region]["coordinate_sha256"]), 1)
            for key in ("max_normalized_Rf", "max_normalized_Rrho"):
                check(checks, label+" "+region+" "+key, diag[key], expected_diag[region][key],
                      atol=TOL["diagnostic_atol"], rtol=TOL["diagnostic_rtol"])
        row["canonical_full_plane_inverse"] = inverse_check(a, case, checks)
        if label == "five":
            maximum = max(abs(float(v)) for v in hp["constraints"]+hp["fourth"])
            row["maximum_five_condition_defect"] = maximum
            check(checks, "five all five conditions", maximum, atol=TOL["five_atol"])
            check(checks, "five historical maximum defect", maximum, 1.190698105718707e-12, atol=1e-17, rtol=1e-6)
        if label == "final":
            row["preserved_stationarity"] = saved_stationarity(a, case, reference, checks)
            check(checks, "published final cl", case["cl"], 1.88763283908, atol=5e-11)
            check(checks, "published final a0", a0, 21.8907400641, atol=TOL["a0_atol"])
        cases[label] = row
    return {"cases": cases, "checks": checks, "passed": all(row["passed"] for row in checks)}


def stationarity(args, a, reference):
    """One fixed archived tangent direction, read-only feasible derivative evaluations."""
    np = a.np
    v = importlib.import_module("stage9")
    chart = v.Chart(read(reference/"chart.json"))
    case = read(reference/"final.json")
    with np.load(reference/"final_stationarity_arrays.npz", allow_pickle=False) as arrays:
        p, r, Z, JZ = (arrays[k] for k in ("p", "r", "Z", "JZ"))
        p, r, Z, JZ = p.copy(), r.copy(), Z.copy(), JZ.copy()
    if not np.array_equal(p, np.r_[case["cl"], case["coefficients"][1:]]):
        raise ValueError("Stationarity vector mismatch")
    stored = read(reference/"fitting_grids.json")["97"]
    xi, yi = coordinates(np, stored["inner"])
    xf, yf = coordinates(np, stored["far"])
    n = 97
    wi = np.outer(np.r_[0., trap(np, np.log(np.hypot(xi, yi).reshape(n,n)[1:,0]))], trap(np, np.arctan2(yi,xi).reshape(n,n)[-1])).ravel()
    wf = np.outer(trap(np, np.log(np.hypot(xf,yf).reshape(n,n)[:,0])), trap(np, np.arctan2(yf,xf).reshape(n,n)[-1])).ravel()
    x, y, root = np.r_[xi,xf], np.r_[yi,yf], np.sqrt(np.r_[wi,.1*wf])
    def residual(pp):
        cc = v.coefficients(pp)  # Only center elimination for perturbed FD probes.
        trial = dict(case, cl=float(pp[0]), coefficients=cc.tolist())
        return root*residuals(a, trial, x, y)["fit"]
    direction = Z[:,args.direction]
    q = p[chart.free]
    rows = []
    for step in (.004, .002):
        print("FD direction {} physical step {}".format(args.direction, step), flush=True)
        h = step/np.linalg.norm(direction)
        rr = [residual(chart.lift(q+k*h*direction[chart.free])) for k in (2,1,-1,-2)]
        fd = (-rr[0]+8*rr[1]-8*rr[2]+rr[3])/(12*h)
        rows.append({"physical_step": step, "FD_gradient": float(fd@r),
                     "FD_gradient_over_rnorm": float(fd@r/np.linalg.norm(r)),
                     "relative_J_error": float(np.linalg.norm(fd-JZ[:,args.direction])/np.linalg.norm(JZ[:,args.direction]))})
    return {"mode": "fresh_stationarity_direction", "physical_vector_sha256": fingerprint(case),
            "direction": args.direction, "rows": rows,
            "note": "No optimizer. Archive Z, r and JZ fixed. Collect all 22 directions before inferring a fresh full stationarity norm.",
            "passed": all(math.isfinite(row[k]) for row in rows for k in ("FD_gradient", "FD_gradient_over_rnorm", "relative_J_error")),
            "fresh_full_stationarity_established": False}


def stationarity_summary(a, reference):
    np = a.np
    case = read(reference/"final.json")
    rows = []
    provenance = None
    for direction in range(22):
        path = MIGRATION/"reproduction/results"/"stationarity_direction_{:02d}.json".format(direction)
        record = read(path)
        if record["physical_vector_sha256"] != fingerprint(case) or record["direction"] != direction:
            raise ValueError("Fresh stationarity file belongs to a different vector or direction")
        signature = {k: record[k] for k in ("verifier_sha256", "portable_source_sha256", "python", "numpy", "scipy", "hostname", "threadpools")}
        if provenance is None:
            provenance = signature
        elif signature != provenance:
            raise ValueError("Fresh stationarity files have different code or environment provenance")
        if not record["passed"]:
            raise ValueError("Fresh stationarity direction contains failed diagnostics")
        if [row["physical_step"] for row in record["rows"]] != [.004, .002]:
            raise ValueError("Fresh stationarity physical step mismatch")
        rows.append([row["FD_gradient_over_rnorm"] for row in record["rows"]])
    norms = np.linalg.norm(np.array(rows), axis=0)
    return {"mode": "fresh_stationarity_summary", "physical_vector_sha256": fingerprint(case),
            "directions": 22, "physical_FD_steps": [.004,.002], "FD_relative": norms.tolist(),
            "direction_run_provenance": provenance,
            "threshold": 1e-5, "passed": bool(max(norms) <= 1e-5),
            "fresh_full_stationarity_established": bool(max(norms) <= 1e-5),
            "note": "Fresh residual-value differences along all archived feasible directions; archived tangent whitening is fixed. A threshold failure must be investigated, never silently reclassified or optimized."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", default="candidates", choices=("candidates", "stationarity", "stationarity-summary"))
    parser.add_argument("--source", type=Path, default=MIGRATION/"portable/stage10_completion")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--labels", nargs="+", choices=("final", "five", "original"), default=["final", "five", "original"])
    parser.add_argument("--direction", type=int, choices=range(22), default=0)
    args = parser.parse_args()
    args.source = args.source.resolve()
    name = "candidates.json" if args.mode == "candidates" else ("stationarity_summary.json" if args.mode == "stationarity-summary" else "stationarity_direction_{:02d}.json".format(args.direction))
    output = args.output or MIGRATION/"reproduction/results"/name
    if MIGRATION not in output.resolve().parents:
        parser.error("Output must be inside migration_preparation")
    began = time.monotonic()
    a, jet = setup(args.source)
    from threadpoolctl import threadpool_limits, threadpool_info
    import scipy
    with threadpool_limits(limits=1):
        reference = args.source/"reference_results"
        if args.mode == "candidates":
            result = reproduce(args, a, jet, reference)
        elif args.mode == "stationarity":
            result = stationarity(args, a, reference)
        else:
            result = stationarity_summary(a, reference)
        result.update({"elapsed_seconds": time.monotonic()-began, "python": platform.python_version(),
                       "hostname": platform.node(), "executable": sys.executable,
                       "generated_utc_epoch": time.time(), "mode": args.mode,
                       "verifier_sha256": sha(Path(__file__)),
                       "portable_source_sha256": {path.name: sha(path) for path in args.source.glob("*.py")},
                       "platform": platform.platform(), "numpy": a.np.__version__, "scipy": scipy.__version__,
                       "threadpools": threadpool_info(), "tolerances": TOL,
                       "no_optimization": True, "original_coefficients_not_re_solved": args.mode == "candidates"})
    atomic_json(output, result)
    print(json.dumps({"passed": result["passed"], "output": str(output), "elapsed_seconds": result["elapsed_seconds"],
                      "failed_checks": [r for r in result.get("checks", []) if not r["passed"]]}), flush=True)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
