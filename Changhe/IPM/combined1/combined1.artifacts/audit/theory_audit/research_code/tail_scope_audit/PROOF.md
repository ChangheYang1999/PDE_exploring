# Audit of the pure-tail inference in numerics_v01

## Statement

Let E be a nonzero real S1 angular polynomial on the circle, A=||E||_(L²(0,2pi)), and let R>0. If F(r,theta)=r^e E(theta) for every r>R, then

||F||_(L²(r>R))=A R^(e+1)/sqrt(-2e-2) for e<-1,
||rF||_(L²(r>R))=A R^(e+2)/sqrt(-2e-4) for e<-2.

These are exact equalities for the specified pure exterior power. They are not universal lower bounds for a field with leading asymptotic term r^e E and no quantified remainder. The corresponding endpoint integrals diverge logarithmically.

This independently confirms the correction in source/N4_PROOF.md. It refutes the general lower-bound inference in section3 of the frozen source/numerics_v01.md. It does not refute the separate finite-family obstruction in ../finite_family_l2_audit/PROOF.md or a complete integral calculation for a fixed candidate.

## Proof and counterexample

The polar area element is r dr dtheta, so direct integration gives the two identities. To disprove a lower bound based only on the leading term, fix e<-2 and choose a smooth cutoff eta which is zero for r<=1, one for r>=2, and takes values between zero and one. For L>R put

F_L(r,theta)=eta(r/L)r^e E(theta).

Every F_L is smooth after extension by zero near the origin, has the same S1 symmetry, and agrees exactly with r^e E for r>=2L. Its asymptotic expansion therefore has that leading term and zero further coefficients. Nevertheless,

||F_L||²_(L²(r>R)) <= A² L^(2e+2)/(-2e-2),
||rF_L||²_(L²(r>R)) <= A² L^(2e+4)/(-2e-4),

which tend to zero as L tends to infinity. For the first norm alone the same argument applies for every e<-1. An asymptotic expansion, even one eventually exact, does not control a fixed onset radius. This construction need not be a finite-generator IPM residual; that restriction is precisely the extra hypothesis needed by a finite-family theorem.

If F=F0+G on r>R and a bound on the full remainder norm is certified, the reverse triangle inequality gives ||F||>=||F0||-||G||. Squaring the sum and discarding cross terms is generally invalid. Alternatively, a dual test or complete exact integral can supply a lower bound.

## Finite coefficient prefixes

A finite prefix a_0,...,a_N by itself has continuations whose generating series is a polynomial, has any prescribed finite convergence radius, or has radius zero. Choose respectively all later coefficients zero, a geometric tail, or a factorial tail. Thus a numerical root test using thirteen known coefficients supplies no theorem about convergence or divergence of the full stationary series. The actual IPM recursion fixes its own continuation, but a theorem about that continuation requires estimates from the recursion beyond the observed prefix. None are supplied by the displayed finite root values. The phrase 'converges only for' must remain a heuristic interpretation, not a condition used by a proof.

## Exact arithmetic check and normalization

The independent code recomputes each angular norm as sqrt(pi sum_n E_n²) from the exact rational sine coefficients, rather than using the rounded norms in numerics_v01 or N4's prior intervals. It then integrates the pure power at R=100 and10000 with Arb. Full-circle and quadrant norms differ by a factor two for S1 fields. The results agree with N4's corrected values. For last retained branch6, the pure-model (G0,rF) at R=100 is approximately(3.75083805646,618.774240469). For last retained branch7 it is(1.53230207287,215.193740622), and G0 at R=10000 is0.000134382349810. These remain pure-model values, not lower bounds for the complete residual.

There are seven nonautomatic forbidden sectors for Hdot^-1 in the stated fixed-exponent family, not eight nonzero sectors. E_(0,0) is identically zero because c gamma=1. The other seven are enumerated in ../membership_audit/PROOF.md. The nonzero E_(1,0) already proves that state131 is not in L²; correcting the count does not change that conclusion.

## Further scope of a truncated stationary profile

Truncating the density series at j=N does not produce a residual containing only its first missing principal sector. Bilinearity gives principal residual sectors with indices h=i+j+1 for all retained i,j<=N, so h can range through2N+1. The next sector after h=N+1 need not be a descendant of order r^-8. Moreover, the coefficients at h>N+1 are computed from the retained pairs; they cannot in general be read as h(c-1)G_h from the full infinite recursion because pairs involving omitted density coefficients have been deleted. Thus the proposed O(r^(gamma-8)) remainder in section8 requires independent cancellation checks for every intervening principal sector, even if descendants q=1,2,3 vanish in each retained branch. This is an algebraic limitation, not a claim about an unpublished candidate's exact coefficients.

## Dependencies and limits

The analytic proof uses only polar integration, smooth cutoffs, the triangle inequality and the stated bilinear residual. The finite-family theorem and candidate-specific computations are independent inputs and retain their own scope. The code is an arithmetic audit of the pure models, with exact source hashes and interval comparisons recorded separately.
