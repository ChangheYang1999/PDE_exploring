# X8 numerical audit inputs, version 03

Frozen 2026-11-04T00:23:59.771094Z, through AN463 and the read AT1750/v531 material. This status summary supersedes version 02; all earlier evidence remains unchanged. Later events are recorded in immutable exchange notes.

The exact source C2-N1-013 has certified whole-plane residual bounds. The current computation has not certified the global background, the near and far operator estimates, the invariant ball or stationary existence.

## Fixed source and complete residual bounds

The parameter is c = 4076476460239181/2251799813685248. Authoritative Candidate 007 remains SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. Source 013 is fixed by raw hash a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a, canonical hash 2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33 and field hash 3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb. The exact normalization ell(h)=0 and eleven forbidden far-field constraints remain confirmed.

At P-S1, W(X)=sqrt(1+4|X|^2), unitary Fourier normalization and ordered derivative tensors,

    ||F_*||_2 in [7.959400186993612e-7, 7.961206656880281e-7],
    ||W F_*||_(H^(21/10)) in [0.0035510975483434412497, 0.0055545729030073655758].

The upper proves the target 0.006. The target 0.0055 is undecided. Neither value is the P-S2 norm or S_F. The exact proofs, source bindings, origin/interior/exterior assembly and independent reviews are mapped in reports/AUDIT_READING_GUIDE_v02.md, section 2. Later optimizer states do not replace this source.

## Regional background results

Original roots 000 through 031 are adopted by both auditors and cover 0<=r^2<=1/3. They prove M>=(3/5)I, |grad h|<=71/500 and ||Sym Du||_op<=137/125. AN451 and AN452 adopt roots 030 and 031. Their local review hashes are 0b54d7af22ad062926d9553c48bfcc2f6084301fa2361eb7d668b618997934c5 and 3ff4b3635d4b844052acd395779ef99c5bb683d5d38f5f4df6de3a8e8ff8d0ab. Their standalone proofs are in research/source013_background_admission/roots/root_030_v01 and root_031_v01.

Balanced root 034 version 01 is adopted in AN446. On 17/47<=r^2<=35/93 it proves the same matrix and strain targets and |grad h|<0.141655687509<71/500. Its local actual review hash is 2f5e6082499c58089e258c980d8b7200281897c2acaa00e1fcc90b8991c8c5c3. The earlier original root 034 timeout remains unchanged.

Balanced root 098 version 01 is adopted in AN437. On 49/15<=r^2<=99/29 it proves the same matrix and strain targets and |grad h|<0.174273660704<1/4. The smaller 71/500 test remains unresolved on one leaf. Its local actual review hash is 9f0155f2c0f2d918912f298a515f3dfa5d2e52ebd7ba2b9af63ce1846b0b7d8a. Original root 098 separately proves the matrix and strain targets; its large gradient interval does not prove a physical violation.

Balanced root102 version01 completed its physical replay in 640.088682023 seconds (AN450), with stored strict gradient upper 79218804901/500000000000=0.158437609802<1/4 and the matrix and strain flags passing. The 71/500 test remains unresolved. Result SHA2569bafb897d5b04cbda5c93e8130cc6b55b9824d0873cb72f90a4422f37ba7156d; physical receipt e0949ccc213e8389d3a8149f71d52bda1a3d2ed4f572c3d8e10869f4039b9f31. Its first independent review reached a local900-second timeout at00:17:01.360950Z without a completed check. A fresh independent review began00:17:17.422816Z with a3600-second local allowance; this does not change the physical execution gate or the first failed review record. Actual containment and regional adoption remain pending.

Each balanced proof is in research/background_balanced_replay/roots/root_NNN_v01/PROOF.md, with exact bindings and publication checks beside it. These annuli do not bridge the missing radial intervals. The admitted mixed consumer in AN438 selects one whole adopted original or balanced record per root, all 128 roots, and both complete original owner results. It does not permit per-component mixing. Its global actual application remains open.

Balanced root100 version02/request155 completed at00:21:32.155168Z, with physical elapsed634.1772666196339 seconds. Compilation took62.38278580131009 seconds and radial preparation310.37864128500223 seconds. AN461 checks320 scalar comparisons and records matrix3/5, strain137/125 and strict gradient39162210713/250000000000=0.156648842852<1/4 in the stored containing intervals; the smaller71/500 target remains unresolved. Its region is25/7<=r^2<=101/27. Result SHA2562f782a5a1bf1fa1514707afa49a003ea29c8fe35429a18a6d1ee3470b196ea42; receipt8fe9bff87613a9e14d7ccf09c2044d6c93bf509e083682cb52b4529e80d039dd. Independent actual-source review and regional adoption remain pending. The earlier root100 version01/order32 timeout is retained unchanged.

## What the remainder and sample diagnostics establish

AN453 recomputes the saved balanced allowances and strict gradient projections with 309 exact checks. Approximate E_rh and E_sh are 2.23e-10 and 5.53e-10 on root 034, 7.00e-19 and 1.72e-18 on root 098, and 2.94e-8 and 8.39e-8 on root 102. Full rational endpoints are in research/background_balanced_diagnostics/verification/result_v02.json. No old-record intersection narrowed a gradient component in these three results. This does not remove the earlier intersection within the fresh evaluator.

AN448 gives the needed qualification of theory_v16's remainder floor. The raw interval C=[A-E,V+E] has magnitude at least E, but intersection with another containing interval need not preserve that floor. The deployed code uses such an intersection. Its failure at a given source and order cannot be inferred from E alone. The endpoint root 127 uses only the independent branch range, without the Taylor calculation or angular splitting; zero unused Taylor errors are not zero uncertainty. T1's note 58 and AT1715-1719 record this correction. Predicted subdivisions and completion costs remain heuristic.

AN454 proves a conditional common-power representation using s=1-t and y=s^((c-1)/(2c)). All 45 metadata exponents have the form n+m(c-1)/(2c), with m<=13. The proposed common denominator has degree 546 and the conditional numerator degree is at most 705 in s and 13 in y. AN459 corrects its general statement by requiring rational scales for rational coefficients; all recorded scales meet that hypothesis. Positive real scales still give the identity over the reals. This is an algebraic alternative, not a completed source transformation, evaluated range, cost estimate or admitted replacement method.

AN460 responds to T1 note 59 with a conditional Taylor remainder for each complete product f_b P_b. It requires an analytic disk avoiding every pole, a containing bound on the entire complex circle and every real angular coordinate in the cell, all seven fields, and a separate terminal exterior estimate. The sampled five angular coordinates and agreement between 32 and 64 circle points do not supply those bounds. No implementation is admitted. A naive full-source scan on 500 arcs revisits 310700000 coefficient records per radial cell, or 14602900000 over the proposed 47 cells. Those are uncached workload counts, not runtime measurements or lower bounds. The proposed finite pilot must price full angular enclosure rather than only point evaluation. AT1748-1750 confirms the specification conditionally and independently checks the coefficient identity; it supplies no actual field bound.

AN463 independently confirms AT1746's exterior join correction. The47-cell geometric cover closes only when its tail starts at t=1-2^(-24), equivalently r^2=2^24-1. A tail starting only at r=4096 leaves a positive compactified gap1/281474993487872. The tail must use the exact adjoining domain, or the finite cells must extend or bridge the gap. The exact radius R=(9/10)(1-m) avoids both positive and negative denominator poles and gives H/R<=10/27 on the proposed finite cells. These254 rational checks supply geometry, not a terminal field bound.

AN457 checks the background sample's algebra on exact Cartesian derivatives in 49 finite checks. Its full strain formula is correct. Its radial jets are converted to binary floats before angular summation, so the unqualified claim of no floating cancellation is refuted. That fact gives no lower bound on the actual error. The FLOAT label remains appropriate; a separate run manifest must bind the exact source files. No sampled value or continuum bound is certified by this formula audit.

## Near and far obligations

All 561 near panels and both endpoint records remain required. AN418 and AT1647-1649 refute the proposed large-radius v^22 extrapolation at the tested geometries, but establish no all-panel maximum. The original owners continue to their complete endpoints. The mu68 fallback remains prepared, untriggered and unexecuted.

AN444 corrects the literal far mesh count to 202 cells and identifies the original sample-grid mismatch. The revised T2 comparison uses the same 166 radii: its FLOAT maxima are 1.1867232199856157 for the symmetric construction and 1.4597266449643085 for the unsymmetrized one. AT1726-1730 confirms the conditional endpoint enclosure analytically. The numerical integration still omits rho<1e-6, and finite radial samples do not cover a continuum. No A_E upper is certified.

AT1731-1733 checks the CS-B rounding correction over 280 cells: 90 budgets require an upward binary64 step; the maximum is unchanged at 8603566328415511/144115188075855872=0.059699233948103884<3/50. The corrected tail is 0.024397461684268512. This is conditional finite arithmetic. AT1540's actual kernel and derivative inputs remain open. The sufficient target A_E<=1.3263305 still requires all matching CS-B, DW and HSB inputs.

## Next finite work and cutoff

No scientific worker is active in this agent at this freeze. AN462 freezes the next sequential capped-root trial, balanced104 version01/request156, order24 and32 uniform angular cells, under the unchanged900-second gate. Its request hash is5b19888bb6bf9c1e67c2bb5a10b5913bd30a3a5ace4e69187e54e0e45d8259c5 and application hash892ec856fd6cd7cf122da3e072c1b933fa20ef1415ef2c5160340f49a5abee5e. Concrete independent admission remains pending; no output exists. Its choice follows the completed100 and102 physical trials and predicts no104 result. Request153 remains deferred. Original032,033,035,036 and037 have physical results pending independent actual review. The coordinator's X8 decision on a bounded complete-product pilot is pending.

At the latest read owner checkpoint, g0 has61/64 original roots completed and g1 has54/64. Both retain capped failures. The g0 release time is still an estimate, not a complete receipt. The planned FLOAT full-velocity sample follows g0 completion within the authorized15-minute window, then a review host needs a concrete accepted assignment. All561 near panels remain in scope.

The final numerical input cutoff is 2026-11-04T16:50Z. This agent stops science at 17:05Z, before the team stop at 17:05:30Z. All times above are measured records or explicitly labelled plans. This agent uses core 50, nice 19 and one numerical thread, with at most one busy computation. It uses no JavaScript/TypeScript, servers/listeners, cluster, remote or paid compute, GPU, Lean/Lake build, foreign writes/signals, commit, push or online post. Collaboration is through the configured theory and coordinator agent files; the provider-side model identity has not been independently queried.
