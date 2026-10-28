# Whole-plane residual norms from exact compactified polynomials

## 1. Scope and inputs

The input is an exact rational potential

    chi = sum_(j,m,k) a_(j,m,k) r^(2k) (1+r^2)^(p_j-k) cos(2m theta),
    p_j=(3+gamma-j delta)/2, gamma=1/c, delta=1-gamma,

where the sum is finite, c is rational, 0<delta<1, and k>=m>=0. Define rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy), and the actual residual F=(cX+U).D rho-rho. All derivatives and norms in this result are those of F, including its nonlinear term, not a truncated asymptotic residual. Tensors count all ordered derivatives. Set omega=(1+4r^2)^(2/5).

The procedure below either detects a nonintegrable sector or gives certified bounds for

    ||rF||2, ||F||2, ||DF||2, ||omega D2F||2, ||omega D3F||2.

For odd-in-y F the first quantity bounds ||F||_Hdot^-1. Therefore the finite bounds give an upper bound E for E2(F), and an upper bound Q for ||omega D3F||2. The inequality in 09_quasilinear/PROOF.md then gives a certified N_s(F) upper bound. An infinite proxy alone is not a proof that the Hdot^-1 norm is infinite, but a nonzero pure-power sector with exponent at least -2 gives the separate negative-order obstruction already proved in 05_tails/PROOF.md.

## 2. Exact compactification and differentiation

Put t=r^2/(1+r^2) in [0,1], w=(1-t)^(delta/2). Direct polar differentiation gives every component of D^dF, for d=0,1,2,3, in the form

    f_d(t) sum_(ell,n,kind) w^ell P_(d,ell,n,kind)(t) T_(n,kind)(theta),
    f_d=t^(a_d)(1-t)^((d-1)/2),
    a_d=1/2 for even d, and a_d=0 for odd d,

where all P are polynomials with exact rational coefficients and T is sine or cosine. Each tensor component has one trigonometric parity. The initial expression d=0 follows from the exact third and fourth derivatives of chi and multiplication of finite trigonometric polynomials. It includes all cross terms.

For clarity, differentiating one term f_d w^ell P(t) T(theta) has radial and angular factors relative to f_(d+1) w^ell:

    d even: Rad(P)=[1-(d+ell delta)t]P+2t(1-t)P', Ang(P)=P;
    d odd:  Rad(P)=-(d-1+ell delta)P+2(1-t)P', Ang(P)=P/t.

Then use partial_x=cos(theta) partial_r-sin(theta) r^-1 partial_theta and partial_y=sin(theta) partial_r+cos(theta) r^-1 partial_theta, with exact product-to-sum identities. At the odd step the nonconstant angular coefficients vanish at t=0, so the apparent P/t has no pole. This is checked as an exact polynomial identity before integration. The zero-frequency angular derivative vanishes. Negative modes are folded using sine oddness and cosine evenness.

## 3. Infinity factors and integrability

For each nonzero polynomial P extract exactly its full factor (1-t)^q by rational polynomial division, obtaining P=(1-t)^q Q with Q(1) nonzero. The resulting term has exact order at infinity determined by q, ell and d. For a fixed angular component, distinct powers can be grouped before testing integrability. In the checkpoint and refit inputs, distinct ell in the finite range cannot differ by an even integer divided by delta; this exact nonresonance test prevents a missed cancellation between separate ell groups.

The full-plane polar measure is

    r dr dtheta = dt dtheta/[2(1-t)^2].

Orthogonality of the trigonometric modes gives angular square integral pi, except the constant cosine, which gives 2pi. The tensor multiplicity of partial_x^i partial_y^(d-i) is binomial(d,i). Thus the square of any norm reduces to finitely many one-dimensional cross integrals. A cross product of ell and ell' has rational radial exponent

    b = d-3 +(ell+ell')delta/2 +q+q',

and integer t factor t^(2a_d). For ||rF||2 include one additional t/(1-t). For the omega-weighted norms include (1-t)^(-4/5)(1+3t)^(4/5).

If the square of the leading nonzero power has b<=-1, its radial integral diverges. Equality is logarithmic divergence. Otherwise all cross integrals are integrable, since their endpoint exponent is the arithmetic mean of the corresponding two diagonal exponents. The origin causes no additional difficulty because all remaining t powers are nonnegative and F is smooth there.

## 4. Exact beta integrals, with a rigorous bound for the residual weight

For rational b>-1 and integer n>=0,

    int_0^1 t^n(1-t)^b dt = n! / [(b+1)(b+2)...(b+n+1)].

This follows from integration by parts, starting with n=0. The value is rational. Consequently every unweighted cross integral can be evaluated exactly as a rational number, with no quadrature error. Cancellation between large polynomial coefficients occurs in exact arithmetic before the final multiplication by pi.

For the remaining positive factor g(t)=(1+3t)^(4/5), write

    g(t)=(5/2)^(4/5) (1+z)^(4/5), z=(6t-3)/5, |z|<=3/5.

Let G_N(t)=sum_(n=0)^N binomial(4/5,n) z^n. For N>=1, the absolute ratio between successive binomial coefficients is less than one. Hence

    |g(t)-(5/2)^(4/5)G_N(t)|
      <= (5/2)^(4/5) |binomial(4/5,N+1)| (3/5)^(N+1)/(1-3/5).

The square of the original residual expression, with the positive rational-power radial measure, is nonnegative. Integrate this uniform error bound against that square, whose integral is another exact rational beta sum. This yields a rigorous interval for the weighted norm squared. It does not bound cross terms separately by their absolute values. The polynomial degree N is increased if the desired relative error has not yet been achieved. The prefactor and pi are enclosed using arbitrary-precision ball arithmetic.

## 5. Certificate and audit requirements

A certificate records the source hash, exact compactified polynomials, the extracted endpoint factors, exact integrability comparisons, rational beta sums, truncation degree, weight error bound, arithmetic precision and outward interval results. The source canonical coefficients are independently recovered from the original state or independently expanded from a refit before this computation.

The residual and each derivative polynomial must also be compared at rational Cartesian points with direct differentiation of the potential, with explicit finiteness checks. This detects a wrong derivative or parity convention. An independent audit recomputes the endpoint factors, integral sums and uniform weight error at higher precision. Finite-point comparison alone is not the norm proof: exact polynomial identities, endpoint tests and the beta integration establish the whole-plane claim.

## 6. Relation to the nonlinear theorem

When all required components are finite, let L0,L1,L2,H0 be certified upper bounds for ||F||2, ||DF||2, ||omega D2F||2, ||rF||2. Then

    E^2 = L2^2+2^14 L1^2+2^18 L0^2+2^18(20/21)H0^2

is a certified E2(F) upper bound. With Q bounding ||omega D3F||2,

    N_s(F) <= E^(1-s)(2Q^2+16410E^2)^(s/2)+34sE.

These are sufficient upper bounds; using ||rF||2 can be less sharp than evaluating Hdot^-1 directly. A failed bound or a divergent proxy never establishes nonexistence of a nearby profile.
