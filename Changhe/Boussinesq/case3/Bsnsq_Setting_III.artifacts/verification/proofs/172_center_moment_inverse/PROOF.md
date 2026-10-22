# Full-plane harmonic moments and a stable local Poisson representation

Status: the identities below are proved. Proposed numerical implementations are diagnostics until tested. They do not constitute a B2 candidate or a full-class exclusion.

## Statement, assumptions and notation

Use (x,y)=(r sin phi,-r cos phi), U=(-Psi_y,Psi_x), Omega=-Delta Psi, and the canonical relative velocity V=U-U(0). Suppose Omega is a finite sine sum with radial coefficients h_n(r), n>=1. Assume the physical source is smooth near0, h_n(r)=O(r^n) there, and h_n(r)=O(r^-s) at infinity for a fixed s in(0,1). Away from0 local C4 regularity suffices for the differentiated formulas below. The relative full-plane inverse is the one in171; no harmonic polynomial may be appended.

For each n>=2 define the convergent harmonic moment

    M_n = int_0^infinity rho^(1-n) h_n(rho) d rho.

For r>0 define

    A_n(r)=int_0^1 z^(n+1) h_n(rz) dz,
    D_n(r)=int_0^1 z^(1-n) h_n(rz) dz.

If psi_n is the canonical stream coefficient, then exactly

    psi_n(r)/r = r^(n-1) M_n/(2n) + r[A_n(r)-D_n(r)]/(2n),
    psi_n'(r)  = r^(n-1) M_n/2 - r[A_n(r)+D_n(r)]/2.       (1)

The first term in each expression is the velocity contribution of the harmonic polynomial M_n r^n sin(n phi)/(2n). Once M_n is determined globally, both remaining integrals use only the source inside the radius r. In exact arithmetic (1) is the same canonical full-plane inverse as the direct Green formula. It is useful near0; for large r its two pieces can be individually large and cancel, so no uniform numerical stability claim is made.

For n=1 define A_1=int_0^1 z^2 h_1(rz)dz and C_1=int_0^1 h_1(rz)dz. Use psi_1/r=r(A_1-C_1)/2 and psi_1prime=-r(A_1+C_1)/2, the finite relative formulas proved in171. Both use only[0,r]. No exterior moment M_1 or difference of divergent integrals is used; M_1 need not converge for these slow tails.

## Proof

Near0 the moment integrand is O(rho), and near infinity it is O(rho^(1-n-s)). The latter is integrable for n>=2 and s>0. Thus M_n converges absolutely. Similarly the integrand defining D_n is O(z) at0, so D_n is finite.

The canonical regular Green expression in171 reads

    psi_n/r = r(A_n+B_n)/(2n),
    psi_n'  = r(-A_n+B_n)/2,
    B_n(r) = int_0^1 z^(n-3) h_n(r/z) dz
           = r^(n-2) int_r^infinity rho^(1-n)h_n(rho) d rho.

Split this genuinely convergent moment at r. The omitted inner portion is

    r^(n-2) int_0^r rho^(1-n)h_n(rho)d rho = D_n(r).

Therefore B_n=r^(n-2)M_n-D_n, which proves (1). Every integral split is absolutely justified. The global moment has not been chosen freely and is not fitted to the center conditions.

Near0, A_n,D_n=O(r^n), so

    psi_n(r) = M_n r^n/(2n) + O(r^(n+2)).                 (2)

For n=2, r^2 sin(2phi)=-2xy, so the B2 center strain is

    c=Psi_xy(0)=-M_2/2.                                  (3)

The n=1 relative coefficient starts at order r^3 and the modes n>=3 have no quadratic term, so they do not alter (3).

For the r2 archive source in171, assume b=beta_basis>1, L>0, degree5 with simple interior knots and endpoint-clamped knot vector 0^6, interior knots, 1^6 on[0,1]. The first floor(k/2) coefficients of each cosine mode are masked as in171; these conditions give smoothness near0 and local C4 regularity across each nonzero knot circle. They will be checked against every frozen archive. The complete decoding is Omega=x sum_k G_k(r)cos(k phi), with G_k=P_k(t)(1-t)^(b+1)chi_k, chi_k=1 for even k and r/sqrt(L^2+r^2) for odd k. The mask gives P_k=O(t^floor(k/2)) on the first cell, or zero there if all six first-cell coefficients are masked. Since t is analytic in r^2, h_n=O(r^n) at0. Bounded splines give h_n=O(r^-1/b) at infinity. Thus s=1/b satisfies the initial hypotheses. With this decoding, h_2(r)=r[G_1(r)-G_3(r)]/2, where G_k are the decoded divided-vorticity radial cosine coefficients. Write b=beta_basis, t=1-(1+(r/L)^2)^(-1/(2b)) and G_k=P_k(t)(1-t)^(b+1)r/sqrt(L^2+r^2) for odd k. Direct differentiation gives

    G_k(r) d r = b L P_k(t) dt  (odd k).

Hence

    M_2 = b L/2 int_0^1 [P_1(t)-P_3(t)] dt,
    c = -b L/4 int_0^1 [P_1(t)-P_3(t)] dt.               (4)

For a degree-d B-spline coefficient vector (p_j) with knot sequence (t_j), its integral is sum_j p_j(t_(j+d+1)-t_j)/(d+1), with the endpoint-clamped basis. The integral identity follows either by integrating the standard B-spline antiderivative or by the recursion and a telescoping sum. The stored binary coefficients and knots therefore determine (4) by exact rational arithmetic, as independently implemented and checked in163. The exact center strain is an input to this local representation, not evidence that an archive satisfies the required value 1+beta/2.

For the manufactured family of171, take1<p<2, so p<n for every n>=2 and the source has decay s=2-p in(0,1). Then psi_n=w_n r^n(1+r^2)^((p-n)/2), n>=2, comparison of its Taylor coefficient with (2) gives M_n=2n w_n exactly. To justify the canonical interpretation directly, the difference of the manufactured coefficient and its regular Green solution is A r^n. Both are O(r^p) at infinity, and p<n, so A=0. This supplies tests of the global moment quadrature that are independent of the numerical inverse. The n=1 family instead requires the relative subtraction w_1 x and is covered by171.

## Independent compact-coordinate moment quadrature

For the finite r2 cosine source, the product identity gives h_n=r(G_(n-1)-G_(n+1))/2 for n>=2, with a coefficient outside the saved range set to0. The n=1 exception is h_1=r(G_0-G_2/2) and is not evaluated with that n>=2 formula. Put z=1-t, S=1-z^(2b) and r=L z^-b sqrt(S). Then dr/dt=bL z^(-b-1)/sqrt(S). For even n the indices n-1,n+1 are odd and G_k dr=bL P_k dt. For odd n they are even and G_k dr=bL P_k dt/sqrt(S). Consequently, for any fixed switch radius R>0,

    R^(n-2)M_n = bL/2 int_0^1 (R/r(t))^(n-2)
                    [P_(n-1)(t)-P_(n+1)(t)] S(t)^(-epsilon_n/2) dt,
    epsilon_n=0 if n is even, 1 if n is odd.             (5)

This follows by direct change of variables in the already absolutely convergent moment. At t=0 the first active polynomial powers cancel the displayed negative powers, giving a bounded integrand; at t=1 it is integrable. Gauss-Legendre quadrature on every spline cell in t therefore supplies a check with a different integration variable and quadrature rule from adaptive Gauss-Kronrod on physical radius. The coefficient decoder is still the same independently written verifier reader, so agreement is not evidence independent of decoding. Comparing several orders is a diagnostic, not a certified integral enclosure. Formula(4) remains the separate exact n=2 anchor. For n=2, (5) is the same degree5 polynomial moment and is exactly integrated in real arithmetic by three or more Gauss-Legendre nodes per cell. Its floating comparison tests the decoding and summation; n>=3 tests the distinct nonpolynomial quadratures.

For two fixed computed moment vectors, write C_n=R^(n-2)M_n. The gradient of delta M_n r^n sin(n phi)/(2n) has magnitude |delta M_n|r^(n-1)/2, by the polar gradient formula and sin^2+cos^2=1. Hence its velocity contribution has magnitude R|delta C_n|(r/R)^(n-1)/2. At r<=R summing modes bounds the difference of the two harmonic velocities by R sum_n|delta C_n|/2. This is a bound between two specified harmonic fields in exact arithmetic, not a bound on their common error relative to the canonical inverse. The floating evaluation of that sum is only a diagnostic.

## Limits of the check

Any error in M_n changes only a harmonic polynomial in the local expression. Its continuous elliptic and divergence residuals vanish, so good local residuals cannot validate that moment. Every reported local E check must therefore be accompanied by a global moment or velocity comparison, and M_2 must be checked against the exact rational archive moment. For n>=3 finite floating quadrature errors remain numerical uncertainties.

Conversely, independent radial quadrature at every nearby point can introduce slightly different errors into the same leading harmonic coefficient. The elliptic diagnostic E=dy V_1-dx V_2-Omega differentiates VELOCITY once, as does div V. Each seven-point first derivative magnifies velocity evaluation errors by at most11/(6h), giving11/(3h) for E before source error. The stencil has sixth-order truncation on smooth data but still differentiates only once; there is no second derivative of velocity or 1/h^2 bound in this diagnostic. Reusing one globally computed moment removes that particular inconsistency without proving a uniform error bound. The seven-point differentiation and its conditional error constants are those of171. Knot crossings and cancellation at large r still need separate diagnostics.

## Dependencies and verification plan

Dependencies:171 for the canonical inverse and manufactured sources;163 for the exact binary-rational center moment and its separate checker. This proof precedes the new implementation. Verify the transformed moment and local identities symbolically, test M_n=2n w_n and the known velocities, then compare the archive velocity with the previous independent full-plane integral and inspect both Cartesian E and divergence while varying step size. Retain the source hashes and all tolerances. The existing numerics-lane evaluator is not imported or executed. No servers, JavaScript/TypeScript, cluster, GPU or Lean/Lake is used.

Written UTC 2026-10-21T13:47:21.769738+00:00, before the implementation.
