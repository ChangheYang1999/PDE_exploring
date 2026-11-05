#!/usr/bin/env python3
"""Exact-input, outward-Arb closure arithmetic. It never declares existence.

Run with the shared environment and -B. Imported combined2 code is read-only.
Every exploratory input is labeled; passing scalar arithmetic does not discharge
the background-form or numerical-certificate obligations.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
OLD = HERE.parents[1] / "combined2" / "IPM.artifacts"
CGDIR = OLD / "theory_agent_2/research/closure_check/ps1copy/ps1"
sys.path.insert(0, str(CGDIR))
import ce_gen as CG
from flint import arb, fmpq, ctx

ctx.prec = 256


def aa(v):
    v = Q(v)
    return arb(fmpq(v.numerator, v.denominator))


def decimal_bound(x, direction, digits=18):
    """Return an exact rational decimal bounded on the requested side of x."""
    assert direction in (-1, 1)
    scale = 10**digits
    z = x.lower() if direction < 0 else x.upper()
    # This floating guess is verified and adjusted by Arb comparisons below.
    n = int(float(z) * scale)
    span = 1
    if direction < 0:
        lo, hi = n-1, n+1
        while not aa(Q(lo, scale)) <= x:
            span *= 2
            lo = n-span
        span = 1
        while aa(Q(hi, scale)) <= x:
            span *= 2
            hi = n+span
        while hi-lo > 1:
            mid = (hi+lo)//2
            if aa(Q(mid, scale)) <= x:
                lo = mid
            else:
                hi = mid
        n = lo
    else:
        lo, hi = n-1, n+1
        while not x <= aa(Q(hi, scale)):
            span *= 2
            hi = n+span
        span = 1
        while x <= aa(Q(lo, scale)):
            span *= 2
            lo = n-span
        while hi-lo > 1:
            mid = (hi+lo)//2
            if x <= aa(Q(mid, scale)):
                hi = mid
            else:
                lo = mid
        n = hi
    return str(Q(n, scale))


def enclosure(x):
    return {"arb": str(x), "lower": decimal_bound(x, -1),
            "upper": decimal_bound(x, 1)}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--beta-l2", default="7/4")
    ap.add_argument("--beta-status", default="INHERITED_WITH_PREMISES")
    ap.add_argument("--matrix-beta", default="704955805507/1000000000000")
    ap.add_argument("--near-loss", default="152627111489/1000000000000")
    ap.add_argument("--epsilon", default="0")
    ap.add_argument("--low-price", default="113428316345")
    ap.add_argument("--rest-price", default="0")
    ap.add_argument("--M", default="387/1000")
    ap.add_argument("--source", default="0.0055545729030073655758")
    ap.add_argument("--dual-residual", help="Certified or exploratory d_F upper; requires stated status")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    p = {k: Q(getattr(args, k.replace('-', '_'))) for k in
         ("beta-l2", "matrix-beta", "near-loss", "epsilon", "low-price", "rest-price", "M", "source")}
    assert p["beta-l2"] > 0 and 0 < p["M"] <= Q(1, 2)
    assert all(p[k] >= 0 for k in ("near-loss", "epsilon", "low-price", "rest-price", "source"))
    f = Q("7961206656880281/10000000000000000000000")
    R = f / p["beta-l2"]
    weight = CG.Weight(Q(1), Q(1, 2), Q(9619, 5000))
    _, rho1, rho2 = weight.best_rhos(float(R), float(p["M"]))
    K = weight.certify_K(R, p["M"], rho1, rho2)
    witness = aa(K) - aa(p["M"]) - weight.E(aa(R), aa(K), rho1, rho2)
    assert witness > 0  # CE proof is an independent retained analytic premise.
    B, A = Q(13, 25), Q(18959, 1000)
    loss = weight.loss(aa(R), aa(K), B, A)
    b0 = p["matrix-beta"] - p["near-loss"] - p["epsilon"]
    bprime = aa(b0) - loss
    neff = aa(p["source"])
    matrix_threshold_pass = True
    if args.dual_residual is not None:
        d = aa(Q(args.dual_residual))
        assert d >= 0
        neff = aa(p["matrix-beta"]).sqrt() * d
        matrix_threshold_pass = bool(aa(p["M"]) >= d/(2*aa(p["matrix-beta"]).sqrt()))
    capacity = aa(p["M"])*(bprime*aa(p["M"]) - neff)/aa(R)**2
    full_price = p["low-price"] + p["rest-price"]
    margin = aa(p["M"])*(bprime*aa(p["M"]) - neff) - aa(full_price*R*R)
    remainder_allowance = capacity - aa(p["low-price"])
    q = aa(Q(21, 10))
    # If |E| <= A_der ||J^(q-1)g||² is ever proved, weighted issues
    # must be resolved first; these are scalar Young constants only.
    interpolation = []
    for eps in (Q(1, 1000), Q(1, 100), Q(1, 10)):
        for ader in (Q(100), Q(1000), Q(10000), Q(100000)):
            ceps = ((q-1)/q)**(q-1) * aa(ader)**q / (q * aa(eps)**(q-1))
            interpolation.append({"epsilon":str(eps), "stipulated_A":str(ader), "C_epsilon":enclosure(ceps),
                                  "status":"SCALAR_ONLY_NO_OPERATOR_ESTIMATE"})
    result = {
        "created_utc":datetime.now(timezone.utc).isoformat(),
        "status":"CONDITIONAL_SCALAR_ARITHMETIC",
        "theorem_proved":False,
        "program_sha256":sha(Path(__file__).resolve()),
        "inherited_program_sha256":sha(CGDIR/"ce_gen.py"),
        "input":{k:str(v) for k,v in p.items()},
        "beta_status":args.beta_status,
        "f":str(f), "R":str(R), "rho1":str(rho1), "rho2":str(rho2), "K":str(K),
        "B_CE":str(B), "A_CE":str(A),
        "CE_witness":enclosure(witness), "L_B":enclosure(loss),
        "b0":str(b0), "bprime":enclosure(bprime),
        "effective_residual":enclosure(neff),
        "total_low_price":str(full_price), "price_capacity":enclosure(capacity),
        "remaining_price_allowance":enclosure(remainder_allowance),
        "selfmap_margin":enclosure(margin),
        "contraction_ratio_upper":str(Q(28,25)*p["M"]/p["beta-l2"]),
        "scalar_checks":{
            "CE_witness_strict":bool(witness>0), "bprime_positive":bool(bprime>0),
            "matrix_source_threshold":matrix_threshold_pass,
            "selfmap_nonnegative":bool(margin>=0),
            "contraction_below_one":bool(Q(28,25)*p["M"] < p["beta-l2"]),
            "reference_radius":R<=Q(17,8750000)},
        "open_obligations":["Complete quantitative actual background commutator form",
                            "All new numerical inputs require rigorous whole-plane enclosures",
                            "Independent full dependency review"],
        "young_interpolation_exploration":interpolation,
    }
    target=Path(args.output)
    assert target.resolve().is_relative_to(HERE)
    with target.open("x") as out:
        json.dump(result,out,indent=2)
        out.write("\n")
    print(json.dumps({k:result[k] for k in ("status","R","L_B","b0","price_capacity","remaining_price_allowance","selfmap_margin","scalar_checks")},indent=2))


if __name__ == "__main__":
    main()
