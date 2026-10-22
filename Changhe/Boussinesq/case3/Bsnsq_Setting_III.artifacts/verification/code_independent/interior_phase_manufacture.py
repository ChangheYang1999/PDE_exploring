"""Independent exact check of a degenerate-phase obstruction, not B2 data."""
from pathlib import Path
from datetime import datetime, timezone
import json, time
import sympy as s
start = time.monotonic()
x, y = s.symbols("x y", real=True, nonzero=True)
t = s.symbols("t", nonnegative=True)
W = s.Matrix([(4-3*y*y)*x, y**3])
a = x*y**3*s.exp(2/y**2)
om = s.diff(W[0], y)-s.diff(W[1], x)
results = {
 "divergence":s.simplify(s.diff(W[0],x)+s.diff(W[1],y)),
 "transport_invariant":s.simplify(W.dot(s.Matrix([s.diff(a,x),s.diff(a,y)]))),
 "negative_curl":s.simplify(om),
 "vorticity_defect_Theta_zero":s.factor(W.dot(s.Matrix([s.diff(om,x),s.diff(om,y)]))+om),
 "slow_derivative":s.simplify(s.diff((y**-2+2*t)**(-s.Rational(1,2)),t)+(y**-2+2*t)**(-s.Rational(3,2)))
}
assert results["divergence"] == 4
assert results["transport_invariant"] == 0
assert results["slow_derivative"] == 0
record = {"checked_utc":datetime.now(timezone.utc).isoformat(),"runtime_seconds":time.monotonic()-start,
 "status":"PASS; kinematic manufacture only, not B2", "symbolic_results":{k:str(v) for k,v in results.items()},
 "weighted_gradient_log_asymptotic":"3*t -(3/2)*log(y0^(-2)+2*t)+2/y0^2 -> +infinity"}
Path("research/58_beta2_interior_fibre_sign/verification/reproducible_manufacture.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))
