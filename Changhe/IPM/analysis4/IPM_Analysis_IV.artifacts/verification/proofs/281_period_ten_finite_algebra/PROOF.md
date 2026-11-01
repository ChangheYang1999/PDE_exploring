# First compatibility polynomial at delta=1/5

Status: PROVED finite statement, admitted V582. Infinite convergence is a separate claim.

## Statement and notation

Let c=5/4, delta=1/5, p_n=1-n/5 and P_n=2-n/5. Take the real leading profile f_1(theta)=sin(theta)+b sin(3theta). For each n before the first positive sine resonance, define f_n by the stationary IPM recurrence and g_n by its zero-kernel Poisson inverse. Define O_20(b) to be the sin(theta) coefficient of f_20. Let P_20(b) be the primitive integer multiple of O_20 with positive leading coefficient, provided this polynomial is nonzero.

The finite calculation will determine P_20, its exact scalar relation to O_20, its degree, the number of its real roots, and rational isolating intervals. If the verified modular factor-degree test below succeeds, it will establish irreducibility over the rationals. Those facts establish only the compatible starting profiles. An infinite tuned continuation still needs the subsequent nonzero response conditions and a convergence proof.

## Derivation and proof

The stationary transport equation gives

    f_n = 4/(n-1) sum_(i+j=n) [(X g_i)(Y f_j)-(Y g_i)(X f_j)],

where X is Cartesian partial_x and Y represents partial_y/i in the signed Laurent convention of topic01. Each field is stored as a finite sum of signed angular frequencies times its fixed radial power. For a mode r^q exp(i m theta), X has coefficients (q+m)/2 and (q-m)/2 at frequencies m-1 and m+1. The artificial Y has the same first coefficient and the negative of the second. Consequently -Delta=-XX+YY, so the stream coefficient at frequency m is the corresponding coefficient of Xf_n divided by m^2-P_n^2. Every computed inverse is checked by applying -XX+YY and comparing exactly with Xf_n.

Inductively f_n is an odd sine polynomial with odd frequencies at most4n-1, g_n has even sine frequencies at most4n, and each coefficient has b-degree at mostn. The induction follows by differentiation and convolution: the density product has total order i+j=n, radial power P_i+p_j-2=p_n, and its degree is at most i+j. Division by a nonzero scalar independent of b preserves that degree.

Positive even stream modes can resonate only when |2-n/5| is positive even. The first such order is20, with stream mode2. Order10 has formal mode0, which is absent in the sine sector. Therefore all density coefficients through20 and all stream coefficients through19 are unambiguously determined. At order20, P_20=-2 as a radial exponent. The m=2 coefficient of Xf_20 receives the sin(theta) contribution with coefficient(p_20-1)/2=-2; the sin(3theta) contribution has coefficient(p_20+3)/2=0. Thus the exact Poisson compatibility is O_20(b)=0. There is one free stream coefficient at mode2 after this compatibility is satisfied.

Exact rational arithmetic gives O_20 and hence its primitive integer polynomial. A Sturm chain, with signs at both infinities and at every rational endpoint, proves the real-root count and isolates all roots. Endpoint evaluations exclude roots at interval boundaries; a squarefree Sturm calculation proves simplicity.

For irreducibility, take primes preserving the polynomial degree and having squarefree reductions. Factor each reduction into monic irreducibles. Independently check every factor by finite-field Frobenius identities and proper-degree gcd tests, then multiply the factors to recover the reduction up to its leading scalar. Any nonconstant rational factor would reduce to a product of these factors at every accepted prime, so its degree must belong to the subset-sum set at every prime. An empty intersection over degrees1 through19 excludes every proper rational factor. This test is decisive only if that intersection is actually empty.

The theory part uses a separate positive-frequency polar recurrence. Exact agreement on every polynomial coefficient and on its rational scale will be recorded separately. Approximate root values are descriptions of the isolated roots, not proof inputs.

## Dependencies and scope

Dependencies: topics01,05 and the independently checked signed Laurent recurrence in119. The implementation and all exact input/output data are retained under sources and verification. No all-index response bound, radius, genericity theorem, potential-logarithm coefficient or whole-plane extension follows from this finite calculation. For nonzero leading amplitude epsilon, homogeneity multiplies O_20 by epsilon^20, so the normalized compatibility roots remain the same.

## Completed verification

Admitted 2026-10-31T21:01:30+00:00. All21 polynomial coefficients and the exact obstruction scale agree. The modular factor-degree patterns [(31, [3, 17]), (41, [2, 2, 3, 13]), (59, [1, 1, 3, 7, 8]), (61, [1, 8, 11])] exclude every proper rational factor degree. Each of the fourteen roots is isolated to width at most1e-60. The190 ordered nonlinear products took1870.699459seconds. Primitive descending coefficient hash:c133c2f4811e855673ffa8f2572a1c04dc8eb1dbe9447779a386463aea6ed720.
