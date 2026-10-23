"""Stage III: fixed 20-parameter model; changes of numerical coordinates only.

The frozen Stage-II model and assessors are copied locally. No explicit length
parameter, extra basis function, tail layer, fit node, or objective row is added.
"""
from ipm_portable import output_dir, peak_rss_mib
import argparse
import json
import math
from pathlib import Path
import resource
import signal
import time
from types import SimpleNamespace

import numpy as np
import psutil
from scipy.linalg import null_space
from scipy.optimize import least_squares
from scipy.optimize._numdiff import approx_derivative
from threadpoolctl import threadpool_info, threadpool_limits

import stage2_engine as s

ROOT = Path(__file__).resolve().parent
OUT = output_dir()
LOW = np.r_[1.02, np.full(19, -100.)]
HIGH = np.r_[10., np.full(19, 100.)]


def save(name, value):
    path = OUT/name
    temp = path.with_suffix(".partial")
    temp.write_text(json.dumps(value, indent=2, allow_nan=False))
    temp.replace(path)


def problem():
    x, y = s.e.polar_grid(13, 13, 8.)
    return s.Problem(3, 4, x, y, "fractional2", True)


def case_at(p, prob, label="state"):
    return {"label": label, "nm": 3, "nk": 4, "family": "fractional2", "nr": 13,
            "nt": 13, "rmax": 8., "stable_center": True, "cl": float(p[0]),
            "coefficients": prob.coefficients(p).tolist(), "a0": prob.metadata(p)["a0"]}


def parameters(case):
    assert (case["nm"], case["nk"], case["family"]) == (3, 4, "fractional2")
    return np.r_[case["cl"], case["coefficients"][1:]]


def start_case(name):
    return json.loads((ROOT/"inputs"/("start_"+name+".json")).read_text())


def hybrid_jac(prob, p, fun=None, cl_step=1e-4):
    """Exact coefficient columns; fourth-order central cl column.

    Stage I rounds radial powers to 13 decimals. sqrt(eps) cl steps can amplify
    that quantization. A cl step of 1e-4*max(1,cl) controls it; convergence of
    the column is checked independently. This changes no objective values.
    """
    fun = prob.fun if fun is None else fun
    cl = p[0]
    mats, strain = prob.data(cl)
    c = prob.coefficients(p)
    f = {key: matrix@c for key, matrix in mats.items()}
    d = {key: matrix[:, 1:]-matrix[:, :1]*(strain[None, 1:]/strain[0]) for key, matrix in mats.items()}
    qmat = mats["ratio"]-strain[None, :]
    q = qmat@c
    dq = qmat[:, 1:]-qmat[:, :1]*(strain[None, 1:]/strain[0])
    wx, wy = cl*prob.x-f["psiy"], cl*prob.y+f["psix"]
    t1, t2, t3 = wx*f["fx"], wy*f["fy"], q*f["f"]
    dt1 = wx[:, None]*d["fx"]-f["fx"][:, None]*d["psiy"]
    dt2 = wy[:, None]*d["fy"]+f["fy"][:, None]*d["psix"]
    dt3 = q[:, None]*d["f"]+f["f"][:, None]*dq
    w = (1+prob.x**2+prob.y**2)**((1/cl-1)/2)
    denominator = np.sqrt(t1*t1+t2*t2+t3*t3+(1e-8*w)**2)
    r = (t1+t2+t3)/denominator
    jc = (dt1+dt2+dt3)/denominator[:, None]
    jc -= r[:, None]*(t1[:, None]*dt1+t2[:, None]*dt2+t3[:, None]*dt3)/denominator[:, None]**2
    h = cl_step*max(1, abs(cl))
    def shifted(a):
        point = p.copy()
        point[0] += a*h
        return fun(point)
    jcl = (-shifted(2)+8*shifted(1)-8*shifted(-1)+shifted(-2))/(12*h)
    return np.column_stack((jcl, jc))


class Coordinates:
    def __init__(self, kind, p0, j0):
        self.kind, self.p0 = kind, p0.copy()
        self.column_scale = 1/np.maximum(1e-14, np.linalg.norm(j0, axis=0))
        self.transform = None
        if kind in ("unit", "adaptive"):
            self.z0, self.bounds = p0.copy(), (LOW, HIGH)
        elif kind in ("frozen", "frozen_uncentered"):
            anchor = p0 if kind == "frozen" else np.zeros(20)
            self.z0 = (p0-anchor)/self.column_scale
            self.bounds = ((LOW-anchor)/self.column_scale, (HIGH-anchor)/self.column_scale)
        else:
            assert kind == "svd_box"
            self.mid, self.half = (LOW+HIGH)/2, (HIGH-LOW)/2
            # arctan is a smooth bijection from R to the ORIGINAL open box.
            self.t0 = np.tan(np.pi*(p0-self.mid)/(2*self.half))
            g0 = 2*self.half/(np.pi*(1+self.t0**2))
            _, singular, vt = np.linalg.svd(j0*g0[None, :], full_matrices=False)
            floor = singular[0]*1e-12
            self.transform = vt.T/np.maximum(singular, floor)[None, :]
            self.whitening_singular_values = singular.tolist()
            self.z0 = np.zeros(20)
            self.bounds = (np.full(20, -np.inf), np.full(20, np.inf))

    def forward(self, z):
        if self.kind in ("unit", "adaptive"):
            return z.copy()
        if self.kind in ("frozen", "frozen_uncentered"):
            anchor = self.p0 if self.kind == "frozen" else 0.
            return anchor+self.column_scale*z
        t = self.t0+self.transform@z
        return self.mid+self.half*2/np.pi*np.arctan(t)

    def derivative(self, z):
        if self.kind in ("unit", "adaptive"):
            return np.eye(20)
        if self.kind in ("frozen", "frozen_uncentered"):
            return np.diag(self.column_scale)
        t = self.t0+self.transform@z
        return (2*self.half/(np.pi*(1+t*t)))[:, None]*self.transform

    def inverse(self, p):
        if self.kind in ("unit", "adaptive"):
            return p.copy()
        if self.kind in ("frozen", "frozen_uncentered"):
            anchor = self.p0 if self.kind == "frozen" else 0.
            return (p-anchor)/self.column_scale
        t = np.tan(np.pi*(p-self.mid)/(2*self.half))
        return np.linalg.solve(self.transform, t-self.t0)


def verify():
    old = json.loads((ROOT/"inputs/C_two_layers180.json").read_text())
    f = json.loads((ROOT/"inputs/A45.json").read_text())
    c = s.embed(f, 3, 4, "fractional2")
    embedded = dict(f, nm=3, nk=4, family="fractional2", coefficients=c.tolist(), stable_center=True)
    for name, case in (("S0", old), ("S1", embedded)):
        (ROOT/"inputs"/("start_"+name+".json")).write_text(json.dumps(case, indent=2))
    prob, p = problem(), parameters(old)
    j = hybrid_jac(prob, p)
    jsmall = hybrid_jac(prob, p, cl_step=5e-5)
    jlarge = hybrid_jac(prob, p, cl_step=2e-4)
    legacy = approx_derivative(prob.fun, p, method="2-point", bounds=(LOW, HIGH))
    central = approx_derivative(prob.fun, p, method="3-point", rel_step=2e-5)
    direction = np.cos(np.arange(20)+.3)
    eps = 1e-5
    fd = (prob.fun(p+eps*direction)-prob.fun(p-eps*direction))/(2*eps)
    result = {"same_20_parameter_space": True, "embedding_F_to20": s.embedding_check(f, embedded),
        "hybrid_vs_central_relative_frobenius": float(np.linalg.norm(j-central)/np.linalg.norm(j)),
        "legacy_vs_hybrid_relative_frobenius": float(np.linalg.norm(legacy-j)/np.linalg.norm(j)),
        "cl_column_step_half_relative": float(np.linalg.norm(jsmall[:, 0]-j[:, 0])/np.linalg.norm(j[:, 0])),
        "cl_column_step_double_relative": float(np.linalg.norm(jlarge[:, 0]-j[:, 0])/np.linalg.norm(j[:, 0])),
        "directional_relative_error": float(np.linalg.norm(j@direction-fd)/np.linalg.norm(fd)),
        "legacy_singular_values": np.linalg.svd(legacy, compute_uv=False).tolist(),
        "hybrid_singular_values": np.linalg.svd(j, compute_uv=False).tolist(), "coordinate_checks": {}}
    for kind in ("unit", "adaptive", "frozen", "frozen_uncentered", "svd_box"):
        coord = Coordinates(kind, p, j)
        mapped = coord.forward(coord.z0)
        shifted = p+.0001*np.sin(np.arange(20))
        roundtrip = coord.forward(coord.inverse(shifted))
        direction_z = np.sin(np.arange(20)+.2)
        mapping_derivative = coord.derivative(coord.z0)
        step_z = 5e-6/max(1, np.linalg.norm(mapping_derivative@direction_z))
        numerical = (prob.fun(coord.forward(coord.z0+step_z*direction_z))
                     -prob.fun(coord.forward(coord.z0-step_z*direction_z)))/(2*step_z)
        analytic = j@mapping_derivative@direction_z
        result["coordinate_checks"][kind] = {"initial_parameter_error": float(max(abs(mapped-p))),
            "roundtrip_parameter_error": float(max(abs(roundtrip-shifted))),
            "initial_objective_error": float(max(abs(prob.fun(mapped)-prob.fun(p)))),
            "initial_J_coordinate_condition": float(np.linalg.cond(j@coord.derivative(coord.z0))),
            "chain_rule_direction_relative_error": float(np.linalg.norm(numerical-analytic)/np.linalg.norm(analytic))}
    save("verification.json", result)
    assert result["directional_relative_error"] < 2e-5
    assert result["hybrid_vs_central_relative_frobenius"] < 2e-5
    assert max(row["roundtrip_parameter_error"] for row in result["coordinate_checks"].values()) < 2e-8
    assert max(row["chain_rule_direction_relative_error"] for row in result["coordinate_checks"].values()) < 2e-4
    print(json.dumps(result, indent=2))


def fit(args):
    wall0, cpu0 = time.monotonic(), time.process_time()
    initial = start_case(args.start)
    p0, prob = parameters(initial), problem()
    calls, accepted, jhistory = [], [], []
    phase = ["setup"]
    def physical_fun(p):
        value = prob.fun(p)
        meta = prob.metadata(p)
        calls.append({"evaluation": len(calls)+1, "phase": phase[0], "cost": float(value@value/2),
                      **meta, "wall_seconds": time.monotonic()-wall0, "cpu_seconds": time.process_time()-cpu0})
        return value
    j0 = hybrid_jac(prob, p0, physical_fun)
    coord = Coordinates(args.strategy, p0, j0)
    zstart = coord.z0
    previous_calls = 0
    if args.resume:
        previous = json.loads((OUT/(args.resume+".json")).read_text())
        assert previous["start"] == args.start and previous["strategy"] == args.strategy
        assert previous["jacobian_method"] == args.jacobian
        zstart = coord.inverse(parameters(previous))
        previous_calls = previous["optimizer"]["nfev"]+previous.get("previous_base_calls", 0)
    checkpoint = {**case_at(coord.forward(zstart), prob, args.label), "interrupted": True, "start": args.start,
        "resume_from": args.resume, "previous_base_calls": previous_calls,
        "strategy": args.strategy, "jacobian_method": args.jacobian,
        "settings": {"max_nfev": args.nfev, "ftol": 1e-8, "xtol": 1e-8, "gtol": 1e-8,
                     "physical_bounds": [LOW.tolist(), HIGH.tolist()], "all_nodes_unchanged": True},
        "coordinates": {"initial": coord.z0.tolist(), "column_scale": coord.column_scale.tolist(),
                        "transform": coord.transform.tolist() if coord.transform is not None else None}}
    def store():
        checkpoint.update(history=calls, accepted_states=accepted, jacobian_history=jhistory)
        save(args.label+".json", checkpoint)
    def stop(signum, frame):
        checkpoint["stop"] = "resource SIGTERM; last accepted profile preserved"
        store()
        raise SystemExit(checkpoint["stop"])
    signal.signal(signal.SIGTERM, stop)
    save(args.label+"_start.json", checkpoint)
    phase[0] = "residual"
    cache = {}
    def fun(z):
        p = coord.forward(z)
        value = physical_fun(p)
        cache[tuple(z)] = value
        return value
    def jac(z):
        p = coord.forward(z)
        phase[0] = "jacobian_probe"
        try:
            if args.jacobian == "legacy":
                f0 = cache[tuple(z)] if tuple(z) in cache else physical_fun(p)
                jp = approx_derivative(physical_fun, p, method="2-point", f0=f0, bounds=(LOW, HIGH))
            else:
                jp = hybrid_jac(prob, p, physical_fun)
        finally:
            phase[0] = "residual"
        jy = jp@coord.derivative(z)
        svp, svy = np.linalg.svd(jp, compute_uv=False), np.linalg.svd(jy, compute_uv=False)
        value = cache[tuple(z)]
        case = case_at(p, prob, args.label)
        accepted.append({"parameters": p.tolist(), "coefficients": case["coefficients"],
                         "cl": case["cl"], "a0": case["a0"], "cost": float(value@value/2),
                         "wall_seconds": time.monotonic()-wall0})
        jhistory.append({"index": len(jhistory), "raw_condition": float(svp[0]/svp[-1]),
                         "coordinate_condition": float(svy[0]/max(1e-300, svy[-1])),
                         "physical_gradient_inf": float(max(abs(jp.T@value))),
                         "coordinate_gradient_inf": float(max(abs(jy.T@value))),
                         "singular_values_physical": svp.tolist(), "singular_values_coordinates": svy.tolist()})
        checkpoint.update(case)
        store()
        return jy
    store()
    result = least_squares(fun, zstart, jac=jac, bounds=coord.bounds,
                           x_scale="jac" if args.strategy == "adaptive" else 1.,
                           ftol=1e-8, xtol=1e-8, gtol=1e-8, max_nfev=args.nfev)
    p = coord.forward(result.x)
    finalcase = case_at(p, prob, args.label)
    if not np.array_equal(p, np.array(accepted[-1]["parameters"])):
        accepted.append({"parameters": p.tolist(), "coefficients": finalcase["coefficients"],
                         "cl": finalcase["cl"], "a0": finalcase["a0"], "cost": float(result.cost),
                         "wall_seconds": time.monotonic()-wall0})
    checkpoint.update(finalcase)
    checkpoint.update(interrupted=False, optimizer={"success": bool(result.success), "status": int(result.status),
        "message": result.message, "cost": float(result.cost), "nfev": result.nfev, "njev": result.njev,
        "accepted_steps": len(accepted)-1, "actual_residual_calls": len(calls),
        "setup_calls": sum(row["phase"] == "setup" for row in calls),
        "optimality_coordinates": float(result.optimality),
        "wall_seconds": time.monotonic()-wall0, "cpu_seconds": time.process_time()-cpu0},
        min_cl_evaluated=min(row["cl"] for row in calls), min_abs_a0_evaluated=min(abs(row["a0"]) for row in calls))
    store()
    print(json.dumps({k: checkpoint[k] for k in ("label", "start", "strategy", "cl", "a0", "optimizer")}, indent=2))


def assess(args):
    if args.common_only_batch:
        records = {}
        n = 65
        angles = np.r_[0, 1e-6, .001, (np.arange(n)+.37)*np.pi/(2*n), np.pi/2-.001, np.pi/2-1e-6, np.pi/2]
        x, y = s.polar(np.geomspace(16.48, 128., n), angles)
        for path in sorted(OUT.glob("*.json")):
            case = json.loads(path.read_text())
            if "optimizer" in case and "coefficients" in case:
                records[path.stem] = s.diagnostic(case, x, y)
        save("dense_holdout_checks.json", records)
        print(json.dumps({name: value["max_normalized_Rf"] for name, value in records.items()}, indent=2))
        return
    s.assess(SimpleNamespace(label=args.label, common_grid_batch=False, compare=None))
    case = json.loads((OUT/(args.label+".json")).read_text())
    records = json.loads((OUT/(args.label+"_checks.json")).read_text())
    for n in (17, 33):
        angles = np.r_[0, 1e-6, .001, (np.arange(n)+.37)*np.pi/(2*n), np.pi/2-.001, np.pi/2-1e-6, np.pi/2]
        x, y = s.polar(np.geomspace(16.48, 128, n), angles)
        records["common_H_"+str(n)] = s.diagnostic(case, x, y)
    save(args.label+"_checks.json", records)


def field_design(prob, p, x, y):
    """Derivatives of physical fields w.r.t. the ORIGINAL 20 parameters."""
    case = case_at(p, prob)
    items = s.basis(p[0], 3, 4, "fractional2")
    mats = s.e.matrices(items, x, y)
    strain = np.array([s.e.evaluate(b["ratio"], [0], [0])[0] for b in items])
    result = {key: mat[:, 1:]-mat[:, :1]*strain[None, 1:]/strain[0] for key, mat in mats.items()}
    h = 1e-4*max(1, abs(p[0]))
    values = []
    for a in (2, 1, -1, -2):
        pp = p.copy()
        pp[0] += a*h
        values.append(s.fields(case_at(pp, prob), x, y))
    for key in result:
        column = (-values[0][key]+8*values[1][key]-8*values[2][key]+values[3][key])/(12*h)
        result[key] = np.column_stack((column, result[key]))
    return s.fields(case, x, y), result


def scale_target(case, x, y, ff):
    items = s.basis(case["cl"], 3, 4, "fractional2")
    terms = s.e.merged(items, case["coefficients"], "psi")
    pxx = s.e.evaluate(s.e.derivative(s.e.derivative(terms, 0), 0), x, y)
    pxy = s.e.evaluate(s.e.derivative(s.e.derivative(terms, 0), 1), x, y)
    pyy = s.e.evaluate(s.e.derivative(s.e.derivative(terms, 1), 1), x, y)
    return {"f": -x*ff["fx"]-y*ff["fy"],
            "psix": ff["psix"]-x*pxx-y*pxy,
            "psiy": ff["psiy"]-x*pxy-y*pyy}


def analyze(args):
    file = OUT/(args.label+".json")
    case = json.loads(file.read_text()) if file.exists() else start_case(args.start)
    prob, p = problem(), parameters(case)
    jp = hybrid_jac(prob, p)
    norms = np.linalg.norm(jp, axis=0)
    d = 1/np.maximum(norms, 1e-14)
    jeq = jp*d[None, :]
    ur, sr, vr = np.linalg.svd(jp, full_matrices=False)
    ue, se, ve = np.linalg.svd(jeq, full_matrices=False)
    legacy = approx_derivative(prob.fun, p, method="2-point", bounds=(LOW, HIGH))
    sl = np.linalg.svd(legacy, compute_uv=False)
    vl = np.linalg.svd(legacy, full_matrices=False)[2]
    theta = np.r_[0, 1e-6, .001, (np.arange(17)+.37)*np.pi/34, np.pi/2-.001, np.pi/2-1e-6, np.pi/2]
    x, y = s.polar(np.geomspace(.035, 8., 17), theta)
    x, y = np.r_[0., x], np.r_[0., y]
    ff, designs = field_design(prob, p, x, y)
    target = scale_target(case, x, y, ff)
    a0 = s.fields(case, [0], [0])["f"][0]
    norm_ref = max(1, abs(a0))
    radial = 1+np.hypot(x, y)
    def pack(mats, n, radial):
        return np.vstack([mats["f"], mats["psix"]/radial[:, None], mats["psiy"]/radial[:, None]])/(norm_ref*np.sqrt(3*n))
    def pack_values(vals, n, radial):
        return np.r_[vals["f"], vals["psix"]/radial, vals["psiy"]/radial]/(norm_ref*np.sqrt(3*n))
    bf = designs["f"]/(norm_ref*np.sqrt(len(x)))
    tf = target["f"]/(norm_ref*np.sqrt(len(x)))
    bjoint, tjoint = pack(designs, len(x), radial), pack_values(target, len(x), radial)
    a0_gradient = designs["f"][0]
    # Scale analysis fixes delta cl=0 and delta a0=0 ONLY in a linear projection.
    # No such condition is imposed on any nonlinear solver.
    z = null_space(a0_gradient[None, 1:])
    ffit = np.linalg.lstsq(bf[:, 1:]@z, tf, rcond=1e-12)
    jointfit = np.linalg.lstsq(bjoint[:, 1:]@z, tjoint, rcond=1e-12)
    vf = np.r_[0., z@ffit[0]]
    vjoint = np.r_[0., z@jointfit[0]]
    hx, hy = s.polar(np.geomspace(16.48, 128., 17), theta)
    hf, hd = field_design(prob, p, hx, hy)
    ht = scale_target(case, hx, hy, hf)
    hr = 1+np.hypot(hx, hy)
    bh = pack(hd, len(hx), hr)
    th = pack_values(ht, len(hx), hr)
    bfh, tfh = hd["f"]/(norm_ref*np.sqrt(len(hx))), ht["f"]/(norm_ref*np.sqrt(len(hx)))
    globalfit = np.linalg.lstsq(np.vstack([bjoint[:, 1:]@z, bh[:, 1:]@z]), np.r_[tjoint, th], rcond=1e-12)
    vglobal = np.r_[0., z@globalfit[0]]
    _, sb, vb = np.linalg.svd(bjoint, full_matrices=False)
    whitening = vb.T/sb[None, :]
    shape_j = jp@whitening
    shape_singular = np.linalg.svd(shape_j, compute_uv=False)
    def rel(error, target):
        return float(np.linalg.norm(error)/max(1e-30, np.linalg.norm(target)))
    def cosine(a, b):
        return float(abs(np.dot(a, b))/max(1e-30, np.linalg.norm(a)*np.linalg.norm(b)))
    vs_eq = vjoint/d
    vs_eq /= np.linalg.norm(vs_eq)
    orth = null_space(vs_eq[None, :])
    no_scale_singular = np.linalg.svd(jeq@orth, compute_uv=False)
    def exact_scaled_residual(loglambda):
        lam = np.exp(loglambda)
        f = s.fields(case, prob.x/lam, prob.y/lam)
        f["fx"] /= lam
        f["fy"] /= lam
        f["psix"] *= lam
        f["psiy"] *= lam
        q0 = s.fields(case, [0], [0])["ratio"][0]
        t1 = (p[0]*prob.x-f["psiy"])*f["fx"]
        t2 = (p[0]*prob.y+f["psix"])*f["fy"]
        t3 = (f["ratio"]-q0)*f["f"]
        w = (1+prob.x**2+prob.y**2)**((1/p[0]-1)/2)
        return (t1+t2+t3)/np.sqrt(t1*t1+t2*t2+t3*t3+(1e-8*w)**2)
    eps = 1e-4
    exact_dr = (exact_scaled_residual(eps)-exact_scaled_residual(-eps))/(2*eps)
    # A second projection balances relative field and objective-derivative errors.
    # This diagnoses whether a good field-value fit is also a good operator
    # tangent; it is analysis only, not a solver constraint or a new gauge.
    operator_weight = np.linalg.norm(tjoint)/max(1e-30, np.linalg.norm(exact_dr))
    op_matrix = np.vstack([bjoint[:, 1:]@z, operator_weight*(jp[:, 1:]@z)])
    op_target = np.r_[tjoint, operator_weight*exact_dr]
    opfit = np.linalg.lstsq(op_matrix, op_target, rcond=1e-12)
    voperator = np.r_[0., z@opfit[0]]
    voperator_eq = voperator/d
    voperator_eq /= np.linalg.norm(voperator_eq)
    operator_restricted = np.linalg.svd(jeq@null_space(voperator_eq[None, :]), compute_uv=False)
    tf_fd = (s.fields(case, x/np.exp(eps), y/np.exp(eps))["f"]
             -s.fields(case, x/np.exp(-eps), y/np.exp(-eps))["f"])/(2*eps)
    weak = []
    for k in range(1, 4):
        vp = d*ve[-k]
        field_norm = np.linalg.norm(bjoint@vp)
        vp_field = vp/field_norm
        weak.append({"rank_from_smallest": k, "equilibrated_singular_value": float(se[-k]),
            "physical_unit_field_direction_parameters": vp_field.tolist(),
            "delta_cl_per_unit_field": float(vp_field[0]), "delta_a0_per_unit_field": float(a0_gradient@vp_field),
            "joint_field_cosine_with_exact_scale": cosine(bjoint@vp, tjoint),
            "f_field_cosine_with_exact_scale": cosine(bf@vp, tf),
            "coordinate_cosine_with_projected_scale": cosine(ve[-k], vs_eq)})
    result = {"label": args.label, "cl": case["cl"], "a0": float(a0),
        "jacobians": {"raw_singular_values": sr.tolist(), "equilibrated_singular_values": se.tolist(),
            "raw_condition": float(sr[0]/sr[-1]), "equilibrated_condition": float(se[0]/se[-1]),
            "column_norm_min": float(min(norms)), "column_norm_max": float(max(norms)),
            "raw_right_singular_vectors": vr.tolist(), "equilibrated_right_singular_vectors": ve.tolist(),
            "legacy_singular_values": sl.tolist(), "legacy_vs_hybrid_relative": rel(legacy-jp, jp),
            "smallest_raw_direction_legacy_cosine": cosine(vl[-1], vr[-1]),
            "field_design_singular_values": sb.tolist(), "field_metric_J_singular_values": shape_singular.tolist(),
            "field_metric_J_condition": float(shape_singular[0]/shape_singular[-1])},
        "scaling_tangent": {"delta_cl": 0., "delta_a0_joint_fit": float(a0_gradient@vjoint),
            "coefficient_direction_joint_fit": vjoint.tolist(), "coefficient_direction_f_fit": vf.tolist(),
            "train_f_only_projection_error": rel(bf@vf-tf, tf),
            "holdout_f_only_transfer_error": rel(bfh@vf-tfh, tfh),
            "train_joint_projection_error": rel(bjoint@vjoint-tjoint, tjoint),
            "holdout_joint_transfer_error": rel(bh@vjoint-th, th),
            "train_f_error_from_joint_fit": rel(bf@vjoint-tf, tf),
            "train_and_holdout_joint_best_error": rel(np.r_[bjoint@vglobal-tjoint,bh@vglobal-th], np.r_[tjoint,th]),
            "exact_f_scale_derivative_FD_error": rel(tf_fd-target["f"], target["f"]),
            "overlap_smallest_eq": cosine(vs_eq, ve[-1]),
            "overlap_bottom3_eq": float(np.linalg.norm(ve[-3:]@vs_eq)),
            "overlap_bottom5_eq": float(np.linalg.norm(ve[-5:]@vs_eq)),
            "condition_after_removing_projected_scale": float(no_scale_singular[0]/no_scale_singular[-1]),
            "exact_scale_objective_derivative_norm": float(np.linalg.norm(exact_dr)),
            "objective_residual_norm": float(np.linalg.norm(prob.fun(p))),
            "parameter_scale_vs_exact_objective_derivative_relative_error": rel(jp@vjoint-exact_dr, exact_dr),
            "parameter_scale_objective_derivative_norm": float(np.linalg.norm(jp@vjoint)),
            "operator_balanced_projection": {
                "relative_field_error": rel(bjoint@voperator-tjoint, tjoint),
                "relative_objective_derivative_error": rel(jp@voperator-exact_dr, exact_dr),
                "holdout_field_transfer_error": rel(bh@voperator-th, th),
                "overlap_smallest_eq": cosine(voperator_eq, ve[-1]),
                "overlap_bottom3_eq": float(np.linalg.norm(ve[-3:]@voperator_eq)),
                "condition_after_removing": float(operator_restricted[0]/operator_restricted[-1]),
                "delta_cl": float(voperator[0]), "delta_a0": float(a0_gradient@voperator)},
            "nonlinear_model_not_extended_by_L": True}, "weak_directions": weak}
    save(args.label+"_conditioning.json", result)
    print(json.dumps({"label": args.label, "jacobian_conditions": {key: value for key, value in result["jacobians"].items() if key.endswith("condition")},
                      "scaling_tangent": result["scaling_tangent"], "weak_directions": weak}, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["verify", "fit", "assess", "analyze"])
    parser.add_argument("--label", default="preflight")
    parser.add_argument("--start", default="S0")
    parser.add_argument("--strategy", choices=["unit", "adaptive", "frozen", "frozen_uncentered", "svd_box"], default="unit")
    parser.add_argument("--jacobian", choices=["hybrid", "legacy"], default="hybrid")
    parser.add_argument("--nfev", type=int, default=180)
    parser.add_argument("--resume")
    parser.add_argument("--common-only-batch", action="store_true")
    args = parser.parse_args()
    try:
        with threadpool_limits(limits=1):
            if args.mode == "verify": verify()
            elif args.mode == "fit": fit(args)
            elif args.mode == "assess": assess(args)
            else: analyze(args)
    finally:
        usage = resource.getrusage(resource.RUSAGE_SELF)
        save(args.mode+"_"+args.label+"_process.json", {"peak_rss_mib": peak_rss_mib(usage),
            "cpu_seconds": usage.ru_utime+usage.ru_stime, "threads_at_exit": psutil.Process().num_threads(),
            "nice": psutil.Process().nice(), "threadpools": threadpool_info()})


if __name__ == "__main__":
    main()
