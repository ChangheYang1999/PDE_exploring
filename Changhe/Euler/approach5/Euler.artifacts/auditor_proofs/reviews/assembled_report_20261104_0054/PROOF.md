# Audit of the report assembled at 00:51Z

Status: A2681-A2682 CONFIRMED; cumulative approval OPEN A2683 pending two precision repairs. All eleven changed blocks read. The directory suffix is an artifact label, not an observed time.

## 1. Exact snapshot and scope

The snapshot has SHA256 `7b1d1a363d0cfa3d2a88b62335b4a2c6a5f740f50467107e74d44e721bfa2936`, 1,026,737 bytes and 6,986 lines, with declared assembly time 2026-11-04T00:51Z and cutoff A2676. The independently generated delta starts at 3355430d, already approved by A2679. All eleven old and new blocks were read in full, including the complete long completion row and the surrounding Section 10 paragraph. Exact bytes, hashes and blocks are in verification.

The audit concerns the front matter, main report and Appendix A. Historical Appendix B remains excluded. The newly inserted Appendix C entry is checked only for its account of the present changes.

## 2. The Liouville repairs are correct

The new local Z convention says explicitly that Section 2B denotes the vortical set by Z while the front matter and Sections 2C and 2D use O. The reference in Lemma 2(e) now correctly uses its own part (d) and Lemma 1(c). The family exception in the plan explicitly supplies (CI-5) for Lemma 13(vi), and the Corollary L.4 diagram now supplies recurrence from Lemma 4.

The reverse inclusion in Lemma 11(a) is completely repaired. Closeness of the positive integer Phi iterates to the compact trapped set bounds those iterates; the upper bound on each intervening unit interval bounds the whole forward orbit. At each fixed time s, the lower bound

    |Phi_(t+s)y|>=exp(ct)(|Phi_s y|-M/c)+M/c

then implies |Phi_s y|<=M/c. Thus the entire forward orbit lies in Q, giving y in K. Equality of the two maps on K identifies their unstable sets, with the regularity interpretation supplied by the existing lemma. No uniform convergence rate over other points is assumed.

The stronger same-orbit interval statement after Corollary L.4 now says that it comes from the proof and Lemma 18 at a recurrent strict-sign point. It is no longer presented as a logical equivalent of the weaker levelwise criterion. The new checklist item accurately records these edits without calling them a fresh full review of Sections 2B and 2D.

## 3. Pressure and cost conclusions, with two precision repairs

The LIT315 clause retains C2 velocity, C1 pressure, the double zero, center pressure normalization, a whole-ball pressure inequality and the distributional Poisson relation. Divergence freedom remains part of the surrounding carrier setting. It states no upper pressure bound and no sign of H. The sharpness is in the stated kinematic Poisson regularity class, not the class of decaying profiles.

The LIT314 clause keeps omega=0, the invariant-ray cost and the two scalar equations that force blow-up. The phrase sufficient but not necessary refers to excluding a completion, and the text explicitly says that LIT311 is not refuted. No new all-omega example is asserted.

The A2666 window now explicitly concerns a full Poisson completion, the finite-exit domain and the LIT311 hypotheses or their C2 replacement. It includes the additive upper constant and the subsequence, and denies an existence conclusion. These are the required mathematical qualifications. Two editorial changes are still needed for a precise assembled statement:

1. In the completion row, y is the two-dimensional section coordinate and x0=sigma(0) is a nonzero physical point. The newly written sequence y_n->x0 mixes the two spaces. Replace it by y_n->0, so sigma(y_n)->x0. Here f(y_n) denotes the section amplitude; in the radial case it is f(|y_n|).
2. In Section 10, the sentence immediately after the necessary window says a carrier with such a completion must fail one of these hypotheses. Its intended referent is the earlier sufficient exclusion criteria, not the just-stated necessary window. Replace these hypotheses by the earlier sufficient exclusion hypotheses. The corresponding O12 sentence has the same proximity problem; it lies outside report approval but should be synchronized. The remaining angular examples are illustrative failures of sufficient criteria, not a complete classification.

The first is a coordinate typo, and the second is an antecedent ambiguity introduced by insertion. Neither refutes the independent mathematical results. Cumulative approval of this exact assembly remains pending those explicit repairs. The prior 3355430d approval remains valid at its own cutoff, and the unrestricted conjecture remains OPEN.

## 4. Verification boundary

The status and history accurately record A2663-A2676. The older approval paragraph need not cite an approval that arrived after this build. No mathematical computation, formal build or new model client was used. Existing configured model coordinator and Theory Agent A  source comparisons were used; actual provider runtime remains independently unattested.
