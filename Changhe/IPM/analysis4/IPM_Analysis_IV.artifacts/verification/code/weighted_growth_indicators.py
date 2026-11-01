"""Finite second-difference diagnostics; no asymptotic model is inferred."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import factorial
import json
import sys
import time
from flint import arb, ctx

ctx.prec = 640
start = time.monotonic()
source = Path(sys.argv[1])
raw = source.read_bytes()
data = json.loads(raw)
root = source.parent
text = lambda x: x.str(32, radius=True)
log10 = arb(10).log()
N = data["maximum_order"]
lfact = {n: arb(factorial(n)).log() / log10 for n in range(N + 1)}
out = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "input_path": str(source),
    "input_sha256": sha256(raw).hexdigest(),
    "checkpoint_sha256": data["checkpoint_sha256"],
    "maximum_order": N,
    "precision_bits": 640,
    "definition": "sigma(n,h)=(L(n)-2L(n-h)+L(n-2h))/(log10(n!)-2log10((n-h)!)+log10((n-2h)!))",
    "interpretation": "Exactly sigma for the finite model norm_n=C*A^n*(n!)^sigma. Without that model this is only a finite statistic.",
    "weights": [],
}
for block in data["weights"]:
    rows = {row["n"]: row for row in block["rows"]}
    ratios = {n: arb(row["rho"]) for n, row in rows.items() if "rho" in row}
    winner = max(ratios, key=lambda n: float(ratios[n].mid()))
    assert all(ratios[winner] > val for n, val in ratios.items() if n != winner)
    stream_ratios = {n: arb(row["stream_over_density"]) for n, row in rows.items()}
    bwinner = max(stream_ratios, key=lambda n: float(stream_ratios[n].mid()))
    assert all(stream_ratios[bwinner] > val for n, val in stream_ratios.items() if n != bwinner)
    record = {
        "s": block["s"],
        "strict_maximum_rho_n": winner,
        "maximum_rho": text(ratios[winner]),
        "strict_maximum_stream_over_density_n": bwinner,
        "maximum_stream_over_density": text(stream_ratios[bwinner]),
        "indicators": [],
        "nine_order_increments": [],
        "late_ratios": [{"n": n, "rho": text(ratios[n])} for n in range(270, N + 1)],
    }
    for field in ["density", "stream"]:
        L = {n: arb(row[field + "_log10"]) for n, row in rows.items()}
        for h in [9, 18, 30]:
            for n in range(max(2 * h + 1, 100), N + 1):
                den = lfact[n] - 2 * lfact[n - h] + lfact[n - 2 * h]
                assert den > 0
                val = (L[n] - 2 * L[n - h] + L[n - 2 * h]) / den
                record["indicators"].append(
                    {"field": field, "n": n, "h": h, "finite_sigma": text(val)}
                )
        for n in range(100, N + 1):
            record["nine_order_increments"].append(
                {"field": field, "n": n, "increment": text((L[n] - L[n - 9]) / 9)}
            )
    out["weights"].append(record)
out["actual_elapsed_s"] = time.monotonic() - start
(root / "growth_indicators.json").write_text(json.dumps(out, indent=2) + "\n")
(root.parent / "sources/weighted_growth_indicators.py.txt").write_bytes(Path(__file__).read_bytes())
for block in out["weights"]:
    print(json.dumps({k: v for k, v in block.items() if k not in ["indicators", "nine_order_increments"]}))
    for field in ["density", "stream"]:
        print(json.dumps({"s": block["s"], "field": field, "selected_indicators": [
            row for row in block["indicators"]
            if row["field"] == field and row["h"] == 30 and row["n"] in [120, 150, 180, 210, 240, 270, N]
        ]}))
print(json.dumps({"actual_elapsed_s": out["actual_elapsed_s"]}))
