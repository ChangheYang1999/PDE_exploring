# Scope of spectral and source-point diagnostics of the stored directions

Date: 2026-10-20. Status: exact statements below; numerical evaluation is separate.

## Statement and notation

Let 0 <= q <= 1, 0 <= s <= pi/2, and theta = s + beta sin(2s)/2 with |beta| < 1. For finite N and M write

    b(q,theta) = sum_{n=0}^N sum_{m=0}^{M-1} a_nm T_n(2q-1) cos(2m s(theta)).

For L>0 and k<1 let q(r)=1-(1+r^2/L^2)^(-(1-k)/2). Stored variations have the same finite representation. Their plain nodal energy means the sum of squared stored delta-b entries, without a physical-area weight and without a relative-density weight. Coefficient energy means sum |a_nm|^2. Neither energy is a Sobolev norm or a physical-space norm.

1. Every such finite representation is real analytic in Cartesian coordinates in a neighbourhood of a point P=(x*,0), x*>0. This says nothing about uniform regularity of a sequence with increasing N,M.
2. Small relative energy in the upper third of a finite Chebyshev spectrum does not imply bounded second derivatives or convergence in C^2. It therefore cannot by itself rule out a limiting singular direction or a sequence of approximate kernel vectors in a stronger norm.
3. Pointwise second differences at finitely many positive steps cannot certify the absence of a smaller-scale singular limit. The second difference can instead be checked against the exact second derivative of each fixed interpolant; this is a diagnostic of that interpolant only.
4. Fractions of plain nodal energy near P or in r>100 are valid only for the specified nodes and variable delta-b. A point at q=1 is an asymptotic coefficient datum, not a physical point of finite radius. An unweighted nodal fraction including that point is not a spatial localization theorem.

## Proof

The map s -> theta is analytic and has derivative 1+beta cos(2s)>=1-|beta|>0. Its inverse is analytic locally. Near theta=0 its inverse is odd, so cos(2m s(theta)) is even analytic in theta. Near P choose the analytic signed angle theta=arctan(y/x) and r=(x^2+y^2)^(1/2), with x>0. The angular evenness gives the same values as the parity-reflected quadrant formula. The radial map is analytic there. Finite sums and products preserve analyticity. The density factor x^2 y (1+r^2/L^2)^((k-3)/2), and its parameter derivatives with respect to k, are also analytic near P. This proves item1, without any uniform bound in N,M.

For item2 take even N>=2 and f_N(z)=1+N^(-1)T_N(z) on [-1,1]. The upper-third coefficient energy divided by the total is 1/(N^2+1), tending to zero; the functions even converge uniformly to1. Yet the Chebyshev differential equation

    (1-z^2)T_N'' - z T_N' + N^2 T_N = 0

at z=0 gives T_N''(0)=-N^2(-1)^(N/2), so |f_N''(0)|=N. Thus no second-derivative bound follows from this energy diagnostic. This example already uses analytic functions and an interior point. It does not claim that the stored IPM directions behave this way; it disproves the proposed inference from the diagnostic alone.

For a separate example of a nonsmooth limit of analytic functions, fix a noninteger p in (2,3), a real coordinate z through P, and set g_eps(z)=(z^2+eps^2)^(p/2), eps>0. Each is real analytic. It converges in C^2 on every compact interval to |z|^p, which is not C^3. To check C^2 convergence, differentiate twice explicitly. In |z|<=eps the differences of derivatives of order j<=2 are O(eps^(p-j)); outside this interval the rescaled formula and the mean value theorem give uniform errors O(eps^2) for j=0 and O(eps^(p-j)) for j=1,2, with constants depending on p and the interval. Each error tends to zero. For any fixed h>0, the centered second differences converge to those of |z|^p. A finite collection of such measurements therefore does not distinguish a smooth approximant from a nonsmooth limit. This proves item3's scope statement.

For practical exact differentiation, put a=(1-k)/2 and B=1+x^2/L^2 on the positive axis. Then

    q' = 2a x L^(-2) B^(-a-1),
    q'' = 2a L^(-2) B^(-a-1) - 4a(a+1)x^2 L^(-4)B^(-a-2).

If F(z)=sum_n (sum_m a_nm)T_n(z), the axis variation is F(2q(x)-1) and

    d_x^2 b = 4(q')^2 F''(2q-1) + 2q'' F'(2q-1).

This follows by two applications of the chain rule. It provides a derivative formula independent of finite differences.

Finally a plain nodal sum assigns the same weight to every grid entry, including q=1. The coordinate transformation has a nonconstant Jacobian and r(q)->infinity as q->1. No change-of-variables formula identifies that sum with area measure; replacing delta-b by relative density also changes the integrand. Hence item4 follows directly from the definition of the reported fractions.

## Dependencies and scope

Only elementary analytic inversion, Chebyshev polynomials and differentiation are used. The finite representation and independent reconstruction are specified in ../inverse/PROOF.md and its collocation.py evaluator. The continuum-kernel inference remains subject to ../crossgrid-actions/PROOF.md. This note neither constructs nor excludes an IPM kernel or nonlinear profile family, and makes no claim of smoothness at the center r=0.

Numerical checks must freeze the input vectors, state and reported JSON, reconstruct the coefficients independently, and compare the fixed interpolant's second differences with the derivative above. Their evidence belongs in verification/.
