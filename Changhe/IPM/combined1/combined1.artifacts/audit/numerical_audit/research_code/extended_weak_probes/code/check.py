"""Exact extended weak probes, with fixed-background row scale diagnostics."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import json
import sys
import time
from flint import fmpq as Q, arb, arb_poly, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/extended_weak_probes"
NAME = "C1-N1-007-d2w-j7-e2bal"
KS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 24, 32, 48, 64, 96,
      128, 192, 256, 384, 512, 768, 1024, 1536, 2048, 3072, 4096]
sys.path.insert(0, str(ROOT / "research/projected_residual/code"))
from build import candidate_source, read_projection, destination
sys.path.insert(0, str(ROOT / "research/localized_weak_probe/code"))
from beta_scale import integral, supremum, groups, ap, ar, Radial, U
sys.set_int_max_str_digits(0)


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def main():
    start = time.monotonic()
    ctx.prec = 2048
    src = candidate_source(NAME)
    assert digest(src) == "153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316"
    oldpath = ROOT / "research/weak_mesh_comparison/verification/candidate007.json"
    old = {row["k"]: row["exact_balls"] for row in json.loads(oldpath.read_text())["rows"]}
    refpath = ROOT / f"research/projected_residual/verification/{NAME}_probe_2048.json"
    refs = {row["k"]: row for row in json.loads(refpath.read_text())["probes"]}
    peerpath = BASE / "source/N1_candidate007.json"
    peer = json.loads(peerpath.read_text(), parse_float=str)
    assert peer["sha256"] == "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21"
    assert peer["k_list"] == KS
    model = Radial(src)
    projected, metadata = read_projection(NAME)
    F = [(ell, ap(P(U))) for ell, P in projected.items()]
    bg = groups(model, ["u1", "u2"])
    cg = groups(model, ["rho_x", "rho_y"])
    radius = ar(Q(3793, 10**9))
    D0 = arb(old[0]["D"])
    rows = []
    for k in KS:
        tick = time.monotonic()
        if k in old:
            vals = {key: arb(value) for key, value in old[k].items()}
        else:
            weight = arb_poly([5, 2*k-4])
            B2 = arb.pi()/2 * sum((integral(P*weight*weight, b, 2*k+1)
                                  for b, P in bg.items()), arb(0))
            C2 = arb.pi()/2 * sum((integral(P, b, 2*k+1)
                                  for b, P in cg.items()), arb(0))
            aa = Q(2*k+2)
            l0 = 3*model.c+1+2*model.c*k
            l1 = 2*model.c*(k+2)
            A2 = arb.pi()/2 * ar(
                (l0*l0-2*l0*l1*aa/(aa+2)+l1*l1*aa*(aa+1)/((aa+2)*(aa+3)))
                /(aa*(aa+1)))
            assert A2 > 0 and B2 > 0 and C2 > 0
            A, B, C = A2.sqrt(), B2.sqrt(), C2.sqrt()
            D = A+B+C
            pairing = arb.pi()/2 * sum((integral(P, ell*model.delta/2-1, k+1)
                                        for ell, P in F), arb(0))
            I = abs(pairing)
            assert I > 0
            H = supremum(k, 2)+2*k*supremum(k, 3)+4*supremum(k+1, 2)
            m = 2*I/(D+(D*D+4*H*I).sqrt())
            vals = dict(pairing=pairing, I=I, A=A, B=B, C=C, D=D, H=H, m=m)
        assert all(v.rel_accuracy_bits() > 150 for v in vals.values())
        expected = {"pairing": "pairing", "A": "A", "B": "B_weighted",
                    "C": "C", "D": "D", "H": "gradient_sup_upper_ball",
                    "m": "L2_radius_lower"}
        overlaps = ({key: bool(vals[key].overlaps(arb(refs[k][pk])))
                     for key, pk in expected.items()} if k in refs else {})
        assert all(overlaps.values())
        peerkeys = {"I": "I_k", "A": "A_k", "B": "B_k", "C": "C_k",
                    "D": "D_k", "H": "H_k", "m": "m_lower_bound"}
        differences = {}
        for key, pk in peerkeys.items():
            floating = ar(Q(str(Fraction(peer["NORM-T-WEAK-v1_a0"][str(k)][pk]))))
            differences[key] = ((floating-vals[key])/vals[key]).str(45)
        threshold = vals["D"]*radius+vals["H"]*radius*radius
        row = {
            "k": k,
            "exact_balls": {key: value.str(80) for key, value in vals.items()},
            "reused_immutable_k0_to8": k in old,
            "previous_exact_overlap": overlaps,
            "peer_relative_difference": differences,
            "radius": "3793/1000000000",
            "necessary_pairing_ceiling_ball": threshold.str(60),
            "ratio_to_necessary_ceiling": (vals["I"]/threshold).str(60),
            "linear_penalty_weight_relative_to_k0": ((D0/vals["D"])**2).str(60),
            "elapsed_seconds": time.monotonic()-tick,
        }
        rows.append(row)
        print("k", k, "m", vals["m"].str(20), "D", vals["D"].str(16),
              "row weight", row["linear_penalty_weight_relative_to_k0"],
              "seconds", row["elapsed_seconds"], flush=True)
    best = max(rows, key=lambda row: float(arb(row["exact_balls"]["m"]).mid()))
    # Certify the finite-list ordering using disjoint enclosures.
    assert all(arb(best["exact_balls"]["m"]) > arb(row["exact_balls"]["m"])
               for row in rows if row["k"] != best["k"])
    paths = [src, destination(NAME), oldpath, refpath, peerpath,
             BASE/"source/N1_weak_tests2.py", Path(__file__), BASE/"PROOF.md",
             ROOT/"research/projected_residual/code/build.py",
             ROOT/"research/localized_weak_probe/code/beta_scale.py",
             ROOT/"research/localized_weak_probe/code/evaluate.py",
             ROOT/"research/radial_fourier/code/radial.py"]
    out = {
        "utc": datetime.now(timezone.utc).isoformat(), "candidate": NAME,
        "precision_bits": ctx.prec, "inputs": {str(p.relative_to(ROOT)): digest(p) for p in paths},
        "rows": rows, "best_tested_k": best["k"], "best_exact_ball": best["exact_balls"]["m"],
        "strict_finite_list_ordering": True, "elapsed_seconds": time.monotonic()-start,
        "status": "OPEN peer for new exact values; prior k0/128/512/1024 comparisons retained",
    }
    with (BASE/"verification/candidate007.json").open("x") as f:
        json.dump(out, f, indent=2)
        f.write("\n")
    print("DONE", out["elapsed_seconds"], "best", best["k"], out["best_exact_ball"], flush=True)


if __name__ == "__main__":
    main()
