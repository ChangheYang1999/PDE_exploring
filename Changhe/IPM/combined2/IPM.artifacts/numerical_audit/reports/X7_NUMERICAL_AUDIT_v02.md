# X7 numerical audit

Published 2026-11-03T21:47:17.445733Z. This immutable account supersedes version01 for the 22:05Z exchange. It summarizes existing verdicts; new results retain their separate dated entries.

The fixed center is C2-N1-013-phi-007-sector-d8-leg24-lat-nf2, based on authoritative Candidate 007. The whole-plane residual norms are certified. The full-plane background and near-cover certificates are still incomplete, so the numerical work does not establish the stationary existence theorem.

## Certified source norms

Fix c = 4076476460239181/2251799813685248. Write psi = partial_y chi_007 + phi_013, rho = -Delta psi, u = (-psi_xy, psi_xx), F = (cX+u).grad rho-rho, and W(X) = sqrt(1+4|X|^2). The independently adopted containing certificates give

    7.959400186993612e-7 <= ||F||_2 <= 7.961206656880281e-7,

    0.0035510975483434412497 <= ||WF||_(H^(21/10))
                             <= 0.0055545729030073655758.

The Sobolev norm uses the unitary Fourier transform and the multiplier (1+|xi|^2)^(21/20). The integer moments use the full ordered Cartesian derivative tensors. The fractional upper follows from the signed cubic Hermite majorant, including use of the lower moment endpoint for its negative coefficient. The origin, middle annuli and exterior have all been included. Neither a P-S2 certificate nor a weighted strong Holder norm S_F follows from this result.

The plain norm is AN305; the fractional interval is AN317. Source identities are documented in research/reference_b18s2_audit/PROOF.md and research/source013_admission/TABLE_RESULT_PROOF.md. Complete norm dependencies are in research/source013_norms/results/whole_plane/; the fractional argument and exact scalar audit are in research/source013_hermite_majorant_audit/.

AN379 verifies that this interval supplies N <= 0.006. The proposed threshold 0.0055 lies strictly inside the interval. The certificate alone therefore decides neither N <= 0.0055 nor its negation. A budget using 0.0055 remains conditional on an additional norm bound. The separately audited 0.006 budgets retain all their other hypotheses, including the background rate, weak-energy constant and generator conditions.

## Background coverage

At 2026-11-03T21:47:17.445733Z, 18 roots have an independent AT actual review and AN adoption: 000, 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017. Their union is 0 <= r^2 <= 9/55. There are 30 successful physical calculations: 000, 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 026, 028, 030, 032. The 12 physical results without an adopted actual review remain pending. The inventory and direct evidence hashes are in reports/evidence/x7_inventory_v02.json.

Each independently adopted regional result uses all 45 exact source branches and 621400 coefficients, fresh 2048-bit containing field calculations and exact scalar comparisons on the complete angular partition. In the common notation of research/source013_background_admission/PROOF.md,

    M = (c+1+V.X/(1/4+|X|^2)) I - (21/10) Sym DV
        + [[rho_y, -rho_x/2], [-rho_x/2, 0]],
    V = cX+u,       h = -Delta phi_013.

The passing joint tests prove M >= (3/5)I, |grad h| <= 71/500 and ||Sym Du||_op <= 137/125 on the stated union of complete radial slabs, uniformly in angle. Every local statement has its own standalone proof under research/source013_background_admission/roots/. The original and fresh ranges are containing intervals, not sampled extrema.

The original 480-second attempts for roots 013 and 024 timed out. Their fresh version-02 attempts used separately reviewed 900-second requests and succeeded. The old attempts remain retained and excluded. The complete retry admissions are AN367, AN375 and AN377. Physical receipt times were 382.38006235007197 seconds for root 013 and 448.6994154220447 seconds for root 024; the results and receipts are bound in AN381 and AN382. Success supplies an input for independent review, not an automatic regional theorem.

AN385 records an original-owner obstruction at root 098: its 64-leaf archive reports passing matrix and strain components but unresolved gradient tests. The target 1/4 is unresolved on one leaf and 71/500 on 54 leaves. These owner observations have no adopted exact-source replay yet and do not establish a physical violation. The original calculation took 923.07 seconds, outside the old passing-root timing sample; N2 now forecasts g0 at 23:00Z to 23:30Z or later, HEURISTIC.

AN392 checks the original root 098 scalar arithmetic independently: its strict conditional gradient upper is 18.943174083661, establishing neither target 1 nor 2.00215453. This is an insufficient interval upper, not a physical counterexample. AN395 freezes request 147 for a fresh root 098 version-02 replay under the admitted 900-second gate. The exact request and the local dispatch extension still require review before execution.

A global background assertion still needs every one of the 128 exact radial roots, both complete successful original owner assignments, and an independently reviewed actual global assembly. Regional coverage cannot replace any missing root or owner receipt.

## Remaining work and schedule

Queuev18 has finished roots021,023 and025. The next reviewed physical batch is queuev19, roots027,029 and031, with requests103,104 and105. The fresh requests124 through146, published in AN384, await individual concrete reviews and an independently reviewed extension of the local actual-review dispatch table. They supply no physical or regional conclusion by themselves.

The coordinator has allocated N2 core 48 to independent AT review hosting after g0 completes successfully, and core 47 after g1 completes successfully. AN357 admits host method v03 and AN376 checks the allocation policy. Each exact assignment still requires its own AN review and AT binding, followed by N2-owned installation and execution, AT intake and AN adoption. A core release alone authorizes no particular root.

The first host batch has at most three roots. Later batches have at most 16 and require the same adopted first-host execution and matching intake lineage. Hosts take eligible completed version-01 roots in descending order; AT works upward locally. The two version-02 retries stay local. The unchanged host worker also requires total physical receipt time below 480 seconds, so a passing stage limit alone does not establish host eligibility. No hosted root starts after 16:00Z on November 4, and its successful completion decision must precede 16:20Z. No bound is claimed for subsequent serialization or operating-system cleanup.

The five near-cover owner jobs are separate. A completed owner can enter the admitted chunk method before the other owners finish, but each such admission needs that owner's whole successful result and receipt. Every chunk checks all 129 coefficient boxes per energy, all 52 source branches, 5136 mode polynomials and 211664 exact coefficients, plus the analytic remainder allowances. Final near integration requires all five owners and both endpoints. No complete near upper has yet been adopted.

The refreshed HEURISTIC physical schedule starts from the 21:46:08Z snapshot with 30 completed roots and 98 remaining. Root 098 receives a chosen 970-second forward allowance; all other original reserves remain. This allowance does not guarantee its completion. The updated scenarios are:

| Remaining physical-root cost | Background phase and selected reserves end | Near admission and final assembly end | Before 16:50Z |
|---|---|---|---|
| all_successful_mean | 2026-11-04T11:46:02.477452Z | 2026-11-04T14:55:19.071112Z | yes |
| recent_six_mean | 2026-11-04T12:44:25.993937Z | 2026-11-04T14:55:19.071112Z | yes |
| 480_wall_cost_planning | 2026-11-04T14:46:10.989685Z | 2026-11-04T16:57:01.643644Z | no |
| recent_mean_with_one_extra_timeout_per_eight_remaining | 2026-11-04T16:30:55.013986Z | 2026-11-04T18:41:45.667945Z | no |
| 900_stage_plus70_overhead_every_remaining | 2026-11-05T03:58:20.989685Z | 2026-11-05T06:09:11.643644Z | no |

The latest six physical receipts, roots [19, 13, 24, 21, 23, 25], average 404.69 seconds. The prefix extrapolations place g0 at 2026-11-04T00:04:12.883321Z, g1 at 2026-11-04T00:50:04.613204Z, n4 at 2026-11-04T07:36:27.357919Z and the last of n0 through n3 at 2026-11-04T13:36:51.896634Z. These are noisy linear projections, not completed owner receipts. Root 098 changes the recent g0 rate materially. The exact adjustment and complete serial near-owner recurrence are in research/background_root098_schedule/PROOF.md and verification/result_v01.json. AT work is excluded from this AN schedule; its separate capacity snapshot is discussed below. Review hosting increases AT capacity and does not increase this agent's physical replay capacity. Saved samples in reports/evidence/x7_at_root015_resource_v01.txt and x7_active_cores_v01.txt document shared-core contention. The coordinator subsequently assigned core 40 to AT and core 41 to T2; T2 reports moving its running row at21:26:30Z. AT1580-1582 clarifies that its five selected reuse samples ran on core41 and did not share core40 with that particular T2 job. Root015 did share core40 and also used fresh compilation. Neither observation isolates a causal timing penalty or establishes a future runtime bound. At the21:26:32Z AT snapshot, the mean-cost serial model with its four-hour reserve overruns the16:50Z deadline by18.6minutes; the best sampled cost leaves106.2minutes. These are reported HEURISTIC scenarios, not independently certified runtime guarantees.

## Scope of other claims

AN348 and AN349 concern the mu72 kernel calculation and radial-core tail under their stated hypotheses. The radial-core tail is only one part of the near calculation. AN364 checks the CS-B scalar assembly conditionally on its derivative and kernel-box bounds and Lemma KT. It does not certify all numerical inputs to CS-B. T2 has also submitted a conditional window transfer at Rw=Ww=200. AN393 independently confirms all proposed window derivative, ratio and scalar-budget comparisons on the full 5120-cell cover. Its 21402 checks, including 8264 central interval pieces, took 0.6963679897598922 seconds. The final record is research/far_window_transfer_audit/verification/result_v03.json; two unsuccessful implementation attempts are retained and excluded. The inherited derivative data, finite kernel calculation and other physical premises remain OPEN. AT1594-1599 independently agrees on the conditional transfer. Its singleton-helper counterexample does not affect the positive-width cells in this actual calculation. AN370 checks the C2 planning arithmetic; a high cost estimate is not a universal algorithmic lower bound. The coordinator keeps C2 OPEN and has scheduled no C2 code before the stop.

AN371 provides a prepared gradient projection from the retained exact component intervals. Its independent conditional method review AT1589-1591 is now adopted in AN394. The complete actual application remains OPEN. The projection can test a gradient threshold independently of the strain predicate, but it still requires all128 roots, both owner results and the complete reviewed assembly.

N1's newer research fits, including b26s, are reported as FLOAT and have not replaced source 013. Their newly reported residual norms have not been independently recomputed in this audit. The conditioning finding AN334 is narrower: it certifies discrepancies in 80 specified stored sixth-derivative mode functionals at one exact radius of source 013. It supplies neither a neighborhood bound nor an error estimate for a full floating integral. A smaller floating loss does not transfer the source 013 certificates to a new coefficient file.

No complete weak-energy constant, invariant-ball closure, definitive closure ratio or stationary existence result is certified here.

## Evidence and execution

AUDIT_LEDGER.md records the dated claims, methods and verdicts, newest last. research/README.md gives the reading order. Candidate 007 SHA256 is ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. Source 013 raw correction SHA256 is a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a and its canonical SHA256 is 2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33.

This agent uses one busy computation on core 50, nice 19 and one numerical thread. Collaboration uses the existing configured agents through files; the provider response identity has not been inspected. There is no JavaScript/TypeScript, server or listener, RLScience or other cluster, remote or paid compute, GPU, Lean/Lake build, foreign write or signal, commit, push or online post. Final audit verdicts are due November 4 at 16:50Z; scientific children stop at 17:05Z and the team at 17:05:30Z.

The new windowed far report also retains the previously reviewed SC(a_W) bound. AT1366-1369 concern this same source and the Rw=Ww=200 flat window and give SC(a_W)<=4194197216881219/9007199254740992. This is a cited independent AT result, not a new AN re-evaluation. The new Schur window transfer and the band term A_E retain their separate verification requirements.

AN386 checks the extra-core option. The current host v03 explicitly admits only N2/core 47 or 48 with the matching complete predecessor. Core 44 hosting or splitting an original near owner would require new reviewed methods and consumers; their review cost is unmeasured. They are not counted as ready capacity.

For the registered mu 68 fallback, this agent names a 23:00Z planning target for the independent weight integrals and endpoint assembly, at the first idle physical-queue boundary after AT's complete mu 68 replay is available. An unblocking host review has priority. Missing inputs defer the slot. The precise scope and initial 120-second cap are in notes/MU68_ASSEMBLY_SLOT_v01.md.
