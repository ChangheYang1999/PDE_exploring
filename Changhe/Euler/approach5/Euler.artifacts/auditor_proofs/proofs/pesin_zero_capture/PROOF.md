# A transported field vanishes on an irrotational Pesin stable curve

Written: 2026-11-02T21:46:58Z. Audit: A201, CONFIRMED. This is an independent proof of coordinator CO16. It does not depend on the 2026 generalized Gibbs preprint.

## Statement and hypotheses

Let B be a complete C2 vector field on R3, let Psi_t be its backward flow, and put F=Psi_1. Let W be C1 and satisfy

    W(Psi_t x) = exp(kappa t) D Psi_t(x) W(x),    kappa>0, t>=0.

Let mu be an ergodic F-invariant probability with compact support. Assume mu({B=0})=0, mu({W=0})=1 and that its three Lyapunov exponents, each simple, are chi>0, 0, -lambda<0. The zero direction is the flow direction. Assume a compact neighbourhood of the support contains the forward iterates of sufficiently small local stable plaques. The compact forward-trapping neighbourhood in CO16 implies this condition.

Then, for mu-almost every q, W vanishes at every point of its global Pesin strong stable curve W^s(q). It also vanishes on every flow translate of those curves. If mu has absolutely continuous conditional measures on its one-dimensional unstable plaques, then {W=0} has positive three-dimensional Lebesgue measure.

In particular this applies to C2 Euler velocity profiles with W=curl U, provided the invariant measure with the stated spectrum and unstable conditional measures is given. No existence of that measure at C2 regularity is asserted.

## Notation and standard inputs

All ambient vector norms below are Euclidean. Write q_n=F^n q and a_n=F^n a. The finite-dimensional multiplicative ergodic theorem and the C2 Pesin stable-manifold theorem give, for every sufficiently small epsilon>0 and every regular q:

1. Linear isomorphisms L_n from an adapted R3 to the tangent space at q_n, with

       ||L_n|| <= C,    ||L_n^{-1}|| <= C_epsilon exp(epsilon n).

   For A_n=L_{n+1}^{-1} DF(q_n) L_n, its conorm, the least singular value, satisfies

       m(A_n) >= exp(-lambda-epsilon).

2. For a in a sufficiently small local stable plaque,

       |a_n-q_n| <= C_{a,epsilon} exp((-lambda+epsilon)n).

The first assertion uses the two-sided Lyapunov norm on each Oseledets line. One may construct it by summing the norms of all forward and backward iterates with weights exp(-lambda_i k-epsilon |k|), and taking the orthogonal sum over the three lines. The one-step estimates follow by shifting the sum. The comparison with the Euclidean norm is tempered. In particular this is a lower bound on the full derivative, including its stable direction, not merely an upper bound on the stable restriction.

These are standard finite-dimensional invertible Pesin inputs. The retained Blumenthal-Young source, Lemma 2.8 and Theorem 3.1, supplies adapted-chart and stable-graph versions; its one-sided formulation by itself is not being cited for the full conorm bound above.

## Proof of vanishing

Choose a full-measure invariant regular set on which W(q_n)=0 for every integer n. This is possible since mu({W=0})=1 and F preserves mu. Fix q in this set and a in its local stable plaque.

Since F is C2, DF is Lipschitz on a compact neighbourhood of the two forward orbits. Define

    Atilde_n = L_{n+1}^{-1} DF(a_n) L_n.

The norm comparison and exponential approach imply

    ||Atilde_n-A_n|| <= C_{a,epsilon} exp((-lambda+2 epsilon)n).

Choose epsilon with 2 epsilon<lambda. This error tends to zero. For all sufficiently large n it is smaller than exp(-lambda-epsilon)-exp(-lambda-2 epsilon). Since the conorm is 1-Lipschitz in the matrix norm,

    m(Atilde_n) >= exp(-lambda-2 epsilon).

Multiply these bounds, absorb finitely many initial invertible matrices into a positive constant, and convert back using L_n. For every vector v and every n>=0,

    |DF^n(a)v| >= c_{a,epsilon} exp((-lambda-3 epsilon)n) |v|.

The C1 regularity of W and W(q_n)=0 give the competing upper bound

    |W(a_n)| <= C |a_n-q_n|
             <= C_{a,epsilon} exp((-lambda+epsilon)n).

On the other hand exact transport and the derivative lower bound give

    |W(a_n)| = exp(kappa n) |DF^n(a)W(a)|
             >= c_{a,epsilon} exp((kappa-lambda-3 epsilon)n) |W(a)|.

Consequently

    |W(a)| <= C_{a,epsilon} exp((-kappa+4 epsilon)n).

Choose also 4 epsilon<kappa and let n tend to infinity. Then W(a)=0. Every point of the global stable curve eventually enters such a local plaque, and the transport identity is invertible. It therefore vanishes on the whole global curve. The same identity makes the zero set flow invariant, proving the flow-saturation conclusion.

Notice that no flatness of W, divergence identity, relation between kappa and lambda, or global flow of W was used. The C1 assumption on W is used through a local Lipschitz bound. Merely continuous transported fields do not satisfy that bound.

## Positive volume when unstable conditionals are absolutely continuous

Choose a local unstable plaque on which the conditional measure of mu is nonzero and absolutely continuous with respect to arclength. Its regular points include a positive-arclength measurable set T. Restrict T to a compact Pesin block of positive arclength, with B bounded away from zero and with uniformly transverse stable, unstable and flow directions. Such a restriction is possible by a countable exhaustion.

A sufficiently short flow strip through T has positive two-dimensional area: in a local flow box the two independent directions are the unstable tangent and B, and the Jacobian is bounded above and below. Flow translates of regular points remain regular; bounded flow times preserve uniform Pesin-block bounds after enlarging the block. Every strong stable plaque through this strip is contained in {W=0}, by the first part and commutation with the flow.

The strong stable lamination is absolutely continuous between two-dimensional transversals, with positive bounded Jacobians on the chosen compact block. Applying this to a short family of transverse slices, and then Fubini, shows that the saturation of the positive-area strip by stable intervals has positive volume. Thus {W=0} has positive volume. This is the same two-dimensional-transversal argument recorded in auditor_proofs/proofs/smooth_core_srb/PROOF.md; it does not incorrectly discard the neutral flow direction.

## Dependencies and limits

The stable absolute-continuity input is retained in in the team records: the stable cutoff can lie below zero, with the zero exponent included among the transverse directions; Theorem A applies to two-dimensional C1+Lip transversals. Its compact-stack construction and bounded Jacobian estimates are the source inputs for the final paragraph. The corresponding finite-dimensional C2 setting is sufficient here.

This result concerns points on actual Pesin strong stable curves. It does not assert that every point whose empirical measures approach mu lies on such a curve. It does not exclude a vortical measure whose support intersects {W=0}. It supplies no arbitrary-rotation Euler nonexistence theorem.
