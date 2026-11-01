# Validated Taylor enclosures of the compact response

Status: PROVED, independently reviewed by the theory part at 17:24Z and admitted as V482. The 28 rational-function arithmetic checks passed. The IPM probe produced a separated degree-two enclosure on [0,1/28160] at 768 bits; this is a local enclosure, not yet a complete response certificate. This changes the enclosure algorithm, not the response being certified.

## Statement

Let I=[a,b] be a compact real interval, m=(a+b)/2, r=(b-a)/2, and let S be a real rational expression whose intermediate denominators are nonzero on I. Its fixed coefficients may depend on parameters in a validated box. Suppose directed interval arithmetic on truncated Taylor jets produces intervals c_j enclosing S^(j)(m)/j! for0<=j<d, and an interval E enclosing S^(d)(t)/d! for every t in I, uniformly in that parameter box. Then the interval obtained by evaluating

    c_0+c_1 x+...+c_(d-1) x^(d-1)+E x^d,  x in[-r,r],

contains S(t) for every t in I. In particular, an absolute lower bound greater than s for this interval proves |S(t)|>s on I. This interval can certify a nonempty leaf in the response-cover arguments149,223,227,232.

## Derivative enclosures from jets

A jet stores coefficients through degree d in a formal variable u. Initialize the independent variable as t+u, with t either the point m or the interval I. Fixed coefficients have only a constant component. Add and multiply jets by the truncated power-series formulas. For division A/B, when the interval B_0 excludes zero, define recursively

    C_0=A_0/B_0,
    C_n=(A_n-sum_(j=1)^n B_j C_(n-j))/B_0.

For every fixed admissible parameter and t, ordinary analytic power-series algebra gives exactly these coefficients for S(t+u). Induction through the expression tree and directed interval inclusion show that the computed coefficient n contains S^(n)(t)/n! for every t in the selected input interval. Parameters are held fixed when differentiating; their validated uncertainty is propagated as constant interval coefficients.

Every denominator test must apply to its constant interval component over I. If that component contains zero, the enclosure is not admitted by this procedure. Subdivision may resolve the test; otherwise the leaf remains open. Division of a merely nonzero midpoint is insufficient.

## Taylor remainder

The stated denominator condition makes S smooth on I. For each t=m+x in I, Taylor's theorem with its real Lagrange remainder gives

    S(m+x)=sum_(j=0)^(d-1) S^(j)(m)x^j/j! + S^(d)(xi)x^d/d!

for some xi between m and m+x. The coefficient intervals contain every term on the right. Directed polynomial evaluation therefore contains S(t), uniformly over I and the parameter box. Interval dependency can enlarge this result, but cannot invalidate inclusion.

When S is the compact response, its expression contains only additions, products and rational divisions of the finite prefix and t. The jet construction thus applies directly. Low-coefficient enclosures and the proven carrier identity retain their original roles. A Taylor leaf still needs an exact partition and integer-range audit. A replay may use a higher precision and independently verify that the new enclosure excludes [-s,s]; overlap of old and new enclosures alone does not prove the bound.

## Scope

This is a real-interval inclusion theorem, not a power-series convergence claim for the full IPM solution. It neither assumes that S has no noninteger zeros nor removes the need to check each admissible integer. It supplies one rigorous way to reduce overestimation when evaluating a cancellation-heavy finite expression.
