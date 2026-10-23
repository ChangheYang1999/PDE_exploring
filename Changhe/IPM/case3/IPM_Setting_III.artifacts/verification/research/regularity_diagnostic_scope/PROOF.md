# Scope of quotient slopes and cubic-jet regularity diagnostics

Written 2026-10-21 UTC before the supporting evaluator. This is verifier result 104.

## Statement and scope

Fix ell > 1, put D = ell - 1 and a = 4D. There are canonical density and velocity pairs with the Setting III parities, rho_y(0) = a, psi_xy(0) = -D and compactly supported density such that:

1. A smooth density has zero cubic density coefficients and its radial quotient q = rho/(a y), extended to the x-axis, satisfies
   d log(1-q)/d log r -> 4 at zero.
2. A family of smooth densities converges in C^4 on compact sets to a density which is not C^5 at zero. Its two cubic coefficients converge to zero, whereas its quintic coefficient diverges. The limiting quotient slope tends to 7/2, which exceeds two. All its angular quotient coefficients except the constant coefficient vanish identically.

The velocity is always obtained from the full-plane canonical inverse. The center normalization is exact and a is a fixed nonzero invariant. These are examples in the ambient canonical, normalized class, not profiles: their transport residual is nonzero. They refute universal inferences about regularity from a slope of two, cubic-jet divergence or an algebraic angular tail. They do not refute any separately proved consequence for exact IPM profiles. In particular they do not establish the regularity or limiting behavior of the computed IPM sequences.

## Notation and dependencies

Let r = sqrt(x^2+y^2). Choose a nonnegative smooth function chi on [0,infinity), equal to one on [0,1], equal to zero on [4,infinity), and at most one. It is evaluated at r^2. Such a function can be obtained from exp(-1/t) for t > 0, extended by zero for t <= 0, using the quotient of two translates whose sum is positive.

For a radial quotient q, write

    rho(x,y) = a y q(r),
    J(r) = r^(-4) int_0^r s^3 q(s) ds
         = int_0^1 u^3 q(ur) du,
    psi(x,y) = -a x y J(r),     U = (-psi_y, psi_x).

For j derivatives, C^j convergence means uniform convergence of every Cartesian partial derivative of order at most j on each fixed compact set. The cubic density coefficients b,e are defined by rho = a y + b x^2 y + e y^3 + terms of degree at least five.

The proof uses elementary differentiation, finite Taylor expansions, an integral estimate in a smoothing parameter, and Liouville's theorem for harmonic functions of sublinear growth. No claim about a solution of the transport equation is assumed.

## 1. Canonical inverse and the center data

For r > 0 the identity r J' + 4J = q implies

    J'' + 5J'/r = q'/r.

Since Delta(x y J) = x y (J'' + 5J'/r), we have

    -Delta psi = a x y q'(r)/r = rho_x.

For a smooth radial q, the integral over u proves that J(|X|) is smooth at zero. If q(0)=1 then J(0)=1/4, so psi_xy(0) = -a/4 = -D and rho_y(0)=a. The required parities are immediate. The stream formula, rather than an arbitrarily imposed harmonic strain, gives this center value.

When q has compact support, J = C r^(-4) beyond its support, hence psi = O(r^(-2)) and U = O(r^(-3)); the differentiated estimates follow directly there. The density and its first derivatives obey the required sublinear bound for every 0 < gamma < 1. If two full-plane velocities obey these Poisson, divergence, parity and sublinear conditions, their difference has harmonic components of sublinear growth. A harmonic function h=o(r) has zero gradient: its interior gradient estimate on a disk of radius R about any fixed point is at most C R^(-1) sup |h|, which tends to zero. Thus the difference is constant. Each component's odd parity removes that constant. This proves that the displayed inverse is the canonical one.

For the finite-regularity limit below, the same formula is interpreted classically with its available derivatives. It still gives a canonical velocity; no assertion that the limit is in the primary C-infinity class is made.

## 2. Smooth example with limiting quotient slope four

Take

    q_s(r) = chi(r^2) exp(-r^4).

Near zero, q_s = 1 - r^4 + O(r^8), so b=e=0. In 0 < r < 1,

    s_s(r) := r d/dr log(1-q_s(r)) = 4r^4/(exp(r^4)-1) -> 4.

The field rho_s is smooth, compactly supported, even in x and odd in y. Section 1 supplies its exact center normalization and canonical inverse. Consequently smoothness alone does not require slope two. A nonzero quadratic term in 1-q would supply slope two on a direction where that term is nonzero; that additional hypothesis is essential.

## 3. A smooth family with a C^4, non-C^5 limit

Set alpha = 7/2 and beta = alpha/2 = 7/4. For epsilon > 0 let

    q_epsilon(r) = chi(r^2) exp(-[(r^2+epsilon^2)^beta-epsilon^alpha]),
    rho_epsilon = a y q_epsilon(r).

All members are smooth, q_epsilon(0)=1 and 0 <= q_epsilon <= 1. They have the same compact support and the same a and c. Their pointwise limit is

    q_0(r) = chi(r^2) exp(-r^alpha),     rho_0 = a y q_0.

We prove C^4 convergence, rather than inferring it from the pointwise formula. Put tau = epsilon^2 and u = r^2+tau. On any fixed disk and for 0 < tau <= 1, each Cartesian derivative of u^p of order j is bounded by C u^(p-j/2). This follows by differentiating a finite sum of terms X^nu u^(p-k) and using |X| <= sqrt(u). The same argument, with the extra factor y, gives

    |D^j[y u^(beta-1)]| <= C u^(beta-1/2-j/2).

Here and below D^j can be any ordered Cartesian derivative of order j. By repeated product and chain rules, a positive-order derivative of exp(-u^beta) is a finite sum whose absolute value is at most a constant times

    sum_{p=1}^j u^(p beta-j/2) exp(-u^beta).

Indeed a term with p derivatives of the exponential's scalar argument contains p derivatives of u^beta with total derivative order j. The estimate follows by multiplying their bounds. It also shows that the derivatives of y exp(-u^beta) through order four are bounded uniformly on the disk: the smallest exponent in a term where the exponential is differentiated is beta + 1/2 - j/2 >= 1/4, and the remaining undifferentiated terms are bounded.

Differentiating rho_tau in tau gives

    partial_tau rho_tau = a beta y chi(r^2) exp(-u^beta+tau^beta)
                         [tau^(beta-1)-u^(beta-1)].

The term with tau^(beta-1) has bounded Cartesian derivatives of order at most four by the preceding estimate. In the second term, the product-rule term with no derivative on the exponential has exponent beta-1/2-j/2. Every term with derivatives on it has that exponent plus p beta for some p >= 1. On a fixed disk these latter powers obey the same upper estimate up to a disk-dependent constant. Derivatives on chi only reduce the derivative order on this product and are bounded. Therefore, for 0 <= j <= 4,

    ||D^j partial_tau rho_tau||_infinity <= C [1+tau^((alpha-1-j)/2)].

For a nonnegative exponent the constant one bounds u to that power on the disk; for a negative exponent u >= tau gives the stated bound. The worst exponent, at j=4, is -3/4, which is integrable at zero. Integration in tau shows that all derivatives through order four are uniformly Cauchy. Their limits are the derivatives of the pointwise limit, by successive applications of the fundamental theorem of calculus on line segments. This proves C^4 convergence on compact sets. The same estimate gives an O(epsilon^(1/2)) bound for the fourth derivatives, with no claim that this rate is sharp in every component.

On the positive y-axis near zero,

    rho_0(0,y) = a y - a y^(alpha+1) + O(y^(2alpha+1)).

Five differentiations for y>0 give a nonzero constant times y^(alpha-4) in the second term, which diverges as y decreases to zero. The remainder and its first five derivatives have higher powers, as follows by the convergent exponential series for positive y. Hence rho_0 is not C^5 at zero.

## 4. The cubic and quintic coefficients

For fixed epsilon > 0 the ordinary expansion in r^2 is

    q_epsilon = 1 - beta epsilon^(alpha-2) r^2
      + [beta^2/2 epsilon^(2alpha-4)
         - beta(beta-1)/2 epsilon^(alpha-4)] r^4 + O_epsilon(r^6).

The cutoff is identically one here. It follows that

    b_epsilon = e_epsilon = -a beta epsilon^(alpha-2) -> 0.

The coefficients of x^4 y and y^5 both equal a times the bracketed expression. Since alpha-4 = -1/2 and 2alpha-4 = 3, they diverge to negative infinity. The x^2 y^3 coefficient is twice this number. Thus the failure of fifth-order regularity is compatible with convergent, vanishing cubic coefficients.

For 0 < r < 1 the limiting quotient slope is

    s_0(r) = alpha r^alpha/(exp(r^alpha)-1) -> alpha = 7/2.

For each fixed positive epsilon, in contrast, the nonzero quadratic term implies s_epsilon(r) -> 2 as r -> 0. These two limiting operations need not commute. At every fixed r the quotient is independent of angle, so all its nonconstant angular Fourier coefficients vanish. Finite regularity at the origin need not produce an algebraic angular Fourier tail at a fixed positive radius.

## 5. Explicit check that these fields are not profiles

For a radial quotient with

    q(r) = 1 - K r^p + higher terms,       K > 0, p > 0,

the inverse from Section 1 gives

    psi = -a x y/4 + a K x y r^p/(p+4) + higher terms.

With a=4D and A=2D+1, the center field is (A x,y). Direct differentiation in the punctured plane gives the leading transport residual

    R = (ell X+U).grad rho-rho
      = a K y r^(p-2)
        {[-p A + a(p+1)/(p+4)] x^2 + [-p+a/(p+4)] y^2}
        + higher terms.

For the examples above their smooth or positive-radius expansions may be differentiated to this order, so the remainder is smaller in each fixed non-axis direction. Both displayed coefficients cannot vanish. The second would require a=p(p+4); the first would then require A=p+1, hence D=p/2 and a=2p. The two equalities for a give p=-2, contrary to p>0. Thus R is not identically zero.

Apply this calculation with p=4, K=1 for rho_s; with p=2, K=beta epsilon^(alpha-2) for each rho_epsilon; and with p=alpha, K=1 for rho_0. This explicitly rules out any unintended profile claim without relying on a prior radial nonexistence theorem.

## Verification and use

The supporting checker must independently expand the rational-power exponential, differentiate Cartesian polynomials for the Poisson identity, check the center data, check the leading residual coefficients and dilation covariance, and retain exact outputs. It supports finite identities; the regularity and limiting arguments above are informal proofs, not a consequence of a finite test.

The producer's derivative diagnostic uses finite differences on finite radial windows. Its sampled eta_k values must be accompanied by absolute numerator and denominator norms, resolution and step refinement, and a distinction between full-plane inverse evaluation and finite-window norm integration. This proof makes no universal inference from eta_k to regularity. A shrinking or rising ratio can have several causes; additional compactness and residual estimates are needed to make a claim about an exact limiting profile.
