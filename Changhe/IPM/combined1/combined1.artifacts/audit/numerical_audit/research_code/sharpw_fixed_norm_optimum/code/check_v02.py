"""Exact fixed-norm scalar maximum, reciprocal source bindings and report repair."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json, re, sys, time
from flint import arb, ctx, fmpq

R = Path(__file__).resolve().parents[3]
B = R / "research/sharpw_fixed_norm_optimum"
S = B / "source"
sys.set_int_max_str_digits(0)


def main():
    start = time.monotonic()
    inputs, external, checks = {}, {}, {}
    sha = lambda p: sha256(Path(p).read_bytes()).hexdigest()

    def bind(p, h=None):
        p = Path(p).resolve()
        v = sha(p)
        assert h is None or h == v, (str(p), h, v)
        try:
            key, target = str(p.relative_to(R)), inputs
        except ValueError:
            key, target = str(p), external
        assert key not in target or target[key] == v
        target[key] = v
        return p

    def read(p, h=None):
        return json.loads(bind(p, h).read_text())

    def ck(label, value):
        assert label not in checks
        checks[label] = bool(value)
        assert value, label

    def ball(s):
        m = re.fullmatch(r"\[([^\s]+) \+/- ([^\]]+)\]", s)
        assert m, s
        c, e = map(Q, m.groups())
        return c - e, c + e

    mf = read(S / "MANIFEST.json")
    ck("proof_first", not mf["checker_exists"])
    bind(B / "PROOF.md", mf["proof_sha256"])
    bind(Path(__file__))
    for row in mf["files"].values():
        bind(R / row["path"], row["sha256"])
        bind(row["source"], row["sha256"])
    p = read(S / "parameters.json", mf["parameters_sha256"])
    p = {k: Q(v) for k, v in p.items()}
    t2 = read(S / "T2_max_result.json")
    repaired = read(S / "T2_repair_result.json")
    t4 = read(S / "T4_479_result.json",
              "db307cd256cf766c0f3ec53cfea77c124b5be258ea0664e64280786bb1e1b569")
    defect = read(S / "T4_defect_result.json",
                  "5c76f8b270fd9365047d06745a3ad85e161f52e710f5107669b11dac33dc6cae")
    ck("T2_primary_counts", t2["checks"] == 17 and not t2["fails"])
    ck("T2_repair_counts", repaired["checks"] == 12 and not repaired["fails"])
    ck("T2_logs", "17 checks, 0 FAIL" in (S / "T2_max_log.txt").read_text()
       and "12 checks, 0 FAIL" in (S / "T2_repair_log.txt").read_text())
    ck("T4_proof_binding", t4["proof_sha256"] == sha(S / "T4_479_PROOF.md"))
    ck("T4_defect_proof_binding", defect["proof_sha256"] == sha(S / "T4_defect_PROOF.md"))
    mu0, C, s, kappa = [p[k] for k in ["mu0", "C", "s", "kappa"]]
    ck("fixed_norm", s == Q(1, 5184) and p["w1"] == 2**15 and p["w2"] == 2**20)
    ck("exact_square_root", Q(1, 72)**2 == s)
    mu, A = mu0 - C * s, kappa * 72
    r, eta = mu / (2 * A), mu**2 / (4 * A)
    ck("positive_constants", mu == Q(201799, 648000) > 0 and A == Q(576, 5) > 0)
    ck("optimum_values", r == p["new_r"] == Q(t2["r_star"]) == Q(repaired["r_star"])
       and eta == p["new_eta"] == Q(t2["eta_star"]) == Q(repaired["eta_star"]))
    # Coefficients of eta-A*(x-r)^2 are exactly those of mu*x-A*x^2.
    ck("polynomial_identity_all_real_r",
       [eta - A*r*r, 2*A*r, -A] == [Q(0), mu, -A])
    ck("attainment", mu - A*r == mu/2 > 0 and r*(mu-A*r) == eta)
    beta0 = mu - A*p["old_r"]
    at0 = beta0*p["old_r"]
    ck("old_exact_beta", beta0 == Q(63092119, 405000000))
    ck("old_exact_product", at0 == Q(85237452769, 405000000000000)
       == Q(repaired["beta_r_at_1351e-6"]))
    ck("selected_beta_floor", beta0 > Q(1557, 10000)
       and p["old_eta"] <= Q(1557, 10000)*p["old_r"])
    ck("strict_improvement", p["old_eta"] < Q("2.1046e-4") < at0 < eta < Q("2.1047e-4"))
    ck("relative_improvement", Q("1.0005") < eta/p["old_eta"] < Q("1.0006"))
    cs2_upper = 1/(4*p["pi_lower"]*s*(1+s))
    contraction_square = cs2_upper*r*r
    ck("cs_square_rational", contraction_square == Q(40722836401, 54043470895104)
       == Q(t2["cs_r_star_sq_upper"]) < Q(".02746")**2)
    ck("contraction_and_slope", Q(".02746")/2 == Q(".01373") < 1
       and Q(7, 10)-Q(".02746") == Q(".67254") > 0)
    ctx.prec = 1024
    aq = lambda x: arb(fmpq(x.numerator, x.denominator))
    pi = arb.pi()
    ck("pi_lower_verified", pi > aq(p["pi_lower"]))
    csr = aq(r)/(4*pi*aq(s)*aq(1+s)).sqrt()
    ck("independent_cs_ball", csr > 0 and csr < aq(Q(".02746")))
    box = next(x for x in defect["boxes"] if x["name"] == "sharpw"
               and Q(x["m"]) == 0 and Q(x["B"]) == 0)
    ck("defect_zero_trial", Q(box["r"]) == r and Q(box["beta"]) == mu/2
       and Q(box["epsilon_at_r"]) == eta == Q(box["epsilon_optimum"]))
    witness = t4["stronger_registered_residual_witness"]
    ck("T4_max_witness", Q(witness["r"]) == r and Q(witness["beta"]) == mu/2
       and Q(witness["epsilon_exact"]) == eta and witness["weights"] == [32768, 1048576])
    ck("defect_identity", ((mu-A*0-0)**2-4*A*0*0)/(4*A) == eta)
    s0 = mu0/(5*C)
    # Derivative numerator: (mu0-C*x)*(mu0-5*C*x).
    ck("other_s_critical", s0 == Q(97, 496250) == Q(t2["s0"])
       and mu0-C*s0 == 4*C*s0 > 0)
    sup2 = Q(25, 4)*C**4*s0**5
    ck("other_s_larger_scalar", sup2 > eta**2)
    supremum = aq(sup2).sqrt()
    sl, su = ball(t2["sup_over_s_arb"])
    ck("other_s_ball", supremum > aq(sl) and supremum < aq(su))
    original = (S / "frozen_report.md").read_text().splitlines()
    for name, lo, hi in [("brief", 22, 26), ("short", 110, 116)]:
        text = " ".join(original[lo-1:hi])
        ck("original_max_attribution:"+name,
           "largest admissible" in text and "2.1035e-4" in text and "sharpw-v1" in text)
    excerpt = {}
    for line in (S / "repaired_excerpt.txt").read_text().splitlines():
        n, value = line.split("\t", 1)
        ck("unique_excerpt_line:"+n, int(n) not in excerpt)
        excerpt[int(n)] = value
    ck("excerpt_ranges", sorted(excerpt) == list(range(22, 32))+list(range(118, 129))
       + list(range(380, 386))+list(range(468, 473)))
    for name, lo, hi in [("brief", 22, 31), ("short", 118, 128), ("defect", 380, 385)]:
        text = " ".join(excerpt[i] for i in range(lo, hi+1))
        ck("repaired_exact_fractions:"+name, str(eta) in text and str(r) in text
           and "T4-479" in text and "g = 0" in text)
    ck("radius_display", Q("1.35155e-3") <= r < Q("1.35165e-3"))
    oldbase = R / "research/registered_norm_assembly"
    old = read(oldbase / "verification/result.json",
               "78210aeee3ae5f7f215dc4058ac20120fc5158b78ce8b668555a5bcf2f449c48")
    for name, h in old["inputs"].items():
        bind(oldbase / name, h)
    revision = read(B / "verification/PROOF_FIRST_v02.json")
    ck("revision_proof_first", not revision["checker_v02_exists"])
    bind(B / "PROOF_v02.md", revision["proof_sha256"])
    bind(B / "verification/FAILED_v01.json", revision["failed_record_sha256"])
    oldmf = read(oldbase / "source/MANIFEST.json")
    historical_current_observations = {}
    for name, row in oldmf["files"].items():
        bind(oldbase / "source" / name, row["sha256"])
        # A mutable peer program is preserved by its old frozen copy.
        if not name.startswith("N3_"):
            bind(row["source"], row["sha256"])
        else:
            historical_current_observations[row["source"]] = sha(row["source"])
    inst = next(x for x in old["instances"] if x["label"] == "sharpw")
    low, high = ball(inst["lower_comparison"]["ball"])
    ck("007_same_norm", Q(inst["s_exact"]) == s and inst["w1"] == p["w1"]
       and inst["w2"] == p["w2"] and inst["sufficient_threshold_strictly_failed"])
    ck("007_lower_comparison", low > p["X007_floor"] > 0
       and inst["lower_comparison"]["strict_bounds_verified"]
       and all(inst["peer_printed_nesting"].values()))
    ck("007_new_factor", p["X007_floor"]/eta > 3594606)
    ck("007_old_factor", p["X007_floor"]/p["old_eta"] > Q("3596535.57"))
    ck("repair_factor_text", "3594606" in excerpt[28] and "756.5312630768" in excerpt[472])
    for rel, h in inputs.items():
        assert sha(R/rel) == h
    for rel, h in external.items():
        assert sha(rel) == h
    out = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": time.monotonic()-start,
        "check_count": len(checks), "checks": checks,
        "inputs": inputs, "external_inputs": external,
        "historical_peer_current_hash_observations": historical_current_observations,
        "fixed_s": str(s), "weights": [32768, 1048576],
        "mu": str(mu), "A": str(A), "r_star": str(r), "eta_star": str(eta),
        "beta_r_at_old_radius": str(at0),
        "cs_rstar_square_upper_exact": str(contraction_square),
        "other_s_star": str(s0), "other_s_maximum_square_exact": str(sup2),
        "X007_floor_exact": str(p["X007_floor"]),
        "X007_over_eta_star_strict_lower_exact": str(p["X007_floor"]/eta),
        "configured_peer_model": "us.anthropic.claude-opus-5-5",
        "actual_provider_response_observed": False,
        "peer_code_executed": False, "source_integrals_recomputed": False,
        "verdict": "CONFIRMED fixed-norm scalar maximum, T4-479 witness and T2 reviews/repair arithmetic. REFUTED original unrestricted selected-threshold maximality. No candidate existence, optimality over different norms, or new correction-distance conclusion."
    }
    target = B / "verification/result.json"
    with target.open("x") as f:
        json.dump(out, f, indent=2)
        f.write("\n")
    print(out["utc"], len(checks), "checks", len(inputs), "local", len(external),
          "external", sha(target), "seconds", out["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
