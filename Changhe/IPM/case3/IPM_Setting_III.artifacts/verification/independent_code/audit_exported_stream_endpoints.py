#!/usr/bin/env python3
"""Independent Decimal interpolation of exported stream values; no producer code."""
from datetime import datetime, timezone
from decimal import Decimal as D, localcontext
from fractions import Fraction
from math import factorial, prod
from pathlib import Path
import argparse
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/interpolated_stream_exports"
PROOF = ROOT / "research/interpolated_inverse_regularity/export_audit/PROOF.md"


def binary_decimal(value):
    """Preserve the exact binary64 number identified by its round-trip string."""
    return D.from_float(float(value))


def endpoint_jets(nodes, values, order):
    """Return derivatives at nodes[0], mode first, using barycentric division."""
    count = len(nodes)
    assert len(set(nodes)) == count and len(values) == count
    assert all(len(row) == len(values[0]) for row in values)
    products = []
    for i, x in enumerate(nodes):
        value = D(1)
        for j, y in enumerate(nodes):
            if i != j:
                value *= x - y
        products.append(value)
    ratios = [products[0] / p for p in products]
    den = [D(1)] + [D(0)] * order
    num = [[row] + [D(0)] * order for row in values[0]]
    for i in range(1, count):
        h = nodes[i] - nodes[0]
        term = -ratios[i]
        for j in range(1, order + 1):
            term /= h
            den[j] += term
            for mode in range(len(num)):
                num[mode][j] += term * values[i][mode]
    answer = []
    for row in num:
        coeff = [row[0]]
        for j in range(1, order + 1):
            coeff.append(row[j] - sum((den[h] * coeff[j-h] for h in range(1, j+1)), D(0)))
        answer.append([x * factorial(j) for j, x in enumerate(coeff)])
    return answer


def gate():
    checks = 0
    peak = D(0)
    for precision in (70, 110):
        with localcontext() as ctx:
            ctx.prec = precision
            for size in (7, 13, 23):
                # Uneven rational nodes, including both endpoints.
                nodes = [-D(1) + D(2) * (D(i)/D(size-1))**2 for i in range(size)]
                order = min(size-1, 6)
                expected = [[D(0)] * (order+1) for _ in range(size+2)]
                values = []
                for x in nodes:
                    z = x+1
                    row = [z**n if n else D(1) for n in range(size)]
                    row += [
                        sum((D((-1)**j) / D(j+1) * (z**j if j else D(1)) for j in range(size)), D(0)),
                        sum((D(j+1) * (z**j if j else D(1)) for j in range(size)), D(0)),
                    ]
                    values.append(row)
                for n in range(size):
                    if n <= order:
                        expected[n][n] = D(factorial(n))
                for j in range(order+1):
                    expected[-2][j] = D((-1)**j) * factorial(j) / D(j+1)
                    expected[-1][j] = D(j+1) * factorial(j)
                got = endpoint_jets(nodes, values, order)
                for a, b in zip(got, expected):
                    for aa, bb in zip(a, b):
                        err = abs(aa-bb) / max(D(1), abs(bb))
                        peak = max(peak, err)
                        checks += 1
                        assert err < D(10)**(-precision+30), (precision, size, err)
    return {"checks": checks, "max_normalized_error": str(peak), "status": "PASS"}


def logarithmic_coefficient(stream, degree, a):
    residual = {}
    for n, v in stream.items():
        for j, c in ((n-1, D(degree+n)/2), (n+1, D(degree-n)/2)):
            residual[j] = residual.get(j, D(0)) + a*c*v
    q = degree-1
    total = sum(
        (D(prod(n+q-2*h for h in range(q+1)))**2 * v*v for n, v in residual.items()), D(0)
    )
    return {
        "residual_sine_coefficients": {str(n): str(v) for n, v in residual.items()},
        "log_coefficient_divided_by_pi": str(total),
        "derivative_order": degree,
    }


def inspect(record, order, precisions):
    path = ROOT / record["export_snapshot"]
    data = json.loads(path.read_text())
    assert hashlib.sha256(path.read_bytes()).hexdigest() == record["export_sha256"]
    assert hashlib.sha256((ROOT / record["state_snapshot"]).read_bytes()).hexdigest() == data["sha256"]
    computed = []
    for precision in precisions:
        with localcontext() as ctx:
            ctx.prec = precision
            nodes = [binary_decimal(v) for v in data["tL"]]
            values = [[binary_decimal(v) for v in row] for row in data["PsiC"]]
            assert nodes[0] == -1 and nodes[-1] == 1
            assert all(x < y for x, y in zip(nodes, nodes[1:]))
            assert len(nodes) == data["N"] + 1
            derivatives = endpoint_jets(nodes, values, order)
            computed.append(derivatives)
    with localcontext() as ctx:
        ctx.prec = max(precisions)
        comparisons = []
        for mode, (lo, hi) in enumerate(zip(*computed)):
            for j, (x, y) in enumerate(zip(lo, hi)):
                err = abs(x-y) / max(D(1), abs(y))
                comparisons.append(err)
        disagreement = max(comparisons)
        assert disagreement < D("1e-65"), disagreement
        a = binary_decimal(data["a0"])
        kap = binary_decimal(data["p"])
        length = binary_decimal(data["L"])
        A = (2*kap*D(2).ln()).exp()/length**2
        derivatives = computed[-1]
        modes = {}
        for i, row in enumerate(derivatives):
            n = 2*(i+1)
            required = i  # Orders 0,...,m-2; empty for n=2.
            modes[str(n)] = {
                "endpoint_derivatives": [str(v) for v in row],
                "required_vanishing_orders": list(range(required)),
                "tested_required_orders": list(range(min(required, order+1))),
                "endpoint_value_exact_binary_rational": str(Fraction(float(data["PsiC"][0][i]))),
                "literal_endpoint_value_nonzero": bool(row[0]),
                "v2_raw": str(row[0]),
                "v4_raw": str(A*(2*row[1]-row[0])),
                "v6_raw": str(A*A*(2*row[2]-(4*kap+2)*row[1]+2*kap*row[0])),
            }
        raw = {2*(i+1): row[0] for i, row in enumerate(derivatives) if i >= 1}
        cleaned4 = {2*(i+1): 2*A*row[1] for i, row in enumerate(derivatives) if i >= 2}
        cleaned6 = {2*(i+1): 2*A*A*row[2] for i, row in enumerate(derivatives) if i >= 3}
        return {
            "source_sha256": data["sha256"],
            "export_sha256": record["export_sha256"],
            "N": data["N"], "M": data["M"], "cl": data["cl"], "a0": data["a0"],
            "L": data["L"], "kappa": data["p"],
            "precisions": precisions, "order": order,
            "max_precision_difference_scaled_by_max_one": str(disagreement),
            "modes": modes,
            "raw_forbidden_quadratic_max": str(max(map(abs, raw.values()))),
            "raw_D2_log": logarithmic_coefficient(raw, 2, a),
            "constant_cleaned_D4_log": logarithmic_coefficient(cleaned4, 4, a),
            "lower_coefficients_cleaned_D6_log": logarithmic_coefficient(cleaned6, 6, a),
            "interpretation": "The raw interpolation at supplied binary64 nodes is not exactly smooth whenever a forbidden endpoint value is nonzero. Cleaning cases are explicit counterfactual changes, not the original data. No canonical-inverse or limiting-regularity conclusion.",
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=6)
    parser.add_argument("--precisions", type=int, nargs=2, default=[100, 160])
    parser.add_argument("--gate-only", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    manufactured = gate()
    before = json.loads((PROOF.parent / "verification/proof_before_code.json").read_text())
    assert hashlib.sha256(PROOF.read_bytes()).hexdigest() == before["sha256"]
    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "proof_sha256": before["sha256"],
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "manufactured": manufactured,
        "states": {},
    }
    if not args.gate_only:
        manifest = json.loads((OUT / "MANIFEST.json").read_text())
        for record in manifest["states"]:
            name = Path(record["export_snapshot"]).stem
            result["states"][name] = inspect(record, args.order, args.precisions)
    result["elapsed_seconds"] = time.monotonic() - started
    name = "manufactured.json" if args.gate_only else "ENDPOINT_AUDIT.json"
    (OUT / name).write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"utc": result["utc"], "manufactured": manufactured,
                      "states": len(result["states"]), "elapsed_seconds": result["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
