"""N12 exact finalization: take a float result (gens + coefficients), make the coefficients exact rationals, re-impose the linear constraints
exactly through pivot coefficients, and compute the exact far-field residual sectors of the new potential (generalized sector code) to certify
which E_{h,q} vanish. Also writes the exact coefficient file (generator list with rational coefficients) and an evaluator-ready JSON.
Generators: chi = H_m R^(p_j - m) T(t); T = t^h ('mono') or t^w P_n(2t-1) ('leg', with the N_n folded into the coefficient).
Far field: R^(p_j-m) T(t) = q^(p_j - m) (1+z)^(p_j-m) T(1/(1+z)), z = 1/q; expand in z exactly: T(1/(1+z)) with t^h = (1+z)^-h -> R^(p_j-m) T = q^(p_j-m) sum_h c_h (1+z)^(p_j - m - h),
so the potential sector (j, qq) coefficient for cos(2m theta): C_{m,j,qq} = sum_h c_h binom(p_j - m - h, qq) (times the generator coefficient); exponent s = 2(p_j - m) - 2 qq + 2m = 2 p_j - 2 qq.
"""
import sys, os, json, math
sys.set_int_max_str_digits(0)
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import farfield_exact as FE

def binom_fr(p, q):
    out = Fr(1)
    for i in range(q): out = out*(p-i)/(i+1)
    return out

def T_coeffs(spec):
    """exact monomial coefficients {h: c_h} of T(t)."""
    if spec[0] == 'mono': return {spec[1]: Fr(1)}
    w, n = spec[1], spec[2]
    return {w+h: Fr((-1)**(n-h)*math.comb(n, h)*math.comb(n+h, h)) for h in range(n+1)}

def T_at_1_exact(spec):
    ct = T_coeffs(spec); return sum(ct.values()), sum(h*c for h, c in ct.items())

def strain_exact(gen, p):
    if gen['spec'][0] != 'mono': return Fr(0)
    m, k = gen['m'], gen['m'] + gen['spec'][1]; pj = p[gen['j']]
    if (m, k) == (0, 0): return 4*pj*(pj-1)
    if (m, k) == (0, 1): return 8*(pj-1)
    if (m, k) == (0, 2): return Fr(8)
    if (m, k) == (2, 2): return Fr(-24)
    return Fr(0)

def sectors_general(gens, coefs, cl, qmax=3, hmax=7, jmax=5):
    g = Fr(1)/cl; lam = 1-g; p = [(3+g-j*lam)/2 for j in range(jmax+1)]
    def alpha(h, q): return g - h*lam - 2*q
    C = {}; G = {}; Phi = {}
    for j in range(jmax+1):
        for q in range(qmax+1):
            Cj = {}
            for gen, a in zip(gens, coefs):
                if gen['j'] != j or a == 0: continue
                m = gen['m']; ct = T_coeffs(tuple(gen['spec']))
                v = a*sum(c*binom_fr(p[j]-m-h, q) for h, c in ct.items())
                if v != 0: Cj[2*m] = Cj.get(2*m, 0) + v
            Cj = {k: v for k, v in Cj.items() if v != 0}
            s = 2*p[j] - 2*q
            C[(j, q)] = Cj; G[(j, q)] = FE.density_rule(Cj, s); Phi[(j, q)] = FE.stream_rule(Cj, s)
    E = {}
    for h in range(hmax+1):
        for q in range(qmax+1):
            terms = []
            if h <= jmax: terms.append(FE.sscale(G[(h, q)], cl*alpha(h, q)-1))
            for i in range(jmax+1):
                jj = h-1-i
                if not (0 <= jj <= jmax): continue
                for u in range(q+1):
                    v = q-u; ai = alpha(i, u); aj = alpha(jj, v)
                    terms.append(FE.sscale(FE.sin_times_cos(Phi[(i, u)], FE.dtheta_sin(G[(jj, v)])), ai+1))
                    terms.append(FE.sscale(FE.sin_times_cos(G[(jj, v)], FE.dtheta_sin(Phi[(i, u)])), -aj))
            E[(h, q)] = FE.ssum(*terms)
    return {'alpha': alpha, 'C': C, 'G': G, 'E': E, 'p': p}

def main(result_json, out_json):
    d = json.load(open(result_json))
    gens = d['gens']; coefs = [Fr(c) for c in d['coefs']]; cl = Fr(d['cl']); g = Fr(1)/cl; lam = 1-g
    p = [(3+g-j*lam)/2 for j in range(6)]
    # constraints exactly: rows/rhs in the file are floats; rebuild them exactly: L1 (branch-0 moments: rhs = exact current values of the CHECKPOINT? we use the float rhs rounded: the frozen branch-0 moments must equal the checkpoint's exact moments -> recompute from the checkpoint coefficients (gens with kind old_*, original a)
    # Here: constraint set = {branch-0 moments (exact checkpoint values)} U {branch-j targets (exact rationals from the formal tail file)} U {center}.
    V = json.load(open(d['formal_tail'])) if 'formal_tail' in d else None
    return gens, coefs, cl, p

if __name__ == '__main__':
    result_json, ckpt_json, formal_json, out_json = sys.argv[1:5]
    d = json.load(open(result_json)); gens = d['gens']; coefs = [Fr(c) for c in d['coefs']]; cl = Fr(d['cl']); g = Fr(1)/cl; lam = 1-g
    p = [(3+g-j*lam)/2 for j in range(8)]
    # exact checkpoint coefficients (for the frozen branch-0 moments): T1 coordinates as exact rationals
    ck = json.load(open(ckpt_json))
    low = [Fr(float.fromhex(h)) for h in ck['P_hex']]; num, den = ck['input_exact_for_checkpoint']['a000_exact'].split('/'); low[0] = Fr(int(num), int(den))
    high = [Fr(float.fromhex(h)) for h in ck['high_hex']]; NN = [Fr(float.fromhex(h)) for h in ck['frozen_Nn_hex']]
    LOW = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]; HIGH = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]
    a_ck = [v for v in low] + [c*NN[n] for c, (m, n, j) in zip(high, HIGH)]
    assert all(gens[i]['kind'] in ('old_low', 'old_high') for i in range(860))
    # branch-0 moments of the checkpoint (exact)
    lead = [T_at_1_exact(tuple(gen['spec']))[0] for gen in gens]
    mom0 = {m: sum(a_ck[i]*lead[i] for i in range(860) if gens[i]['m'] == m and gens[i]['j'] == 0) for m in range(10)}
    V = json.load(open(formal_json))
    for extra in os.environ.get('N12_EXTRA_ORDERS', '').split(','):
        if extra: V['stationary_density_orders'].update(json.load(open(extra))['stationary_density_orders'])
    branches = {int(j): ((int(v[0]), v[1]) if (v and not isinstance(v[0], list)) else (max(int(e_[0]) for e_ in v), None)) for j, v in d['branches'].items()}
    # exact targets: invert the density rule exactly
    targets = {}
    for j, (Mj, kx) in branches.items():
        coef = {int(k): Fr(v) for k, v in V['stationary_density_orders'][str(j+1)]['coefficients'].items()}
        M = (max(coef)-1)//2; s = 2*p[j]
        # upper bidiagonal solve from the top harmonic
        Cm = {}
        for m in range(M, -1, -1):
            n = 2*m; diag = -(s*s - n*n)*(s-2-n)/2
            if m == 0: diag += -(s*s - n*n)*(s-2+n)/2          # folded sin(-theta) term
            rhs = coef.get(2*m+1, Fr(0))
            if m+1 <= M:
                n2 = 2*(m+1); rhs -= Cm[m+1]*((s*s - n2*n2)*(s-2+n2)/2)
            Cm[m] = rhs/diag
        targets[j] = Cm
        assert M == Mj, (M, Mj)
    # impose exactly via pivots: for each constrained (m, j): pivot = first generator of that (m,j) with kind 'new' if any else the 'old_high' n=0 (or old_low k=m)
    def pivot_index(m, j):
        cands = [i for i, gen in enumerate(gens) if gen['m'] == m and gen['j'] == j]
        for i in cands:
            if gens[i]['kind'] == 'new' and gens[i]['spec'][1] == 0: return i
        for i in cands:
            if gens[i]['kind'] == 'old_high' and gens[i]['spec'][2] == 0: return i
        for i in cands:
            if gens[i]['kind'] == 'old_low' and gens[i]['spec'][1] == 0: return i
        return cands[0]
    maxchange = Fr(0)
    # order: center condition first (pivot a_000, the only pivot with nonzero strain), then all moment constraints with zero-strain pivots
    s_i = [strain_exact({'m': gen['m'], 'j': gen['j'], 'spec': tuple(gen['spec'])}, p) for gen in gens]
    cur = sum(coefs[i]*s_i[i] for i in range(len(gens)))
    delta = (1 - cl - cur)/s_i[0]; coefs[0] += delta; maxchange = max(maxchange, abs(delta))
    def pivot_index(m, j):
        cands = [i for i, gen in enumerate(gens) if gen['m'] == m and gen['j'] == j and s_i[i] == 0]
        for i in cands:
            if gens[i]['kind'] == 'new' and gens[i]['spec'][1] == 0: return i
        for i in cands:
            if gens[i]['kind'] == 'old_high' and gens[i]['spec'][2] == 0: return i
        return cands[0]
    DESC = [int(v) for v in sys.argv[5].split(',')] if len(sys.argv) > 5 and sys.argv[5] not in ('', 'none') else []
    q1 = [Fr(gens[i]['j'] and 0) for i in range(len(gens))]
    for i, gen in enumerate(gens):
        T1, dT1 = T_at_1_exact(tuple(gen['spec'])); q1[i] = (p[gen['j']] - gen['m'])*T1 - dT1      # q = 1 potential moment of the generator: beta T(1) - T'(1)
    def impose(m, j, tgt):
        """impose sum_block a lead = tgt (and, if j in DESC, sum_block a q1 = 0) exactly through one or two zero-strain pivots of the (m, j) block."""
        global maxchange
        blk = [k for k in range(len(gens)) if gens[k]['m'] == m and gens[k]['j'] == j]
        cur = sum(coefs[k]*lead[k] for k in blk)
        if j not in DESC:
            i = pivot_index(m, j); delta = (tgt - cur)/lead[i]; coefs[i] += delta; maxchange = max(maxchange, abs(delta)); return
        curD = sum(coefs[k]*q1[k] for k in blk)
        i1 = pivot_index(m, j)
        cands = [k for k in blk if s_i[k] == 0 and k != i1 and lead[k]*q1[i1] - lead[i1]*q1[k] != 0]
        assert cands, ('no second pivot for descendant constraint', m, j)
        i2 = sorted(cands, key=lambda k: (gens[k]['kind'] != 'new', gens[k]['spec'][1] if gens[k]['spec'][0] == 'mono' else 99))[0]
        det = lead[i1]*q1[i2] - lead[i2]*q1[i1]
        b1 = tgt - cur; b2 = -curD
        d1 = (b1*q1[i2] - lead[i2]*b2)/det; d2 = (lead[i1]*b2 - q1[i1]*b1)/det
        coefs[i1] += d1; coefs[i2] += d2; maxchange = max(maxchange, abs(d1), abs(d2))
    for m in range(10): impose(m, 0, mom0[m])
    if 0 in DESC:
        for m in sorted({gen['m'] for gen in gens if gen['j'] == 0 and gen['m'] >= 10}): impose(m, 0, Fr(0))   # branch-0 harmonics beyond the checkpoint's: leading moment 0 (Theta_0 fixed), descendant 0
    for j, Cm in targets.items():
        for m, tgt in Cm.items(): impose(m, j, tgt)
        if j in DESC:
            for m in sorted({gen['m'] for gen in gens if gen['j'] == j and gen['m'] not in Cm}): impose(m, j, Fr(0))
    for j in DESC:
        for m in sorted({gen['m'] for gen in gens if gen['j'] == j}):
            blk = [k for k in range(len(gens)) if gens[k]['m'] == m and gens[k]['j'] == j]
            assert sum(coefs[k]*q1[k] for k in blk) == 0, ('descendant not zero', j, m)
    print('descendant constraints D_(j,m) = 0 imposed and verified exactly for branches', DESC)
    assert sum(coefs[i]*s_i[i] for i in range(len(gens))) == 1 - cl
    print('exact projection: max pivot change %.3e' % float(maxchange))
    X = sectors_general(gens, coefs, cl, qmax=2, hmax=8, jmax=7)
    g = Fr(1)/cl
    print('residual sectors (exact):')
    for (h, q), S in sorted(X['E'].items(), key=lambda kv: -float(X['alpha'](*kv[0]))):
        ex = float(X['alpha'](h, q))
        if ex < -2.5: continue
        n2 = sum(v*v for v in S.values())/4
        print('   (%d,%d) exponent %+.4f: %s  ||E||_{L2(0,pi/2)} = %.6g  max harmonic %s' % (h, q, ex, 'EXACT ZERO' if not S else 'nonzero', math.sqrt(float(n2)*math.pi) if S else 0.0, max(S) if S else '-'))
    G00 = X['G'][(0, 0)]; print('leading density profile Theta_0 unchanged:', all(G00.get(k, 0) == v for k, v in {int(k): Fr(vv) for k, vv in V['stationary_density_orders']['1']['coefficients'].items()}.items()))
    out = {'cl': str(cl), 'generators': [{'m': gen['m'], 'j': gen['j'], 'spec': list(gen['spec']), 'coef': '%d/%d' % (c.numerator, c.denominator)} for gen, c in zip(gens, coefs)],
           'note': 'chi = H_m (1+r^2)^(p_j - m) T(t), t = r^2/(1+r^2); spec [mono, h]: T = t^h; spec [leg, w, n]: T = t^w P_n(2t-1) (N_n folded into coef); rho = -d_y Lap sum coef chi'}
    json.dump(out, open(out_json, 'w'))
    print('exact coefficient file written:', out_json)
