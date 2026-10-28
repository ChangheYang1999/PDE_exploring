"""Cancellation-free enclosure of the residual F over boxes.

Identity (Euler operator; verified numerically below): (c_l X.grad - 1) rho[chi] = rho[(c_l X.grad - 3 c_l - 1) chi], and for
chi_{mkj} = r^{2k} R^{p_j-k} cos 2m theta:  (c_l X.grad - 3c_l - 1) chi_{mkj} = -j(c_l - 1) chi_{mkj} + 2 c_l (k - p_j) u chi_{mkj},  u = 1/R.
Hence F = rho[phi_L] + U.grad rho with  phi_L = sum a_{mkj} [ -j(c_l-1) chi_{mkj} + 2c_l (k - p_j) r^{2k} R^{p_j-k-1} cos 2m theta ],
and both terms are O(r^{2gamma-1}) at infinity: no cancellation between large terms.
phi_L in branch form: for each (m, j): H_m R^{p_j-m} [-j(c_l-1) sum_k a t^{k-m}] + H_m R^{p_j-m-1} [2c_l sum_k (k-p_j) a t^{k-m}].
T1 form of the second bracket: 2c_l R^{p_j-m-1} (t d/dt + m - p_j) L_{mj}(t), L_{mj} = sum_h c_h t^h + t^w sum_n g_n N_n P_n(2t-1):
  (t d/dt + m - p) L = sum_h (h + m - p) c_h t^h + t^w sum_n g_n N_n [ (w + m - p) P_n(z) + 2 t P_n'(z) ].
Similarly K_bar = rho[phi_K], phi_K = sum a [(4 - 2p_j) chi + 2(p_j - k) u chi]  (K_bar = rho - X.grad rho, from (4 - X.grad) chi).
"""
import math, sys, os
def _fup(x):
    """binary64 >= the upper bound of the arb x (outward rounding of a radius conversion)."""
    return math.nextafter(float(x.upper()), math.inf)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import arb, arb_series, acb, ctx, fmpq, fmpq_mat
from boxenc3 import BoxEnclosure3, FIELDS, _arb_fr, falling, lah
from boxenc2 import P_gamma

class FCert(BoxEnclosure3):
    def branches(self, kind):
        """List of (m, beta, coeffs[t^0..]) for the potential 'base', 'L' (transport) or 'K' (scaling)."""
        out = []
        for (m, j), coeffs in self.A.items():
            p = self.p[j]
            if kind == 'base':
                out.append((m, p - m, coeffs))
            elif kind == 'L':
                out.append((m, p - m, [(-j*(self.cl - 1))*c for c in coeffs]))
                out.append((m, p - m - 1, [2*self.cl*((m+i) - p)*c for i, c in enumerate(coeffs)]))
            elif kind == 'K':
                out.append((m, p - m, [(4 - 2*p)*c for c in coeffs]))
                out.append((m, p - m - 1, [2*(p - (m+i))*c for i, c in enumerate(coeffs)]))
        return out

    def series_branches(self, br, x0, y0, u, v, order):
        N = order+1
        if ctx.cap < N: ctx.cap = N
        X = arb_series([x0, arb(u)], N); Y = arb_series([y0, arb(v)], N)
        q = X*X + Y*Y; R = q + 1; t = q/R; logR = R.log()
        re2 = X*X - Y*Y; im2 = 2*X*Y
        mmax = max(m for (m, beta, coeffs) in br)
        H = [arb_series([1], N)]
        pre, pim = arb_series([1], N), arb_series([0], N)
        for m in range(1, mmax+1):
            pre, pim = pre*re2 - pim*im2, pre*im2 + pim*re2
            H.append(pre)
        total = arb_series([0], N)
        for (m, beta, coeffs) in br:
            G = arb_series([0], N)
            for c in reversed(coeffs): G = G*t + c
            total = total + H[m]*(beta*logR).exp()*G
        return total

    def jet_branches(self, br, x0, y0, order):
        if ctx.cap < order+1: ctx.cap = order+1
        D = self._directions(order)
        series = [self.series_branches(br, x0, y0, u, v, order) for (u, v) in D]
        coef = [[s[d] for d in range(order+1)] for s in series]
        jet = {(0, 0): coef[0][0]}
        for d in range(1, order+1):
            dirs = D[:d+1]
            M = fmpq_mat([[fmpq(u)**a * fmpq(v)**(d-a) for a in range(d, -1, -1)] for (u, v) in dirs])
            Minv = M.inv(); rhs = [coef[i][d] for i in range(d+1)]
            for row, a in enumerate(range(d, -1, -1)):
                val = arb(0)
                for col in range(d+1): val += arb(Minv[row, col])*rhs[col]
                jet[(a, d-a)] = val*math.factorial(a)*math.factorial(d-a)
        return jet

    # ---- crude radial bounds for the T1 forms of phi_L / phi_K: specs = list of (m, beta, lows{h:|c|}, highs{n:|g N|}, c0, mode)
    #      mode 'plain': R^beta [sum c_h t^h + t^w sum g P_n];  mode 'deriv': R^beta [sum (h+m-p) c_h t^h + t^w sum g ((w+m-p) P_n + 2 t P_n')] scaled
    def radial_specs(self, kind):
        specs = []
        for (m, j) in self.A:
            p = self.p[j]; lows = self.lowabs.get((m, j), {}); highs = self.highabs.get((m, j), {})
            if kind == 'L':
                s1 = abs(-j*(self.cl - 1)); s2 = abs(2*self.cl)
                specs.append((m, p - m, {h: s1*c for h, c in lows.items()}, {n: s1*g for n, g in highs.items()}, None, 'plain'))
                specs.append((m, p - m - 1, {h: s2*abs(h + m - p)*c for h, c in lows.items()}, {n: s2*g for n, g in highs.items()}, abs(max(5-m, 0) + m - p), 'deriv'))
            elif kind == 'K':
                s1 = abs(4 - 2*p); s2 = arb(2)
                specs.append((m, p - m, {h: s1*c for h, c in lows.items()}, {n: s1*g for n, g in highs.items()}, None, 'plain'))
                specs.append((m, p - m - 1, {h: s2*abs(p - h - m)*c for h, c in lows.items()}, {n: s2*g for n, g in highs.items()}, abs(max(5-m, 0) + m - p), 'deriv'))
        return specs

    def radial_bounds_specs(self, specs, q_lo, q_hi, order):
        R_lo = 1 + q_lo; R_hi = 1 + q_hi; u_hi = 1/R_lo; u_lo = 1/R_hi
        t_lo = 1 - u_hi; t_hi = 1 - u_lo
        z_lo = 2*t_lo - 1; z_hi = 2*t_hi - 1; z_mid = (z_lo + z_hi)/2; hz = arb((z_hi - z_lo).upper())/2
        PD = self.legendre_derivs(z_mid, 26)
        nmax = 25
        Pi = [[arb(0)]*(nmax+2) for _ in range(nmax+1)]
        hzp = [arb(1)]
        for k in range(1, nmax+2): hzp.append(hzp[-1]*hz)
        for n in range(nmax+1):
            for s in range(n+2):
                acc = arb(0)
                for k in range(max(n-s, 0)+1): acc += abs(PD[n][s+k])*hzp[k]/math.factorial(k)
                Pi[n][s] = acc
        t_hi_p = [arb(1)]
        for k in range(1, 32): t_hi_p.append(t_hi_p[-1]*t_hi)
        u_hi_p = [arb(1)]
        for k in range(1, 2*order+4): u_hi_p.append(u_hi_p[-1]*u_hi)
        out = []
        for (m, beta, lows, highs, c0, mode) in specs:
            w = max(5-m, 0)
            Lam = []
            for k in range(order+1):
                acc = arb(0)
                for h, c in lows.items():
                    if h >= k: acc += c*math.perm(h, k)*t_hi_p[h-k]
                for i in range(min(k, w)+1):
                    s = k - i
                    inner = arb(0)
                    for n, g in highs.items():
                        if mode == 'plain':
                            if s <= n: inner += g*(2**s)*Pi[n][s]
                        else:
                            # d^s/dt^s [c0 P_n(2t-1) + 2 t P_n'(2t-1)] <= c0 2^s Pi[n][s] + 2 (t_hi 2^(s+1) Pi[n][s+1] + s 2^s Pi[n][s])
                            val = c0*(2**s)*Pi[n][s] + 2*(t_hi*(2**(s+1))*Pi[n][s+1] + s*(2**s)*Pi[n][s])
                            inner += g*val
                    acc += math.comb(k, i)*math.perm(w, i)*t_hi_p[w-i]*inner
                Lam.append(acc)
            Dq = [Lam[0]]
            for a in range(1, order+1):
                acc = arb(0)
                for k in range(1, a+1): acc += Lam[k]*lah(a, k)*u_hi_p[a+k]
                Dq.append(acc)
            G = []
            for l in range(order+1):
                acc = arb(0)
                for a in range(l+1):
                    e = beta - (l-a)
                    Rmax = R_hi**e if e >= 0 else R_lo**e
                    acc += math.comb(l, a)*abs(falling(beta, l-a))*Rmax*Dq[a]
                G.append(acc)
            out.append((m, G))
        return out

    def crude_branches(self, specs, xabs, yabs, q_lo, q_hi, order):
        GB = self.radial_bounds_specs(specs, q_lo, q_hi, order)
        Gm = {m: [arb(0)]*(order+1) for m in range(10)}
        for (m, G) in GB:
            for l in range(order+1): Gm[m][l] = Gm[m][l] + G[l]
        xp = [arb(1)]; yp = [arb(1)]
        for i in range(order+1): xp.append(xp[-1]*xabs); yp.append(yp[-1]*yabs)
        rabs = (xabs*xabs + yabs*yabs).sqrt(); rp = [arb(1)]
        for i in range(19): rp.append(rp[-1]*rabs)
        out = {}
        for a in range(order+1):
            b = order - a; total = arb(0)
            for m in range(10):
                n = 2*m
                for b1 in range(min(a, n)+1):
                    for b2 in range(min(b, n-b1)+1):
                        k = b1 + b2; dH = math.perm(n, k)*rp[n-k]
                        s = arb(0)
                        for l, poly in P_gamma((a-b1, b-b2)).items():
                            pv = arb(0)
                            for (i, jj), c in poly.items(): pv += abs(c)*xp[i]*yp[jj]
                            s += Gm[m][l]*pv
                        total += dH*s*(math.comb(a, b1)*math.comb(b, b2))
            out[(a, b)] = total
        return out

    def enclose_F(self, x_c, y_c, hx, hy, K=8, want_K=False):
        """F over the box = rho[phi_L] (center Taylor of degree K + crude remainder) + U.grad rho (tight field enclosures)."""
        ctx.prec = self.prec
        base = self.enclose(x_c, y_c, hx, hy, K=K, fields={'U1': FIELDS['U1'], 'U2': FIELDS['U2'], 'rho_x': FIELDS['rho_x'], 'rho_y': FIELDS['rho_y']})
        xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); hxA = _arb_fr(Fr(hx)); hyA = _arb_fr(Fr(hy))
        xabs = abs(xc) + hxA; yabs = abs(yc) + hyA
        xmin = abs(xc) - hxA; ymin = abs(yc) - hyA
        xmin = xmin if xmin > 0 else arb(0); ymin = ymin if ymin > 0 else arb(0)
        q_lo = xmin*xmin + ymin*ymin; q_hi = xabs*xabs + yabs*yabs
        dx = arb(0, _fup(hxA)); dy = arb(0, _fup(hyA))
        dxp = [arb(1)]; dyp = [arb(1)]; hxp = [arb(1)]; hyp = [arb(1)]
        for i in range(K+2): dxp.append(dxp[-1]*dx); dyp.append(dyp[-1]*dy); hxp.append(hxp[-1]*hxA); hyp.append(hyp[-1]*hyA)
        out = {'x': base['x'], 'y': base['y']}
        for kind, name in (('L', 'rhoL'), ('K', 'rhoK')) if want_K else (('L', 'rhoL'),):
            J = self.jet_branches(self.branches(kind), xc, yc, 3 + K)
            crude = self.crude_branches(self.radial_specs(kind), xabs, yabs, q_lo, q_hi, 3 + K + 1)
            comb = FIELDS['rho']
            poly = arb(0)
            for b1 in range(K+1):
                for b2 in range(K+1-b1):
                    coef = sum((c*J[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                    poly += coef*dxp[b1]*dyp[b2]/(math.factorial(b1)*math.factorial(b2))
            rem = arb(0)
            for b1 in range(K+2):
                b2 = K+1-b1
                coef = sum((abs(c)*crude[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                rem += coef*hxp[b1]*hyp[b2]/(math.factorial(b1)*math.factorial(b2))
            out[name] = poly + arb(0, _fup(rem)); out[name+'_rem'] = _fup(rem); out[name+'_center'] = J and sum((c*J[(a, b)] for (a, b), c in comb.items()), arb(0))
        out['F'] = out['rhoL'] + base['U1']*base['rho_x'] + base['U2']*base['rho_y']
        out['UgradRho'] = base['U1']*base['rho_x'] + base['U2']*base['rho_y']
        if want_K: out['K'] = out['rhoK']
        for k in ('U1', 'U2', 'rho_x', 'rho_y'): out[k] = base[k]
        return out

if __name__ == '__main__':
    import time
    from cert_M import cell_box
    S = FCert(sys.argv[1], sys.argv[2], prec=256)
    # identity check at points: F (direct) vs rho[phi_L] + U.grad rho
    for (x, y) in [(0.3, 0.5), (1.0, 2.0), (7.0, 1.0), (0.0, 500.0), (2000.0, 100.0)]:
        f = S.fields(x, y, 4)
        JL = S.jet_branches(S.branches('L'), arb(x), arb(y), 3)
        rhoL = -(JL[(2, 1)] + JL[(0, 3)])
        JK = S.jet_branches(S.branches('K'), arb(x), arb(y), 3)
        rhoK = -(JK[(2, 1)] + JK[(0, 3)])
        Kdir = f['rho'] - arb(x)*f['rho_x'] - arb(y)*f['rho_y']
        print('point (%g,%g): F direct %s ; rho[phi_L] + U.grad rho = %s ; diff %s | K direct %s rho[phi_K] diff %s' % (x, y, f['F'].str(10), (rhoL + f['U1']*f['rho_x'] + f['U2']*f['rho_y']).str(10), (f['F'] - rhoL - f['U1']*f['rho_x'] - f['U2']*f['rho_y']).str(3), Kdir.str(8), (Kdir - rhoK).str(3)))
    p2 = float(2/S.cl - 1)
    for (r_lo, t_lo) in [(0.01, 1.5), (0.3, 1.0), (3.0, 0.3), (30.0, 1.5), (300.0, 0.7), (1000.0, 0.7), (9000.0, 1.55)]:
        xc, yc, hx, hy = cell_box(r_lo, r_lo*1.02, t_lo, t_lo + math.pi/160)
        t0 = time.time(); o = S.enclose_F(xc, yc, hx, hy, K=8); dt = time.time()-t0
        print('cell r=%g th=%.2f: F in %s (rhoL %s rem %.1e; U.grad rho %s) -> |F| r^-p2 <= %.5g   t=%.2fs' % (r_lo, t_lo, o['F'].str(6), o['rhoL'].str(6), o['rhoL_rem'], o['UgradRho'].str(6), float(abs(o['F']).upper())/r_lo**p2, dt))
