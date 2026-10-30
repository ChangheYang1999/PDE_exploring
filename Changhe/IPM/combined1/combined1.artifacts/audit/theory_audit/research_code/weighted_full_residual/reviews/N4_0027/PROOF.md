# Complete weighted residual norm at regularization radius one

## Statement, notation and exact input

Let c>1 be rational, delta=1-1/c, and let chi be a finite rational canonical potential of the campaign. Its terms are

    b_(j,m,k) r^(2k)(1+r²)^(p_j-k) cos(2m theta),
    p_j=(3+1/c-j delta)/2,

with nonnegative integer j,m,k and k>=m. These hypotheses make chi smooth at the origin. Define rho=-partial_y Delta chi and U=(-partial_xyy chi,partial_xxy chi), so div U=0 and the signs agree with the canonical IPM convention. Let

    F=(cX+U).D rho-rho,
    v=1/(1+r²), t=1-v, w_a=v^(a/2).

Assume the exact Cartesian differentiation and product algebra give a finite expression

    F=r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta),

where ell is a positive integer, n is positive odd and every P is rational. All angular products are retained. Put Q_(ell,n)(v)=P_(ell,n)(1-v). This topic proves the full-plane norm in L²(w_a² dX), where the regularization radius is exactly one. A different radius defines a different norm.

For each nonzero Q let q_(ell,n) be its exact vanishing order at v=0. If

    a-3+ell delta+2q_(ell,n)>-1

for every component, then each separated product is integrable and

    ||w_a F||²=(pi/2) sum_n sum_(ell,k)
       integral_0^1 v^(a-3+(ell+k)delta/2)(1-v)
                     Q_(ell,n)(v) Q_(k,n)(v) dv.          (1)

For rational a the right side is pi/2 times an exact rational. This is an identity for the forcing norm, not a necessary correction distance or an existence condition by itself.

## Cartesian construction and proof of the identity

For a term f(r)cos(n theta) or f(r)sin(n theta), apply

    partial_x=cos(theta)partial_r-sin(theta)partial_theta/r,
    partial_y=sin(theta)partial_r+cos(theta)partial_theta/r.

The product-to-sum identities shift n by one and fold negative sine indices with a minus sign. Applying these rules three times gives rho and U; four times gives D rho. Multiplying the complete cosine and sine families in U1 rho_x+U2 rho_y and adding the linear term constructs F. The exact radial powers yield the displayed finite representation. Apparent origin denominators are removed only after exact polynomial divisibility checks. These are the independently audited identities of ../radial_fourier/PROOF.md; no peer polar residual array is used.

The full-circle identity integral sin(n theta)sin(m theta) dtheta=pi if n=m and zero otherwise removes the unequal angular modes. Since r²=(1-v)/v and r dr=-dv/(2v²), the remaining radial Jacobian is r³dr=-(1-v)dv/(2v³). This gives (1). Ordered branch products can equivalently be summed as diagonal products once and off-diagonal products twice.

After extracting q_(ell,n), each diagonal has endpoint exponent strictly greater than -1 by hypothesis. Every cross exponent is the arithmetic mean of its two diagonal exponents, so it also exceeds -1. All finite expansions and integrations in (1) are therefore legitimate. The original smoothness handles r=0; it also appears as bounded polynomial factors at v=1 and the explicit factor1-v.

If a grouped polynomial is H_e(v)=sum_j h_(e,j)v^j with radial prefactor v^e, its integral is sum_j h_(e,j)/(e+j+1). Each nonzero term has positive denominator after the endpoint test. Retaining all signed coefficients before taking a square root preserves cancellation exactly. Outward enclosures of pi and the square root then enclose the norm without a spatial quadrature error or an omitted tail.

## Sharp membership from a surviving leading sector

For every nonzero coefficient Q_(ell,n)[j], collect its angular coefficient at exact exponent z=ell delta/2+j. Combine equal z and equal n before selecting the smallest z=q with a nonzero angular vector A(theta). This exact combination also handles accidental resonances. The finite expression in v has

    F=r v^q [A(theta)+O(v^epsilon)]

uniformly in theta for some epsilon>0, because the set of remaining exponents is finite and has a positive gap. If there is only one exponent, the remainder is zero. Since v=r^-2(1+O(r^-2)), this becomes

    F=r^(1-2q)[A(theta)+O(r^-epsilon')]

for some epsilon'>0. Angular L² convergence implies the squared angular norm, after dividing by r^(2-4q), tends to pi times the sum of squared leading sine coefficients, which is strictly positive. Therefore the weighted radial integral is finite exactly when

    a>2-2q.

At equality the divergent radial power is r^-1. Below equality it diverges faster. A failed separated test alone would not prove divergence, but this exact nonzero leading vector does. For the stated state131 source, the checker must establish q=delta, giving threshold a>2/c.

## Independent verification and scope

The checker reads the independently reconstructed state131 potential from this lane. It verifies the frozen peer input, proof and code identities, constructs every residual component through Cartesian differentiation, computes the exact rational energy at each requested weight and compares the entire rational number with the peer result. It separately checks the exact leading vector norm and membership threshold. Direct field values check the assembled residual at four rational points.

The peer uses its separately derived polar density and stream algebra. Shared input coefficients are necessary for a meaningful comparison and are not an independent source-data audit. That source-data audit was completed in the baseline topic. No canonical velocity extension on the proposed weighted correction space, high-order inverse or nonlinear fixed point is proved here.
