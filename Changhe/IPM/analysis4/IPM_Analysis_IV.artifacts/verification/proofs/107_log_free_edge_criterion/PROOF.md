# Rational edge convergence with log-independent low factors

Status: PROVED. The theory part independently reviewed and adopted this proof; the final transcription was checked in V207 and V208. This is a sufficient condition for the modified edge recurrence. It does not settle the unrestricted stationary nonlinear recurrence.

## Statement and notation

Let delta=a/b in (0,1) be reduced, c=(1-delta)^(-1), and let F_1 be a nonzero finite real odd sine polynomial of highest frequency L. Fix an integer K>=1. Use the canonical stationary polynomial-log recursion, retaining exactly the ordered pairs (i,j) with i+j=n and min(i,j)<=K. Count every ordered pair once. At Poisson resonance set the entire resonant stream constant to zero.

Assume that every density F_i and stream G_i with 1<=i<=K is independent of t=log r. Then all density, stream, velocity and compatible potential series converge in a sufficiently distant exterior with every fixed natural weighted derivative. Their sums are real analytic and satisfy the modified edge equation.

In particular the hypothesis holds whenever K delta<4. It therefore holds for K=1 at every rational delta in (0,1), and for K=1,2,3,4,5 at delta=2/3. This is a sufficient range only. At a first possible resonance the actual obstruction can vanish, so the strict inequality is not a necessary condition.

## Quantitative constants

Put

    d_*=gcd(a,2)/b, s=2/d_*, C_P=2/d_*, B=L+1,
    ||H||_s=sum_(q>=0) q!s^q||[t^q]H||_(angular l1),
    p_i=1-i delta, P_i=2-i delta,
    H_i=||F_i||_(angular l1), Q_i=||G_i||_(angular l1), i<=K.

For each retained low index define

    b_i = 4B/[3(c-1)] * {
              [|P_i|+i(1+d_*/4)] Q_i
              + C_P[(2-delta+d_*/4)i+|p_i|] H_i }.

Choose

    A=max(1, 2 sum_(i=1)^K b_i),
    C_0=max_(1<=n<=2K) ||F_n||_s A^(-n).

Then, for every n>=1,

    ||F_n||_s <= C_0 A^n,
    ||G_n||_s <= C_P C_0 A^n.                    (1)

Every exterior radius R>A^(1/delta) is sufficient for the stated convergence. These coarse constants are not optimal; topic106 gives much smaller constants for the unit-sine K1 and K3 cases at delta2/3.

## Uniform inverse bounds

Since d_*<=delta and ||D||_s<=1/s=d_*/2, the scalar stationary inverse satisfies

    ||((n-1)(c-1)-cD)^(-1)||
       <= 1/[(c-1)(n-3/2)], n>=2.              (2)

Indeed c d_*/2<=c delta/2=(c-1)/2, and the finite polynomial Neumann series is bounded by this positive denominator.

Every nonzero Poisson shift is at least d_* in modulus. Thus its inverse norm is at most1/(d_*-1/s)=2/d_*=C_P. The zero shift is integration from zero, of norm s=C_P. The two angular incidences each have factor1/2, and the canonical deletion of a resonant constant contracts the norm. Consequently

    ||G_n||_s <= C_P ||F_n||_s.                  (3)

This proof includes all resonances. It uses the canonical whole-mode normalization, not a nonresonant-only formula.

## The linear tail inequality

Angular support induction gives maxfreq(F_j)<=Bj-1 and maxfreq(G_j)<=Bj. Set M_j=||F_j||_s and N_j=||G_j||_s.

For n>2K, each retained ordered pair has exactly one index i<=K. Write j=n-i>K. Thus j>=2, and the two orientations are distinct. Since the low factors have no t dependence, their multiplication is bounded column by column in this norm. The two ordered forcing terms satisfy

    ||P_i G_i F_j' - G_i'(p_j+D)F_j||_s
       <= B j [|P_i|+i(1+d_*/4)] Q_i M_j,       (4)

    ||(P_j+D)G_j F_i' - G_j' p_i F_i||_s
       <= B j [(2-delta+d_*/4)i+|p_i|] H_i N_j. (5)

To check these inequalities, use |p_j|<=j and |P_j|<=(2-delta)j for j>=1, together with d_*/2<=j d_*/4 for j>=2. Bound angular derivatives by Bj for high factors and Bi for low factors. No derivative in t falls on a low factor.

Use (3) in (5), sum (4)-(5), and apply (2). Since n>=3 and j<=n-1,

    j/(n-3/2) <= (n-1)/(n-3/2) <= 4/3.

It follows that

    M_n <= sum_(i=1)^K b_i M_(n-i), n>2K.      (6)

This finite-memory bound has constants independent of n. It is the point where the log-independence hypothesis is used. Multiplication of two general log polynomials need not be bounded in this factorial norm.

## Geometric induction

The definition of A gives A>=1 and

    sum_(i=1)^K b_i A^(-i)
       <= (sum_(i=1)^K b_i)/A <= 1/2.

The finite first2K coefficients obey (1) by the definition of C_0. For n>2K, substituting the induction hypotheses into (6) gives M_n<=C_0 A^n/2, and hence (1). Equation (3) gives the stream bound.

Factorial weights give ||H(t)||<=exp(|t|/s)||H||_s. Together with the linear angular support bound, (1) proves absolute exterior convergence whenever A R^(-delta)<1. The factor exp(|log r|/s) is absorbed by all sufficiently late radial powers, and finitely many early terms are treated individually. Every fixed derivative costs only a polynomial in n and fixed constants. A small complex angular strip and local complex logarithm can be included within the same strict geometric margin.

The joint potential reconstruction uses only the linear identities relating potential, density and stream. Its bound from topic41 remains valid here because ||D||_s=d_*/2<=1. It adds a polynomial factor in n to the geometric coefficient bounds, apart from finitely many explicitly solvable early orders. Thus the potential and all requested derivatives converge too.

Writing rho_<=K and u_<=K for the finite low-order sums, termwise regrouping gives exactly

    (c x dot grad-1)rho + u_<=K dot grad rho
       +u dot grad rho_<=K-u_<=K dot grad rho_<=K=0.

This is the modified equation. No equality with the complete nonlinear stationary equation is claimed.

## Why K delta<4 is sufficient

The stream sine frequencies are positive even integers q>=2. At positive order i the radial stream exponent is P_i=2-i delta<2. A genuine stream resonance therefore requires P_i=-q and i delta=q+2>=4. A zero-frequency channel is absent by symmetry.

If K delta<4, induction through i=K has no genuine stream resonance. Starting from the log-independent F_1, the density forcing is then log-independent, the unique stationary polynomial inverse remains constant in t, and the nonresonant stream inverse remains constant in t. Thus every low F_i,G_i is log-independent, as required. Possible earlier logarithms in a potential representation do not affect this argument, which uses only density and stream.

## Dependencies and limits

The canonical recurrence and resonance conventions are topics01,10 and17. Topic89 supplies the factorial Poisson bound, repeated above. Topic41 supplies the linear potential reconstruction. Topic106 verifies sharper constants and exact finite examples. The present proof applies to every rational parameter under the stated low-factor hypothesis; no uniform statement in delta, no irrational extension, and no necessity claim is made.
