#!/usr/bin/env python3
"""Check outward displays and exact rational identities in the final proof."""
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ART = HERE.parent
ctx.prec = 512


def read(p):
    return json.loads(p.read_text())


def sha(p):
    return sha256(p.read_bytes()).hexdigest()


def main():
    final = HERE / "fixed_parameter_closure_v01.json"
    proof = HERE / "FIXED_PARAMETER_THEOREM_PROOF_v01.md"
    rational = ART / "RATIONAL_FINAL_BALL.json"
    root_replay = ART / "ROOT_FINAL_LOCAL_Q_REPLAY.json"
    audit = ART / "independent_closure_audit/final_join_audit.json"
    d = read(final)
    assert d["status"] == "FINAL_NUMERICAL_CLOSURE_PASS"
    assert read(root_replay)["status"] == "ROOT_INDEPENDENT_FINAL_LOCAL_Q_NUMERICAL_PASS"
    assert read(root_replay)["consumer_result_sha256"] == sha(final)
    assert read(audit)["status"] == "INDEPENDENT_FINAL_SCALAR_JOIN_PASS"
    assert read(rational)["status"] == "EXACT_RATIONAL_FIXED_PARAMETER_BALL_PASS"
    assert d["selected"]["M"] == "3/10"
    c, s = d["constants"], d["selected"]
    upper = {
        "K1": "483.477", "K0": "117.012", "Wu2": "5.348",
        "source_H1": "14.831", "source_A2": "222.177",
        "source_Aq": "247.658", "M2u": "10.993", "M3u": "50.955",
        "M3xu": "92.811", "R3_coefficient": "15.430",
    }
    for key, bound in upper.items():
        assert arb(c[key]) < arb(bound)
    for group, bounds in [
        ("Db", {"1": "17.012", "2": "10.466", "3": "28.415", "4": "992.321"}),
        ("Dxb", {"2": "57.994", "4": "279.212"}),
    ]:
        for key, bound in bounds.items():
            assert arb(c[group][key]) < arb(bound)
    for key, bound in [
        ("background_loss", ".157652150"), ("nonlinear_loss", ".227998902"),
        ("contraction_ratio", ".122235"), ("nonlinear_loss", ".228"),
    ]:
        assert arb(s[key]) < arb(bound)
    assert arb(s["frozen_exterior_decay"]) > arb(".314348949")
    assert arb(s["selfmap_energy_margin"]) > arb(".0260144054")
    for key, bound in [
        ("lower_source_near", ".062680871151"),
        ("transport_third", ".012591769585"),
        ("source_principal", ".048512437102"),
    ]:
        assert arb(s["rates"][key]) < arb(bound)
    assert arb(s["far_source_rate"]) < arb(".0308328987471")
    r, m = F(381377, 10**12), F(3, 10)
    beta2, f2, n = F(2087491, 10**6), F(7961207, 10**13), F(759, 100000)
    eps, weak = F(3491, 31250), F(28427625600)
    b0 = F(7, 10)-eps
    bp = b0-F(57, 250)
    assert b0 == F(9192, 15625) and bp == F(11259, 31250)
    assert r*beta2-f2 == F(355107, 10**18)
    margin = bp*m*m-n*m-weak*r*r
    assert margin == F(8129427150678683343, 312500000000000000000)
    assert margin > F(260141, 10**7)
    assert F(25)*m*m/(11*F(157, 50)*beta2*beta2) < F(123, 1000)**2
    paths = [final, proof, rational, root_replay, audit, Path(__file__)]
    result = {
        "status": "FINAL_PROOF_NUMERICAL_DISPLAYS_PASS",
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "bindings": {str(p.relative_to(ART)): sha(p) for p in paths},
        "exact_rational_selfmap_margin": str(margin),
        "scope": "Outward displayed numerical bounds and exact rational identities only; analytic proof and complete producer certificates are separate linked dependencies.",
    }
    (HERE / "final_proof_numbers_v01.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
