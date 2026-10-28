"""Ball jets of phi over a box via radial Taylor models and equispaced directional series (DFT-conditioned solve).

For X0 in the box B (ball coordinates xb, yb) and a direction e = (cos t, sin t), the series s -> phi(X0 + s e) is computed with the RTM
(rtm.RTMState.radial_model: Taylor coefficients at q_c, Cauchy tail bounds) and ball coordinates, to order N. Its degree-d coefficient is
P_d(e) = sum_{a+b=d} T_{ab} cos^a t sin^b t with T_{ab} = d^a_x d^b_y phi(X0)/(a! b!). Sampling M = 2N+2 equispaced angles t_k = pi k / M
(k = 0..M-1) and solving the normal equations (M x (d+1) matrix of monomials cos^a sin^b) gives balls for T_{ab} containing the true values
for every X0 in B. The normal matrix is well conditioned (about 4^d), unlike integer-slope Vandermonde systems.
Output: dict (a,b) -> arb ball containing d^a_x d^b_y phi(X0) for all X0 in B, for all a+b <= N.
"""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import arb, arb_series, arb_mat, ctx, fmpq
from rtm import RTMState, _arb_fr

def box_phi_series_dir(S, xb, yb, cu, su, N, models, q_c):
    """series of phi along the arb direction (cu, su) from ball coordinates (cu, su arb)."""
    X = arb_series([xb, cu], N+1); Y = arb_series([yb, su], N+1)
    q = X*X + Y*Y
    eps = q - q_c; eps0 = eps[0]; Delta = eps - eps0
    re2 = X*X - Y*Y; im2 = 2*X*Y
    H = [arb_series([1], N+1)]
    pre, pim = arb_series([1], N+1), arb_series([0], N+1)
    for m in range(1, 10):
        pre, pim = pre*re2 - pim*im2, pre*im2 + pim*re2
        H.append(pre)
    Dp = [arb_series([1], N+1)]
    for n in range(1, N+1): Dp.append(Dp[-1]*Delta)
    total = arb_series([0], N+1)
    for (m, j), (gd, taus) in models.items():
        P = arb_series([0], N+1)
        for c in reversed(gd): P = P*eps + c
        Tail = arb_series([0], N+1)
        for n in range(N+1):
            tb = taus[n]/math.factorial(n)
            Tail = Tail + Dp[n]*arb(0, float(tb.upper()) if float(tb.upper()) > 0 else 5e-324)
        total = total + H[m]*(P + Tail)
    return total

def ball_jet(S, x_c, y_c, hx, hy, N, D=60):
    ctx.prec = S.prec
    ctx.cap = max(ctx.cap, D+1, N+2)
    xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); hxA = _arb_fr(Fr(hx)); hyA = _arb_fr(Fr(hy))
    xb = xc + arb(0, float(hxA.upper())); yb = yc + arb(0, float(hyA.upper()))
    q_c = xc*xc + yc*yc
    eps0 = xb*xb + yb*yb - q_c; delta = arb(abs(eps0).upper())
    models = {key: S.radial_model(key[0], key[1], q_c, delta, D, N) for key in S.A}
    M = 2*N + 2
    angles = [arb(math.pi)*k/M for k in range(M)]
    cs = [(t.cos(), t.sin()) for t in angles]
    series = [box_phi_series_dir(S, xb, yb, cu, su, N, models, q_c) for (cu, su) in cs]
    jet = {}
    for d in range(N+1):
        # A (M x (d+1)): A[k, a] = cos^a sin^(d-a); b[k] = series_k[d]
        A = arb_mat(M, d+1); b = arb_mat(M, 1)
        for k, (cu, su) in enumerate(cs):
            cp = [arb(1)]; sp = [arb(1)]
            for i in range(d): cp.append(cp[-1]*cu); sp.append(sp[-1]*su)
            for a in range(d+1): A[k, a] = cp[a]*sp[d-a]
            b[k, 0] = series[k][d]
        At = A.transpose()
        T = (At*A).solve(At*b)
        for a in range(d+1):
            jet[(a, d-a)] = T[a, 0]*math.factorial(a)*math.factorial(d-a)
    return jet, xb, yb

if __name__ == '__main__':
    import time
    from cert_M import cell_box
    S = RTMState(sys.argv[1], prec=256)
    for (r_lo, t_lo) in [(0.3, 1.0), (3.0, 0.3), (30.0, 1.5)]:
        xc, yc, hx, hy = cell_box(r_lo, r_lo*1.02, t_lo, t_lo + math.pi/160)
        t0 = time.time(); J, xb, yb = ball_jet(S, xc, yc, hx, hy, N=13); dt = time.time()-t0
        Jc = S.phi_jet(_arb_fr(Fr(xc)), _arb_fr(Fr(yc)), 13)
        print('cell r=%g: %.2fs; ratios (ball upper)/|center value| at orders 4, 9, 13:' % (r_lo, dt))
        for d in (4, 9, 13):
            print('   order %d:' % d, ['%.1f' % (float(abs(J[(a, d-a)]).upper())/max(abs(float(Jc[(a, d-a)].mid())), 1e-300)) for a in range(d+1)])
