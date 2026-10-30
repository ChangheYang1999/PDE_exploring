from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib
import json
import time
from flint import arb, ctx

B = Path(__file__).resolve().parents[1]
start = time.monotonic()
ctx.prec = 768
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
m = json.loads((B / "data/manifest.json").read_text())
assert sha(B / "PROOF.md") == m["proof_sha256"]
for rel, digest in m["inputs"].items():
    assert sha(B / rel) == digest, rel
p = json.loads((B / "data/parameters.json").read_text())
old = json.loads((B / "source/cutoff_result.json").read_text())
oldrows = {r["candidate"]: r for r in old["rows"]}
checks = []


def A(x):
    f = Q(str(x))
    return arb(f.numerator) / f.denominator


def interval(s):
    if s.startswith("["):
        v, e = s.strip("[]").split("+/-")
        return arb(v.strip(), e.strip())
    return A(s)


def check(label, claim):
    assert bool(claim), label
    checks.append(label)


c = Q(p["c"])
q = 1 / c - 4
d = 1 - 1 / c
k = 1 - q
D = 5 * c - 1
alpha = -2 * q - 2
f = k / (k + d)
u = Q(p["relaxed_universal"])
emin = (-q - 1) / (2 * (-q) * (-q - 3))
lam = A(1) / 2 + 5 * A(2) ** A(1 - q)
check("exponent identities", -5 < q < -3 and 0 < d < q + 5 and D == c * k)
check("Green integral powers", q - 2 == -k - 1 and c * (k + d) == D / f)
check("fallback branch joins", u * (1 - d / (k + d)) == u * f)
check("u is strictly a relaxed lower bound", emin > u)
check("lambda > 109.6", lam > A("109.6"))
check("average factor > .908", f > Q("0.908"))
check("seven peer groups", (B / "source/T1_log.txt").read_text().count("\nPASS ") == 6)
rows = []
for name, angle in p["angles"].items():
    ep = json.loads((B / f"data/{name}_endpoint.json").read_text())
    F = {int(n): Q(v) for n, v in ep["F12"].items()}
    P = {int(n): Q(v) for n, v in ep["P"].items()}
    th = {int(n): Q(v) for n, v in ep["Theta0"].items()}
    ns = set(F) | set(P)
    pp = sum(P.get(n, 0) ** 2 for n in ns)
    proj = sum(F.get(n, 0) ** 2 for n in ns)
    proj -= sum(F.get(n, 0) * P.get(n, 0) for n in ns) ** 2 / pp
    check(name + ": exact projection positive", pp > 0 and proj > 0)
    b = (arb.pi() * A(proj)).sqrt() / (4 * A(c))
    t = A(angle)

    def ev(cf, derivative=False):
        return sum(
            A(v) * n * (n * t).cos() if derivative else A(v) * (n * t).sin()
            for n, v in cf.items()
        )

    fv, fd, pv, pd = ev(F), ev(F, True), ev(P), ev(P, True)
    phi = abs(A(q) * (fv * pd - fd * pv))
    phi /= 4 * A(c) * (A(q * q) * pv * pv + pd * pd).sqrt()
    g0 = sum(n * v for n, v in th.items())
    check(name + ": endpoint matches421", b.overlaps(interval(oldrows[name]["B"]))
          and phi.overlaps(interval(oldrows[name]["Phi"]))
          and g0 == Q(oldrows[name]["g0_exact"]))
    su = (lam * A(g0) / A(D)) ** A(1 / d)
    row = {"candidate": name, "B": b.str(50), "Phi": phi.str(50),
           "g0_exact": str(g0), "fallback_switch": su.str(50), "targets": {}}
    for target, beta in p["betas"].items():
        tag = name + ":" + target
        rb = (b / (A(beta) * A(alpha).sqrt())) ** A(1 / (-q - 1))
        K = A(D) * b * rb ** A(d) / ((2 * arb.pi()).sqrt() * A(g0) * phi)
        j = lam * A(u * g0 / D) / rb ** A(d)
        jr = A(f) * j
        ef = A(u) * (1 - A(d / (k + d)) * (rb / su) ** A(k))
        check(tag + ": K below relaxed fallback", K < A(u))
        check(tag + ": source cutoff matches", K.overlaps(
            interval(oldrows[name]["targets"][target]["Ecrit_upper"])))
        check(tag + ": rounded outer lower", j > A(p["J_lower"][target]))
        check(tag + ": constant obstruction", j > K)
        check(tag + ": averaged ratio > 4.34", jr / K > A("4.34"))
        check(tag + ": switch beyond cutoff", su > rb)
        check(tag + ": fallback obstruction", ef > K)
        check(tag + ": printed .7930 is too high", ef < A(u))
        check(tag + ": repaired fallback > .7929999", ef > A("0.7929999"))
        vals = {"r_beta": rb.str(50), "K": K.str(50), "outer_lower": j.str(50),
                "averaged_outer_lower": jr.str(50), "averaged_ratio": (jr / K).str(50),
                "fallback_lower": ef.str(50), "thresholds": {}}
        for ps in p["profile_coefficients"]:
            prof = Q(ps)
            if A(prof) >= K:
                check(tag + ps + ": no room entry", Q(p["threshold_upper"][ps][target]) == 0)
                vals["thresholds"][ps] = {"no_room": True}
                continue
            room = K - A(prof)
            y0 = room / A(f)
            multiplier = A(D) * rb ** A(d) / A(u * g0)
            lc = y0 * multiplier
            if K <= A(prof + f * (u - prof)):
                y = y0
                gy = A(prof) + A(f) * y
                branch = "unsaturated"
            else:
                check(tag + ps + ": positive saturated gap", A(u) > K)
                y = A(u - prof) * (A((1 - f) * (u - prof)) / (A(u) - K)) ** A(d / k)
                gy = A(u) - A((1 - f) * (u - prof)) * (y / A(u - prof)) ** A(-k / d)
                branch = "saturated"
            lf = y * multiplier
            check(tag + ps + ": inverse identity", gy.overlaps(K))
            check(tag + ps + ": constant table", lc < A(p["threshold_upper"][ps][target]))
            upper = p["fallback_fixed_upper"][ps] if target == "fixed_sharpw_ball" else p["threshold_upper"][ps][target]
            check(tag + ps + ": fallback table", lf < A(upper))
            check(tag + ps + ": fallback cannot lower threshold",
                  lf.overlaps(lc) or lf > lc)
            check(tag + ps + ": uniform bounds", lc < A("25.3") and lf < 29)
            check(tag + ps + ": factor3.75 gap", lc * A("3.75") < lam and lf * A("3.75") < lam)
            vals["thresholds"][ps] = {
                "constant": lc.str(50), "fallback": lf.str(50), "branch": branch}
        row["targets"][target] = vals
    rows.append(row)

result = {
    "utc": datetime.now(timezone.utc).isoformat(), "elapsed_s": time.monotonic() - start,
    "precision_bits": ctx.prec, "check_count": len(checks), "checks": checks,
    "q_exact": str(q), "delta_exact": str(d), "average_factor_exact": str(f),
    "lambda": lam.str(50), "universal_lower_exact": str(emin), "rows": rows,
    "proof_sha256": sha(B / "PROOF.md"), "code_sha256": sha(Path(__file__)),
    "manifest_sha256": sha(B / "data/manifest.json"),
    "verdict": "CONFIRMED outer obstruction and necessary kernel thresholds; REFUTED the printed .7930 fallback lower bound and removal of the delta exponent merely by reducing a velocity constant."
}
(B / "verification/result.json").write_text(json.dumps(result, indent=2) + "\n")
print("PASS", len(checks), result["utc"], result["elapsed_s"])
for row in rows:
    print(row["candidate"], "fixed fallback", row["targets"]["fixed_sharpw_ball"]["fallback_lower"])
