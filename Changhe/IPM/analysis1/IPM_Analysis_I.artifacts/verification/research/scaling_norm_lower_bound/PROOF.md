# A finite-annulus lower bound for the canonical scaling-field norm

This proof is written before the numerical implementation. Its numerical application is OPEN. It concerns the distinguished exact normalized modal trial, not X3 or an exact stationary profile. No inverse estimate is asserted.

## Statement and exact trial

Let rho be the exact normalized trial defined in modal_repair/PROOF.md, with its accepted exact JSON data, scalar correction and canonical velocity. Put t=log r, D=partial_t, K=rho-D rho, and use the weighted weak H1 norm

    ||f||_X^2 = integral_R2 [f^2+r^2|grad f|^2] w(r) dX,
    w(r)=L^6 r^-6(1+r^2/L^2)^(3/2-k).

Here L>0 and 0<k<1/2 are the exact dyadic input values. Topic138, modal_graph_scaling, proves that this actual K belongs to X and to its stated broad graph domain, has Sigma(K)=0, and has nonzero image LK=epsilon-D epsilon. Its full hypotheses and supplements are inherited when drawing a consequence for that domain. A norm lower bound below does not require the finite annulus to cover the whole plane.

In the middle annulus a<=t<=b, the exactly normalized density equals the unaltered finite spline expression

    rho = r^3 cos(theta)^2 sin(theta) sum_(m=0)^259 S_m(t) cos(2m theta).

The exactification only changes the inner and outer join coefficients and the outer scalar correction. No change is made to a middle spline coefficient. The knot data have degree7, eightfold endpoints, and1558 strictly positive spans. Fix any finite collection of distinct whole positive knot spans, with no overlaps except endpoints. Empty or repeated spans are inadmissible in this calculation. The full middle annulus, if selected, consists of all1558 spans. All endpoints are exact log radii, never separately rounded physical radii.

On one selected span [a_i,b_i], put d_i=b_i-a_i>0 and x=(t-a_i)/d_i. Each S_m is a degree-at-most7 polynomial in x. The identity cos(theta)^2 sin(theta)=(sin(theta)+sin(3theta))/4 gives

    rho = r^3 sum_(j=0)^260 H_j(x) sin(nu_j theta), nu_j=2j+1.

Every H_j is a rational polynomial of degree at most7. Define

    B_j = -2 H_j - H_j'/d_i,
    C_j = 3 B_j + B_j'/d_i,
    Q_i = d_i integral_0^1 sum_j [(1+nu_j^2) B_j^2+C_j^2] dx.

Primes here differentiate x. Then Q_i is an exact nonnegative rational. Let

    v(t)=L^6 exp(2t)(1+exp(2t)/L^2)^(3/2-k).

For the physical annulus A_i={exp(a_i)<r<exp(b_i)}, one has

    pi v(a_i) Q_i <= ||K||_(X,A_i)^2 <= pi v(b_i) Q_i.       (1)

Consequently

    ||K||_X^2 >= pi sum_i v(a_i) Q_i.                       (2)

For the selected union only, the analogous sum of right endpoints is an upper bound. It is not a whole-plane upper bound. Any finite selected union gives a valid global lower bound by nonnegativity outside that union. A failed or incomplete full-annulus run is not reported as a complete result.

## Derivation of the norm and weights

Since D(r^3 H_j)=r^3(3H_j+H_j'/d_i), the fields K and DK have coefficients r^3 B_j and r^3 C_j. The angular derivative has cosine coefficients r^3 nu_j B_j. Orthogonality of distinct positive integer sine frequencies, and separately cosine frequencies, gives a factor pi for each square integral on0<=theta<=2pi. In polar coordinates r^2|grad K|^2=(DK)^2+K_theta^2 and dX=r^2 dt dtheta. Multiplying the resulting r^6 by r^2w gives v(t). Thus the squared norm on A_i is exactly

    pi d_i integral_0^1 v(a_i+d_i x)
          sum_j [(1+nu_j^2)B_j(x)^2+C_j(x)^2] dx.

The polynomial in brackets is pointwise nonnegative. Both exp(2t) and (1+exp(2t)/L^2)^(3/2-k) are strictly increasing and positive because3/2-k>0. Bounding v between its endpoint values proves(1). The exact global K has the inherited weak gradient; no join measure is introduced by decomposing its integral. Boundary circles have planar measure zero. Additivity and nonnegativity prove(2).

## Two independent finite calculations

The first method decodes exact binary64 hexadecimal inputs to rationals, reconstructs the local B-spline basis by the defining Cox recurrence, and multiplies its coefficient matrix by the eight active coefficients of each mode. It projects to odd angular modes using the signed sin(p+2m)+sin(p-2m) rule. After differentiating the resulting rational polynomials, it multiplies B_j and C_j by themselves, and integrates each monomial x^q as1/(q+1). It accumulates all positive spans in increasing order. Exact arithmetic computes Q_i even though signed polynomial coefficients may cancel. Positivity of Q_i is checked exactly, not inferred from the rounded output.

The second method independently decodes each hexadecimal string by its integer significand and binary exponent. On a span it reconstructs each modal polynomial by the de Boor interpolation recurrence applied to the eight active coefficients, with the polynomial argument a_i+d_i x. No Cox basis or first-method polynomial is imported. Let A_m=S_|m|/2 when m is nonzero and |m|<=259, A_0=S_0, and A_m=0 otherwise. Its independent angular projection is

    H_(nu) = [A_((nu-1)/2)-A_((nu+1)/2)
                 +A_((nu-3)/2)-A_((nu+3)/2)]/4,

for nu=1,3,...,521. This follows by the complex Fourier coefficients of the even cosine sum and the two sine factors. Negative indices are intentional. Each B_j and C_j is expanded in shifted Legendre polynomials P_l(2x-1) by descending exact coefficient elimination. Orthogonality gives

    integral_0^1 p(x)^2 dx = sum_(l=0)^7 p_l^2/(2l+1).

For completeness, Rodrigues' formula for P_l and integration by parts imply orthogonality against all polynomials of lower degree on[-1,1]; its norm there is2/(2l+1). Changing variables to x gives the displayed diagonal formula. The recurrence P_0=1, P_1=z, (l+1)P_(l+1)=(2l+1)zP_l-lP_(l-1) constructs every needed polynomial exactly. The numerical verifier independently checks this finite orthogonality matrix by rational monomial integration. Descending elimination is valid since the leading coefficient is nonzero. This supplies a separate exact nonnegative sum for Q_i. The two Q_i values and all density polynomial coefficient digests must agree. Agreement supplements the two derivations; it does not replace either proof.

Arb512 evaluates pi v(a_i)Q_i and pi v(b_i)Q_i by positive powers and square roots. mpmath.iv220 separately uses the logarithmic weight expression

    log(v(t))=6 log L+2t+(3/2-k)log(1+exp(2t)/L^2),

and reversed-order sums, then exp(log(sum)/2) for positive root sums. All saved endpoints are exact dyadic rationals. The lower endpoint of each lower-bound expression is a proved lower bound on the true global squared norm. The upper endpoint of a computed lower-bound expression is not necessarily a lower bound on the true norm. Publication therefore uses the smaller of the two root lower endpoints and a strictly downward terminating decimal. It must be positive and its exact square must be smaller than both lower square endpoints. Independent integer comparisons recheck every printed direction. Every root interval must enclose the square root of the associated exact endpoint expression as verified by the enclosing arithmetic; interval overlap is only an additional consistency check.

## Inverse-constant consequence and limits

Under the exact graph-domain theorem138, a constant C satisfying ||h||_X<=C||Lh||_X for all h in its stated normalized, zero-strain domain necessarily satisfies ||K||_X<=C||epsilon-D epsilon||_X. If a later FINAL certificate proves ||K||_X>q>0 and ||epsilon-D epsilon||_X<=b with b>0 for this same canonical trial and the same norm, then C>q/b. This is a necessary lower bound on constants in that broad domain, not an upper bound, an inverse existence result, or a claim for fixed-leading-tail spaces that exclude K. No number is substituted into this consequence until the numerator and denominator certificates and their same-trial linkage are independently reviewed as an actual application. The historical floating quotient near170 and the unverified13.07 estimate are not used as premises.

Freeze the actual source and exact span selection before numerical acceptance. Require all selected spans, both independent polynomial paths, both weight calculations, the integer output audit, complete parent pin rehashes, actual Claude Opus5.5 review and a later own adjudication. A source review or manufactured self-check is not numerical acceptance. Record any small preparation run separately. The result gives no distance to X3, nonlinear closure, existence, exclusion or decisive endpoint.
