"""Per-circle 1D optimal transport costs for the far-field measure (upper-bound blueprint).
On the circle |z - m| = rho (m = e1/2, beta = pi/4 kernel K(z) = z1 z2/(pi|z|^4)), the density of k = K(.-e1) - K(.) w.r.t.
d(theta) is mu(theta) = k(m + rho e^{i theta}) rho.  It has zero mean (odd in theta).  We compute, by a discrete LP on n points,
  W1(rho) = min_plan sum pi_ij c_ij, c_ij = (2 rho |sin((th_i - th_j)/2)|)^alpha   (exact 1D OT cost, heuristic discretisation)
and compare with: (a) the lead's (1/2) osc bound (1/2) int |mu| (2 rho)^alpha, (b) the antipodal plan int_{mu>0} mu (2 rho)^alpha,
(c) the reflection plan across the axis theta -> -theta: int_{mu>0} mu (2 rho |sin theta|)^alpha,
(d) the asymptotic n=3 extremal value 2 a_3(alpha) rho^(alpha-2) * rho (per unit rho) for the dipole approximation.
Prints per-circle costs and the integral over rho in [1, R] (log-spaced quadrature) of each."""
import numpy as np, sys
from scipy.optimize import linprog
from scipy.integrate import quad
def K(x, y): return x*y/(np.pi*(x*x + y*y)**2)
def mu_circle(rho, th): 
    z1 = 0.5 + rho*np.cos(th); z2 = rho*np.sin(th)
    return (K(z1 - 1, z2) - K(z1, z2))*rho
def ot_cost(rho, alpha, n=360):
    th = (np.arange(n) + 0.5)*2*np.pi/n; dth = 2*np.pi/n
    mu = mu_circle(rho, th)*dth
    mu -= mu.mean()   # exact zero mean (odd), remove discretisation drift
    P = np.nonzero(mu > 0)[0]; N = np.nonzero(mu < 0)[0]
    a = mu[P]; b = -mu[N]
    s = min(a.sum(), b.sum()); a = a*s/a.sum(); b = b*s/b.sum()
    C = (2*rho*np.abs(np.sin((th[P][:, None] - th[N][None, :])/2)))**alpha
    nP, nN = len(P), len(N)
    # LP: variables pi (nP*nN), row sums = a, col sums = b
    from scipy.sparse import lil_matrix, csr_matrix, kron, identity, eye
    A1 = kron(identity(nP), np.ones((1, nN)))           # row sums
    A2 = kron(np.ones((1, nP)), identity(nN))           # col sums
    from scipy.sparse import vstack
    A = vstack([A1, A2]).tocsr()
    res = linprog(C.ravel(), A_eq=A, b_eq=np.concatenate([a, b]), bounds=(0, None), method='highs')
    return res.fun, np.abs(mu).sum()
def plans(rho, alpha, n=2000):
    th = (np.arange(n) + 0.5)*2*np.pi/n; dth = 2*np.pi/n
    mu = mu_circle(rho, th)*dth
    pos = mu > 0
    half_osc = 0.5*np.abs(mu).sum()*(2*rho)**alpha
    antipodal = mu[pos].sum()*(2*rho)**alpha
    refl = (mu[pos]*(2*rho*np.abs(np.sin(th[pos])))**alpha).sum()
    return half_osc, antipodal, refl
if __name__ == "__main__":
    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    a3 = 3/np.pi*quad(lambda t: np.sin(3*t)*(2*np.sin(t))**alpha, 0, np.pi/6)[0]
    print(f"alpha = {alpha}: per-circle costs (per unit rho); dipole asymptote 2 a_3 rho^(alpha-2) with a_3 = {a3:.5f}")
    print(f"{'rho':>8} {'OT (LP)':>10} {'(1/2)osc':>10} {'antipodal':>10} {'reflect':>10} {'dipole':>10} {'|mu|_1':>8}")
    rows = []
    for rho in [1.0, 1.25, 1.5, 2, 3, 5, 10, 30, 100, 1000]:
        w, m1 = ot_cost(rho, alpha); ho, an, re = plans(rho, alpha)
        rows.append((rho, w, ho, an, re))
        print(f"{rho:8.2f} {w:10.5f} {ho:10.5f} {an:10.5f} {re:10.5f} {2*a3*rho**(alpha-2):10.5f} {m1:8.4f}")

# ---- explicit plan: split each positive lobe and match anti-monotonically with the adjacent negative lobes
def lobe_plan_cost(rho, alpha, n=4000, split_opt=True):
    th = (np.arange(n) + 0.5)*2*np.pi/n; dth = 2*np.pi/n
    mu = mu_circle(rho, th)*dth
    sgn = np.sign(mu)
    # lobes: maximal runs of constant sign (cyclic); rotate so that a sign change is at index 0
    change = np.nonzero(sgn != np.roll(sgn, 1))[0]
    if len(change) == 0: return 0.0, 0
    k0 = change[0]; mu = np.roll(mu, -k0); th = np.roll(th, -k0); sgn = np.roll(sgn, -k0)
    change = np.nonzero(sgn != np.roll(sgn, 1))[0]
    bounds = list(change) + [n]
    lobes = [(bounds[i], bounds[i+1]) for i in range(len(bounds) - 1)]
    L = len(lobes)
    masses = np.array([mu[a:b].sum() for a, b in lobes])
    pos = [i for i in range(L) if masses[i] > 0]
    def cost_for(fracs):
        # fracs[j]: fraction of positive lobe pos[j] sent LEFT (to lobe i-1); rest goes right (to lobe i+1)
        total = 0.0
        for j, i in enumerate(pos):
            a, b = lobes[i]; s = fracs[j]
            m = mu[a:b]; cum = np.cumsum(m); mt = cum[-1]
            kL = np.searchsorted(cum, s*mt)                      # left part: indices a..a+kL
            # left part -> left neighbour lobe (i-1), anti-monotone: nearest-to-boundary pairs first
            for part, nb, rev in [((a, a + kL), lobes[(i - 1) % L], True), ((a + kL, b), lobes[(i + 1) % L], False)]:
                pa, pb = part
                if pb <= pa: continue
                src = mu[pa:pb]; sth = th[pa:pb]
                na, nbb = nb; dst = -mu[na:nbb]; dth_ = th[na:nbb]
                if rev:   # left part of positive lobe (near its left boundary) matched with the RIGHT end of the left lobe
                    src = src[::-1]; sth = sth[::-1]; dst = dst[::-1]; dth_ = dth_[::-1]
                # we only use the portion of the destination lobe adjacent to the boundary, in order; amounts: min(src total, available)
                # sequential greedy anti-monotone matching (both ordered from the shared boundary outward)
                i1 = i2 = 0; r1 = src[0] if len(src) else 0; r2 = dst[0] if len(dst) else 0
                # the destination lobe also receives mass from the other side; we take from its boundary-adjacent end first
                while i1 < len(src) and i2 < len(dst):
                    q = min(r1, r2)
                    d = 2*rho*abs(np.sin((sth[i1] - dth_[i2])/2))
                    total += q*d**alpha
                    r1 -= q; r2 -= q
                    if r1 <= 1e-18: i1 += 1; r1 = src[i1] if i1 < len(src) else 0
                    if r2 <= 1e-18: i2 += 1; r2 = dst[i2] if i2 < len(dst) else 0
        return total
    # balance: each negative lobe must receive exactly its mass: symmetric choice by solving the linear constraints with one free parameter
    # simple approach: choose fractions so that each negative lobe's inflow equals its mass; with alternating lobes the system is
    # (1 - s_j) m_{p_j} + s_{j+1} m_{p_{j+1}} = m_neg between them. Fix s_0 and solve forward; scan s_0 on a grid for the minimum.
    best = (np.inf, None)
    P = len(pos)
    for s0 in np.linspace(0.0, 1.0, 11) if split_opt else [0.5]:
        fr = [s0]
        ok = True
        for j in range(P - 1):
            i = pos[j]; neg = (i + 1) % L; nxt = pos[(j + 1) % P]
            s_next = (-masses[neg] - (1 - fr[j])*masses[i])/masses[nxt]
            fr.append(s_next)
            if not (-1e-9 <= s_next <= 1 + 1e-9): ok = False
        if not ok: continue
        fr = np.clip(fr, 0, 1)
        c = cost_for(fr)
        if c < best[0]: best = (c, fr)
    return best

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[2] == 'plan':
    alpha = float(sys.argv[1])
    print(f"\nexplicit adjacent-lobe anti-monotone plan vs LP optimum, alpha={alpha}")
    for rho in [1.0, 1.25, 1.5, 2, 3, 5, 10]:
        w, _ = ot_cost(rho, alpha)
        c, fr = lobe_plan_cost(rho, alpha)
        print(f"rho={rho:6.2f}: OT {w:.5f}  lobe plan {c:.5f}  ratio {c/w:.4f}  fractions {np.round(fr,3) if fr is not None else None}")
