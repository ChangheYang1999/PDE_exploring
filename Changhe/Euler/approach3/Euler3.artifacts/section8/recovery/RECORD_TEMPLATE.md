# Section 8 single-command recovery test (lead d128 QD item 4, RT-A to RT-D) -- TEMPLATE prepared in shift 14; the executing shift copies it to RECORD.md and fills every [bracket]; nothing is cited before the lead's review (RT-D)

Scope: a software test of the supervisor's stop and restart with an empty queue and no running job; not evidence about any state.

## RT-A timing preconditions (all must hold; each checked in one call with date -u and pasted here)
- Both R4 JOB DONE records exist in NUM_REPORT (control s3r4_L10_cl0.45_om+1.0_fixed_cont150, perturbed s3r4_L10_cl0.45_om+1.0_fixed_p1e-2_s31010): [stamps]
- Both R4 cap watchers have exited: `pgrep -af cap_watcher_v4_1 | grep -v pgrep` -> [empty]; watcher status files status/cap_watcher_<job>.json -> [status, occupied seconds]
- queue/pending is empty: `ls queue/pending` -> [empty]; queue/running is empty: `ls queue/running` -> [empty]
- status.py shows no running job: `.venv/bin/python scripts/status.py 0 | head -1` -> [line]
- Complete by 2026-10-28T12:00:00Z. If any job is running under the supervisor, do not stop it.

## RT-B command and record (from a NEW login shell: `bash -l -c '...'`; one attempt)
- Script hashes at the test (sha256sum): scripts/stop_supervisor.sh [sha; 0efb2ae79ae2f994 at 16:4xZ Oct 27], scripts/start_supervisor.sh [sha; 51dcda6f4e215183], scripts/supervisor.py [sha; 53f53cfdcb791bb1], configs/supervisor.json [sha]
- status.py output BEFORE the stop (full first line and the queue counts): [text]; ledger line count before: [n]; queue/done file count: [n]; queue/hold file count: [n]
- Old supervisor pid 3548537 alive before the stop: [ps line]; heartbeat guard pid 866595 (left running): [ps line]
- STOP: `bash -l -c 'cd . && date -u && bash scripts/stop_supervisor.sh && date -u'` -> [stamps, output]; old pid gone: [pgrep]
- START: `bash -l -c 'cd . && date -u && bash scripts/start_supervisor.sh && date -u'` -> [stamps, output]; new supervisor pid: [pid] (from logs/supervisor.log / status/STATUS.json)
- First heartbeat after the restart: status/STATUS.json 'status written' stamp and supervisor heartbeat age: [stamps] (usual interval: a poll every about 20 s; heartbeat_stale_s 1500)
- status.py output AFTER the restart: [text]; ledger line count after: [n] (only supervisor_start-type rows may be added; list them); queue/done, queue/hold counts after: [n, n]

## RT-C pass criteria (fixed in advance by the lead)
- The restarted supervisor is alive, heartbeats within its usual interval, and shows the same accepted queue and ledger state as before the stop (pending 0, running 0, done [n], failed 30, the hold queues unchanged). Any difference is REPORTED here and not repaired silently.

## RT-D
- FINAL_REPORT quotes the recovery command only after the lead's review of this record. Send the lead the record path and sha256.
