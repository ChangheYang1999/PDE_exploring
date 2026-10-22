# An exact positivity certificate for the exponent-three temperature representation

Status: conditional certificate theorem proved below; lambda.97K16 exact sign certificate passed101 leaves. Strengthened archive-validation checker passed after model audit.
Written UTC: 2026-10-21T01:26:38.285919+00:00.
This concerns represented temperature fields only. It is not a PDE existence result.

## Statement, notation and hypotheses

Fix L>0 and the exact basis exponent b=3. For physical r=sqrt(x^2+y^2), define

    t=1-(1+r^2/L^2)^(-1/6), z=1-t, rho=sqrt(1-z^6), eta=-y/r.

At r=0 use continuous extension. Let P_k(t) be real piecewise polynomials on a finite rational knot partition of[0,1], of at least class C1. Require P_k to vanish at t=0 to order at least floor(k/2). In the application these are the masked degree-five clamped spline coefficients, interpreted as exact binary rationals. Set

    E(t,eta)=sum_(k even) P_k(t) T_k(eta),
    O(t,eta)=sum_(k odd)  P_k(t) T_k(eta),
    F=z^5(E+rho O),     Theta=x^2 F.

On each radial knot interval, define the rational polynomials

    E_S=2E+(1-eta^2)[ z(1-z^6) E_t/3
                        -5(1-z^6) E/3-eta E_eta ],
    O_S=2O+(1-eta^2)[ z(1-z^6) O_t/3
                        -5(1-z^6) O/3-eta O_eta+z^6 O ].    (1)

Suppose a finite recursive rectangular subdivision of each knot interval times[-1,1] has the following certificate. For every leaf rectangle, let a_lo,a_hi be rational bounds on sqrt(1-(1-t)^6) on that rectangle. Express each of E+a_lo O, E+a_hi O, E_S+a_lo O_S and E_S+a_hi O_S in the tensor product Bernstein basis of that rectangle. All four coefficient sets have strictly positive minima. Then F>0 at every finite physical point and Theta_x>0 at every x>0. The same certificate proves the desingularized derivative 2F+xF_x>0 on the whole physical plane.

The conditions are sufficient and need not succeed for every positive field. If the subdivision fails within an allotted finite search, the verdict is OPEN, not a negative theorem.

## Derivative identity

For r>0, at fixed y,

    x partial_x t=(1-eta^2)z(1-z^6)/3,
    x partial_x eta=-eta(1-eta^2),
    x partial_x rho=(1-eta^2)rho z^6,
    x partial_x z^5=-(5/3)(1-eta^2)(1-z^6)z^5.

The first identity follows by differentiating z=(1+r^2/L^2)^(-1/6) and using x partial_x r=r(1-eta^2). The second follows from eta=-y/r. For the third use rho=r/sqrt(r^2+L^2), so r partial_r rho=rho L^2/(r^2+L^2)=rho z^6. The last follows from the first. Product differentiation gives

    2F+xF_x=z^5(E_S+rho O_S),     Theta_x=x(2F+xF_x).        (2)

The center condition proves smooth extension near the origin: t is an analytic function of r^2 with a simple zero; for even k=2j, t^j T_k(-y/r) is smooth because r^k T_k(-y/r) is a polynomial in x,y; for odd k=2j+1 the extra rho supplies the remaining factor r divided by sqrt(r^2+L^2). The residual smooth radial factors are analytic near0. Thus all identities extend by continuity to the origin. On the axis x=0, the formula gives 2F+xF_x=2F, consistently with the factor1-eta^2=0. A certificate covering the full closed(t,eta) rectangle consequently covers every finite physical point. Its t=1 edge is used only for closure, not as a physical point at infinity. The factor z^5 is strictly positive at every finite r.

## Bernstein lower bound and exact verification

On[0,1], the Bernstein polynomials B_i^n(u)=binom(n,i)u^i(1-u)^(n-i) are nonnegative and sum to1. The tensor products B_i^n(u)B_j^m(v) have the same properties. Thus a polynomial's value lies between its smallest and largest Bernstein coefficients.

At any fixed point in a leaf, rho lies in[a_lo,a_hi]. Since E+rho O is affine in rho, it lies between E+a_lo O and E+a_hi O at that point. Positivity of the Bernstein coefficients of both bounding polynomials proves E+rho O>0. The identical argument with E_S,O_S proves the second sign. Combining with(2) proves the theorem.

The bound for rho needs no floating-point square root. It increases with t. For a rational q in[0,1] and a chosen integer precision B, put N=floor(sqrt(floor(q 2^(2B)))). Then N/2^B<=sqrt(q)<=(N+1)/2^B, with equality sharpenable if needed. This follows by squaring the endpoints. Applying this formula at the two radial ends gives exact rational a_lo,a_hi.

All conversions are rational. The Cox--de Boor recursion, restricted to one knot interval, yields its power-polynomial coefficients exactly. If a polynomial sum_j c_j u^j has degree at most n, its Bernstein coefficient i is sum_(j<=i)c_j binom(i,j)/binom(n,j), as follows by expanding u^j in the Bernstein basis. Apply this in each coordinate. Subdivision at a rational midpoint uses the de Casteljau recursion, which is repeated exact affine averaging of the coefficients and preserves the represented polynomial. Every binary split replaces a closed rectangle by its two closed halves, so a finite recursive tree verifies coverage without trusting a sampled grid.

The certificate input must contain the exact rational knot values, coefficients, basis degree and L, together with a checksum of the original archive. The checker rederives(1), converts the polynomials and follows the full subdivision tree; it recomputes every bound. A printed success flag from a search is not sufficient evidence without those inputs and checks.

## Scope and dependencies

This is a direct algebraic certificate. It imports no PDE identity, inverse, positivity assumption about vorticity or claim about the flow. The stored piecewise polynomial field has its actual spline regularity, not automatically C-infinity. Global positivity and monotonicity may help a numerical change of coordinates but do not make a rejected forced state a B2 profile. The positive far-field horizontal coefficient, when separately certified, yields growth of Theta(x,y) as x tends to infinity at fixed y and can support properness of that one change of variables.

No large coefficient list is hardcoded in source code. Exact numerical inputs and the subdivision tree are JSON artifacts, processed by a reusable Python checker. No formalization or interval-certified PDE residual is claimed; Lean and Lake execution are prohibited.

## Input checks and first concrete certificate

The application has exactly degree+1 endpoint knot multiplicity. The checker now checks this explicitly and independently verifies the actual vanishing order of every first-span polynomial. This closes an input-validation defect identified by actual Opus5.5 review126: an overclamped input could pass the coefficient mask but violate origin continuity. Both overclamped endpoints now have rejection tests. The actual archive had the correct multiplicity throughout, so this defect did not apply to its input.

The exact JSON is also checked directly against the raw NPZ arrays, including the original archive SHA256, degree, exponent, map scale, reconstructed knot values and every effective masked coefficient. An earlier standalone exporter already made this exact comparison; it is now repeated within check mode. General rational test fields may have degrees other than5. The theorem permits this and does not require dyadic coefficients. For a claimed binary archive, the correspondence check enforces the exact stored doubles, so non-dyadic substitutions are rejected. L does not enter the sign polynomials because it disappears in the compactified variables; it is still tied to the archive and required positive.

The lambda.97K16 archive has SHA2562b9019a726888b1e3776706390ad4c53739f7892b7232f79f96a97561f3b7a35. Its exact input aa19d1e6d732c5e715a151ba6a448f724853ef10b1bb7d09a60b0414ea1e161a was searched over56 positive radial spans. The search found101 positive leaves, maximum depth2, in19.475364s. A separate check invocation recomputed all101 leaves in17.651099s at2026-10-21T01:33:20Z. The certificate hash is29b0e38730b6c5d642ea9072aca3eaff963ffffcbc553e81dc9b3195e56b4cbe. The strengthened checker is rerun below before the final verification record is closed. Positive and negative manufactures, forged positive claims and high-precision Cartesian derivatives are checked separately. No smooth B2 profile follows.

## Final check of first archive, 2026-10-21T01:36:53Z
The strengthened checker directly matched the raw archive and recomputed all101 positive leaves in17.716246s, verdictCONFIRMED. Checker SHA2567549727b71a99a8820e8c442afc6f6ccf725204c5e0e44c5df2c2af36e754d8f; exact input and certificate hashes unchanged. Generic malformed endpoint defects were repaired and tested; the actual archive satisfies every hypothesis. The confirmed conclusion is exactly F>0 and Theta_x>0 on x>0, not a B2 solution.
