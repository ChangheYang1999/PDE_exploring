"""Gauge-invariant splice (lead route H2): rho_R = rho_s + chi (rho_1 - rho_s), psi_R = psi_s + chi (psi_1 - psi_s), chi = chi_R(r) smoothstep in log r
(1 for r <= R/2, 0 for r >= 2R); rho_1, psi_1 from a refit potential (generator form), rho_s, psi_s from the exact six-order stationary tail (pure powers,
evaluated through their sector series: no overflow). The pair (rho_R, psi_R) is not canonical on the annulus: S := -Lap psi_R - d_x rho_R is supported
there; the canonical stream function is psi_R - psi_c with -Lap psi_c = S solved by the mode formula (even sine modes). U = grad^perp(psi_R - psi_c),
F = (c_l X + U).grad rho_R - rho_R, its first and second derivatives, and the lead-weight E2 components on the grid (r <= Rmax) + far part from the
stationary residual sectors (orders >= 7). FLOAT throughout. Usage: splice2.py ref_exact.json formal_tail.json R [ns nth Rmax_factor]"""
import sys, os, json, math
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n12_eval import make_cache, generator_jet
from n12_fit import ORDER, density_rule_matrix
from boxenc2 import P_gamma
import farfield_exact as FE
import farfield_bounds as FB
from splice_norms import far_sectors_stationary

def trig_eval(T, th):
    v = np.zeros_like(th)
    for (kind, k), c in T.items(): v += float(c)*(np.sin(k*th) if kind == 's' else np.cos(k*th))
    return v

def stationary_sectors(formal_json):
    """per order n: density exponent p_n, density sine dict G_n, stream sine dict Phi_n (exponent p_n + 1), from the potential sectors (inverse density rule)."""
    V = json.load(open(formal_json)); out = {}
    for n in range(1, 7):
        coef = {int(k): Fr(v) for k, v in V['stationary_density_orders'][str(n)]['coefficients'].items()}
        pn = Fr(V['stationary_density_orders'][str(n)]['power']); s = pn + 3
        M = (max(coef)-1)//2
        Cm = {}
        for m in range(M, -1, -1):
            nn = 2*m; diag = -(s*s - nn*nn)*(s-2-nn)/2
            if m == 0: diag += -(s*s - nn*nn)*(s-2+nn)/2
            rhs = coef.get(2*m+1, Fr(0))
            if m+1 <= M: n2 = 2*(m+1); rhs -= Cm[m+1]*((s*s - n2*n2)*(s-2+n2)/2)
            Cm[m] = rhs/diag
        C = {2*m: v for m, v in Cm.items() if v != 0}
        G = FE.density_rule(C, s); Phi = FE.stream_rule(C, s)
        assert all(G.get(k, 0) == coef.get(k, 0) for k in set(G) | set(coef)), 'density rule inversion mismatch'
        out[n] = {'p': float(pn), 'G': {('s', k): float(v) for k, v in G.items()}, 'Phi': {('s', k): float(v) for k, v in Phi.items()}, 'C_exact': C, 's_exact': s}
    return out

def deriv_table(T, e, order):
    """all Cartesian derivatives d^a_x d^b_y of r^e T(theta) up to `order`: dict (a,b) -> (exponent, trig dict) via the polar rules."""
    out = {(0, 0): (e, T)}
    for o in range(1, order+1):
        for a in range(o+1):
            b = o - a
            if a > 0: ep, Tp = out[(a-1, b)]; out[(a, b)] = (ep-1, FB.dx(Tp, ep))
            else: ep, Tp = out[(a, b-1)]; out[(a, b)] = (ep-1, FB.dy(Tp, ep))
    return out

def stationary_fields(sects, r, th, order):
    """jets (a,b)->array of rho_s and psi_s to `order` from the sector series."""
    rho = {}; psi = {}
    for n, S in sects.items():
        for (field, T, e) in (('rho', S['G'], S['p']), ('psi', S['Phi'], S['p'] + 1)):
            tab = deriv_table(T, e, order)
            for (a, b), (ee, TT) in tab.items():
                val = r**ee*trig_eval(TT, th)
                dst = rho if field == 'rho' else psi
                dst[(a, b)] = dst.get((a, b), 0) + val
    return rho, psi

def chi_jets(x, y, q, q1, q2, order):
    """Cartesian jets of chi(r) = S(u), u = (log q2 - log q)/(log q2 - log q1), S smoothstep (1 for q <= q1, 0 for q >= q2)."""
    import sympy as sp
    qs = sp.symbols('q', positive=True)
    u = (sp.log(q2) - sp.log(qs))/(sp.log(q2) - sp.log(q1)); Ssym = 6*u**5 - 15*u**4 + 10*u**3
    ders = [sp.lambdify(qs, sp.diff(Ssym, qs, a), 'numpy') for a in range(order+1)]
    gl = []
    mid = (q > q1) & (q < q2)
    for a in range(order+1):
        v = np.zeros_like(q); v[mid] = ders[a](q[mid])
        if a == 0: v[q <= q1] = 1.0
        gl.append(v)
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

def jet_mul(A, B, order):
    out = {}
    for (i, j), u in A.items():
        for (k, l), v in B.items():
            if i+k+j+l <= order: key = (i+k, j+l); out[key] = out.get(key, 0) + u*v*(math.comb(i+k, i)*math.comb(j+l, j))
    return out

def _exp_lin_integrals(svals, k):
    """For the piecewise-linear interpolant of a function g(s) on the grid, return matrices L, Rm (ns x ns) such that
    (L @ g)[j] = int_{s' <= s_j} e^{-k (s_j - s')} g(s') ds' and (Rm @ g)[j] = int_{s' >= s_j} e^{-k (s' - s_j)} g(s') ds'  (exact for piecewise-linear g)."""
    ns = len(svals); ds = svals[1] - svals[0]
    # on an interval [s_i, s_{i+1}] with g linear: g(s') = g_i (1 - t) + g_{i+1} t, t = (s' - s_i)/ds.
    # left integral for target s_j >= s_{i+1}: e^{-k(s_j - s_{i+1})} * int_0^ds e^{-k(ds - x)} [g_i (1 - x/ds) + g_{i+1} x/ds] dx  (x = s' - s_i)
    # closed form: A = int_0^ds e^{-k(ds-x)} (1 - x/ds) dx = (1/k) - (1 - e^{-k ds})/(k^2 ds);  B = int_0^ds e^{-k(ds-x)} (x/ds) dx = (1 - e^{-k ds})/(k^2 ds) - e^{-k ds}/k
    E = math.exp(-k*ds); A = 1/k - (1 - E)/(k*k*ds); B = (1 - E)/(k*k*ds) - E/k
    L = np.zeros((ns, ns)); Rm = np.zeros((ns, ns))
    for j in range(ns):
        # intervals fully to the left: i = 0..j-1 (interval [s_i, s_{i+1}] with s_{i+1} <= s_j)
        i = np.arange(0, j)
        w = np.exp(-k*(svals[j] - svals[i+1]))
        np.add.at(L[j], i, w*A); np.add.at(L[j], i+1, w*B)
        # intervals to the right: i = j..ns-2, mirrored: int over [s_i, s_{i+1}] of e^{-k(s' - s_j)} g = e^{-k(s_i - s_j)} [g_i B' + g_{i+1} A'] with B' = int_0^ds e^{-k x}(1 - x/ds) dx = B (by symmetry x -> ds - x), A' = A
        i = np.arange(j, ns-1)
        w = np.exp(-k*(svals[i] - svals[j]))
        np.add.at(Rm[j], i, w*B); np.add.at(Rm[j], i+1, w*A)
    return L, Rm

def mode_solve(Sgrid, svals, thetas, kmax):
    """S on the (ns x nth) quadrant grid (odd-odd); even sine modes k <= kmax: S_k = (4/pi) int_0^{pi/2} S sin(k th) dth;
    u_k(r) = (1/2k)[r^-k I_1 + r^k I_2], I_1 = int_0^r t^{k+1} S_k dt, I_2 = int_r^inf t^{1-k} S_k dt (exact kernel quadrature against piecewise-linear e^{2s} S_k).
    Also returns the closed-form radial derivatives: u_k' = (-r^{-k-1} I_1 + r^{k-1} I_2)/2,
    u_k'' = ((k+1) r^{-k-2} I_1 + (k-1) r^{k-2} I_2)/2 - S_k  (from I_1' = r^{k+1} S_k, I_2' = -r^{1-k} S_k)."""
    nth = len(thetas); dth = math.pi/2/nth
    ks = np.arange(2, kmax+1, 2)
    W = (4/math.pi)*dth*np.sin(np.outer(ks, thetas))
    Sk = Sgrid @ W.T
    rvals = np.exp(svals)
    U = np.zeros_like(Sk); U1 = np.zeros_like(Sk); U2 = np.zeros_like(Sk)
    for j, k in enumerate(ks):
        L, Rm = _exp_lin_integrals(svals, k)
        g = rvals**2*Sk[:, j]
        rI1 = L @ g        # = r^-k I_1
        rI2 = Rm @ g       # = r^k I_2
        U[:, j] = (rI1 + rI2)/(2*k)
        U1[:, j] = (-rI1/rvals + rI2/rvals)/2
        U2[:, j] = ((k+1)*rI1/rvals**2 + (k-1)*rI2/rvals**2)/2 - Sk[:, j]
    return ks, Sk, U, (U1, U2)

def modes_to_jets(ks, Umodes, svals, thetas, order, derivs=None):
    """jets (a,b) -> array over the grid of u(r, th) = sum_k u_k(r) sin(k th), using u_k(sqrt(q)) q^{-k/2} as the radial factor of Im(z^k):
    radial derivatives of u_k in log r by spline, converted to q-derivatives of G_k(q) = u_k(r) r^{-k} symbolically."""
    import sympy as sp
    from scipy.interpolate import CubicSpline
    rvals = np.exp(svals); ns = len(svals); nth = len(thetas)
    rr = np.repeat(rvals, nth); tt = np.tile(thetas, ns); x = rr*np.cos(tt); y = rr*np.sin(tt); q = rr*rr; logr = np.log(rr)
    # symbolic: G(q) = u(r) r^-k with q = r^2, d/dq = (1/(2r)) d/dr; dG/dq^l in terms of u^(j)(r)
    rs, k_s = sp.symbols('r k', positive=True)
    uf = sp.Function('u')
    G = uf(rs)*rs**(-k_s)
    Gl = [G]
    for l in range(1, order+1): Gl.append(sp.diff(Gl[-1], rs)/(2*rs))
    uj = sp.symbols('u0 u1 u2 u3 u4 u5 u6')
    exprs = []
    for l in range(order+1):
        ex = sp.expand(Gl[l].doit()*rs**k_s)          # H_l := r^k G^{(l)}: no large powers of r (the r^-k is moved to the angular factor)
        for j in range(order, 0, -1): ex = ex.subs(sp.Derivative(uf(rs), (rs, j)), uj[j])
        ex = ex.subs(uf(rs), uj[0])
        exprs.append(sp.lambdify((rs, k_s) + uj[:order+1], ex, 'numpy'))
    xp = [np.ones_like(x)]; yp = [np.ones_like(y)]
    for i in range(order+1): xp.append(xp[-1]*x); yp.append(yp[-1]*y)
    out = {}
    for j, k in enumerate(ks):
        uR = [None]*(order+1)
        if derivs is not None:
            U1m, U2m = derivs
            uR[0] = Umodes[:, j]
            if order >= 1: uR[1] = U1m[:, j]
            if order >= 2: uR[2] = U2m[:, j]
            if order >= 3:
                cs2 = CubicSpline(svals, U2m[:, j]); uR[3] = cs2(svals, 1)/rvals      # d/dr of u'' via spline in s
        else:
            cs = CubicSpline(svals, Umodes[:, j])
            us = [cs(np.log(rvals), nu) for nu in range(order+1)]
            uR[0] = us[0]
            if order >= 1: uR[1] = us[1]/rvals
            if order >= 2: uR[2] = (us[2] - us[1])/rvals**2
            if order >= 3: uR[3] = (us[3] - 3*us[2] + 2*us[1])/rvals**3
        uRg = [np.repeat(v, nth) for v in uR[:order+1]]
        gl = [exprs[l](rr, float(k), *uRg) for l in range(order+1)]
        n = int(k)
        for a in range(order+1):
            for b in range(order+1-a):
                acc = np.zeros_like(x)
                for b1 in range(min(a, n)+1):
                    for b2 in range(min(b, n-b1)+1):
                        kk = b1 + b2
                        dh = math.perm(n, kk)*np.sin((n-kk)*tt + b2*math.pi/2)*np.exp(-kk*logr)      # r^(n-kk) * r^-k = r^-kk
                        s_ = np.zeros_like(x)
                        for l, poly in P_gamma((a-b1, b-b2)).items():
                            pv = np.zeros_like(x)
                            for (i, jj), c in poly.items(): pv += c*xp[i]*yp[jj]
                            s_ += gl[l]*pv
                        acc += math.comb(a, b1)*math.comb(b, b2)*dh*s_
                out[(a, b)] = out.get((a, b), 0) + acc
    return out

def F_from_fields(rho, U1, U2, cl, x, y, K=2):
    """jets of F = (cl X + U).grad rho - rho from field jets (rho to order K+1, U to order K)."""
    def coord(which, i, j):
        if (i, j) == (0, 0): return x if which == 0 else y
        if (i, j) == ((1, 0) if which == 0 else (0, 1)): return np.ones_like(x)
        return 0.0
    out = {}
    for i in range(K+1):
        for j in range(K+1-i):
            acc = -rho[(i, j)]
            for g1 in range(i+1):
                for g2 in range(j+1):
                    cb = math.comb(i, g1)*math.comb(j, g2)
                    V1 = cl*coord(0, g1, g2) + U1[(g1, g2)]; V2 = cl*coord(1, g1, g2) + U2[(g1, g2)]
                    acc = acc + cb*(V1*rho[(1+i-g1, j-g2)] + V2*rho[(i-g1, 1+j-g2)])
            out[(i, j)] = acc
    return out

if __name__ == '__main__':
    ref_json, formal_json, R = sys.argv[1], sys.argv[2], float(sys.argv[3])
    ns = int(sys.argv[4]) if len(sys.argv) > 4 else 240; nth = int(sys.argv[5]) if len(sys.argv) > 5 else 160; Rf = float(sys.argv[6]) if len(sys.argv) > 6 else 64.0
    d = json.load(open(ref_json)); cl = Fr(d['cl']); clf = float(cl); g = 1/clf; p = [(3+g-j*(1-g))/2 for j in range(6)]
    gens = [{'m': g_['m'], 'j': g_['j'], 'spec': tuple(g_['spec']), 'coef': float(Fr(g_['coef']))} for g_ in d['generators']]
    smin, smax = math.log(1e-3), math.log(Rf*R)
    svals = np.linspace(smin, smax, ns); thetas = (np.arange(nth)+0.5)/nth*math.pi/2; ds = svals[1]-svals[0]; dth = math.pi/2/nth
    rr = np.repeat(np.exp(svals), nth); tt = np.tile(thetas, ns); x = rr*np.cos(tt); y = rr*np.sin(tt)
    wq = rr*rr*ds*dth*4; wq[:nth] *= 0.5; wq[-nth:] *= 0.5
    # reference fields (only needed where chi > 0: r < 2R) -> evaluate everywhere r < 2R, zero beyond
    m1 = rr < 2*R; x1, y1 = x[m1], y[m1]; cache = make_cache(x1, y1, ORDER)
    J1 = {}
    for gen in gens:
        if gen['coef'] == 0: continue
        gj = generator_jet(x1, y1, gen['m'], p[gen['j']]-gen['m'], gen['spec'], ORDER, cache)
        for k, v in gj.items(): J1[k] = J1.get(k, 0) + gen['coef']*v
    def full(v):
        f = np.zeros_like(x); f[m1] = v; return f
    rho1 = {(a, b): full(-(J1[(2+a, 1+b)] + J1[(a, 3+b)])) for a in range(4) for b in range(4-a)}
    psi1 = {(a, b): full(J1[(1+a, 1+b)]) for a in range(4) for b in range(4-a)}
    # stationary fields where (1 - chi) > 0: r > R/2 -> evaluate for r > R/4
    sects = stationary_sectors(formal_json)
    m2 = rr > R/4
    rhos_, psis_ = stationary_fields(sects, rr[m2], tt[m2], 3)
    rhos = {k: full2 for k, full2 in ((k, np.zeros_like(x)) for k in rhos_)}
    for k in rhos_: rhos[k][m2] = rhos_[k]
    psis = {k: np.zeros_like(x) for k in psis_}
    for k in psis_: psis[k][m2] = psis_[k]
    q = rr*rr; CJ = chi_jets(x, y, q, (R/2)**2, (2*R)**2, 3)
    dR = {k: rho1[k] - rhos[k] for k in rho1}; dP = {k: psi1[k] - psis[k] for k in psi1}
    rhoR = jet_mul(CJ, dR, 3); psiR = jet_mul(CJ, dP, 3)
    rhoR = {k: rhos[k] + rhoR.get(k, 0) for k in rhos}; psiR = {k: psis[k] + psiR.get(k, 0) for k in psis}
    # Poisson defect S = -Lap psi_R - d_x rho_R
    S = -(psiR[(2, 0)] + psiR[(0, 2)]) - rhoR[(1, 0)]
    Sgrid = S.reshape(ns, nth)
    print('defect S: max |S| = %.4g at r = %.3g; max |S| outside the annulus [R/2, 2R]: %.2e' % (np.abs(S).max(), rr[np.argmax(np.abs(S))], np.abs(S[(rr < R/2) | (rr > 2*R)]).max()))
    kmax = min(2*nth - 2, 160)
    ks, Sk, Umodes, derivs = mode_solve(Sgrid, svals, thetas, kmax)
    print('mode energies of S (first 6 even k):', ['%.3g' % float(np.sqrt(np.sum(Sk[:, j]**2))) for j in range(6)], '; max |psi_c| = %.4g' % np.abs(Umodes).max())
    psic = modes_to_jets(ks, Umodes, svals, thetas, 3, derivs)
    # check: -Lap psi_c vs S on the grid
    lapc = -(psic[(2, 0)] + psic[(0, 2)])
    print('check -Lap psi_c = S: relative L2 error %.3e' % (np.sqrt(np.sum(wq*(lapc - S)**2))/np.sqrt(np.sum(wq*S**2))))
    psican = {k: psiR[k] - psic[k] for k in psiR}
    U1 = {(a, b): -psican[(a, b+1)] for a in range(3) for b in range(3-a)}; U2 = {(a, b): psican[(a+1, b)] for a in range(3) for b in range(3-a)}
    FJ = F_from_fields(rhoR, U1, U2, clf, x, y, K=2)
    D1 = FJ[(1, 0)]**2 + FJ[(0, 1)]**2; D2 = FJ[(2, 0)]**2 + 2*FJ[(1, 1)]**2 + FJ[(0, 2)]**2; wL = (1 + 4*rr*rr)**0.4
    comps = {'rF': rr*rr*FJ[(0, 0)]**2, 'F': FJ[(0, 0)]**2, 'gradF': D1, 'wLD2F': wL*wL*D2}
    # far part beyond Rmax from the stationary residual sectors (orders >= 7)
    dens = {n: (S_['p'], S_['C_exact']) for n, S_ in sects.items()}
    E = far_sectors_stationary(dens, cl); Rmax = Rf*R
    def far(e, deriv):
        secs = [(al, {('s', k): v for k, v in Sd.items()}) for h, (al, Sd) in E.items() if Sd and h >= 6]
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
                    total += math.pi*sum(v*T2.get(k, 0) for k, v in T1.items())*Rmax**ex/(-ex)
        return total
    cL = (2**0.8*(1 + 1/(4*Rmax*Rmax))**0.4)**2
    res = {}
    for name, integrand in comps.items():
        e = {'rF': 1.0, 'F': 0.0, 'gradF': 0.0, 'wLD2F': 0.8}[name]; deriv = {'rF': 0, 'F': 0, 'gradF': 1, 'wLD2F': 2}[name]
        inner = float(np.sum(wq*integrand)); fp = far(e, deriv)*(cL if name == 'wLD2F' else 1.0)
        jb = np.floor(np.log2(rr)).astype(int); prof = {int(j): float(np.sum((wq*integrand)[jb == j])) for j in np.unique(jb)}
        res[name] = {'grid_sq': inner, 'far_sq': fp, 'norm': math.sqrt(inner + fp), 'octaves': prof}
    E2sq = res['wLD2F']['norm']**2 + 2**14*res['gradF']['norm']**2 + 2**18*res['F']['norm']**2 + 2**18*(20/21)*res['rF']['norm']**2
    print('SPLICE2 R=%g: ||rF||=%.4g (far %.2e) ||F||=%.4g (far %.2e) ||gradF||=%.4g (far %.2e) ||wLD2F||=%.4g (far %.2e); E2 upper (lead F1) = %.4g; sup|F| = %.4g at r=%.3g' % (R, res['rF']['norm'], math.sqrt(res['rF']['far_sq']), res['F']['norm'], math.sqrt(res['F']['far_sq']), res['gradF']['norm'], math.sqrt(res['gradF']['far_sq']), res['wLD2F']['norm'], math.sqrt(res['wLD2F']['far_sq']), math.sqrt(E2sq), np.abs(FJ[(0, 0)]).max(), rr[np.argmax(np.abs(FJ[(0, 0)]))]))
    print('   octaves of ||wL D^2 F||^2:', {j: '%.2e' % v for j, v in sorted(res['wLD2F']['octaves'].items()) if j >= -2})
    print('   octaves of ||F||^2:', {j: '%.2e' % v for j, v in sorted(res['F']['octaves'].items()) if j >= -2})
    json.dump({'R': R, 'components': res, 'E2_upper': math.sqrt(E2sq), 'grid': [ns, nth, Rf]}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'splice2_%s_R%g.json' % (os.path.basename(ref_json).replace('.json', ''), R)), 'w'))
