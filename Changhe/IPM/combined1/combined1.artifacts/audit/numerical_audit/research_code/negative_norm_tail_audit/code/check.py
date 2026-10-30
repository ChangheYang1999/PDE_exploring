"""Independent exact factor audit; no foreign module is imported or executed."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import ast
import json
import time
from flint import arb, ctx

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def ar(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator


start = time.monotonic()
ctx.prec = 256
checks = []
for n, a, b in [(1, -4, -4), (1, -4, -3), (3, -4, -5)]:
    # R=1. This remains defined at b+n+2=0.
    triangle = Q(1, (n-a-2)*(-a-b-4))
    direct = None
    if b+n+2:
        direct = (Q(1, -a-b-4)-Q(1, n-a-2))/Q(b+n+2)
        assert triangle == direct
    checks.append({
        "n": n, "a": a, "b": b, "triangle": str(triangle),
        "old_expression": str(direct) if direct is not None else "division by zero",
    })
synthetic = Q(1, 12)
potential_integral = Q(1, 2)*Q(1, 3)-Q(1, 3)*Q(1, 4)
assert potential_integral == synthetic
log = BASE/"source/N1_d2_v4.out"
line = next(line for line in log.read_text().splitlines() if line.startswith("{'inner':"))
old = ast.literal_eval(line)
# Exact decimals from the displayed log, followed by outward square root.
corrected_sq = sum((Q(str(old[k])) for k in ["inner", "cross", "outer", "outer"]), Q(0))
corrected = ar(corrected_sq).sqrt()
target = ROOT/"research/whole_plane_norms/verification/d2_Hminus1_ball_2048.json"
exact = arb(json.loads(target.read_text())["norm_ball"])
out = {
    "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "claim": "The frozen N1 outer-outer formula omits a factor two.",
    "source_sha256": digest(BASE/"source/N1_ipm_hminus1.py"),
    "log_sha256": digest(log),
    "proof_sha256": digest(BASE/"PROOF.md"),
    "code_sha256": digest(Path(__file__)),
    "exact_synthetic_norm_squared_div_pi": str(synthetic),
    "independent_potential_integral_div_pi": str(potential_integral),
    "triangle_tests": checks,
    "logged_contributions": old,
    "corrected_logged_squared_sum_exact": str(corrected_sq),
    "corrected_logged_H": corrected.str(55),
    "exact_full_plane_H": exact.str(55),
    "corrected_log_minus_exact_H": (corrected-exact).str(40),
    "exact_full_plane_record_sha256": digest(target),
    "scope": "The factor error is algebraic. Remaining quadrature and finite asymptotic errors are not certified.",
    "elapsed_seconds": time.monotonic()-start,
}
(BASE/"verification/factor_audit.json").write_text(json.dumps(out, indent=2)+"\n")
print("Synthetic norm squared/pi:", synthetic)
print("Corrected log H:", corrected.str(25))
print("Difference from exact H:", (corrected-exact).str(15))
