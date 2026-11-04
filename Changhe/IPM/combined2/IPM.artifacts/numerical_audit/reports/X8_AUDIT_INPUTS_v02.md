# X8 numerical audit inputs, version 02

Frozen 2026-11-03T23:35:01Z. Supersedes version 01 as a status summary. Every earlier audit and immutable exchange version remains intact. The cutoff is AN445; later actual reviews must be added explicitly.

## Results admitted by both auditors

The unchanged exact source C2-N1-013 has the whole-plane residual bounds

    ||F_*||_2 in [7.959400186993612e-7, 7.961206656880281e-7],
    N_(21/10)(F_*) in [0.0035510975483434412497, 0.0055545729030073655758]

at P-S1: W(X)=sqrt(1+4|X|^2), unitary Fourier normalization, and ordered derivative tensors. The upper fits N<=0.006; N<=0.0055 is undecided. These do not certify P-S2 or S_F. See reports/AUDIT_READING_GUIDE_v01.md for the exact norm proofs and source bindings.

Original background roots 000 through 029 are now adopted. Their union is 0<=r^2<=15/49. Every root passes M>=(3/5)I, |grad h|<=71/500 and ||Sym Du||_op<=137/125. AN443 adopts root028, review SHA256 2b68cc7e13361bb5b88240234806263437b88d50bfb0010202634f43058d7476. AN445 adopts root029, review SHA256 411983815efaa22f210544c3b8e89433355a2b7191926d8201101e7002e6a064. Their standalone proofs and bindings are in research/source013_background_admission/roots/root_028 and root_029.

Balanced root098 version01 is independently adopted in AN437 on 49/15<=r^2<=99/29. It proves M>=(3/5)I, strain<=137/125 and |grad h|<0.174273660704<1/4. The smaller 71/500 gradient target remains unresolved on one leaf. The original root098 matrix/strain-only result in AN432 is separate; its large gradient upper is not a physical violation. Neither result bridges the intervening radial gap.

The actual mixed-consumer method is admitted in AN438. It selects one complete adopted original or balanced record for each of all 128 roots, together with both complete original owner results. It does not permit per-component mixing. No global physical application exists at this cutoff.

## New physical replay and pending request

AN441 records successful balanced root034 version01, request152, order16 and eight uniform angular cells. All four stored joint tests pass; the independently recounted strict gradient upper is 141655687509/10^12=0.141655687509. Its exact radial annulus is 17/47<=r^2<=35/93. The result hash is 8b447b732afd1fdd778d04db71f40006f939d556a26a3432698831de7850eaaf, receipt f59871282a0544f18491dddb830d805666c735e97fae441a0e5e7cc0b9fcd9e2. The successful receipt spans 23:22:50.682492Z to 23:31:10.263789Z on November 3, elapsed 499.581289942842 seconds. AN's 80 scalar comparisons are conditional on the containing ranges. AT's complete actual-source review and AN adoption remain OPEN. The prepared proof in research/background_balanced_replay/roots/root_034_v01/PROOF.md is explicitly conditional until those records and its final check exist.

Request151, balanced root100 order32/depth5, timed out after its unchanged 900-second scientific limit and supplies no result. AN436 retains the rejected receipt and genuine elapsed 901.5657887761481 seconds including gate overhead. Its radial preparation took 631.6488261651248 seconds. No silent time extension or retry in the same namespace is permitted.

The next single capped-root trial is request154, root102 version01, order24/depth5. AN442 freezes 473 bindings, request SHA256 a8960b5967ff7b8e5cadf69047a4d265f8ad01da7023ea6b7e08c07e095a0d77 and application 82bac60a380b6fac45bde1a35c212fac1d071378c6c991fb9a110bacffffded2. Its exact concrete review and execution are still OPEN. AN413's order24 remainder ratio supports this as a planning trial only, with the same polynomial factors; it does not predict the physical enclosure or runtime. Request153 remains deferred under the coordinator's 23:14Z decision.

## Far-band plan audit

AN444 audits T2_FAR_AE_PLAN_v01 using 368 exact finite checks, measured 0.04517439426854253 seconds. The literal mesh needs 202 cells, not about130. The earlier symmetric and unsymmetric records have 165 and20 sampled radii respectively, with18 common points; their parameter and integration-grid settings match, but the sampled suprema do not use the same set. The quoted unsymmetric1.45495 also uses different tau, slopes and derivative orders from the final rational trial. Verdict: REFUTED for the cell count and final-configuration attribution.

The final stored FLOAT grid has peak1.1867232199856157 atxi=13/20 and reconstructed minimum kernel multiplier margin1.4274500303843765 atxi=73/20. These are consistent finite scalar diagnostics. The grid spans10^-9 to25, not[0,8pi]; RHOMIN=10^-6 is a separate omitted integration disk. They supply no continuum or integration certificate. The first checker stopped on the unequal xi arrays, and that failed attempt is retained. The corrected proof preceded the successful checker.

Proof: research/far_band_plan_audit/PROOF.md, SHA256 d382b98b21c10320b6fde96a2bfcea501942ba58ba3685f6846fe0de7f782b16. Exact evidence: research/far_band_plan_audit/verification/result_v02.json, SHA256 85ec41065a0c6aa6f73752f980db7764c101f69e8796b8b35b5e198e49993a6a. AT1697-1703 independently confirms SYM and conditional AE-CS, with the correct antipodal support and factor4, no old inner-region zero shortcut, and a finite continuum essential supremum still required.

## Remaining closure requirements

The full561-panel near cover remains required. AN418 and AT1647-1649 reject the earlier large-radius allowance extrapolation but provide no all-panel maximum or completed assembly. The proposed mu68 fallback remains untriggered. The full background, same-coefficient far derivative application, certified A_E<=1.3263305, full inverse and invariant ball remain OPEN. No stationary existence theorem has been completed.

X8 inputs are due00:30Z, freeze00:35Z, publication about00:45Z on November4. X9 follows by04:30Z with freeze04:15Z. Final numerical input cutoff16:50Z; science stops17:05Z and the team stops17:05:30Z. Times are actual observations or explicitly labelled plans. Computation stays local, core50/nice19, one busy job and one numerical thread. No JavaScript, servers, cluster, remote compute, GPU or Lean build was used. Collaboration with the configured the main model theory/coordinator agents is through the published files; provider-side identity was not independently queried.
