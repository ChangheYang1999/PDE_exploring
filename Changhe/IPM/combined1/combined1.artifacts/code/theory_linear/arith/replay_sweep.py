"""Replay of the README commands in a mirror tree, compared with the distributed outputs.

Why a mirror: several results files record their run time (keys elapsed, elapsed_s, elapsed_seconds, seconds, utc,
'lane rerun utc'), and three scripts assert the sha256 of upstream results (data/family_ceilings_exact_results.json in
h18_item2_check.py, h18_wu_sharp.py, review_t4_459.py; data/h18_item2_check_results.json in h18_wu_sampling.py,
h18_wu_sharp.py). A rerun of an upstream script in place changes that hash, so the downstream assertion then fails
although nothing of substance changed. The replay protocol is therefore:
  1. before each script, the mirror's arith/, data/ and logs/ are reset to the distributed files (extra files
     removed);
  2. the script runs in the mirror as in its README row (no optional flags), stdout to a replay log, stderr to a
     separate file (the README commands differ in whether they capture stderr; warnings are not results);
  3. its exit code and PASS/FAIL line counts are compared with the distributed log logs/<name>.log, and every data/
     file it rewrote is compared with the distributed one as JSON with the timing keys above removed (exact
     equality of everything else; files that are not JSON are compared byte for byte).
So each upstream output is shown to reproduce up to timing fields, and each downstream script runs on the distributed
upstream files whose hashes it pins. The report also compares each replay log with the distributed log line by line,
after masking run times (numbers followed by s or seconds, clock times hh:mm:ss, elapsed fields) and dropping the
date(1) and 'EXIT n' lines that some original wrappers appended; the number of
differing lines and the first few are recorded, and every nonzero count is classified by hand in the README row.

Mirror: MIRROR/r6/c1-t2/artifacts is a copy of artifacts/; every other entry of the lane (scratch/ included, which
holds the sha256-pinned lane copies read by some scripts), every other entry of r6 and every sibling of r6 is a symlink
to the real one (read only use; no script writes outside its artifacts/ tree, checked by grep before the first run).
Scripts that address other lanes by absolute path read the real files, as in the original runs. The README setup step
is applied in the mirror once (gunzip -k of the compressed inputs, then sha256sum -c data/COMPRESSED_INPUTS.sha256),
and these uncompressed copies are kept through the resets.

Usage, from artifacts/:
  python3 -B -u arith/replay_sweep.py MIRROR run SCRIPT.py [SCRIPT.py ...]   (appends to MIRROR/replay_results.jsonl)
  python3 -B -u arith/replay_sweep.py MIRROR report                           (writes data/replay_sweep_results.json)
Each run call must stay below 10 min; the sweep is split into batches by the recorded durations.
Not replayed: arith/weighted_weak_sharp.py (4405 s) and arith/t4_094_review.py (5427 s), each longer than one 10 min
command, arith/qa_hash_abbrev_check.py (its output depends on the files present in the lanes at run time; its
README row says so), and this script itself.
"""
import filecmp
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ART = Path(__file__).resolve().parents[1]
LANE = ART.parent
R6 = LANE.parent
BASE = R6.parent
TIMING = {"elapsed", "elapsed_s", "elapsed_seconds", "seconds", "utc", "lane rerun utc"}
PY = "python3"
if len(sys.argv) < 3 or sys.argv[2] not in ("run", "report"):
    sys.exit("usage: replay_sweep.py MIRROR run SCRIPT.py [...] | replay_sweep.py MIRROR report")
MIR = Path(sys.argv[1]).resolve()
MART = MIR / R6.name / LANE.name / ART.name
RES = MIR / "replay_results.jsonl"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def build_mirror():
    if MART.exists():
        return
    for p in BASE.iterdir():
        if p.name != R6.name:
            (MIR / p.name).parent.mkdir(parents=True, exist_ok=True)
            os.symlink(p, MIR / p.name)
    for p in R6.iterdir():
        if p.name != LANE.name:
            (MIR / R6.name).mkdir(parents=True, exist_ok=True)
            os.symlink(p, MIR / R6.name / p.name)
    for p in LANE.iterdir():
        if p.name != ART.name:
            (MIR / R6.name / LANE.name).mkdir(parents=True, exist_ok=True)
            os.symlink(p, MIR / R6.name / LANE.name / p.name)
    shutil.copytree(ART, MART, symlinks=True)
    gz = sorted(str(p.relative_to(MART)) for p in (MART / "data").rglob("*.json.gz"))
    subprocess.run(["gunzip", "-k"] + gz, cwd=MART, check=True)
    subprocess.run(["sha256sum", "--quiet", "-c", "data/COMPRESSED_INPUTS.sha256"], cwd=MART, check=True)


KEEP = {Path(l.split()[1]).relative_to("data") for l in (ART / "data/COMPRESSED_INPUTS.sha256").read_text().splitlines()}


def reset(sub):
    """make MART/sub equal to ART/sub: copy changed or missing files, remove extra files"""
    real, mir = ART / sub, MART / sub
    rel_real = {p.relative_to(real) for p in real.rglob("*") if p.is_file()}
    for p in list(mir.rglob("*")):
        if p.is_file() and p.relative_to(mir) not in rel_real and not (sub == "data" and p.relative_to(mir) in KEEP):
            p.unlink()
    for r in rel_real:
        a, b = real / r, mir / r
        if not b.exists() or not filecmp.cmp(a, b, shallow=False):
            b.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(a, b)


def strip(o):
    if isinstance(o, dict):
        return {k: strip(v) for k, v in o.items() if k not in TIMING}
    if isinstance(o, list):
        return [strip(v) for v in o]
    return o


def diffs(a, b, path="", out=None):
    out = [] if out is None else out
    if len(out) >= 8:
        return out
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b), key=str):
            if k not in a or k not in b:
                out.append(path + "/" + str(k) + (" missing in replay" if k not in b else " new in replay"))
            else:
                diffs(a[k], b[k], path + "/" + str(k), out)
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for i, (x, y) in enumerate(zip(a, b)):
            diffs(x, y, path + "[%d]" % i, out)
    elif a != b:
        out.append("%s: %s -> %s" % (path, str(a)[:70], str(b)[:70]))
    return out


MASKS = [(re.compile(r"\d{4}-\d\d-\d\dT\d\d:\d\d(:\d\d(\.\d+)?)?(\+00:00|Z)?"), "<UTC>"),
         (re.compile(r"\b\d\d:\d\d:\d\d(\.\d+)?Z?"), "<UTC>"),
         (re.compile(r"(elapsed|time|took|wall)[ =:a-z]*[\d.]+(e[-+]?\d+)?"), r"\1 <T>"),
         (re.compile(r"\b[\d.]+(e[-+]?\d+)? ?(s|sec|seconds)\b"), "<T> s")]


WRAP = re.compile(r"^(EXIT -?\d+|\w{3} \w{3} +\d+ \d\d:\d\d:\d\d \w+ \d{4})$")


def masked(text):
    out = []
    for line in text.splitlines():
        if WRAP.match(line.strip()):
            continue
        for rx, rep in MASKS:
            line = rx.sub(rep, line)
        out.append(line)
    return out


def logcmp(a, b):
    import difflib
    d = [l for l in difflib.unified_diff(masked(a), masked(b), lineterm="", n=0)
         if (l.startswith("-") or l.startswith("+")) and not l.startswith(("---", "+++"))]
    return len(d), d[:6]


def counts(text):
    return (sum(1 for l in text.splitlines() if l.lstrip().startswith("PASS")),
            sum(1 for l in text.splitlines() if l.lstrip().startswith("FAIL")))


if sys.argv[2] == "run":
    build_mirror()
    (MIR / "replay_logs").mkdir(exist_ok=True)
    for name in sys.argv[3:]:
        stem = Path(name).stem
        reset("arith")
        reset("data")
        reset("logs")
        before = {p.relative_to(MART / "data"): sha(p) for p in (MART / "data").rglob("*") if p.is_file()}
        log = MIR / "replay_logs" / (stem + ".log")
        t0 = time.time()
        start = time.strftime("%H:%M:%SZ", time.gmtime())
        env = dict(os.environ, OMP_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
        with open(log, "w") as fh, open(log.with_suffix(".err"), "w") as fe:
            rc = subprocess.run(["timeout", "540", PY, "-B", "-u", "arith/" + stem + ".py"], cwd=MART, env=env,
                                stdout=fh, stderr=fe).returncode
        el = time.time() - t0
        fresh = log.read_text(errors="replace")
        dist_log = ART / "logs" / (stem + ".log")
        dist = dist_log.read_text(errors="replace") if dist_log.exists() else None
        rec = {"script": stem + ".py", "start": start, "elapsed_s": round(el, 1), "exit": rc,
               "stderr_lines": len(log.with_suffix(".err").read_text(errors="replace").splitlines()),
               "pass_fail_replay": counts(fresh), "pass_fail_distributed": counts(dist) if dist is not None else None,
               "data": {}}
        for p in (MART / "data").rglob("*"):
            if not p.is_file():
                continue
            r = p.relative_to(MART / "data")
            if before.get(r) == sha(p):
                continue
            real = ART / "data" / r
            if not real.exists():
                rec["data"][str(r)] = "new file (not distributed)"
                continue
            try:
                a, b = strip(json.loads(real.read_text())), strip(json.loads(p.read_text()))
                d = diffs(a, b)
                rec["data"][str(r)] = "equal up to timing keys" if not d else {"differs": d}
            except ValueError:
                rec["data"][str(r)] = "differs (not JSON, bytes differ)"
        rec["ok"] = (rc == 0 and rec["pass_fail_replay"][1] == 0
                     and (dist is None or rec["pass_fail_replay"] == rec["pass_fail_distributed"])
                     and all(v == "equal up to timing keys" for v in rec["data"].values()))
        with open(RES, "a") as fh:
            fh.write(json.dumps(rec) + "\n")
        print("%-28s exit %3d  %6.1f s  PASS/FAIL replay %s distributed %s  data %s  -> %s"
              % (stem, rc, el, rec["pass_fail_replay"], rec["pass_fail_distributed"],
                 {k: (v if isinstance(v, str) else "DIFFERS") for k, v in rec["data"].items()} or "-",
                 "OK" if rec["ok"] else "CHECK"), flush=True)
        for k, v in rec["data"].items():
            if not isinstance(v, str):
                for line in v["differs"]:
                    print("      %s %s" % (k, line))
    reset("data")
    reset("logs")
else:
    recs = {}
    for line in RES.read_text().splitlines():
        r = json.loads(line)
        recs[r["script"]] = r                      # the last replay of each script counts
    rows = [l for l in (ART / "README.md").read_text().splitlines() if l.startswith("|")]
    listed = []
    for l in rows:
        for m in re.findall(r"python3 [-Bu ]*arith/([\w]+\.py)", l.split("|")[1]):
            if m not in listed:
                listed.append(m)
    skipped = ["weighted_weak_sharp.py", "t4_094_review.py", "qa_hash_abbrev_check.py", "replay_sweep.py"]
    missing = [s for s in listed if s not in recs and s not in skipped]
    for s_, r in recs.items():
        a, b = ART / "logs" / (Path(s_).stem + ".log"), MIR / "replay_logs" / (Path(s_).stem + ".log")
        if a.exists() and b.exists():
            r["log_lines_differing_after_masking"], r["log_first_differences"] = logcmp(
                a.read_text(errors="replace"), b.read_text(errors="replace"))
        else:
            r["log_lines_differing_after_masking"], r["log_first_differences"] = None, ["no distributed log"]
    out = {"replayed": len(recs), "ok": sorted(s for s, r in recs.items() if r["ok"]),
           "check": {s: r for s, r in recs.items() if not r["ok"]}, "not_replayed_by_design": skipped,
           "listed_in_README_but_not_replayed": missing, "records": recs}
    (ART / "data/replay_sweep_results.json").write_text(json.dumps(out, indent=1) + "\n")
    print("README scripts: %d; replayed: %d; OK: %d; to check: %d (%s); not replayed by design: %s; missing: %s"
          % (len(listed), len(recs), len(out["ok"]), len(out["check"]), ", ".join(sorted(out["check"])),
             ", ".join(skipped), ", ".join(missing) or "none"))
    for s in sorted(recs):
        r = recs[s]
        print("  %-30s %s exit %d, %s s, PASS/FAIL %s (distributed %s), log lines differing %s"
              % (s, "OK   " if r["ok"] else "CHECK", r["exit"], r["elapsed_s"], r["pass_fail_replay"],
                 r["pass_fail_distributed"], r["log_lines_differing_after_masking"]))
        for l in (r["log_first_differences"] if r["log_lines_differing_after_masking"] else []):
            print("      " + l[:150])
