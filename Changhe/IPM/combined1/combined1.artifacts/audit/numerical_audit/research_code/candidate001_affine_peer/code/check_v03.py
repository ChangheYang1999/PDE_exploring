"""Independent exact raw-to-leading-coefficient replay and annular inputs."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from collections import defaultdict
import json
import os
import sys
import time
from flint import fmpq as Q

R = Path(__file__).resolve().parents[3]
B = R / "research/candidate001_affine_peer"
CID = "C1-N1-001-refit860-jabs"
RAW = "8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7"
now = lambda: datetime.now(timezone.utc).isoformat()
sha = lambda p: sha256(Path(p).read_bytes()).hexdigest()
sys.set_int_max_str_digits(0)


def main():
    tick = time.monotonic()
    assert os.sched_getaffinity(0) == {57}
    assert os.getpriority(os.PRIO_PROCESS, 0) == 19
    for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        assert os.environ[key] == "1"
    inputs, checks, external = {}, {}, {}

    def bind(p, expected=None):
        p = Path(p)
        h = sha(p)
        assert expected is None or h == expected, (str(p), h, expected)
        key = str(p.relative_to(R))
        assert key not in inputs or inputs[key] == h
        inputs[key] = h
        return p

    def read(p, expected=None):
        return json.loads(bind(p, expected).read_text())

    def check(label, value):
        assert label not in checks
        checks[label] = bool(value)
        assert value, label

    def rational_map(d):
        return {int(k): Q(v) for k, v in d.items() if Q(v)}

    def compare(label, actual, supplied):
        supplied = rational_map(supplied)
        check(label + ":support", set(actual) == set(supplied))
        for k in sorted(set(actual) | set(supplied)):
            check(label + f":coefficient{k}", actual.get(k, Q(0)) == supplied.get(k, Q(0)))

    first = read(B / "verification/PROOF_FIRST.json")
    bind(B / "PROOF.md", first["proof_sha256"])
    manifest = read(B / "source/MANIFEST.json", first["manifest_sha256"])
    bind(Path(__file__))
    bind(B / "SOURCE_SCHEMA_v02.md")
    bind(B / "SOURCE_SCHEMA_v03.md")
    bind(B / "code/check_v02.py")
    bind(R / "logs/candidate001_affine_peer_v02.out")
    bind(B / "code/check.py")
    bind(R / "logs/candidate001_affine_peer_v01.out")
    check("proof_precedes_checker", first["checker_not_yet_written"])
    for name, rec in manifest["files"].items():
        bind(B / "source" / name, rec["sha256"])
    for p, h in manifest["own_retained"].items():
        bind(R / p, h)
    rawp = R / f"research/candidate_audits/data/{CID}/candA_Jabs_exact.json"
    normalizedp = rawp.parent / "normalized_generators.json"
    raw = read(rawp, RAW)
    normalized = read(normalizedp)
    old = read(R / f"research/candidate_audits/verification/{CID}.json",
               "7c523fc56a2f6ac8cd54b74d8a6c3103c5022e6cf226172081c74d9354b64222")
    canonical = read(rawp.parent / "canonical.json", old["canonical_sha256"])
    check("normalization_only_adds_exact_cl",
          normalized == dict(raw, cl=raw["cl_exact"]))
    check("old_raw_bridge", old["generator_sha256"] == RAW and old["candidate"] == CID)
    check("old_manifest_bridge", old["manifest_sha256"] == sha(rawp.parent / "MANIFEST.json"))
    check("old_audit_entry", old["code_sha256"] == sha(R / "research/candidate_audits/code/audit_v1.py"))
    shared = R.parent / "c1-shared/candidate_snapshots" / CID / rawp.name
    external[str(shared)] = sha(shared)
    check("immutable_raw_current", external[str(shared)] == RAW)
    table = read(B / "source/T4_coefficients.json")
    t4 = read(B / "source/T4_review_result.json",
              "96c9365d3ecae7f96c8c71068dca5b093cb9d8ac2c41be1f606735c10caede8e")
    t4app = read(B / "source/T4_application_result.json",
                 "f367ac93db809c7d9c74c27d7b788bd198e4448c62afa1db894ae5251d324f61")
    check("T4_review_accepted", t4["verdict"].startswith("CONFIRMED") and all(t4["checks"].values()))
    check("T4_original_exact_input_record", t4app["check_count"] == 896
          and len(t4app["checks"]) == len(set(t4app["checks"])) == 896
          and all(isinstance(x, str) and x for x in t4app["checks"])
          and t4app["independent_inputs_recomputed"])
    for key in ["fixed_c_no_L2_application", "any_real_c_application"]:
        check("original_application_scope:" + key,
              t4app[key].startswith("CONFIRMED") and "awaits Opus review" in t4app[key])
    for key, name in [
        ("proof_sha256", "T4_review_PROOF.md"),
        ("code_sha256", "T4_review_check.py"),
        ("original_application_sha256", "T4_application_PROOF.md"),
        ("erratum_sha256", "T4_errata.md"),
        ("T1_review_sha256", "T1_review.md"),
        ("T2_review_sha256", "T2_review.md"),
    ]:
        check("peer_identity:" + key, t4[key] == sha(B / "source" / name))
    t2 = read(B / "source/T2_result.json")
    check("Opus_T2_exact_review_passed", t2["checks"] == 30 and not t2["fails"])
    check("Opus_T1_exact_review_passed", "RESULT PASS" in (B / "source/T1_check.out").read_text())
    check("review_rejects_FLOAT_as_premise", t4["FLOAT_diagnostics_used_as_proof"] is False)
    remote = read(B / "source/T4_review_external.json")
    check("peer_external_record_passed", remote["all_matched"])
    # The compact frozen manifest identifies every source used by T4's review.
    # Rehash each original as documentary evidence; execute none of them.
    peer_manifest = read(B / "source/T4_review_manifest.json")
    for i, rec in enumerate(peer_manifest):
        if "original" in rec:
            path = Path(rec["original"])
        else:
            peerroot = R.parent / "c1-t4/research/candidate001_affine_review"
            path = (peerroot / rec["local"]).resolve()
            assert path.is_relative_to(peerroot.resolve())
        external[str(path)] = sha(path)
        check(f"review_external_identity{i}", external[str(path)] == rec["sha256"])

    sys.path.insert(0, str(R / "research/refit_audit/code"))
    import convert as C
    import sectors_flint as S

    c = Q(raw["cl_exact"])
    gamma, delta = 1 / c, 1 - 1 / c
    q = gamma - delta
    check("exact_exponents", str(c) == table["c_exact"] and str(gamma) == table["gamma_exact"]
          and str(q) == table["q_exact"])
    check("strict_exponent_order", 0 < q < gamma < 1 and gamma - 1 < q)
    check("leading_transport_zero", c * gamma == 1)
    check("next_labels_below_q", gamma - 2 * delta < q and gamma - 2 < q)
    check("generator_count", len(raw["generators"]) == 860)
    branch_sums = defaultdict(lambda: defaultdict(Q))
    degrees = set()
    for i, row in enumerate(raw["generators"]):
        j, m, spec = row["j"], row["m"], row["spec"]
        valid = (type(j) is int and 0 <= j <= 3 and type(m) is int and 0 <= m <= 9
                 and spec[0] in ("mono", "leg")
                 and len(spec) == (2 if spec[0] == "mono" else 3)
                 and all(type(k) is int and k >= 0 for k in spec[1:]))
        check(f"raw_generator{i}", valid)
        branch_sums[j][2 * m] += Q(row["coef"])
        if spec[0] == "leg":
            degrees.add(spec[2])
    for n in sorted(degrees):
        check(f"Legendre_endpoint{n}", C.legendre(n)(1) == 1)
    fresh = C.convert(normalizedp)
    for key in ["cl", "a0", "strain", "order", "coefficients",
                "canonical_serialization_sha256", "generator_count"]:
        check("fresh_canonical:" + key, fresh[key] == canonical[key])
    alpha, potential, density, residual = S.sectors(fresh, qmax=0, hmax=1)
    for j in range(4):
        check(f"raw_to_leading_branch{j}", potential[j, 0] ==
              {n: a for n, a in branch_sums[j].items() if a})
        compare(f"potential{j}", potential[j, 0], table["leading_potential"][str(j)])
        compare(f"density{j}", density[j, 0], table["density"][str(j)])
        degree = alpha(j, 0) + 3
        stream = S.dy(S.dx(potential[j, 0], degree, "c"), degree - 1, "c")
        compare(f"stream{j}", stream, table["stream"][str(j)])
    E, G0 = residual[1, 0], density[0, 0]
    check("complete_leading_residual_zero", residual[0, 0] == {})
    compare("complete_E", E, table["E10"])
    compare("original_N4_028_E", E, old["first_nonzero_sector"]["sine_coefficients"])
    firstsector = old["first_nonzero_sector"]
    check("original_label", (firstsector["h"], firstsector["q"]) == (1, 0)
          and Q(firstsector["exponent"]) == q)
    check("E_support", sorted(E) == list(range(21, 40, 2)))
    check("G0_support", sorted(G0) == list(range(1, 20, 2)))
    e2 = sum((a * a for a in E.values()), Q(0))
    g2 = sum((a * a for a in G0.values()), Q(0))
    eg = sum((a * G0.get(n, Q(0)) for n, a in E.items()), Q(0))
    check("E_positive_exact", e2 > 0 and e2 == Q(table["E10_sum_squares_exact"])
          and e2 == Q(t4["E_norm_square_div_pi_exact"]))
    check("G0_positive_exact", g2 > 0 and g2 == Q(t4["G0_norm_square_div_pi_exact"]))
    check("changed_test_orthogonality", eg == 0 and eg == Q(t4["E_G0_inner_product_div_pi_exact"]))
    # Exact finite tests of the stated multiplier identities supplement the
    # algebraic proof; they are not its proof for all frequencies.
    for a, b in [(1, 0), (0, 1), (2, 3), (-5, 2)]:
        x, y = Q(a), Q(b)
        mod = x * x + y * y
        ux, uy = x * y / mod, -x * x / mod
        check(f"symbol:{a},{b}", x * ux + y * uy == 0
              and ux * ux + uy * uy == x * x / mod <= 1)
    for name, module in list(sys.modules.items()):
        filename = getattr(module, "__file__", None)
        if filename:
            p = Path(filename).resolve()
            if p.suffix == ".py" and p.is_relative_to(R):
                check("import_bound:" + name, str(p.relative_to(R)) in inputs)
    for p, h in inputs.items():
        assert sha(R / p) == h, p
    for p, h in external.items():
        assert sha(p) == h, p
    result = {
        "utc": now(), "candidate": CID, "raw_sha256": RAW,
        "inputs": inputs, "external_readonly_identities": external,
        "checks": checks, "check_count": len(checks),
        "c0_exact": str(c), "gamma_exact": str(gamma), "q_exact": str(q),
        "E": {str(n): str(a) for n, a in sorted(E.items())},
        "G0": {str(n): str(a) for n, a in sorted(G0.items())},
        "E_norm_squared_over_pi_exact": str(e2),
        "G0_norm_squared_over_pi_exact": str(g2),
        "E_G0_inner_product_over_pi_exact": str(eg),
        "fresh_own_conversion_and_derivatives": True,
        "peer_code_executed": False, "FLOAT_used_as_proof": False,
        "elapsed_seconds": time.monotonic() - tick,
        "verdict": "CONFIRMED corrected candidate001 affine L2 exclusion for every real c "
                   "and every fixed constant background velocity, by the standalone annular "
                   "proof and fresh complete exact coefficient replay. No non-L2 exclusion "
                   "or existence conclusion."
    }
    with (B / "verification/result_v03.json").open("x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(result["utc"], "PASS", len(checks), "checks", len(inputs), "own bindings",
          len(external), "external identities", result["elapsed_seconds"], "seconds", flush=True)


if __name__ == "__main__":
    main()
