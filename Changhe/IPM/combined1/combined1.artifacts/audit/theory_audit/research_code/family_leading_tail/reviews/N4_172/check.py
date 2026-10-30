"""Independent canonical sums and scaled-generator limits for the whole family."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from collections import defaultdict, Counter
from hashlib import sha256
import json
import sys
import time

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/"research/family_tail_equality"
SRC = BASE/"source"
C = Q(4076476460239181, 2251799813685248)
digest = lambda p: sha256(Path(p).read_bytes()).hexdigest()


def clean(mapping):
    return {k: v for k, v in sorted(mapping.items()) if v}


def canonical_amplitudes(data):
    assert Q(data["cl"]) == C
    result = defaultdict(Q)
    for (j, m, k), value in zip(data["order"], data["coefficients"], strict=True):
        assert int(j) == j and int(m) == m and int(k) == k and k >= m >= 0 and j >= 0
        if j == 0:
            result[m] += Q(value)
    return clean(result)


def raw_amplitudes(data):
    assert Q(data.get("cl", data.get("cl_exact"))) == C
    result = defaultdict(Q)
    counts = Counter()
    scaled = []
    endpoint_checks = 0
    for row in data["generators"]:
        j, m = row["j"], row["m"]
        assert int(j) == j and int(m) == m and min(j, m) >= 0
        spec = row["spec"]
        kind = spec[0]
        counts[kind] += 1
        if kind == "mono":
            assert len(spec) == 2
            w, n, q, R = int(spec[1]), 0, 0, Q(1)
        elif kind in ("leg", "legq", "legqs"):
            assert len(spec) == {"leg": 3, "legq": 4, "legqs": 5}[kind]
            w, n = map(int, spec[1:3])
            q = int(spec[3]) if len(spec) >= 4 else 0
            R = Q(spec[4]) if len(spec) == 5 else Q(1)
        else:
            raise AssertionError(kind)
        assert min(w, n, q) >= 0 and R > 0
        assert all(int(z) == z for z in spec[1:4] if not isinstance(z, str))
        # Endpoint from the Legendre three-term recurrence, distinct from
        # the peer's explicit alternating binomial sum.
        prev = current = Q(1)
        for k in range(1, n):
            prev, current = current, ((2*k+1)*current-k*prev)/(k+1)
        assert current == 1
        endpoint_checks += 1
        if kind == "legqs":
            scaled.append({"j": j, "m": m, "q": q, "R": str(R)})
        if j == 0 and q == 0:
            result[m] += Q(row["coef"])*current
    return clean(result), dict(counts), scaled, endpoint_checks


def density(amps):
    d = 3+1/C
    fourier = {}
    for m, value in amps.items():
        if m == 0:
            fourier[0] = value
        else:
            fourier[2*m] = fourier[-2*m] = value/2
    imag = defaultdict(Q)
    for n, value in fourier.items():
        lap = (d*d-n*n)*value
        imag[n+1] += lap*(d-2-n)/2
        imag[n-1] -= lap*(d-2+n)/2
    assert all(imag[n] == -imag[-n] for n in list(imag))
    return clean({n: -2*z for n, z in imag.items() if n > 0})


def main():
    start = time.monotonic()
    manifest_path = SRC/"MANIFEST.json"
    manifest = json.loads(manifest_path.read_text())
    for name, entry in manifest["files"].items():
        assert digest(SRC/name) == entry["sha256"]
    assert digest(SRC/"T4_result.json") == "18a18ba0262e6f7b593b5858601f76668eafa0e4a47ada0b7c775ce42ad9acfc"
    peer = json.loads((SRC/"T4_result.json").read_text())
    assert peer["proof_sha256"] == digest(SRC/"T4_PROOF.md")
    assert peer["code_sha256"] == digest(SRC/"T4_check.py")
    reference_path = ROOT/"research/leading_tail_nonzero/verification/candidate007.json"
    assert digest(reference_path) == "bc06d154c0e20e0ba1c38d0dd2ca3331f1f2aef7424f57570917025ef9ce8f1d"
    confirmed = json.loads(reference_path.read_text())
    ref = clean({int(k): Q(v) for k, v in confirmed["leading_potential_amplitudes"].items()})
    density_ref = clean({int(k): Q(v) for k, v in confirmed["leading_density_sine_coefficients"].items()})
    assert density(ref) == density_ref
    assert 18 < density_ref[1] < 19
    cases = []
    for record in peer["records"]:
        name = record["candidate"]
        paths = []
        canonical_path = None
        raw_path = None
        if name in ("state131", "d2"):
            canonical_path = ROOT/(
                "research/baseline/data/state131_independent.json" if name == "state131"
                else "research/refit_audit/data/d2_canonical.json")
            if name == "d2":
                raw_path = ROOT/"research/refit_audit/data/d2_generators.json"
        elif name.startswith("C1-N1-011-"):
            raw_path = SRC/"011_exact.json"
            snapshot_manifest = SRC/"011_MANIFEST.json"
        else:
            folder = ROOT/"research/candidate_audits/data"/name
            snapshot_manifest = folder/"MANIFEST.json"
            snapshot = json.loads(snapshot_manifest.read_text())
            assert snapshot["id"] == name and len(snapshot["coefficient_files"]) == 1
            raw_path = folder/snapshot["coefficient_files"][0]["name"]
            if (folder/"canonical.json").exists():
                canonical_path = folder/"canonical.json"
                audit_path = ROOT/"research/candidate_audits/verification"/(name+".json")
                audit = json.loads(audit_path.read_text())
                assert audit["canonical_sha256"] == digest(canonical_path)
                paths.append(audit_path)
        if name.startswith("C1-N1-"):
            snapshot = json.loads(snapshot_manifest.read_text())
            assert snapshot["id"] == name and len(snapshot["coefficient_files"]) == 1
            assert digest(raw_path) == snapshot["coefficient_files"][0]["sha256"] == record["source_sha256"]
            paths.append(snapshot_manifest)
        A = None
        counts, scaled, endpoint_checks = {}, [], 0
        canonical_equal = None
        if canonical_path is not None:
            can = json.loads(canonical_path.read_text())
            A = canonical_amplitudes(can)
            paths.append(canonical_path)
        if raw_path is not None:
            raw = json.loads(raw_path.read_text())
            B, counts, scaled, endpoint_checks = raw_amplitudes(raw)
            paths.append(raw_path)
            if A is not None:
                assert A == B
                canonical_equal = True
            else:
                A = B
            if name.startswith(("C1-N1-010-", "C1-N1-011-")):
                assert scaled and all(z["q"] == 4 for z in scaled)
        assert A == ref
        assert A == clean({int(k): Q(v) for k, v in record["leading_potential_amplitudes"].items()})
        G = density(A)
        assert G == density_ref and G[1] == Q(record["first_density_harmonic"])
        assert 18 < G[1] < 19
        cases.append({
            "candidate": name, "inputs": {str(p.relative_to(ROOT)): digest(p) for p in paths},
            "leading_potential_equal_confirmed007": True,
            "entire_leading_density_equal_confirmed007": True,
            "peer_amplitudes_and_b1_exact_match": True,
            "raw_canonical_maps_equal": canonical_equal,
            "generator_counts": counts, "Legendre_endpoint_checks": endpoint_checks,
            "scaled_generator_count": len(scaled),
            "scaled_q_values": sorted({z["q"] for z in scaled}),
            "scaled_radii": sorted({z["R"] for z in scaled}),
            "strict_b1_lower": "18", "strict_b1_upper": "19",
            "b1_float_diagnostic": float(G[1]),
        })
    assert len(cases) == 10
    out = {
        "utc": datetime.now(timezone.utc).isoformat(), "c_exact": str(C),
        "gamma_exact": str(1/C), "cases": cases,
        "exact_reference_path": str(reference_path.relative_to(ROOT)),
        "exact_reference_sha256": digest(reference_path),
        "peer_result_sha256": digest(SRC/"T4_result.json"),
        "source_manifest_sha256": digest(manifest_path),
        "proof_sha256": digest(BASE/"PROOF.md"), "code_sha256": digest(__file__),
        "elapsed_seconds": time.monotonic()-start,
        "verdict": "CONFIRMED common entire leading density and18<b1<19 for state131,d2,005..012",
        "scope": "Any-c conclusions use the audited weighted canonical affine chart; no new exclusion for an unchecked011 ball.",
    }
    target = BASE/"verification/result.json"
    target.parent.mkdir(exist_ok=True)
    with target.open("x") as f:
        json.dump(out, f, indent=2)
        f.write("\n")
    print(out["verdict"], out["elapsed_seconds"], flush=True)
    for row in cases:
        print(row["candidate"], "raw/canonical", row["raw_canonical_maps_equal"],
              "scaled", row["scaled_generator_count"], row["scaled_q_values"], flush=True)


if __name__ == "__main__":
    main()
