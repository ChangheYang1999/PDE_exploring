"""Check declared decimal endpoints independently, without executing source code."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
from flint import arb, ctx
from brjuno_constants_verify import ball, continued_fraction, convergents


def main():
    ctx.prec = 512
    target = Path("research/27_decimal_bounds/repair")
    for folder in ("sources", "verification"):
        (target / folder).mkdir(parents=True, exist_ok=True)
    src = Path("../a4-num/notes/theoremE_constants_arb.json")
    blob = src.read_bytes()
    source = json.loads(blob)
    (target / "sources/theoremE_constants_arb.json").write_bytes(blob)
    code = Path("../a4-num/code/theoremE_constants_arb.py").read_bytes()
    (target / "sources/theoremE_constants_arb.py.txt").write_bytes(code)
    leading = json.loads(Path("research/02_candidate007/data/leading_exact.json").read_text())
    F007 = sum((abs(Fraction(x)) for x in leading["density"].values()), Fraction())
    assert Fraction(source["alpha1_cand007_exact"]) == F007
    rows = []
    for label, row in source.items():
        if not isinstance(row, dict):
            continue
        dq = Fraction(row["delta"])
        d = ball(dq)
        qs = [q for p, q in convergents(continued_fraction(dq / 2))]
        B = sum((arb(qs[k + 1]).log() / qs[k] for k in range(len(qs) - 1)), arb(0))
        F, L = (F007, 19) if label.startswith("cand007") else (Fraction(1), 1)
        lam = ball(Fraction(3, 2)) + d / 2 + 1 / d
        K = 2 * lam * (L + 2) / (1 / (1 - d) - 1)
        A = 8 * K * (2 * B).exp() * ball(F) / d
        values = {"B_rat": B, "K_c": K, "A": A,
                  "log10_A": A.log() / arb(10).log(),
                  "R0": (A.log() / d).exp()}
        keys = {"B_rat_upper": ("B_rat", "upper"),
                "B_rat_lower": ("B_rat", "lower"),
                "R0_lower": ("R0", "lower"),
                "A_upper_integer": ("A", "upper"),
                "K_c_upper": ("K_c", "upper"),
                "A_upper": ("A", "upper"), "A_lower": ("A", "lower"),
                "log10_A_upper": ("log10_A", "upper"),
                "R0_upper = A^(1/delta)": ("R0", "upper")}
        for field, (quantity, direction) in keys.items():
            bound = ball(Fraction(row[field]))
            true = values[quantity]
            gap = bound - true if direction == "upper" else true - bound
            status = "CONFIRMED" if gap > 0 else "REFUTED" if gap < 0 else "UNRESOLVED_EQUALITY"
            rows.append(dict(case=label, field=field, declared_decimal=row[field],
                             independently_computed=str(true), signed_safety_margin=str(gap),
                             verdict=status))
    out = dict(checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               source=str(src), source_sha256=sha256(blob).hexdigest(),
               source_code_sha256=sha256(code).hexdigest(), arithmetic="Arb 512 bits",
               checks=rows)
    (target / "verification/endpoint_checks.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({v: sum(r["verdict"] == v for r in rows)
                      for v in ["CONFIRMED", "REFUTED", "UNRESOLVED_EQUALITY"]}))
    for r in rows:
        if r["verdict"] == "REFUTED":
            print(r["case"], r["field"], r["declared_decimal"], r["signed_safety_margin"])


if __name__ == "__main__":
    main()
