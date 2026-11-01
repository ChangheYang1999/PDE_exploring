"""Compare a ball checkpoint with independently verified exact log data."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from math import factorial
import io
import json
import pickle
import time
from flint import fmpq as Q, arb, ctx


class PlainUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        raise ValueError("Only plain checkpoint containers are accepted")


def dyadic(m, e):
    return Q(int(m)) * Q(2) ** int(e)


def exact_ball(record):
    m, e, r = record
    mid = dyadic(m, e)
    if r == "0":
        rad = Q(0)
    else:
        rm, re = r.split("*2^")
        rad = dyadic(rm, re)
    assert rad >= 0
    return mid, rad


def main():
    start = time.monotonic()
    target = Path("research/21_logarithmic_data_audit")
    src = Path("../a4-num/ckpt/log_sin1_c9_5_p512.pkl")
    raw = src.read_bytes()
    data = PlainUnpickler(io.BytesIO(raw)).load()
    exact_path = target / "sources/lead_exact_log_data.json"
    exact_raw = exact_path.read_bytes()
    exact = json.loads(exact_raw)
    assert Q(int(data["A"]), int(data["B"])) == Q(exact["delta"]) == Q(4, 9)
    N = min(73, max(data["f"]), exact["completed_order"])
    prefix = {key: data[key] for key in ["ring", "prec", "A", "B"]}
    for key in ["f", "g", "stats", "resonances"]:
        prefix[key] = {n: row for n, row in data[key].items() if n <= N}
    prefix_blob = pickle.dumps(prefix, protocol=4)
    (target / "sources/numerics_log_prefix73.pkl").write_bytes(prefix_blob)
    count = {"density": 0, "stream": 0}
    rows = []
    ctx.prec = 512
    for field, key in [("density", "f"), ("stream", "g")]:
        for n in range(1, N + 1):
            exact_modes = {int(m): [Q(v) for v in coeffs]
                           for m, coeffs in exact[field][str(n)].items()}
            columns = data[key][n]
            normcols = [Q(0)] * max(len(columns), max(map(len, exact_modes.values()), default=0))
            for mode, coeffs in exact_modes.items():
                idx = (mode - 1) // 2 if field == "density" else mode // 2
                for power, value in enumerate(coeffs):
                    assert power < len(columns) and idx < len(columns[power])
                    normcols[power] += abs(value)
            for power, col in enumerate(columns):
                for idx, record in enumerate(col):
                    mode = 2 * idx + 1 if field == "density" else 2 * idx
                    coeffs = exact_modes.get(mode, [])
                    value = coeffs[power] if power < len(coeffs) else Q(0)
                    mid, rad = exact_ball(record)
                    assert abs(value - mid) <= rad, (field, n, power, mode)
                    count[field] += 1
            if n in [9, 18, 36, 40, 72, 73]:
                plain = sum(normcols, Q(0))
                factorial1 = sum((v * factorial(k) for k, v in enumerate(normcols)), Q(0))
                factorial36 = sum((v * factorial(k) * 36 ** k for k, v in enumerate(normcols)), Q(0))
                rows.append(dict(field=field, n=n,
                                 log_degree=max(k for k, v in enumerate(normcols) if v),
                                 plain_norm=str(arb(plain)),
                                 plain_root=str(arb(plain).root(n)),
                                 factorial1_root=str(arb(factorial1).root(n)),
                                 factorial36_root=str(arb(factorial36).root(n))))
            if n % 10 == 0:
                print(field, n, "exact containment passed", flush=True)
    out = dict(checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               source=str(src), source_sha256=sha256(raw).hexdigest(),
               original_checkpoint_N=max(data["f"]), checked_N=N,
               retained_prefix_sha256=sha256(prefix_blob).hexdigest(),
               exact_source=str(exact_path), exact_source_sha256=sha256(exact_raw).hexdigest(),
               exact_containment_counts=count, all_containments_passed=True,
               arithmetic="Exact rational comparison of every dyadic interval endpoint; Arb512 norm summaries",
               norm_summaries=rows, actual_elapsed_s=time.monotonic() - start)
    (target / "verification/numerics_ball_containment.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(dict(N=N, counts=count, actual_elapsed_s=out["actual_elapsed_s"])))


if __name__ == "__main__":
    main()
