# A sharper rational Poisson norm

Status: PROVED. Independent theory-part review dated2026-10-31T12:56Z closes the analytic audit; exact finite certificates are retained. See V327.

## Statement

Let h and Q be positive integers with 2h<Q and delta=2h/Q. At order n>=1 set P=2-n delta. For an S1 sine polynomial f, let Pi_n f be its angular Poisson inverse after deleting every resonant output frequency entirely. On nonresonant orders this is the usual inverse. In the sine coefficient l1 norm,

    ||Pi_n f||_1 <= L_Q ||f||_1,
    L_Q = 3 Q^2/[4(3Q-1)].

The estimate is uniform in n and in angular bandwidth. It is smaller than Q/2. At delta=4/9 the bound L_9=243/104 is attained by f=sin(3 theta) at n=13, so no smaller uniform operator constant is possible for that exponent.

This is a bound on the particular inverse, not on independently added harmonic stream coefficients. The latter retain their separate eta variables in the rational majorant.

## Proof

For one input sine mode sin(l theta), l positive and odd, cancellation in the quadratic Poisson multiplier gives the following two possible outputs:

    sin((l-1)theta): 1/[2(l-1-P)],
    sin((l+1)theta): -1/[2(l+1+P)].

The first output is absent when l=1. Any resonant output is deleted before using these formulas. For each retained output its linear denominator is nonzero. Since P=2-2hn/Q and l is odd, both linear denominators belong to (2/Q)Z. Each therefore has modulus at least d=2/Q.

For l=1 there is just one output, so its coefficient sum is at most1/(2d)=Q/4<L_Q. For l>=3 put u=l-1-P and v=l+1+P, so u+v=2l. If one of the outputs is deleted, the same one-output bound applies. Otherwise |u|,|v|>=d. When u and v are positive, u lies in[d,2l-d], and the convex function 1/u+1/(2l-u) is largest at an endpoint. When one is negative, write u=-w with w>=d; then 1/|u|+1/|v|=1/w+1/(2l+w), which is smaller than the same endpoint bound. Both cannot be negative. Hence

    (1/2)(1/|u|+1/|v|)
       <= 1/(2d)+1/[2(2l-d)]
       <= Q/4+Q/[4(3Q-1)]
       = L_Q.

The triangle inequality over input modes proves the operator bound. At delta4/9, n13, P=-34/9 and l3, the two output coefficients are9/104 and-9/4. Their absolute sum is243/104, proving attainment.

## Use in the convergence theorem

The only use of L=Q/2 in the majorant inequalities131 and145 is the uniform bound on the particular Poisson inverse. Replacing L by L_Q preserves each inequality, every nonnegative generating shift and the strictly triangular zero-level map. The same replacement is valid in the independently bounded initial-coefficient extension168. Any exact box computed with this smaller constant proves the same convergence and derivative conclusions once its other hypotheses are checked. This substitution does not alter the tuning responses or their required positive lower bound.

## Verification plan and scope

Recompute each input column from the original quadratic multiplier, including explicit deletion of singular outputs, and compare it with the canceled expressions using exact fractions. Check the bound over several rational exponents and finite orders, and check exact attainment at delta4/9,n13,l3. These finite tests verify the implementation; the all-order proof is the preceding lattice and convexity argument. The result does not estimate canonical logarithmic inverses or prove a global stationary extension.

## Completed finite verification

The exact program checks8,564 retained coefficients over ten rational exponent pairs, through order4Q and input frequencies through4Q+1. Every original quadratic multiplier agrees with the canceled formula and every column obeys the bound. The4/9 equality case is reproduced. Actual elapsed time0.3618618310429156 seconds.

## Review closure

The theory part independently checked the complete argument at12:56Z and reproduced the dyadic certificates using a separate Fourier implementation. Earlier pending-review statements above record their original status; V327 closes that review for this topic. The separate resonance-period and longer-prefix extensions require their own reviews.
