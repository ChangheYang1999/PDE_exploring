"""Controlled Stage-II experiments, using the frozen local Stage-I engine.

No source or result in ../pilot_y_branch is written.  The alternative family
adds a fractional far-tail correction suggested by the nonlinear balance:
rho_0~r^gamma and U_0.grad rho_0~r^(2 gamma-1).  A density correction of
degree 2 gamma-1 corresponds to a chi power offset (1-gamma)/2.
"""
from ipm_portable import output_dir, peak_rss_mib
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import resource
import signal
import time

import numpy as np
import psutil
from scipy.optimize import least_squares, minimize_scalar
from scipy.optimize._numdiff import approx_derivative
from threadpoolctl import threadpool_info, threadpool_limits

import stage1_engine as e

ROOT = Path(__file__).resolve().parent
OUT = output_dir()


def save(name, value):
    path = OUT/name
    temp = path.with_suffix(".partial")
    temp.write_text(json.dumps(value, indent=2, allow_nan=False))
    temp.replace(path)


def load_case(name):
    path = ROOT/"inputs"/(name[4:]+".json") if name.startswith("old:") else OUT/(name+".json")
    return json.loads(path.read_text())


def basis(cl, nm, nk, family):
    if family == "integer":
        return e.basis(cl, nm, nk)
    assert family in ("fractional", "fractional2") and nk >= 1
    d, delta = (3+1/cl)/2, (1-1/cl)/2
    fractional_count = 1 if family == "fractional" else 2
    integer_count = nk+1-fractional_count
    result = []
    for m in range(nm+1):
        for k in range(nk+1):
            offset = k if k < integer_count else (k-integer_count+1)*delta
            chi = [(float((-1)**j*math.comb(2*m, 2*j)), 2*m-2*j, 2*j, d-m-offset)
                   for j in range(m+1)]
            psi = e.derivative(e.derivative(chi, 0), 1)
            rho = [(-c, a, b, p) for c, a, b, p in e.derivative(e.laplace(chi), 1)]
            f = e.divide_y(rho)
            psix = e.derivative(psi, 0)
            result.append({"f": f, "fx": e.derivative(f, 0), "fy": e.derivative(f, 1),
                           "psi": psi, "psix": psix, "psiy": e.derivative(psi, 1),
                           "ratio": e.divide_y(psix)})
    return result


def fields(case, x, y):
    items = basis(case["cl"], case["nm"], case["nk"], case.get("family", "integer"))
    return {key: matrix@case["coefficients"] for key, matrix in e.matrices(items, x, y).items()}


class Problem(e.Fit):
    def __init__(self, nm, nk, x, y, family="integer", stable=False):
        super().__init__(nm, nk, x, y, "relative")
        self.family, self.stable = family, stable

    def data(self, cl):
        if cl != self.cached_cl:
            items = basis(cl, self.nm, self.nk, self.family)
            self.cached = (e.matrices(items, self.x, self.y),
                           np.array([e.evaluate(b["ratio"], [0], [0])[0] for b in items]))
            self.center_f = np.array([e.evaluate(b["f"], [0], [0])[0] for b in items])
            self.cached_cl = cl
        return self.cached

    def fun(self, p):
        if not self.stable:
            return super().fun(p)
        cl = p[0]
        mats, strain = self.data(cl)
        c = self.coefficients(p)
        f = {key: matrix@c for key, matrix in mats.items()}
        t1 = (cl*self.x-f["psiy"])*f["fx"]
        t2 = (cl*self.y+f["psix"])*f["fy"]
        # By the eliminated center identity cl-1+Q(X)=(Q(X)-Q(0)).
        # Subtract basis rows BEFORE dot products; origin rows are exactly zero.
        reaction = (mats["ratio"]-strain[None, :])@c
        t3 = reaction*f["f"]
        w = (1+self.x**2+self.y**2)**((1/cl-1)/2)
        return (t1+t2+t3)/np.sqrt(t1*t1+t2*t2+t3*t3+(1e-8*w)**2)

    def metadata(self, p):
        self.data(p[0])
        c = self.coefficients(p)
        return {"cl": float(p[0]), "a0": float(self.center_f@c)}


def embed(start, nm, nk, family):
    assert nm >= start["nm"]
    def labels(kind, last):
        fractional = 0 if kind == "integer" else (1 if kind == "fractional" else 2)
        return [("integer", k) for k in range(last+1-fractional)]+[("fractional", k+1) for k in range(fractional)]
    source_labels = labels(start.get("family", "integer"), start["nk"])
    target_labels = labels(family, nk)
    assert all(label in target_labels for label in source_labels), "target must contain all starting layers"
    c = np.zeros((nm+1)*(nk+1))
    for m in range(start["nm"]+1):
        for k, label in enumerate(source_labels):
            target_k = target_labels.index(label)
            c[m*(nk+1)+target_k] = start["coefficients"][m*(start["nk"]+1)+k]
    return c


def embedding_check(start, target):
    x = np.array([0, .17, .9, 2.7, 0, 5, 11, 31, -2.1])
    y = np.array([0, .33, 0, 1.2, 3, 0, 7, 18, -.4])
    before, after = fields(start, x, y), fields(target, x, y)
    return {key: float(np.max(abs(before[key]-after[key]))) for key in before}


def fit(args):
    start_wall = time.monotonic()
    start_cpu = time.process_time()
    source = load_case(args.start)
    if args.recorded_initial:
        source = dict(source, cl=source["initial"]["cl"], coefficients=source["initial"]["coefficients"])
    nm = args.nm if args.nm is not None else source["nm"]
    nk = args.nk if args.nk is not None else source["nk"]
    c = embed(source, nm, nk, args.family)
    trial = {"label": args.label, "cl": source["cl"], "coefficients": c.tolist(),
             "nm": nm, "nk": nk, "family": args.family,
             "nr": args.nr, "nt": args.nt, "rmax": args.rmax,
             "stable_center": args.stable_center, "objective": "Stage-I relative, epsilon=1e-8*w"}
    preservation = embedding_check(source, trial)
    assert max(preservation.values()) < 2e-9, preservation
    x, y = e.polar_grid(args.nr, args.nt, args.rmax)
    problem = Problem(nm, nk, x, y, args.family, args.stable_center)
    p0 = np.r_[trial["cl"], c[1:]]
    bounds = (np.r_[1.02, np.full(len(p0)-1, -100.)], np.r_[10., np.full(len(p0)-1, 100.)])
    calls, jacobians, accepted = [], [], []
    cache = {}
    phase = ["residual"]
    checkpoint = {**trial, "interrupted": True, "embedding_max_abs": preservation,
                  "initial": {**trial, "source": args.start, "recorded_initial": args.recorded_initial},
                  "settings": {"max_nfev": args.nfev, "ftol": 1e-8, "xtol": 1e-8, "gtol": 1e-8,
                               "jacobian": "2-point, same scipy approx_derivative as Stage I",
                               "bounds": [bounds[0].tolist(), bounds[1].tolist()]}}
    save(args.label+"_start.json", checkpoint)
    def checkpoint_now():
        checkpoint.update(history=calls, jacobian_history=jacobians, accepted_states=accepted)
        save(args.label+".json", checkpoint)
    def stop(signum, frame):
        checkpoint["stop"] = "SIGTERM resource/interrupt stop; last accepted state preserved"
        checkpoint_now()
        raise SystemExit(checkpoint["stop"])
    signal.signal(signal.SIGTERM, stop)
    def fun(p):
        value = problem.fun(p)
        meta = problem.metadata(p)
        calls.append({"evaluation": len(calls)+1, "phase": phase[0],
                      "cost": float(np.dot(value, value)/2), **meta,
                      "wall_seconds": time.monotonic()-start_wall,
                      "cpu_seconds": time.process_time()-start_cpu})
        cache[tuple(p)] = value
        return value
    def jac(p):
        key = tuple(p)
        f0 = cache[key] if key in cache else fun(p)
        phase[0] = "jacobian_probe"
        try:
            j = approx_derivative(fun, p, method="2-point", f0=f0, bounds=bounds)
        finally:
            phase[0] = "residual"
        singular = np.linalg.svd(j, compute_uv=False)
        g = j.T@f0
        origin = (x == 0) & (y == 0)
        meta = problem.metadata(p)
        row = {"jacobian": len(jacobians)+1, "residual_evaluations": len(calls),
               "cost": float(f0@f0/2), "gradient_inf": float(max(abs(g))),
               "singular_max": float(singular[0]), "singular_min": float(singular[-1]),
               "condition_2": float(singular[0]/max(1e-300, singular[-1])),
               "origin_rows_J_frobenius": float(np.linalg.norm(j[origin])),
               "origin_residual_max": float(max(abs(f0[origin]))), **meta,
               "wall_seconds": time.monotonic()-start_wall, "cpu_seconds": time.process_time()-start_cpu}
        jacobians.append(row)
        coefficients = problem.coefficients(p).tolist()
        accepted.append({**meta, "coefficients": coefficients, "cost": row["cost"],
                         "parameters": p.tolist(), "wall_seconds": row["wall_seconds"]})
        checkpoint.update(cl=meta["cl"], a0=meta["a0"], coefficients=coefficients)
        checkpoint_now()
        return j
    checkpoint_now()
    result = least_squares(fun, p0, jac=jac, bounds=bounds, max_nfev=args.nfev,
                           ftol=1e-8, xtol=1e-8, gtol=1e-8)
    meta = problem.metadata(result.x)
    c = problem.coefficients(result.x)
    if not np.array_equal(result.x, np.array(accepted[-1]["parameters"])):
        accepted.append({**meta, "coefficients": c.tolist(), "parameters": result.x.tolist(),
                         "cost": float(result.cost), "wall_seconds": time.monotonic()-start_wall})
    base_evaluations = sum(row["phase"] == "residual" for row in calls)
    checkpoint.update(cl=meta["cl"], a0=meta["a0"], coefficients=c.tolist(), interrupted=False,
        optimizer={"success": bool(result.success), "status": int(result.status), "message": result.message,
                   "cost": float(result.cost), "nfev": result.nfev, "njev": result.njev,
                   "actual_residual_calls_including_FD": len(calls), "base_residual_calls": base_evaluations,
                   "accepted_steps": len(accepted)-1, "optimality": float(result.optimality),
                   "gradient_inf": float(max(abs(result.grad))), "active_mask": result.active_mask.tolist()},
        wall_seconds=time.monotonic()-start_wall, cpu_seconds=time.process_time()-start_cpu,
        min_abs_a0_evaluated=min(abs(row["a0"]) for row in calls),
        near_cl_boundary=bool(meta["cl"] < 1.021 or meta["cl"] > 9.99))
    checkpoint_now()
    print(json.dumps({key: checkpoint[key] for key in ("label", "family", "cl", "a0", "optimizer",
                                                      "wall_seconds", "cpu_seconds", "embedding_max_abs")}, indent=2))


def diagnostic(case, x, y):
    f = fields(case, x, y)
    cl = case["cl"]
    rf = e.residual(cl, f, x, y)
    rr = y*rf
    nf = abs((cl*x-f["psiy"])*f["fx"])+abs((cl*y+f["psix"])*f["fy"])+abs((cl-1+f["ratio"])*f["f"])
    rho, rx, ry = y*f["f"], y*f["fx"], f["f"]+y*f["fy"]
    nrho = abs((cl*x-f["psiy"])*rx)+abs((cl*y+f["psix"])*ry)+abs(rho)
    a0 = fields(case, [0], [0])["f"][0]
    ef, er = 1e-10*max(1, abs(a0)), 1e-10*max(1, float(max(abs(rho))))
    values = {"abs_Rf": abs(rf), "abs_Rrho": abs(rr),
              "normalized_Rf": abs(rf)/np.maximum(nf, ef),
              "normalized_Rrho": abs(rr)/np.maximum(nrho, er)}
    result = {"points": len(x), "radius_min": float(min(np.hypot(x, y))),
              "radius_max": float(max(np.hypot(x, y))), "epsilon_f": float(ef), "epsilon_rho": float(er),
              "floor_hits_f": int(sum(nf <= ef)), "floor_hits_rho": int(sum(nrho <= er)),
              "rms_normalized_Rf": float(np.sqrt(np.mean(values["normalized_Rf"]**2)))}
    for key, v in values.items():
        j = int(np.argmax(v))
        result["max_"+key] = float(v[j])
        result["location_"+key] = [float(x[j]), float(y[j])]
    return result


def polar(radii, theta):
    r, t = np.meshgrid(radii, theta, indexing="ij")
    x, y = r*np.cos(t), r*np.sin(t)
    x[t == np.pi/2] = 0.0
    y[t == 0] = 0.0
    return x.ravel(), y.ravel()


def independent_checks(case):
    cl, c = case["cl"], np.array(case["coefficients"])
    items = basis(cl, case["nm"], case["nk"], case.get("family", "integer"))
    points = [(0, 0), (.3, .2), (1, .7), (2, 1.5), (0, 2), (2, 0)]
    x, y = np.array(points).T
    exact = fields(case, x, y)
    source = [(co, a, b+1, p) for co, a, b, p in e.merged(items, c, "fx")]
    inv = [e.canonical_inverse(source, points, order) for order in (80, 120)]
    inv_abs = max(abs(row[key]-exact[key][j]) for j, row in enumerate(inv[0])
                  for key in ("psi", "psix", "psiy"))
    scale = max(abs(value) for key in ("psi", "psix", "psiy") for value in exact[key])
    center = fields(case, [0], [0])
    checks = {"canonical_inverse": {"points": points, "max_abs": inv_abs,
        "relative_max_field": inv_abs/max(1e-14, scale),
        "80_vs_120": max(abs(a[key]-b[key]) for a, b in zip(*inv) for key in ("psi", "psix", "psiy")),
        "center_strain_abs_error": abs(inv[0][0]["strain"]-center["ratio"][0]),
        "exterior_strain": {str(r): e.exterior_strain(source, r) for r in (8, 16, 32, 128)}}}
    poisson = []
    for step in (.002, .001):
        lap = np.zeros_like(x)
        for dx, dy in ((step, 0), (0, step)):
            lap += (fields(case, x+dx, y+dy)["psi"]-2*exact["psi"]+fields(case, x-dx, y-dy)["psi"])/step**2
        error = float(max(abs(-lap-y*exact["fx"])))
        poisson.append({"step": step, "max_abs": error,
                        "over_max_source": error/max(1e-14, float(max(abs(y*exact["fx"]))))})
    checks["poisson_FD"] = poisson
    offgrid = np.array([(0, 0), (.173, .291), (.721, 1.137), (2.31, .817),
                        (.73, 0), (0, .91), (1.13, 1e-9), (1e-9, 1.29),
                        (-.731, .419), (.382, -.927), (3.73, 2.11), (9.1, 4.7),
                        (17.3, 11.2), (0, 23.1), (29.1, 0)])
    xx, yy = offgrid.T
    fterms = e.merged(items, c, "f")
    hterms = [(co, a-1, b-1, p) for co, a, b, p in e.merged(items, c, "psi")]
    assert all(a >= 0 and b >= 0 for _, a, b, _ in hterms)
    fv = lambda a, b: e.evaluate(fterms, a, b)
    hv = lambda a, b: e.evaluate(hterms, a, b)
    rhov = lambda a, b: b*fv(a, b)
    analytic = fields(case, xx, yy)
    rf = e.residual(cl, analytic, xx, yy)
    transport = []
    for step0 in (.002, .001):
        step = step0*np.maximum(1, np.hypot(xx, yy))
        def diff(fun, axis):
            dx, dy = (step, 0) if axis == 0 else (0, step)
            return (-fun(xx+2*dx, yy+2*dy)+8*fun(xx+dx, yy+dy)
                    -8*fun(xx-dx, yy-dy)+fun(xx-2*dx, yy-2*dy))/(12*step)
        h = hv(xx, yy)
        ratio = h+xx*diff(hv, 0)
        wx, wy = cl*xx-xx*(h+yy*diff(hv, 1)), cl*yy+yy*ratio
        rf_fd = wx*diff(fv, 0)+wy*diff(fv, 1)+(cl-1+ratio)*fv(xx, yy)
        rr_fd = wx*diff(rhov, 0)+wy*diff(rhov, 1)-rhov(xx, yy)
        transport.append({"relative_step": step0, "max_abs_Rf": float(max(abs(rf_fd))),
                          "max_abs_Rrho": float(max(abs(rr_fd))), "Rf_disagreement": float(max(abs(rf_fd-rf))),
                          "Rrho_disagreement": float(max(abs(rr_fd-yy*rf)))})
    checks["transport_FD"] = {"points": offgrid.tolist(), "steps": transport}
    def second(name, axis):
        return float(e.evaluate(e.derivative(e.derivative(e.merged(items, c, name), axis), axis), [0], [0])[0])
    a0, strain = float(center["f"][0]), float(center["ratio"][0])
    fxx, fyy, qxx, qyy = second("f", 0), second("f", 1), second("ratio", 0), second("ratio", 1)
    taylor = {"a0": a0, "strain": strain, "center_identity_defect": abs(cl+strain-1),
              "fxx": fxx, "fyy": fyy, "Qxx": qxx, "Qyy": qyy,
              "Rf_x2": (2*cl-1)*fxx+a0*qxx/2, "Rf_y2": fyy+a0*qyy/2}
    estimates = []
    r0 = e.residual(cl, center, np.array([0.]), np.array([0.]))[0]
    for h in (.002, .001):
        xf, yf = np.array([h, 0.]), np.array([0., h])
        r = e.residual(cl, fields(case, xf, yf), xf, yf)
        estimates.append({"h": h, "Rf_x2_from_axis_values": float((r[0]-r0)/h**2),
                          "Rf_y2_from_axis_values": float((r[1]-r0)/h**2)})
    taylor["independent_axis_expansion"] = estimates
    checks["taylor"] = taylor
    parity = 0.
    for sx, sy in ((-1, 1), (1, -1), (-1, -1)):
        ff = fields(case, sx*x, sy*y)
        parity = max(parity, float(max(abs(ff["f"]-exact["f"]))),
                     float(max(abs(ff["psi"]-sx*sy*exact["psi"]))),
                     float(max(abs(ff["ratio"]-exact["ratio"]))))
    checks["parity_max_abs"] = parity
    tails = []
    for r in (8, 16, 32, 64, 128, 256):
        xx, yy = polar([r], np.linspace(0, np.pi/2, 35))
        ff = fields(case, xx, yy)
        grad = np.hypot(yy*ff["fx"], ff["f"]+yy*ff["fy"])
        tails.append({"r": r, "max_rho": float(max(abs(yy*ff["f"]))),
                      "max_U_over_r": float(max(np.hypot(ff["psix"], ff["psiy"]))/r),
                      "density_gradient_bound_ratio": float(max(abs(yy*ff["f"])+(1+r)*grad)/(1+r)**(1/cl))})
    checks["tails"] = tails
    return checks


def assess(args):
    if args.common_grid_batch:
        records = {}
        for path in sorted(OUT.glob("*.json")):
            case = json.loads(path.read_text())
            if "optimizer" not in case or "coefficients" not in case:
                continue
            rows = {}
            for n in (17, 33):
                angles = np.r_[0, 1e-6, .001, (np.arange(n)+.37)*np.pi/(2*n),
                               np.pi/2-.001, np.pi/2-1e-6, np.pi/2]
                x, y = polar(np.geomspace(16.48, 128, n), angles)
                rows[str(n)] = diagnostic(case, x, y)
            records[path.stem] = rows
        save("common_holdout_checks.json", records)
        print(json.dumps({name: rows["33"]["max_normalized_Rf"] for name, rows in records.items()}, indent=2))
        return
    case = load_case(args.label)
    records, regional = {}, []
    x, y = e.polar_grid(case["nr"], case["nt"], case["rmax"])
    records["fit"] = diagnostic(case, x, y)
    for n in (17, 33):
        angles = np.r_[0, 1e-6, .001, (np.arange(n)+.37)*np.pi/(2*n),
                       np.pi/2-.001, np.pi/2-1e-6, np.pi/2]
        for name, rlo, rhi in (("between", .035, case["rmax"]),
                               ("outside", 1.03*case["rmax"], 32), ("far_holdout", 32.03, 128),
                               ("near_origin", 1e-4, .08)):
            radii = np.geomspace(rlo, rhi, n)
            x, y = polar(radii, angles)
            row = diagnostic(case, x, y)
            records[f"{name}_{n}"] = row
            regional.append({"region": name, "resolution": n, **row})
        ax = np.r_[0, np.geomspace(.01, 32, 3*n-1)]
        for name, x, y in (("x_axis", ax, ax*0), ("y_axis", ax*0, ax)):
            row = diagnostic(case, x, y)
            records[f"{name}_{n}"] = row
            regional.append({"region": name, "resolution": n, **row})
        xx, yy = polar(np.geomspace(.035, 32, n), [0, 1e-9, 1e-6, .001,
                      np.pi/2-.001, np.pi/2-1e-6, np.pi/2-1e-9, np.pi/2])
        row = diagnostic(case, xx, yy)
        records[f"near_axes_{n}"] = row
        regional.append({"region": "near_axes", "resolution": n, **row})
    records["independent"] = independent_checks(case)
    if args.label == "A45":
        old = load_case("old:refined_relative")
        old_checks = json.loads((ROOT/"inputs/refined_relative_checks.json").read_text())
        records["stage1_reproduction"] = {"cl_abs_diff": abs(case["cl"]-old["cl"]),
            "a0_abs_diff": abs(records["independent"]["taylor"]["a0"]-old["a0"]),
            "max_coefficient_diff": float(max(abs(np.array(case["coefficients"])-old["coefficients"]))),
            "outside_normalized_Rf_abs_diff": abs(records["outside_17"]["max_normalized_Rf"]-old_checks["outside_fit"]["max_normalized_Rf"])}
    save(args.label+"_checks.json", records)
    with (OUT/(args.label+"_regions.csv")).open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(regional[0]))
        writer.writeheader()
        writer.writerows(regional)
    if args.compare:
        previous = load_case(args.compare)
        x, y = polar(np.geomspace(.05, 8, 23), np.linspace(0, np.pi/2, 15))
        reference = fields(previous, x, y)["f"]
        norm = max(1e-14, np.linalg.norm(reference))
        def difference(logscale):
            scale = np.exp(logscale)
            value = fields(case, x/scale, y/scale)["f"]
            return np.linalg.norm(value-reference)/norm
        align = minimize_scalar(difference, bounds=(math.log(.25), math.log(4)), method="bounded")
        comparison = {"reference": args.compare, "cl_difference": case["cl"]-previous["cl"],
                      "a0_difference": records["independent"]["taylor"]["a0"]-fields(previous, [0], [0])["f"][0],
                      "relative_shape_L2_before": difference(0), "relative_shape_L2_after": align.fun,
                      "postprocess_lambda": math.exp(align.x),
                      "amplitude_factors_applied": False,
                      "alignment_grid": "23 log radii 0.05..8, 15 angles, f values; no amplitude scaling"}
        save(args.label+"_shape.json", comparison)
    print(json.dumps({"label": args.label, "fit": records["fit"], "outside_33": records["outside_33"],
                      "taylor": records["independent"]["taylor"]}, indent=2))


def verify():
    e.verify()
    case = {"cl": 2., "nm": 1, "nk": 3, "family": "fractional",
            "coefficients": [-.12, .09, .01, -.03, .02, -.01, .005, .007]}
    check = independent_checks(case)
    save("fractional_verification.json", check)
    assert check["canonical_inverse"]["max_abs"] < 1e-9
    assert check["canonical_inverse"]["center_strain_abs_error"] < 1e-9
    assert check["parity_max_abs"] < 1e-12
    print("Fractional-layer manufactured potential verified:", check["canonical_inverse"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["verify", "fit", "assess"])
    parser.add_argument("--label", default="trial")
    parser.add_argument("--start", default="old:refined_relative")
    parser.add_argument("--recorded-initial", action="store_true")
    parser.add_argument("--nm", type=int)
    parser.add_argument("--nk", type=int)
    parser.add_argument("--family", choices=["integer", "fractional", "fractional2"], default="integer")
    parser.add_argument("--stable-center", action="store_true")
    parser.add_argument("--nr", type=int, default=13)
    parser.add_argument("--nt", type=int, default=13)
    parser.add_argument("--rmax", type=float, default=8.)
    parser.add_argument("--nfev", type=int, default=45)
    parser.add_argument("--compare")
    parser.add_argument("--common-grid-batch", action="store_true")
    args = parser.parse_args()
    try:
        with threadpool_limits(limits=1):
            if args.mode == "verify":
                verify()
            elif args.mode == "fit":
                fit(args)
            else:
                assess(args)
    finally:
        usage = resource.getrusage(resource.RUSAGE_SELF)
        save(args.mode+"_"+args.label+"_process.json", {"peak_rss_mib": peak_rss_mib(usage),
            "cpu_seconds": usage.ru_utime+usage.ru_stime, "threads_at_exit": psutil.Process().num_threads(),
            "nice": psutil.Process().nice(), "threadpools": threadpool_info()})


if __name__ == "__main__":
    main()
