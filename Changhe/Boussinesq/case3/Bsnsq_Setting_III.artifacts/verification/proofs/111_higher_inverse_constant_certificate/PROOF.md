# Exact higher-order constant of the serialized relative inverse

UTC 2026-10-21T02:33:33.730450+00:00. Status: proof completed before implementation; exact certificates and manufactured checks completed, as recorded in verification/SUMMARY.md. Scope: individual finite r2 source representations, not profile convergence.

## Statement and hypotheses

Let b>2 be noninteger, N=floor(b), and L>0. Let S(t) be a degree d>=N real spline on[0,1] with S through S^(N-1) continuous and piecewise bounded derivative of order N. Put z=1-t and r=L sqrt(z^(-2b)-1). The first-cosine coefficient of vorticity is

    q(r)=r z^(b+1) S(1-z).

Write the polynomial on the last spline interval as P(z)=sum p_j z^j. The first N homogeneous terms of q are A_j r^[-(j+1)/b], j=0,...,N-1, where A_j=L^[1+(j+1)/b]p_j. Remove these homogeneous angular sources globally as distributions. Their remainder has integrable absolute center velocity: each removed power at0 is less singular than r^-1, and the remainder at infinity is O(r^[-(N+1)/b]). The constant after their homogeneous relative velocities is C=(0,C2), with

    C2=-(1/2) integral_0^infinity
               [q(r)-sum_(j<N) A_j r^[-(j+1)/b]]dr.    (1)

This is the same constant as the canonical subtracted full-plane inverse: only the first cosine source contributes to its vertical value at0, and the relative inverse is the sum of homogeneous velocities and U_eta(X)-U_eta(0). The constant is -U_eta(0). Other permitted angular modes contribute zero to this center velocity by angular orthogonality.

Set a=N+1-b in(0,1), D_k=product_(j=1)^k(b-j), D_0=1. Then

    C2=-(b L²/2) J,
    J=sum_(k=0)^(N-1) (-1)^(k+1) S^(k)(0)/D_(k+1)
          +(-1)^N/D_N integral_0^1 (1-t)^(a-1)S^(N)(t)dt. (2)

For rational b,L,knots,coefficients, the power-bound method of packet104 gives an exact rational interval for(2). It applies to N=3 and hence3<b<4, not only to2<b<3.

## Direct finite-part reduction

The change of variables gives q(r)|dr/dz|=bL² z^-b P(z) exactly. With the cutoff r=L sqrt(epsilon^-2b-1), the integral of the jth homogeneous term over[0,r] equals

    bL² p_j/(b-j-1) epsilon^(j+1-b)
                  (1-epsilon^(2b))^[(b-j-1)/(2b)].

Replacing the last parenthesis by1 changes this expression by O(epsilon^(j+1+b)), which tends to0. Therefore(1) is minus bL²/2 times

    J=lim_(epsilon->0){integral_epsilon^1 z^-b S(1-z)dz
                   +sum_(j<N) p_j/(j+1-b) epsilon^(j+1-b)}. (3)

No analytic continuation convention is needed. This ordinary limit of explicitly subtracted integrals is determined by the canonical inverse. Terms j>=N are integrable at0 because N-b>-1.

## Repeated integration by parts

Let J_k be the corresponding finite part of integral_0^1 (1-t)^(k-b)S^(k)(t)dt for k<N. Differentiation gives an antiderivative (1-t)^(k+1-b)/(b-k-1). Integration on[0,1-epsilon], followed by subtracting the Taylor divergences, yields

    J_k=-S^(k)(0)/(b-k-1)-J_(k+1)/(b-k-1).              (4)

There is no surviving constant at the far endpoint because b is noninteger: each endpoint Taylor power is epsilon to a nonzero real power. At interior spline knots there is no jump term since the derivatives through N-1 are continuous. At k=N the integral converges ordinarily. Iterating(4) gives(2), including every alternating sign and boundary derivative. For N=2 this is exactly packet104.

## Exact cell integration and checks

On a knot cell[A,B], reconstruct S(A+(B-A)u) by rational Cox recursion. Differentiate N times, substitute u=(1-A-z)/(B-A), and obtain S^(N)(1-z)=sum d_j z^j. The contribution to the last integral of(2) is

    sum_j d_j/(a+j)[(1-A)^(a+j)-(1-B)^(a+j)].          (5)

All denominators a+j are positive. Every endpoint power is v^j v^a, so packet104's rational logarithm/exponential enclosures apply verbatim. Adding signed cell intervals and the exact boundary terms proves containment for J and C2. Outward rational rounding preserves it. A certificate must also check the raw archive's degree, knot sequence, source mask, beta, scale, source snapshot and exact binary coefficient values. Nonzero interval is a statement about that represented source only.

For a global polynomial P(z)=sum p_j z^j, equation(3) reduces exactly to J=sum p_j/(j+1-b). This supplies manufactured controls for every degree, including the noninteger pole signs. Piecewise splines need both boundary and cell terms and will be compared with independent high-precision quadrature of the absolutely convergent integral in(2). Tampered input/certificate must fail.

## Resonance and scope

Extend the last-interval polynomial P to all[0,1]. The difference S(1-z)-P(z) vanishes near0, so its weighted integral has no endpoint divergence. This exact decomposition isolates the terms -(bL²/2)p_j/(j+1-b) from the global polynomial. For3<b<4 its j=2 contribution to C2 is

    -(bL²/2) p2/(3-b).

Storing +(bL²/2)p2/(3-b) as the constant contribution reverses its sign. The full source constant itself can nevertheless be computed correctly by another formula. As b approaches3, this contribution can be large and is not a uniform obstruction to field or residual convergence. Packet109 shows why an additional tail topology is needed. At integer b, logarithmic terms replace this decomposition and equations(2)-(3) as written do not apply.

A nonzero C excludes an exact B2 field only with the separately audited expansion hypotheses and b=beta. It gives neither a broad nonexistence theorem nor a bound on nearby functions. Restrictions: no JavaScript/TypeScript, servers, RLScience cluster, Lean/Lake or GPU.
