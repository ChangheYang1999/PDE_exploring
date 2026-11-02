# Timing challenge results

Checked 2026-10-31T17:17:19.826548+00:00.

The no-defeat claim is CONFIRMED. The no-W/D/L-regression claim is CONFIRMED.

The emergency-template control scores 60W/0D/0L; the frozen Fortress 38 handoff scores 60W/0D/0L. All sixty conditions per continuation are included. W/D/L transitions are {'W->W': 60}. These are thirty deliberately selected development targets in both physical assignments, not samples from an opponent population.

Each outcome cell gives counter outcome, HP counter:target and final round. Equal assignments share a cell; differences are explicit. The last column gives the target's actual minion-purchase count against template/Fortress 38. The target parameter is a proposed attack round; an unaffordable or unproductive attack can result in zero purchases. Its budget fraction controls defensive forecasting.

| Target | Emergency template | Fortress 38 handoff | Selected branch | Actual target purchases old/new |
|---|---|---|---|---|
| budget_r3_tier2_f000 | W 692:-40 r9 | W 692:-40 r9 | growth | 3/3 |
| budget_r3_tier2_f050 | W 728:-180 r9 | W 728:-180 r9 | growth | 2/2 |
| budget_r3_tier2_f100 | W 728:-40 r8 | W 728:-40 r8 | growth | 2/2 |
| budget_r3_tier3_f000 | W 644:-40 r9 | W 644:-40 r9 | growth | 1/1 |
| budget_r3_tier3_f050 | W 644:-600 r9 | W 644:-600 r9 | growth | 1/1 |
| budget_r3_tier3_f100 | W 800:740 r50 | W 800:-520 r11 | early | 0/0 |
| budget_r4_tier2_f000 | W 680:-40 r9 | W 680:-40 r9 | growth | 5/5 |
| budget_r4_tier2_f050 | W 728:-40 r8 | W 728:-40 r8 | growth | 3/3 |
| budget_r4_tier2_f100 | W 776:680 r50 | W 776:-246 r12 | early | 2/2 |
| budget_r4_tier3_f000 | W 514:-40 r9 | W 514:-40 r9 | growth | 2/2 |
| budget_r4_tier3_f050 | W 670:-320 r9 | W 670:-320 r9 | growth | 1/1 |
| budget_r4_tier3_f100 | W 800:740 r50 | W 800:-520 r11 | early | 0/0 |
| budget_r4_tier4_f000 | W 800:-40 r9 | W 800:-40 r9 | growth | 0/0 |
| budget_r4_tier4_f050 | W 800:380 r50 | W 800:380 r50 | growth | 0/0 |
| budget_r4_tier4_f100 | W 800:740 r50 | W 800:-520 r11 | early | 0/0 |
| budget_r5_tier3_f000 | W 436:-40 r9 | W 436:-40 r9 | growth | 3/3 |
| budget_r5_tier3_f050 | W 566:-320 r9 | W 566:-320 r9 | growth | 2/2 |
| budget_r5_tier3_f100 | W 800:740 r50 | W 800:-520 r11 | early | 0/0 |
| budget_r5_tier4_f000 | W 500:-40 r9 | W 500:-40 r9 | growth | 1/1 |
| budget_r5_tier4_f050 | W 800:380 r50 | W 800:380 r50 | growth | 0/0 |
| budget_r5_tier4_f100 | W 800:740 r50 | W 800:-520 r11 | early | 0/0 |
| budget_r6_tier4_f000 | W 320:-40 r9 | W 320:-40 r9 | growth | 2/2 |
| budget_r6_tier4_f050 | W 560:-320 r9 | W 560:-320 r9 | growth | 1/1 |
| budget_r6_tier4_f100 | W 800:740 r50 | W 800:-520 r11 | early | 0/0 |
| budget_r6_tier5_f000 | W 800:-40 r9 | W 800:-40 r9 | growth | 0/0 |
| budget_r6_tier5_f050 | W 800:380 r50 | W 800:380 r50 | growth | 0/0 |
| budget_r6_tier5_f100 | W 800:740 r50 | W 800:-520 r11 | early | 0/0 |
| budget_r7_tier5_f000 | W 380:-40 r9 | W 380:-40 r9 | growth | 1/1 |
| budget_r7_tier5_f050 | W 800:380 r50 | W 800:380 r50 | growth | 0/0 |
| budget_r7_tier5_f100 | W 800:740 r50 | W 800:-520 r11 | early | 0/0 |

All 120 games pass strict accounting, original-engine replay, registered source/data checks, and 2504 freshly regenerated counter decisions. Every submitted action is legal, observations remain unchanged, and no bot error is recorded. An independent implementation checks 2504 public handoff decisions and 18 actual starts. Every paired game has exactly the same first four complete rounds after removing only the run identifier. All 42 selected growth-branch pairs have identical complete histories; 42 of sixty pairs agree completely overall.

The first 001 attempt stopped after twelve games when its archive audit found three unregistered JSON dependencies. These files already had constructor-level hash checks, but that did not satisfy explicit data registration. The full unchanged grid was redeclared as002 with all three files registered and archived. All twelve completed initial histories agree exactly with the corresponding corrected runs. Both attempts and the audit failure are retained. Only the complete002 grid supplies the table above.

Measured counter decision costs are summarized in the receipt as call counts, summed wall time and maximum call time. They are low-priority measurements on shared hardware. Frozen teammate planners may use wall-clock cutoffs; observed equality does not guarantee equality under arbitrary load. No installed-candidate change or held-out claim follows.

Reproduce the ten delegated-timing-*-002 manifests using run_data_development, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_delegated_histories and audit_delegation. Run this publisher after all campaigns finish. Use the existing project Python, disabled bytecode, research temporary directory, assigned affinity, one numerical thread and low priority. Exact commands are in the corrected pipeline log; verification/full_games.json pins all result inputs and the publisher.
