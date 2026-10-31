# Queue plan for Phase II (specification 8.2, 8.3, 8.4) - prepared before the release; executed only after the lead's PROVISIONAL / FULL RELEASE

Objective O1 for every job (specification 4.1); label FREE unless stated; priority decides the order (higher first); every job is exclusive on its GPU.
Budgets (specification 8.5): wave-1 pilot max_iter 120, time_limit 3600 s (at about 50 s per iteration the 3600 s limit binds at about 70 iterations; this is
accepted for a pilot and recorded); medium max_iter 300, time_limit 10800 s; long when O1 still falls by more than 1 per cent per hour (continuation
jobs from the saved end state). specification 8.4 pairs: each FIXED-CONTROL mirrors its FREE partner SEGMENT BY SEGMENT (same max_iter and time_limit per
segment, same start file; every continuation of the FREE partner is matched by a continuation of the control from its own end state); the iterations
actually reached and the wall time are recorded for both partners and stated in the pair result when a time limit stopped one of them.

## Wave 1 (pilots, provisional release: at most two concurrent FREE jobs; lead correction 21:36Z/22:08Z: three distinct lineages)
P1  FREE  S01 nest6 (0.45, 1.0) own parameters            [F1, nest-ladder lineage]      tag w1_S01
P2  FREE  S09 d6w R1 (0.45, 0.3) own parameters           [F1, D6 / independent-route lineage]  tag w1_S09

## Wave 2 (full release; F1 lineage starts at their own parameters)
F1: S03 s11 closure-1 (0.45, 1.0); S07 s11 closure-1 (0.45, 0.3); S11 nest6 (0.42, 0.3); S09 d6w R1 (0.45, 0.3); S10 d6t (0.45, 0.3; basis without
    extended channels: its own basis is kept); S02 nest6 p1 (0.45, 1.0); S06 nest6 p1 (0.45, 0.3); S12 s12 rl3 (0.42, 0.3); S13/S14/S15 omega scans
    (0.5, 0.2, 0.1); S16/S17 c_l scans (0.47, 0.46); S18 R0 = 0.15 refit; S19/S20 all-mode class (unrestricted m).
FIXED-CONTROL pairs (specification 8.4, at most 15 per cent of GPU-hours together with PROFILE; lead 21:36Z: three lineages): P1 S01 (nest ladder),
    P2 S09 (D6 lineage), P3 S20 (all-mode class), each FREE and FIXED-CONTROL with the same max_iter and time limits (tags c_S01, c_S09, c_S20).
    S05 and S11 share the nest-ladder lineage with S01 and are not used as pair partners.

## Wave 3 (F2 to F6: perturbed parameters, perturbed coefficients, random seeds, Sobol design)
F2: S01 at (0.42, 0.3) and at (0.47, 5.0), S05 at (0.45, 1.0), S11 at (0.45, 0.3); each twice: coefficients kept and refit (param_init refit).
F3: S01 and S05 with perturb_nonaxi 1e-3 and 1e-1 (seeds 1, 2).
F4/F6: random seeds (family random, nonaxi, toroidal, poloidal) at the 16 Sobol points of specification 8.2 F6 (c_l in [0.405, 0.495], log omega in
    [log 0.05, log 20]; scrambled Sobol, seed 20261028), pilots first (max_iter 60), promoted when O1 falls below 10 x the best F1 pilot.
F5: S18 (R0 = 0.15 basis) and S19/S20 (all modes) as diverse core/tail structures.

## Commands (examples)
python scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FREE --tag w1_S01 --max_iter 120 --time_limit 3600 --priority 20
python scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FIXED-CONTROL --fixed --tag c_S01 --max_iter 120 --time_limit 3600 --priority 11   # mirrors w1_S01
python scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FREE --tag f2_S01_a --c_l 0.42 --omega 0.3 --param_init refit --max_iter 300 --priority 12
python scripts/enqueue_d6.py --random --family random --c_l 0.44 --omega 0.3 --seed 7 --label FREE --tag f4_s07 --max_iter 60 --time_limit 1800 --priority 9
Continuation of an end state: --start runs/<job>/starts/start_000.pt (the saved state carries c_l, omega in z when free; the basis is identical).
