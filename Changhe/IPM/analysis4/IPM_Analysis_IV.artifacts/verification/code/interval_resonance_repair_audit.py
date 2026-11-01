"""Regression audit of the corrected three-state interval resonance decision."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util
import json
import sys
sys.dont_write_bytecode = True
from flint import arb, fmpq

src = Path("../a4-num/code/ffcore.py")
blob = src.read_bytes()
digest = sha256(blob).hexdigest()
snapshot = Path("research/19_interval_resonance/sources") / ("ffcore_" + digest + ".py")
snapshot.write_bytes(blob)
spec = importlib.util.spec_from_file_location("audited_ffcore_repair", snapshot)
ff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ff)
R = ff.RingArb(256)
obj = ff.FarField(R, "2", ["1"])
assert obj.delta_exact == fmpq(1, 2)
rows = []
for label, a0, expected in [
    ("exact_zero", arb(0), "compatible"),
    ("ambiguous_zero", arb(0, "1e-30"), "open"),
    ("positive", arb(1), "incompatible"),
    ("negative", arb(-1), "incompatible"),
    ("positive_interval", arb(1, "1e-30"), "incompatible"),
]:
    try:
        _, stats = obj.poisson([a0], 8)
        record = stats["resonances"][0]
        actual = record["status"]
        detail = record
    except ArithmeticError as error:
        actual = "open"
        detail = str(error)
        assert "contains zero but is not exactly zero" in detail
    assert actual == expected, (label, actual, expected)
    rows.append(dict(label=label, input=str(a0), expected=expected,
                     actual=actual, detail=detail))
out = dict(checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
           source=str(src), source_sha256=digest, source_snapshot=str(snapshot),
           precision_bits=256, delta="1/2", n=8, resonant_j=1, tests=rows,
           all_passed=True)
Path("research/19_interval_resonance/verification/repair_check.json").write_text(
    json.dumps(out, indent=2) + "\n")
print(json.dumps({"source_sha256": digest, "checks": len(rows), "all_passed": True}))
