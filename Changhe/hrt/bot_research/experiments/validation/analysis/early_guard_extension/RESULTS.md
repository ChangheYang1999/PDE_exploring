# Early round6 guard extensions: development results

2026-10-31T14:47:58.565928+00:00

All72 declared games ended at round50. The table reports the target's
outcome, with identical results and normalized complete histories in both
assignments. P5TNUB wins22 and loses2 games; strike_until6 and strike_until7
each win20 and lose4. These are counts over designed conditions, not
independent random samples or estimated deployment rates.

| Target | Extension and handoff | Target:counter HP | Outcome |
| --- | --- | ---: | --- |
| P5TNUB | none_h10 | 660:755 | L |
| P5TNUB | none_h12 | 660:547 | W |
| P5TNUB | screened_h10 | 800:729 | W |
| P5TNUB | screened_h12 | 800:157 | W |
| P5TNUB | free_t3x3_h10 | 800:695 | W |
| P5TNUB | free_t3x3_h12 | 800:81 | W |
| P5TNUB | free_t3x6_h10 | 800:755 | W |
| P5TNUB | free_t3x6_h12 | 800:215 | W |
| P5TNUB | free_t4x1_h10 | 800:755 | W |
| P5TNUB | free_t4x1_h12 | 800:215 | W |
| P5TNUB | splash200_h10 | 800:695 | W |
| P5TNUB | splash200_h12 | 800:155 | W |
| P5TNUB_strike6 | none_h10 | 520:729 | L |
| P5TNUB_strike6 | none_h12 | 520:287 | W |
| P5TNUB_strike6 | screened_h10 | 520:755 | L |
| P5TNUB_strike6 | screened_h12 | 520:453 | W |
| P5TNUB_strike6 | free_t3x3_h10 | 800:755 | W |
| P5TNUB_strike6 | free_t3x3_h12 | 800:635 | W |
| P5TNUB_strike6 | free_t3x6_h10 | 800:755 | W |
| P5TNUB_strike6 | free_t3x6_h12 | 800:695 | W |
| P5TNUB_strike6 | free_t4x1_h10 | 800:755 | W |
| P5TNUB_strike6 | free_t4x1_h12 | 800:695 | W |
| P5TNUB_strike6 | splash200_h10 | 800:755 | W |
| P5TNUB_strike6 | splash200_h12 | 800:635 | W |
| P5TNUB_strike7 | none_h10 | 380:521 | L |
| P5TNUB_strike7 | none_h12 | 380:53 | W |
| P5TNUB_strike7 | screened_h10 | 520:549 | L |
| P5TNUB_strike7 | screened_h12 | 520:13 | W |
| P5TNUB_strike7 | free_t3x3_h10 | 660:549 | W |
| P5TNUB_strike7 | free_t3x3_h12 | 660:65 | W |
| P5TNUB_strike7 | free_t3x6_h10 | 800:755 | W |
| P5TNUB_strike7 | free_t3x6_h12 | 800:695 | W |
| P5TNUB_strike7 | free_t4x1_h10 | 800:755 | W |
| P5TNUB_strike7 | free_t4x1_h12 | 800:695 | W |
| P5TNUB_strike7 | splash200_h10 | 660:575 | W |
| P5TNUB_strike7 | splash200_h12 | 660:215 | W |

The hypothesis that either strike setting repairs the empty-extension H10
control is REFUTED. Strike6 buys eight tier2 in round6 against the visible
one-splash map. The counter installs its original second splash that same
round; all eight are stopped. Reduced insurance then allows two tier5 copies
to arrive in round7, costing280 HP. The target ends520:729. Strike7 ends
380:521. Both strike settings also lose against the two-gun screened H10
extension. The proposed three-tier3 early strike was not the attack actually
selected by current-map scoring.

The hypothesis that stronger guards preserve the counter's H10 advantage
is REFUTED for the tested140,180 and200-cost extensions: all these variants
lose against all three targets. The60-cost screened extension wins against
both strike policies but loses729:800 against ordinary P5TNUB. Thus component
zero-damage checks do not imply stronger full-game counters. Their extra
construction changes growth and the later responses of both policies.

All72 strict checks and original-engine replays pass. Replays took33.135876
seconds. All73 declared inputs and the exact sharded condition coverage
pass the data archive audit. Fresh counter calls through round6 reproduce
all72 prefixes exactly, leave observations unchanged, submit only legal
actions and complete their chosen extension. Twelve additional full-history
checks cover all three targets against empty and screened H10. All600
fresh decisions reproduce exactly and legally. Their elapsed runtime was
56.965422 seconds. Filtered excess factory proposals are recorded; they
are not submitted actions or game rejections.

The independent action replays do not add strength samples. The handoff
F34 delegate retains its3-second planning cutoff; observed exact reproduction
does not prove timing-independent behavior on every future machine load.
Evidence is in verification/full_games.json, verification/full_histories.json,
runs/validation/early-guard-{strict,replay,summary,data,prefixes,full-histories}-001.json,
and the original predeclared early-guard-handoff-001.json. Pool C remains unused.
