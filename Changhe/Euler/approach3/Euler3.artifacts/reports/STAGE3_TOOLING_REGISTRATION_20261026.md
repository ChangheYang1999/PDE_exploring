# Stage III tooling registration (numerics; 2026-10-26T18:57Z; rule AU: nothing here is used on a Stage III job before the lead's dated review, due 2026-10-27T12:00Z)

## T1. scripts/cap_watcher.py (lead IE/IF condition S3-14; separate detached process acting on the live worker PID; lead IH (c))
- Frozen sha256 of scripts/cap_watcher.py: e4e3a5aa1f82faace27631486e8313eca112b3da59c8293911dc17954c03f353
- Exact command line (one watcher per job, started detached right after the job's first heartbeat appears; CPU only, no GPU):
  cd . && setsid nohup .venv/bin/python scripts/cap_watcher.py --job <JOB_ID> --cap_seconds <CAP> --abs_end <YYYY-MM-DDThh:mm:ssZ> --poll 30 --grace 120 > runs/_logs/capwatch_<JOB_ID>.log 2>&1 &
- What it binds: the job id (string); the owned worker PID read from status/heartbeat_<JOB_ID>.json (field pid; or --pid), verified against /proc/<pid>/cmdline, which must contain
  the job id, otherwise nothing is signalled and the watcher exits with a record; the start epoch (the first heartbeat's epoch field); the whole-job cap in occupied seconds
  (setup + LM + battery) measured from that epoch; the absolute UTC end; the grace period between SIGTERM and SIGKILL (default 120 s; the worker checkpoints on SIGTERM).
- Actions: poll every 30 s; exit without action when the owned PID is gone or the job's queue/running entry disappears (job ended on its own); at the cap or the absolute end:
  SIGTERM to the owned PID, wait the grace period, SIGKILL if still alive; never a retry or relaunch; the record status/cap_watcher_<JOB_ID>.json (job, watcher pid, owned pid, start
  epoch, cap, absolute end, events with UTC stamps, action, occupied seconds at stop and at exit, final flag) is rewritten atomically every poll and on exit.
- Smoke logs (disposable fake workers, CPU; S3-14 (b)):
  - SIGTERM path: runs/stage3_smoke/capwatch_smoke_20261026T1844Z.log (sha 0693e0788b9be446162a818227b44a7e2c78fe48420d15bd583d0134af2e8bfb); record runs/stage3_smoke/capwatch/record_smoke_capwatch_20261026T1844Z.json (sha 04d7908f5bda3c53b3d11e8b32c5ce86ab94340a8b27b274d6d93a10a85c0a93):
    fake worker 'exec -a worker_fake_<job> sleep 600', hand-written heartbeat and running entry, cap 15 s, poll 2 s, grace 6 s; bound 18:44:30Z; SIGTERM at occupied 17 s (one poll late);
    the process ended within the grace; action SIGTERM; occupied_seconds_final 19.0; final true.
  - SIGKILL path: runs/stage3_smoke/capwatch_smokeK_20261026T1847Z.log (sha ab37cb8d5fd406d40109920d63711760e9357bdc4844e58a44d7283c1cdb1b7f); record runs/stage3_smoke/capwatch/record_smoke_capwatchK_20261026T1847Z.json (sha ccf56575e2b3d7c19259081abf251df29d99a72351700d8281c98775ad0c0fd2):
    a Python fake worker ignoring SIGTERM (argv carries the job id), cap 8 s, grace 6 s; SIGTERM at occupied 8 s, SIGKILL at 14 s, process gone; action SIGKILL; final true.
- Limits: the watcher's cap is wall-clock occupied seconds, not GPU utilisation; it acts only on the bound PID (the worker process; its CUDA context dies with it); the supervisor sees the
  job end as a failure/exit and, with max_retries 0, does not relaunch (S3-2). For Stage III jobs the cap values are those of the registration section 6 (3.4 GPU-h = 12240 s; R2a 4.6 GPU-h =
  16560 s; R3 8 GPU-h = 28800 s) and the absolute ends of section 7 / IF.

## T2. pivot_rank option (lead IE condition S3-5) and the S3-22 start record: ONE worker diff (lead IJ)
- Production state at 2026-10-26T18:57Z: scripts/worker.py sha256[:12] 3bed13b5c663 and src/optimization/problem.py ca146af805bd (the pivot_rank edit of 18:49Z, accepted by the lead for the pending
  Stage II jobs with the default path unchanged; backups scripts/worker.py.bak_1849 = 1db489a1a0f5, src/optimization/problem.py.bak_1849 = 185cecd9c831).
- Candidate (NOT in production; a separate tree runs/stage3_smoke/worker_candidate_tree/): scripts/worker.py with the S3-22 start_record block (flag start_record, default off); sha256[:12]
  57c2386aeee8 at 2026-10-26T18:57Z (frozen sha and diff appended below after the smoke).
- Smokes (disposable L4 Nk12 lm_only job from nest4 (0.45, 1) p0, 6 iterations, CPU; the sgsmoke configuration):
  - prsmoke A/B/C (runs/stage3_smoke/prsmoke_20261026T1850Z/): A = the OLD worker 1db489a1 with the old problem.py 185cecd9 (copied tree old_tree/), B = the live code (pivot_rank absent),
    C = pivot_rank 2. Required: A and B bitwise equal in cost, damping, acceptance and iterate hash on every iteration (results.jsonl and the saved z compared); C logs the rank-2 pivot.
    RESULT: appended below when complete.
  - candidate smoke A'/B'/D: A' = the production worker 3bed13b5 (defaults), B' = the candidate worker with start_record absent (must be bitwise equal to A'), D = the candidate with
    start_record true (the record written; the frozen residual bitwise restored after the probe; the first LM trial identical to A'/B'). RESULT: appended below when complete.
- Equality with block_costs.py --phase_align (S3-22): the record's cost_frozen_at_projected and cost_refreshed_at_projected are compared with the pre-launch block-cost totals of the same
  start and job JSON (relative 1e-6).

### T2 result 1 (2026-10-26T19:11Z; wording corrected per lead IR (1) at the end of this section): prsmoke A/B/C COMPLETE (runs/stage3_smoke/prsmoke_20261026T1850Z/; 6 LM iterations each, lm_only; torch intra-op threads 2 (job field threads, worker.py line 101), OMP_NUM_THREADS=4 in the environment; the LM ran 1052 s (A), 1060 s (B) and 1061 s (C) against time_limit_per_start 900 s: lm.py checks the time limit only after each iteration, so it is not a cap; status time_limit)
- A (old worker 1db489a1 + old problem.py 185cecd9, copied tree old_tree/) and B (live worker 3bed13b5 + problem.py ca146af8, pivot_rank absent): the saved histories are BITWISE EQUAL on all
  6 iterations (cost to 17 digits: 8.1318105546369929e-07, 1.7529182517008575e-06, 9.4415465558474490e-07, 7.5307759093551682e-07, 7.2208754822272771e-07, 7.1363254166746050e-07; damping
  3.0e-3, 9.0e-4, 4.32e-3, 5.184e-3, 6.2208e-3, 1.741824e-2; all accepted; iterate hashes 21f92990de74 ... 1bfdd72ad10d) and the saved z vectors are bitwise equal (sha256 dfe5cd9338639655...);
  the chosen pivot is the same (S, q 5, amplitude 0.12545). So the default rank-1 path is byte-identical to the previous worker on its outputs.
- C (pivot_rank 2): logged 'PIVOT RANK 2: pivot (T, q 5, amplitude 0.0936, rank 2, margin 1.230)'; cost at iteration 0 2.098e-5 (the LM's initial projection rotated the start to the rank-2
  pivot against the stale closure target, weight 0.1 in this job: the FA 54 mechanism, which is why S3-5 requires a PRE-ALIGNED rank-2 start) then 1.19e-6, 9.26e-7, 8.10e-7, 7.32e-7, 7.09e-7.
- Files and shas: A.log 951e319a1f0038de1b81c380c2609afd993dbfe41cb5e0f3ad2bc8e506118bbd; B.log 876a6c6178776b5ce0391e0a596c3e165c000ac965e940484dde6d54a670cce7; C.log 1173680c948d28dc8fcd57c8530aa75bba377c947f38989dfe84d051d25db385; COMPARISON.json e7b01a8b0a4edfb329aec9aaa45530cd3288429218eaa49f7aa0221e93b51b5d.
- Frozen shas of the production files at 2026-10-26T19:11Z: src/optimization/problem.py ca146af805bdaafe6d3f73e1a16885afd1e56cd9bffcf2450de1a302c8fa919c; scripts/worker.py 3bed13b5c6638ac16f65bf67d80469eb7a2bd50db1a38f738538477b45868c79 (the pivot_rank edit only; the S3-22 start record is in the candidate tree, smoke running).

- Lead IR (1) (19:18:58Z): S3-25 (d) MET for the default path on this smoke (A and B LM/pivot/status lines identical apart from timings; verifier PR4, PR5 confirmed). C is not a pre-aligned rank-2 replay, so S3-25 (b) (the R2d start) stays open. Lead IR (2): the S3-22 candidate 57c2386a is NOT ACCEPTED; re-submission by 2026-10-27T12:00Z with SL1 (isolation by a second Problem or deepcopy plus finally; a probe exception ends the job as a tooling failure before the first trial), SL2 (two named costs: cost_refreshed_closure_only = the block_costs --phase_align quantity for the 1e-6 equality, and cost_refreshed_closure_and_nl_weights), SL3 (a bitwise frozen-residual guard at project(z) that STOPS the job on failure), SL4 (the job-file byte sha plus full 64-hex shas of lm/worker/problem/block_costs), SL5 (json allow_nan=False, exclusive create, a new file on resume, the row set stated), SL6 (the A'/B', D and forced-exception smokes). The running A'/B'/D smoke stays as evidence of off-flag equality.

## T1 v2 (2026-10-26T19:27Z): scripts/cap_watcher_v2.py, re-registration for S3-14 after lead IP (W1 to W10) and the W3/W4 amendment (V = 45 s)
- v1 (sha e4e3a5aa..., section T1 above) is WITHDRAWN (lead IP). Frozen sha256 of scripts/cap_watcher_v2.py: baf27bc46de5031741019216dd4114d9995a4c865f97ff8713dec54cd2004e13
- Command line: cd . && setsid nohup .venv/bin/python scripts/cap_watcher_v2.py --job <JOB_ID> --cap_seconds <CAP> --abs_end <YYYY-MM-DDThh:mm:ssZ> --poll 30 --grace 120 > runs/_logs/capwatch_<JOB_ID>.log 2>&1 &
  (record status/cap_watcher_<JOB_ID>.json; heartbeat status/heartbeat_<JOB_ID>.json; queue dir queue/; the supervisor log status/supervisor.log for the launch line).
- W1 identity: at binding the PID (from the job's heartbeat), its start ticks (/proc/PID/stat field 22) and its full argv are recorded; binding requires an argv ELEMENT equal to the job id or
  to <JOB_ID>.json (no substring test); before every signal the same pid, the same start ticks and exact argv equality are required; no new PID is ever taken after binding.
- W2 start clock: whole-job start = btime (/proc/stat) + start_ticks / CLK_TCK (the process start, covering imports and build); elapsed after binding from a monotonic clock anchored at the
  bind wall time; abs_end is the second guard; the supervisor-log launch line is recorded when found. W3 (amended): D_TERM = min(start + cap, abs_end) - (grace + poll + V + 10 s) with V = 45 s
  (30 s /proc check + Q = 15 s nvidia-smi hard timeout); KILL at D_TERM + grace; the binding loop stops at abs_end; binding after D_TERM or missing it by more than one poll writes
  'cap incomplete: TERM deadline missed' into the record (the job's reading then carries the qualifier). W4: after KILL, /proc gone or Z with the bound ticks within 30 s, then ONE nvidia-smi
  --query-compute-apps call (15 s timeout; a timeout records 'GPU release unverified', no retry); both recorded with the measured verification time; otherwise 'termination UNVERIFIED'.
  W5: a vanished queue/running entry while the bound process lives is recorded and monitoring continues. W6: cap/poll/grace must be finite and positive and abs_end in the future;
  ProcessLookupError and PermissionError caught on every signal; main loop in try/finally with a failure record; a failed record write goes to stderr and the loop continues. W7: the job's
  queue JSON must have max_retries 0 (recorded) or the watcher refuses to bind. W8 choice (b): the worker is unchanged; the heartbeat phase at TERM and at KILL is recorded; a stop in the
  battery is recorded 'battery incomplete; state not read'.
- W9 smokes (runs/stage3_smoke/capwatch_v2b/; harness run_smokes.sh sha a361b586eaa118e225b1740c3f8aba3364707003002f177d67e7de460130ab2b; log run_smokes_20261026T1921Z.log sha 5b17a3034cad368b437451108ddac26458d6236b9bdc4fc4979850f8c382c109; SUMMARY.json sha cb0c75bcb038205bc1533ba8e5736d7de5616a118e09c4107d144ee7aaf639b0; disposable
  Python fake workers whose argv carries the job JSON path; --no_nvidia; poll 2 s, grace 5 s; every record states the action wall time against the cap and abs_end and the verification time):
  | case | result |
  |---|---|
  | 1 late binding (process started 25 s before the watcher; cap 110 s) | bound with elapsed 26.2 s at bind (start from btime + ticks), TERM at D_TERM 19:22:11Z, verified at 19:22:12Z, occupied 49.4 s, within cap and end; verification 1.5e-5 s |
  | 2 stale PID (heartbeat names a live process whose argv does not name the job) | not bound, no action (exit 1) |
  | 3 job-substring collision (watch cwv2_c3, the PID runs cwv2_c3x) | not bound (exact-element rule), no action (exit 1) |
  | 4 disappearance between checks (killed externally 8 s after binding) | 'job process ended on its own (process gone); no action' |
  | 5 process ignores TERM (cap 90 s) | TERM at D_TERM, KILL after the 5 s grace, termination verified (verification 1.0 s), occupied 35.6 s, within cap and end |
  | 6 queue entry removed 20 s after binding (cap 95 s) | 'running entry vanished: NOT completion; monitoring continues', TERM at D_TERM, verified, occupied 34.6 s, within cap and end |
  | 7 abs_end 20 s ahead, no heartbeat ever | 'not bound before abs_end; no action' (exit 1) |
  | 8 heartbeat phase battery (cap 90 s) | TERM at D_TERM with phase_at_TERM battery, record 'battery incomplete; state not read', verified, occupied 30.6 s, within cap and end |
  All eight actions ended before the published cap and end (within_cap and within_abs_end true wherever an action was taken). GPU-release verification is exercised only with --no_nvidia
  here (no GPU process in a CPU smoke); the first production use records the real nvidia-smi result.
- W10: submitted to the lead with this section; nothing runs under it before the lead's dated review.

### T2 result 2 (2026-10-26T19:36Z): candidate v1 smoke A'/B'/D COMPLETE (runs/stage3_smoke/cwsmoke_20261026T1910Z/; 6 LM iterations, lm_only, torch intra-op threads 2, OMP_NUM_THREADS=4; status max_iter at 6)
- A' (production worker 3bed13b5, defaults), B' (candidate v1 worker 57c2386a..., start_record absent) and D (candidate v1, start_record true): ALL THREE BITWISE EQUAL on every iteration
  (histories: cost, damping, acceptance, iterate hash) and in the saved z (sha256 dfe5cd9338639655... for all three). So the v1 record block, on or off, left the LM trajectory identical;
  the lead's rejection of v1 (IR (2), SL1-SL6) concerns isolation, guards and the record's content, not the trajectory.
- D's start_record_000.json (sha 77319e7ba476fc45034d6c6213b45169d9c799036b76e060a51994cb6c1f5708): pivot chosen (S, q 5, amplitude 0.12545) against the start's saved pivot (T, q 2, amplitude 0.6143) = a pivot change for this smoke start;
  ||project(z) - z||/||z|| 0.8658; frozen cost at z 3.98603174643857e-4 = at project(z) (rotation invariance) = refreshed (closure refreshed only) 3.98603174643857e-4 (the smoke start carries
  no B/D/E coefficients, so the closure rows are rotation invariant here); meta cost0 (unrounded) 3.98603174643857e-4; frozen residual restored bitwise true; 205417 residual rows.
- Files and shas: Ap.log 42e5f818d728ef3b0ab75422fb3cbf7344491903f0c48b7539826fc5b83564c0; Bp.log 83d8669f21fd953c47c04c865533de7de124c5b028758632fbef94c29334dbdf; D.log b40da91eed1bb9b4f86e761df4e5e5401400b5681e40061cf513478591c94037; COMPARISON.json 7db732313795f2b465d443375b95d3c62f8d88151982cf0200212dc01e80ac68.
- Candidate v1 frozen sha (superseded): 57c2386aeee8f651932f1f3d85e55d5d1e6f5f3f06ee8a4ed07dacc0412df86d. Candidate v2 (SL1-SL6; runs/stage3_smoke/worker_candidate_tree/scripts/worker.py): d8f35862cce7647ff400a16c31151f06f08a823a2bb09384f1a1358c9f756274; its smoke
  A''/B''/D2/E (production vs v2 off vs v2 on vs forced probe exception E3_SR_TEST_FORCE_FAIL) is running (runs/stage3_smoke/cwsmoke2_20261026T1934Z/); results appended when complete.

## T1 v3 (2026-10-26T19:58Z): scripts/cap_watcher_v3.py, re-registration for S3-14 after lead IU (C1 to C8) and IV (C9); v1 and v2 are withdrawn and kept as history
- Frozen sha256 of scripts/cap_watcher_v3.py: 2cddfebe9cbed281061ded60464e14a4ee04a1821cb3d485c5aa0a9a9448f9c8
- Command line (one watcher per Stage III job, started detached after the job's launch; CPU only): cd . && setsid nohup
  .venv/bin/python scripts/cap_watcher_v3.py --job <JOB_ID> --cap_seconds <CAP> --abs_end <YYYY-MM-DDThh:mm:ssZ> --poll 30 --grace 120 > runs/_logs/capwatch_<JOB_ID>.log 2>&1 &
  Binds: the heartbeat status/heartbeat_<JOB_ID>.json (pid), the exact supervisor launch argv [ROOT/.venv/bin/python, ROOT/scripts/worker.py, ROOT/queue/running/<JOB_ID>.json, ROOT/runs/<JOB_ID>]
  (C6; no basename or job-id rule), the start ticks (/proc/PID/stat field 22), the queue JSON's max_retries (must be the int 0, W7/C5), the supervisor log ROOT/logs/supervisor.log line
  'launched <JOB_ID> on GPU <g> pid <P>' matched token by token (C9; an unreadable log is recorded; a pid mismatch refuses the binding); record status/cap_watcher_<JOB_ID>.json.
- Clocks and deadlines (W2, W3 amended, C1, C2): process start = btime + ticks/CLK_TCK; D_TERM = min(start + cap, abs_end) - (grace + poll + V + 10 s), V = 45 s (30 s /proc check + 15 s
  nvidia-smi hard timeout); monotonic cutoffs M_TERM, M_KILL = M_TERM + grace, M_END = M_KILL + V fixed at binding; a wall-clock guard on both deadlines; both clocks recorded at TERM, KILL and
  final; KILL at M_KILL (if the TERM went out later than M_KILL - 5 s: KILL at TERM + 5 s with 'grace shortened' and 'cap incomplete'); every wait and the nvidia-smi timeout bounded by the time
  left to M_END (floor 5 s, below it 'GPU release unverified (no time left)'); binding after D_TERM or a TERM late by more than one poll writes 'cap incomplete: ...' (the job's reading carries
  the qualifier); the binding loop stops at abs_end and the binding timeout.
- Identity (W1, C4, C5): one /proc read per decision; 'ended' only when /proc/PID is absent, the ticks differ (pid reused) or the state is Z with the bound ticks; same ticks, alive, argv
  unreadable or different = final status 'ownership unverified; process alive; cap NOT enforced; manual action under S3-14 (b)'; every ending branch runs the GPU query and records it; the whole
  body after argument parsing is in one try/finally with a failure record; inputs validated (cap, poll, grace, bind_timeout finite and positive; abs_end in the future); --no_nvidia only with
  --pid (smoke mode).
- Termination proof (W4, C3): /proc gone or Z with the bound ticks within 30 s, then one nvidia-smi --query-compute-apps=pid call (15 s timeout) that counts as 'clear' only with returncode 0,
  every non-empty line an integer and none equal to the pid; otherwise None = 'GPU release unverified (...)'; 'termination verified' requires both; in smoke mode the status is never
  'termination verified' ('GPU release not queried (smoke mode)'). W5: a vanished queue/running entry is recorded, monitoring continues. W8 (b), C8: the heartbeat phase at TERM and KILL is
  recorded; phase 'lm' -> 'stopped in the LM phase'; a battery phase -> 'battery incomplete; state not read'; phase None -> 'phase unknown at TERM; state not read unless the saved LM endpoint
  is verified by sha'.
- Tests (C7): --selftest fixture suite (15 checks: /proc stat parsing incl. comm with spaces, zombie, short read; nvidia parsing incl. nonzero exit with empty output and unparsable output;
  the deadline arithmetic incl. abs_end binding; proc_stat gone; classify alive / ticks differ / argv differs) PASS; the driver runs/stage3_smoke/capwatch_v3/run_smokes.py (sha 97c1707663bdb7dfe251623256c791d70234d411deb0a420268fdff804314c93) runs
  disposable Python fake workers whose argv has the supervisor's shape (--argv_override gives the exact expected argv; --no_nvidia; expected statuses pre-registered; PASS/FAIL table and
  SUMMARY.json with the watcher sha): cases 1-8 of W9 plus c9 TERM late by more than one poll (the watcher SIGSTOPped 6 s around D_TERM), c10 binding after D_TERM, c11 production parameters
  (poll 30 s, grace 120 s, TERM-ignoring fake, cap 245 s), c12 ownership-unverified (fixture). Run 1 (pre-C9 build after the bind-rule tightening; archived runs/stage3_smoke/capwatch_v3_run1_preC9/,
  SUMMARY sha 068836d468578d300b7f80efc8c5ce00b0951ca31e04487be4178da7e676794d, log sha 2cecafac942c461dce059a7c47536a7746827382b7517c23e4a795010e549316): ALL 12 PASS. Run 2 (the frozen C9 build above): appended below.
- Not exercised by the CPU smokes: a real GPU process (the nvidia-smi 'clear' path with returncode 0 is covered by the fixture test only; the lead's positive control shows the query lists the
  live worker PIDs); the first production use records the real nvidia-smi result. Caps stay manual under S3-14 (b) until the lead's dated review (W10).
- T1 v3 RUN 2 (2026-10-26T20:01Z; the frozen C9 build 2cddfebe9cbed281..., recorded in SUMMARY.json watcher_sha256): ALL 12 PASS (runs/stage3_smoke/capwatch_v3/; SUMMARY.json sha 584b9781a3875ac49ab912e39212440b4e9dc439fbc5e94c65e54429516293a8; log
  run_smokes_20261026T1952Z.log sha a96c0d630ace8a4f49d943e11816de6175c8dbbe483e454d7b0f118473c7476e); every action within the cap and abs_end; c11 (production parameters) KILL within the 245 s cap; c9 and c10 carry 'cap incomplete' as designed.
  In smoke mode the supervisor-log launch line is 'not found (smoke mode)' and the GPU is 'not queried (smoke mode)'. Submitted to the lead (W10).

### T2 result 3 (2026-10-26T20:02Z): S3-22 start_record v2 (SL1 to SL6) SUBMISSION. Candidate runs/stage3_smoke/worker_candidate_tree/scripts/worker.py, frozen sha256 d8f35862cce7647ff400a16c31151f06f08a823a2bb09384f1a1358c9f756274; diff against the
production scripts/worker.py (3bed13b5c663): reports/stage3_tooling/worker_s3_22_v2.diff (sha 4978b4c2d2fe71422fce6b38b08fee882fa577ffa7b43650f51caec281368a59; the only change is the start_record block before the LM call, off by default).
- SL1 isolation: the refreshed probe runs on a SECOND Problem instance built from the same config (same pivot, nl weights and closure target at z); the production prob is never mutated; a
  probe exception ends the job as a tooling failure before the first LM trial (SystemExit 3, failure record written); the second instance is deleted in a finally block.
- SL2 two named costs: cost_refreshed_closure_only (= the block_costs --phase_align quantity for the 1e-6 equality) and cost_refreshed_closure_and_nl_weights; also cost_frozen_at_z,
  cost_frozen_at_projected and probe_frozen_cost_second_instance with probe_instance_consistent (relative 1e-12).
- SL3 guard: the frozen residual at project(z) is evaluated twice and must be bitwise identical (frozen_residual_guard_bitwise), and the production residual at z must be bitwise unchanged
  after the probe (production_residual_unchanged_bitwise); a failed guard ends the job as a tooling failure.
- SL4 shas: job-file byte sha, config-JSON sha, start-file sha, source-of-start sha, and full 64-hex shas of lm.py, worker.py (the running file), problem.py and block_costs.py, plus CODE VERSIONS.
- SL5: json allow_nan=False; exclusive create (open 'x'); a resumed run writes start_record_<idx>_resume_it<k>.json; row_set stated (PDE rows + closure rows + gauge rows in the worker's order,
  n_residual_rows recorded).
- SL6 smokes (runs/stage3_smoke/cwsmoke2_20261026T1934Z/; the L4 Nk12 lm_only job, 6 iterations, torch intra-op threads 2, OMP_NUM_THREADS=3 under box load average above 300):
  A2 (production worker, defaults) vs B2 (candidate, flag absent) vs D2 (candidate, flag on): histories BITWISE EQUAL on all 6 iterations (cost, damping, acceptance, iterate hash) and the saved z
  bitwise equal for all three (sha 7593d076fc015d9c...; this differs from the A'/B'/D set's dfe5cd93... because that set ran with OMP_NUM_THREADS=4 and this one with 3, so the BLAS reductions
  differ in the last bits between sets while each set is internally bitwise identical: comparisons are valid only within one thread setting); the end statuses differ only by the wall-clock time limit (A2, B2 'time_limit' at 1522 / 1526 s against the 1500 s limit checked after
  each iteration; D2 'max_iter' at 1525 s): a timing artefact of the loaded box, not a code difference. D2's record (sha 179e1c60bca6d158b05d4ec4e1d222a42829b2d118479c609f8bbb4508e80163): pivot (S, q 5, amplitude 0.12545) against the saved
  (T, q 2, 0.6143) (a pivot change for this smoke start; ||project(z) - z||/||z|| 0.8658), frozen cost at z = at project(z) = refreshed (closure only) = refreshed (closure + nl weights) =
  3.98603174643857e-4 (this start has no B/D/E coefficients, so the closure rows are rotation invariant here), probe_instance_consistent true, both guards true, 205417 rows, full shas.
  E (E3_SR_TEST_FORCE_FAIL=1): 'TOOLING FAILURE before the first LM trial', exit 3, failure record (sha f16e59b65a3536907e22ab659779f2009df3cba8626e311646a31f15c00960e4), no LM trial made.
  Logs: A2 13ffa255f540105049751506ddd1924a412343d7d6e178fe631b2d779de69a3d; B2 8f087b8452b46df0a0e21e603a77dd38e6340d4ad3b727da126390a30224e015; D2 63e109f23cd5684410a54e64e9c4e993c5ae4ae5ab21573fca29ff23a85b638a; E daf2bcd83c1cf0c24e6e135e4a7b59b538153edd2be12c753ba65a4582649737; COMPARISON.json 5e1a444951878cc5c2c7250c00e620e32c4aa8e4763f93f8e4cefc78257e9435.
- Equality with block_costs.py --phase_align (S3-22): to be shown on a real Stage III start at enqueue time (the record's cost_frozen_at_projected / cost_refreshed_closure_only against the
  pre-launch record, relative 1e-6); on the smoke start both tools give the same frozen total by construction (same Problem code path).
- Deployment rule (S3-25 (e)): after the lead's dated review, the candidate replaces scripts/worker.py only with the queue held (no pending or running job), with the sha recorded in WORKLOG and the
  first production job's CODE VERSIONS line cited; the Stage III job drafts carry start_record true.

## T1 v4 (2026-10-26T20:19Z): scripts/cap_watcher_v4.py, re-registration for S3-14 after lead IY (C10 to C15, CW3-7); v3 (2cddfebe) withdrawn and kept as history
- Frozen sha256: c5b46cb2a712f71fc5ff5d1ec389080729058fd013c00fd2d6b4052a147a0731; diff against v3 2cddfebe: reports/stage3_tooling/cap_watcher_v3_to_v4.diff (sha 3ca094bf203c3f1b4a1736b502aca581520cc347d385f3c9cb90c3abf3c66e8d); the changes are limited to C10 to C15 and the header.
- C10: kill_decision(): SIGTERM and SIGKILL only on a fresh 'alive_ok' classification immediately before the signal; 'unreadable' is retried within the remaining allowance (TERM up to
  M_KILL - 5 s; KILL up to M_END - V) and never signalled; if the identity is still not 'alive_ok' at the deadline nothing is sent and the final status is 'ownership unverified; cap NOT
  enforced; manual action under S3-14 (b)'. C11: launch_bind_check(): in production an unreadable supervisor log, a missing launch line, an unparsable launch pid or a pid mismatch REFUSES the
  binding (smoke mode, --pid, records 'launch line not found (smoke mode)'). C12: nv_timeout(): the nvidia-smi timeout is min(Q_NV, M_END - now) with no floor at both call sites; nothing left
  = 'GPU release unverified (no time left)' and no query. C13: sleep_allowance(): no sleep longer than the remaining allowance anywhere (no floors); the grace and verification loops test the
  monotonic cutoffs AND the wall clock (abs_end) in every iteration. C14: the heartbeat is re-read at KILL (phase_at_KILL) and battery_note() uses both phases (a battery phase at either ->
  'battery incomplete; state not read'; None at either -> 'phase unknown; state not read unless the saved LM endpoint is verified by sha'). C15: --argv_override only with --pid (smoke mode).
  Header (CW3-7) corrected: validation and the expected argv precede the try (failures call finish()); the body from the binding loop on is in one try/finally.
- Selftest fixtures (34 checks PASS): one per repaired branch (kill_decision x4, launch_bind_check x6, nv_timeout x2, sleep_allowance, battery_note x4, argv_override_allowed) plus the v3
  fixtures (stat parsing with other ticks / Z / short read, nvidia parsing with nonzero exit and unparsable output, deadlines, classify).
- Smoke run on the new sha (runs/stage3_smoke/capwatch_v4/; driver run_smokes.py sha caba950c429a0cce042528c9a46c25c1484314351f2dccdaa0edd494273023e9 = the v3 driver pointed at v4; SUMMARY.json sha 4adb88bda3dd34f4dacfe290002060a3912642efa123a01f0c3512eb4d975c9c with
  watcher_sha256 inside; log run_smokes_20261026T2010Z.log sha 685cca70691c06914492ab901e5a0a3579027f7a19e8c743e82e646bec326051): ALL 12 PASS (the same cases as T1 v3: late binding, stale PID, substring collision refused, disappearance, TERM ignored, vanished
  queue entry, abs_end before any bind, battery phase, TERM late by more than one poll, binding after D_TERM, production parameters, ownership-unverified by fixture); every action within the
  cap and abs_end. Not exercised: a real GPU process (the nvidia 'clear' path with returncode 0 is a fixture); the first production use records the real nvidia-smi result. Caps stay manual
  under S3-14 (b) until the lead's dated review and the verifier's audit (W10).

### T2 result 4 (2026-10-26T20:29Z): S3-22 start_record v2.2 (lead IZ SR1-SR3, JB SR5-SR10, K4). Candidate runs/stage3_smoke/worker_candidate_tree/scripts/worker.py, frozen sha256 6f64fdbb06b12fa1a4521fb221fd064583dc8f0562476e56d51dd4c3e9483aad
(v2 d8f35862 and v2.1 97a2544e kept as history: worker.py.v2_d8f35862, worker.py.v2_1_97a2544e, worker.py.v2_2_3ca5b2c8 = v2.2 before the SR8-fields edit); diff against the production
worker 3bed13b5: reports/stage3_tooling/worker_s3_22_v2_2.diff (sha 8855c2b8fefcaa3c1710b27eb5a5749a355b9916924a2e24709135f7ec500b88; the flagged block before the LM call and nothing else; off by default).
- SR1 (completed, SR9 boundary): the probe is a function _probe() returning scalars, bools and strings only; the second Model and Problem (model2, prob2) are built inside it and deleted in its
  finally block; every probe tensor (r_ref, r_fro, z_proj, r2, r_after) is local or deleted before return; then gc.collect(), torch.cuda.synchronize(), torch.cuda.empty_cache(); the memory
  readings (allocated before the probe, max_memory_allocated during it with the peak reset just before the probe, allocated after the release, back_to_pre_probe) are taken at the stated boundary
  'after release of all probe objects and tensors, before the LM'.
- SR2: prob2 receives nonaxi_r_tail and the resolved core_pin / nonaxi_pin from prob (recorded under pins_copied); probe_instance_consistent (relative 1e-12 cost agreement) is a stopping guard.
- SR5: the frozen residual at project(z) is cloned before the probe (r_fro); after all second-instance work prob.residual_vector(z_proj) is compared bitwise (frozen_residual_at_projected_unchanged_bitwise)
  and the at-z check is kept under its own name (production_residual_at_z_unchanged_bitwise); the pre-probe pair is frozen_residual_reproducible_pre_probe_bitwise. Any false guard -> exit 3.
- SR6: the sha field is code_sha256_on_disk_after_import (lm, worker = the running file, problem, block_costs with the note 'on disk, not imported by the worker'); CODE VERSIONS kept beside it.
- SR7: refusal (exit 3, reason and values in the failure record) when use_scalar is true, balance_lambda > 0 or scalar rows are present; use_scalar, balance_lambda and sigmaZ recorded.
- SR8: E3_SR_TEST_FORCE_FAIL_AFTER_REFRESH raises after both refreshes and before the record write; the failure JSON carries production_residual_at_z_unchanged_bitwise and
  frozen_residual_at_projected_unchanged_bitwise as fields (plus the hook name). The early hook E3_SR_TEST_FORCE_FAIL stays.
- SR10 / SL5: the record is written once, after the release, with exclusive create ('x') and allow_nan=False; a resumed run writes start_record_<idx>_resume_it<k>.json; no rewrite anywhere.
- K4: probe_instance_bitwise (torch.equal of prob2's frozen residual at project(z) against the r_fro clone) recorded.
- Record fields also include: job_file_sha256, config_json_sha256, start_sha256, source_sha256, pivot_chosen / pivot_rank / pivot_saved_in_start, rel_change_projection, the four costs,
  guards, n_residual_rows, row_set, threads (torch intra-op threads and OMP_NUM_THREADS), scalar_rows, cuda_memory.
- Hook smokes on this design (runs/stage3_smoke/cwsmoke3_20261026T2019Z/): E (early hook; sha 3ca5b2c8 build): exit 3 before any LM trial, failure record sha d2d06f1a5e3046fbd4b04b575fd8705020031269c938afc23a3dcd5a8837b588 (log ea852152186445ea905925f041cf17467a9f7432990cd1892fb50c3eaade84f2);
  E2b (after-refresh hook; the final sha above): exit 3 before any LM trial, failure record sha ebdc9b36095f166b0630765ba594e852f28516686d413f613d4a161e9bde27b5 (log 22ba2489880958f1e3b18617c21e4ec9348275d8bef752fd692ed75bea2ebc5a) with production_residual_at_z_unchanged_bitwise true and
  frozen_residual_at_projected_unchanged_bitwise true. D3 (flag on, sha 3ca5b2c8 build, CPU): all four guards true, probe_instance_bitwise true, the two refreshed costs recorded, threads recorded.
- RELEASE SMOKES still owed on the final sha (lead JB (4)), due 2026-10-27T10:00Z: A''/B'' bitwise (A3/B3 running on 3ca5b2c8: valid for the shared code; a D'' on the final sha), SR3 on the GPU
  (s3r4 L10 Nk24 configuration, jtj_blocks 2, lm_only, max_iter 1: all guards true on CUDA, memory before / peak / after with back_to_pre_probe true, the record written once; the record states
  OMP_NUM_THREADS=2 of run_sr3.sh and the job's threads 1), then the verifier's audit and the lead's review. Fallback: the production worker with the S3-22 (d) qualifier.

## T1 v4.1 (2026-10-26T20:33Z): scripts/cap_watcher_v4_1.py, re-registration for S3-14 after lead JE (C16 to C22); v4 c5b46cb2 withdrawn and kept as history
- Frozen sha256: 83a5d4208edce057020f5107ee1b52c99d9b27336459902d03be55b4c4262522; diff against v4 c5b46cb2: reports/stage3_tooling/cap_watcher_v4_to_v4_1.diff (sha 483eed9b0e541408829b412139cd7d09bb306e2b39e5a9945663e1eaadd3f24e); the changes are limited to C16 to C22.
- C16: the binding sleep is sleep_allowance(min(poll, 5 s), min(abs_end - now, t_b0 + bind_timeout - now)) (unfloored, bounded by abs_end and the bind_timeout remainder).
- C17: one pure helper allowance(mono_deadline, wall_deadline, mono_now, wall_now) = the smaller of the monotonic and the wall-clock remainder (never negative), used at every wait and timeout:
  main-loop sleep (M_TERM / min(d_term, abs_end)), TERM retry (M_KILL - 5 / d_kill - 5), grace loop condition and sleep (kill_at / min(kill_at_wall, abs_end); a shortened grace fixes
  kill_at_wall = wall + 5 at the TERM), verification loop (M_END - Q / d_end - Q) and both nvidia-smi timeouts (M_END / d_end); the wall deadlines d_term, d_kill, d_end are fixed at binding.
  Fixtures: forward wall jump (the wall remainder binds), backward wall jump (the monotonic remainder binds), both zero or negative -> 0.
- C18: one validated heartbeat reader read_heartbeat_phase() (parse_heartbeat()) returns the phase only when the heartbeat's job_id equals the job and its pid equals the bound pid; otherwise
  None with the reason (unreadable / job mismatch / pid mismatch) recorded beside the phase (last_phase_reason, phase_at_TERM_reason, phase_at_KILL_reason); used for last_phase, TERM and KILL.
  Fixtures: matching, job mismatch, pid mismatch, unreadable.
- C19: battery_note precedence: a known phase other than 'lm' at either observation -> 'battery incomplete; state not read'; otherwise an unknown phase -> 'phase unknown; ...'; only 'lm' at
  both -> 'stopped in the LM phase'; both raw phases recorded (phases field). Fixtures: (None, diagnostics, killed), (diagnostics, None, killed), (None, None, killed), (lm, None, killed) ->
  unknown, (lm, None, not killed) -> LM.
- C20: at KILL the phase and the clocks are read first, then ONE fresh classification, then os.kill at once on alive_ok (only the decision lookup in between; logging after the signal); the TERM
  order is unchanged (logging after the signal).
- C21: version 'cap_watcher_v4.1' and watcher_sha256 (the sha of the watcher's own source read at start) in every record.
- C22: header and this registration state that KILL has NO retry allowance: 'unreadable' or 'ownership_unverified' at KILL ends as 'ownership unverified; cap NOT enforced; manual action under
  S3-14 (b)' with no signal (the TERM retry allowance up to M_KILL - 5 s stays); the selftest count is given as named checks: 45 named checks PASS (selftest log selftest_20261026T2033Z.log, sha 47a1981d68c799b92a78c5c69149f7c82b28079e19b78df0bdce4e315531c1f5).
- Smoke run of the 12 cases on the new sha: runs/stage3_smoke/capwatch_v4_1/ (driver = the v4 driver pointed at v4.1); RESULT appended below when complete. The verifier's static audit of the
  new source is requested with the lead's review. Caps stay manual under S3-14 (b) until the lead's dated review.
- T1 v4.1 SMOKE RUN (2026-10-26T20:40Z; the frozen sha 83a5d4208edce057... recorded in SUMMARY.json watcher_sha256): ALL 12 PASS (runs/stage3_smoke/capwatch_v4_1/; SUMMARY.json sha 48a801b4f090464587e532b9da89dff35fe41cca50f5fbaa58d44da0318a7f83; log run_smokes_20261026T2032Z.log sha cf28c1e8d09d6b6a8c14e2ac60ac6dd502e69359bb26703c3f4a55c504ccf37f); every action within the cap and abs_end; in smoke mode 'GPU release not queried (smoke mode)' and 'launch line not found (smoke mode)'. Submitted to the lead (JE evidence list: sha, diff vs c5b46cb2, selftest 45 named checks, the 12 cases on the new sha); the verifier's static audit is requested.

### T2 result 5 (2026-10-26T20:43Z): S3-22 start_record v2.3 (lead JG: SR11, SR12) and v2.4 (lead message of 20:4xZ: SR13), each in a NEW tree
- v2.3: runs/stage3_smoke/worker_candidate_tree_v2_3/scripts/worker.py, sha db04eaeb9b6f63e1ddb4bdfbc8e44aae8849f046d0f06899555f12c728538375 (diff from v2.2 6f64fdbb: reports/stage3_tooling/worker_s3_22_v2_2_to_v2_3.diff): SR11 attempt-numbered record names
  (base.json, else base_attempt<n>.json with the first free n >= 2, exclusive create; attempt, supervisor_retries = job.get('retries') and earlier_records with shas recorded; a FileExistsError at the
  write is routed to the tooling failure); SR12 failure records only under base.failure.json / base_attempt<n>.failure.json. Its F2 smoke (early hook, max_iter 1; runs/stage3_smoke/cwsmoke4_20261026T2041Z/F2/):
  exit 3 before any LM trial and ONLY start_record_000.failure.json written (sha 5b942b552745e1f66135beff4da973bc221f708ea2d3c46cecf4d875b5c446f5); F1 (base.json pre-created) and F3 (base.json and _attempt2 pre-created) running. SUPERSEDED by v2.4 (the
  attempt loop advanced only on the success name).
- v2.4: runs/stage3_smoke/worker_candidate_tree_v2_4/scripts/worker.py, frozen sha 2edbd00ccd2bc2b5110297f270211850838b63414a73b24bad72fcb67e6b6b63 (diff from v2.3: reports/stage3_tooling/worker_s3_22_v2_3_to_v2_4.diff sha f277d5931d56ee85c716f22e0ef977ab6588baffce282a7e0829dbb5eb9c9b0f; full diff against the
  production worker 3bed13b5: reports/stage3_tooling/worker_s3_22_v2_4.diff sha 5f243f3e3465715fa6a1d76b9c73149af399a4eece4310ff2984215f6f8ff516): SR13 the attempt counter advances while EITHER the n-th success name or the n-th failure name exists
  (n = 1: base.json / base.failure.json; n >= 2: base_attempt<n>.json / base_attempt<n>.failure.json), and earlier_records lists both kinds with name, sha256 and kind ('record' / 'failure').
- RELEASE SET owed on the v2.4 sha (lead): A''/B''/D'' bitwise (the L4 lm_only job, 6 iterations, one thread setting), SR3 on the GPU (s3r4 L10 Nk24 configuration, jtj_blocks 2, lm_only, max_iter 1;
  job runs/stage3_smoke/sr3/job_sr3smoke.json, runner run_sr3.sh <gpu> pointed at the v2.4 tree; on the next naturally free GPU), and F1 to F5 (F1 base.json pre-created -> record to _attempt2 and the
  LM runs; F2 early hook -> only base.failure.json; F3 base.json and _attempt2 pre-created -> _attempt3; F4 base.failure.json pre-created, flag-on job -> record to base_attempt2.json, earlier_records lists
  base.failure.json with its sha, the LM runs; F5 base.failure.json pre-created, early hook -> failure to base_attempt2.failure.json, base.failure.json unchanged (sha before and after)). Due 2026-10-27T10:00Z;
  fallback = the production worker with the S3-22 (d) qualifier. The A3/B3/D3 set on 3ca5b2c8 is off-flag equality evidence only.

### T2 result 6 (2026-10-26T21:14Z): v2.4 release set, part 1: F1 to F5 on the frozen sha 2edbd00ccd2bc2b5... (runs/stage3_smoke/cwsmoke6_20261026T2050Z/; SUMMARY_F1_F5.json sha 3d425e902cc35ffe15b2563c1d38ec0f5311b32635116dd132594a436ca1beca; the L4 lm_only job, max_iter 1, OMP_NUM_THREADS=3, torch intra-op threads 2; pre-created names and their shas in precreated_shas_before.json)
- F1 (base.json pre-created): the record went to start_record_000_attempt2.json (attempt 2, earlier_records = [base.json, kind record]), all guards true, the LM ran (exit 0). PASS.
- F2 (early hook): ONLY start_record_000.failure.json written, exit 3, no LM trial. PASS.
- F3 (base.json and _attempt2 pre-created): the record went to start_record_000_attempt3.json (attempt 3), the LM ran (exit 0). PASS.
- F4 (base.failure.json pre-created, flag on): the record went to start_record_000_attempt2.json (attempt 2), earlier_records lists start_record_000.failure.json with kind 'failure' and its sha, all four guards
  true, the LM ran (exit 0), base.failure.json byte-identical before and after. PASS.
- F5 (base.failure.json pre-created, early hook): the failure went to start_record_000_attempt2.failure.json (attempt 2, earlier_records lists base.failure.json), base.failure.json byte-identical before and
  after (sha equal), exit 3, no LM trial. PASS.
- Part 2 (A4/B4/D4 bitwise on the same sha; runs/stage3_smoke/cwsmoke5_20261026T2047Z/) and part 3 (SR3 on the GPU) follow; the next shift records them in RUN_STATUS for the next lead shift.
- T2 result 6 PART 2 (2026-10-26T21:17Z): A4 (production worker 3bed13b5, defaults) vs B4 (candidate v2.4 2edbd00c, start_record absent) vs D4 (candidate v2.4, start_record true), the L4 lm_only job, 6 LM iterations,
  OMP_NUM_THREADS=3 / torch intra-op threads 2 (runs/stage3_smoke/cwsmoke5_20261026T2047Z/; COMPARISON.json sha 17206eaf421cdd29eefa4825e63ad6039d09d0b5b5ca37fc96d4fce76f361de3 with the log shas and D4's record fields): histories BITWISE EQUAL on all 6
  iterations (cost, damping, acceptance, iterate hash) and saved z bitwise equal across the three (same sha); D4's record start_record_000.json (attempt 1): all four guards true, probe_instance_bitwise true,
  the two named refreshed costs, scalar_rows recorded (use_scalar false, balance_lambda 0, sigmaZ null), threads recorded, cuda_memory null on the CPU, code_sha256_on_disk_after_import with the worker sha
  2edbd00c. Part 3 owed: SR3 on the GPU (s3r4 L10 Nk24 configuration, jtj_blocks 2, lm_only, max_iter 1, start_record true; run_sr3.sh pointed at the v2.4 tree; the record must show both guards true on
  CUDA, the second instance consistent, cuda memory before / peak / after with back_to_pre_probe true, the record written once, threads OMP 2 (run_sr3.sh) and the job's threads 1) on the next naturally free GPU.
- T2 result 6 PART 3 (2026-10-26T22:37Z): SR3 on the GPU DONE for the start record. Runner runs/stage3_smoke/sr3/run_sr3_v24.sh (new file, sha256 d92f80d67ad1f8d4...; points at runs/stage3_smoke/worker_candidate_tree_v2_4;
  the old run_sr3.sh kept), launched detached 2026-10-26T22:17:01Z on physical GPU 5 (free, nothing pending; the queue was not held), OMP_NUM_THREADS=2, the job's threads 1. Job
  runs/stage3_smoke/sr3/job_sr3smoke.json (sha a4feab228ab939aa...; sr3smoke_L10_cl0.45_om+1.0_fixed_startrecord: L10 Nk24 Nr72 even, SPEC channels 4/4/4 with LB/LD/LE 23/22/10, closure 1e-3,
  jtj_blocks 2, chunk 64, lm_only, max_iter 1, start_record true; start nest10_L10_cl0.45_om+1.0_fixed_p0/starts/start_000.pt sha b2c111728a215c98..., source cont150 76d4624a...). Worker shas on disk
  after import: worker.py 2edbd00ccd2bc2b5110297f270211850838b63414a73b24bad72fcb67e6b6b63, problem.py ca146af805bd..., lm.py 82aafe7cf939... (the record's code_sha256_on_disk_after_import). Projected
  warm start 22:27:05Z (pde 1.682e-8, gauge 1.263e-10, U change 1.6e-16). RECORD runs/stage3_smoke/sr3/run_v24/start_record_000.json, sha256 49d7120b2170ccde815fff53469d3248d39ea248b057b256d79cf92c29aeeb87,
  utc 2026-10-26T22:34:17Z, attempt 1, earlier_records [], record_file start_record_000.json, written once (stdout: 'written start_record_000.json once'; no failure-named file). ON CUDA: guards
  frozen_residual_reproducible_pre_probe_bitwise TRUE, production_residual_at_z_unchanged_bitwise TRUE, frozen_residual_at_projected_unchanged_bitwise TRUE, probe_instance_consistent TRUE;
  probe_instance_bitwise FALSE (second-instance frozen cost 1.6943711809911093e-08 against 1.694371180991107e-08 in the production instance, 1.4e-15 relative: the CUDA second instance is consistent
  within the tolerance, not bitwise, as the design allows for a separately built instance; on the CPU (D4) it was bitwise). Costs: frozen at z 1.694371180991107e-08 (meta cost0 unrounded the
  same), at project(z) 1.6943711809911093e-08, refreshed closure only 1.6943711809911093e-08, refreshed closure + nl weights 1.6943711809911116e-08; ||project(z) - z||/||z|| 3.05e-17;
  n_residual_rows 1293121; scalar rows none (use_scalar false, balance_lambda 0, sigmaZ null; SR7 not triggered). cuda_memory: allocated before probe 1490736128 B, peak during probe 19300957184 B
  (19.3 GB; the smoke's single-GPU peak, below the 80 GB card with the LM state not yet built), allocated after release 1490736128 B, back_to_pre_probe TRUE (boundary: after release of all probe
  objects, gc.collect, cuda.synchronize, empty_cache, before the LM). threads: torch_intraop 1, OMP_NUM_THREADS 2. pivot_chosen S q5 rank 1, amp 0.13044009 at this L10 Z0; pivot_saved_in_start S q5
  amp 0.13053049 (the source's Z0 metadata; RUN_STATUS item 0n). pins none. All checklist items of the release set part 3 are met by the record. The job's single LM iteration and lm_only save were
  still running at 2026-10-26T22:37Z; the 'SR3_DONE' line and the exit code in runs/stage3_smoke/sr3/run_sr3_v24_gpu5.log are recorded by the next numerics shift (RUN_STATUS 0d); the start record is
  complete and does not depend on them. With parts 1 and 2 this completes the v2.4 release set for the lead's review (due 2026-10-27T10:00Z); DEPLOYMENT only after the lead's dated release and with
  the queue empty.
- T2 result 6 PART 3 COMPLETION (2026-10-26T22:39Z): the SR3 job finished: worker_v24_stdout.log 'start 0 LM-ONLY done: max_iter, 1 its, 657s; costs [1.694370e-08]; peak GPU memory 38.5 GB; no battery, not a ranked state' and
  'JOB DONE (1/1 starts, 1259s total)' at 2026-10-26T22:38:00Z; runner log runs/stage3_smoke/sr3/run_sr3_v24_gpu5.log: 'exit 0' then 'SR3_DONE' at 22:38:02Z; GPU 5 released (0 MiB). The whole smoke took 21 min on GPU 5
  (build about 10 min, probe about 7 min, one L10 LM iteration 657 s under box load above 300). The LM's first cost 1.694370e-08 equals the record's frozen cost at project(z) to the printed digits. Release set
  parts 1 to 3 COMPLETE on the frozen sha 2edbd00ccd2bc2b5...; the lead's review decides deployment.
- SR3-R1 (lead KD, 2026-10-26T22:39:57Z; recorded 2026-10-26T22:41Z): the reused job file runs/stage3_smoke/sr3/job_sr3smoke.json (sha a4feab228ab939aa...) carries the note 'start_record v2.1 candidate' from its first
  registration (lead IZ), although the runner run_sr3_v24.sh and the record are v2.4 (the record's own 'record' field reads 'start_record_v2.4 (S3-22; ...)' and its code shas name the v2.4 tree). Cosmetic;
  the job file is not edited (its sha is cited in the record); no rerun. KD finds every registered part-3 requirement MET; probe_instance_bitwise FALSE at 1.4e-15 is allowed under SR2 and K4. The release
  review of the whole v2.4 set waits for the verifier's SL24-3 and stays due 2026-10-27T10:00Z; no deployment before the lead's dated release.

### T2 result 7 (2026-10-26T23:46:03Z): R2d pre-aligned rank-2 replay smoke, GPU pair COMPLETE (six iterations each); CPU pair in progress (S3-25 (b), IR PR6; lead KH item 4, KK item 6, KM item 3)
- Directory runs/stage3_smoke/r2dreplay_20261026T2308Z/. Production worker 3bed13b5c6638ac1 / problem ca146af805bdaafe / lm 82aafe7cf9390941. Job configuration = the R2d draft (L 8, Nk 20, Nr 60, even basis, channels 4/4/4 at degrees 19/18/8, closure rows
  1e-3, all5far, tail constraints, chunk 128, far anchor radii 4096 / 16384 / 65536 R0) with the smoke protocol: lm_only, max_iter 6, ftol 1e-12, holdout off, ckpt_interval_s 600, threads 4, time limit 16200 s; start_record
  removed (production worker). A = pivot_rank absent (the production rank-1 path) from St-C cont150 76d4624a (unaligned); B = pivot_rank 2 from the pre-aligned rank-2 start cont150_pivot_rank2_aligned.pt 8db60584.
  Job files: job_A.json 2d8764c5 / job_B.json 54678cbf (CPU; run.sh ba4f1319, OMP 4, launched 23:08:03Z); job_A_gpu.json ed933b19 / job_B_gpu.json b6b34405 (identical apart from job_id and note; run_gpu.sh 9820cbab).
- GPU PAIR (GPU 5, A then B sequentially, launched 23:28:11Z; A exit 0 at 23:36:07Z, B exit 0 at 23:44:01Z; logs A_gpu.log a4ba1e0cb12f4c1d..., B_gpu.log 04d382fb4e18198c...; peak GPU memory 34.4 GB each; LM-ONLY wall
  clock 252 s / 253 s for 6 iterations, tjac 37 to 38.5 s): a first launch on GPU 4 at 23:26:31Z (a placement mistake while GPU 4 held the (0.42, 0.3) stage (ii) job) was stopped at 23:27:42Z during its CPU setup; its
  partial files are archived in aborted_gpu4_20261026T2326Z/ (lead KP item 3 incident).
  - B PIVOT line: 'PIVOT RANK 2 (lead IE S3-5): pivot {pot S, q 8, amp 0.10848765368441801, rank 2, margin 1.0871866368041943}' = the aligned file's saved pivot (S, q 8, amp 0.10848765368441803, margin 1.0871866368041945)
    to 2e-16 relative (GPU against CPU arithmetic; the CPU B log reproduces the saved digits exactly).
  - Projected warm start, both runs: relative change of U on the holdout grid 1.224e-16 (A) / 1.291e-16 (B); cost blocks parent = projected: pde 2.113e-08, gauge 1.784e-10 in both. So neither start is rotated by the worker's
    exact phase projection, and the two starts (related by the rigid rotation +0.5428 rad) have the same PDE and gauge block costs to the printed digits.
  - Per-iteration costs (LM-ONLY done lines; iteration 0 = the first accepted step): A 2.130797e-08, 2.130752e-08, 2.130696e-08, 2.130640e-08, 2.130501e-08, 2.130170e-08 (relative decrease from iteration 0: 2.1e-5, 4.7e-5,
    7.4e-5, 1.4e-4, 2.9e-4); B 2.130796e-08, 2.130785e-08, 2.130774e-08, 2.130748e-08, 2.130729e-08, 2.130715e-08 (5.2e-6, 1.0e-5, 2.3e-5, 3.1e-5, 3.8e-5); relative differences |A - B| / A 4.7e-7, 1.6e-5, 3.7e-5, 5.1e-5,
    1.1e-4, 2.6e-4. Damping (LM lines at iterations 0 and 5): A 3.0e-3 and 7.3e-6; B 3.1e+0 and 1.9e+0; |g| 3.74e-08 (both) and 2.21e-06 / 2.26e-06; rms 2.328e-07 in all lines.
  - READING (primary; the lead reviews): the pre-aligned rank-2 start passes the worker's pivot choice and projection checks (S3-1-type equalities at Z0), and the first accepted step reaches the same cost to 4.7e-7 relative;
    but the rank-2 run B is NOT a replay of the production path A up to rounding: its damping stays three orders larger (about three rejected trial steps at iteration 0, lambda 3.1 against 3.0e-3; 1.9 against 7.3e-6 at
    iteration 5) and its cost decrease over six iterations is 7.7 times smaller (3.8e-5 against 2.9e-4 relative). The gauge row of the rank-2 pair enters the LM's Marquardt-scaled trust region differently from the rank-1
    row, so the gauge-fixing choice changes the optimization trajectory within this budget; whether the two paths end at gauge-equivalent states is not established by six iterations. No field evaluation beyond the worker's
    own lines; no state is ranked.
  - Comparison records: COMPARISON_gpu.json 98599f8abcf3482f... (compare_replay.py 4b31681473603be2..., LM-line parsing) and COMPARISON_gpu_v2.json 5c6710a895e129f7... (compare_replay_v2.py 913aa4b7fd563c1c..., adds the
    done-line cost lists); both pure log parsing.
- CPU PAIR (OMP 4 each, since 23:08:03Z): LM it 0 at 23:32:48Z (A, tjac 1300.8 s) and 23:34:40Z (B, tjac 1411.0 s) with the same printed values as the GPU runs (A 2.130797e-08 lam 3.0e-03; B 2.130796e-08 lam 3.1e+00;
  |g| 3.74e-08); about 23 min per iteration, six iterations expected by about 01:50Z within the 16200 s limit; COMPARISON.json 7b67fe03... / COMPARISON_v2.json fc95e4cb... (partial) are regenerated when it ends.

### T2 result 7, ADDENDUM 1 (2026-10-26T23:50:43Z; lead KU 23:48:32Z, verifier 23:44Z to 23:48Z): R2d DROPPED; wording corrections; two process defects recorded
- VERDICT (lead KU, review tmp/shift10/r2drev/REVIEW.md 21584f36, check 25/0 on the logs, job files and full-precision ledger rows): the rank-2 replay does NOT meet S3-25 (b). The registered criterion (the B job note, written before launch) was 'costs equal to rounding'; the
  full-precision ledger cost histories differ by 6.2e-7, 1.5e-5, 3.7e-5, 5.1e-5, 1.1e-4 and 2.6e-4 relative at iterations 0 to 5 and the damping by about 1000 times; no tolerance is chosen after the data. R2d is dropped as registered; no pivot_rank > 1 job runs; its 3.4 GPU-h cap is
  released, not reassigned. The job draft reports/stage3_jobs/s3r2d_L8_cl0.45_om+1.0_fixed_pivot2.json (sha256 3e07443677e2ef675e9737e407c3d52f547f2f15ec49753eb8a51ce5e139dbd1) was moved to reports/stage3_jobs/dropped/ at 2026-10-26T23:50:43Z; the pre-aligned start file 8db60584 stays as a record. The Stage III launch order is R1 x 3, R3, R2a to R2c, R4.
- WORDING CORRECTIONS to the result above (KU item 2): the iteration-0 relative difference is 6.2e-7 from the full-precision ledger values (4.7e-7 was computed from the printed 7-digit costs); the six-iteration cost decrease of A is about 7.8 times B's (2.942e-4 against 3.789e-5); 'about three
  rejected trial steps' is NOT in the log and is withdrawn: the log supports only 'a damping parameter about 1000 times larger after iteration 0' (the verifier: a rounded lambda cannot identify a rejection count, since a Cholesky failure multiplies lambda by 10 and a rejected trial by 4
  before the accepted 0.3 / 0.7 update). CAUSE: the sentence 'the gauge row enters the trust region differently, so the gauge-fixing choice changes the LM trajectory' is a hypothesis, not established by the pair (verifier 23:46:39Z): the registered wording is 'the cost and damping paths
  differ; cause OPEN'. A second candidate mechanism is the verifier's exact counterexample theory/marquardt_rotation/PROOF.md (3c35f7f5): diagonal Marquardt damping lam * diag(J^T J) is not covariant under a rotation of the coefficient vector even for an exactly rotation-invariant
  objective (the primary lm.py 82aafe7c implements diagonal damping, lm.py line 171). No separating analysis has been run.
- PROCESS DEFECT 1 (rule AU; KU item 3): compare_replay.py 4b316814 (23:44:02Z) and compare_replay_v2.py 913aa4b7 (23:44:48Z) ran before any lead review. Neither COMPARISON JSON (98599f8a, 5c6710a8, 7b67fe03, fc95e4cb) is cited; the lead's own check from the logs and ledger rows is the
  record. No reader repair is requested.
- DEFECT 2 (verifier RV2-2): the JSONs' 'complete_six' flag is computed from the 'LM it k' lines, which lm.py prints every 5 iterations only, so it reads false (n_iterations 2) for complete six-iteration runs although the done-line cost lists hold 6 values (n_done_costs 6); completion is
  established by the LM-ONLY done lines, the exit codes and the ledger rows, not by that flag. The v2 ratio uses A as the denominator; the verifier's full-precision ratios use max(A, B).
- CPU pair: may finish as informational only (KU item 4); it is stopped and the stop recorded if the CPU is needed for the stage (ii) readings.

### T2 result 7, ADDENDUM 2 (2026-10-27T01:41:24Z): the CPU replay pair finished (INFORMATIONAL ONLY, lead KU item 4; no comparison script run; raw done lines)
- A (CPU, OMP 4, from the unaligned St-C start, rank 1): '2026-10-27T01:15:19Z start 0 LM-ONLY done: max_iter, 6 its, 7458s; costs ['2.130797e-08', '2.130752e-08', '2.130696e-08', '2.130640e-08', '2.130501e-08', '2.130170e-08']'; 'JOB DONE (1/1 starts, 7637s total)'.
  A.log sha256 0d7fde6d630f6106f89fdc1cedbb176f8d81aaecb62d946df909d7386a4d3fe1.
- B (CPU, OMP 4, from the pre-aligned rank-2 start, pivot_rank 2): '2026-10-27T01:26:42Z start 0 LM-ONLY done: max_iter, 6 its, 8141s; costs ['2.130796e-08', '2.130785e-08', '2.130774e-08', '2.130748e-08', '2.130729e-08', '2.130715e-08']'; 'JOB DONE (1/1 starts, 8320s total)'.
  B.log sha256 6eadcbcf42c0d37c9056d020fa1401406033bfccdd3df90cc2708606cfce4250.
- Observation (informational): all twelve printed 7-digit costs equal the GPU pair's (A_gpu.log a4ba1e0c..., B_gpu.log 04d382fb...) digit for digit; the CPU pair therefore reproduces the GPU pair's cost histories at the printed precision, on both the rank-1 and the rank-2 path.
  The registered S3-25 (b) verdict (not met; R2d dropped, lead KU) is unchanged; the paths differ between A and B as before; cause OPEN.
