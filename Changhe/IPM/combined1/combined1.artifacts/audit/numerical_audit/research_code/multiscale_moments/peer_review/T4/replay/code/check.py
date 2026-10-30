"""Calibrate finite-panel certificates against independent elementary formulas."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import time
from flint import arb, ctx, fmpq as Q
from moments import integral, ar

BASE = Path(__file__).resolve().parents[1]
start = time.monotonic()
source = BASE / "data/calibration.json"
data = json.loads(source.read_text())
ctx.prec = data["precision_bits"]


def exact_formula(case):
    b = Q(case["b"])
    factors = [(Q(a), m) for a, m in case["factors"]]
    form = case["formula"]
    if form == "polynomial":
        return sum((ar(Q(p) / (b + k + 1)) for k, p in enumerate(case["P"])), arb(0))
    a, m = factors[0]
    aa = ar(a)
    if form == "single_integer":
        return (1 + aa).log() / aa if m == 1 else ar((1 - (1 + a)**(1-m)) / (a*(m-1)))
    if form == "half_minus":
        return 2 * aa.sqrt().atan() / aa.sqrt()
    if form == "half_plus":
        return 2 * (1 - aa.sqrt().atan() / aa.sqrt()) / aa
    d = ar(factors[1][0])
    if form == "double_log":
        return ((1 + d).log() - (1 + aa).log()) / (d - aa)
    assert form == "double_half"
    return 2 * (d.sqrt() * d.sqrt().atan() - aa.sqrt() * aa.sqrt().atan()) / (d - aa)


rows = []
for case in data["cases"]:
    elapsed = time.monotonic()
    result = integral(case["b"], case["P"], case["factors"], Q(data["tail_tolerance"]))
    reference = exact_formula(case)
    overlaps = result["lower"] <= reference.upper() and result["upper"] >= reference.lower()
    assert overlaps, case["id"]
    width = result["upper"] - result["lower"]
    assert width >= 0
    rows.append({
        "id": case["id"], "lower": result["lower"].str(100),
        "upper": result["upper"].str(100), "width": width.str(30),
        "reference": reference.str(100), "overlaps": bool(overlaps),
        "panels": result["panels"], "elapsed_seconds": time.monotonic() - elapsed,
    })
    print(case["id"], len(result["panels"]), "panels", "width", width.str(12),
          "seconds", rows[-1]["elapsed_seconds"], flush=True)

inputs = [source, BASE / "PROOF.md", Path(__file__), BASE / "code/moments.py"]
out = {
    "utc": datetime.now(timezone.utc).isoformat(), "precision_bits": ctx.prec,
    "inputs": {str(p.relative_to(BASE)): sha256(p.read_bytes()).hexdigest() for p in inputs},
    "rows": rows, "elapsed_seconds": time.monotonic() - start,
    "status": "Elementary calibration passed; theorem and candidate applications OPEN peer review",
}
target = BASE / "verification/calibration.json"
target.parent.mkdir(exist_ok=True)
assert not target.exists()
target.write_text(json.dumps(out, indent=2) + "\n")
print("DONE", len(rows), out["elapsed_seconds"], flush=True)
