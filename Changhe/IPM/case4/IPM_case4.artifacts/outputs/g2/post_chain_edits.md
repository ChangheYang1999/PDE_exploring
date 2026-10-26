# Edits to re-apply AFTER the g2_v3 chain is complete (reverted to frozen bytes at 05:47Z so the per-step hash verification passes)
1. campaign860.py initialize(): replay file carries P, high, low, residual only (no column_scales); compute `A, scales = feasible_matrix(J, chart)` from the Jacobian at the seed.
2. bench860.py: load `B.REPLAY_REFERENCE_FILE` instead of seed_860.npz.
3. tests/g3_t4.py: P/high/r_seed from `B.REPLAY_REFERENCE_FILE`; scales_seed from the sealed g2_v1 seed_860.npz only as a comparison note (not a gate).
4. bin/supervise860.sh: SEEDNPZ = outputs/campaign860/seed/seed_860_replay_v2.npz.
5. freeze_manifest.sh (new version): also hash research/base/basis_tests.py, base/engine/ipm_portable.py, base/engine/taylor_jet.py, base/spectral_basis.py (loaded handoff files not in the frozen 181D closure list).
6. (2026-10-24T05:59:39Z) Lead pre-audit F1-F11 implemented in outputs/g2/pending_edits/campaign860.py (v2) and supervise860.sh (v2); new files work/research860/assess_cadence860.py and outputs/campaign860/campaign_policy_v2.json (PSI 60, max_seconds 6600 = slice 3300 + reserve 1800 + recover 1500). Launch line: taskset -c 78-89 nice -n 19 setsid nohup bin/supervise860.sh <root> <label> 3300 8 ... G4 restart tests (SIGTERM between trials, SIGKILL inside a trial) to be run in the pilot.
[2026-10-24T06:10:31Z] pending edits copied into place after the g2_v3 chain stop (campaign860.py v2, bench860.py, tests/g3_t4.py, bin/supervise860.sh v2)
7. (2026-10-24T06:57:40Z) campaign860_v3.py and supervise860_v3.sh (F12-F19, SPEC v9.3 section 11: exceptional-parameter stop, rounding bound kappa=2^11) written in outputs/g2/pending_edits; to be applied after the g2_v4 chain under manifest g3_v1 with their G4 fixtures.
