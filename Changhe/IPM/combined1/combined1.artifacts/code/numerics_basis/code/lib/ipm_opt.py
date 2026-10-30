"""Constrained Gauss-Newton optimizer for S1/IPM candidates (lane c1-n1).

Basis: list of generator dicts {m, j (or p exact), spec ['mono',h] | ['leg',w,n]}; coefficients a (float).  Exactness is restored at the end by
pivoting (ipm_exact-compatible rational finalization in finalize_exact).
Linear constraints: center (sum s_i a_i = 1-c), fixed leading moments (Theta_0), prescribed branch moments, zero descendant moments.
Nonlinear constraints: the five Taylor equations (quadratic), treated by SQP linearization each step.
Objective: sum_i w_i R_f(X_i)^2 with w_i = mesh weight (ds dtheta) * omega_i, omega chosen by `objective`:
  'Jabs' : omega = 1/(pi a_ref^2)                       (training loss of case 4)
  'F2'   : omega = 4 r^4 sin^2 th                        (||F||_2^2 over R^2, F = y R_f, dX = r^2 ds dth, 4 quadrants)
  'E2low': omega = 4 r^4 sin^2 th (2^18 + 2^18 (20/21) r^2) (the two low-order E_2 components with ||F||_H replaced by its Hardy bound ||rF||_2)
  'FrF'  : omega = 4 r^4 sin^2 th (1 + r^2)
Nodes with r < r_cut are excluded from the objective (binary64 cancellation near the origin; the Taylor constraints control the origin).
"""
import math, json, time, hashlib, os
import numpy as np
import torch
from gmpy2 import mpq
import ipm_exact as X
import ipm_origin as O
import ipm_eval as EV

DT = torch.float64

# ------------------------------------------------------------------ basis specification
def t1_generators_860():
    """the 860 case4 generators in T1 form (coefficients then include N_n for the Legendre ones)"""
    gens = []
    for j in range(4):
        for m in range(5):
            for k in range(m, 5): gens.append({'m': m, 'j': j, 'spec': ['mono', k-m]})
    for j in range(4):
        for m in range(10):
            for n in range(26-max(5, m)): gens.append({'m': m, 'j': j, 'spec': ['leg', max(5-m, 0), n]})
    return gens

def case4_coefficients_t1(J, c_exact):
    """coefficients for t1_generators_860 from a case4 checkpoint JSON (exact a_000); returns float array and exact list"""
    P = [float.fromhex(h) for h in J['P_hex']]; high = [float.fromhex(h) for h in J['high_hex']]
    NN = [X.Q(float.fromhex(h)) for h in J['frozen_Nn_hex']]
    s = X.strain_values(c_exact)
    low = [X.Q(v) for v in P]
    low[0] = (1-c_exact-sum((s[k]*low[k] for k in range(1, 60)), mpq(0)))/s[0]
    ex = list(low)+[X.Q(v)*NN[n] for v, (m, n, j) in zip(high, X.HIGH)]
    return np.array([X.qfloat(v) for v in ex]), ex

def gen_p(g, c):
    return X.Q(g['p']) if 'p' in g else X.p_branch(c, int(g['j']))

def gens_to_terms_unit(gens, c):
    """for each generator, its canonical monomial expansion [(m,k,p,coef)] with unit coefficient (exact)"""
    out = []
    for g in gens:
        out.append(X.generators_to_terms(c, [dict(g, coef=1)]))
    return out

def moment_row(gterms, m, p, q):
    """exact q-th moment contribution of a (unit-coefficient) generator to block (m,p)"""
    tot = mpq(0)
    for t in gterms:
        if t['m'] == m and t['p'] == p: tot += X.term_moment(t, q)
    return tot

class Problem:
    def __init__(self, gens, c_exact, mesh, objective='Jabs', r_cut=0.02, r_max=None, device=None, fixed=()):
        """fixed: list of (gen dict, exact coef) with coefficients that are not optimized (fixed stationary tail)"""
        self.gens = gens; self.c = c_exact; self.cf = X.qfloat(c_exact); self.n = len(gens)
        self.fixed = list(fixed); self.fixed_coefs = np.array([X.qfloat(v) for _, v in self.fixed])
        self.mesh = mesh; self.device = mesh.device
        self.unit_terms = gens_to_terms_unit(gens, c_exact)
        # origin jets (exact) on the canonical terms of each generator: build per-generator Taylor data by summing its monomials
        self.origin = self._origin_jets()
        self.strain = np.array([X.qfloat(v) for v in self.strain_exact])
        # evaluator
        self.ev_gens = [EV.Generator(g['m'], X.qfloat(gen_p(g, c_exact)), tuple(g['spec'])) for g in gens]
        self.ev_fixed = [EV.Generator(g['m'], X.qfloat(gen_p(g, c_exact)), tuple(g['spec'])) for g, _ in self.fixed]
        self.basis = EV.Basis(self.ev_gens+self.ev_fixed, mesh, self.cf)
        self.set_objective(objective, r_cut, r_max)
        self.lin_rows = []   # list of (row vector np, rhs float, exact row (list mpq), exact rhs mpq, name)
    def _origin_jets(self):
        # OriginJets works on canonical terms with 'coef'; make a flat list and a map generator -> term indices
        flat = []; owner = []
        for i, gt in enumerate(self.unit_terms):
            for t in gt:
                if t.get('kind') == 'series':
                    # legqs inner functions vanish at the origin to order 2(m+w) >= 10: no Taylor data up to degree 8
                    assert 2*t['k_origin'] >= 10, 'legqs generator with origin order < 10 not supported in the Taylor chart'
                    continue
                flat.append(t); owner.append(i)
        OJ = O.OriginJets(flat, degmax=4, exact=True)
        self._OJ = OJ; self._owner = owner; self._flat = flat
        strains_flat = OJ.strains()
        se = [mpq(0)]*self.n
        for i, t, s in zip(owner, flat, strains_flat): se[i] += t['coef']*s
        self.strain_exact = se
        return OJ
    def _flat_coefs(self, a):
        return [X.Q(float(a[i]))*t['coef'] for i, t in zip(self._owner, self._flat)]
    def taylor_values(self, a):
        """the six R_f Taylor coefficients (center, x^2, y^2, x^4, x^2y^2, y^4) as floats, exact arithmetic on binary64 inputs"""
        vals = self._OJ.Rf_coeffs(self.c, self._flat_coefs(a))
        return np.array([X.qfloat(v) if isinstance(v, type(mpq(1))) else float(v) for v in vals])
    def taylor_jacobian(self, a):
        cols = self._OJ.Rf_coeffs_jacobian(self.c, self._flat_coefs(a))      # per flat term
        Jt = np.zeros((6, self.n))
        for i, t, col in zip(self._owner, self._flat, cols):
            cf = X.qfloat(t['coef'])
            for r in range(6):
                v = col[r]; Jt[r, i] += cf*(X.qfloat(v) if isinstance(v, type(mpq(1))) else float(v))
        return Jt
    def set_objective(self, objective, r_cut=0.02, r_max=None):
        """r_max: nodes with r > r_max get zero weight (the far field is accounted for exactly through the sectors)"""
        mesh = self.mesh; r = mesh.r[:, None]; sn = mesh.sin[None, :]
        if objective == 'Jabs': om = torch.full((mesh.Nr, mesh.Nt), 1/(math.pi*EV.A_REF**2), dtype=DT, device=self.device)
        elif objective == 'F2': om = 4*r**4*sn**2*torch.ones_like(mesh.W)
        elif objective == 'FrF': om = 4*r**4*sn**2*(1+r**2)*torch.ones_like(mesh.W)
        elif objective == 'E2low': om = 4*r**4*sn**2*(2.**18+2.**18*(20/21)*r**2)*torch.ones_like(mesh.W)
        else: raise ValueError(objective)
        om = om*(r >= r_cut)
        if r_max is not None: om = om*(r <= r_max)
        self.objective = objective; self.r_cut = r_cut; self.r_max = r_max
        self.w = (mesh.W*om).reshape(-1)
        self.sqrtw = torch.sqrt(self.w)
    # ------------------------------------------------------------ constraints
    def add_center(self):
        row = [self.strain_exact[i] for i in range(self.n)]
        self.lin_rows.append((np.array([X.qfloat(v) for v in row]), X.qfloat(1-self.c), row, 1-self.c, 'center'))
    def add_moment(self, m, p, q, target_exact, name):
        row = [moment_row(self.unit_terms[i], m, p, q) for i in range(self.n)]
        if all(v == 0 for v in row):
            if target_exact != 0: raise ValueError('no generator carries moment %s but target nonzero' % name)
            return False
        self.lin_rows.append((np.array([X.qfloat(v) for v in row]), X.qfloat(target_exact), row, X.Q(target_exact), name))
        return True
    def constraint_matrix(self):
        A = np.array([r[0] for r in self.lin_rows]); b = np.array([r[1] for r in self.lin_rows])
        return A, b
    # ------------------------------------------------------------ objective and GN
    def residual(self, a):
        at = torch.as_tensor(np.r_[np.asarray(a, float), self.fixed_coefs], dtype=DT, device=self.device)
        Rf, Fd = self.basis.residual_Rf(at)
        return Rf, Fd
    def objective_value(self, a):
        Rf, _ = self.residual(a)
        return float(torch.sum(self.w*Rf.reshape(-1)**2))
    def gn_step(self, a, lam, taylor=True, verbose=False):
        """one constrained GN/LM step from a; returns candidate a_new, predicted decrease"""
        Rf, Fd = self.residual(a)
        r = (self.sqrtw*Rf.reshape(-1))
        J = self.basis.jacobian_Rf(Fd)[:, :self.n]*self.sqrtw[:, None]
        # constraints: linear rows and linearized Taylor rows
        A, b = self.constraint_matrix() if self.lin_rows else (np.zeros((0, self.n)), np.zeros(0))
        d = b-A@a
        if taylor:
            tv = self.taylor_values(a)[1:]; Jt = self.taylor_jacobian(a)[1:]
            A = np.vstack([A, Jt]); d = np.r_[d, -tv]
        At = torch.as_tensor(A, dtype=DT, device=self.device); dt = torch.as_tensor(d, dtype=DT, device=self.device)
        # particular solution and null space via SVD of A
        U, S, Vh = torch.linalg.svd(At, full_matrices=True)
        rank = int((S > S.max()*1e-13).sum()) if len(S) else 0
        if rank < len(S) and verbose: print('  constraint rank', rank, 'of', len(S))
        Vr = Vh[:rank]; Z = Vh[rank:].T                      # (n, n-rank)
        dp = Vr.T@((U[:, :rank].T@dt)/S[:rank])              # min-norm particular solution
        JZ = J@Z; rhs = -(r+J@dp)
        # column scaling
        colnorm = torch.sqrt((JZ*JZ).sum(0)); colnorm[colnorm == 0] = 1
        JZs = JZ/colnorm
        G = JZs.T@JZs; g = JZs.T@rhs
        G += lam*torch.eye(G.shape[0], dtype=DT, device=self.device)
        try:
            L = torch.linalg.cholesky(G); eta = torch.cholesky_solve(g[:, None], L)[:, 0]
        except Exception:
            eta = torch.linalg.lstsq(G, g[:, None]).solution[:, 0]
        eta = eta/colnorm
        delta = dp+Z@eta
        pred = float((r*r).sum()-((r+J@delta)**2).sum())
        a_new = a+delta.cpu().numpy()
        return a_new, pred, float((r*r).sum())
    def taylor_project(self, a, iters=3, tol=1e-14):
        """Newton iterations restoring the five Taylor equations (and the linear rows) with a minimum-norm correction"""
        A, b = self.constraint_matrix() if self.lin_rows else (np.zeros((0, self.n)), np.zeros(0))
        for _ in range(iters):
            tv = self.taylor_values(a)[1:]
            if np.abs(tv).max() < tol and (len(b) == 0 or np.abs(b-A@a).max() < tol): break
            Jt = self.taylor_jacobian(a)[1:]
            C = np.vstack([A, Jt]); d = np.r_[b-A@a, -tv]
            delta = np.linalg.lstsq(C, d, rcond=None)[0]
            a = a+delta
        return a
    def optimize(self, a0, steps=20, lam0=1e-6, taylor=True, log=None, ckpt=None, verbose=True):
        a = np.array(a0, float); lam = lam0
        f0 = self.objective_value(a)
        hist = [(0, f0, lam)]
        for it in range(1, steps+1):
            t0 = time.time()
            a_new, pred, fcur = self.gn_step(a, lam, taylor=taylor, verbose=verbose)
            if taylor: a_new = self.taylor_project(a_new)
            fnew = self.objective_value(a_new)
            tv = self.taylor_values(a_new)
            if fnew < fcur:
                a = a_new; lam = max(lam/3, 1e-14); ok = True
            else:
                lam = lam*10; ok = False
            hist.append((it, fnew if ok else fcur, lam))
            msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} pred {pred:.3e} lam {lam:.1e} maxTaylor {np.abs(tv).max():.2e} ({time.time()-t0:.1f}s)'
            if verbose: print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
            if ckpt and ok: np.save(ckpt, a)
        return a, hist

# ------------------------------------------------------------------ exact finalization
def finalize_exact(prob, a, pivots=None):
    """Return exact rational coefficients: binary64 values for all generators except one pivot per linear constraint row,
    chosen (if not given) as the generator with the largest |row entry| among not-yet-used generators that do not appear in other rows
    with large entries; solves the pivot system exactly (gmpy2). Returns list of mpq and the pivot indices."""
    rows = prob.lin_rows; nrow = len(rows)
    a_q = [X.Q(float(v)) for v in a]
    if nrow == 0: return a_q, []
    A = np.array([r[0] for r in rows])
    if pivots is None:
        pivots = []; used = set()
        # greedy: process rows by number of nonzeros ascending
        order = sorted(range(nrow), key=lambda i: np.count_nonzero(A[i]))
        for i in order:
            cand = [j for j in np.argsort(-np.abs(A[i])) if A[i, j] != 0 and j not in used]
            if not cand: raise ValueError('no pivot for row %s' % rows[i][4])
            pivots.append((i, int(cand[0]))); used.add(int(cand[0]))
        pivots = [p for _, p in sorted(pivots)]
    # exact solve of the pivot system with flint fmpq_mat
    import flint
    piv = pivots
    pivset = set(piv); free = [j for j in range(prob.n) if j not in pivset]
    M = flint.fmpq_mat(nrow, nrow)
    for i in range(nrow):
        for jj, j in enumerate(piv):
            v = rows[i][2][j]
            if v != 0: M[i, jj] = flint.fmpq(int(v.numerator), int(v.denominator))
    rhs = flint.fmpq_mat(nrow, 1)
    for i in range(nrow):
        v = rows[i][3]-sum((rows[i][2][j]*a_q[j] for j in free if rows[i][2][j] != 0), mpq(0))
        rhs[i, 0] = flint.fmpq(int(v.numerator), int(v.denominator))
    sol = M.solve(rhs)
    out = list(a_q)
    for jj, j in enumerate(piv):
        v = sol[jj, 0]; out[j] = mpq(int(v.p), int(v.q))
    # verify
    for i in range(nrow):
        assert sum((rows[i][2][j]*out[j] for j in range(prob.n)), mpq(0)) == rows[i][3], 'exact constraint check failed: '+rows[i][4]
    return out, piv

def exact_terms(prob, a_exact):
    """canonical monomial terms (merged) for exact coefficients, fixed tail included"""
    gens = [dict(g, coef=v) for g, v in zip(prob.gens, a_exact)]+[dict(g, coef=v) for g, v in prob.fixed]
    return X.generators_to_terms(prob.c, gens)

def write_candidate_json(path, prob, a_exact, meta):
    out = {'format': 'c1-n1 generator list: chi = sum coef * H_m (1+r^2)^(p-m) T(t), T = t^h (mono) or t^w P_n(2t-1) (leg); p = (3+gamma-j lambda)/2 for branch j; coef exact rational',
           'cl_exact': X.qstr(prob.c), 'cl_float': prob.cf, 'generators': [], 'meta': meta}
    for g, v in list(zip(prob.gens, a_exact))+list(prob.fixed):
        d = {'m': int(g['m']), 'spec': list(g['spec']), 'coef': X.qstr(v), 'coef_float': X.qfloat(v)}
        if 'j' in g: d['j'] = int(g['j'])
        else: d['p'] = X.qstr(X.Q(g['p']))
        out['generators'].append(d)
    out['n_free'] = len(prob.gens); out['n_fixed'] = len(prob.fixed)
    json.dump(out, open(path, 'w'))
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()

def load_candidate_json(path):
    J = json.load(open(path))
    c = X.Q(J['cl_exact'])
    gens = []; coefs = []
    for g in J['generators']:
        d = {'m': g['m'], 'spec': g['spec']}
        if 'j' in g: d['j'] = g['j']
        else: d['p'] = g['p']
        gens.append(d); coefs.append(X.Q(g['coef']))
    return c, gens, coefs, J

def sector_report(c, terms, qmax=3, exp_min=None):
    gamma = 1/c
    if exp_min is None: exp_min = gamma-9*(1-gamma)-mpq(1, 100)
    E, dens, strm, moments = X.residual_sectors(c, terms, qmax, exp_min=exp_min)
    rows = []
    for ex in sorted(E.keys(), reverse=True):
        if ex < exp_min: continue
        S = E[ex]
        rows.append({'exponent_exact': X.qstr(ex), 'exponent': X.qfloat(ex), 'status': 'EXACT-ZERO' if not S else 'EXACT-NONZERO',
                     'max_harmonic': max(S) if S else 0, 'quarter_L2': X.quarter_norm(S), 'full_circle_L2': 2*X.quarter_norm(S),
                     'coefficients_float': {str(k): X.qfloat(v) for k, v in sorted(S.items())} if S and len(S) <= 400 else None})
    first = next((r for r in rows if r['status'] != 'EXACT-ZERO'), None)
    return {'cl_exact': X.qstr(c), 'qmax': qmax, 'rows': rows, 'first_nonzero': first, 'Theta0_float': X.to_float_dict(dens[gamma]) if gamma in dens else None,
            'Theta0_quarter_norm': X.quarter_norm(dens.get(gamma, {}))}
