# g4_v1 draft: policy and supervisor files (DRAFT, NOT FROZEN; lead 14:17Z item 2)

Prepared 2026-10-24T14:19Z in outputs/dev_v9/pending_g4. No manifest-listed file is edited; nothing is frozen; the g3_v1 manifest is untouched.
Reason: the guard's family RSS is the plain per-process RSS sum. T4 s3 peaked at 120629.3 MiB on that measure at elapsed 281 s (13:36:57Z; 8-worker fork pool
forming the Jacobian origin-column polynomials from a parent holding the 15.7 GiB longdouble basis cache), T4 s1 at 120621.1 MiB; item F (assessment, 8 workers)
at 19147.1 MiB. A campaign slice builds the same Jacobian with the same fork pool, so campaign_policy_v2's max_family_rss_mib 40960 would stop it with no real
memory pressure (host available memory never below about 952 GiB during T4 s3 and item F).

## (a) outputs/dev_v9/pending_g4/campaign_policy_v3.json
sha256 62eb3cb3d3b86d0fcf4b31cd2e0af5a704c7dfef2dfcc5f69bc52f32b09a5658. Counterpart outputs/campaign860/campaign_policy_v2.json (g3_v1 manifest entry,
sha256 d60588811184c140d187546af45431651356c18bf4846e8635dc3bb9379ac97a, 423 bytes). Same key set; exactly one value differs:
- max_family_rss_mib 40960 -> 163840 (PLACEHOLDER by the lead's rule: max(163840, ceil(1.3 x the largest of the guard peak, the bench row peak and the bench child-sampler peak)); with the largest known peak 120629.3 MiB, 1.3x = 156819 < 163840, so 163840 stands unless the bench shows a larger peak).
- max_seconds stays 6600 (changed only if the bench step cost requires it; set after the bench read).
Every other limit unchanged: blas_threads 1, max_load_per_cpu 1.5, PSI full 60, pageout 8 MiB/s, max_session_seconds 900000, swap growth 512 MiB, swapout 8 MiB/s,
temperature 95 C, min_available_mib 16384, min_available_pct 10, min_disk_free_gib 10, nice_increment 15, sample_seconds 2, terminate_grace_seconds 120.
Real protection remains min_available_mib 16384 and min_available_pct 10 (lead checklist A3); 163840 MiB leaves the 1.1 TiB host more than a 2x margin over the true peak (parent VmHWM 24.4 GiB).

## (b) outputs/dev_v9/pending_g4/supervise860_v4.sh (revised 15:2xZ, lead ruling 15:10:19Z)
sha256 8e04b4fcc1099c9376674220293f93f6ded9badef808cdf05b9a8b5cd73fbb6e. Counterpart bin/supervise860_v3.sh (g3_v1 manifest entry, sha256
f7b13f3b44e7c543a2ab5c8df545435dff12d301621da45706d92cdc764ff1d9, 11566 bytes). The supervisor does not take the policy as an argument (line 16 hard-codes it),
so (b) is needed. `diff bin/supervise860_v3.sh outputs/dev_v9/pending_g4/supervise860_v4.sh` has exactly THREE changes:
1. line 16: POLICY=$LANE/outputs/campaign860/campaign_policy_v2.json -> campaign_policy_v3.json (the g4_v1 purpose).
2. line 30 (STOP branch): `erc=$?` is captured directly after the end-assessment guard call and the log line says `end assessment exit=$erc` (v3 logged `exit=$?` after `$(stamp)` in the same string, so it always printed 0).
3. lines 51-52 (slice guard call): `grc=$?` now follows the guard call directly and `RENEWARG=""` comes after it (v3 assigned RENEWARG first, so grc was the status of the assignment, always 0, and the F12 "guard exited 0" test at line 75 and the guard_exit log value were dead).
bash -n passes. Previous draft (POLICY line only, sha256 5956f33d...) kept as outputs/dev_v9/pending_g4/supervise860_v4_before_1520Z.sh.bak. At the freeze the file is installed as
bin/supervise860_v4.sh (new path; v3 stays listed and unexecuted) and the policy as outputs/campaign860/campaign_policy_v3.json; the manifest g4_v1 (base g3_v1)
adds both entries through freeze_g4_supplement.py and changes nothing else.

## (c) Does any T4 file import these two files?
tests/g3_t4.py imports campaign860 (feasible_trial, durable). campaign860.py references:
    32:bin/supervise860_v3.sh (reads slice_completion/slice_<n>_<run_id>.json; passes its own sha256 in SUPERVISOR_SHA256, recorded in slice_start).
These are string/metadata references, not reads of the policy at import; the policy is consumed only by the guard (guard.py init/run via the supervisor's POLICY line),
and the supervisor is a shell file no Python module imports. So no T4 computation depends on either file (the verifier is asked to confirm, lead 14:17Z).

## Freeze condition (revised 14:45Z after verifier 14:29Z: no broad-scan freezer for a two-entry supplement)
Only after the bench read and the lead's word: (1) copy (a) to outputs/campaign860/campaign_policy_v3.json and (b) to bin/supervise860_v4.sh (chmod +x);
(2) run the exact-supplement writer outputs/dev_v9/pending_g4/freeze_g4_supplement.py (first with --dry-run): it copies the g3_v1 manifest object, re-verifies
every existing files[] and closure row against the live bytes, refuses on any mismatch, on an existing target or on an installed file that differs from its
draft, and appends EXACTLY the two new rows (tag g4_v1, base_manifest_tag g3_v1, base_manifest_sha256 recorded, a supplement_statement naming the writer's
sha256). bin/freeze_manifest_v3.sh is NOT used for g4_v1 (its find roots would scan bin/ broadly and would omit the new policy; the frozen freezer stays unchanged).
(3) check the new manifest (all g3_v1 rows present with equal hashes, exactly two added rows, closure identical); (4) record ACTIVE_MANIFEST (lead A4) with the
absolute path of code_manifest_g4_v1.json; (5) the pilot per the lead's G4 checklist, launched through bin/supervise860_v4.sh.

## Final values (lead ruling G3-R2, 2026-10-24T22:41:05Z; applied to the draft 22:48Z)
- max_family_rss_mib = max(163840, ceil(1.3 x 131536.14)) = 170997. Governing peak 131536.14 MiB = the guard's peak_family_rss_mib in outputs/g3/session_g3_v1_s4/runs/20261024T182153Z_1792866113826692144_g3_bench/result.json (main sampler 131513.3, child record 131460.4).
- max_seconds = 6600 (unchanged). W = 4539 s = the largest completed bench s4 full-assessment wall: outputs/g3/g3_v1/bench.assess_0.json began_utc 2026-10-24T19:28:35Z, finished_utc 2026-10-24T20:44:14Z (assess_1: 4106 s, 20:52:20Z to 22:00:46Z). 1.3 W = 5901 <= 6600, so the rule "100 x ceil(1.3 W / 100)" is not triggered. These walls were measured under the external box load (load average about 85 to 90) and therefore govern, per the lead's 20:49:48Z ruling; item F (2747 s) does not.
- Draft outputs/dev_v9/pending_g4/campaign_policy_v3.json now: sha256 60cf96429e9859278cb5f5321089fe2901bb924a5e97100aae11de91991b21b3, 423 bytes; the only key differing from campaign_policy_v2.json is max_family_rss_mib (40960 -> 170997). The bench s4 step itself ended as a guard stop (CPU load per logical CPU ceiling, box-wide), strict FAIL, exception E-G3.B.
