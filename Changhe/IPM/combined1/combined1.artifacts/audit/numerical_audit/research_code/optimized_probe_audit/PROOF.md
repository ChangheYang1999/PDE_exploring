# Independent Cartesian audit of the rational span probe for candidate007

## Exact claim and hypotheses

Let rho be the exact rational candidate C1-N1-007-d2w-j7-e2bal at c=4076476460239181/2251799813685248, and u=U[rho] its canonical S1 velocity. Let F=(cX+u).grad rho-rho. The candidate is smooth, div u=0, u=O(r^gamma), grad rho=O(r^(gamma-1)) with gamma=1/c<1, and F belongs to L2(R^2). These exact background facts are established in the candidate audits.

Suppose a real h in L2(R^2) has canonical divergence-free velocity U[h] in L2, with ||U[h]||2<=||h||2, and solves

    F+div((cX+u)h)-(2c+1)h+U[h].grad rho+div(U[h]h)=0

in distributions. Let P be exactly the rational polynomial whose15 coefficients and powers are in source/T4_a0.json, verified against its frozen hash, and put t=r^2/(1+r^2), v=1-t, phi=y v^2 P(t). The result being checked is

    ||h||2 > 7868527/25000000000 = 0.00031474108.

This excludes only the indicated fixed-background, fixed-c correction ball. It does not exclude other stationary profiles or prove an inverse estimate.

## Weak inequality

The probe is smooth and behaves as O(r^-3), with gradient O(r^-4), at infinity. Its products with the sublinear background and the L2 correction justify smooth cutoffs and integration by parts. Testing the displayed divergence equation against phi gives

    |I| <= (M+C)m+H m^2,
    I=int F phi, m=||h||2,
    M=||(2c+1)phi+(cX+u).grad phi||2,
    C=||phi grad rho||2, H>=||grad phi||infinity.

The two linear estimates are Cauchy-Schwarz, and the quadratic term uses ||U[h]||2<=m. Since all quantities are nonnegative, a positive I implies

    m >= 2|I|/(M+C+sqrt((M+C)^2+4H|I|)).

The checker compares this complete interval with the exact claimed rational floor. No optimization optimality is required.

## Independent Cartesian field construction

Use the established N4 radial-Fourier derivatives of the exact potential. Write their velocity and density-gradient components as

    u_i=r sum_j,n v^d_j U_(i,j,n)(t) trig_n(theta),
    partial_i rho=sum_j,n v^d_j R_(i,j,n)(t) trig_n(theta),
    d_j=(j+1)(1-1/c)/2.

These forms follow from the existing r^-3 or r^-4 potential derivatives after exact cancellation of t^2; every cancellation is checked. They are Cartesian derivatives, independently of T4's stream/radial transport construction.

Set B=v P'-2P and X=tB. Direct differentiation yields

    partial_x phi=v^2 X sin(2theta),
    partial_y phi=v^2[(P+X)-X cos(2theta)],
    (2c+1)phi+cX_vector.grad phi=r v^2[(3c+1)P+2cX]sin(theta).

Multiply these explicit Cartesian probe derivatives by the corresponding u_i modes, using exact product-to-sum identities and folding negative sine frequencies with their sign. Add the displayed linear term to obtain the complete M function. Multiply each Cartesian density-gradient component by r v^2 P sin(theta), again by exact product-to-sum identities, to obtain the two components entering C. Every resulting term has the form r v^(2+ell delta/2) A_(ell,n)(t), where delta=1-1/c. All angular frequencies are positive odd integers, so each squared trigonometric mode integrates to pi. Vector components are squared separately and then added.

For every two radial branches of a matching angular mode, the squared norm contribution is

    (pi/2) int_0^1 t v^(1+(ell1+ell2)delta/2) A1(t)A2(t) dt.

All ordered branch pairs are included, equivalently diagonal terms once and off-diagonal terms twice. The exponents exceed-1. Transform the exact polynomials to v and integrate with outward coefficients using positive power moments. The independently constructed first-sine residual gives

    I=(pi/2) sum_ell int_0^1 t v^(ell delta/2-1) F_(ell,1)(t)P(t)dt.

The existing projected residual retains all background interactions giving the first sine mode. No angular truncation, quadrature or omitted radial tail enters these quantities.

## Exact Bernstein certificate for the probe gradient

In polar coordinates grad phi has components v^2 Q sin(theta) and v^2 P cos(theta), where Q=(1-4t)P+2tvP'. Thus its pointwise angular maximum is max(|v^2P|,|v^2Q|). It suffices to bound two exact rational polynomials Z on[0,1].

For a degree-n polynomial Z(t)=sum_j a_j t^j, its Bernstein coefficients are

    b_k=sum_(j<=k) a_j binom(k,j)/binom(n,j).

The identity follows by expressing each monomial in the degree-n Bernstein basis. Those basis functions are nonnegative and sum to1, so |Z|<=max_k|b_k|. Midpoint de Casteljau subdivision replaces adjacent coefficients by their average and yields exact Bernstein coefficients for the two halves. Repeating subdivision therefore proves a bound on the union of all accepted dyadic cells. The checker stores every accepted leaf and its exact largest absolute coefficient, verifies that leaves tile[0,1], and requires each coefficient bound to be strictly smaller than the peer's rational H=13032047/250000000000. Elementary constant, linear and quadratic fixtures are checked first.

## Evidence and independence

The own code consumes the peer's frozen probe coefficients, candidate identity and comparison numbers. It does not use either peer's field-assembly or Gram code. The candidate potential, derivative helper, first-mode projection, proof, own code, peer proof and Opus R1-021 review are hashed. The Opus review independently used T2's generator-based fields and a Taylor subdivision; our audit uses N4 Cartesian fields and exact Bernstein subdivision. All actual enclosures and timings are retained under verification/. A successful reproduction can confirm the stated finite certificate only under the explicit weak-equation hypotheses above.
