"""Exact actual-shape and recorded-history audit; no publisher execution."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import ast
import hashlib
import json
import re
import shlex
import sys
import time

sys.set_int_max_str_digits(0)
B = Path(__file__).resolve().parents[1]
R = B.parent
start = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
inputs, checks = {}, []


def read(p, h=None):
    digest = sha(p)
    assert h is None or h == digest, (p, h, digest)
    inputs[str(p)] = digest
    return json.loads(p.read_text())


def check(label, condition):
    assert condition, label
    checks.append(label)


manifest = read(B / "data/manifest.json")
check("proof binding", sha(B / "PROOF.md") == manifest["proof_sha256"])
for name, row in manifest["inputs"].items():
    check("input " + name, sha(B / name) == row["sha256"])
    inputs[str(B / name)] = row["sha256"]
a = read(B / "data/candidate024.json",
         "3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d")
quot = read(B / "data/quotient013.json",
            "c0d3536ea961908a8a4d251054192bad0b5b2534435e3c8224fe0424bda5f7fe")
parent = read(R / "higher_mode_rank_audit/data/parent016.json",
              "a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42")
old = read(B / "data/old_basis.json")
rank = read(B / "source/T4_prior_rank.json")
check("rank theorem", rank["potential_dimension"] == rank["density_dimension"] == 2426
      and rank["verdict"].startswith("CONFIRMED"))
for path, h in rank["inputs"].items():
    check("rank dependency " + path, sha(Path(path)) == h)
    inputs[path] = h
shape = lambda g: (int(g["j"]), int(g["m"]), tuple(g["spec"]))
actual = list(map(shape, a["generators"]))
base = list(map(shape, quot["generators"]))
extra = [(j, m, ("legqs", 0, n, 4, 25))
         for j in (1, 2, 3) for m in range(9, 16) for n in range(12)]
check("all2174 actual shapes",
      actual == list(map(shape, parent["generators"])) == base + extra)
check("old1922 basis set", len(base) == len(set(base)) == 1922
      and set(base) == set(map(shape, old["generators"])))
check("distinct actual shapes", len(actual) == len(set(actual)) == 2174)
c = Q(a["cl_exact"])
check("exact common c", c == Q(parent["cl_exact"]) == Q(quot["cl_exact"])
      == Q(4076476460239181, 2251799813685248))
check("rational coefficients", all(Q(g["coef"]).denominator > 0 for g in a["generators"]))
rows = lambda d: [(1, k) if isinstance(k, int) else tuple(k)
                  for k in d["meta"]["pair_k"]]
first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 24, 32, 48, 64, 96,
         128, 192, 256, 384, 512, 768, 1024, 1536, 2048, 3072, 4096]
objective = [(1, k) for k in first] + [
    (n, (n - 1) // 2 + s) for n in range(3, 18, 2) for s in (0, 8, 32, 128, 512)]
check("same67 analytic rows", rows(a) == rows(parent) == objective
      and len(objective) == len(set(objective)) == 67)


def launch(name):
    text = (B / "source" / name).read_text()
    tag = re.search(r"^TAG=([^\s]+)$", text, re.M).group(1)
    calls = []
    for line in text.splitlines():
        if line.startswith("taskset ") and "run_quot.py" in shlex.split(line):
            words = shlex.split(line.replace("${TAG}", tag).replace("$TAG", tag))
            calls.append(words[words.index("run_quot.py") + 1:])
    assert len(calls) == 1
    return text, calls[0]


newtext, newcall = launch("N1_chain024.sh")
oldtext, oldcall = launch("N1_chain016.sh")
meta = a["meta"]
check("same input path", newcall[0] == oldcall[0]
      and Path(newcall[0]).name == meta["parent_json"])
for i in [1, 2, 4, 6, 7, 8, 9, 10]:
    check("same launch parameter " + str(i), newcall[i] == oldcall[i])
check("middle order changes16to32", int(newcall[5]) == meta["middle_order"] == 32
      and int(oldcall[5]) == parent["meta"]["middle_order"] == 16)
check("backend also changed", "IPM_DEVICE=cuda" in newtext and "IPM_DEVICE=cpu" in oldtext)
for i, key, value in [(1, "angular_midpoint", 180), (2, "steps", 12)]:
    check(key, int(newcall[i]) == meta[key] == value)
for i, key, value in [(6, "wlog", 26214400), (7, "wkap", 3000000), (8, "wpair", 10**12)]:
    check(key, Q(newcall[i]) == Q(str(meta[key])) == value)
check("no hidden held-in block", meta["n_heldin_rows"] == 0 and meta["wpair_heldin"] is None)
check("added scale metadata", meta["added_legqs"] == "1,2,3:9:15:25:12"
      and meta["tag"] == newcall[3] and meta["pair_mode"] == newcall[10] == "penalty")
logged = (B / "source/N1_024.out").read_text()
iterations = [(int(i), flag) for i, flag in re.findall(
    r"^it\s+(\d+) obj [^\n]*? (ACC|rej) ", logged, re.M)]
check("12 attempted 5accepted 7rejected",
      [i for i, flag in iterations] == list(range(1, 13))
      and sum(flag == "ACC" for i, flag in iterations) == 5)
check("log raw binding", sha(B / "data/candidate024.json") in logged
      and "generators 2174" in logged
      and "pair rows 67 weight 1000000000000.0" in logged
      and "middle 32" in logged and "per-row weights:" not in logged)
source = (B / "source/N1_run_quot.py").read_text()
ast.parse(source)
check("zero addition then projection", source.index("np.zeros(added)")
      < source.index("a_start = prob.taylor_project(a0, iters=8)"))
check("row propagation", "pair_k=PAIRK" in source and "WLIST = " in source
      and "max(5-m, 0)" in source)
beforepath = R / "candidate021_shapes/source/N1_run_quot020.py"
inputs[str(beforepath)] = sha(beforepath)
parts = []
for text in (beforepath.read_text(), source):
    tree = ast.parse(text)
    parsers = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_parse"]
    assigns = [n for n in ast.walk(tree) if isinstance(n, ast.Assign)
               and any(isinstance(t, ast.Name) and t.id == "PAIRK" for t in n.targets)]
    assert len(parsers) == len(assigns) == 1
    parts.append((ast.dump(parsers[0], include_attributes=False),
                  ast.dump(assigns[0], include_attributes=False)))
check("unchanged analytic row parser", parts[0] == parts[1])
held = (B / "source/N1_HELDOUT_024.md").read_bytes()
heldhash = hashlib.sha256(held).hexdigest()
oldhash = "58586004ad6ae0d0bf1545de2afbaa2f4643170e9d86334b59eda032eb02f4f5"
check("actual heldout hash", heldhash == "e171c051207448d35c53b44567b45c3699ed54de3349fb9e7402e06755fc0fab")
check("single heading occurrence", held.count(b"Objective rows (67):") == 1)
reconstruction = held.replace(b"Objective rows (67):", b"Objective rows (81? no: 67):")
check("exact earlier hash reconstructed", hashlib.sha256(reconstruction).hexdigest() == oldhash)
reconpath = B / "verification/RECONSTRUCTED_heldout.txt"
reconpath.write_bytes(reconstruction)
pairpattern = rb"(?<![\d:])(\d+):(\d+)(?![\d:])"
probes = [tuple(map(int, pair)) for pair in re.findall(pairpattern, held.split(b"HELD OUT")[1].split(b"Start:")[0])]
reg = read(B / "source/register.json")
expectedprobes = [tuple(pair) for pair in reg["pairs"]] + [
    (n, (n - 1) // 2 + s) for n in range(19, 32, 2) for s in (0, 8, 32, 128, 512)]
check("all60 probes", probes == expectedprobes and len(probes) == len(set(probes)) == 60)
check("reconstruction preserves probe bytes",
      held.split(b"HELD OUT")[1] == reconstruction.split(b"HELD OUT")[1])
check("analytic outside span", all(n > 17 and n % 2 and k >= (n - 1) // 2 for n, k in probes))
index = (B / "source/N1_INDEX.md").read_text()
line = [line for line in index.splitlines() if line.startswith("C1-N1-024-rulem32-legqs25 |")]
check("index historical label defects", len(line) == 1 and oldhash in line[0]
      and "LOSS (MID 16)" in line[0] and "Optimizer report (MID 16)" in line[0])
smtext = (B / "source/snapshot_manifest.json").read_text()
check("neither heldout hash in manifest", oldhash not in smtext and heldhash not in smtext)
peer = read(B / "source/N4_result.json")
check("peer actual shape and history comparisons",
      peer["raw_sha256"] == sha(B / "data/candidate024.json")
      and peer["potential_dimension"] == peer["density_dimension"] == 2174
      and peer["objective_rows"] == [list(row) for row in objective]
      and peer["iterations"] == [{"i": i, "flag": flag} for i, flag in iterations]
      and peer["current_heldout_sha256"] == heldhash)
check("public register before recorded launch",
      datetime.fromisoformat(reg["utc"]) < datetime.fromisoformat(peer["publisher_recorded_launch_utc"]))
for path in (B / "PROOF.md", Path(__file__)):
    inputs[str(path)] = sha(path)
out = {
    "utc": datetime.now(timezone.utc).isoformat(), "elapsed_seconds": time.monotonic() - start,
    "inputs": inputs, "checks": checks, "check_count": len(checks),
    "raw_sha256": sha(B / "data/candidate024.json"),
    "potential_dimension": 2174, "density_dimension": 2174,
    "exact_objective_rows": objective, "outside_analytic_span": probes,
    "iterations": iterations, "attempted": 12, "accepted": 5, "rejected": 7,
    "current_heldout_sha256": heldhash, "reconstructed_sha256": oldhash,
    "publisher_code_executed": False,
    "scope": "Actual024, parent016 shape and launch comparison, exact013 quotient; no earlier optimizer history or independently witnessed09:13 save times",
    "verdict": "CONFIRMED actual2174-dimensional spaces and67-row analytic span; CONFIRMED exact heldout hash reconstruction; REFUTED two MID16 index labels and single-variable comparison"
}
with (B / "verification/result.json").open("x") as stream:
    json.dump(out, stream, indent=2)
    stream.write("\n")
print(out["utc"], len(checks), out["elapsed_seconds"], sha(B / "verification/result.json"))
