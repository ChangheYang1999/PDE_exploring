# Small rotational defect with uniform compactness assumptions

## Statement

Write S=(DU+DU^T)/2 and L U=(Jy dot grad)U-JU. First, for any c>0 and any real omega, a bounded C2 divergence-free Euler profile is constant if

    lambda_max(S(y))<1 whenever |y|<=sup|U|/c.

Second, fix 0<c1<=c2<1/2, 0<alpha<=1, M>0 and eta:[0,infinity)->(0,infinity) with eta(r)->0. There exists epsilon>0 depending only on these fixed data such that every C2 Euler profile with

    c in [c1,c2],  ||U||_C1,alpha<=M,
    |U(y)|<=eta(|y|),
    |omega| sup_y |L U(y)|/(1+|y|)<=epsilon

vanishes. The norm is understood to control sup|U| and sup|DU| by M. No explicit value of epsilon is claimed.

## The strain criterion

Let m=sup|U|. If m=0 the assertion is immediate. Compactness and continuity give delta>0 and theta>0 such that lambda_max S<=1-theta on the closed ball of radius m/c+delta. This ball is backward invariant because

    B(y) dot y >= |y|(c|y|-m)>0

on its boundary. Every backward orbit enters it in finite time: outside it the backward radial derivative is at most -c delta. On this ball vorticity transport gives

    d/dt |Omega(Phi_t x)|^2
       =2 Omega dot (S-I)Omega <= -2 theta |Omega(Phi_t x)|^2.

Apply this forward inequality from Phi_-T x to a fixed backward point after entry. The starting vorticity is uniformly bounded on the compact ball, while the factor exp(-theta T) tends to zero. Thus Omega vanishes at the fixed point and, by invertible transport, at x. Since x was arbitrary, Omega=0; bounded harmonic Liouville makes U constant.

## Compactness argument

If the second conclusion fails, choose nonzero profiles U_n with defects tending to zero. Passing to a subsequence gives c_n->c* in [c1,c2] and U_n->U0 in C1 on every compact set, by the uniform Holder modulus. The exact equation is

    grad P_n=omega_n L U_n-(1-c_n)U_n-(c_n y+U_n) dot grad U_n.

Its right side converges locally uniformly to

    G=-(1-c*)U0-(c* y+U0) dot grad U0.

A locally uniform limit of gradients is a gradient on R3: normalize the potentials at the origin, integrate on line segments, and pass to limits in path integrals. Consequently G=grad P0 with P0 in C1. The limit U0 is C1, divergence-free, decays by the common envelope, and solves the nonrotating equation. The C1 nonrotating Liouville theorem audited in A010 gives U0=0.

To deduce global uniform convergence, use the tail envelope

    eta_star(R)=sup_{s>=R}eta(s),

which tends to zero for sufficiently large R. On |y|>=R, |U_n|<=eta_star(R), and on the ball U_n->0 uniformly. Hence m_n=sup|U_n|->0. Also DU_n->0 uniformly on the unit ball. For all sufficiently large n, m_n/c_n<1 and lambda_max S_n<1 on that ball. The strain criterion forces U_n constant, and the common decay envelope forces that constant to be zero, a contradiction.

Finally |L U|<=(1+|y|)M, so |omega|<=epsilon/M suffices. The defect condition also covers large omega when the same compactness assumptions and sufficiently small L U hold.

## Scope and dependencies

This is a compact-family perturbative theorem, not an arbitrary-rotation Liouville theorem without extra bounds. No uniform decay envelope is deduced from individual decay, and no explicit rotation threshold is computed. The proof corrects the coordinator's use of eta(R) outside a ball: eta need not be monotone, so eta_star is required. Dependencies are A002/A006, A010, Arzela-Ascoli, and bounded harmonic Liouville. CO8 and CO8a are CONFIRMED with this minor proof correction.

## Strengthening: no common decay modulus (LIT21, A102)

Fix 0<c1<=c2<1/2, 0<alpha<=1 and M>0. There is an epsilon depending only on these data such that every bounded C2 exact rotating Euler profile with c in [c1,c2], global C^{1,alpha} norm at most M, and

    |omega| sup_y |L U(y)|/(1+|y|)<=epsilon

is constant. The norm here is sup|U|+sup|DU|+[DU]_alpha, using Euclidean and induced operator norms. Individual decay at infinity then makes this constant zero. No decay assumption is required for the constant conclusion.

Suppose otherwise and take nonconstant profiles with defects tending to zero. The compactness and pressure argument above still gives a bounded C1 nonrotating limit U0 with c* in [c1,c2]. A010 makes this limit a constant vector b, which need not be zero. Choose the fixed radius R=M/c1+1. Local C1 convergence implies sup_{|y|<=R}|DU_n(y)| tends to zero. For all sufficiently large n this supremum is below 1/2 and R>sup|U_n|/c_n. The already proved strain criterion therefore makes U_n constant, a contradiction.

This strengthens, rather than contradicts, the earlier theorem. Global convergence of U_n and preservation of decay are unnecessary. It also yields a uniform small-rotation result because |L U(y)|<=M(1+|y|). Neither the threshold nor a theorem without the uniform derivative modulus has been proved.

Audit date: 2026-11-02T19:35:29Z. Source: in the team records.
