"""Evaluate localized probes from the exact projected residual."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import argparse
import json
import sys
import time
from flint import fmpq as Q, arb, arb_poly, ctx
from build import candidate_source, read_projection, destination, digest, ROOT

sys.path.insert(0, str(ROOT/"research/localized_weak_probe/code"))
from beta_scale import integral, supremum, groups, ap, ar, Radial, U

BASE = ROOT/"research/projected_residual"


def run(name, ks, bits):
    start = time.monotonic()
    ctx.prec = bits
    path = candidate_source(name)
    model = Radial(path)
    assert 0 < model.g < 1
    projected, metadata = read_projection(name)
    F = [(ell, ap(P(U))) for ell, P in projected.items()]
    bg = groups(model, ["u1", "u2"])
    cg = groups(model, ["rho_x", "rho_y"])
    evidence = {}
    if name.startswith("C1-N1-"):
        audit_path = ROOT/f"research/candidate_audits/verification/{name}.json"
        audit = json.loads(audit_path.read_text())
        assert audit["canonical_sha256"] == digest(path)
        forbidden = [s for s in audit["sectors"] if Fraction(s["exponent"]) >= -1]
        assert forbidden and all(s["exact_zero"] for s in forbidden)
        evidence = {
            "candidate_audit_sha256": digest(audit_path),
            "checked_sectors_with_exponent_at_least_minus_one": len(forbidden),
            "all_these_sectors_exact_zero": True,
            "scope": "Membership also uses the complete asymptotic remainder argument in the candidate audit.",
        }
    old_path = ROOT/f"research/localized_weak_probe/verification/{name}_beta_{bits}.json"
    refs = {row["k"]: row for row in json.loads(old_path.read_text())["probes"]} if old_path.exists() else {}
    out = {
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidate": name,
        "precision_bits": bits,
        "source_sha256": digest(path),
        "projection_sha256": digest(destination(name)),
        "projection_code_sha256": metadata["code_sha256"],
        "code_sha256": digest(Path(__file__)),
        "projection_proof_sha256": digest(BASE/"PROOF.md"),
        "probe_proof_sha256": digest(ROOT/"research/localized_weak_probe/PROOF.md"),
        "beta_proof_sha256": digest(ROOT/"research/localized_weak_probe/BETA_EVALUATION.md"),
        "comparison_reference_sha256": digest(old_path) if refs else None,
        "membership_evidence": evidence,
        "scope": "Necessary L2 correction radius at fixed c; complete background modes; N4-ORIGIN pending peer reproduction.",
        "probes": [],
    }
    print("prepared", name, "seconds", time.monotonic()-start, flush=True)
    for k in ks:
        tick = time.monotonic()
        weight = arb_poly([5, 2*k-4])
        B2 = arb.pi()/2*sum((integral(P*weight*weight, b, 2*k+1) for b, P in bg.items()), arb(0))
        C2 = arb.pi()/2*sum((integral(P, b, 2*k+1) for b, P in cg.items()), arb(0))
        a = Q(2*k+2)
        l0 = 3*model.c+1+2*model.c*k
        l1 = 2*model.c*(k+2)
        A2 = arb.pi()/2*ar((l0*l0-2*l0*l1*a/(a+2)+l1*l1*a*(a+1)/((a+2)*(a+3)))/(a*(a+1)))
        assert A2 > 0 and B2 > 0 and C2 > 0
        A, B, C = A2.sqrt(), B2.sqrt(), C2.sqrt()
        D = A+B+C
        pair = arb.pi()/2*sum((integral(P, ell*model.delta/2-1, k+1) for ell, P in F), arb(0))
        I = abs(pair)
        assert I > 0
        H = arb(1) if k == 0 else supremum(k, 2)+2*k*supremum(k, 3)+4*supremum(k+1, 2)
        radius = 2*I/(D+(D*D+4*H*I).sqrt())
        vals = {"pairing": pair, "A": A, "B_weighted": B, "C": C, "D": D,
                "gradient_sup_upper_ball": H, "L2_radius_lower": radius}
        comparison = {key: value.overlaps(arb(refs[k][key])) for key, value in vals.items()} if k in refs else {}
        assert all(comparison.values())
        out["probes"].append({
            "k": k, **{key: value.str(80) for key, value in vals.items()},
            "full_residual_reference_comparisons": comparison,
            "elapsed_seconds": time.monotonic()-tick,
        })
        out["total_elapsed_seconds"] = time.monotonic()-start
        dest = BASE/f"verification/{name}_probe_{bits}.json"
        dest.write_text(json.dumps(out, indent=2)+"\n")
        print("k", k, "pair", pair.str(16), "L2 lower", radius.str(22),
              "comparisons", len(comparison), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate")
    parser.add_argument("--k", nargs="+", type=int, default=[0, 128, 512, 1024])
    parser.add_argument("--bits", type=int, default=2048)
    args = parser.parse_args()
    assert all(k >= 0 for k in args.k)
    run(args.candidate, args.k, args.bits)
