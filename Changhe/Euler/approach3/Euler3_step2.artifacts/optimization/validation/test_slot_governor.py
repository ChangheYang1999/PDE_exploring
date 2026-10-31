#!/usr/bin/env python
"""Unit test of scripts/slot_governor.decide (no processes, no files): the decisions for the PLACE "4:1 5:1 6:0 6:0" pending set."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import slot_governor as G

def jid(tag, c_l, omega, free):
    """Exactly the job_id format of scripts/enqueue_d6.py: f"{tag}_L6_cl{c_l:.4f}_om{omega:.4f}_{'free' if free else 'fixed'}" (V213)."""
    return f"{tag}_L6_cl{c_l:.4f}_om{omega:.4f}_{'free' if free else 'fixed'}"
PEND = [dict(job_id=jid("p1_s1_S01", 0.45, 1.0, True), gpus_allowed=[4], exclusive=True, priority=30), dict(job_id=jid("p1c_s1_S01", 0.45, 1.0, False), gpus_allowed=[5], exclusive=True, priority=29),
        dict(job_id=jid("p2_s1_S09", 0.45, 0.3, True), gpus_allowed=[6], exclusive=False, priority=28), dict(job_id=jid("p2c_s1_S09", 0.45, 0.3, False), gpus_allowed=[6], exclusive=False, priority=27)]
SEG2 = [dict(job_id=jid("p1_s2_S01", 0.45, 1.0, True), gpus_allowed=[4], exclusive=True, priority=30), dict(job_id=jid("p1c_s2_S01", 0.45, 1.0, False), gpus_allowed=[5], exclusive=True, priority=29)]
# pair-key contract with the real enqueuer names (V213)
assert G.pair_key(PEND[0]["job_id"]) == G.pair_key(PEND[1]["job_id"]) == "p1_s1_S01_L6_cl0.4500_om1.0000", (G.pair_key(PEND[0]["job_id"]), G.pair_key(PEND[1]["job_id"]))
assert G.pair_key(PEND[2]["job_id"]) == G.pair_key(PEND[3]["job_id"]) == "p2_s1_S09_L6_cl0.4500_om0.3000"
assert G.pair_key(PEND[0]["job_id"]) != G.pair_key(PEND[2]["job_id"]) and G.pair_key(SEG2[0]["job_id"]) == G.pair_key(SEG2[1]["job_id"]) != G.pair_key(PEND[0]["job_id"])
assert G.pair_key("smk_x_L6_cl0.4500_om1.0000_free") == "smk_x_L6_cl0.4500_om1.0000_free" and G.pair_key("g7_gpu_v1_L6_cl0.4500_om1.0000_free") == "g7_gpu_v1_L6_cl0.4500_om1.0000_free"
print("pair_key contract with the enqueue_d6.py job_id format: PASS")
def V(n): return [dict(pid=100 + i, gpu="7", script="validation/gates.py") for i in range(n)]   # budget-only fixtures: validation on a GPU outside the pairs (co-tenancy scenarios use VG)
def W(gpus): return [dict(pid=200 + i, gpu=str(g), script="scripts/worker_d6.py") for i, g in enumerate(gpus)]
def VG(gpus): return [dict(pid=300 + i, gpu=str(g), script="validation/gates.py") for i, g in enumerate(gpus)]
def WR(gpus): return [dict(pid=400 + i, gpu=str(g), script="scripts/run_gpu_battery.sh", covered=False) for i, g in enumerate(gpus)]
cases = [  # (name, validation (int n on GPU 5, or list of records), worker gpus, hold, pending, expected gpus, expected max_running[, wrappers, runner_alive])
 ("hold with 4 validation", 4, [], 5, PEND, [], 1),
 ("hold with 2 validation", 2, [], 1, PEND, [], 1),
 ("no hold, 4 validation", 4, [], 0, PEND, [], 1),
 ("no hold, 3 validation: P1 needs two slots -> wait", 3, [], 0, PEND, [], 1),
 ("no hold, 2 validation: P1 starts together on 4 and 5, P2 waits", 2, [], 0, PEND, [4, 5], 2),
 ("no hold, 1 validation, P1 running: P2 needs 2, budget 1", 1, [4, 5], 0, PEND[2:], [4, 5], 2),
 ("no hold, 0 validation, P1 running: P2 starts together on 6", 0, [4, 5], 0, PEND[2:], [4, 5, 6], 4),
 ("no hold, 0 validation, nothing running: both pairs pending -> one grant per tick: P1 only (P2 next tick)", 0, [], 0, PEND, [4, 5], 2),
 ("no hold, 1 validation, nothing running: 3 slots -> P1 only", 1, [], 0, PEND, [4, 5], 2),
 ("no hold, 0 validation, P2 running on 6: P1 starts", 0, [6, 6], 0, PEND[:2], [4, 5, 6], 4),
 ("no hold, 2 validation, P2 running on 6: budget 0", 2, [6, 6], 0, PEND[:2], [6], 2),
 ("no hold, no pending, 2 workers", 0, [4, 5], 0, [], [4, 5], 2),
 ("no hold, no pending, no workers", 0, [], 0, [], [], 1),
 ("P1 segment 2 pending while P1 segment 1 still runs on 4 and 5: wait (exclusive)", 0, [4, 5], 0, SEG2, [4, 5], 2),
 ("P1 segment 2 pending, P2 running on 6, budget 2: start", 0, [6, 6], 0, SEG2, [4, 5, 6], 4),
 ("P1 segment 2 pending, P2 running on 6, 1 validation: wait", 1, [6, 6], 0, SEG2, [6], 2),
 ("strict order: P1 blocked by a worker on GPU 4, P2 feasible -> P2 waits too", 0, [4], 0, PEND, [4], 1),
 ("V212: queue empty but the runner still alive -> hold", 2, [], 0, PEND, [], 1, [], True),
 ("V212: wrapper on GPU 4 without a visible python child counts as busy (3 val + 1 wrap = 4)", 3, [], 0, PEND, [], 1, WR([4]), False),
 ("V212: two validation on GPUs 4 and 6, budget 2: P1 would share GPU 4 with a gate -> wait; P2 behind it waits (strict order)", VG([4, 6]), [], 0, PEND, [], 1),
 ("V212: two validation on GPU 6 and 6? one gates per GPU: validation on 6 only, budget 3: P1 starts on 4 and 5, P2 waits (co-tenant on 6)", VG([6]), [], 0, PEND, [4, 5], 2),
 ("V212: validation on GPU 5 blocks P1 (unequal sharing), P2 waits behind it", VG([5]), [], 0, PEND, [], 1),
 ("V212 recovery: P2 FREE runs on 6, its partner is re-queued alone: granted (free slot on 6, no co-tenant)", 0, [6], 0, PEND[3:], [6], 2, [], False, dict(running={PEND[2]["job_id"]: dict(exclusive=False)}, done={})),
 ("V212 recovery with a gate on GPU 6: partner waits", VG([6]), [6], 0, PEND[3:], [6], 1, [], False, dict(running={PEND[2]["job_id"]: dict(exclusive=False)}, done={})),
 ("V214: lone pending member whose partner is neither running nor done: wait", 0, [], 0, PEND[3:], [], 1),
 ("V214: lone pending member, partner done: granted alone", 0, [], 0, PEND[3:], [6], 1, [], False, dict(running={}, done={PEND[2]["job_id"]: dict(exclusive=False)})),
 ("wrapper covered later: 2 val + 1 wrap on GPU 4, budget 1, P1 waits", 2, [], 0, PEND, [], 1, WR([4]), False),
]
def FLEX(tag, c_l, om, free, prio, queue="pending", target=None): return dict(job_id=jid(tag, c_l, om, free), gpus_allowed=[], exclusive=None, priority=prio, placement="governor", queue=queue, target=target)
FPEND = [FLEX("p1_s1_S01", 0.45, 1.0, True, 30), FLEX("p1c_s1_S01", 0.45, 1.0, False, 29), FLEX("p2_s1_S09", 0.45, 0.3, True, 28), FLEX("p2c_s1_S09", 0.45, 0.3, False, 27)]
FW = lambda gpus, ids: [dict(pid=200 + i, gpu=str(g), script="scripts/worker_d6.py", job_id=j) for i, (g, j) in enumerate(zip(gpus, ids))]
flex_cases = [  # (name, validation records, worker records, hold, pending, expected gpus, expected max_running, expected placements, queue_state)
 ("flex: three gates running, budget 1: hold on budget", VG([4, 5, 6]), [], 0, FPEND, [], 1, {}, None),
 ("flex: gates on 4 and 5, GPU 6 clear, budget 2: P1 together on 6", VG([4, 5]), [], 0, FPEND, [6], 2, {FPEND[0]["job_id"]: [6, False], FPEND[1]["job_id"]: [6, False]}, None),
 ("flex: gate on 6 only, budget 3: P1 alone on 4 and 5; P2 waits (no clear GPU)", VG([6]), [], 0, FPEND, [4, 5], 2, {FPEND[0]["job_id"]: [4, True], FPEND[1]["job_id"]: [5, True]}, None),
 ("flex: nothing running, budget 4: one grant per tick -> P1 alone on 4 and 5; P2 at the next tick", [], [], 0, FPEND, [4, 5], 2, {FPEND[0]["job_id"]: [4, True], FPEND[1]["job_id"]: [5, True]}, None),
 ("flex: P1 running together on 6 (placed), gate on 4, GPU 5 clear, budget 1: P2 waits", VG([4]), FW([6, 6], [FPEND[0]["job_id"], FPEND[1]["job_id"]]), 0, FPEND[2:], [6], 2, {}, None),
 ("flex: P1 running together on 6, GPUs 4 and 5 clear, budget 2: P2 alone on 4 and 5", [], FW([6, 6], [FPEND[0]["job_id"], FPEND[1]["job_id"]]), 0, FPEND[2:], [4, 5, 6], 4, {FPEND[2]["job_id"]: [4, True], FPEND[3]["job_id"]: [5, True]}, None),
 ("flex: P1 alone on 4 and 5, GPU 6 clear, budget 2: P2 together on 6", [], FW([4, 5], [FPEND[0]["job_id"], FPEND[1]["job_id"]]), 0, FPEND[2:], [4, 5, 6], 4, {FPEND[2]["job_id"]: [6, False], FPEND[3]["job_id"]: [6, False]}, None),
 ("flex: P1 alone on 4 and 5, gate on 6, budget 1: P2 waits", VG([6]), FW([4, 5], [FPEND[0]["job_id"], FPEND[1]["job_id"]]), 0, FPEND[2:], [4, 5], 2, {}, None),
 ("flex: lone P2 FIXED re-queued, partner running non-exclusive on 6 with a free slot: same GPU", [], FW([6], [FPEND[2]["job_id"]]), 0, FPEND[3:], [6], 2, {FPEND[3]["job_id"]: [6, False]}, dict(running={FPEND[2]["job_id"]: dict(exclusive=False)}, done={})),
 ("flex: lone P2 FIXED re-queued, partner running exclusive on 4, GPU 5 clear: alone on 5", [], FW([4], [FPEND[2]["job_id"]]), 0, FPEND[3:], [4, 5], 2, {FPEND[3]["job_id"]: [5, True]}, dict(running={FPEND[2]["job_id"]: dict(exclusive=True)}, done={})),
 ("flex: lone member without running or done partner: wait", [], [], 0, FPEND[3:], [], 1, {}, None),
 ("flex: hold while the runner is alive", [], [], 0, FPEND, [], 1, {}, "runner"),
 ("v6: one grant per tick: nothing running, budget 4, P1 pending and P2 staged -> only P1 (alone on 4, 5)", [], [], 0, FPEND[:2] + [dict(j, queue="staged") for j in FPEND[2:]], [4, 5], 2, {FPEND[0]["job_id"]: [4, True], FPEND[1]["job_id"]: [5, True]}, None),
 ("v6: V217 state: P1 FREE alone left on 6 (partner finished), P2 staged, GPUs 4 and 5 clear, budget 3 -> P2 alone on 4 and 5 (moved into pending by apply)", [], FW([6], [FPEND[0]["job_id"]]), 0, [dict(j, queue="staged") for j in FPEND[2:]], [4, 5, 6], 3, {FPEND[2]["job_id"]: [4, True], FPEND[3]["job_id"]: [5, True]}, None),
 ("v6: staged P2 with a gate on 4 and P1 together on 6: GPU 5 alone is clear but P2 needs two slots on one GPU -> wait", VG([4]), FW([6, 6], [FPEND[0]["job_id"], FPEND[1]["job_id"]]), 0, [dict(j, queue="staged") for j in FPEND[2:]], [6], 2, {}, None),
 ("v6: segment-2 targets (P1 s2 together on 6), GPU 6 clear, budget 2 -> both on 6 non-exclusive", [], FW([4, 5], ["other_a", "other_b"]), 0, [FLEX("p1_s2_S01", 0.45, 1.0, True, 30, "staged", dict(gpu=6, exclusive=False)), FLEX("p1c_s2_S01", 0.45, 1.0, False, 29, "staged", dict(gpu=6, exclusive=False))], [4, 5, 6], 4, {jid("p1_s2_S01", 0.45, 1.0, True): [6, False], jid("p1c_s2_S01", 0.45, 1.0, False): [6, False]}, None),
 ("v6: segment-2 targets (alone on 4 and 5) while a worker still runs on 5 -> wait", [], FW([5], ["other_a"]), 0, [FLEX("p1_s2_S01", 0.45, 1.0, True, 30, "staged", dict(gpu=4, exclusive=True)), FLEX("p1c_s2_S01", 0.45, 1.0, False, 29, "staged", dict(gpu=5, exclusive=True))], [5], 1, {}, None),
 ("v6: segment-2 targets (alone on 4 and 5), both clear, budget 4 -> granted", [], [], 0, [FLEX("p1_s2_S01", 0.45, 1.0, True, 30, "staged", dict(gpu=4, exclusive=True)), FLEX("p1c_s2_S01", 0.45, 1.0, False, 29, "staged", dict(gpu=5, exclusive=True))], [4, 5], 2, {jid("p1_s2_S01", 0.45, 1.0, True): [4, True], jid("p1c_s2_S01", 0.45, 1.0, False): [5, True]}, None),
 ("v6: segment-2 target GPU 6 with a gate on it -> wait", VG([6]), [], 0, [FLEX("p1_s2_S01", 0.45, 1.0, True, 30, "staged", dict(gpu=6, exclusive=False)), FLEX("p1c_s2_S01", 0.45, 1.0, False, 29, "staged", dict(gpu=6, exclusive=False))], [], 1, {}, None),
]
for name, vals, works, hold, pend, eg, emr, epl, qs in flex_cases:
    G.lane_procs = (lambda vals=vals, works=works: (list(vals), list(works), []))
    G.pending_jobs = (lambda pend=pend: [dict(j) for j in pend])
    G.hold_count = (lambda hold=hold: hold)
    G.runner_alive = (lambda qs=qs: qs == "runner")
    G.queue_state = (lambda qs=qs: (qs if isinstance(qs, dict) else dict(running={}, done={})))
    d = G.decide([4, 5, 6], 2)
    ok = (d["gpus"] == eg and d["max_running"] == emr and d["placements"] == epl)
    print(("PASS" if ok else "FAIL"), name, "->", d["gpus"], d["max_running"], d["placements"], "" if ok else f"(expected {eg}, {emr}, {epl})", "; ".join(d["reasons"]))
    if not ok: fails_flex = globals().get("fails_flex", 0) + 1; globals()["fails_flex"] = fails_flex
# apply_placements on a temporary queue directory
import tempfile, json as _json
tmpd = tempfile.mkdtemp(); os.makedirs(os.path.join(tmpd, "queue", "pending"))
for jb in FPEND[:2]:
    _json.dump(dict(job_id=jb["job_id"], gpus_allowed=None, exclusive=None, priority=jb["priority"], placement="governor", note="n", config={"max_iter": 120}), open(os.path.join(tmpd, "queue", "pending", jb["job_id"] + ".json"), "w"))
old_root = G.ROOT; G.ROOT = tmpd
G.pending_jobs = lambda: G._read_jobs("pending")
w = G.apply_placements({FPEND[0]["job_id"]: (4, True), FPEND[1]["job_id"]: (5, True)})
j0 = _json.load(open(os.path.join(tmpd, "queue", "pending", FPEND[0]["job_id"] + ".json"))); j1 = _json.load(open(os.path.join(tmpd, "queue", "pending", FPEND[1]["job_id"] + ".json")))
ok = (j0["gpus_allowed"] == [4] and j0["exclusive"] is True and j1["gpus_allowed"] == [5] and j1["exclusive"] is True and j0["config"] == {"max_iter": 120} and "placed by the slot governor" in j0["note"] and len(w) == 2)
w2 = G.apply_placements({FPEND[0]["job_id"]: (4, True)})   # idempotent
print(("PASS" if ok and w2 == [] else "FAIL"), "apply_placements writes gpus_allowed/exclusive/note, leaves config, idempotent")
if not (ok and w2 == []): globals()["fails_flex"] = globals().get("fails_flex", 0) + 1
# staged -> placed -> moved into pending
os.makedirs(os.path.join(tmpd, "queue", "staged"))
for jb in FPEND[2:]:
    _json.dump(dict(job_id=jb["job_id"], gpus_allowed=[], exclusive=None, priority=jb["priority"], placement="governor", note="n", config={"max_iter": 120}), open(os.path.join(tmpd, "queue", "staged", jb["job_id"] + ".json"), "w"))
G.pending_jobs = lambda: G._read_jobs("pending") + G._read_jobs("staged")
w3 = G.apply_placements({FPEND[2]["job_id"]: (6, False), FPEND[3]["job_id"]: (6, False)})
moved = all(os.path.exists(os.path.join(tmpd, "queue", "pending", jb["job_id"] + ".json")) and not os.path.exists(os.path.join(tmpd, "queue", "staged", jb["job_id"] + ".json")) for jb in FPEND[2:])
j2 = _json.load(open(os.path.join(tmpd, "queue", "pending", FPEND[2]["job_id"] + ".json")))
ok3 = moved and j2["gpus_allowed"] == [6] and j2["exclusive"] is False and j2["config"] == {"max_iter": 120} and j2["placement_by_governor"]["moved_from"] == "queue/staged" and len(w3) == 2 and all(x[3] for x in w3)
print(("PASS" if ok3 else "FAIL"), "apply_placements on staged files: placement written, files moved into pending, config untouched")
if not ok3: globals()["fails_flex"] = globals().get("fails_flex", 0) + 1
# V220/V223 barrier with persisted closure state (fake supervisor log, cfg and heartbeat in the temporary directory)
import threading, time
G.STATE_PATH = os.path.join(tmpd, "state.json")
cfgp = os.path.join(tmpd, "cfg.json"); _json.dump(dict(gpus=[6], max_running=2, slots_per_gpu=2), open(cfgp, "w"))
fake_log = os.path.join(tmpd, "supervisor.log"); open(fake_log, "w").write("2026-10-29T09:00:00Z supervisor started\n2026-10-29T09:00:20Z GPU list changed: [] -> [6]\n")
hbp = os.path.join(tmpd, "hb.json"); _json.dump(dict(epoch=time.time() - 1000, pid=os.getpid()), open(hbp, "w"))
st = dict(closed=False, closure_epoch=None, log_offset=None, acked=False)
# (1) exposed -> close, no ack within the timeout -> deferred, state keeps the closure offset
acked, detail = G.barrier_close_and_ack(cfgp, st, timeout_s=1.0, poll_s=0.2, sup_log=fake_log, hb_path=hbp)
c1 = _json.load(open(cfgp)); ok1 = (not acked) and c1["gpus"] == [] and st["closed"] and st["log_offset"] is not None and not st["acked"]
print(("PASS" if ok1 else "FAIL"), "barrier: exposed config closed, no acknowledgment -> deferred with persisted closure offset", detail)
# (2) next tick: file already closed; without the ack of THE SAME closure it still waits (V223)
acked2, detail2 = G.barrier_close_and_ack(cfgp, st, timeout_s=1.0, poll_s=0.2, sup_log=fake_log, hb_path=hbp)
ok2 = (not acked2) and (not st["acked"])
print(("PASS" if ok2 else "FAIL"), "barrier: closed file alone is not trusted on the next tick (V223)", detail2)
# (3) the supervisor's acknowledgment line for that closure arrives -> the next tick publishes
with open(fake_log, "a") as f: f.write("2026-10-29T09:01:00Z GPU list changed: [6] -> []\n")
acked3, detail3 = G.barrier_close_and_ack(cfgp, st, timeout_s=2.0, poll_s=0.2, sup_log=fake_log, hb_path=hbp)
ok3 = acked3 and st["acked"]
print(("PASS" if ok3 else "FAIL"), "barrier: the deferred closure is acknowledged later by its own change line", detail3)
# (4) a restarted supervisor that read the closed file also acknowledges
st4 = dict(closed=True, closure_epoch=time.time(), log_offset=os.path.getsize(fake_log), acked=False)
with open(fake_log, "a") as f: f.write('2026-10-29T09:02:00Z supervisor started pid 1 cfg={"gpus": [], "slots_per_gpu": 2}\n')
ok4 = G.closure_acknowledged(cfgp, st4, sup_log=fake_log, hb_path=hbp)[0]
print(("PASS" if ok4 else "FAIL"), "barrier: a supervisor start line showing gpus [] acknowledges the closure")
# (5) startup with a closed file and unknown cache: heartbeat must be later than the governor start + 35 s
st5 = dict(closed=True, closure_epoch=None, log_offset=None, acked=False)
ok5a = not G.closure_acknowledged(cfgp, st5, sup_log=fake_log, hb_path=hbp)[0]
_json.dump(dict(epoch=G.GOV_START + 40, pid=os.getpid()), open(hbp, "w"))
ok5a = ok5a and not G.closure_acknowledged(cfgp, st5, sup_log=fake_log, hb_path=hbp)[0]   # 40 s is not enough (iteration bound)
_json.dump(dict(epoch=G.GOV_START + 130, pid=999999), open(hbp, "w"))
ok5a = ok5a and not G.closure_acknowledged(cfgp, st5, sup_log=fake_log, hb_path=hbp)[0]   # dead supervisor pid: no acknowledgment
_json.dump(dict(epoch=G.GOV_START + 130, pid=os.getpid()), open(hbp, "w"))
ok5b = G.closure_acknowledged(cfgp, st5, sup_log=fake_log, hb_path=hbp)[0]
print(("PASS" if ok5a and ok5b else "FAIL"), "barrier: startup with a closed file waits for a live-pid heartbeat after start + 120 s (40 s or a dead pid is not enough), then publishes")
# (6) dry run executes nothing
ok6 = not G.barrier_close_and_ack(cfgp, dict(st), dry=True, sup_log=fake_log, hb_path=hbp)[0]
print(("PASS" if ok6 else "FAIL"), "barrier: dry run executes nothing")
for ok_ in (ok1, ok2, ok3, ok4, ok5a and ok5b, ok6):
    if not ok_: globals()["fails_flex"] = globals().get("fails_flex", 0) + 1
# (7) lone member alone with its partner DONE carries the sharing-condition note
G.lane_procs = lambda: ([], [], []); G.pending_jobs = lambda: [dict(FPEND[3])]; G.hold_count = lambda: 0; G.runner_alive = lambda: False
G.queue_state = lambda: dict(running={}, done={FPEND[2]["job_id"]: dict(exclusive=False)})
d7 = G.decide([4, 5, 6], 2); ok7 = d7["placements"] == {FPEND[3]["job_id"]: [4, True]} and "sharing condition differs from partner" in d7["placement_notes"].get(FPEND[3]["job_id"], "")
print(("PASS" if ok7 else "FAIL"), "lone member with a DONE partner: placed alone with the 'sharing condition differs from partner' note", d7["placement_notes"])
G.queue_state = lambda: dict(running={FPEND[2]["job_id"]: dict(exclusive=False)}, done={}); G.lane_procs = lambda: ([], FW([6], [FPEND[2]["job_id"]]), [])
d8 = G.decide([4, 5, 6], 2); ok8 = d8["placements"] == {FPEND[3]["job_id"]: [6, False]} and "same sharing condition" in d8["placement_notes"].get(FPEND[3]["job_id"], "")
print(("PASS" if ok8 else "FAIL"), "lone member beside its running non-exclusive partner: same sharing condition", d8["placement_notes"])
for ok_ in (ok7, ok8):
    if not ok_: globals()["fails_flex"] = globals().get("fails_flex", 0) + 1
G.ROOT = old_root
fails = globals().get("fails_flex", 0)
for case in cases:
    name, nv, wg, hold, pend, eg, emr = case[:7]
    wraps = case[7] if len(case) > 7 else []
    ralive = case[8] if len(case) > 8 else False
    vals = V(nv) if isinstance(nv, int) else list(nv)
    G.lane_procs = (lambda vals=vals, wg=wg, wraps=wraps: (vals, W(wg), list(wraps)))
    G.pending_jobs = (lambda pend=pend: list(pend))
    G.hold_count = (lambda hold=hold: hold)
    G.runner_alive = (lambda ralive=ralive: ralive)
    qs = case[9] if len(case) > 9 else dict(running={}, done={})
    G.queue_state = (lambda qs=qs: qs)
    d = G.decide([4, 5, 6], 2)
    ok = (d["gpus"] == eg and d["max_running"] == emr)
    fails += (not ok)
    print(("PASS" if ok else "FAIL"), name, "->", d["gpus"], d["max_running"], "" if ok else f"(expected {eg}, {emr})", "; ".join(d["reasons"]))
print("ALL_PASS" if fails == 0 else f"{fails} FAILURES")
