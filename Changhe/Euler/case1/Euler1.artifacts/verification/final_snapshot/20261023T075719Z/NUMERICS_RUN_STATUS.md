# RUN_STATUS (e1-num, numerics)

Status: CAMPAIGN STOPPED (lead instruction 2026-10-23 07:38Z, PROMPT section 13: Theorem L2 excludes the whole primary
exact-profile class 0 < c_l < 1/2; independently proved by the verifier and audited). Last update 2026-10-23T08:05Z. Shift 1.

Stop confirmation: bin/stop.sh issued 07:46:51Z; runner exited 07:47:05Z after all six workers checkpointed and exited with
code 3 (pilot_cl045_M1, v1_M1_cl050, v2_M1_cl041, v2_M1_cl043, v2_M1_cl045, v2_M1_cl050). Verified at 07:47:39Z: no train.py or
runner.py process exists. CAMPAIGN_LEDGER.jsonl final state: 64 records,
SHA256 9f9477b05b19cafb4b8cd911b06c188db5ab1eb22933ae1510703fd3647505ff. Nothing is appended to the ledger after this.
Queue: 12 entries in queue/stopped (all trained, with checkpoints; the ledger has these 12 experiment ids), 18 in queue/pending
(never started), 0 running/done/failed. Credited elapsed time (union over workers): 0.999 h to 1.180 h (STATE.json; verifier's
reconstruction agrees). This bounds trainer-credited intervals (incl. checkpoint I/O and pauses < 30 s), not eligible compute.

Done this shift (06:13-07:50Z): full solver (euler_ss/: vector potential + pressure, hard Q symmetry, two representations v1/v2,
seed and blob families, fast hand-derived second-order forward propagation), 17 unit tests incl. EQUATIONS.md T1-T8, worker with
atomic checkpoints and exact resume (Adam and L-BFGS mid-block, bitwise), detached runner with launch/status/stop/resume/hold,
ledger with per-step credited elapsed chunks and lower/upper bounds, holdout validation with stagnation-set, parity,
Fourier and tail diagnostics, offline audit evaluate.py, publish.py, snapshot.py; 12 experiments trained for 0.3-1.1 h each
(all stopped in Adam stage 0/1); two astra consultations (code audit, far-field expansion).

RESUME_HERE (next shift): the campaign is CLOSED unless the lead's NOTES_FOR_TEAM.md reopens numerical work. Do NOT run bin/resume.sh
or train.py (they append to the ledger) unless the lead asks. Each shift: (1) read e1-lead/NOTES_FOR_TEAM.md, e1-lead/REPORT.md,
e1-ver/VERIFY_REPORT.md, e1-ver/REPORT_AUDIT.md for requests addressed to numerics (e.g. checkpoint/format questions, STATE.json
fields, artifact fixes) and answer them in files; (2) keep project/artifacts current (code, configs, ledger copy, STATE.json,
NEXT_STEPS.md, NUM_REPORT.md, reports/, candidates/) and under 50 MB; (3) keep NUM_REPORT.md consistent with the verifier's
verdicts (never quote trainer metrics as evidence). If reopened: NEXT_STEPS.md lists the continuation queue; entry point bin/resume.sh.
