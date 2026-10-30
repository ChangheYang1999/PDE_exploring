"""Exact comparison with the coefficient realization used by binary64 loaders."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
from hashlib import sha256
import copy
import json
import sys
import time
from flint import arb, fmpq as Q, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/rounding_realization"
sys.path.insert(0, str(ROOT / "research/refit_audit/code"))
sys.path.insert(0, str(ROOT / "research/multiscale_generators/code"))
from convert import convert
from sectors_flint import sectors, aq
from cartesian import GeneratorJet


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def norm(poly):
    return (arb.pi()*sum((aq(v)**2 for v in poly.values()), arb(0))).sqrt()


def run(name):
    start = time.monotonic()
    ctx.prec = 1024
    source = ROOT / f"research/candidate_audits/data/{name}/normalized_generators.json"
    canonical = ROOT / f"research/candidate_audits/data/{name}/canonical.json"
    exact = json.loads(source.read_text())
    rounded = copy.deepcopy(exact)
    changes = []
    for a, b in zip(exact["generators"], rounded["generators"]):
        value = Fraction(a["coef"])
        stored = float(a["coef_float"])
        assert stored == float(value)
        realized = Fraction(stored)
        b["coef"] = str(realized)
        changes.append(abs(realized-value))
    assert any(changes)
    folder = BASE / "data" / name
    folder.mkdir(parents=True, exist_ok=True)
    raw_path = folder / "binary64_coefficients_exact.json"
    assert not raw_path.exists()
    raw_path.write_text(json.dumps(rounded, indent=2)+"\n")
    state_b = convert(raw_path)
    state_a = json.loads(canonical.read_text())
    can_b = folder / "binary64_canonical.json"
    can_b.write_text(json.dumps(state_b, indent=2)+"\n")
    hmax = max(7, max(j for j, m, k in state_a["order"])+1)
    alpha, Ca, Ga, Ea = sectors(state_a, qmax=1, hmax=hmax)
    _, Cb, Gb, Eb = sectors(state_b, qmax=1, hmax=hmax)
    rows = []
    for h, q in sorted(set(Ea) | set(Eb), key=lambda v: alpha(*v), reverse=True):
        if alpha(h, q) < -2:
            continue
        pa, pb = Ea.get((h, q), {}), Eb.get((h, q), {})
        assert not pa
        rows.append({
            "h": h, "q": q, "exponent": str(alpha(h, q)),
            "exact_zero": not pa, "rounded_exact_zero": not pb,
            "rounded_full_circle_norm": norm(pb).str(70),
        })
    lead = next((r for r in rows if not r["rounded_exact_zero"]), None)
    result = {
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidate": name, "source_sha256": digest(source),
        "canonical_source_sha256": digest(canonical),
        "realized_source_sha256": digest(raw_path),
        "realized_canonical_sha256": digest(can_b),
        "code_sha256": digest(Path(__file__)),
        "proof_sha256": digest(BASE / "PROOF.md"),
        "jet_code_sha256": digest(ROOT / "research/multiscale_generators/code/cartesian.py"),
        "precision_bits": ctx.prec,
        "stored_binary64_matches_correct_rounding": True,
        "coefficient_count": len(changes),
        "changed_coefficients": sum(v != 0 for v in changes),
        "maximum_absolute_coefficient_error": str(max(changes)),
        "maximum_absolute_coefficient_error_ball": aq(Q(str(max(changes)))).str(50),
        "fixed_c_unchanged": Q(state_a["cl"]) == Q(state_b["cl"]),
        "strain_difference": str(Q(state_b["strain"])-Q(state_a["strain"])),
        "strain_difference_ball": aq(Q(state_b["strain"])-Q(state_a["strain"])).str(60),
        "a0_difference_ball": aq(Q(state_b["a0"])-Q(state_a["a0"])).str(60),
        "leading_potential_unchanged": Ca[0, 0] == Cb[0, 0],
        "leading_density_unchanged": Ga[0, 0] == Gb[0, 0],
        "forbidden_sectors": rows,
        "leading_nonzero_forbidden_sector": lead,
        "points": [],
        "scope": "Coefficient conversion only, at fixed exact c and exact generators. Not a defect of the published rational candidate.",
    }
    print("coefficients", len(changes), "changed", result["changed_coefficients"],
          "leading sector", lead, flush=True)
    for x, y in [("0", "1/4"), ("100", "200")]:
        a = GeneratorJet(exact, x, y).fields()
        b = GeneratorJet(rounded, x, y).fields()
        differences = {k: (b[k]-a[k]).str(70) for k in a}
        v1, v2 = b["u1"]-a["u1"], b["u2"]-a["u2"]
        e, ex, ey = b["rho"]-a["rho"], b["rho_x"]-a["rho_x"], b["rho_y"]-a["rho_y"]
        c = aq(Q(state_a["cl"]))
        expanded = (c*aq(Q(x))+a["u1"])*ex+(c*aq(Q(y))+a["u2"])*ey
        expanded += v1*a["rho_x"]+v2*a["rho_y"]+v1*ex+v2*ey-e
        assert expanded.overlaps(b["residual"]-a["residual"])
        result["points"].append({
            "point": [x, y], "exact_residual": a["residual"].str(70),
            "rounded_residual": b["residual"].str(70),
            "differences": differences,
            "residual_expansion_overlap": True,
        })
        print("point", x, y, "F difference", differences["residual"], flush=True)
    result["elapsed_seconds"] = time.monotonic()-start
    dest = BASE / f"verification/{name}.json"
    assert not dest.exists()
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print("seconds", result["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    run(sys.argv[1])
