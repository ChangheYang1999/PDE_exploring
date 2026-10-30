"""Combine independently reproduced radial and angular compression energies."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import sys
import time
from flint import arb, ctx, fmpq as Q

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/overlap_compression_audit"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def ar(x):
    return arb(x.numerator) / x.denominator


def main():
    start = time.monotonic()
    ctx.prec = 1024
    name = "C1-N1-008-d2w-j7-x3bal"
    angular_path = ROOT / "research/parity_angular_audit/source/T4_008_n8_m6.json"
    angular_check = ROOT / "research/parity_angular_audit/verification/candidate008_n8_m6.json"
    radial_path = ROOT / "research/parity_budget_audit/verification/candidate008_d32.json"
    peer_path = BASE / "source/T4_008_n8_m6_d32.json"
    energy_path = ROOT / f"research/background_sobolev/verification/{name}.json"
    dest = BASE / "verification/candidate008_n8_m6_d32.json"
    assert not dest.exists()
    a = json.loads(angular_path.read_text())
    ac = json.loads(angular_check.read_text())
    r = json.loads(radial_path.read_text())
    peer = json.loads(peer_path.read_text())
    e = json.loads(energy_path.read_text())
    assert a["candidate"] == r["candidate"] == peer["candidate"] == name
    assert ac["inputs"][str(angular_path.relative_to(ROOT))] == digest(angular_path)
    canonical = ROOT / f"research/candidate_audits/data/{name}/canonical.json"
    assert r["inputs"][str(canonical.relative_to(ROOT))] == digest(canonical)
    assert e["source_sha256"] == digest(canonical)
    assert a["N"] == 8 and a["M"] == 6 and r["dimension"] == 32
    maps = {
        f"parity_hs_angular/verification/{name}_n8_m6.json": angular_path,
        f"parity_hs_budget/verification/{name}_d32.json":
            ROOT / "research/parity_budget_audit/source/T4_008_d32.json",
        "nested_compression_union/code/combine.py": BASE / "source/T4_combine.py",
        "nested_compression_union/PROOF.md": BASE / "source/T4_PROOF.md",
    }
    for path, value in peer["inputs"].items():
        assert digest(maps[path]) == value, path
    block = a["blocks"]["++"]
    indices = [i for i, label in enumerate(block["labels"]) if label[0:2] == ["cos", 0]]
    assert len(indices) == 8
    checks = 0
    for i in indices:
        for j in indices:
            n, m = block["labels"][i][2], block["labels"][j][2]
            for key in ["G_over_pi", "B_over_pi"]:
                assert Q(block[key][i][j]) == Q(r[key][n][m])
                checks += 1
    rows = {x["dimension"]: x for x in r["rows"]}
    common = Q(rows[8]["captured_exact"])
    extended = Q(rows[32]["captured_exact"])
    angular = Q(a["total_captured_exact"])
    assert extended >= common
    union = angular + extended - common
    assert union == Q(peer["union_energy_exact"])
    norms = e["norms"]
    ex = Q(norms["D_rho_x"]["unweighted_rational_sum"])
    ey = Q(norms["D_rho_y"]["unweighted_rational_sum"])
    kappa2 = ((arb(2).log() - Q(1, 2)) * ar(ex) +
              (3 * arb(2).log() - 2) * ar(ey)) / 32
    assert kappa2 > ar(union)
    bound = (kappa2 - ar(union)).sqrt()
    c = Q(4076476460239181, 2251799813685248)
    values = {
        "angular_energy": ar(angular),
        "radial_common_energy": ar(common),
        "radial_extended_energy": ar(extended),
        "union_energy": ar(union),
        "S1_absolute_upper": bound,
        "theta_budget_for_beta2": ar(c - 1) - bound,
    }
    assert all(v.overlaps(arb(peer[k])) for k, v in values.items())
    inputs = [
        angular_path, angular_check, radial_path, peer_path, energy_path,
        canonical, BASE / "PROOF.md", BASE / "verification/proof_review.json",
        Path(__file__), *maps.values(),
    ]
    out = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "candidate": name,
        "precision_bits": ctx.prec,
        "angular_N": 8,
        "angular_M": 6,
        "radial_dimension": 32,
        "common_matrix_entries_checked": checks,
        "union_energy_exact": str(union),
        "all_scalar_balls_overlap": True,
        **{k: v.str(85) for k, v in values.items()},
        "inputs": {str(p.relative_to(ROOT)): digest(p) for p in inputs},
        "elapsed_seconds": time.monotonic() - start,
        "status": "CONFIRMED finite compression union; separate theta and generator hypotheses remain",
    }
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print("DONE", bound.str(30), values["theta_budget_for_beta2"].str(30), flush=True)


if __name__ == "__main__":
    main()
