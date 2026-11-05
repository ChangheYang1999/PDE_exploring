#!/usr/bin/env python3
"""Execute the improved A/B data in the inherited N closure arithmetic.

The old high-energy/CE premises remain explicit. This comparison is not
the preferred local-Q theorem certificate and never claims existence.
"""
import hashlib
import json
import sys
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
from flint import arb, ctx

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
OLD = HERE.parents[1] / "combined2/IPM.artifacts"
sys.path.insert(0, str(OLD / "theory_agent_2/research/closure_check/ps1copy/ps1"))
import ce_gen as CG


def aa(x):
    x = F(x)
    return arb(x.numerator) / arb(x.denominator)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ctx.prec = 320
    source = HERE / "coercivity_residual/full_matrix_residual_m115_v01.cert.json"
    data = json.loads(source.read_text())
    row = data["by_beta"]["13999/20000"]
    beta_o = F(13999, 20000)
    near = F(152627111489, 10**12)
    eps = F(2328694018, 10**12)
    beta = aa(beta_o - near - eps)
    norm = aa(data["inherited_source_norm_upper"])
    coord = arb(data["absolute_coordinate_lower"])
    coord = coord.lower()
    gamma = arb(row["Gamma_upper"]).upper()
    B = arb(row["B_upper"]).upper()
    d2 = norm * norm / beta - coord * coord / (beta * beta * (gamma + B / beta))
    assert d2 > 0
    deff = d2.sqrt()
    neff = beta.sqrt() * deff
    f2 = F(7961207, 10**13)
    M = F(387, 1000)
    Cnear = F(113428316345)
    Crest = F(9941475955)
    rows = []
    for label, beta_l2, use_matrix in [
        ("inherited_L2_scalar_source", F(7, 4), False),
        ("direct_actual_L2_scalar_source", F(2087491, 10**6), False),
        ("direct_actual_L2_full_matrix_source", F(2087491, 10**6), True),
    ]:
        R = f2 / beta_l2
        weight = CG.Weight(F(1), F(1, 2), F(9619, 5000))
        _, r1, r2 = weight.best_rhos(float(R), float(M))
        K = weight.certify_K(R, M, r1, r2)
        witness = aa(K) - aa(M) - weight.E(aa(R), aa(K), r1, r2)
        assert witness > 0
        loss = weight.loss(aa(R), aa(K), F(13, 25), F(18959, 1000))
        n = neff if use_matrix else norm
        decay = beta - loss
        margin = decay * aa(M)**2 - n * aa(M) - aa((Cnear + Crest) * R * R)
        if use_matrix:
            assert aa(M) > deff / (2 * beta.sqrt())
        rows.append({
            "case": label, "beta_L2": str(beta_l2), "R": str(R),
            "M": str(M), "K": str(K), "rho1": str(r1), "rho2": str(r2),
            "CE_graph_witness": str(witness), "L_B": str(loss),
            "effective_source": str(n), "b_prime": str(decay),
            "low_price": str(Cnear + Crest), "selfmap_energy_margin": str(margin),
            "conditional_scalar_selfmap_pass": bool(decay > 0 and margin > 0),
        })
    out = {
        "status": "EXECUTED_OLD_N_A_B_COMPARISON_WITH_RETAINED_PREMISES",
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "program_sha256": sha(Path(__file__)),
        "source_certificate_sha256": sha(source),
        "inherited_CE_program_sha256": sha(Path(CG.__file__)),
        "baseline_beta_o": str(beta_o), "near_high_loss": str(near),
        "rest_high_loss": str(eps), "remaining_free_baseline": str(beta_o-near-eps),
        "loss_adjusted_matrix_residual_d_upper": str(deff),
        "loss_adjusted_matrix_effective_source": str(neff),
        "rows": rows,
        "retained_premises": [
            "Actual whole-plane M >= 7/10 I (fresh certificate still pending when this comparison was written).",
            "Inherited original-N near/rest form constants and the old CE analytic premise.",
            "Old high-space inverse/domain proof; a scalar pass does not supply it.",
        ],
        "theorem_proved": False,
        "scope": "Priority A/B propagation and comparison only. No transfer of the N residual bound to Q.",
    }
    (HERE / "old_N_actual_AB_comparison.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
