"""Independent Laurent/Kronecker convolution audit of selected log orders."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import gzip
import json
import pickle
import sys
import time
from flint import arb, arb_poly, ctx
from stream_precision_audit import unpack

sys.dont_write_bytecode = True
ap = argparse.ArgumentParser()
ap.add_argument("--checkpoint", default="research/82_weighted_loss_criterion/update_N290_20261031T0624Z/verification/input_checkpoint.pkl.gz")
ap.add_argument("--orders", default="2,6,7,12,20,40,60")
ap.add_argument("--seconds", type=float, default=480)
ap.add_argument("--output", required=True)
a = ap.parse_args()
ctx.prec = 640
start = time.monotonic()
root = Path(a.output)
root.mkdir(parents=True, exist_ok=False)
(root / "sources").mkdir()
path = Path(a.checkpoint)
raw = path.read_bytes()
if path.suffix == ".gz":
    raw = gzip.decompress(raw)
digest = sha256(raw).hexdigest()
state = pickle.loads(raw)
del raw
assert (state["A"], state["B"]) == ("2", "3")
orders = list(map(int, a.orders.split(",")))
N = max(orders)
assert max(state["f"]) >= N
values = {
    field: {
        n: [[arb(*unpack(v)) for v in row] for row in cols]
        for n, cols in state[field].items() if n <= N
    } for field in ["f", "g"]
}
del state
text = lambda x: x.str(30, radius=True)
record = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "checkpoint_path": str(path),
    "checkpoint_sha256": digest,
    "precision_bits": 640,
    "orders": [],
    "source_sha256": {},
}
for name in ["bivariate_residual_audit.py", "stream_precision_audit.py"]:
    content = Path("code", name).read_bytes()
    (root / "sources" / (name + ".txt")).write_bytes(content)
    record["source_sha256"][name] = sha256(content).hexdigest()


def pack(field, n, stride, operation, radial=arb(0), derivative=arb(0)):
    """Pack i times a sine polynomial or its E/radial derivative."""
    cols = values[field][n]
    shift = 2 * n
    coefficients = [arb(0) for _ in range(stride * (len(cols) - 1) + 4 * n + 1)]
    for q, row in enumerate(cols):
        for k, value in enumerate(row):
            m = 2 * k + (1 if field == "f" else 0)
            if m == 0:
                assert value == 0
                continue
            assert m <= shift, (field, n, m, shift)
            v = value / 2
            plus, minus = stride * q + shift + m, stride * q + shift - m
            if operation == "E":
                coefficients[plus] += m * v
                coefficients[minus] += m * v
            else:
                coefficients[plus] += radial * v
                coefficients[minus] -= radial * v
                if q and derivative != 0:
                    coefficients[plus - stride] += derivative * q * v
                    coefficients[minus - stride] -= derivative * q * v
    return arb_poly(coefficients)


for n in orders:
    if time.monotonic() - start > a.seconds:
        break
    order_start = time.monotonic()
    stride = 4 * n + 1
    expected = pack("f", n, stride, "radial", arb(2 * (n - 1)), arb(-3))
    total = arb_poly()
    max_input_length = 0
    for i in range(1, n):
        j = n - i
        gr = pack("g", i, stride, "radial", arb(2) - arb(2 * i) / 3, arb(1))
        fe = pack("f", j, stride, "E")
        ge = pack("g", i, stride, "E")
        fr = pack("f", j, stride, "radial", arb(1) - arb(2 * j) / 3, arb(1))
        max_input_length = max(max_input_length, len(gr), len(fe), len(ge), len(fr))
        total += gr * fe - ge * fr
    residual = total - expected
    residual_values = residual.coeffs()
    failures = [k for k, value in enumerate(residual_values) if not value.contains(0)]
    forcing_norm = sum(map(abs, expected.coeffs()), arb(0))
    residual_norm = sum(map(abs, residual_values), arb(0))
    relative = residual_norm / forcing_norm
    row = {
        "n": n,
        "pairs": n - 1,
        "kronecker_stride": stride,
        "maximum_input_length": max_input_length,
        "output_length": max(len(expected), len(total)),
        "checked_coefficients": len(residual_values),
        "failed_coefficients": failures[:20],
        "failure_count": len(failures),
        "all_residual_coefficients_contain_zero": not failures,
        "forcing_norm": text(forcing_norm),
        "residual_norm_enclosure": text(residual_norm),
        "relative_residual_enclosure": text(relative),
        "actual_elapsed_s": time.monotonic() - order_start,
    }
    record["orders"].append(row)
    record["actual_elapsed_s"] = time.monotonic() - start
    (root / "checks.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(row), flush=True)
    assert not failures, (n, failures[:20])
record["complete_requested_orders"] = len(record["orders"]) == len(orders)
record["actual_elapsed_s"] = time.monotonic() - start
(root / "checks.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"complete": record["complete_requested_orders"], "actual_elapsed_s": record["actual_elapsed_s"]}), flush=True)
