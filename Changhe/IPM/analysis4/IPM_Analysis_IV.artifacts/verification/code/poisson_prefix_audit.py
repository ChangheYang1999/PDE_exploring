"""Direct coefficientwise Poisson identities, including resonant normalization."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import gzip
import json
import pickle
import sys
import time
from flint import arb, ctx
from stream_precision_audit import unpack

sys.dont_write_bytecode = True
ap = argparse.ArgumentParser()
ap.add_argument("--checkpoint", default="research/82_weighted_loss_criterion/update_N290_20261031T0624Z/verification/input_checkpoint.pkl.gz")
ap.add_argument("--max-order", type=int, default=290)
a = ap.parse_args()
ctx.prec = 640
start = time.monotonic()
now = datetime.now(timezone.utc)
root = Path("research/84_bivariate_residual_audit/verification") / now.strftime("poisson_%Y%m%dT%H%M%SZ")
root.mkdir()
(root / "sources").mkdir()
path = Path(a.checkpoint)
from read_checkpoint_archive import read_bytes
raw = read_bytes(path)
digest = sha256(raw).hexdigest()
state = pickle.loads(raw)
del raw
assert (state["A"], state["B"]) == ("2", "3")
N = min(max(state["f"]), a.max_order)
zero = arb(0)
text = lambda x: x.str(30, radius=True)
result = {
    "checked_at_utc": now.isoformat(timespec="seconds"),
    "checkpoint_path": str(path),
    "checkpoint_sha256": digest,
    "precision_bits": 640,
    "maximum_order": N,
    "orders": [],
    "source_sha256": {},
}
for name in ["poisson_prefix_audit.py", "stream_precision_audit.py", "read_checkpoint_archive.py"]:
    content = Path("code", name).read_bytes()
    (root / "sources" / (name + ".txt")).write_bytes(content)
    result["source_sha256"][name] = sha256(content).hexdigest()


def get(cols, q, j):
    return cols[q][j] if 0 <= q < len(cols) and 0 <= j < len(cols[q]) else zero


for n in range(1, N + 1):
    F = [[arb(*unpack(z)) for z in row] for row in state["f"][n]]
    G = [[arb(*unpack(z)) for z in row] for row in state["g"][n]]
    P = arb(2) - arb(2 * n) / 3
    errors = []
    checked = 0
    norms = [arb(0), arb(0), arb(0)]
    canonical_checks = 0
    for row in G:
        assert row[0] == 0
    angular_count = max(max(map(len, F)), max(map(len, G)))
    for q in range(max(len(F), len(G))):
        for j in range(1, angular_count + 1):
            m = 2 * j
            lhs = (m * m - P * P) * get(G, q, j) - 2 * P * (q + 1) * get(G, q + 1, j) - (q + 1) * (q + 2) * get(G, q + 2, j)
            rhs = ((P - m) * get(F, q, j - 1) + (q + 1) * get(F, q + 1, j - 1) + (P + m) * get(F, q, j) + (q + 1) * get(F, q + 1, j)) / 2
            residual = lhs - rhs
            if not residual.contains(0):
                errors.append([q, j, text(residual)])
            norms[0] += abs(lhs)
            norms[1] += abs(rhs)
            norms[2] += abs(residual)
            checked += 1
            if q == 0 and 3 * (2 + m) == 2 * n:
                canonical_checks += 1
                assert get(G, 0, j) == 0, (n, j, "resonant constant")
    scale = norms[0] + norms[1]
    relative = norms[2] / scale if scale > 0 else zero
    item = {
        "n": n,
        "checked_coefficients": checked,
        "failure_count": len(errors),
        "failures": errors[:20],
        "canonical_constant_checks": canonical_checks,
        "all_residual_coefficients_contain_zero": not errors,
        "lhs_norm": text(norms[0]),
        "rhs_norm": text(norms[1]),
        "residual_norm": text(norms[2]),
        "relative_residual": text(relative),
    }
    result["orders"].append(item)
    assert not errors, (n, errors[:20])
    if n % 20 == 0 or n == N:
        result["actual_elapsed_s"] = time.monotonic() - start
        (root / "checks.json").write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"output_directory": str(root), **item}), flush=True)
result["complete"] = True
result["total_checked_coefficients"] = sum(r["checked_coefficients"] for r in result["orders"])
result["total_canonical_constant_checks"] = sum(r["canonical_constant_checks"] for r in result["orders"])
result["actual_elapsed_s"] = time.monotonic() - start
(root / "checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k not in ["orders", "source_sha256"]}), flush=True)
