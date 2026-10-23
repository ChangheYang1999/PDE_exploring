# Post-stop trainer repair audit

Date: 2026-10-23T08:01:05.202601+00:00. Source train.py SHA256: `61c6f9e23750908e6b3bb655dca6e72660bcf0ca6b8f36df1c4cb817f451a66c`. Source bundle: `post_stop_audit/61c6f9e23750908e/SOURCE_MANIFEST.json`. These changes were read after the numerical campaign stopped and after the evidence freeze. No checkpoint result or frozen ledger is changed by this audit.

| Check | Method and result | Verdict |
|---|---|---|
| Stage-boundary retained-batch repair | Repeated the earlier four-step Euler Adam counterexample against a copied new trainer: two stages, resample_every5, interruption immediately after the atomic stage-advance checkpoint. Model parameters now agree bitwise (maximum difference0); optimizer, sampler, RNG states and numerical counters also agree. Only validation metrics were replaced by a deterministic inexpensive stub. | CONFIRMED |
| Claimed exclusion of every logging or pause interval | Executed the actual interval-merging AST branch on work intervals[0,0.1] and[0.5,0.6]. It credits[0,0.6], including the0.4-second nonwork gap, because MERGE_GAP=0.5. The true work union is0.2seconds. | REFUTED |
| Future measurement improvement | Step starts and synchronized ends are now recorded and validation intervals are included. This fixes the omitted first-step structure, but rounding, merged gaps and suspension within a timed block remain. The historical ledger is unchanged. | CONFIRMED |
| Exact resume for all histories and configurations | The executed case is specific. Legacy retained batches without new stage/count/sampler metadata are redrawn; arbitrary configuration edits and every optimizer interruption are not covered by this test. | OPEN |
| Full NaN recovery | The new source diff does not repair full sampler/RNG/counter and L-BFGS-state rollback. No assertion is made that a campaign run encountered a NaN. | OPEN |

The lifecycle test ran from 2026-10-23T08:00:14.326436+00:00 to 2026-10-23T08:00:28.681857+00:00 in a local single-thread CPU child at nice19. Its duration is separately recorded, receives no campaign-time credit, and is outside the frozen report snapshot. No server, JavaScript/TypeScript, RLScience access, remote compute or out-of-lane write was used by this verifier test.

Evidence: `post_stop_audit/61c6f9e23750908e/RESULT.json`, `post_stop_audit/61c6f9e23750908e/ACCOUNTING_GAP.json`, and the continuous/interrupted/resumed logs. The earlier historical counterexample remains valid for its original source hash.

## Later accounting repair, 2026-10-23T08:13:04.375037+00:00

Current train.py SHA `2f6dbd5ecb0f18f8f2256c24274b6e02beee289a7a7bf812f97266ddc3131033` removes merging from both the optimizer and validation accounting branches. I read the complete diff from61c6f9e23750908e and executed both actual AST branches on the same two intervals[0,.1]and[.5,.6]. Each now credits two separate intervals totaling0.2seconds. The demonstrated0.4-second gap defect is repaired: **CONFIRMED**. This is a static code-branch test, with no model execution or campaign-time credit. Millisecond endpoint rounding and time suspended inside a measured block remain; exact eligible accounting is not established. The stage-transition repair code is unchanged by this diff.

The queue now has two stopped and three pending c_l=.5entries, with25primary entries preserved under archived_primary. The earlier queue-scope finding is repaired: **CONFIRMED**. New c_l>.5or free-exponent configurations are still absent. Evidence: `post_stop_audit/2f6dbd5ecb0f18f8/ACCOUNTING_FOLLOWUP.json`.
