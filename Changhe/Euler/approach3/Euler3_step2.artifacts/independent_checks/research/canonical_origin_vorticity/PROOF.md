# Exact axial vorticity residual at the origin

Date: 2026-10-29. Status: complete informal argument, independently checked by the verifier; lead review and arithmetic results are recorded separately. This is an adaptation of the frozen Euler3 canonical-origin argument to the degree-six campaign.

## Statement and hypotheses

Let T and S be finite sums of real, orthonormal regular solid harmonics H_{ell,m,k}, with no Condon-Shortley phase, multiplied by scalar functions smooth in q = |y|^2 near zero. All azimuthal orders m are even. Define

    U = curl(T y) + curl curl(S y),       Omega = curl U.

The main toroidal A and poloidal C radial channels have envelopes equal to one at q = 0, and Chebyshev coordinate xi(0) = -1. Any B, D and E correction channel has a factor (q/(q+R1^2))^d, where R1 > 0 and the integer d >= 1, times a smooth function. The smooth angular twist vanishes at q = 0. These hypotheses are properties of the represented field, not assertions that it solves Euler. The result applies to any finite degree; the reader for this campaign additionally requires main degree six.

For ell = 1,2 let a_ell and g_ell be the alternating sums of the A and C coefficients, respectively, in column (ell,0,0). A missing column has sum zero. Set

    c1 = sqrt(3/(4 pi)),       c2 = sqrt(5/(16 pi)).

These constants are not the similarity exponent. In this normalization,

    H_10 = c1 y3,       H_20 = c2 (2 y3^2 - y1^2 - y2^2).

For real parameters c and w, write Jy = (-y2,y1,0), W = (c I - w J)y + U, and

    R_Omega = Omega + D Omega W + w J Omega - DU Omega.

Then the following identities hold exactly:

    U3(0) = 2 c1 g1,                Omega3(0) = 2 c1 a1,
    partial3 U3(0) = 12 c2 g2,      partial3 Omega3(0) = 12 c2 a2,
    R_Omega(0) = 2 c1 [a1 + 12 c2 (g1 a2 - a1 g2)] e3.                 (1)

If a1 is nonzero, the signed ratio R_Omega,3(0)/Omega3(0) is

    1 + 12 c2 (g1 a2/a1 - g2).                                       (2)

A rigorous interval for the scalar in (1) that excludes zero proves that this particular exact finite represented field does not solve the rotating momentum equation with any C2 pressure. It does not exclude nearby profiles, certify a distance to them, or give a full-domain residual bound.

## Proof of the derivative formulas

For a homogeneous harmonic polynomial H of degree ell, put h = grad H. Direct differentiation, homogeneity y.h = ell H, and Delta H = 0 give

    curl(f(q) H y) = f(q) (h cross y),
    curl curl(g(q) H y)
      = [(ell+1)g(q) + 2q g'(q)] h - 2 ell g'(q) y H.                 (3)

The second formula also follows by expanding curl curl(Sy) = 2 grad S + (D2 S)y - y Delta S. Toroidal velocity begins at degree ell in y. Poloidal velocity begins with (ell+1)g(0)h at degree ell-1; every radial correction has degree at least ell+1. Thus U(0) comes from ell = 1 poloidal terms only, and DU(0) from ell = 1 toroidal and ell = 2 poloidal terms only.

Even m leaves only m = 0 for ell = 1. Its toroidal velocity is c1 f(q) Jy, with zero third component. The other allowed ell = 2 harmonics are multiples of y1^2-y2^2 and y1 y2, and have zero second y3 derivative. Since partial3^2 H_20 = 4 c2, (3) proves the two formulas for U3 and partial3 U3.

Curling the toroidal term gives the poloidal formula (3), with f in place of g. It therefore contributes 2 c1 f_10(0) and 12 c2 f_20(0) to Omega3(0) and partial3 Omega3(0). For the curl of the poloidal term, each component of K = h cross y is harmonic and homogeneous of degree ell: the cross terms in its Laplacian cancel by symmetry of the Hessian of H. Consequently

    curl curl curl(g(q) H y)
      = -Delta(g(q) K) = -[4q g''(q) + (4ell+6)g'(q)] K.             (4)

For ell >= 2 this has zero value and first derivative at zero. For ell = 1 its third component vanishes identically, since K = c1 Jy. Thus (4) contributes neither axial quantity. This also checks the possibly nonzero radial derivatives of the damped channels: they cannot contribute either axial entry in (1).

The twist can be absorbed into smooth real radial coefficient pairs. At zero its angle is zero. Main envelopes have value one, correction envelopes value zero, and T_k(-1) = (-1)^k. The four surviving scalar values are exactly the four alternating sums in the statement. This proves the first four identities in (1).

## Proof of the residual identity and its scope

Even azimuthal order implies equivariance under the proper rotation Q = diag(-1,-1,1). Hence U(0) and Omega(0) are axial. At zero, W = U and J Omega = 0, so

    R_Omega(0) = [Omega3 + U3 partial3 Omega3 - Omega3 partial3 U3](0) e3.

Substitution proves (1) and (2). In particular, the transport term U3 partial3 Omega3 is retained; the origin need not be a stagnation point or a vorticity maximum.

The representation is smooth and divergence free. For its momentum residual

    R_u = (1-c)U + [(c I-w J)y+U].grad U + w JU + grad P,

the product rule gives curl[(1-c)U+c(y.grad)U] = Omega+c(y.grad)Omega. Proper-rotation covariance gives the corresponding identity for w[JU-(Jy.grad)U]. Finally, incompressibility gives curl[(U.grad)U] = (U.grad)Omega-(Omega.grad)U, and curl grad P = 0 for C2 pressure. Thus curl R_u = R_Omega. Nonzero (1) is incompatible with R_u identically zero.

Under physical dilation U_L(y) = L U(y/L), L > 0, the four coefficients transform as (a1,a2,g1,g2) -> (a1,a2/L,L g1,g2), as follows directly from the derivative identities. Both (1) and (2) are invariant. Axial rotation preserves the m = 0 coefficients. No gauge normalization is needed.

## Exact interval arithmetic

A finite binary64 coefficient denotes its exact dyadic rational. Thus the four sums and g1 a2-a1 g2 are exact rational operations. The two normalization constants are enclosed as follows.

For 0 < t < 1, the alternating partial sums S_N(t) and S_{N+1}(t) of sum_{j>=0} (-1)^j t^(2j+1)/(2j+1) enclose arctan(t). This follows by integrating the finite geometric series for 1/(1+t^2), whose remainder has the next term's sign and no larger magnitude. If a = arctan(1/5) and b = arctan(1/239), tangent doubling gives tan(4a) = 120/119 and tan(4a-b) = 1. The integral bounds t/(1+t^2) < arctan(t) < t imply 0 < 4a-b < 4/5 < pi/2. Therefore pi = 16a-4b. The reader uses N = 64, fixed before selected-state evaluation.

For rational x >= 0 and integer M > 0, k = isqrt(floor(x M^2)) satisfies k/M <= sqrt(x) <= (k+1)/M. If (k/M)^2 = x the lower endpoint is exact. Taking M = 10^60 and using the endpoints of the pi interval in 3/(4 pi) and 5/(16 pi) encloses c1 and c2. Interval multiplication uses all four endpoint products; negative exact factors reverse endpoints. Equation (2) divides only by the exact nonzero rational a1. Decimal reporting uses floor at the lower endpoint and ceiling at the upper endpoint. Every operation therefore preserves inclusion.

## Dependencies and verification

The vector identities are proved above. The canonical coefficient semantics are checked by the local bounded exchange decoder, copied from the frozen Euler3 independent route, with source hashes recorded. The v1 decoder is unchanged. The v2 decoder additionally accepts the historical five-key channel schema only when B, D and E each have exactly zero rows; it checks raw archive/metadata equality before filling the unused degree caps with the main degree. This changes no coefficient or field definition. The reader checks archive and metadata consistency, exact finite binary64 values, harmonic support, even m, main degree six, and correction damping. Its arithmetic controls include a separate exact polynomial construction of both curls, with radial and m = 2 terms present, plus signed, zero-vorticity and cancellation cases. Verification files distinguish the analytic argument, arithmetic outcome and external model review. No Lean or other formal verification is claimed.
