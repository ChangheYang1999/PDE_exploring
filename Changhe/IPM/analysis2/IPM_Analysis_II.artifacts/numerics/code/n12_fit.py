"""N12: improved approximate solution rho_tilde = sum_i a_i rho[chi_i] with exact stationary far-field sectors, by constrained Gauss-Newton.

Unknowns: coefficients a of the generators chi_i = H_m R^{p_j - m} T_i(t) (old 860 in T1 form + new branch-j generators ('mono', k-m)).
Constraints (linear, exact): leading moments per (m, j): sum over generators of (m,j) of a_i * lead_i = target_{m,j}, where lead_i is the
 coefficient of t^0 ... careful: the leading far-field moment of a generator is its value at t = 1 (r -> infinity): T_i(1) (mono: 1; leg: P_n(1) = 1),
 so C_{m,j,0} = sum_i a_i T_i(1). Descendant (q = 1) moments: C_{m,j,1} = sum_k a_{mkj} (p_j - k) in monomial form; in T1 form the q=1 moment of
 R^{p_j-m} T(t) = sum_h c_h t^h R^{p_j - m}: t^h R^{beta} = R^{beta}(1 - u)^h -> the r^{-2} coefficient: beta*... we compute it generically as
 d/dz [ (1+z)^{beta} T(1/(1+z)) ] at z = 0 with t = 1/(1+z)... i.e. C_{m,j,1} = beta T(1) - T'(1)  (z = 1/q, R = q(1+z), t = 1/(1+z): R^beta T(t) =
 q^beta (1+z)^beta T((1+z)^-1); d/dz at 0: beta T(1) - T'(1)).  Center condition: sum_i a_i s_i = 1 - c_l with s_i = chi_i,xxyy(0) (nonzero only
 for m = 0: k in {0,1,2} and m = 2, k = 2 monomials; for Legendre T1 generators with t^w prefactor, w >= 1 for m <= 4 so s = 0; for m >= 5 s = 0).
Objective: J(a) = sum_pts wq [ |w_H r F|^2 + |omega_0 F|^2 + |omega_1 DF|^2 + |omega_2 D^2 F|^2 ] + beta_T sum (Taylor coefficients of F at degrees 3,5)^2,
 omega_k = <r>^(k-1-sigma), w_H = <r>^(-(2+sigma)).  F quadratic in a; GN step on the linearization.
"""
import math, sys, os, json, time
sys.set_int_max_str_digits(0)
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n12_eval import make_cache, generator_jet

ORDER = 5   # potential jets to order 5 -> F to order 2 (D^2 F needs rho to order 3 = potential 6? rho = 3 derivatives, D^2 rho = 5; U = 3, D^2 U = 5: order 5 suffices for D^2 F)
# F = V.grad rho - rho: D^2 F needs D^2 V (DU: order 4+... D^2 U = 5), D^3 rho = 6!  (D^2 (V.grad rho) includes V . D^3 rho) -> ORDER 6 for D^2 F.
ORDER = 6

def load_state(ckpt_json):
    ck = json.load(open(ckpt_json))
    cl_fr = Fr(ck['input_exact_for_checkpoint']['cl_exact']); cl = float(cl_fr); g = 1/cl
    p = [(3 + g - j*(1-g))/2 for j in range(8)]
    low = [float.fromhex(h) for h in ck['P_hex']]; num, den = ck['input_exact_for_checkpoint']['a000_exact'].split('/'); low[0] = int(num)/int(den)
    high = [float.fromhex(h) for h in ck['high_hex']]; NN = [float.fromhex(h) for h in ck['frozen_Nn_hex']]
    LOW = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]; HIGH = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]
    gens = []   # dict: m, j, beta, spec, coef, lead (T(1)), q1 (beta T(1) - T'(1)), strain s
    for c, (m, k, j) in zip(low, LOW):
        gens.append({'m': m, 'j': j, 'beta': p[j]-m, 'spec': ('mono', k-m), 'a': c, 'k': k, 'kind': 'old_low'})
    for c, (m, n, j) in zip(high, HIGH):
        gens.append({'m': m, 'j': j, 'beta': p[j]-m, 'spec': ('leg', max(5-m, 0), n), 'a': c*NN[n], 'kind': 'old_high'})
    return cl, cl_fr, p, gens

def T_at_1(spec):
    """T(1), T'(1) for the radial polynomial."""
    if spec[0] == 'mono': h = spec[1]; return 1.0, float(h)
    w, n = spec[1], spec[2]
    # T = t^w P_n(2t-1): T(1) = P_n(1) = 1; T'(1) = w P_n(1) + 2 P_n'(1) = w + n(n+1)
    return 1.0, float(w + n*(n+1))

def strain(gen, p):
    """chi_xxyy(0) for the generator (nonzero only for low monomials (0,0),(0,1),(0,2),(2,2))."""
    if gen['spec'][0] != 'mono': return 0.0
    m, k = gen['m'], gen['k'] if 'k' in gen else gen['m'] + gen['spec'][1]; pj = p[gen['j']]
    if (m, k) == (0, 0): return 4*pj*(pj-1)
    if (m, k) == (0, 1): return 8*(pj-1)
    if (m, k) == (0, 2): return 8.0
    if (m, k) == (2, 2): return -24.0
    return 0.0

def add_new_generators(gens, p, branches):
    """branches: dict j -> (M_j, spec) with spec an int kextra (monomials t^h, h = 0..kextra-1) or a string 'L<n>' (Legendre block
    t^0 P_n(2t-1), n = 0..<n>-1, as in the old high block for m >= 5) or 'B<kextra>+<n>' (both). New generators only for (m, j) not spanned by the old family."""
    for j, entries in branches.items():
      for (Mj, spec) in (entries if isinstance(entries, list) else [entries]):
        for m in range(Mj+1):
            sp = str(spec)
            if m <= 9 and j <= 3 and not (sp.startswith('X') or sp.startswith('F@')): continue      # (m,j) already spanned by the old family (low monomials + Legendre high block)
            specs = []
            if isinstance(spec, int): specs = [('mono', h) for h in range(spec)]
            else:
                if sp.startswith('L'): specs = [('leg', 0, n) for n in range(int(sp[1:]))]
                elif sp.startswith('B'):
                    kx, nn = sp[1:].split('+'); specs = [('mono', h) for h in range(int(kx))] + [('leg', 0, n) for n in range(int(nn))]
                elif sp.startswith('X'):
                    # far-field-only monomials t^h, h = h0..h0+n-1 (near-field footprint r^(2m+2h)), for ALL m <= Mj including m <= 9
                    h0, nn = sp[1:].split('+'); specs = [('mono', h) for h in range(int(h0), int(h0)+int(nn))]
                elif sp.startswith('F@'):
                    # all canonical triples (j', m', k) of a canonical coefficient file (e.g. the verifier's algebraic repairs) with j' == j, m' == m, as monomials t^(k-m)
                    import json as _json
                    rep = _json.load(open(sp[2:])); specs = [('mono', int(t[2]) - m) for t in rep['canonical_order'] if int(t[0]) == j and int(t[1]) == m]
            existing = {(g_['m'], g_['j'], tuple(g_['spec'])) for g_ in gens}
            for sp_ in specs:
                if (m, j, sp_) in existing: continue
                existing.add((m, j, sp_))
                gen = {'m': m, 'j': j, 'beta': p[j]-m, 'spec': sp_, 'a': 0.0, 'kind': 'new'}
                if sp_[0] == 'mono': gen['k'] = m + sp_[1]
                gens.append(gen)
    return gens

def density_rule_matrix(M, s):
    """Matrix A (rows: odd harmonics 1..2M+1, cols: m = 0..M) with sine coefficients of rho from potential r^s sum_m C_m cos(2m theta):
    cos(n) -> -C(s^2-n^2)(s-2-n)/2 at sin(n+1), +C(s^2-n^2)(s-2+n)/2 at sin(n-1)."""
    A = np.zeros((M+1, M+1))
    for m in range(M+1):
        n = 2*m
        A[m, m] += -(s*s - n*n)*(s-2-n)/2            # sin(2m+1) row index m
        if m >= 1: A[m-1, m] += (s*s - n*n)*(s-2+n)/2  # sin(2m-1) row index m-1
        else: A[0, 0] += -(s*s - n*n)*(s-2+n)/2       # m = 0: the sin(-theta) term folds into sin(theta) with a sign flip (farfield_exact.sadd)
    return A

def stationary_targets(formal_json, p, g, orders):
    """target moments C_{m,j,0} (float) for branch j = order-1 from the verifier's stationary density orders."""
    V = json.load(open(formal_json)); targets = {}
    for extra in os.environ.get('N12_EXTRA_ORDERS', '').split(','):      # extra stationary orders (e.g. order 7 from code/stationary_order.py), same format
        if extra: V['stationary_density_orders'].update(json.load(open(extra))['stationary_density_orders'])
    for n in orders:
        j = n - 1; coef = {int(k): float(Fr(v)) for k, v in V['stationary_density_orders'][str(n)]['coefficients'].items()}
        M = (max(coef) - 1)//2; s = 2*p[j]
        A = density_rule_matrix(M, s); rhs = np.array([coef.get(2*m+1, 0.0) for m in range(M+1)])
        C = np.linalg.solve(A, rhs)
        targets[j] = {m: C[m] for m in range(M+1)}
        # check
        print('branch %d target moments: M=%d, max|C|=%.3g, check residual %.2e' % (j, M, np.abs(C).max(), np.abs(A@C - rhs).max()))
    return targets

def grid(smin, smax, ns, nth):
    s = np.linspace(smin, smax, ns); ds = s[1]-s[0]
    th = (np.arange(nth)+0.5)/nth*math.pi/2; dth = math.pi/2/nth
    S, TH = np.meshgrid(s, th, indexing='ij'); r = np.exp(S)
    x = (r*np.cos(TH)).ravel(); y = (r*np.sin(TH)).ravel(); r = r.ravel()
    wq = (r*r*ds*dth*4)                     # dX = r dr dtheta = r^2 ds dtheta; 4 quadrants
    wq = wq.copy(); wq[:nth] *= 0.5; wq[-nth:] *= 0.5   # trapezoid in s
    return x, y, r, wq

def jets_of_sum(x, y, gens, cache, order, coef_key='a'):
    J = {}
    for gen in gens:
        c = gen[coef_key]
        if c == 0: continue
        gj = generator_jet(x, y, gen['m'], gen['beta'], gen['spec'], order, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + c*v
    return J

def F_jets(Jb, Jd, cl, x, y, K=2, linear_in_d=False):
    """Jets (i,j) for i+j <= K of F = (cl X + U).grad rho - rho from potential jets. If linear_in_d: the derivative L_b d = V_b.grad rho_d - rho_d + U_d.grad rho_b
    with background Jb and direction Jd (both potential jets); else full F for the single jet Jb (Jd ignored)."""
    def field(J, name, i, j):
        if name == 'rho': return -(J[(2+i, 1+j)] + J[(0+i, 3+j)])
        if name == 'U1': return -J[(1+i, 2+j)]
        if name == 'U2': return J[(2+i, 1+j)]
    def coord(which, i, j):
        if (i, j) == (0, 0): return x if which == 0 else y
        if (i, j) == ((1, 0) if which == 0 else (0, 1)): return np.ones_like(x)
        return 0.0
    out = {}
    for i in range(K+1):
        for j in range(K+1-i):
            acc = 0.0
            for g1 in range(i+1):
                for g2 in range(j+1):
                    cb = math.comb(i, g1)*math.comb(j, g2)
                    if linear_in_d:
                        V1 = cl*coord(0, g1, g2) + field(Jb, 'U1', g1, g2); V2 = cl*coord(1, g1, g2) + field(Jb, 'U2', g1, g2)
                        acc = acc + cb*(V1*field(Jd, 'rho', 1+i-g1, j-g2) + V2*field(Jd, 'rho', i-g1, 1+j-g2))
                        acc = acc + cb*(field(Jd, 'U1', g1, g2)*field(Jb, 'rho', 1+i-g1, j-g2) + field(Jd, 'U2', g1, g2)*field(Jb, 'rho', i-g1, 1+j-g2))
                    else:
                        V1 = cl*coord(0, g1, g2) + field(Jb, 'U1', g1, g2); V2 = cl*coord(1, g1, g2) + field(Jb, 'U2', g1, g2)
                        acc = acc + cb*(V1*field(Jb, 'rho', 1+i-g1, j-g2) + V2*field(Jb, 'rho', i-g1, 1+j-g2))
            acc = acc - field(Jd if linear_in_d else Jb, 'rho', i, j)
            out[(i, j)] = acc
    return out

def norms_table(FJ, r, wq, sigmas):
    """S14 norms: ||r w F||, ||omega_k D^k F|| for k = 0,1,2 with omega_k = <r>^(k-1-sigma), w = <r>^-(2+sigma)."""
    br = np.sqrt(1 + r*r); out = {}
    D1 = FJ[(1, 0)]**2 + FJ[(0, 1)]**2; D2 = FJ[(2, 0)]**2 + 2*FJ[(1, 1)]**2 + FJ[(0, 2)]**2
    for sg in sigmas:
        out[sg] = {'rwF': math.sqrt(np.sum(wq*(r*br**(-(2+sg))*FJ[(0, 0)])**2)), 'w0F': math.sqrt(np.sum(wq*(br**(-1-sg))**2*FJ[(0, 0)]**2)),
                   'w1DF': math.sqrt(np.sum(wq*(br**(-sg))**2*D1)), 'w2D2F': math.sqrt(np.sum(wq*(br**(1-sg))**2*D2))}
    return out

if __name__ == '__main__':
    ckpt, formal = sys.argv[1], sys.argv[2]
    cl, cl_fr, p, gens = load_state(ckpt); g = 1/cl
    print('c_l = %.16g, gamma = %.16g; old generators %d' % (cl, g, len(gens)))
    x, y, r, wq = grid(math.log(1e-3), math.log(1e4), 60, 12)      # small test grid
    t0 = time.time(); cache = make_cache(x, y, ORDER); print('cache %.1fs' % (time.time()-t0))
    t0 = time.time(); Jb = jets_of_sum(x, y, gens, cache, ORDER); print('background jets at %d points: %.1fs' % (len(x), time.time()-t0))
    FJ = F_jets(Jb, None, cl, x, y, K=2)
    tab = norms_table(FJ, r, wq, [0.3])
    print('checkpoint norms (sigma=0.3, truncated grid r<=1e4): rwF %.4g w0F %.4g w1DF %.4g w2D2F %.4g' % (tab[0.3]['rwF'], tab[0.3]['w0F'], tab[0.3]['w1DF'], tab[0.3]['w2D2F']))
    # spot check F against arb at 3 points
    from ipm_arb import State
    S = State(sys.argv[3], prec=128)
    for i in (5, 300, 700):
        f = S.fields(x[i], y[i], 5)
        print('  F float %.10e arb %s at r=%.3g' % (FJ[(0, 0)][i], f['F'].str(10), r[i]))
    targets = stationary_targets(formal, p, g, orders=[2, 3, 4])
