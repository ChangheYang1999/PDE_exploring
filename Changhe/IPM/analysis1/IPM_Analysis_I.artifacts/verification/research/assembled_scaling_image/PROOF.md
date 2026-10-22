# Exact finite audit of the saved all-mode scaling image

Status: proof before implementation. Numerical claims remain OPEN until complete independent checks, actual model review and subsequent verifier adjudication.

## Exact statement and hypotheses

The untrusted data consist of 42 arrays A_j in R^(467 times 40), each with integer labels [l_j,r_j) intended to partition [0,260), a saved assembled array Z, a saved direct array D, strictly increasing nodes t_i and positive weights w_i. Every binary64 datum is interpreted as an exact dyadic real. The labels describe the claimed provenance; they do not prove that A_j is the image of the corresponding physical modes. Define S=sum_j A_j in exact real arithmetic. Require matching node and weight bytes in all files, the declared shapes, finite numbers, and a disjoint contiguous partition of [0,260). Missing, duplicate, overlapping or empty ranges invalidate the finite-data claim.

Let d_i=t_(i+1)-t_i>0, omega_0=d_0/2, omega_(466)=d_(465)/2, and omega_i=(d_(i-1)+d_i)/2 at interior nodes. Put v_i=(w_i+w_(i+1))/2 and a_n=1+(2n+1)^2. For any array F define four exact positive quadratic forms:

 Q_L2(F)=sum_(i,n) w_i^2 F_(i,n)^2,
 Q_L2q(F)=sum_(i,n) omega_i w_i^2 F_(i,n)^2,
 Q_H1(F)=sum_(i,n) a_n w_i^2 F_(i,n)^2
           +sum_(i<466,n) v_i^2 (F_(i+1,n)-F_(i,n))^2/d_i^2,
 Q_H1q(F)=sum_(i,n) a_n omega_i w_i^2 F_(i,n)^2
           +sum_(i<466,n) v_i^2 (F_(i+1,n)-F_(i,n))^2/d_i.

Write R_b(F)=sqrt(Q_b(F)). The desired result is a rigorously enclosed statement about R_b(D), R_b(Z), R_b(S), R_b(Z-D), R_b(S-D), and their ratios to R_b(D), with separately enclosed max-norm discrepancies. It also checks the saved JSON summaries against these exact finite functionals. These are discrete data functionals, not continuous Sobolev norms. It must state the difference between relative difference of two norm values and norm of the difference divided by the reference norm.

## Proof of the formulas and their interpretation

Each expression is a finite sum of squares with positive weights. Since w_i>0, Q_L2 and Q_L2q vanish only for F=0; the value terms give the same property for Q_H1 and Q_H1q. The four square roots are Euclidean norms after an injective linear map. Thus they are norms on this finite real array space and obey the triangle and reverse triangle inequalities. In particular, |R_b(S)-R_b(D)|/R_b(D) <= R_b(S-D)/R_b(D) whenever D is nonzero. This inequality does not identify the two quantities.

The formulas result by squaring the explicit finite row weights. The quadrature-labelled variants multiply the value rows by sqrt(omega_i) and the difference rows by sqrt(d_i); the latter cancels one power of d_i in the squared denominator. The H1 variants additionally multiply the value rows by sqrt(a_n). Expanding those definitions gives the displayed rational expressions exactly. No integration or quadrature accuracy statement is invoked.

Exact dyadic summation computes S without floating accumulation. A second exact implementation must check each S entry and each row's basic positive rational quantities. Independently implemented Arb and mpmath.iv evaluations enclose the positive finite forms, square roots and ratios; every comparison uses outward endpoints. The exact max-norm quantities can additionally be evaluated by rational comparisons. A saved floating Z need not equal S; this audit will quantify Z-S, not identify it as zero or assume a generic roundoff model for its production.

## Dependency and scope

The analytic scaling identity L K=epsilon-X.grad epsilon and the trial's normalization belong to separate results. Neither that identity nor the file labels proves that the saved D or A_j is an evaluated exact PDE field. No constituent mode is reassembled in this result, so the complete physical assembler comparison remains floating and unreproduced here. The audit only establishes the meaning, exact summation and numerical sizes of the saved finite arrays. It proves no global norm, angular tail, error of the underlying field evaluation, projection theorem, bounded inverse, lower bound, or decisive IPM endpoint.

Any new assertion about actual physical assembly requires an additional independent reconstruction. Runtime arithmetic libraries are trusted computational dependencies, not formally verified by this result. Freeze the source inputs before checking, retain any failed attempts, and do not alter accepted files.
