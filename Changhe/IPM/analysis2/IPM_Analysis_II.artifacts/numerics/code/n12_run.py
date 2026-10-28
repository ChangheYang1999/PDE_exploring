"""N12 milestone driver: constrained Gauss-Newton for rho_tilde with exact stationary far-field sectors (state 131).
Usage: n12_run.py ckpt.json formal_tail.json out_prefix ns nth sigma branches_spec iters
 branches_spec: e.g. "1:19:4" (branch 1 up to m=19, 4 radial functions per new (m,j)); several separated by commas.
Constraints: (L1) branch-0 leading moments frozen; (L2) leading moments of constrained branches = stationary targets; (L4) center condition.
Taylor rows: degree-3 and degree-5 Taylor coefficients of F at 0 (from float Taylor polynomials of the generators), weight beta_T.
"""
import math, sys, os, json, time
sys.set_int_max_str_digits(0)
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n12_eval import make_cache, generator_jet
from n12_fit import load_state, T_at_1, strain, add_new_generators, stationary_targets, grid, F_jets, norms_table, ORDER

# ---------- Taylor polynomials at the origin (float) of each generator's potential, to degree DEG ----------
def gen_taylor(gen, DEG=10):
    """phi_i Taylor coefficients {(a,b): float} for chi = H_m R^beta T(t), t = q/(1+q): expand T(t) R^beta = sum_h c_h q^h (1+q)^(beta-h) as a power series in q."""
    m, beta, spec = gen['m'], gen['beta'], gen['spec']
    # T(t) as a polynomial in t: coefficients c_h
    if spec[0] == 'mono': ct = {spec[1]: 1.0}
    else:
        w, n = spec[1], spec[2]
        # P_n(2t-1) = sum_h (-1)^(n-h) C(n,h) C(n+h,h) t^h
        ct = {w+h: (-1)**(n-h)*math.comb(n, h)*math.comb(n+h, h) for h in range(n+1)}
    nmax = (DEG - 2*m)//2
    if nmax < 0: return {}
    rad = np.zeros(nmax+1)
    for h, c in ct.items():
        # q^h (1+q)^(beta-h) = sum_l C(beta-h, l) q^(h+l)
        b = beta - h; coef = 1.0
        for l in range(0, nmax+1-h):
            if l > 0: coef *= (b - l + 1)/l
            rad[h+l] += c*coef
    poly = {}
    for l in range(m+1):
        ang = (-1)**l*math.comb(2*m, 2*l)       # H_m = sum_l (-1)^l C(2m,2l) x^(2m-2l) y^(2l)
        for nq, c in enumerate(rad):
            if c == 0: continue
            for i in range(nq+1):               # q^nq = sum_i C(nq,i) x^(2i) y^(2(nq-i))
                key = (2*m-2*l+2*i, 2*l+2*(nq-i))
                if sum(key) <= DEG: poly[key] = poly.get(key, 0.0) + ang*c*math.comb(nq, i)
    return poly

def pdx(P): return {(a-1, b): a*v for (a, b), v in P.items() if a > 0}
def pdy(P): return {(a, b-1): b*v for (a, b), v in P.items() if b > 0}
def padd(*Ps):
    out = {}
    for P in Ps:
        for k, v in P.items(): out[k] = out.get(k, 0.0) + v
    return out
def pscale(P, c): return {k: c*v for k, v in P.items()}
def pmul(P, Q, deg):
    out = {}
    for (a, b), u in P.items():
        for (c, d), v in Q.items():
            if a+b+c+d <= deg: out[(a+c, b+d)] = out.get((a+c, b+d), 0.0) + u*v
    return out

def fields_taylor(phi):
    psi = pdy(pdx(phi)); lap = padd(pdx(pdx(phi)), pdy(pdy(phi))); rho = pscale(pdy(lap), -1)
    return {'rho': rho, 'rho_x': pdx(rho), 'rho_y': pdy(rho), 'U1': pscale(pdy(psi), -1), 'U2': pdx(psi)}

TAYLOR_KEYS = [(2, 1), (0, 3), (4, 1), (2, 3), (0, 5)]
def F_taylor_coeffs(FT_b, FT_d, cl, linear=False):
    """Taylor coefficients (keys TAYLOR_KEYS) of F (or of L_b d if linear) from the field Taylor dicts; degree <= 5 needed."""
    X = {(1, 0): 1.0}; Y = {(0, 1): 1.0}
    if linear:
        V1 = padd(pscale(X, cl), FT_b['U1']); V2 = padd(pscale(Y, cl), FT_b['U2'])
        F = padd(pmul(V1, FT_d['rho_x'], 5), pmul(V2, FT_d['rho_y'], 5), pmul(FT_d['U1'], FT_b['rho_x'], 5), pmul(FT_d['U2'], FT_b['rho_y'], 5), pscale(FT_d['rho'], -1))
    else:
        V1 = padd(pscale(X, cl), FT_b['U1']); V2 = padd(pscale(Y, cl), FT_b['U2'])
        F = padd(pmul(V1, FT_b['rho_x'], 5), pmul(V2, FT_b['rho_y'], 5), pscale(FT_b['rho'], -1))
    return np.array([F.get(k, 0.0) for k in TAYLOR_KEYS])

def sum_taylor(gens, coefs):
    tot = {}
    for gen, c in zip(gens, coefs):
        if c == 0: continue
        for k, v in gen['taylor'].items(): tot[k] = tot.get(k, 0.0) + c*v
    return tot

if __name__ == '__main__':
    ckpt, formal, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
    ns, nth, sigma = int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    branches = {}
    for item in sys.argv[7].split(','):
        if not item or item == 'none': continue
        j, Mj, kx = item.split(':', 2); branches.setdefault(int(j), []).append((int(Mj), int(kx) if kx.isdigit() else kx))
    iters = int(sys.argv[8]); beta_T = float(sys.argv[9]) if len(sys.argv) > 9 else 1e3
    cl, cl_fr, p, gens = load_state(ckpt); g = 1/cl
    gens = add_new_generators(gens, p, branches)
    for gen in gens: gen['taylor'] = gen_taylor(gen, 10)
    N = len(gens); print('generators: %d (old 860 + %d new)' % (N, N-860), flush=True)
    a = np.array([gen['a'] for gen in gens])
    # ---- constraints C a = b
    rows = []; rhs = []
    lead = np.array([T_at_1(gen['spec'])[0] for gen in gens])
    # L1: branch 0 moments frozen (m <= 9)
    for m in range(10):
        row = np.array([lead[i] if (gens[i]['m'] == m and gens[i]['j'] == 0) else 0.0 for i in range(N)]); rows.append(row); rhs.append(row @ a)
    # L2: stationary targets for constrained branches
    targets = stationary_targets(formal, p, g, orders=[j+1 for j in branches]) if branches else {}
    for j, entries in branches.items():
        Mj = max(e[0] for e in entries)
        for m in range(Mj+1):
            row = np.array([lead[i] if (gens[i]['m'] == m and gens[i]['j'] == j) else 0.0 for i in range(N)]); rows.append(row); rhs.append(targets[j][m])
    # L3: descendant moments D_(j,m) = sum_i a_i (beta_i T_i(1) - T_i'(1)) = 0 for the branches listed in argv[14] (e.g. '0,1'); exact in T1 coordinates
    DESC = [int(v) for v in sys.argv[14].split(',')] if len(sys.argv) > 14 and sys.argv[14] not in ('', 'none') else []
    if DESC:
        q1 = np.array([gens[i]['beta']*T_at_1(gens[i]['spec'])[0] - T_at_1(gens[i]['spec'])[1] for i in range(N)])
        for j in DESC:
            for m in sorted(set(gen['m'] for gen in gens if gen['j'] == j)):
                row = np.array([q1[i] if (gens[i]['m'] == m and gens[i]['j'] == j) else 0.0 for i in range(N)]); rows.append(row); rhs.append(0.0)
        print('descendant constraints for branches', DESC, flush=True)
    # L4: center
    srow = np.array([strain(gen, p) for gen in gens]); rows.append(srow); rhs.append(1 - cl)
    C = np.array(rows); b = np.array(rhs)
    print('constraints: %d; current violation max |C a - b| = %.3e (branch-1 targets change the state)' % (len(rows), np.abs(C@a - b).max()), flush=True)
    # particular solution: minimal-norm correction a0 = a + C^T (C C^T)^-1 (b - C a); nullspace basis Nmat
    U_, S_, Vt = np.linalg.svd(C, full_matrices=True)
    rank = int((S_ > 1e-12*S_[0]).sum()); Nmat = Vt[rank:].T
    if rank < C.shape[0]:
        dep = []; cur_rank = 0
        for i in range(C.shape[0]):
            rk = np.linalg.matrix_rank(C[:i+1], tol=1e-10)
            if rk == cur_rank: dep.append(i)
            cur_rank = rk
        print('WARNING: %d dependent constraint rows (indices %s); the projection is least-squares, check consistency: residual of C a0 = b below' % (len(dep), dep[:20]), flush=True)
    a0 = a + np.linalg.lstsq(C, b - C@a, rcond=None)[0]
    print('rank %d, free directions %d; initial correction norm %.3e; constraint residual after projection %.2e' % (rank, Nmat.shape[1], np.linalg.norm(a0 - a), np.abs(C@a0 - b).max()), flush=True)
    # ---- grid, cache, generator jets (all generators, all points) stored as needed: we store the field jets needed for L_a d: rho (orders<=3), U (orders<=2) -> potential jets to order 6
    RMIN = float(os.environ.get("N12_RMIN", "1e-3")); RMAX = float(os.environ.get("N12_RMAX", "1e4"))   # fit grid radii (env override; default as before)
    x, y, r, wq = grid(math.log(RMIN), math.log(RMAX), ns, nth); P = len(x); print("fit grid: %d radii x %d angles on [%g, %g]" % (ns, nth, RMIN, RMAX), flush=True)
    NF = float(sys.argv[12]) if len(sys.argv) > 12 else 1.0      # near-field protection: multiply the quadrature weights by NF for r < 5
    LREG = float(sys.argv[13]) if len(sys.argv) > 13 else 0.0     # Tikhonov weight: rows sqrt(LREG) * (a_i - a_ck,i) * scale_i (scale_i = 1 for old T1 coordinates, 1 for new)
    a_ck_vec = np.array([gen['a'] for gen in gens])
    if NF != 1.0: wq = wq*np.where(r < 5.0, NF, 1.0); print('near-field weight boost %g for r < 5' % NF, flush=True)
    D4TAU = float(os.environ.get('N12_D4TAU', '0')); D4BETA = float(os.environ.get('N12_D4BETA', '0'))
    if D4BETA > 0: ORDER = 7; print('fourth-derivative penalty: rows sqrt(beta wq) (<r>^2 |D^4 rho|_F - tau)_+ with tau = %g, beta = %g (potential jets to order 7)' % (D4TAU, D4BETA), flush=True)
    cache = make_cache(x, y, ORDER)
    t0 = time.time()
    GJ = []        # per generator: dict (a,b)->array (28 arrays of P) ... memory: N*28*P*8 bytes
    for gen in gens: GJ.append(generator_jet(x, y, gen['m'], gen['beta'], gen['spec'], ORDER, cache))
    print('generator jets: %d x %d points, %.0f s, memory %.2f GB' % (N, P, time.time()-t0, N*28*P*8/1e9), flush=True)
    br = np.sqrt(1 + r*r); sq = np.sqrt(wq)
    wts = {'rw': sq*r*br**(-(2+sigma)), 'w0': sq*br**(-1-sigma), 'w1': sq*br**(-sigma), 'w2': sq*br**(1-sigma)}
    def rows_from_FJ(FJ):
        return np.concatenate([wts['rw']*FJ[(0, 0)], wts['w0']*FJ[(0, 0)], wts['w1']*FJ[(1, 0)], wts['w1']*FJ[(0, 1)], wts['w2']*FJ[(2, 0)], wts['w2']*math.sqrt(2)*FJ[(1, 1)], wts['w2']*FJ[(0, 2)]])
    def total_jets(coefs):
        J = {}
        for gj, c in zip(GJ, coefs):
            if c == 0: continue
            for k, v in gj.items(): J[k] = J.get(k, 0) + c*v
        return J
    # ---- soft descendant penalty: rows sqrt(beta_D) D_(j,m)(a) for the branches in N12_DPEN = "j1,j2:beta" (linear, constant Jacobian); shrinks the q = 1 residual sectors of those branches
    DPEN = os.environ.get('N12_DPEN', '')
    Drows = np.zeros((0, N))
    if DPEN:
        jl, bd = DPEN.split(':'); jl = [int(v) for v in jl.split(',')]; bd = float(bd)
        q1v = np.array([gens[i]['beta']*T_at_1(gens[i]['spec'])[0] - T_at_1(gens[i]['spec'])[1] for i in range(N)])
        rr = []
        for j in jl:
            for m in sorted(set(gen['m'] for gen in gens if gen['j'] == j)):
                rr.append(np.array([q1v[i] if (gens[i]['m'] == m and gens[i]['j'] == j) else 0.0 for i in range(N)]))
        Drows = math.sqrt(bd)*np.array(rr); print('soft descendant penalty: branches %s, weight %g, %d rows' % (jl, bd, len(rr)), flush=True)
    # ---- energy-matrix penalty (SPEC S9): rows sqrt(beta_M wq) (tau - lambda_min(M(X)))_+ on the fit grid; M = (2cl+1) I + sym(DU) + [[rho_y, -rho_x/2], [-rho_x/2, 0]]
    MTAU = float(os.environ.get('N12_MTAU', '0')); MBETA = float(os.environ.get('N12_MBETA', '0'))
    if MBETA > 0: print('energy-matrix penalty: tau = %g, beta_M = %g (rows on all %d grid points, active where lambda_min < tau)' % (MTAU, MBETA, P), flush=True)
    def M_entries(J):
        rho_x = -(J[(3, 1)] + J[(1, 3)]); rho_y = -(J[(2, 2)] + J[(0, 4)])
        DU11 = -J[(2, 2)]; DU12 = -J[(1, 3)]; DU21 = J[(3, 1)]; DU22 = J[(2, 2)]
        return DU11 + rho_y, 0.5*(DU12 + DU21) - 0.5*rho_x, DU22          # (M11 - (2cl+1), M12, M22 - (2cl+1))
    D4MULT = [1.0, 4.0, 6.0, 4.0, 1.0]
    def D4_parts(J): return [-(J[(2+i, 5-i)] + J[(i, 7-i)]) for i in range(5)]      # d_x^i d_y^(4-i) rho
    def D4_penalty(Jb):
        if D4BETA <= 0: return np.zeros(0), None
        T = D4_parts(Jb); nF = np.sqrt(sum(mlt*t*t for mlt, t in zip(D4MULT, T))); v = (1 + r*r)*nF
        active = v > D4TAU
        return np.sqrt(D4BETA*wq)*np.where(active, v - D4TAU, 0.0), (active, T, nF)
    def D4_penalty_jac(Jd, info):
        active, T, nF = info; dT = D4_parts(Jd)
        dv = (1 + r*r)*sum(mlt*t*dt for mlt, t, dt in zip(D4MULT, T, dT))/np.where(nF > 0, nF, 1.0)
        return np.sqrt(D4BETA*wq)*np.where(active, dv, 0.0)
    def M_penalty(Jb):
        if MBETA <= 0: return np.zeros(0), None
        a11, a12, a22 = M_entries(Jb); m11 = (2*cl+1) + a11; m22 = (2*cl+1) + a22
        disc = np.sqrt(0.25*(m11 - m22)**2 + a12**2); lam = 0.5*(m11 + m22) - disc
        # eigenvector of lambda_min: (M - lam I) v = 0 -> v = (a12, lam - m11) normalized (or (lam - m22, a12))
        v1 = np.where(np.abs(a12) > 1e-300, a12, lam - m22); v2 = np.where(np.abs(a12) > 1e-300, lam - m11, a12)
        nv = np.sqrt(v1*v1 + v2*v2); nv = np.where(nv > 0, nv, 1.0); v1 = v1/nv; v2 = v2/nv
        active = lam < MTAU
        rows = np.sqrt(MBETA*wq)*np.where(active, MTAU - lam, 0.0)
        return rows, (active, v1, v2, lam)
    def M_penalty_jac(Jd, info):
        active, v1, v2, lam = info
        d11, d12, d22 = M_entries(Jd)
        dlam = v1*v1*d11 + 2*v1*v2*d12 + v2*v2*d22
        return -np.sqrt(MBETA*wq)*np.where(active, dlam, 0.0)
    def objective(coefs):  # (minfo attribute set below)
        Jb = total_jets(coefs); FJ = F_jets(Jb, None, cl, x, y, K=2)
        FT = fields_taylor(sum_taylor(gens, coefs)); tay = F_taylor_coeffs(FT, None, cl)
        mrows, minfo = M_penalty(Jb); d4rows, d4info = D4_penalty(Jb)
        res = np.concatenate([rows_from_FJ(FJ), math.sqrt(beta_T)*tay, math.sqrt(LREG)*(coefs - a_ck_vec), Drows @ coefs, mrows, d4rows])
        objective.minfo = minfo; objective.d4info = d4info
        return res, FJ, tay, Jb
    if LREG: print('Tikhonov weight %g toward the checkpoint coefficients' % LREG, flush=True)
    res0, FJ0, tay0, Jb0 = objective(a)
    tab0 = norms_table(FJ0, r, wq, [sigma])[sigma]
    print('checkpoint: objective %.4e ; norms rwF %.4g w0F %.4g w1DF %.4g w2D2F %.4g ; Taylor %s' % (res0@res0, tab0['rwF'], tab0['w0F'], tab0['w1DF'], tab0['w2D2F'], np.array2string(tay0, precision=2)), flush=True)
    cur = a0.copy(); MU = float(sys.argv[10]) if len(sys.argv) > 10 else 1.0
    if len(sys.argv) > 11 and sys.argv[11] != 'none':
        if sys.argv[11].endswith('.json'):
            prev = json.load(open(sys.argv[11]))
            if 'canonical_order' in prev:
                # verifier's algebraic repair: canonical (j, m, k) triples with coefficients -> my ('mono', k - m) generators in branch j (canonical coefficient of r^(2k)(1+r^2)^(p_j-k) cos 2m theta
                # equals the coefficient of H_m R^(p_j-m) t^(k-m)); generators not in my list are reported
                pmap = {}; missing = 0
                for trip, c in zip(prev['canonical_order'], prev['canonical_coefficients']):
                    jj, mm, kk = int(trip[0]), int(trip[1]), int(trip[2]); key = (mm, jj, ('mono', kk - mm))
                    pmap[key] = pmap.get(key, 0.0) + float(Fr(c)) if isinstance(c, str) else pmap.get(key, 0.0) + float(c)
                have = {(gen['m'], gen['j'], tuple(gen['spec'])) for gen in gens}
                missing = sum(1 for key in pmap if key not in have)
                print('canonical repair init: %d triples, %d not representable in the current generator list (their coefficients are dropped: add the matching mono specs)' % (len(pmap), missing), flush=True)
            else:
                pmap = {(g_['m'], g_['j'], tuple(g_['spec'])): c for g_, c in zip(prev['gens'], prev['coefs'])}
            init = np.array([pmap.get((gen['m'], gen['j'], tuple(gen['spec'])), 0.0) for gen in gens]); nm = sum(1 for gen in gens if (gen['m'], gen['j'], tuple(gen['spec'])) in pmap)
            init = init + np.linalg.lstsq(C, b - C@init, rcond=None)[0]
            cur = init.copy(); print('initial coefficients mapped from', sys.argv[11], '(%d of %d generators matched), projected; constraint viol %.1e' % (nm, N, np.abs(C@cur - b).max()), flush=True)
        else:
            init = np.load(sys.argv[11])
            if len(init) == N: cur = init.copy(); print('initial coefficients loaded from', sys.argv[11], 'constraint viol %.1e' % np.abs(C@cur - b).max(), flush=True)
            else: print('init file has wrong length; ignored', flush=True)
    for it in range(iters):
        res, FJ, tay, Jb = objective(cur)
        tab = norms_table(FJ, r, wq, [sigma])[sigma]
        nd4 = P if D4BETA > 0 else 0
        mi = objective.minfo; mtxt = (' ; min lambda_min(M) %.4f (%d active, penalty %.3e)' % (mi[3].min(), int(mi[0].sum()), float(res[len(res)-nd4-P:len(res)-nd4]@res[len(res)-nd4-P:len(res)-nd4]))) if (MBETA > 0 and mi is not None) else ''
        if D4BETA > 0 and objective.d4info is not None:
            a4, T4, n4 = objective.d4info; v4 = (1 + r*r)*n4; mtxt += ' ; max <r>^2|D4rho| %.2f (%d active, penalty %.3e)' % (v4.max(), int(a4.sum()), float(res[-P:]@res[-P:]))
        if DPEN: dv = Drows @ cur; mtxt += ' ; desc penalty %.3e (max |D| %.3e)' % (float(dv@dv), float(np.abs(dv).max())/math.sqrt(bd))
        print('iter %d: objective %.4e ; rwF %.4g w0F %.4g w1DF %.4g w2D2F %.4g ; Taylor max %.2e ; constraint viol %.1e%s' % (it, res@res, tab['rwF'], tab['w0F'], tab['w1DF'], tab['w2D2F'], np.abs(tay).max(), np.abs(C@cur - b).max(), mtxt), flush=True)
        # Jacobian wrt a: column i = rows of L_cur chi_i (linear in d) + Taylor rows
        t0 = time.time()
        Jac = np.empty((len(res), N))
        FTb = fields_taylor(sum_taylor(gens, cur))
        for i, gen in enumerate(gens):
            LJ = F_jets(Jb, GJ[i], cl, x, y, K=2, linear_in_d=True)
            FTd = fields_taylor(gen['taylor'])
            ei = np.zeros(N); ei[i] = math.sqrt(LREG)
            Jac[:, i] = np.concatenate([rows_from_FJ(LJ), math.sqrt(beta_T)*F_taylor_coeffs(FTb, FTd, cl, linear=True), ei, Drows[:, i], M_penalty_jac(GJ[i], objective.minfo) if MBETA > 0 else np.zeros(0), D4_penalty_jac(GJ[i], objective.d4info) if D4BETA > 0 else np.zeros(0)])
        JN = Jac @ Nmat
        print('   Jacobian %s built in %.0f s' % (Jac.shape, time.time()-t0), flush=True)
        t0 = time.time()
        # Levenberg-Marquardt with column scaling: min ||JN dz + res||^2 + mu^2 ||S dz||^2, S = column norms; mu adapted by the gain ratio
        colnorm = np.linalg.norm(JN, axis=0); colnorm[colnorm == 0] = 1.0
        JNs = JN/colnorm
        Us, Ss, Vts = np.linalg.svd(JNs, full_matrices=False)
        Utr = Us.T @ (-res)
        best = None
        for mu in [MU*2.0**k for k in range(0, 12)]:
            dzs = Vts.T @ (Ss*Utr/(Ss*Ss + mu*mu))
            step = Nmat @ (dzs/colnorm)
            trial = cur + step; rt, *_ = objective(trial)
            pred = res@res - np.linalg.norm(JN @ (dzs/colnorm) + res)**2
            gain = (res@res - rt@rt)/max(pred, 1e-300)
            print('      mu %.3g: step %.3e, objective %.4e (gain %.2f)' % (mu, np.linalg.norm(step), rt@rt, gain), flush=True)
            if rt@rt < res@res and (best is None or rt@rt < best[0]): best = (rt@rt, step, mu)
            if best is not None and rt@rt > best[0]: break
        if best is None: print('   no decrease found; stopping'); break
        cur = cur + best[1]; MU = max(best[2]/4, 1e-6)
        print('   accepted mu %.3g, step norm %.3e, solve %.0f s' % (best[2], np.linalg.norm(best[1]), time.time()-t0), flush=True)
        np.save(prefix + '_coefs_iter%d.npy' % it, cur)
        json.dump({'gens': [{k: (list(v) if isinstance(v, tuple) else v) for k, v in gen.items() if k != 'taylor'} for gen in gens], 'coefs': cur.tolist(), 'cl': str(cl_fr), 'formal_tail': formal, 'constraints_rows': C.tolist(), 'constraints_rhs': b.tolist(), 'sigma': sigma, 'grid': [ns, nth], 'branches': {str(k): [list(e) for e in v] for k, v in branches.items()}, 'iter': it}, open(prefix + '_result.json', 'w'))
    res, FJ, tay, Jb = objective(cur); tab = norms_table(FJ, r, wq, [sigma])[sigma]
    if D4BETA > 0: a4, T4, n4 = objective.d4info; print('FINAL max <r>^2 |D4 rho| on the fit grid: %.4f at r = %.4g theta = %.3f ; active %d' % (((1 + r*r)*n4).max(), r[np.argmax((1 + r*r)*n4)], math.atan2(y[np.argmax((1 + r*r)*n4)], x[np.argmax((1 + r*r)*n4)]), int(a4.sum())), flush=True)
    if MBETA > 0: print('FINAL min lambda_min(M) on the fit grid: %.5f at r = %.4g theta = %.3f ; active %d' % (objective.minfo[3].min(), r[np.argmin(objective.minfo[3])], math.atan2(y[np.argmin(objective.minfo[3])], x[np.argmin(objective.minfo[3])]), int(objective.minfo[0].sum())), flush=True)
    print('FINAL: objective %.4e ; rwF %.4g w0F %.4g w1DF %.4g w2D2F %.4g ; Taylor %s ; max|a_new| %.3g ; max |da_old| %.3g' % (res@res, tab['rwF'], tab['w0F'], tab['w1DF'], tab['w2D2F'], np.array2string(tay, precision=2), np.abs(cur[860:]).max() if N > 860 else 0, np.abs(cur[:860] - a[:860]).max()), flush=True)
    json.dump({'gens': [{k: (list(v) if isinstance(v, tuple) else v) for k, v in gen.items() if k != 'taylor'} for gen in gens], 'coefs': cur.tolist(), 'cl': str(cl_fr), 'constraints_rows': C.tolist(), 'constraints_rhs': b.tolist(), 'sigma': sigma, 'grid': [ns, nth], 'branches': {str(k): [list(e) for e in v] for k, v in branches.items()}}, open(prefix + '_result.json', 'w'))
    print('saved', prefix + '_result.json', flush=True)
