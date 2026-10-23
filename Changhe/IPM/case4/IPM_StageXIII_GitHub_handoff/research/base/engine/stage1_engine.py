"""Small full-plane IPM pilot. No periodic box, wall, or harmonic strain.

chi = sum c_mk Re[(x+iy)^(2m)] (1+r^2)^(d-m-k), d=(3+1/cl)/2.
rho = -partial_y Delta chi; psi = partial_x partial_y chi.
All fields are analytic on R^2, and U=O(r^(1/cl))=o(r).
"""
from ipm_portable import output_dir, peak_rss_mib
import argparse
from functools import lru_cache
import json
import math
from pathlib import Path
import resource
import signal
import time

import numpy as np
import scipy
from scipy.optimize import least_squares, root
from scipy.special import beta, betainc
from threadpoolctl import threadpool_info, threadpool_limits
import psutil

ROOT = Path(__file__).resolve().parent
OUT = output_dir()


def save(name, data):
    target = OUT / name
    temporary = target.with_suffix(".partial")
    temporary.write_text(json.dumps(data, indent=2, allow_nan=False))
    temporary.replace(target)


def derivative(terms, axis):
    """Terms are (coefficient, x power, y power, (1+r^2) power)."""
    result = []
    for c, a, b, p in terms:
        n = a if axis == 0 else b
        if n:
            result.append((c*n, a-(axis == 0), b-(axis == 1), p))
        if p:
            result.append((2*c*p, a+(axis == 0), b+(axis == 1), p-1))
    return combine(result)


def combine(terms):
    result = {}
    for c, a, b, p in terms:
        key = (a, b, round(p, 13))
        result[key] = result.get(key, 0.0) + c
    return [(c, a, b, p) for (a, b, p), c in result.items() if c != 0]


def laplace(terms):
    return combine(derivative(derivative(terms, 0), 0) + derivative(derivative(terms, 1), 1))


def evaluate(terms, x, y):
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float))
    h = 1+x*x+y*y
    value = np.zeros_like(h)
    for c, a, b, p in terms:
        value += c * x**a * y**b * h**p
    return value


def divide_y(terms):
    assert all(b >= 1 for _, _, b, _ in terms), "parity violation"
    return combine([(c, a, b-1, p) for c, a, b, p in terms])


def basis(cl, nm, nk):
    d = (3+1/cl)/2
    result = []
    for m in range(nm+1):
        for k in range(nk+1):
            chi = [(float((-1)**j * math.comb(2*m, 2*j)), 2*m-2*j, 2*j, d-m-k)
                   for j in range(m+1)]
            psi = derivative(derivative(chi, 0), 1)
            rho = [(-c, a, b, p) for c, a, b, p in derivative(laplace(chi), 1)]
            f = divide_y(rho)
            psix = derivative(psi, 0)
            ratio = divide_y(psix)
            result.append({"f": f, "fx": derivative(f, 0), "fy": derivative(f, 1),
                           "psi": psi, "psix": psix, "psiy": derivative(psi, 1),
                           "ratio": ratio})
    return result


def matrices(items, x, y):
    return {name: np.column_stack([evaluate(item[name], x, y) for item in items])
            for name in items[0]}


def fields(cl, coefficients, nm, nk, x, y):
    return {name: value @ coefficients for name, value in matrices(basis(cl, nm, nk), x, y).items()}


def residual(cl, f, x, y):
    return ((cl*x-f["psiy"])*f["fx"] + (cl*y+f["psix"])*f["fy"]
            + (cl-1+f["ratio"])*f["f"])


def merged(items, coefficients, name):
    return combine([(c*weight, a, b, p) for item, weight in zip(items, coefficients)
                    for c, a, b, p in item[name]])


@lru_cache(None)
def angular_sine_coefficient(a, b, n):
    """Exact finite Fourier expansion of cos(theta)^a sin(theta)^b."""
    if n > a+b or (a+b+n) % 2:
        return 0.0
    total = 0
    target = (a+b+n)//2
    for j in range(a+1):
        k = target-j
        if 0 <= k <= b:
            total += math.comb(a, j)*math.comb(b, k)*(-1)**(b-k)
    return float(-2 * (total / (2**(a+b) * 1j**b)).imag)


def modal_source(source):
    modes = {}
    for c, a, b, p in source:
        for n in range(2, a+b+1, 2):
            amplitude = c * angular_sine_coefficient(a, b, n)
            if amplitude:
                key = (a+b, p)
                modes.setdefault(n, {})[key] = modes.setdefault(n, {}).get(key, 0) + amplitude
    return modes


def canonical_inverse(source, points, order=80):
    """Independent polar Green integral of rho_x over 0<r<infinity.

    Interior integral: Gauss Legendre; exterior: incomplete beta, including
    the entire infinite tail. No fitted potential or boundary values used.
    """
    modes = modal_source(source)
    z, w = np.polynomial.legendre.leggauss(order)
    answer = []
    for x, y in points:
        r = math.hypot(x, y)
        if not r:
            strain = 0.0
            for (degree, p), amplitude in modes.get(2, {}).items():
                aa = -p-degree/2
                bb = degree/2
                assert aa > 0 and bb > 0
                strain += amplitude * beta(aa, bb)/4
            answer.append({"psi": 0.0, "psix": 0.0, "psiy": 0.0, "strain": float(strain)})
            continue
        theta = math.atan2(y, x)
        s = r*(z+1)/2
        value = radial = angular = 0.0
        for n, terms in modes.items():
            gn = np.zeros_like(s)
            exterior = 0.0
            for (degree, p), amplitude in terms.items():
                gn += amplitude * s**degree * (1+s*s)**p
                aa = -p-(degree+2-n)/2
                bb = (degree+2-n)/2
                assert aa > 0 and bb > 0, (aa, bb, n, degree, p)
                exterior += amplitude * beta(aa, bb)*betainc(aa, bb, 1/(1+r*r))/2
            interior = r/2 * np.dot(w, s**(n+1)*gn)
            pn = (r**(-n)*interior + r**n*exterior)/(2*n)
            dn = (-r**(-n-1)*interior + r**(n-1)*exterior)/2
            value += pn*math.sin(n*theta)
            radial += dn*math.sin(n*theta)
            angular += n*pn*math.cos(n*theta)
        answer.append({"psi": float(value),
                       "psix": float(math.cos(theta)*radial-math.sin(theta)*angular/r),
                       "psiy": float(math.sin(theta)*radial+math.cos(theta)*angular/r)})
    return answer


def exterior_strain(source, radius):
    """Contribution from source outside radius to psi_xy(0)."""
    total = 0.0
    for (degree, p), amplitude in modal_source(source).get(2, {}).items():
        aa, bb = -p-degree/2, degree/2
        total += amplitude*beta(aa, bb)*betainc(aa, bb, 1/(1+radius*radius))/4
    return float(total)


def verify():
    start = time.monotonic()
    points = [(0, 0), (.2, .3), (1, .4), (2, 3), (0, 2), (2, 0)]
    manufactured = []
    for exponent in (1, 2):
        source = [(-2*exponent, 1, 1, -exponent-1)]
        results = canonical_inverse(source, points)
        errors = []
        for (x, y), computed in zip(points, results):
            q = x*x+y*y
            if q == 0:
                errors.append(abs(computed["strain"]+.25))
                continue
            integral = q-np.log1p(q) if exponent == 1 else np.log1p(q)+1/(1+q)-1
            h = -integral/(2*q*q)
            hp = -(1+q)**(-exponent)/(2*q)+integral/q**3
            exact = {"psi": x*y*h, "psix": y*h+2*x*x*y*hp,
                     "psiy": x*h+2*x*y*y*hp}
            errors += [abs(computed[key]-value) for key, value in exact.items()]
        manufactured.append({"rho": "y/(1+r^2)^"+str(exponent),
                             "max_psi_or_velocity_abs_error": max(errors),
                             "canonical_center_strain": results[0]["strain"]})
    cl, nm, nk = 2.0, 1, 1
    items = basis(cl, nm, nk)
    coefficients = np.array([-.12, .09, .02, -.01])
    source = [(c, a, b+1, p) for c, a, b, p in merged(items, coefficients, "fx")]
    check = canonical_inverse(source, points)
    xx, yy = np.array(points).T
    exact = fields(cl, coefficients, nm, nk, xx, yy)
    inverse_error = max(abs(value[key]-exact[key][j]) for j, value in enumerate(check)
                        for key in ("psi", "psix", "psiy"))
    center_strain = fields(cl, coefficients, nm, nk, [0], [0])["ratio"][0]
    inverse_strain_error = abs(check[0]["strain"]-center_strain)
    lap = laplace(merged(items, coefficients, "psi"))
    poisson_error = np.max(np.abs(-evaluate(lap, xx, yy)-yy*exact["fx"]))
    parity = 0.0
    for sx, sy in ((-1, 1), (1, -1), (-1, -1)):
        other = fields(cl, coefficients, nm, nk, sx*xx, sy*yy)
        parity = max(parity, np.max(abs(other["f"]-exact["f"])),
                     np.max(abs(other["psi"]-sx*sy*exact["psi"])),
                     np.max(abs(other["ratio"]-exact["ratio"])))
    result = {"numpy": np.__version__, "scipy": scipy.__version__,
              "threadpools": threadpool_info(), "manufactured": manufactured,
              "basis_full_plane_inverse_abs_error": float(inverse_error),
              "basis_center_strain_inverse_abs_error": float(inverse_strain_error),
              "algebraic_poisson_abs_error": float(poisson_error), "parity_abs_error": float(parity),
              "seconds": time.monotonic()-start}
    save("verification.json", result)
    print(json.dumps(result, indent=2))
    assert max(x["max_psi_or_velocity_abs_error"] for x in manufactured) < 1e-9
    assert inverse_error < 1e-9 and inverse_strain_error < 1e-9 and poisson_error < 1e-9


def polar_grid(nr, nt, rmax, holdout=False):
    if holdout:
        radii = np.geomspace(.035, rmax, nr)
        theta = np.unique(np.r_[0, np.pi/2, 1e-5, np.pi/2-1e-5,
                               (np.arange(nt)+.37)*np.pi/(2*nt)])
    else:
        radii = np.r_[0, np.geomspace(.08, rmax, nr-1)]
        theta = np.linspace(0, np.pi/2, nt)
    r, t = np.meshgrid(radii, theta, indexing="ij")
    return (r*np.cos(t)).ravel(), (r*np.sin(t)).ravel()


class Fit:
    def __init__(self, nm, nk, x, y, objective="absolute"):
        self.nm, self.nk, self.x, self.y = nm, nk, x, y
        self.objective = objective
        self.cached_cl, self.cached = None, None

    def data(self, cl):
        if cl != self.cached_cl:
            items = basis(cl, self.nm, self.nk)
            self.cached = (matrices(items, self.x, self.y),
                           np.array([evaluate(item["ratio"], [0], [0])[0] for item in items]))
            self.cached_cl = cl
        return self.cached

    def coefficients(self, parameters):
        cl = parameters[0]
        _, strain = self.data(cl)
        return np.r_[(1-cl-strain[1:] @ parameters[1:])/strain[0], parameters[1:]]

    def fun(self, parameters):
        cl = parameters[0]
        mats, _ = self.data(cl)
        c = self.coefficients(parameters)
        f = {name: matrix @ c for name, matrix in mats.items()}
        weight = (1+self.x**2+self.y**2)**((1/cl-1)/2)
        rf = residual(cl, f, self.x, self.y)
        if self.objective == "relative":
            t1 = (cl*self.x-f["psiy"])*f["fx"]
            t2 = (cl*self.y+f["psix"])*f["fy"]
            t3 = (cl-1+f["ratio"])*f["f"]
            return rf/np.sqrt(t1*t1+t2*t2+t3*t3+(1e-8*weight)**2)
        return rf/weight

    def jac(self, parameters):
        cl = parameters[0]
        mats, strain = self.data(cl)
        c = self.coefficients(parameters)
        f = {name: matrix @ c for name, matrix in mats.items()}
        x, y = self.x[:, None], self.y[:, None]
        derivative_c = ((cl*x-f["psiy"][:, None])*mats["fx"]
                        + (cl*y+f["psix"][:, None])*mats["fy"]
                        + (cl-1+f["ratio"][:, None])*mats["f"]
                        - mats["psiy"]*f["fx"][:, None] + mats["psix"]*f["fy"][:, None]
                        + mats["ratio"]*f["f"][:, None])
        jac_c = derivative_c[:, 1:]-derivative_c[:, :1]*strain[None, 1:]/strain[0]
        weight = (1+self.x**2+self.y**2)**((1/cl-1)/2)
        step = 2e-5
        plus, minus = parameters.copy(), parameters.copy()
        plus[0] += step
        minus[0] -= step
        jac_cl = (self.fun(plus)-self.fun(minus))/(2*step)
        return np.column_stack((jac_cl, jac_c/weight[:, None]))


def diagnostics(cl, c, nm, nk, x, y):
    f = fields(cl, c, nm, nk, x, y)
    rf = residual(cl, f, x, y)
    rr = y*rf
    # Sum of magnitudes of terms in each ORIGINAL equation, floor declared.
    df = (np.abs((cl*x-f["psiy"])*f["fx"])+np.abs((cl*y+f["psix"])*f["fy"])
          +np.abs((cl-1+f["ratio"])*f["f"]))
    rho, rhox, rhoy = y*f["f"], y*f["fx"], f["f"]+y*f["fy"]
    dr = np.abs((cl*x-f["psiy"])*rhox)+np.abs((cl*y+f["psix"])*rhoy)+np.abs(rho)
    floor_f = 1e-10*max(1, abs(fields(cl, c, nm, nk, [0], [0])["f"][0]))
    floor_r = 1e-10*max(1, float(np.max(np.abs(rho))))
    return {"npoints": len(x), "rmin": float(np.min(np.hypot(x, y))),
            "rmax": float(np.max(np.hypot(x, y))),
            "max_abs_Rf": float(np.max(np.abs(rf))), "max_abs_Rrho": float(np.max(np.abs(rr))),
            "max_normalized_Rf": float(np.max(np.abs(rf)/np.maximum(df, floor_f))),
            "max_normalized_Rrho": float(np.max(np.abs(rr)/np.maximum(dr, floor_r))),
            "rms_normalized_Rf": float(np.sqrt(np.mean((rf/np.maximum(df, floor_f))**2))),
            "denominator_floor_f": floor_f, "denominator_floor_rho": floor_r,
            "max_tail_scaled_Rf": float(np.max(np.abs(rf)/(1+x*x+y*y)**((1/cl-1)/2)))}


def fit(args):
    start = time.monotonic()
    x, y = polar_grid(args.nr, args.nt, args.rmax)
    problem = Fit(args.nm, args.nk, x, y, args.objective)
    count = (args.nm+1)*(args.nk+1)
    cl = args.initial_cl
    items = basis(cl, args.nm, args.nk)
    strain = np.array([evaluate(b["ratio"], [0], [0])[0] for b in items])
    a0 = np.array([evaluate(b["f"], [0], [0])[0] for b in items])
    if args.resume:
        previous = json.loads((OUT / (args.resume+".json")).read_text())
        cl = previous["cl"]
        old = np.array(previous["coefficients"])
        c = np.zeros(count)
        old_nk = previous["nk"]
        for m in range(previous["nm"]+1):
            for k in range(old_nk+1):
                c[m*(args.nk+1)+k] = old[m*(old_nk+1)+k]
    elif args.sign < 0:
        constraints = np.vstack([strain, a0])
        c = np.linalg.lstsq(constraints, [1-cl, -4*(cl-1)], rcond=None)[0]
    else:
        c = np.zeros(count)
        c[0] = (1-cl)/strain[0]
        if args.perturb:
            c[1:] = args.perturb*np.sin(np.arange(1, count))
            c[0] = (1-cl-strain[1:] @ c[1:])/strain[0]
    parameters = np.r_[cl, c[1:]]
    before = diagnostics(cl, c, args.nm, args.nk, x, y)
    # Record initial data BEFORE fitting; center identity is eliminated, not a penalty.
    initial = {"cl": cl, "a0": float(fields(cl, c, args.nm, args.nk, [0], [0])["f"][0]),
               "coefficients": c.tolist(), "diagnostics": before}
    checkpoint = {"label": args.label, "nm": args.nm, "nk": args.nk,
                  "nr": args.nr, "nt": args.nt, "rmax": args.rmax, "initial": initial,
                  "objective": args.objective,
                  "cl": cl, "coefficients": c.tolist(), "interrupted": True}
    save(args.label+".json", checkpoint)
    def stop(signum, frame):
        raise SystemExit("Resource stop; initial checkpoint preserved.")
    signal.signal(signal.SIGTERM, stop)
    # Verify supplied Jacobian against an independent directional finite difference.
    direction = np.cos(np.arange(count)+.2)
    epsilon = 1e-6
    jac_error = None
    if args.objective == "absolute":
        analytic = problem.jac(parameters) @ direction
        numeric = (problem.fun(parameters+epsilon*direction)-problem.fun(parameters-epsilon*direction))/(2*epsilon)
        jac_error = float(np.max(abs(analytic-numeric))/max(1, np.max(abs(numeric))))
        assert jac_error < 1e-5, jac_error
    evaluations = [0]
    def checkpointed_fun(p):
        value = problem.fun(p)
        evaluations[0] += 1
        if evaluations[0] % 5 == 0:
            checkpoint.update(cl=float(p[0]), coefficients=problem.coefficients(p).tolist(),
                              evaluations=evaluations[0], weighted_rms=float(np.sqrt(np.mean(value**2))))
            save(args.label+".json", checkpoint)
        return value
    result = least_squares(checkpointed_fun, parameters,
                           jac=problem.jac if args.objective == "absolute" else "2-point",
                           bounds=(np.r_[1.02, np.full(count-1, -100)],
                                   np.r_[10, np.full(count-1, 100)]),
                           max_nfev=args.nfev, ftol=1e-8, xtol=1e-8, gtol=1e-8)
    cl = result.x[0]
    c = problem.coefficients(result.x)
    center = fields(cl, c, args.nm, args.nk, [0], [0])
    checkpoint.update({"cl": float(cl), "a0": float(center["f"][0]),
                       "strain": float(center["ratio"][0]),
                       "center_identity_defect": float(abs(cl+center["ratio"][0]-1)),
                       "coefficients": c.tolist(), "interrupted": False,
                       "jac_directional_relative_error": jac_error,
                       "optimizer": {"success": bool(result.success), "status": int(result.status),
                                     "nfev": result.nfev, "njev": result.njev,
                                     "cost": result.cost, "message": result.message},
                       "fit": diagnostics(cl, c, args.nm, args.nk, x, y),
                       "seconds": time.monotonic()-start})
    save(args.label+".json", checkpoint)
    print(json.dumps(checkpoint, indent=2))


def assess(args):
    data = json.loads((OUT / (args.label+".json")).read_text())
    cl, c, nm, nk = data["cl"], np.array(data["coefficients"]), data["nm"], data["nk"]
    items = basis(cl, nm, nk)
    checks = {}
    for name, radii in (("between_nodes", (0.035, data["rmax"])),
                        ("outside_fit", (data["rmax"]*1.03, 32))):
        r = np.geomspace(*radii, 17)
        theta = np.r_[0, 1e-6, .001, (np.arange(17)+.37)*np.pi/34, np.pi/2-.001, np.pi/2-1e-6, np.pi/2]
        rr, tt = np.meshgrid(r, theta, indexing="ij")
        x, y = (rr*np.cos(tt)).ravel(), (rr*np.sin(tt)).ravel()
        checks[name] = diagnostics(cl, c, nm, nk, x, y)
    # Axes use actual zero coordinates, not a small-y numerical quotient.
    ax = np.r_[0, np.geomspace(.01, 32, 50)]
    checks["x_axis"] = diagnostics(cl, c, nm, nk, ax, np.zeros_like(ax))
    checks["y_axis"] = diagnostics(cl, c, nm, nk, np.zeros_like(ax), ax)
    points = [(0, 0), (.3, .2), (1, .7), (2, 1.5), (0, 2), (2, 0)]
    x, y = np.array(points).T
    exact = fields(cl, c, nm, nk, x, y)
    source = [(coef, a, b+1, p) for coef, a, b, p in merged(items, c, "fx")]
    inverse80 = canonical_inverse(source, points, 80)
    inverse120 = canonical_inverse(source, points, 120)
    inverse_abs = max(abs(row[key]-exact[key][j]) for j, row in enumerate(inverse80)
                      for key in ("psi", "psix", "psiy"))
    inverse_scale = max(abs(v) for key in ("psi", "psix", "psiy") for v in exact[key])
    checks["canonical_inverse"] = {"max_abs_error": inverse_abs,
        "max_error_over_max_field": inverse_abs/max(1e-14, inverse_scale),
        "80_vs_120_max_abs": max(abs(a[key]-b[key]) for a, b in zip(inverse80, inverse120)
                                  for key in ("psi", "psix", "psiy")),
        "center_strain_error": abs(inverse80[0]["strain"]-data["strain"]),
        "points": points, "outside_radius_strain_contribution":
        {str(r): exterior_strain(source, r) for r in (data["rmax"], 16, 32, 128)}}
    # Independent Cartesian finite-difference Poisson check: no derivative term lists.
    poisson_fd = []
    for step in (.002, .001):
        total = np.zeros_like(x)
        centerpsi = exact["psi"]
        for dx, dy in ((step, 0), (0, step)):
            total += (fields(cl, c, nm, nk, x+dx, y+dy)["psi"]-2*centerpsi
                      +fields(cl, c, nm, nk, x-dx, y-dy)["psi"])/step**2
        g = y*exact["fx"]
        error = np.abs(-total-g)
        poisson_fd.append({"step": step, "max_abs": float(max(error)),
                           "max_error_over_max_source": float(max(error)/max(1e-14, max(abs(g))))})
    checks["cartesian_poisson_fd"] = poisson_fd
    # Off-grid independent transport derivatives: 4th-order Cartesian differences
    # of field VALUES. H=psi/(xy) is formed symbolically, so the axis ratio is
    # H+x H_x, never a quotient by a small coordinate.
    offgrid = np.array([(0, 0), (.173, .291), (.721, 1.137), (2.31, .817),
                        (.73, 0), (0, .91), (1.13, 1e-9), (1e-9, 1.29),
                        (-.731, .419), (.382, -.927), (3.73, 2.11), (9.1, 4.7),
                        (17.3, 11.2), (0, 23.1), (29.1, 0)])
    xx, yy = offgrid.T
    f_terms = merged(items, c, "f")
    h_terms = [(coef, a-1, b-1, p) for coef, a, b, p in merged(items, c, "psi")]
    assert all(a >= 0 and b >= 0 for _, a, b, _ in h_terms)
    f_value = lambda a, b: evaluate(f_terms, a, b)
    h_value = lambda a, b: evaluate(h_terms, a, b)
    rho_value = lambda a, b: b*f_value(a, b)
    transport_fd = []
    analytic_offgrid = fields(cl, c, nm, nk, xx, yy)
    exact_rf = residual(cl, analytic_offgrid, xx, yy)
    for base_step in (.002, .001):
        step = base_step*np.maximum(1, np.hypot(xx, yy))
        def difference(value, axis):
            dx, dy = (step, 0) if axis == 0 else (0, step)
            return (-value(xx+2*dx, yy+2*dy)+8*value(xx+dx, yy+dy)
                    -8*value(xx-dx, yy-dy)+value(xx-2*dx, yy-2*dy))/(12*step)
        hh = h_value(xx, yy)
        q_value = hh+xx*difference(h_value, 0)
        wx = cl*xx-xx*(hh+yy*difference(h_value, 1))
        wy = cl*yy+yy*q_value
        rf_fd = wx*difference(f_value, 0)+wy*difference(f_value, 1)+(cl-1+q_value)*f_value(xx, yy)
        rr_fd = wx*difference(rho_value, 0)+wy*difference(rho_value, 1)-rho_value(xx, yy)
        transport_fd.append({"base_step_times_max_1_r": base_step,
            "max_abs_Rf_independent": float(max(abs(rf_fd))),
            "max_abs_Rrho_independent": float(max(abs(rr_fd))),
            "max_Rf_disagreement": float(max(abs(rf_fd-exact_rf))),
            "max_Rrho_disagreement": float(max(abs(rr_fd-yy*exact_rf)))})
    checks["independent_cartesian_transport"] = {"points": offgrid.tolist(), "steps": transport_fd}
    # Necessary quadratic Taylor constraints for Rf=0; center identity already exact.
    def center_derivative(name, axis):
        terms = derivative(derivative(merged(items, c, name), axis), axis)
        return float(evaluate(terms, [0], [0])[0])
    fxx, fyy = center_derivative("f", 0), center_derivative("f", 1)
    qxx, qyy = center_derivative("ratio", 0), center_derivative("ratio", 1)
    checks["taylor"] = {"fxx": fxx, "fyy": fyy, "ratio_xx": qxx, "ratio_yy": qyy,
                         "Rf_x2_coefficient": (2*cl-1)*fxx+data["a0"]*qxx/2,
                         "Rf_y2_coefficient": fyy+data["a0"]*qyy/2}
    # Exactly represent the genuine orbit: rho_L=L rho(X/L), psi_L=L^2 psi(X/L).
    # At corresponding points Rf is unchanged and Rrho is multiplied by L.
    scale = 2.0
    rf = residual(cl, exact, x, y)
    transformed = {key: value.copy() for key, value in exact.items()}
    for key in ("psix", "psiy"):
        transformed[key] *= scale
    for key in ("fx", "fy"):
        transformed[key] /= scale
    scaled_rf = residual(cl, transformed, scale*x, scale*y)
    checks["scale_orbit"] = {"lambda": scale, "Rf_invariance_error": float(max(abs(scaled_rf-rf))),
                             "Rrho_covariance_error": float(max(abs(scale*y*scaled_rf-scale*y*rf))),
                             "a0_invariance_error": 0.0, "cl_invariance_error": 0.0}
    parity_error = 0.0
    for sx, sy in ((-1, 1), (1, -1), (-1, -1)):
        z = fields(cl, c, nm, nk, sx*x, sy*y)
        parity_error = max(parity_error, float(max(abs(z["f"]-exact["f"]))),
                           float(max(abs(z["psi"]-sx*sy*exact["psi"]))))
    checks["parity_max_abs_error"] = parity_error
    # Far-tail growth and |U|/r on a whole quadrant, independent of fitting nodes.
    theta = np.linspace(0, np.pi/2, 31)
    tails = []
    for r in (8, 16, 32, 64, 128, 256):
        xx, yy = r*np.cos(theta), r*np.sin(theta)
        z = fields(cl, c, nm, nk, xx, yy)
        rho = yy*z["f"]
        grad = np.hypot(yy*z["fx"], z["f"]+yy*z["fy"])
        tails.append({"radius": r, "max_abs_rho": float(max(abs(rho))),
                      "max_abs_U_over_r": float(max(np.hypot(z["psix"], z["psiy"]))/r),
                      "weighted_density_gradient": float(max(abs(rho)+(1+r)*grad)/(1+r)**(1/cl))})
    checks["tails"] = tails
    checks["tail_gamma_by_construction"] = 1/cl
    # W roots: origin is exact. Bounded multistart search is evidence, not completeness.
    def w(point):
        z = fields(cl, c, nm, nk, [point[0]], [point[1]])
        return np.array([cl*point[0]-z["psiy"][0], cl*point[1]+z["psix"][0]])
    roots = [[0.0, 0.0]]
    for guess in ((.2, .2), (1, 0), (0, 1), (1, 1), (3, 0), (0, 3), (3, 3)):
        solved = root(w, guess, options={"maxfev": 70})
        candidate = np.abs(solved.x)
        if solved.success and np.linalg.norm(w(candidate)) < 1e-7 and max(candidate) <= 32:
            if all(np.linalg.norm(candidate-np.array(previous)) > 1e-5 for previous in roots):
                roots.append(candidate.tolist())
    checks["W_stationary_point_search"] = {"roots_first_quadrant": roots,
        "origin_jacobian_eigenvalues": [2*cl-1, 1.0], "seeds": 7,
        "complete_enumeration": False, "characteristics_integrated": False}
    save(args.label+"_checks.json", checks)
    print(json.dumps(checks, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["verify", "fit", "assess"])
    parser.add_argument("--label", default="trial")
    parser.add_argument("--nm", type=int)
    parser.add_argument("--nk", type=int)
    parser.add_argument("--nr", type=int)
    parser.add_argument("--nt", type=int)
    parser.add_argument("--rmax", type=float)
    parser.add_argument("--initial-cl", type=float, default=2)
    parser.add_argument("--sign", type=int, default=1)
    parser.add_argument("--perturb", type=float, default=0)
    parser.add_argument("--resume")
    parser.add_argument("--nfev", type=int, default=30)
    parser.add_argument("--objective", choices=["absolute", "relative"], default="absolute")
    args = parser.parse_args()
    try:
        with threadpool_limits(limits=1):
            if args.mode == "verify":
                verify()
            elif args.mode == "fit":
                assert all(getattr(args, name) is not None for name in ("nm", "nk", "nr", "nt", "rmax"))
                fit(args)
            else:
                assess(args)
    finally:
        usage = resource.getrusage(resource.RUSAGE_SELF)
        proc = psutil.Process()
        save(args.mode+"_"+args.label+"_process.json", {
            "peak_rss_mib": peak_rss_mib(usage),
            "cpu_seconds": usage.ru_utime+usage.ru_stime,
            "threads_at_exit": proc.num_threads(), "nice": proc.nice(),
            "threadpools": threadpool_info(), "ru_maxrss_units": "platform adapter to MiB"})


if __name__ == "__main__":
    main()
