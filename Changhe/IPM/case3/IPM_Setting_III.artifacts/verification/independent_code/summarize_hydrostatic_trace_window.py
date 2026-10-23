"""Independent arithmetic postprocessing of previously computed whole-line inverses."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import re

r = Path("research/hydrostatic_trace_compatibility_diagnostic/verification/comparison")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
w = json.loads((r / "WINDOWS.json").read_text())
inputs = {s["tag"]: s for s in json.loads((r.parent / "INPUTS.json").read_text())["states"]}
checks = []


def check(name, ok):
    checks.append(dict(name=name, passed=bool(ok)))
    assert ok, name


def close(a, b, atol=1e-14):
    return abs(a - b) <= atol * max(1., abs(a), abs(b))


def slope(points):
    x, y = zip(*[(math.log(p["r"]), math.log(p["ratio"])) for p in points])
    xb, yb = math.fsum(x) / len(x), math.fsum(y) / len(y)
    s = math.fsum((a-xb)*(b-yb) for a, b in zip(x, y)) / math.fsum((a-xb)**2 for a in x)
    return s, math.exp(yb-s*xb)


producer = {}
tag = None
for line in (r / "producer_cp.txt").read_text().split("# near-axis window", 1)[1].splitlines():
    if line.startswith("hs"):
        tag = line.split()[0]
        producer[tag] = {}
    m = re.match(r"#   delta (\S+): (.*?)   log-log slope over 100 <= r <= 1e4: ([+-]?\S+), prefactor (\S+)", line)
    if m:
        producer[tag][float(m[1])] = dict(values=list(map(float, m[2].split())),
                                        slope=float(m[3]), prefactor=float(m[4]))
check("completed run", w["status"] == "DONE")
check("driver unchanged since evaluation", w["code_sha256"] == sha("independent_code/audit_hydrostatic_trace_window.py"))
out = dict(utc=datetime.now(timezone.utc).isoformat(), started_utc=w["started_utc"],
           finished_utc=w["finished_utc"], states=[], checks=checks,
           hashes={str(r / name): sha(r / name) for name in ["WINDOWS.json", "producer_cp.txt"]},
           code_sha256=sha(__file__), proof_sha256=sha(r.parent.parent / "WINDOW_SUMMARY_PROOF.md"))
text = [f"# Independent finite-window audit\n\n{out['utc']}. Hydrostatic diagnostics only. "
        "Finite samples and inverse refinements do not establish a global power law or an endpoint.\n"]
for state in w["states"]:
    tag = state["tag"]
    check(tag+" source hash", state["sha256"] == inputs[tag]["sha256"] == sha(inputs[tag]["file"]))
    check(tag+" four levels", len(state["levels"]) == 4)
    checked_slopes = []
    for i, level in enumerate(state["levels"]):
        check(f"{tag} level{i}96points", len(level["points"]) == 96)
        for j, p in enumerate(level["points"]):
            A = (state["c"] * p["x"] + p["V1"]) * p["gx"]
            B = (state["c"] * p["y"] + p["V2"]) * p["gy"]
            R, Nf = A+B-p["g"], abs(A)+abs(B)+abs(p["g"])
            check(f"{tag} L{i}point{j} residual", Nf > 0 and close(R, p["R"])
                  and close(Nf, p["Nf"]) and close(R/Nf, p["signed_ratio"])
                  and close(abs(R)/Nf, p["ratio"]))
        calculated = {}
        for item in level["slopes"]:
            pts = [p for p in level["points"] if p["delta"] == item["delta"] and 100 <= p["r"] <= 10000]
            check(f"{tag} L{i}delta{item['delta']}9radii", len(pts) == 9 and all(p["ratio"] > 0 for p in pts))
            s, a = slope(pts)
            check(f"{tag} L{i}delta{item['delta']}slope", close(s, item["slope"]) and close(a, item["prefactor"]))
            calculated[item["delta"]] = dict(slope=s, prefactor=a)
        checked_slopes.append(calculated)
    row = dict(tag=tag, sha256=state["sha256"], changes=[], deltas=[])
    for i, recorded in enumerate(state["refinement_changes"]):
        before, after = state["levels"][i]["points"], state["levels"][i+1]["points"]
        point_changes = []
        for a, b in zip(before, after):
            check(f"{tag} change{i}samepoint", all(a[k] == b[k] for k in ["delta","r","x","y","g","gx","gy","gxx"]))
            point_changes.append(dict(delta=a["delta"], r=a["r"],
                abs_signed_ratio_change=abs(a["signed_ratio"]-b["signed_ratio"]),
                relative_abs_ratio_change=abs(a["ratio"]-b["ratio"])/max(a["ratio"], b["ratio"]),
                velocity_change=max(abs(a[k]-b[k]) for k in ["V1","V2"])))
        m = max(p["abs_signed_ratio_change"] for p in point_changes)
        v = max(p["velocity_change"] for p in point_changes)
        check(tag+f" change{i}recorded maxima", close(m, recorded["max_absolute_ratio_change"])
              and close(v, recorded["max_velocity_change"]))
        row["changes"].append(dict(from_level=i, to_level=i+1, max_signed_ratio_change=m,
                                   max_velocity_change=v, points=point_changes))
    text += [f"\n## {tag}\n\nCoefficient SHA256 `{state['sha256']}`. "
             f"Four full-line quadratures; last maximum ratio change "
             f"{row['changes'][-1]['max_signed_ratio_change']:.6g}; "
             f"last velocity change {row['changes'][-1]['max_velocity_change']:.6g}.\n",
             "| delta | independent slope100..1e4 | last slope change | producer slope | ratio at1e4 | ratio at1e8 |\n"
             "|---|---:|---:|---:|---:|---:|\n"]
    for delta, calc in checked_slopes[-1].items():
        pts = [p for p in state["levels"][-1]["points"] if p["delta"] == delta]
        d = dict(delta=delta, slope=calc["slope"], prefactor=calc["prefactor"],
                 slope_changes=[checked_slopes[i+1][delta]["slope"]-checked_slopes[i][delta]["slope"] for i in range(3)],
                 points=pts)
        if delta in producer[tag]:
            prod = producer[tag][delta]
            first = [p for p in pts if p["r"] <= 10000]
            check(tag+f"delta{delta}producer13", len(prod["values"]) == len(first) == 13)
            d["producer"] = prod
            d["producer_slope_difference"] = d["slope"]-prod["slope"]
            d["printed_point_comparison"] = [
                dict(r=p["r"], own=p["ratio"], printed=v, difference=p["ratio"]-v,
                     relative_to_printed=(p["ratio"]-v)/v,
                     within_two_significant_digit_rounding=abs(p["ratio"]-v) <= 0.50001 * 10**(math.floor(math.log10(v))-1))
                for p, v in zip(first, prod["values"])]
        row["deltas"].append(d)
        p4 = next(p for p in pts if p["r"] == 10000)
        p8 = next(p for p in pts if p["r"] == 1e8)
        text += [f"|{delta:g}|{d['slope']:.10g}|{d['slope_changes'][-1]:.4g}|"
                 f"{producer[tag][delta]['slope'] if delta in producer[tag] else 'not supplied'}|"
                 f"{p4['ratio']:.8g}|{p8['ratio']:.8g}|\n"]
    row["verdict"] = ("CONFIRMED_FINITE_OBSERVATIONS_WITH_UNRESOLVED_INVERSE_DIGITS"
                      if state["c"] == 2 else "CONFIRMED_FINITE_OBSERVATIONS")
    out["states"].append(row)
text += ["\nThe c=3 finite-window slopes are negative with last quadrature changes below4e-9. "
         "Several producer slopes disagree beyond printed rounding. The c=2 capped state has positive100..1e4 slopes "
         "at all six angles, but its delta=.03 slope moves by about.0356 at the last inverse refinement; "
         "digits there remain unresolved. All eighteen last-level ratios at1e8 are below their same-angle values "
         "at1e4, so the positive early-window c=2 fits fail to describe that later range. Detailed raw-point discrepancies, "
         "including near-zero amplification, are retained in WINDOW_SUMMARY.json. "
         "No trial-space nonconvergence theorem or primary-PDE endpoint follows.\n"]
check("later fall at every angle",
      all(next(p for p in d["points"] if p["r"] == 1e8)["ratio"]
          < next(p for p in d["points"] if p["r"] == 1e4)["ratio"]
          for s in out["states"] for d in s["deltas"]))
out["check_count"] = len(checks)
(r / "WINDOW_SUMMARY.json").write_text(json.dumps(out, indent=2)+"\n")
(r / "WINDOW_SUMMARY.md").write_text("".join(text))
(r / "WINDOW_VERDICT.md").write_text(f"{out['utc']}: {len(checks)} arithmetic/source checks PASS. "
    "Finite sampled trends CONFIRMED; exact producer slopes are not all reproduced. "
    "Some c=2 inverse digits OPEN. No global far-field law or PDE endpoint established.\n")
print(len(checks), "PASS")
