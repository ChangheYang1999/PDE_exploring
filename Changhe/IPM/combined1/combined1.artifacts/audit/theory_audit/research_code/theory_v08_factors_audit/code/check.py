"""Check proposed factors against containing accepted sources, never peer code."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import ast
import hashlib
import json
import time
from flint import arb, ctx

B = Path(__file__).resolve().parents[1]
start = time.monotonic()
ctx.prec = 512
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda name: json.loads((B / "source" / name).read_text())
checks = []


def require(name, test, value=None):
    assert bool(test), (name, str(value))
    checks.append({"claim": name, "value": None if value is None else str(value)})


def ar(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


manifest = json.loads((B / "data/manifest.json").read_text())
for row in manifest:
    require("binding " + row["local"], sha(B / row["local"]) == row["sha256"])
tree = ast.parse((B / "source/T1_factors.py").read_text())
literal = next(ast.literal_eval(n.value) for n in tree.body
               if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name)
               and t.id == "ROWS" for t in n.targets))
rows = json.loads((B / "data/proposed_rows.json").read_text())
require("all 24 literal rows copied", [list(r) for r in literal] == rows and len(rows) == 24)
mapping = {r[0].split()[0]: r for r in rows}
norms = {r["label"]: r for r in read("norms.json")["instances"]}
weak = read("weak.json")
require("distance exact floor", Q(weak["strict_lower_exact"]) == Q(mapping["D1"][1]))
require("distance full ball above floor", arb(weak["radius"]) > ar(mapping["D1"][1]))
for key in ["D2", "D3", "D4", "D5"]:
    require(key + " same distance", Q(mapping[key][1]) == Q(mapping["D1"][1]))
sharp = {r["name"]: r for r in read("sharp.json")["rows"]}
for name, key in [("sharpw", "D2"), ("sharp", "D3")]:
    r = sharp[name]
    mu, C = ar(r["mu"]), ar(r["C"])
    ceiling = (2 * mu / 3) * (mu / (3 * C)).sqrt() / (ar("8/5") * arb(r["weights"][1]).sqrt())
    require(key + " containing family ceiling", ceiling < ar(mapping[key][3]), ceiling)
require("D4 exact fixed radius", Q(mapping["D4"][3]) == Q(sharp["sharpw"]["r"]) / 1024)
old = read("draft34_parameters.json")
require("D1 accepted TB ceiling", Q(mapping["D1"][3]) == Q(old["ceilings"][0]))
require("D5 accepted graded ceiling", Q(mapping["D5"][3]) == Q(old["ceilings"][2]))

for key, name in [("S1", "sharpw"), ("S2", "sharp")]:
    require(key + " exact threshold", Q(mapping[key][3]) == Q(norms[name]["threshold_exact"]))
require("S1 sharpw lower", arb(norms["sharpw"]["lower_comparison"]["ball"]) > ar(mapping["S1"][1]))
require("S2 proposed bound refuted by sharp upper",
        arb(norms["sharp"]["upper_comparison"]["ball"]) < ar(mapping["S2"][1]))
corrected_s2 = Q("516.9717852723")
require("S2 corrected lower", arb(norms["sharp"]["lower_comparison"]["ball"]) > ar(corrected_s2))
require("S2 sharp displayed upper", arb(norms["sharp"]["upper_comparison"]["ball"]) < ar("517.5527701453"))
require("norm weights genuinely differ",
        (norms["sharp"]["w1"], norms["sharp"]["w2"], norms["sharp"]["s_exact"])
        == (2**14, 2**18, "1/7744")
        and (norms["sharpw"]["w1"], norms["sharpw"]["w2"], norms["sharpw"]["s_exact"])
        == (2**15, 2**20, "1/5184"))

origin = read("origin.json")
require("O1 all seven cells present", len(origin["rows"]) == 7)
for k, r in enumerate(origin["rows"]):
    require("O1 ratio cell " + str(k), arb(r["ratio"]) > ar(mapping["O1"][1]))

c = Q("4076476460239181/2251799813685248")
q = 1 / c - 4
Emin = (-q - 1) / (2 * (-q) * (-q - 3))
uni = read("universal.json")
require("universal exact exponent", q == Q(uni["q"]))
require("universal exact coefficient", Emin == Q(uni["Etest_exact"]), Emin)
outer = read("outer.json")
profile = read("profile.json")
average = read("average.json")
o = next(r for r in outer["rows"] if r["candidate"] == "007")
p = next(r for r in profile["rows"] if r["candidate"] == "007")
a = next(r for r in average["rows"] if r["candidate"] == "007")
targets = ["fixed_sharpw_ball", "sharpw_rounded_ceiling",
           "TB_sharp_rounded_ceiling", "original_graded_ceiling"]
for key, target in zip(["U1", "U2", "U3", "U4"], targets):
    require(key + " rational universal lower", Emin > Q(mapping[key][1]))
    require(key + " target upper", arb(o["targets"][target]["K"]) < ar(mapping[key][3]))

for key, target in [("P1", targets[3]), ("P2", targets[3]),
                    ("P3", targets[0]), ("P4", targets[1]), ("P5", targets[2])]:
    require(key + " critical coefficient upper",
            arb(p["targets"][target]["critical_E"]) < ar(mapping[key][3]))
require("P1 chosen coefficient", Q(mapping["P1"][1]) == Q(93, 250))
for key in ["P3", "P4", "P5"]:
    require(key + " chosen coefficient", Q(mapping[key][1]) == Q(583, 1000))
require("P2 angular-family lower", arb(p["coefficient_lower"]) > ar(mapping["P2"][1]))
for key, target in zip(["R1", "R2", "R3"], targets[:3]):
    require(key + " remainder majorant lower",
            arb(p["targets"][target]["J_over_H_lower"]) > ar(mapping[key][1]))
    room = arb(p["targets"][target]["room_Phi"])
    require(key + " positive room upper", room > 0 and room < ar(mapping[key][3]), room)
require("graded room negative", arb(p["targets"][targets[3]]["room_Phi"]) < 0)
for target in targets:
    require("A1 radial floor " + target,
            arb(a["targets"][target]["averaged_floor_at_beta"]) > ar(mapping["A1"][1]))
require("A1 target upper", arb(o["targets"][targets[0]]["K"]) < ar(mapping["A1"][3]))
lam = arb(1) / 2 + 5 * arb(2) ** ar(1 - q)
require("current bracket source overlap", lam.overlaps(arb(outer["lambda"])))
for key, target in zip(["K1", "K2", "K3"], targets[:3]):
    require(key + " current bracket lower", lam > ar(mapping[key][1]))
    threshold = arb(o["targets"][target]["thresholds"]["93/250"]["fallback"])
    require(key + " hypothetical threshold upper", threshold < ar(mapping[key][3]), threshold)

scopes = {
    "D": "necessary weak-distance obstruction to specified correction balls",
    "S": "failure of sufficient norm-smallness test",
    "O": "specified conditional origin inverse test",
    "U": "universal compensated-velocity class with stated CI and tail inputs",
    "P": "chosen profile coefficient; P2 alone is a lower obstruction in N/G angular family",
    "R": "specified error-majorant formula versus positive remaining coefficient room",
    "A": "allowed T4-410 and universal-fallback Green averages",
    "K": "current outer-tail bracket with Eprof=93/250 and allowed relaxed fallback",
}
factors = []
for label, pn, ps, tn, ts in rows:
    key = label.split()[0]
    p0, t0 = Q(pn), Q(tn)
    original_ratio = p0 / t0
    numerator = corrected_s2 if key == "S2" else p0
    ratio = numerator / t0
    digits = 4 if ratio < 100 else 2
    scale = 10**digits
    down = Q((ratio * scale).numerator // (ratio * scale).denominator, scale)
    require(key + " exact downward factor", 1 < down <= ratio, ratio)
    factors.append({"row": key, "label": label, "numerator_exact": str(numerator),
                    "threshold_exact": str(t0), "ratio_exact": str(ratio),
                    "downward_factor_exact": str(down), "decimal_places": digits,
                    "original_ratio_exact": str(original_ratio),
                    "source_assertion": "REFUTED original numerator; corrected" if key == "S2" else "CONFIRMED in stated scope",
                    "scope": scopes[key[0]]})
require("S2 corrected exact quotient", corrected_s2 / Q(mapping["S2"][3]) == Q(5169717852723, 762190))
out = {"utc": datetime.now(timezone.utc).isoformat(), "elapsed_s": time.monotonic() - start,
       "precision_bits": ctx.prec, "check_count": len(checks), "checks": checks, "rows": factors,
       "proof_sha256": sha(B / "PROOF.md"), "code_sha256": sha(Path(__file__)),
       "manifest_sha256": sha(B / "data/manifest.json"),
       "parameters_sha256": sha(B / "data/proposed_rows.json"),
       "foreign_code_executed": False, "heavy_integrations_repeated": False,
       "verdict": "REFUTED S2 norm lower assertion; CONFIRMED corrected 24 factors under separate stated scopes"}
with (B / "verification/result.json").open("x") as f:
    json.dump(out, f, indent=2)
    f.write("\n")
print("PASS", len(checks), "checks", out["utc"], out["elapsed_s"])
for r in factors:
    print(r["row"], r["downward_factor_exact"], r["source_assertion"])
