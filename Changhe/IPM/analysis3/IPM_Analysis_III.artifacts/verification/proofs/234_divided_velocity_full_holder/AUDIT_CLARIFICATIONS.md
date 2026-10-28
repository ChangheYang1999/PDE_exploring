# Binding clarifications after the full divided-velocity audit

Date: 2026-10-28T16:23:36.141297+00:00. Read this file together with the unchanged PROOF.md. The independent actual independent audit found no gap in the quotient lemma, annular estimate, complete coupling estimate or threshold deduction. No computation was run for this analytic audit.

1. In the compact lemma, both suprema defining K are over x!=0. The value assigned to g on x=0 is irrelevant to h=x^2g and to every integral. All vertical Holder estimates are uniform on the nonzero vertical lines. This removes an irrelevant arbitrary-axis-value issue.

2. The canonical U1 of a bounded compact h equals the L2 multiplier representative here because the possible far-subtraction constant vanishes by x-parity, as in proof 214. Continuity alone is not the reason. The dyadic proof identifies a continuous representative of U1/x. Its hypotheses are those stated in the compact lemma with item1 above. The unused sentence about extension by approximation to arbitrary bounded measurable g is withdrawn; no such extension is needed.

3. In the near-axis convolution argument H is C1 and even, and moreover belongs locally to W^(2,infinity) by equation(11). These are successive conclusions, not equivalent regularity statements. No derivative of h in x is taken.

4. Radial localization in the annular step controls the entire vertical line seminorm of the localized cofactor. Close pairs inside the same comparable-radius annulus use the divided vertical seminorm of proof 228. Pairs on opposite components across the annular hole, or with substantially different radii, have a uniformly positive separation after rescaling and use the cofactor supremum from proof 228 equation(5). Pairs crossing a cutoff use its Lipschitz difference times that same supremum. The finitely many inner pieces for2<=R<8 use the local chi h E2 term where appropriate. This proves the actual global vertical-line hypothesis of the compact lemma with a constant independent of R.

5. For the full moving-tail column use proof 232/AUDIT_CLARIFICATIONS.md items1 and2. Both first Cartesian derivatives of Q=M0/x^2 satisfy |grad Q|<=C r^(2k-4)(1+log r), by proof 217's fixed cylinder derivatives and smooth angular division. Split Delta(x_t^2Q)=Delta(x_t^2)Q+x_t^2Delta Q. The result is Cq^2 delta(1+t)exp(ell(2k-1)t), not a bound obtained from partial_x M0 alone. H0 has the same finite-time quadratic difference. This supplies the load-bearing column term for all1/2<alpha<1.

6. Uniform stationary phase uses the positive off-critical lower bound in proof 232/AUDIT_CLARIFICATIONS.md item3. It follows from compactness and uniform C1 convergence of the exact q-dependent phase. The actual simple-turn certificate and proof 232 are now independently confirmed as V262. For clarity the coupling operator in equation(18) can be denoted Ccp in{C0,Cren}, reserving C for a generic bound.

7. At alpha=1/2 the dyadic series still converge. What fails to give a contradiction is only the final comparison b<=C N. The theorem here is precisely non-surjectivity of T,Lren,A0 on this Z2 for1/2<alpha<1,2k-1<beta<k,gamma>4k. It does not decide other targets, a degenerate turn, either side of the endpoint, the range of F0, an infinite cokernel or nonlinear existence. Proof 236 is a separate stronger target, not a consequence of this non-surjectivity statement.

The complete dependency manifest and audit hash are in evidence/audit_record.json. The original proof and initial derivation record are preserved unchanged.
