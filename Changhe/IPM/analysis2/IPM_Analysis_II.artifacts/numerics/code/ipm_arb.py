"""Rigorous (ball arithmetic) evaluator of the case-4 potential family and all fields needed for the S1 analysis.

phi(x,y) = sum_{m,j} H_m(x,y) R^{p_j} sum_k a_{mkj} t^k,   H_m = Re (x+iy)^{2m}, q = x^2+y^2, R = 1+q, t = q/R
(because r^{2k} R^{p_j-k} cos(2m theta) = H_m q^{k-m} R^{p_j-k} = H_m R^{p_j} t^k / q^m ... careful: we use the form
 chi_{mkj} = cos(2m theta) r^{2k} R^{p_j-k} = (H_m / q^m) q^k R^{p_j-k} = H_m q^{k-m} R^{p_j-k} = H_m R^{p_j-m} t^{k-m}).
So phi = sum_{m,j} H_m R^{p_j-m} G_{mj}(t), G_{mj}(t) = sum_{k>=m} a_{mkj} t^{k-m}.

psi = phi_xy, rho = -d_y Lap phi, U = (-psi_y, psi_x) = (-phi_xyy, phi_xxy), V = cl X + U,
F(rho) = V . grad rho - rho  (the stationary self-similar IPM residual, 'R_rho' of the case-4 report; R_f = F/y).

All partial derivatives of phi up to a chosen order at a point are obtained from univariate Taylor series along
exact integer directions (python-flint arb_series), solved exactly for the mixed partials. Every output is an arb ball.
"""
import json, math
from fractions import Fraction as Fr
from flint import arb, arb_series, arb_mat, ctx, fmpq, fmpq_mat

def canon(j, m, k): return 215*j + 26*m - m*(m-1)//2 + (k-m)

class State:
    def __init__(self, exact_json, prec=256):
        ctx.prec = prec
        d = json.load(open(exact_json))
        self.label = d['label']
        self.cl_fr = Fr(d['cl'])
        self.a_fr = [Fr(s) for s in d['a_canonical']]
        self.prec = prec
        self._refresh()

    def _refresh(self):
        ctx.prec = self.prec
        self.cl = arb(fmpq(self.cl_fr.numerator, self.cl_fr.denominator))
        g = 1/self.cl; lam = 1-g
        self.p = [(3 + g - j*lam)/2 for j in range(4)]
        self.p_fr = [(3 + Fr(1)/self.cl_fr - j*(1-Fr(1)/self.cl_fr))/2 for j in range(4)]
        # coefficient table A[(m,j)] = list over k=m..25 of arb
        self.A = {}
        for j in range(4):
            for m in range(10):
                self.A[(m, j)] = [arb(fmpq(self.a_fr[canon(j, m, k)].numerator, self.a_fr[canon(j, m, k)].denominator)) for k in range(m, 26)]
        self.lam_c = 2*self.cl - 1

    # ---------- series machinery ----------
    @staticmethod
    def _directions(order):
        D = [(1, 0), (0, 1), (1, 1), (1, -1), (1, 2), (2, 1), (1, 3), (3, 1), (1, -2), (2, -1), (1, 4), (4, 1), (1, -3), (3, -1), (1, -4), (4, -1), (1, 5), (5, 1)]
        return D[:order+1]

    def phi_series(self, x0, y0, u, v, order):
        """Taylor coefficients (arb_series) of s -> phi(x0 + u s, y0 + v s) to the given order. x0,y0: arb; u,v: int."""
        N = order+1
        X = arb_series([x0, arb(u)], N); Y = arb_series([y0, arb(v)], N)
        q = X*X + Y*Y; R = q + 1; t = q/R; logR = R.log()
        # H_m = Re (X+iY)^{2m}: iterate Z^2 = (X^2 - Y^2) + i 2XY, then powers
        re2 = X*X - Y*Y; im2 = 2*X*Y            # Z^2
        H = [arb_series([1], N)]
        pre, pim = arb_series([1], N), arb_series([0], N)
        for m in range(1, 10):
            pre, pim = pre*re2 - pim*im2, pre*im2 + pim*re2
            H.append(pre)
        # powers of t
        tp = [arb_series([1], N)]
        for k in range(1, 26): tp.append(tp[-1]*t)
        total = arb_series([0], N)
        for j in range(4):
            for m in range(10):
                coeffs = self.A[(m, j)]
                G = arb_series([0], N)
                for i, c in enumerate(coeffs):
                    if not c.is_zero(): G = G + tp[i]*c
                fac = ((self.p[j]-m)*logR).exp()
                total = total + H[m]*fac*G
        return total

    def phi_jet(self, x0, y0, order=5):
        """Dictionary {(a,b): d^a_x d^b_y phi (x0,y0)} for a+b <= order (arb)."""
        x0 = arb(x0) if not isinstance(x0, arb) else x0
        y0 = arb(y0) if not isinstance(y0, arb) else y0
        D = self._directions(order)
        series = [self.phi_series(x0, y0, u, v, order) for (u, v) in D]
        coef = [[s[d] for d in range(order+1)] for s in series]   # coef[i][d]: degree-d coefficient along direction i
        jet = {(0, 0): coef[0][0]}
        for d in range(1, order+1):
            # unknowns T_{a,b} = d^a_x d^b_y phi/(a! b!), a+b = d, a = d..0; equations sum_a T_{a,d-a} u^a v^(d-a) = coef[i][d]
            dirs = D[:d+1]
            M = fmpq_mat([[fmpq(u)**a * fmpq(v)**(d-a) for a in range(d, -1, -1)] for (u, v) in dirs])
            Minv = M.inv()
            rhs = [coef[i][d] for i in range(d+1)]
            for row, a in enumerate(range(d, -1, -1)):
                val = arb(0)
                for col in range(d+1):
                    val += arb(Minv[row, col])*rhs[col]
                b = d-a
                jet[(a, b)] = val*math.factorial(a)*math.factorial(b)
        return jet

    def fields(self, x0, y0, order=5):
        """phi jet plus the physical fields at (x0,y0): psi, U=(U1,U2), rho, grad rho, V = cl X + U, F = V.grad rho - rho,
        DU (2x2), Drho Hessian (needs order>=5). Returns dict of arb."""
        x0 = arb(x0) if not isinstance(x0, arb) else x0
        y0 = arb(y0) if not isinstance(y0, arb) else y0
        J = self.phi_jet(x0, y0, order)
        def P(a, b): return J[(a, b)]
        out = {'phi': P(0, 0), 'psi': P(1, 1), 'psi_x': P(2, 1), 'psi_y': P(1, 2), 'psi_xy': P(2, 2)}
        out['U1'] = -P(1, 2); out['U2'] = P(2, 1)
        out['rho'] = -(P(2, 1) + P(0, 3))
        out['rho_x'] = -(P(3, 1) + P(1, 3)); out['rho_y'] = -(P(2, 2) + P(0, 4))
        out['V1'] = self.cl*x0 + out['U1']; out['V2'] = self.cl*y0 + out['U2']
        out['F'] = out['V1']*out['rho_x'] + out['V2']*out['rho_y'] - out['rho']
        # DU = [[d_x U1, d_y U1],[d_x U2, d_y U2]] = [[-phi_xxyy, -phi_xyyy],[phi_xxxy, phi_xxyy]]
        out['DU'] = [[-P(2, 2), -P(1, 3)], [P(3, 1), P(2, 2)]]
        if order >= 5:
            out['rho_xx'] = -(P(4, 1) + P(2, 3)); out['rho_xy'] = -(P(3, 2) + P(1, 4)); out['rho_yy'] = -(P(2, 3) + P(0, 5))
        return out


# ---------------- T1 (internal Legendre) representation: O(1) coefficients, suitable for box enclosures ----------------
LOW_T1 = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]
HIGH_T1 = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]

def legendre_series_list(z, nmax):
    """P_n(z) for n = 0..nmax as arb_series (z an arb_series)."""
    N = len(z)
    P = [arb_series([1], N), z]
    for n in range(1, nmax):
        P.append((P[n]*z*(2*n+1) - P[n-1]*n)/(n+1))
    return P

def load_T1(self, json_path):
    """Load internal coordinates (exact binary64 low chart without a_000, exact a_000 rational, binary64 high) from the checkpoint JSON."""
    import json as _json
    d = _json.load(open(json_path))
    low = [Fr(float.fromhex(h)) for h in d['P_hex']]      # low[0] is cl: replace by a_000
    num, den = d['input_exact_for_checkpoint']['a000_exact'].split('/')
    low[0] = Fr(int(num), int(den))
    high = [Fr(float.fromhex(h)) for h in d['high_hex']]
    NN = [Fr(float.fromhex(h)) for h in d['frozen_Nn_hex']]
    ctx.prec = self.prec
    def A(fr): return arb(fmpq(fr.numerator, fr.denominator))
    self.low_T1 = {}
    for v, (m, k, j) in zip(low, LOW_T1): self.low_T1.setdefault((m, j), {})[k-m] = A(v)
    self.high_T1 = {}
    for v, (m, n, j) in zip(high, HIGH_T1): self.high_T1.setdefault((m, j), {})[n] = A(v*NN[n])
    self.has_T1 = True

def phi_series_T1(self, x0, y0, u, v, order):
    """Same as phi_series but in the T1 representation: phi = sum_{m,j} H_m R^{p_j-m} [ sum_{h<=4-m} c_{m,m+h,j} t^h + t^{max(5-m,0)} sum_n g_{mnj} N_n P_n(2t-1) ]."""
    N = order+1
    X = arb_series([x0, arb(u)], N); Y = arb_series([y0, arb(v)], N)
    q = X*X + Y*Y; R = q + 1; t = q/R; logR = R.log(); z = t*2 - 1
    re2 = X*X - Y*Y; im2 = 2*X*Y
    H = [arb_series([1], N)]
    pre, pim = arb_series([1], N), arb_series([0], N)
    for m in range(1, 10):
        pre, pim = pre*re2 - pim*im2, pre*im2 + pim*re2
        H.append(pre)
    tp = [arb_series([1], N)]
    for k in range(1, 6): tp.append(tp[-1]*t)
    P = legendre_series_list(z, 20)
    total = arb_series([0], N)
    for j in range(4):
        for m in range(10):
            G = arb_series([0], N)
            for h, c in self.low_T1.get((m, j), {}).items(): G = G + tp[h]*c
            w = max(5-m, 0)
            Lsum = arb_series([0], N)
            for n, c in self.high_T1.get((m, j), {}).items(): Lsum = Lsum + P[n]*c
            G = G + tp[w]*Lsum
            fac = ((self.p[j]-m)*logR).exp()
            total = total + H[m]*fac*G
    return total

State.load_T1 = load_T1
State.phi_series_T1 = phi_series_T1
_orig_phi_jet = State.phi_jet
def phi_jet(self, x0, y0, order=5, rep='canonical'):
    if ctx.cap < order+1: ctx.cap = order+1
    x0 = arb(x0) if not isinstance(x0, arb) else x0
    y0 = arb(y0) if not isinstance(y0, arb) else y0
    D = self._directions(order)
    fn = self.phi_series_T1 if rep == 'T1' else self.phi_series
    series = [fn(x0, y0, u, v, order) for (u, v) in D]
    coef = [[s[d] for d in range(order+1)] for s in series]
    jet = {(0, 0): coef[0][0]}
    for d in range(1, order+1):
        dirs = D[:d+1]
        M = fmpq_mat([[fmpq(u)**a * fmpq(v)**(d-a) for a in range(d, -1, -1)] for (u, v) in dirs])
        Minv = M.inv()
        rhs = [coef[i][d] for i in range(d+1)]
        for row, a in enumerate(range(d, -1, -1)):
            val = arb(0)
            for col in range(d+1): val += arb(Minv[row, col])*rhs[col]
            jet[(a, d-a)] = val*math.factorial(a)*math.factorial(d-a)
    return jet
State.phi_jet = phi_jet
_orig_fields = State.fields
def fields(self, x0, y0, order=5, rep='canonical'):
    x0 = arb(x0) if not isinstance(x0, arb) else x0
    y0 = arb(y0) if not isinstance(y0, arb) else y0
    J = self.phi_jet(x0, y0, order, rep)
    def P(a, b): return J[(a, b)]
    out = {'phi': P(0, 0), 'psi': P(1, 1), 'psi_x': P(2, 1), 'psi_y': P(1, 2), 'psi_xy': P(2, 2)}
    out['U1'] = -P(1, 2); out['U2'] = P(2, 1)
    out['rho'] = -(P(2, 1) + P(0, 3))
    out['rho_x'] = -(P(3, 1) + P(1, 3)); out['rho_y'] = -(P(2, 2) + P(0, 4))
    out['V1'] = self.cl*x0 + out['U1']; out['V2'] = self.cl*y0 + out['U2']
    out['F'] = out['V1']*out['rho_x'] + out['V2']*out['rho_y'] - out['rho']
    out['DU'] = [[-P(2, 2), -P(1, 3)], [P(3, 1), P(2, 2)]]
    if order >= 5:
        out['rho_xx'] = -(P(4, 1) + P(2, 3)); out['rho_xy'] = -(P(3, 2) + P(1, 4)); out['rho_yy'] = -(P(2, 3) + P(0, 5))
    return out
State.fields = fields

if __name__ == '__main__':
    import sys, time
    S = State(sys.argv[1], prec=256)
    t0 = time.time()
    f0 = S.fields(0, 0, order=5)
    print('time one point', time.time()-t0)
    print('rho_y(0) = a0 :', f0['rho_y'])
    print('psi_xy(0) = c[rho]:', f0['psi_xy'], ' cl + c - 1 =', S.cl + f0['psi_xy'] - 1)
    print('F(0)', f0['F'], 'rho(0)', f0['rho'], 'U(0)', f0['U1'], f0['U2'])
    print('DU(0):', f0['DU'])
    print('lambda = 2cl-1 =', S.lam_c)
    for (x, y) in [(0, 74.3), (0, 50), (5, 5), (0.01, 0.02), (100, 0), (0, 1e6)]:
        t0 = time.time(); f = S.fields(x, y, order=4); dt = time.time()-t0
        aref = 23.95065822465609
        print((x, y), 'F=', f['F'].str(10), 'R_f=F/y=', (f['F']/arb(y)).str(10) if y else 'n/a', 'E_f=', (f['F']/arb(y)/aref).str(8) if y else 'n/a', 'rho=', f['rho'].str(8), 't=%.3f' % dt)
