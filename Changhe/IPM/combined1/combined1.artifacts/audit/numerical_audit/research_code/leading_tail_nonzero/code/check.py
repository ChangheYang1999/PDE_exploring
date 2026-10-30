"""Independent raw-generator Fourier calculation of the leading density."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import sys
import time

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/leading_tail_nonzero"


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def main():
    start = time.monotonic()
    manifest_path = BASE / "source/MANIFEST.json"
    manifest = json.loads(manifest_path.read_text())
    for name, value in manifest["files"].items():
        assert digest(ROOT / name) == value
    raw = json.loads((ROOT / "research/basis_redundancy/source/candidate007.json").read_text())
    canonical = json.loads((ROOT / "research/basis_redundancy/source/canonical007.json").read_text())
    peer = json.loads((BASE / "source/T4_203_result.json").read_text())
    c = Q(raw.get("cl", raw.get("cl_exact")))
    assert c == Q(4076476460239181, 2251799813685248)
    d = 3 + 1 / c
    assert 0 < 1 / c < 1
    amps = defaultdict(Q)
    endpoint_checks = []
    for g in raw["generators"]:
        coefficient = g["coef"]
        if int(g["j"]) != 0:
            continue
        spec = g["spec"]
        if spec[0] == "mono":
            endpoint = 1
        else:
            assert spec[0] == "leg"
            n = int(spec[2])
            endpoint = sum((-1)**(n-k)*comb(n, k)*comb(n+k, k) for k in range(n+1))
        assert endpoint == 1
        endpoint_checks.append(endpoint)
        amps[int(g["m"])] += Q(coefficient) * endpoint
    canonical_amps = defaultdict(Q)
    for (j, m, k), coefficient in zip(canonical["order"], canonical["coefficients"]):
        if int(j) == 0:
            canonical_amps[int(m)] += Q(coefficient)
    assert dict(amps) == dict(canonical_amps)
    fourier = {}
    for m, a in amps.items():
        if m == 0:
            fourier[0] = a
        else:
            fourier[2*m] = fourier[-2*m] = a / 2
    imaginary_density = defaultdict(Q)
    k = d - 2
    for n, a in fourier.items():
        laplacian = (d*d-n*n)*a
        imaginary_density[n+1] += laplacian*(k-n)/2
        imaginary_density[n-1] -= laplacian*(k+n)/2
    assert all(n % 2 != 0 for n in imaginary_density)
    assert all(a == -imaginary_density[-n] for n, a in imaginary_density.items())
    sine = {n: -2*a for n, a in sorted(imaginary_density.items()) if n > 0}
    b = sine[1]
    formula = -amps[0]*d*d*(d-2) + amps[1]*(d*d-4)*d/2
    assert b == formula == Q(peer["first_density_harmonic"])
    assert 18 < b < 19
    assert peer["source_sha256"] == digest(ROOT / "research/basis_redundancy/source/canonical007.json")
    assert {int(m): Q(a) for m, a in peer["leading_potential_amplitudes"].items()} == dict(amps)
    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "candidate": "C1-N1-007-d2w-j7-e2bal",
        "coefficient_sha256": digest(ROOT / "research/basis_redundancy/source/candidate007.json"),
        "canonical_sha256": digest(ROOT / "research/basis_redundancy/source/canonical007.json"),
        "raw_generator_endpoint_checks": len(endpoint_checks),
        "leading_potential_amplitudes": {str(m): str(a) for m, a in sorted(amps.items())},
        "leading_density_sine_coefficients": {str(n): str(a) for n, a in sine.items()},
        "first_density_harmonic": str(b),
        "strict_rational_lower_bound": "18",
        "strict_rational_upper_bound": "19",
        "float_diagnostic": float(b),
        "raw_canonical_amplitudes_agree": True,
        "all_peer_amplitudes_agree": True,
        "peer_b1_agrees_exactly": True,
        "peer_result_sha256": digest(BASE / "source/T4_203_result.json"),
        "proof_sha256": digest(BASE / "PROOF.md"),
        "code_sha256": digest(__file__),
        "manifest_sha256": digest(manifest_path),
        "elapsed_seconds": time.monotonic() - start,
        "status": "CONFIRMED exact b1 and finite leading expansion; analytic solution theorem separate",
    }
    with (BASE / "verification/candidate007.json").open("x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({k: result[k] for k in (
        "utc", "raw_generator_endpoint_checks", "strict_rational_lower_bound",
        "strict_rational_upper_bound", "float_diagnostic", "peer_b1_agrees_exactly",
        "elapsed_seconds", "status")}, indent=2))


if __name__ == "__main__":
    main()
