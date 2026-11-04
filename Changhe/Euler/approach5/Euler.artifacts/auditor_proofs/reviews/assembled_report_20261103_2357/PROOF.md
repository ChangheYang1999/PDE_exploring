# Report transfer of the sign-changing carrier construction

Status: exact assembly audit of the front matter, main sections and Appendix A. The companion T38 sentence has a separate scope defect stated below.

## 1. Exact versions and reading boundary

The previous approved report is b9de6a1659808204eccd5899f4c0a65cfb0357e974aaff7563839256603171e6, at cutoff A2566, approved in A2578. The new report is sha256 6c23e90d36f1f9a58e6944ffea8802db53eaab34c526f20b154dfa8068af2c06, 1006636 bytes, at cutoff A2587. Both versions are pinned in the respective verification directories. This proof concerns the exact new version, not subsequent changes.

The full coordinator delta of 29762 characters was read in two contiguous pieces. An independent line comparison finds exactly the same changed content. The companion PROOF_OBSTRUCTIONS delta, 6227 characters, and THEOREM_ATTEMPTS delta, 9712 characters, were read in full. The changed mathematical lines in ASSUMPTIONS are exact copies of the report's changed rows; their equality is recorded in the team records. The remaining changed history lines were read in full. No new conclusion is inferred from an unexamined row or an unchanged historical appendix.

## 2. The carrier row and its logical content

The new LIT306 row states precisely a local smooth carrier for each 0<c<1/2 and every finite omega, on a flowbox through a nonzero point of X, flat exactly on the central orbit. Its two actual section ratios are in every Lp with 0<p<2 and fail every L2+C0/r majorant. The trace tr((DV)^2) takes both signs arbitrarily near every point of a smaller orbit segment. These are exactly A2580-A2586.

The construction description retains the logarithmic radial factor, disjoint cubic-width bumps, fixed indefinite Hessian, positive radial derivative of the stream function, the short-support Volterra derivative bound and the full determinant trace formula with its moving-coordinate error. It does not identify coordinate divergence with physical divergence or suppress the geometric density. Its sign argument uses different point sequences in the same field. No scalar, pressure or full system is asserted.

The section 10 and O12 summaries reproduce this scope. Their no-completion-constructed statement is faithful to A2587 OPEN. They do not infer a theorem of non-completability. The positivity hypothesis on the radial factor in the separate LIT305 clause is now explicit and matches the original isolated-orbit construction. Thus it does not apply the radial trace sign to the nonradial bumps.

One optional precision concerns the row's words about C61's necessary positive trace. The exact consequence is that every neighbourhood of x0 contains a point with T>0, under the full stated C61 hypotheses. It does not require T>0 throughout a neighbourhood. The new row is consistent with that reading; replacing the phrase with this quantifier would make it unambiguous.

## 3. A stronger method-necessity statement in the companion T38 entry

The new T38(k) sentence in THEOREM_ATTEMPTS says that the remaining sign exclusions "must use S or the pressure". This inference is not supplied by the construction. What has been proved is that the displayed local carrier conditions, flat orbit and ratio properties do not imply a single sign of T. A later argument could impose another geometric, global or regularity consequence not encoded in those local hypotheses. Nothing in LIT306 proves that every possible exclusion must pass through one of the two named quantities.

In literal generality the necessity claim is false: an additional real-analytic carrier assumption alone would exclude a field flat at a point and nonzero nearby, by its convergent Taylor series, without S or pressure. This observation does not make analyticity available in the original smooth class. It demonstrates the missing logical quantifier in a claim of universal method necessity.

Replace the sentence after the LIT306 citation by:

    so these local carrier and ratio hypotheses do not force a single sign of T; a stronger exclusion needs an additional input (A2556, A2587 OPEN).

The preceding factual descriptions in T38 are correct. The defect is in this final inference only. It is not present in the new front/main/Appendix A assembly and does not invalidate that narrower approval.

## 4. Verdict and boundaries

The changed front matter correctly records approval A2578 at the earlier cutoff. The new history accurately lists A2567-A2587; no pending LIT307-LIT310 result or reduced B67 example is promoted by this pin. The entire front/main/Appendix A assembly is therefore confirmed at the exact sha256 and cutoff of Section1, by combining A2578 with the complete new delta and the substantive checks in Section2.

The separate method-necessity inference of Section3 is refuted and needs the stated repair. Later report versions, every historical Appendix B item, arbitrary carrier completions and unrestricted rotating-profile nonexistence remain outside this approval. In particular no local carrier construction here is a smooth decaying Euler profile.
