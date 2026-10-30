"""Exact comparison of tight Laurent packing against the full d2 cache."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
from pipeline import load, source, digest, OUT, ROOT, DATA
from packed_tight import residual_sine
from radial import Radial

start = time.monotonic()
name = "d2"
model = Radial(source(name))
result = {(h+1, "s", n): P for (h, n), P in residual_sine(model, True).items()}
reference = load(name, 0)[0, 0]
assert result == reference
out = {
    "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "candidate": name, "exact_coefficient_agreement": True,
    "components": len(result), "source_sha256": digest(source(name)),
    "reference_sha256": digest(DATA / f"{name}_D0.json.gz"),
    "product_code_sha256": digest(Path(__file__).with_name("packed_tight.py")),
    "code_sha256": digest(Path(__file__)),
    "proof_sha256": digest(ROOT / "research/whole_plane_norms/PROOF.md"),
    "elapsed_seconds": time.monotonic()-start,
}
dest = OUT / "tight_product_check.json"
assert not dest.exists()
dest.write_text(json.dumps(out, indent=2)+"\n")
print("exact comparison passed", len(result), "components",
      out["elapsed_seconds"], "seconds", flush=True)
