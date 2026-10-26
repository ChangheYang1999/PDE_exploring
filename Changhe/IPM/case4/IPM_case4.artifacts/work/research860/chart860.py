"""Analytic-center C5 chart for the 860 T1 representation: raw P = [cl, a_1..a_59] (low monomials) -> 55 feasible (SPEC v5 section 7).

Same semantics as the frozen absolute_chart_v2.AbsoluteC5ChartV2: raw P = [cl, c_1..c_59] with c_0 eliminated by
the exact center condition; five Taylor compatibility equations E_x, E_y, D_1, D_2, D_3; coefficient-only right-inverse
normal corrections (zero cl row); full-row SVD complement gives the 55 free seeds; Newton lift with backtracking at
target 3e-12 and tolerance 1e-10; cl bit pattern preserved by the lift. Bounds inherited: 1.02<=cl<=10, |c_i|<=100.
"""
import json
from decimal import Decimal, localcontext
import numpy as np
import basis860 as B

LOW = np.r_[1.02, np.full(59, -100.)]
HIGH = np.r_[10., np.full(59, 100.)]
NRAW, NFREE, NCON = 60, 55, 5


def coefficients(P):
    """Analytic center elimination supporting complex-step cl: c_0 = (1-cl-sum s_i c_i)/s_0 with s = jet h row."""
    P = np.asarray(P); M = B.jet_matrix(P[0])             # 12 x 60, row 6 = h = strain
    c0 = (1-P[0]-M[6, 1:]@P[1:])/M[6, 0]
    return np.r_[c0, P[1:]]


def constraint_values(P):
    P = np.asarray(P)
    a, b, c, d, f, g, h, u, v, w, z, k = B.jet_matrix(P[0])@coefficients(P)
    cl = P[0]
    return np.asarray([2*(2*cl-1)*b+3*a*u, 2*c+a*v, 4*(2*cl-1)*d+b*u+5*a*w, 4*cl*f-5*b*v+9*c*u+3*a*z, 4*g+3*c*v+a*k])


def constraint_jacobian(P):
    """Complex-step derivative in every raw parameter including cl (exponents, c_0 chain)."""
    P = np.asarray(P, dtype=float); result = np.empty((NCON, NRAW))
    for i in range(NRAW):
        probe = P.astype(complex); probe[i] += 1e-25j
        result[:, i] = np.imag(constraint_values(probe))/1e-25
    return result


def six_constraints_unreduced(z):
    """Center defect and the five Taylor conditions as functions of (cl, a_000, a_1..a_59) with a_000 an independent variable (complex-step capable)."""
    z = np.asarray(z); clz = z[0]; a60 = z[1:]
    a, b, c, d, f, g, h, u, v, w, zz, k = B.jet_matrix(clz)@a60
    return np.asarray([h-(1-clz), 2*(2*clz-1)*b+3*a*u, 2*c+a*v, 4*(2*clz-1)*d+b*u+5*a*w, 4*clz*f-5*b*v+9*c*u+3*a*zz, 4*g+3*c*v+a*k])


def unreduced_constraint_jacobian(P):
    """6 x 61 Jacobian of (center, C5) in (cl, a_000, a_1..a_59) at the chart point (a_000 from the analytic elimination); the 800 high
    coordinates have identically zero rows, so this matrix carries the rank of the full 6 x 861 system (expected rank 6)."""
    P = np.asarray(P, dtype=float); a000 = float(hp_report(P)['coefficients_decimal'][0])
    z0 = np.r_[P[0], a000, P[1:]].astype(complex); G = np.empty((6, 61))
    for i in range(61):
        probe = z0.copy(); probe[i] += 1e-25j; G[:, i] = np.imag(six_constraints_unreduced(probe))/1e-25
    return G


def hp_report(P, precision=70):
    """Independent Decimal evaluation of center, five constraints, Poisson jets, a0 and bounds."""
    P = np.asarray(P, dtype=float)
    with localcontext() as ctx:
        ctx.prec = precision
        cl = Decimal.from_float(float(P[0])); columns = B.jets(cl, True)
        c = [Decimal(0)]+[Decimal.from_float(float(x)) for x in P[1:]]
        c[0] = (1-cl-sum((columns[j][6]*c[j] for j in range(1, NRAW)), Decimal(0)))/columns[0][6]
        values = [sum((columns[j][i]*c[j] for j in range(NRAW)), Decimal(0)) for i in range(12)]
        a, b, cy, d, f, g, h, u, v, w, z, k = values
        cc = [2*(2*cl-1)*b+3*a*u, 2*cy+a*v, 4*(2*cl-1)*d+b*u+5*a*w, 4*cl*f-5*b*v+9*cy*u+3*a*z, 4*g+3*cy*v+a*k]
        poisson = [3*(u+v)+b, 20*w+6*z+4*d, 6*z+20*k+2*f]
        center = cl+h-1
        return {'precision': precision, 'center_convention': 'analytic_center_elimination',
                'coefficients_decimal': [str(x) for x in c], 'jets': dict(zip(B.JET_NAMES, map(str, values))),
                'constraints_decimal': list(map(str, cc)), 'constraints': [float(x) for x in cc],
                'max_abs': float(max(abs(x) for x in cc)), 'center_decimal': str(center), 'center_abs': float(abs(center)),
                'poisson_max_abs': float(max(abs(x) for x in poisson)), 'a0': float(a),
                'physical_bounds': bool(np.all(P >= LOW) and np.all(P <= HIGH))}


class Chart860:
    version = 'chart860_analytic_center_full55_c5_rightinverse_v2_T1'

    def __init__(self, P, tolerance=1e-10, target=3e-12):
        self.base = np.asarray(P, dtype=float).copy(); self.tolerance = float(tolerance); self.target = float(target)
        if self.base.shape != (NRAW,): raise ValueError('Expected 60 raw chart parameters [cl, c_1..c_59]')
        self._verify(self.base)
        g = constraint_jacobian(self.base)
        norms = np.linalg.norm(g[:, 1:], axis=1)
        if not np.all(np.isfinite(norms)) or np.any(norms <= 0): raise ValueError('All five coefficient constraint rows must be nonzero')
        self.constraint_row_scales = 1/norms
        bmat = self.constraint_row_scales[:, None]*g[:, 1:]
        u, s, vt = np.linalg.svd(bmat, full_matrices=True)
        if len(s) != NCON or not np.all(np.isfinite(s)) or np.any(s <= 0): raise ValueError('All five coefficient constraint singular values must be positive')
        rank_floor = max(bmat.shape)*np.finfo(float).eps*s[0]
        if s[-1] <= rank_floor: raise ValueError('Full five-constraint coefficient rank is unresolved')
        self.normal = np.zeros((NRAW, NCON)); self.normal[1:] = vt[:NCON].T@((u.T/s[:, None])*self.constraint_row_scales[None, :])
        full = self.constraint_row_scales[:, None]*g
        _, sf, vf = np.linalg.svd(full, full_matrices=True)
        if len(sf) != NCON or np.any(sf <= max(full.shape)*np.finfo(float).eps*sf[0]): raise ValueError('Full five-constraint physical rank is unresolved')
        self.free = vf[NCON:].T.copy()
        if self.free.shape != (NRAW, NFREE) or not np.array_equal(self.normal[0], np.zeros(NCON)): raise ValueError('C5 dimensions or coefficient-only policy changed')
        self.base_tangent = self.tangent(self.base)
        self.complete = np.column_stack((self.base_tangent, self.normal))
        if np.linalg.matrix_rank(self.complete) != NRAW or np.linalg.matrix_rank(self.base_tangent) != NFREE: raise ValueError('A physical parameter or feasible tangent direction was lost')
        if np.linalg.norm(self.base_tangent[0]) == 0: raise ValueError('cl must remain a free tangent direction')
        self.geometry_diagnostics = {'version': self.version, 'constraint_row_scales': self.constraint_row_scales.tolist(),
            'coefficient_row_scaled_singular_values': s.tolist(), 'coefficient_row_scaled_condition': float(s[0]/s[-1]),
            'full_row_scaled_constraint_singular_values': sf.tolist(),
            'raw_G_normal_minus_identity_norm': float(np.linalg.norm(g@self.normal-np.eye(NCON))),
            'tangent_constraint_error': float(np.linalg.norm(g@self.base_tangent)),
            'relative_tangent_backward_error': float(np.linalg.norm(g@self.base_tangent)/max(np.linalg.norm(g)*np.linalg.norm(self.base_tangent), 1e-300)),
            'tangent_rank': int(np.linalg.matrix_rank(self.base_tangent)), 'complete_rank': int(np.linalg.matrix_rank(self.complete)),
            'complete_condition': float(np.linalg.cond(self.complete)), 'cl_tangent_row_norm': float(np.linalg.norm(self.base_tangent[0])),
            'base_HP': hp_report(self.base), 'feasible_core_dimension': NFREE, 'raw_core_parameters': NRAW, 'constraints': NCON,
            'nonzero_constraint_columns': int(np.count_nonzero(np.linalg.norm(g, axis=0) > 0)),
            'unreduced_center_plus_C5_6x61_rank': int(np.linalg.matrix_rank(unreduced_constraint_jacobian(self.base))),
            'unreduced_center_plus_C5_6x61_singular_values': np.linalg.svd(unreduced_constraint_jacobian(self.base), compute_uv=False).tolist()}

    def _bounds(self, P):
        if P.shape != (NRAW,) or not np.all(np.isfinite(P)) or np.any(P < LOW) or np.any(P > HIGH): raise ValueError('Outside physical parameter bounds')

    def _verify(self, P):
        self._bounds(P); report = hp_report(P)
        if report['max_abs'] >= self.tolerance or report['poisson_max_abs'] >= self.tolerance or abs(report['a0']) <= 1e-12:
            raise ValueError('Analytic-center C5 point fails independent feasibility/nondegeneracy')
        return report

    def tangent(self, P):
        g = constraint_jacobian(P); a = g@self.normal
        if np.linalg.cond(a) > 1e10: raise ValueError('Analytic-center C5 normal system is unresolved')
        return self.free-self.normal@np.linalg.solve(a, g@self.free)

    def lift_delta(self, q, derivative=False):
        q = np.asarray(q, dtype=float)
        if q.shape != (NFREE,) or not np.all(np.isfinite(q)): raise ValueError('Expected all 55 finite core coordinates')
        if not np.any(q): return (self.base.copy(), self.base_tangent.copy()) if derivative else self.base.copy()
        seed = self.base+self.free@q; z = np.zeros(NCON); P = seed.copy(); self._bounds(P); history = []
        for it in range(24):
            hp = hp_report(P); c = np.asarray(hp['constraints']); size = float(np.linalg.norm(c))
            history.append({'iteration': it, 'constraint_norm': size, 'max_abs': hp['max_abs']})
            if hp['max_abs'] < self.target: break
            g = constraint_jacobian(P); a = g@self.normal
            if np.linalg.cond(a) > 1e10: raise ValueError('C5 correction lost numerical invertibility')
            dz = np.linalg.solve(a, -c)
            for alpha in (1., .5, .25, .125, .0625, .03125, .015625):
                zz = z+alpha*dz; trial = seed+self.normal@zz
                try: self._bounds(trial)
                except ValueError: continue
                if np.linalg.norm(hp_report(trial)['constraints']) < size: P, z = trial, zz; break
            else: raise ValueError('C5 correction cannot improve independent constraints')
        report = self._verify(P)
        if float(P[0]).hex() != float(seed[0]).hex(): raise ValueError('Coefficient-only corrector changed free cl')
        self.last_diagnostics = {'version': self.version, 'iterations': history, 'final': report}
        return (P, self.tangent(P)) if derivative else P
