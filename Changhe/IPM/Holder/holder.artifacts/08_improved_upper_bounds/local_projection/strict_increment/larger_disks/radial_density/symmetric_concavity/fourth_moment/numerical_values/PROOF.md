# Directed upper endpoints with the symmetric reflection saving

## Statement and hypotheses

Use the real or complex homogeneous Euclidean Holder seminorm

    [f]_alpha = sup_(x != y) |f(x)-f(y)|/|x-y|^alpha,

on R^2, with 0<alpha<1. The diagonal operator is R_1^2=T_xx-I/2, with the circular principal-value kernel K_xx(z)=(z_1^2-z_2^2)/(2pi|z|^4) and the quotient extension modulo constants specified in the setup. Write D_alpha for its operator seminorm. All analytic hypotheses of the radial reflection and retained-edge lemmas are confirmed in the V195 acceptance in ../../../verification/accepted.json.

At alpha=1/1000 and 1/100, let U_alpha be the exact rational upper endpoint of J_D at the rational radius s=rho saved in the accepted V118 rational_cutoffs.json. These radii lie in (0,1/3]. At alpha=1/20 and 1/10, use the accepted exterior-circle bounds in data/circle_composite_upper_n768.json and s=1/2. At alpha=1/5,3/10,1/2,3/4,9/10,99/100, use the V190 cross2048 diagonal upper endpoint and s=1/2. All the latter bounds retain the local positive measure of mass 1/2 outside phase interpolation.

Define

    p=alpha(1-alpha), q=p(2-alpha)(3-alpha),
    J=653/288-(63/8)log(4/3),
    K=(1/2) integral_0^(1/4) t^5(1-32t^2/9)/(3/4+t)^2 dt.

For the cutoff rows put

    c_2=s^4/[512(1-s)^2], c_4=s^6/[49152(1-s)^2].

For every other row put c_2=c_4=0. The confirmed reflection lemmas imply

    D_alpha <= U_alpha - eta_2 - eta_4,
    eta_2=p(Js^2-c_2), eta_4=q(Ks^4-c_4).

Both savings are strictly positive. In the cutoff rows, their density is the guaranteed surviving w-H, not the full Q density. In the other rows, they replace only the translation cost of a radial submeasure; the local singular, cross, middle and far terms and every identity atom are unchanged. No correction is subtracted twice. The scalar calculation compares both the quadratic and quartic endpoints, but selects the stronger quartic bound.

## Exact coefficient evaluation and directed rounding

The formula in ../PROOF.md writes K=(B_5-(32/9)B_7)/2 as a rational linear expression in log(4/3). The coefficient of that logarithm is -729/512. The defining integral proves K>0 independently of cancellation in this expression.

Enclose log(4/3) by a ball at384 bits. Separately compute256 exact rational terms of

    log(4/3)=2 sum_(n>=0) (1/7)^(2n+1)/(2n+1),

with positive remainder at most

    2(1/7)^(513)/[513(1-1/49)].

Use the signs of each rational coefficient to propagate this rational interval through J, K and the two savings. Those exact rational enclosures must lie inside the384-bit ball enclosures. A separate768-bit logarithm and independently regrouped moment evaluation must also lie inside the first enclosures. All radii, exponents, p, q and density corrections are exact rationals.

If ell is the lower endpoint of the384-bit enclosure of eta_2+eta_4, then U_alpha-ell is an upper bound. Its ceiling at ten decimal places is checked by an exact rational inequality. The quadratic-only endpoint is computed with the same rule for comparison. All source certificates, their transitive input hashes, the confirmed analytic proofs, this proof and the scalar program are registered in accepted.json. No new quadrature or transport optimization is required.

## Scope

The accepted file, when produced, proves only the finite listed endpoints. The all-exponent analytic inequalities are in the parent proofs. A heuristic value is never substituted for an interval endpoint. The numerical run is conditional on all hash checks and directed comparisons succeeding.
