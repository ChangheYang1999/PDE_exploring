# Axis leakage in the quadrant Euler-derivative saddle norm

Date 2026-10-22T03:05:37.606661+00:00. Proof written before the new exact working-weight check and actual review. Status OPEN until the parent pins, complete actual Claude Opus5.5 review and later own adjudication are recorded.

## Exact statement and dependencies

For real a,b and an integer m>=0, let Z_(a,b,m) be the functions on the open quadrant Q={x>0,y>0} whose distributional Euler derivatives have finite norm

 ||f||_Z^2=sum_(i,j>=0,i+j<=m) integral_Q x^(-2a)y^(-2b)
                       |(x partial_x)^i(y partial_y)^j f|^2 dxdy.

In particular the sum includes i=j=0. No completeness or closed realization is asserted here. Fix the full PLUS-strain linearization and any background satisfying axis_weighted_nonlocal_mapping/PROOF.md, including the exactly joined canonical modal trial. There exists a single smooth compact even-x/odd-y h with a smooth global x^2y factor, supported in1<r<2 at positive distance from both axes, with J(h)=Sigma(h)=0, such that its quadrant restriction belongs to Z_(a,b,m) for every fixed finite a,b,m, but the restriction of L_rho h does not belong to Z_(a,b,m) whenever a>=5/2, for every finite real b and every integer m>=0.

This includes the working weights a=129/20, b=307/100. The result refutes mapping of the whole stated smooth compact test class. It does not refute an inverse on a smaller domain which requires image membership, or supply any PDE endpoint.

## Complete argument

Use the exact h constructed in axis_weighted_nonlocal_mapping. That accepted proof gives a closed positive y interval [y1,y2], with0<y1<y2, and constants x1,c>0 such that g=L_rho h satisfies g(x,y)>=c x^2 for0<x<x1 and y1<=y<=y2. The proof uses the exact positive sin3/sin5 Gram determinant, the nonzero interior quartic moment, and the differentiated background expansion. All angular modes are retained. Its parent verdict and181 inherited pins must be freshly rehashed before the canonical application is accepted here.

For any real b, the continuous positive function y^(-2b) on[y1,y2] is bounded below by

 d_b=min(y1^(-2b),y2^(-2b))>0.

This formula follows from monotonicity of the real power (constant if b=0). Since the zeroth summand is part of the nonnegative norm sum, any f in Z satisfies

 ||f||_Z^2 >= d_b integral_(y1)^y2 integral_0^x1
                                         x^(-2a)|f(x,y)|^2 dxdy.

Applying this lower bound to g gives the divergent extended integral

 d_b c^2(y2-y1) integral_0^x1 x^(4-2a)dx=+infinity

when a>=5/2. At the endpoint the integral is logarithmically divergent. Thus even the zeroth summand fails, regardless of how higher Euler derivatives are interpreted. No existence of those higher derivatives of g is assumed or needed for the exclusion.

On the other hand h is smooth compact and supported away from both axes. Every finite Euler derivative of h has the same compact support. The weight is smooth positive and bounded there, so every integral in its finite norm sum is finite, for arbitrary finite a,b and m. The accepted construction already provides parity, factor and the two exact normalization cancellations.

For a=129/20, the x-integrand exponent is4-2a=-89/10<-1. The value b=307/100 affects the positive finite constant d_b but not convergence in x. This directly answers the proposed quadrant-norm corollary without any additional numerical enclosure.

## Verification and scope

The proof is independent of any frozen inverse estimate and uses only the parent192 rectangle lower bound. A new exact rational check will record the working exponent and threshold; it is bookkeeping, not proof of the analytic lower bound. The latter is supplied explicitly above and inherited from the accepted parent. Actual model review is additional adversarial scrutiny, not a replacement for either argument.

This result concerns the sum norm as defined, on the open quadrant with no Taylor subtraction. It does not automatically cover a quotient norm, prescribed axis jets, a different residual variable, weaker image norms, or an inverse on an image-compatible subdomain. It is not nonexistence of stationary profiles or an exclusion neighborhood of X3. No decisive endpoint follows.
