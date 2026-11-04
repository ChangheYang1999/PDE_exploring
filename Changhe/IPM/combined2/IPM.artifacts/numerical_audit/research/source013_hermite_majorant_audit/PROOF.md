# Independent audit of the cubic spectral majorant

## Exact statement and conventions

Let g in H^3(R^2), use the unitary Fourier transform, and put T_j=int |xi|^(2j)|g_hat(xi)|^2 dxi for j=0,1,2,3. These are squared norms of the full ordered Cartesian derivative tensors. Assume certified rational bounds 0<=L_j<=T_j<=U_j. Let q=21/10 and f(s)=(1+s)^q for s>=0. Set a=1, b=13000, t=b-a and u=(s-a)/t. Define

    H00(u)=2u^3-3u^2+1,  H10(u)=u^3-2u^2+u,
    H01(u)=-2u^3+3u^2,  H11(u)=u^3-u^2,
    P(s)=f(a)H00(u)+t f'(a)H10(u)+f(b)H01(u)+t f'(b)H11(u).

Write P(s)=sum_(j=0)^3 p_j s^j. If each p_j lies in the rational interval[I_j,J_j], then

    ||g||_(H^(21/10))^2 <= sum_j max(I_j L_j,I_j U_j,J_j L_j,J_j U_j).

Applied to the accepted source013 residual, g=sqrt(1+4|X|^2)F013, the proposed displayed consequence is

    0.0035510975483434412497 <= ||g||_(H^(21/10))
                            <= 0.0055545729030073655758.

The exact candidate and parameter c=4076476460239181/2251799813685248 remain fixed. The lower bound is imported from AN307, not rederived from P.

## Proof

The four displayed basis polynomials give P(a)=f(a), P'(a)=f'(a), P(b)=f(b), P'(b)=f'(b), by direct evaluation and differentiation. For any s>=0 distinct from both nodes, let K=(f(s)-P(s))/((s-a)^2(s-b)^2). The function f(v)-P(v)-K(v-a)^2(v-b)^2 has the two double zeros a,b and the further zero s. Applying Rolle's theorem four times on the interval between the smallest and largest of these points gives a point z where its fourth derivative vanishes. Consequently f(s)-P(s)=f''''(z)(s-a)^2(s-b)^2/24. All involved points are nonnegative, and

    f''''(z)=q(q-1)(q-2)(q-3)(1+z)^(q-4)<0.

Thus f<=P on the entire half-line, with equality at the two nodes. The argument applies outside as well as inside the node interval. Multiplying by the nonnegative density |g_hat|^2 and integrating gives ||g||_(H^q)^2<=sum_j p_j T_j. These integrals are finite since q<3 and g is in H^3. A bilinear expression on a rectangle takes its maximum at a corner, which proves the stated bound. In particular, a negative coefficient uses a lower moment endpoint for its largest contribution.

For exact computation, write z_a=(1+a)^(1/10), z_b=(1+b)^(1/10). Then f(a)=(1+a)^2 z_a and f'(a)=q(1+a)z_a, and likewise at b. Expanding the four basis polynomials therefore produces exact rational linear forms in z_a,z_b for every coefficient. Rational tenth-power inequalities prove the supplied root enclosures. Signed rational interval arithmetic then encloses the coefficients and all four coefficient-moment products. Squaring the proposed rational decimal upper verifies the final norm display without any floating arithmetic.

## Dependencies and audit scope

The original source013 whole-plane moments and their actual independent review are taken from ../source013_norms/verification/weighted_publication_v01/. Their exact source and fractional order are checked. The previous lower bound and its independent AN307 check come from ../source013_moment_refinement_audit/. The AT proposal is retained as immutable local snapshots, with its review and original bindings checked.

The checker expands the Hermite basis directly, independently of the coefficient formula used in the AT proposal. It uses the original moment intervals; for this polynomial the linear coefficient is negative, so its contribution uses the original lower endpoint. It verifies every coefficient sign and every root and norm power inequality. This proof is written before the checker is executed. No new quadrature, optimized-node claim, P-S2 bound, near or far operator estimate, global background, inverse, invariant ball or existence statement follows.
