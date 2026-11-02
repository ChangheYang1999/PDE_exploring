# Early-wall transfer over the complete development union

Checked 2026-10-31T18:32:24.303546+00:00.

The strict paired improvement claim is REFUTED: the old delegated counter scored 80W/10D/0L, and guard00 scored 86W/0D/4L on the same ninety target-and-seat conditions. There are 8 improvements and 4 regressions in W/D/L order. The separate no-loss claim on four additional counter policies is REFUTED: 2W/4D/2L.

The policy, component-selected witness and target set were fixed before this matrix. This is development evidence after guard00 performed well on four current teammates; it is not an estimate from an untouched opponent sample.

| Target | Earlier delegated counter | Early-wall guard00 |
|---|---|---|
| E20 | W 618:-40 r10 | W 785:740 r50 |
| E25RM | W 618:-40 r10 | W 785:740 r50 |
| E27 | W 618:-40 r10 | W 785:740 r50 |
| E29 | W 618:-40 r10 | W 785:740 r50 |
| E30 | W 618:-40 r10 | W 785:740 r50 |
| F36 | W 765:740 r50 | W 780:740 r50 |
| F37 | W 765:740 r50 | W 780:740 r50 |
| F38 | W 765:740 r50 | W 780:740 r50 |
| F39 | W 765:740 r50 | W 780:740 r50 |
| P4TNUB | W 755:740 r50 | W 770:740 r50 |
| P5M_poke0 | W 788:740 r50 | L 722:740 r50 |
| P5M_poke2 | W 744:740 r50 | W 754:740 r50 |
| P5M_poke3 | W 755:740 r50 | W 770:740 r50 |
| P5M_poke4 | W 740:660 r50 | W 760:740 r50 |
| P5TNUBM | W 755:740 r50 | W 770:740 r50 |
| bait_guard_A | not in paired control | L 365:380 r50 |
| bait_guard_B | not in paired control | W 365:360 r50 |
| best_v9e | W 755:740 r50 | W 770:740 r50 |
| cash_rank_10_g3_tier1 | W 715:-210 r9 | W 800:-235 r9 |
| cash_rank_10_g3_tier5 | W 660:-3 r9 | W 660:-15 r9 |
| cash_rank_10_g6_tier1 | W 800:-200 r10 | W 800:-50 r10 |
| cash_rank_10_g6_tier5 | W 380:-115 r11 | W 380:-115 r11 |
| cash_rank_1_g3_tier1 | W 710:-210 r9 | W 800:-235 r9 |
| cash_rank_1_g3_tier5 | W 380:-195 r9 | W 660:-15 r9 |
| cash_rank_1_g6_tier1 | W 800:-70 r10 | W 800:-50 r10 |
| cash_rank_1_g6_tier5 | W 240:-100 r11 | W 240:-100 r11 |
| delegated_adaptive | not in paired control | D 740:740 r50 |
| delegated_early | not in paired control | D 740:740 r50 |
| eco3_t1 | W 800:-40 r8 | W 800:-235 r9 |
| eco5_t1 | W 800:-40 r8 | W 800:-55 r9 |
| eco5_t3 | D -526:-40 r8 | W 592:-15 r9 |
| eco6_t5 | D -40:-40 r8 | W 520:-100 r11 |
| empty_g3_tier1 | W 800:-40 r8 | W 800:-235 r9 |
| empty_g3_tier5 | W 240:-40 r8 | W 660:0 r9 |
| empty_g6_tier1 | W 800:-40 r8 | W 800:-50 r10 |
| empty_g6_tier5 | D -40:-40 r8 | W 520:-100 r11 |
| gun_t3 | W 540:-40 r8 | W 774:-144 r9 |
| heavy_t4 | W 800:-40 r8 | W 800:-50 r8 |
| lead8 | D -40:-40 r8 | L 380:500 r50 |
| lead_opening_g3_tier1 | W 715:-210 r9 | W 800:-235 r9 |
| lead_opening_g3_tier5 | W 660:-3 r9 | W 660:-15 r9 |
| lead_opening_g6_tier1 | W 800:-200 r10 | W 800:-50 r10 |
| lead_opening_g6_tier5 | W 380:-115 r11 | W 380:-115 r11 |
| mixed5 | D -40:-40 r8 | W 680:-30 r9 |
| rush_t1 | W 650:-40 r8 | W 720:-95 r8 |
| rush_t2 | W 560:-40 r8 | W 740:-95 r8 |
| rush_t3 | W 462:-40 r8 | W 696:-50 r8 |
| splash3_t4 | W 620:-40 r8 | W 740:-22 r9 |
| splash_t2 | W 728:-40 r8 | W 800:-96 r9 |

All 5248 fresh action-generating calls across both policies agree with recorded actions. Original-engine replay, explicit source and JSON archives, observation immutability and legal submissions pass. There are 0 filtered guard proposals, zero rejected submitted actions and zero bot errors. 49 of 49 assignment pairs have identical complete canonical histories.

Actual guard decisions took 506.066961 seconds across 2624 calls; the largest single call was 1.306246 seconds. These measurements use one assigned CPU core at low priority, one numerical thread, and the shared-machine load. Audit time is excluded.

The old control used best.py at the frozen best_v9e hash. The new target imports its byte-identical frozen copy, allowing the lead to work without changing this comparison. The receipt verifies that equivalence from the old source attestation. Forty-four other old target specifications are unchanged. Earlier control results and their original audits are reused explicitly; they are not additional new games.

A favorable aggregate does not establish dominance over every tested opponent: the paired regression list in verification/full_games.json is authoritative. Nor does this test cover the full public-clone timing grid or arbitrary randomized opponents.

Reproduce every manifest listed in early-wall-transfer-campaigns-001.json using bot_research.experiments.validation.run_data_development, then audit_development_strict, replay_audit, audit_data_archives and check_early_wall_histories. The pipeline log retains exact bounded commands. Restore any archived old replay before pairing controls. Use the existing Python with bytecode disabled, research temporary directory, assigned affinity, low priority and one numerical thread.
