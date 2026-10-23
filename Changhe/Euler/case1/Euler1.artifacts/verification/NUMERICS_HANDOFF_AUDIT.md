# Numerics final handoff audit

Date: 2026-10-23T07:50:06.315698+00:00. These findings refer to the source hashes in `evidence/final-numerics-handoff-preaudit.json`. Later companion-file repairs need a separate entry; the final REPORT is audited separately.

| Check | Method and result | Verdict |
|---|---|---|
| Graceful stop | runner.log records six worker exits followed by runner exit at 07:47:05 UTC; all seven retained PIDs are no longer active. Written stop confirmation gives the matching final ledger SHA. | CONFIRMED |
| Final training ledger | 64 records, SHA 9f9477b05b19cafb4b8cd911b06c188db5ab1eb22933ae1510703fd3647505ff. Independent credited elapsed union enclosure is 0.999384131987840 to 1.179929723408487 hours. | CONFIRMED |
| Exact compute chunks in STATE and RUN_STATUS | Source instrumentation counts inter-step elapsed pieces, including I/O and short pauses, and omits first steps. Serialized endpoints are rounded. The displayed rounded bounds agree, but the exact-compute wording is false. | REFUTED |
| Ten trained experiments and twenty never-started pending entries | The ledger has 12 distinct experiment IDs. Pending v2_M1_cl047 and v2_M1_cl049 have training history and checkpoints. There are 20 pending entries, of which 18 have no ledger history. | REFUTED |
| Resume reaches the described new secondary branches automatically | bin/resume.sh restores eligible stopped entries and launches the existing queue, including primary-interval runs. It creates no new c_l>1/2 configuration and does not fix the stage-transition resume defect. The proposed secondary program requires configuration and queue changes first. | OPEN |
| Companion NUM_REPORT is current | At this audit it is still the 07:15 report, with superseded countability, runtime and compute-time claims. Update it or preserve it explicitly as historical. | REFUTED |

These are artifact and scope checks. They do not change the confirmed mathematical obstruction or turn any checkpoint into an acceptable approximation. No additional numerical activity is claimed for this audit.

## Partially updated companion report

Date: 2026-10-23T07:53:26.822713+00:00. NUM_REPORT SHA256 `815becd39377604cdeaba42f95ace20767da16e653623328af69e307a27220db`. The new opening has the correct L2 scope and stopped ledger. Sections4,6,7 retain incompatible historical claims. Final acceptance of this companion document remains **REFUTED for the listed assertions**.

- **Numerical screening range**: Section4 and current verdict use 0.17-0.33 and every worst shell1_2; the table already includes 0.146251 and shell0.25_1 cases. Refresh from the forthcoming frozen table. 0.15-0.33 versus 1e-3 is about 2.2-2.5 orders of magnitude, not three to four.
- **Theorem and search status**: Section6 still invokes countability L1 and says the search continues. Replace by the confirmed L2 scope, with the qualitative fixed-class floor only under its full bounds.
- **Runtime and activity**: Section7 still says 24 legacy records and exact compute chunks. The final ledger has 38 legacy and 26 chunk records. Rounded inter-step elapsed chunks include I/O/short pauses and omit first steps. Record bounds on credited elapsed pieces, not eligible compute.
- **Exact resume and rollback**: Restrict exact resume to the tested within-stage cases. The stage-transition counterexample gives max parameter difference 0.00400168198. Disk parameter reload does not fully restore optimizer/sampler/RNG/counters on NaN. Do not state never triggered without an audited log claim.
- **Derivative agreement**: The fast derivative tests use forward values 1e-12, Jacobian 1e-11, Hessian 1e-10, and parameter gradients relative1e-9. The statement 1e-12 including parameter gradients is false.
- **Tail theorem**: Qualify saturation by nonzero first-layer radial weights. Generic tail degeneration is not unconditional over all representable weights.
- **Candidate and amplitude wording**: Write no acceptable candidate was found. A sampled soft amplitude penalty discourages zero collapse but does not prevent it mathematically.
- **Internal diagnostics**: Internal held-out metrics were reused for checkpoint selection. They are diagnostics, not independent acceptance evidence; full-scope ranges and zero-set completeness are not established.

## Further partial repair

Date: 2026-10-23T07:55:18.714208+00:00. Read NUM_REPORT SHA `bee662039bf5c624af5e911cddd4dd3ac9089b48b4a24282ec89e6c52c6117d6` in full, preserved in snapshots. Queue now has12 stopped and18 pending, matching training history. This repairs the earlier count defect. Derivative tolerance wording is corrected. The outstanding stage-transition cause, exact eligible-time scope, old theorem continuation and stale numerical assertions are listed in NOTES_FOR_TEAM at this timestamp. Future revision headers are not used as evidence of elapsed time.

## 2026-10-23T08:08:11.651311+00:00: companion final-report follow-up

Source NUM_REPORT SHA **45c834c82ccc8d239ef7838783eb6be64003c225871541106853efc4f3f796f6**, read in full and frozen at `snapshots/NUM_REPORT-45c834c82ccc8d23.md`. The L2stop,12trained/18never-started counts,64-record ledger,77-state result section,nonzero-radial-weight qualification in the method section,and post-stop stage-boundary repair are now stated correctly. The current header uses an actual past date. These repairs are CONFIRMED.

Remaining REFUTED statements:

- Opening numeric range: 0.17–0.33 is stale; final range0.129427920625–0.333164099022.
- Section4tail ranges: V2includes108.178,so0.8–60is false; v1maximum is2.455906e6.
- Affine lower bound: Minimum0.3286623469does not support at least0.3287. Use at least0.3286or about0.329.
- Section8combined bounds: Inward-rounded1.145–1.325does not enclose1.144556348681–1.325101940102. Use1.144–1.326for conservative display.
- Future accounting: The actual MERGE_GAP=.5branch credits a.4secondnonwork gap. I/O and pauses excluded remains false; see POST_STOP_RUNTIME_AUDIT.
- Continuation scope: The existing resume queue includes many primary exponents and has no c>.5or free-exponent entry. It does not concern secondary questions only.
- Section5tail theorem: The constant angular limit is for the learned leading potential with every first-layer radial weight nonzero. Its learned velocity is an axisymmetric swirl, not an angular constant in Cartesian coordinates.

Evidence: `evidence/numerics-handoff-45c834c82ccc8d23.json`. Current main REPORT approval is separate and cannot endorse these companion statements.

## 2026-10-23T08:13:04.375037+00:00: current source and queue repairs

Read the complete NUM_REPORT diff to SHA37492ea37adf6ca0888e037691223f5cba512e63738a46f2170ed898a86a0f52and the complete train.py diff to2f6dbd5ecb0f18f8. Opening momentum range,v2tail range,affine lower bound and credited-time enclosures are repaired: CONFIRMED. The source now preserves separated work intervals; the prior gap counterexample passes in both actual accounting branches. Current queue has only five c=.5eligible entries;25primary entries are archived. Both repairs are CONFIRMED by `post_stop_audit/2f6dbd5ecb0f18f8/ACCOUNTING_FOLLOWUP.json`.

Remaining REFUTED companion assertions: section5unconditionally identifies the learned leading tail as angularly constant without specifying potential or nonzero radial weights; section7still calls stage-transition failure a current remaining defect; section4states a v1range ending at1e6although the maximum is2.455906e6. Universal exact resume and eligible-time certification remain OPEN. The section3steps6400-7500also miss the actual cl.41finalstep7643; the table is labeled approximate but should be refreshed. No main-report endorsement transfers to companion prose.
