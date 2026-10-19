"""Reproduce the small damped linear-solve check from its exact saved inputs."""
import json
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator, lsmr

path = Path("centre/verification/recycled_linear_solve.json")
data = json.loads(path.read_text())
A = np.array(data["matrix"])
b = np.array(data["rhs"])
lam = data["damping"]
augmented = np.vstack([A, np.sqrt(lam) * np.eye(A.shape[1])])
rhs = np.r_[b, np.zeros(A.shape[1])]
op = LinearOperator(augmented.shape, matvec=lambda x: augmented @ x,
                    rmatvec=lambda y: augmented.T @ y)
actual = lsmr(op, rhs, damp=0., x0=np.array(data["initial_guess"]),
              atol=1e-14, btol=1e-14)[0]
expected = np.linalg.solve(A.T @ A + lam * np.eye(A.shape[1]), A.T @ b)
error = float(np.max(abs(actual - expected)))
assert error < 1e-12
data["maximum_error_vs_normal_equations"] = error
data["command"] = "timeout 540 bash bounded.sh python3 verify_recycle.py"
path.write_text(json.dumps(data, indent=2))
print(json.dumps(data, indent=2))
