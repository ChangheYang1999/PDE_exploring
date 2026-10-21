# Obstruction accounting when the first axis equation has a residual

Date: 2026-10-20. Status: complete informal proof, independent review pending. This is an identity for supplied axis functions, not a coupled existence theorem or a certified numerical obstruction measurement.

## Statement, hypotheses and notation

Fix A>2, beta=2/A, p=6+beta and L>0. Let w,g be smooth on [0,L], analytic near the endpoints, with w odd and g even near zero, and assume

    w=-Ax+O(x^3),  g=x^2+O(x^4) as x -> 0,
    w<0 on (0,L),  g>0 on (0,L],
    w(L)=0,  w'(L)=A,  g(L)=g_*>0.

The first axis equation is not assumed. For a smooth trace G that is even analytic near zero, define

    r_1=w g'-(w'-A)g,
    Q=(g'-w'')/(2g^3),   F=g^4 Q'/3,
    r_3=w G'-(3w'-3A-2)G-F,
    m=-w/g,   H=A^beta g^3 m^(-beta).

In particular H/x^p tends to one at zero. Finite parts below are defined in the original x coordinate by subtracting all divergent center powers, with no added constant. Put

    B_F = -FP integral_0^L F/(wH) dx,
    B_Q = (beta-1) A^(1-beta)/3
          * FP integral_0^L (Q-Q(L))m^(beta-2)/g dx,
    D_1 = (beta-1)/(3A^beta)
          * FP integral_0^L (Q-Q(L))r_1 m^(beta-2)/g^2 dx.

Then all three quantities exist and

    B_F = B_Q-D_1,                                      (1)
    B_Q = D_1 + FP integral_0^L
          [r_3-(3+beta)r_1 G/g]/(wH) dx.                 (2)

When r_1=0 these reduce to the usual axis functional and the residual identity of ../axis-residual/PROOF.md. When r_1 is nonzero, H need not be the homogeneous solution of the actual third equation, and B_F or B_Q cannot silently be interpreted as its connection coefficient.

If, in addition, r_1 and r_3 vanish on a neighborhood of zero, every residual integral on the right of (2) is an ordinary absolutely convergent integral. Consequently

    |B_Q| <= (1-beta)/(3A^beta)
             * integral_0^L |Q-Q(L)| |r_1| m^(beta-2)/g^2 dx
             + integral_0^L |r_3-(3+beta)r_1G/g|/|wH| dx. (3)

The vanishing assumption in (3) is sufficient, not asserted necessary. Without adequate center cancellation, a finite part is not an integral of a positive measure and one cannot apply this absolute-value estimate to it.

## Two exact logarithmic derivative identities

Since m=-w/g, direct differentiation and the definition of r_1 give

    m'=(-w'g+w g')/g^2=-A/g+r_1/g^2,
    g'/g=(w'-A)/w+r_1/(wg).

It follows that

    H'/H=(3+beta)g'/g-beta w'/w
         =(3w'-3A-2)/w+(3+beta)r_1/(wg).                (4)

For Z=G/H, equations (4) and the definition of r_3 yield

    Z'=[F+r_3-(3+beta)r_1G/g]/(wH).                    (5)

Thus omitting the r_1 term changes the exact accounting even when all derivatives of the supplied functions are computed exactly.

## Endpoint terms in (5)

At zero, m=(A/x) times a positive even analytic function equal to one there. Hence H=x^p times an even analytic function equal to one. The expansion of Z has exponents 2n-p. Since 6<p<7, none is zero. Its finite constant at zero is therefore zero. At L, m=(A/g_*)(L-x)(1+O(L-x)) and H is a positive constant times (L-x)^(-beta)(1+O(L-x)). Bounded G implies Z tends to zero.

The separate integrals in (5) have finite parts. At zero, F and r_3 are even analytic, and r_1=O(x^4) is even analytic. Since G/g has at worst a double pole with even Laurent powers, the numerator is an even Laurent series with no odd powers. Division by wH gives powers 2n-7-beta, whose primitives have nonzero exponents 2n-6-beta. There is no logarithm. At L, F,r_3,G and g^(-1) are bounded, r_1=O(L-x), and 1/(wH)=O((L-x)^(beta-1)), which is integrable. Integrating (5) and using these two endpoint values proves

    B_F = FP integral_0^L [r_3-(3+beta)r_1G/g]/(wH) dx. (6)

## Integration by parts without the first axis equation

The algebraic definitions, without using r_1=0, give

    wH=-A^beta g^4 m^(1-beta),
    F/(wH)=-Q'm^(beta-1)/(3A^beta).

Use Q-Q(L) for integration by parts. At L, its product with m^(beta-1) is O((L-x)^beta) and tends to zero. At zero, Q is an odd Laurent series beginning no worse than x^(-5). The product (Q-Q(L))m^(beta-1) has two types of exponents:

    -4-beta+2n,  and  1-beta+2n.

No exponent is zero because 0<beta<1. Its finite constant is zero. Both boundary terms are therefore justified. Using m'=-A/g+r_1/g^2 gives

    FP integral Q'm^(beta-1)
      = (beta-1)A FP integral (Q-Q(L))m^(beta-2)/g
        -(beta-1) FP integral (Q-Q(L))r_1m^(beta-2)/g^2.

Multiplying by 1/(3A^beta) proves (1). Combining (1) with (6) proves (2).

For completeness, these last two finite parts also exist separately. Their center expansions again consist of powers with noninteger exponents and hence no logarithmic primitive. At L the B_Q integrand is O((L-x)^(beta-1)), while the D_1 integrand is O((L-x)^beta), since Q-Q(L)=O(L-x) and r_1=O(L-x). Both are integrable. Under the additional assumption preceding (3), the residual integrands vanish near zero and are integrable at L by these estimates. The triangle inequality proves (3).

## Consequence for numerical use and scope

The identities identify two distinct first-equation error terms: the defect of the explicit integrating factor in (4), and the correction D_1 in the integration-by-parts formula. Evaluating a formula derived under r_1=0 on inexact axis data does not remove them. Small ordinary norms of r_1 or r_3 alone do not justify omitting singularly weighted integrals. The earlier cutoff example already disproves such a bound even when r_1=0.

This proof does not assert that a numerical trial satisfies the endpoint assumptions, that its errors vanish near zero, or that its finite-part values are stable or certified. It does not replace the endpoint regularity analysis for a genuine solution. Its dependencies are the stated definitions, Taylor and Laurent expansions of analytic functions, ordinary differentiation, and integrations by parts with the endpoint terms checked above.

Verification evidence consists of independent symbolic identities for general formal w,g,G and a manufactured explicit analytic pair with r_1 nonzero. Any supplementary finite-part quadrature is a diagnostic, not a proof. No numerics-lane program is imported.
