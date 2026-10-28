"""H2 (lead 04:21Z): FLOAT E2 components of the spliced potential phi_R = chi_R phi_ref + (1 - chi_R) phi_stat, where phi_ref is a refit (or the checkpoint)
in generator form, phi_stat = sum_{n=1}^{6} r^(p_n + 3) sum_m C_{n,m} cos(2m theta) is the exact potential of the verifier's six stationary density orders
(C_{n,m} by the inverse density rule), and chi_R(r) = S((log(2R) - log r)/log 4) (smoothstep S(u) = 6u^5 - 15u^4 + 10u^3 on [0,1]): chi = 1 for r <= R/2, 0 for r >= 2R.
Fields from the jets of phi_R (Leibniz with the radial jets of chi, universal polynomials P_{gamma,l}); F = (c_l X + U).grad rho - rho.
Norms (lead weights): ||r F||_2, ||F||_2, ||grad F||_2, ||(1+4r^2)^0.4 D^2 F||_2 on a log-polar grid up to 4R (where phi_R = phi_stat exactly), plus the far part
r >= 4R from the exact residual sectors of phi_stat (orders 7 and 8: exponents p_7, p_8 and their q = 0 descendants... phi_stat has pure powers, so its residual sectors
are E_{h,0}, h = 6, 7, ..., 11 (pairs i + j + 1 = h with i, j <= 5); we use h = 6..11) integrated analytically. Octave profile of the weighted Hessian also printed.
Usage: splice_norms.py ref_exact.json formal_tail.json R [ns nth]"""
import sys, os, json, math
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n12_eval import make_cache, generator_jet, falling_prod
from n12_fit import F_jets, ORDER, density_rule_matrix
from boxenc2 import P_gamma
import farfield_exact as FE

def smoothstep_derivs_q(q, q1, q2, order):
    """chi(q) = S(u), u = (log q2 - log q)/(log q2 - log q1) (so chi = 1 at q <= q1, 0 at q >= q2); returns [d^a chi/dq^a] for a <= order via sympy."""
    import sympy as sp
    qs = sp.symbols('q', positive=True)
    u = (sp.log(q2) - sp.log(qs))/(sp.log(q2) - sp.log(q1))
    S = 6*u**5 - 15*u**4 + 10*u**3
    ders = [sp.lambdify(qs, sp.diff(S, qs, a), 'numpy') for a in range(order+1)]
    out = []
    for a in range(order+1):
        v = np.zeros_like(q)
        mid = (q > q1) & (q < q2)
        v[mid] = ders[a](q[mid])
        if a == 0: v[q <= q1] = 1.0
        out.append(v)
    return out

def radial_jet_from_g(x, y, gl, order):
    """jet dict of a radial function g(q) given its q-derivatives gl[l] (arrays): d^gamma g = sum_l g^{(l)} P_{gamma,l}(x,y)."""
    xp = [np.ones_like(x)]; yp = [np.ones_like(y)]
    for i in range(order+1): xp.append(xp[-1]*x); yp.append(yp[-1]*y)
    out = {}
    for a in range(order+1):
        for b in range(order+1-a):
            acc = np.zeros_like(x)
            for l, poly in P_gamma((a, b)).items():
                pv = np.zeros_like(x)
                for (i, j), c in poly.items(): pv += c*xp[i]*yp[j]
                acc += gl[l]*pv
            out[(a, b)] = acc
    return out

def power_jet(x, y, m, beta, order, cache):
    """jet of H_m(x,y) q^beta (pure power), evaluated only where q > 0."""
    q = cache['q']; logq = np.log(np.maximum(q, 1e-300))
    gl = [falling_prod(beta, 0, a)*np.exp((beta - a)*logq) for a in range(order+1)]
    xp = [np.ones_like(x)]; yp = [np.ones_like(y)]
    for i in range(order+1): xp.append(xp[-1]*x); yp.append(yp[-1]*y)
    dH = cache['H'][m]; n = 2*m; logr = cache['logr']
    out = {}
    for a in range(order+1):
        for b in range(order+1-a):
            acc = np.zeros_like(x)
            for b1 in range(min(a, n)+1):
                for b2 in range(min(b, n-b1)+1):
                    k = b1 + b2; dh = dH[(b1, b2)]*np.exp((n-k)*logr)
                    s = np.zeros_like(x)
                    for l, poly in P_gamma((a-b1, b-b2)).items():
                        pv = np.zeros_like(x)
                        for (i, j), c in poly.items(): pv += c*xp[i]*yp[j]
                        s += gl[l]*pv
                    acc += math.comb(a, b1)*math.comb(b, b2)*dh*s
            out[(a, b)] = acc
    return out

def jet_mul(A, B, order):
    """Leibniz product of two jets (derivative dicts)."""
    out = {}
    for (i, j), u in A.items():
        for (k, l), v in B.items():
            if i+k+j+l <= order:
                key = (i+k, j+l); out[key] = out.get(key, 0) + u*v*(math.comb(i+k, i)*math.comb(j+l, j))
    return out

def stationary_potential(formal_json, cl):
    """list of (m, beta, coef) with phi_stat = sum coef H_m q^beta, beta = (s_n - 2m)/2, s_n = p_n + 3 (density exponent p_n = order n), plus the density sectors dict for the far residual."""
    V = json.load(open(formal_json)); g = 1/cl; lam = 1-g
    terms = []; dens = {}
    for n in range(1, 7):
        coef = {int(k): float(Fr(v)) for k, v in V['stationary_density_orders'][str(n)]['coefficients'].items()}
        pn = float(Fr(V['stationary_density_orders'][str(n)]['power'])); s = pn + 3
        M = (max(coef)-1)//2; A = density_rule_matrix(M, s); rhs = np.array([coef.get(2*m+1, 0.0) for m in range(M+1)])
        C = np.linalg.solve(A, rhs)
        for m in range(M+1): terms.append((m, (s - 2*m)/2, C[m]))
        dens[n] = (pn, {2*m: Fr(C[m]).limit_denominator(10**15) for m in range(M+1)})
    return terms, dens

def far_sectors_stationary(dens, cl):
    """residual sectors E_{h,0} (h = 0..11) of the stationary pure-power potential: FE rules with Fractions (coefficients rationalized)."""
    g = Fr(1)/cl; lam = 1-g
    def alpha(h): return g - h*lam
    G = {}; Phi = {}
    for n, (pn, C) in dens.items():
        j = n-1; s = 2*(Fr(pn).limit_denominator(10**15)) + 0
        s = Fr(pn).limit_denominator(10**15) + 3
        G[j] = FE.density_rule(C, s); Phi[j] = FE.stream_rule(C, s)
    E = {}
    for h in range(12):
        terms = []
        if h in G: terms.append(FE.sscale(G[h], cl*alpha(h) - 1))
        for i in range(6):
            jj = h-1-i
            if jj in G and i in Phi:
                terms.append(FE.sscale(FE.sin_times_cos(Phi[i], FE.dtheta_sin(G[jj])), alpha(i)+1)); terms.append(FE.sscale(FE.sin_times_cos(G[jj], FE.dtheta_sin(Phi[i])), -alpha(jj)))
        E[h] = FE.ssum(*terms)
    return {h: (float(alpha(h)), {k: float(v) for k, v in S.items()}) for h, S in E.items()}

if __name__ == '__main__':
    ref_json, formal_json, R = sys.argv[1], sys.argv[2], float(sys.argv[3])
    ns = int(sys.argv[4]) if len(sys.argv) > 4 else 200; nth = int(sys.argv[5]) if len(sys.argv) > 5 else 24
    d = json.load(open(ref_json)); cl = Fr(d['cl']); clf = float(cl); g = 1/clf
    p = [(3+g-j*(1-g))/2 for j in range(6)]
    gens = [{'m': g_['m'], 'j': g_['j'], 'spec': tuple(g_['spec']), 'coef': float(Fr(g_['coef']))} for g_ in d['generators']]
    smin, smax = math.log(1e-3), math.log(4*R)
    s = np.linspace(smin, smax, ns); ds = s[1]-s[0]; th = (np.arange(nth)+0.5)/nth*math.pi/2; dth = math.pi/2/nth
    S_, TH = np.meshgrid(s, th, indexing='ij'); r = np.exp(S_).ravel(); x = (np.exp(S_)*np.cos(TH)).ravel(); y = (np.exp(S_)*np.sin(TH)).ravel()
    wq = r*r*ds*dth*4; wq[:nth] *= 0.5; wq[-nth:] *= 0.5
    cache = make_cache(x, y, ORDER)
    # reference jets (only needed where chi > 0: r < 2R)
    Jref = {}
    for gen in gens:
        if gen['coef'] == 0: continue
        gj = generator_jet(x, y, gen['m'], p[gen['j']]-gen['m'], gen['spec'], ORDER, cache)
        for k, v in gj.items(): Jref[k] = Jref.get(k, 0) + gen['coef']*v
    terms, dens = stationary_potential(formal_json, clf)
    Jstat = {}
    mask = r > R/4         # the stationary potential is used only where 1 - chi > 0 (r > R/2); evaluate for r > R/4 and zero elsewhere
    xs, ys = x[mask], y[mask]; cache_s = make_cache(xs, ys, ORDER)
    for (m, beta, c) in terms:
        pj = power_jet(xs, ys, m, beta, ORDER, cache_s)
        for k, v in pj.items():
            full = np.zeros_like(x); full[mask] = v; Jstat[k] = Jstat.get(k, 0) + c*full
    q = cache['q']; chi_l = smoothstep_derivs_q(q, (R/2)**2, (2*R)**2, ORDER)
    Jchi = radial_jet_from_g(x, y, chi_l, ORDER)
    one_minus = {k: (-v if k != (0, 0) else 1 - v) for k, v in Jchi.items()}
    J = jet_mul(Jchi, Jref, ORDER); J2 = jet_mul(one_minus, Jstat, ORDER)
    J = {k: J.get(k, 0) + J2.get(k, 0) for k in set(J) | set(J2)}
    FJ = F_jets(J, None, clf, x, y, K=2)
    D1 = FJ[(1, 0)]**2 + FJ[(0, 1)]**2; D2 = FJ[(2, 0)]**2 + 2*FJ[(1, 1)]**2 + FJ[(0, 2)]**2; wL = (1 + 4*r*r)**0.4
    comps = {'rF': r*r*FJ[(0, 0)]**2, 'F': FJ[(0, 0)]**2, 'gradF': D1, 'wLD2F': wL*wL*D2}
    # far part r >= 4R from the stationary residual sectors (h >= 6, exponents p_7 ... ) : sum over pairs of sectors
    E = far_sectors_stationary(dens, cl); Rf = 4*R
    import farfield_bounds as FB
    def far(e, deriv):
        secs = [(al, {('s', k): v for k, v in S.items()}) for h, (al, S) in E.items() if S and h >= 6]
        comps_ = []
        for (al, T) in secs:
            if deriv == 0: comps_.append([(al, T)])
            elif deriv == 1: comps_.append([(al-1, FB.dx(T, al)), (al-1, FB.dy(T, al))])
            else:
                Tx = FB.dx(T, al); Ty = FB.dy(T, al); comps_.append([(al-2, FB.dx(Tx, al-1)), (al-2, FB.dx(Ty, al-1)), (al-2, FB.dy(Tx, al-1)), (al-2, FB.dy(Ty, al-1))])
        ncomp = 1 if deriv == 0 else (2 if deriv == 1 else 4); total = 0.0
        for ci in range(ncomp):
            terms_ = [c[ci] for c in comps_]
            for (a1, T1) in terms_:
                for (a2, T2) in terms_:
                    ex = 2*e + a1 + a2 + 2
                    if ex >= 0: return float('inf')
                    total += math.pi*sum(v*T2.get(k, 0) for k, v in T1.items())*Rf**ex/(-ex)
        return total
    cL = (2**0.8*(1 + 1/(4*Rf*Rf))**0.4)**2
    res = {}
    for name, integrand in comps.items():
        e = {'rF': 1.0, 'F': 0.0, 'gradF': 0.0, 'wLD2F': 0.8}[name]; deriv = {'rF': 0, 'F': 0, 'gradF': 1, 'wLD2F': 2}[name]
        inner = float(np.sum(wq*integrand)); fp = far(e, deriv)*(cL if name == 'wLD2F' else 1.0)
        jb = np.floor(np.log2(r)).astype(int); prof = {int(j): float(np.sum((wq*integrand)[jb == j])) for j in np.unique(jb)}
        res[name] = {'grid_sq': inner, 'far_sq': fp, 'norm': math.sqrt(inner + fp), 'octaves': prof}
    print('splice R=%g: ||rF||=%.4g (far %.2e) ||F||=%.4g (far %.2e) ||gradF||=%.4g (far %.2e) ||wLD2F||=%.4g (far %.2e); 128*gradF = %.4g; stationary residual sector norms h=6,7: %s' % (R, res['rF']['norm'], math.sqrt(res['rF']['far_sq']), res['F']['norm'], math.sqrt(res['F']['far_sq']), res['gradF']['norm'], math.sqrt(res['gradF']['far_sq']), res['wLD2F']['norm'], math.sqrt(res['wLD2F']['far_sq']), 128*res['gradF']['norm'], [(h, round(E[h][0], 3), round(math.sqrt(math.pi*sum(v*v for v in E[h][1].values())/4), 4)) for h in (6, 7)]))
    print('   octaves of ||wL D^2 F||^2:', {j: '%.2e' % v for j, v in sorted(res['wLD2F']['octaves'].items()) if j >= -4})
    E2sq = res['wLD2F']['norm']**2 + 2**14*res['gradF']['norm']**2 + 2**18*res['F']['norm']**2 + 2**18*(20/21)*res['rF']['norm']**2
    print('   E2(R_tilde) (lead F1 definition, with ||R||_H <= ||rF||): %.4g' % math.sqrt(E2sq))
    json.dump({'R': R, 'components': res, 'E2_upper': math.sqrt(E2sq), 'stationary_sectors_h_ge_6': {str(h): (E[h][0], E[h][1]) for h in E if h >= 6}}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'splice_%s_R%g.json' % (os.path.basename(ref_json).replace('.json', ''), R)), 'w'))
