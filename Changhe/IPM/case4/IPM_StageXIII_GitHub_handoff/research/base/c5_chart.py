"""Fixed 19-coordinate nested C5 chart for the unchanged Stage X trial family.

Importing this module performs no numerical experiment.  All callers must run
under the verified Mac Pro launcher/resource supervisor.  The copied engine is
read only; its coefficient ordering, center elimination and PDE loss are used
unchanged.  Chart geometry depends only on the Taylor constraints and historical
physical-field metric, never on assessment residuals.
"""
from functools import lru_cache
import json
from pathlib import Path
import sys

import numpy as np

ENGINE = Path(__file__).resolve().parent / "engine"
if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))
import stage10 as stage10

stage9 = stage10.v
jet = stage9.jet
LOW, HIGH = stage9.LOW, stage9.HIGH


def constraints(p, jac=False):
    """C5=(Ex,Ey,D1,D2,D3), with the verified analytic/complex-step Jacobian."""
    p = np.asarray(p, dtype=float)
    if jac:
        c2, g2 = stage9.constraint(p, True)
        c4, g4 = stage10.fourth(p, True)
        return np.r_[c2, c4], np.vstack([g2, g4])
    return np.r_[stage9.constraint(p), stage10.fourth(p)]


@lru_cache(maxsize=512)
def _hp_cached(parameter_bytes):
    # Decimal.from_float inside the verified series reads the actual saved
    # binary64 center coefficient, including its historical elimination.
    p = np.frombuffer(parameter_bytes, dtype=np.float64)
    return jet.high_precision(p[0], stage9.coefficients(p), prec=70)


def hp_values(p):
    """Independent scalar 70-digit Taylor constraints of physical binary64 p."""
    p = np.ascontiguousarray(p, dtype=np.float64)
    hp = _hp_cached(p.tobytes())
    return np.array([float(v) for v in hp["constraints"] + hp["fourth"]])


def hp_report(p):
    """Independent feasibility, dimensionless defects, center and Poisson jets."""
    p = np.ascontiguousarray(p, dtype=np.float64)
    # Make a separate dictionary so callers cannot alter a cached report.
    hp = json.loads(json.dumps(_hp_cached(p.tobytes())))
    v = {k: float(value) for k, value in hp["jets"].items()}
    a, b, c, d, e, g = (v[k] for k in ("a", "b", "c", "d", "e", "g"))
    u, vv, w, z, k = (v[key] for key in ("u", "v", "w", "z", "k"))
    cl = p[0]
    scales = np.array([
        max(1., abs(2*(2*cl-1)*b), abs(3*a*u)),
        max(1., abs(2*c), abs(a*vv)),
        max(1., abs(4*(2*cl-1)*d), abs(b*u), abs(5*a*w)),
        max(1., abs(4*cl*e), abs(5*b*vv), abs(9*c*u), abs(3*a*z)),
        max(1., abs(4*g), abs(3*c*vv), abs(a*k)),
    ])
    exact = np.array([float(x) for x in hp["constraints"]+hp["fourth"]])
    double = constraints(p)
    return {
        "high_precision": hp,
        "absolute_constraints": exact.tolist(),
        "constraint_term_scales": scales.tolist(),
        "dimensionless_constraints": (exact/scales).tolist(),
        "max_abs": float(np.max(np.abs(exact))),
        "double_constraints": double.tolist(),
        "double_minus_high_precision": (double-exact).tolist(),
        "center_abs": abs(float(hp["center"])),
        "poisson_max_abs": max(abs(float(x)) for x in hp["poisson"]),
        "coefficients": stage9.coefficients(p).tolist(),
        "physical_bounds": bool(np.all(p >= LOW) and np.all(p <= HIGH)),
        "a0": a,
    }


def physical_metric(prob, p):
    """Unmodified historical metric B and its fixed coordinates/normalizer."""
    return stage9.metric(prob, np.asarray(p, dtype=float))


def _c2_tangent(p, pair, free):
    _, g = constraints(p, True)
    r = np.zeros((24, 22))
    r[free] = np.eye(22)
    r[pair] = -np.linalg.solve(g[:2, pair], g[:2, free])
    return r


def build_record(p_anchor, prob, c2_record=None):
    """Construct the frozen invertible 22-map and its 19/3 C4 partition.

    This is a numerical setup operation and must be invoked under the guard.
    No residual or holdout objective is used to select this parameterization.
    """
    p = np.asarray(p_anchor, dtype=float)
    if p.shape != (24,):
        raise ValueError("expected original 24 physical parameters")
    if c2_record is None:
        c2_record = json.loads((ENGINE/"reference_results/chart.json").read_text())
    pair = np.array(c2_record["pair"], dtype=int)
    free = np.array(c2_record["free"], dtype=int)
    if pair.tolist() != [12, 17] or len(free) != 22:
        raise ValueError("historical quadratic chart has changed")
    report = hp_report(p)
    if report["max_abs"] > 1e-10 or not report["physical_bounds"]:
        raise ValueError("C5 anchor fails independent feasibility/bounds")
    b, mr, _, _ = physical_metric(prob, p)
    _, g = constraints(p, True)
    r = _c2_tangent(p, pair, free)
    _, sb, vb = np.linalg.svd(b@r, full_matrices=False)
    if len(sb) != 22 or not np.all(sb > 0):
        raise ValueError("historical field metric lost a direction")
    f22 = vb.T/sb
    u4, s4, vt4 = np.linalg.svd(g[2:]@r@f22, full_matrices=True)
    if len(s4) != 3 or s4[-1] <= s4[0]*1e-10:
        raise ValueError("fourth constraints do not have independent rank three")
    normal = f22@vt4[:3].T
    tangent = f22@vt4[3:].T
    # Complete 22-map is invertible: none of the weak/scaling directions is
    # discarded.  Only the five Taylor constraints reduce dimension.
    complete = np.column_stack([tangent, normal])
    full_field_s = np.linalg.svd(b, compute_uv=False)
    full_f = np.linalg.svd(b, full_matrices=False)[2].T/full_field_s
    gfield = g@full_f
    raw_s = np.linalg.svd(g, compute_uv=False)
    field_s = np.linalg.svd(gfield, compute_uv=False)
    if field_s[-1] <= field_s[0]*1e-10:
        raise ValueError("full C5 constraint Jacobian rank is below five")
    return {
        "schema": "ipm_stage11_nested_c5_chart_v1",
        "dimension": 19,
        "physical_dimension": 24,
        "constraint_names": ["Ex", "Ey", "D1", "D2", "D3"],
        "anchor": p.tolist(),
        "q_anchor": [0.]*19,
        "c2_chart": c2_record,
        "pair": pair.tolist(),
        "free22": free.tolist(),
        "free_map22x19": tangent.tolist(),
        "normal_map22x3": normal.tolist(),
        "complete_map22x22": complete.tolist(),
        "field_whitener22x22": f22.tolist(),
        "field_metric_coordinates": {
            "x": np.asarray(mr[0]).tolist(), "y": np.asarray(mr[1]).tolist(),
            "normalizer": float(mr[2]),
        },
        "field_metric_chart_singular_values": sb.tolist(),
        "full_constraint_raw_singular_values": raw_s.tolist(),
        "full_constraint_field_singular_values": field_s.tolist(),
        "fourth_on_c2_field_singular_values": s4.tolist(),
        "fourth_on_c2_field_left_vectors": u4.tolist(),
        "fourth_on_c2_field_right_vectors": vt4.tolist(),
        "full_constraint_jacobian": g.tolist(),
        "c2_tangent24x22": r.tolist(),
        "c2_pair_condition": float(np.linalg.cond(g[:2, pair])),
        "normal_condition": float(s4[0]/s4[-1]),
        "complete_coordinate_map_condition": float(np.linalg.cond(complete)),
        "target_abs_tolerance": 3e-12,
        "constraint_abs_tolerance": 1e-10,
        "max_pair_condition": float(c2_record["max_pair_condition"]),
        "max_normal_condition": 1e6,
        "min_normal_singular_fraction": 1e-6,
        "normal_branch_field_radius": 2.,
        "pair_branch_radius": float(c2_record["branch_radius"]),
        "inner_max_iterations": 24,
        "outer_max_iterations": 24,
        "anchor_independent_report": report,
        "fixed": True,
        "all_22_coordinate_directions_retained": True,
        "no_objective_or_assessment_values_used_for_geometry": True,
    }


class C5Chart:
    """p(s)=C2lift(p0_free + N*s + E*z(s)), s in R^19.

    z(s) solves C4=0 on the unchanged C2 chart.  The returned tangent is
    R[N-E (G4 R E)^(-1) G4 R N], including all eliminated coefficients.
    Newton solves use independent high-precision residuals and verified analytic
    derivatives; final acceptance uses the independent five-condition defect.
    """
    def __init__(self, record):
        self.record = record
        if record.get("schema") != "ipm_stage11_nested_c5_chart_v1":
            raise ValueError("unrecognized C5 chart record")
        self.anchor = np.array(record["anchor"], dtype=float)
        self.zpair = np.array(record["pair"], dtype=int)
        self.free22 = np.array(record["free22"], dtype=int)
        self.n = np.array(record["free_map22x19"], dtype=float)
        self.e = np.array(record["normal_map22x3"], dtype=float)
        self.complete = np.column_stack([self.n, self.e])
        self.target = float(record["target_abs_tolerance"])
        self.tolerance = float(record["constraint_abs_tolerance"])
        if self.n.shape != (22, 19) or self.e.shape != (22, 3):
            raise ValueError("invalid frozen coordinate map dimensions")
        self.last_diagnostics = None

    def coordinates(self, p):
        """Invert the frozen free-variable map; no nonlinear refit is performed."""
        p = np.asarray(p, dtype=float)
        return np.linalg.solve(self.complete, p[self.free22]-self.anchor[self.free22])[:19]

    def _bounds(self, p):
        if not np.all(np.isfinite(p)) or np.any(p < LOW) or np.any(p > HIGH):
            raise ValueError("chart proposal is outside original physical bounds")

    def _pair_check(self, p, g):
        if np.linalg.cond(g[:2, self.zpair]) > self.record["max_pair_condition"]:
            raise ValueError("historical quadratic implicit pair lost invertibility")
        origin = np.asarray(self.record["c2_chart"]["anchor"])
        if np.max(abs(p[self.zpair]-origin[self.zpair])) > self.record["pair_branch_radius"]:
            raise ValueError("historical quadratic branch radius exceeded")

    def _c2_lift(self, free_values):
        p = self.anchor.copy()
        p[self.free22] = free_values
        self._bounds(p)
        best = p.copy()
        best_norm = np.inf
        for iteration in range(self.record["inner_max_iterations"]):
            c = hp_values(p)[:2]
            _, g = constraints(p, True)
            self._pair_check(p, g)
            norm = float(np.linalg.norm(c))
            if norm < best_norm:
                best, best_norm = p.copy(), norm
            if np.max(abs(c)) <= self.target:
                return p, _c2_tangent(p, self.zpair, self.free22), iteration
            dz = np.linalg.solve(g[:2, self.zpair], -c)
            accepted = False
            for fraction in (1., .5, .25, .125, .0625, .03125, .015625):
                trial = p.copy()
                trial[self.zpair] += fraction*dz
                try:
                    self._bounds(trial)
                except ValueError:
                    continue
                trial_norm = float(np.linalg.norm(hp_values(trial)[:2]))
                if trial_norm < norm:
                    p, accepted = trial, True
                    if trial_norm < best_norm:
                        best, best_norm = p.copy(), trial_norm
                    break
            if not accepted:
                break
        # Binary64 coefficient storage imposes a small quantization floor.  It
        # is reported and independently bounded, never hidden by rounding.
        if np.max(abs(hp_values(best)[:2])) > self.tolerance:
            raise ValueError("quadratic chart did not reach Taylor feasibility")
        _, g = constraints(best, True)
        self._pair_check(best, g)
        return best, _c2_tangent(best, self.zpair, self.free22), iteration

    def _normal_check(self, p, r):
        _, g = constraints(p, True)
        a = g[2:]@r@self.e
        singular = np.linalg.svd(a, compute_uv=False)
        if (singular[-1] <= 0 or singular[0]/singular[-1] > self.record["max_normal_condition"]
                or singular[-1] < self.record["min_normal_singular_fraction"]*
                   self.record["fourth_on_c2_field_singular_values"][-1]):
            raise ValueError("fourth-order implicit block lost local invertibility")
        return a, g

    def lift(self, q, derivative=False):
        q = np.asarray(q, dtype=float)
        if q.shape != (19,) or not np.all(np.isfinite(q)):
            raise ValueError("C5 chart requires 19 finite reduced coordinates")
        # Preserve the user's exact full-precision starting profile before any
        # optimization; its measured 1.2e-12 defect already meets our accuracy
        # needs.  No coefficient is silently rounded or reprojected at zero.
        if np.all(q == 0):
            p = self.anchor.copy()
            self._bounds(p)
            if np.max(abs(hp_values(p))) > self.tolerance:
                raise ValueError("stored C5 anchor has lost feasibility")
            r = _c2_tangent(p, self.zpair, self.free22)
            a, g = self._normal_check(p, r)
            self._pair_check(p, g)
            iterations, inner_total, z = 0, 0, np.zeros(3)
        else:
            z = np.zeros(3)
            best = None
            best_norm = np.inf
            inner_total = 0
            for iterations in range(self.record["outer_max_iterations"]):
                p, r, inner = self._c2_lift(self.anchor[self.free22]+self.n@q+self.e@z)
                inner_total += inner
                a, g = self._normal_check(p, r)
                c = hp_values(p)
                norm = float(np.linalg.norm(c[2:]))
                if norm < best_norm:
                    best, best_norm = (p.copy(), r.copy(), z.copy()), norm
                if np.max(abs(c)) <= self.target:
                    break
                dz = np.linalg.solve(a, -c[2:])
                accepted = False
                for fraction in (1., .5, .25, .125, .0625, .03125, .015625):
                    zz = z+fraction*dz
                    if np.linalg.norm(zz) > self.record["normal_branch_field_radius"]:
                        continue
                    try:
                        trial, tr, inner = self._c2_lift(self.anchor[self.free22]+self.n@q+self.e@zz)
                        inner_total += inner
                        self._normal_check(trial, tr)
                    except ValueError:
                        continue
                    trial_norm = float(np.linalg.norm(hp_values(trial)[2:]))
                    if trial_norm < norm:
                        # Keep the physical point, its C2 derivative and the
                        # associated normal coordinates together, including
                        # when this is the last permitted Newton iteration.
                        p, r, z, accepted = trial, tr, zz, True
                        if trial_norm < best_norm:
                            best = (p.copy(), r.copy(), z.copy())
                            best_norm = trial_norm
                        break
                if not accepted:
                    break
            if best is None:
                raise ValueError("C5 chart produced no feasible branch point")
            # Include the current solved point if the target stopped the loop.
            if np.linalg.norm(hp_values(p)[2:]) <= best_norm:
                best = (p.copy(), r.copy(), z.copy())
            p, r, z = best
            a, g = self._normal_check(p, r)
            if np.max(abs(hp_values(p))) > self.tolerance:
                raise ValueError("C5 chart did not reach independent Taylor feasibility")
        self.last_diagnostics = {
            "outer_iterations": int(iterations),
            "inner_iterations": int(inner_total),
            "normal_coordinates": z.tolist(),
            "pair_condition": float(np.linalg.cond(g[:2, self.zpair])),
            "normal_condition": float(np.linalg.cond(a)),
            "max_high_precision_defect": float(np.max(abs(hp_values(p)))),
        }
        if not derivative:
            return p
        dzdq = -np.linalg.solve(a, g[2:]@r@self.n)
        tangent = r@(self.n+self.e@dzdq)
        self.last_diagnostics["full_constraint_tangent_max_abs"] = float(np.max(abs(g@tangent)))
        return p, tangent
