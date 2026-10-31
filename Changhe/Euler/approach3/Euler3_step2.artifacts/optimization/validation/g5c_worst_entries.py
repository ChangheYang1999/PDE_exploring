"""Follow-up of g5c_closure_grid: the entries of the first_correction analysis table (924 closure points, pressure modes of degree <= 18, values
only) whose normalized error against the 70-digit reference exceeds 2.3e-16: point, mode, production and reference values, ulp distance."""
import sys, os, json
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT)
VER = "RUN_ROOT/verifier"
sys.path.insert(0, os.path.join(VER, "scripts")); sys.path.insert(0, os.path.join(VER, "independent", "src"))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from decimal import Decimal, getcontext
from validation.gates import Case, ROOT
from src.bases.solid_harmonics import eval_solid
from src.far_field.correction import mode_list
import mpmath as _mp
_mp.mp.dps = 80                      # the verifier script sets mp.mp.dps = 80 only inside its main(): without it, compiled() builds the normalization factor at 15 digits (the cause of the spurious 1.4-ulp "errors" of the first run, 00:32Z)
from verify_angular_tables import compiled, decimal_values
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
case = Case("S01", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); model = case.model
import sys as _s
which = _s.argv[1] if len(_s.argv) > 1 else "unit"
y = (case.prob.closure["grid"].n if which == "unit" else model.R0 * case.prob.closure["grid"].n).to(dev)
Lq = 2 * model.L + 6; pmodes = mode_list(Lq, model.m_parity, l_min=0)
A0, _, _ = eval_solid(y, pmodes, Lq, 0, path="dd")
print("points:", which, "|y| =", float(y.norm(dim=1).mean()))
A0n = A0.cpu().numpy(); pts = y.cpu().numpy()
getcontext().prec = 70
polys = [compiled(tuple(int(v) for v in m)) for m in pmodes]; powers = set(p for norm, rows in polys for row in rows for p, c in row)
worst = []
import math
for i in range(pts.shape[0]):
    vv = decimal_values(pts[i], polys, powers)
    scale = max(abs(float(A0n[i, q])) for q in range(len(pmodes)))
    for q in range(len(pmodes)):
        ref = vv[q][0]; prod = float(A0n[i, q]); err = float(abs(Decimal.from_float(prod) - ref))
        if err / scale > 2.3e-16:
            ulp = math.ulp(prod) if prod != 0 else float("nan")
            worst.append(dict(point=i, y=[float(v) for v in pts[i]], mode=pmodes[q], prod=prod, ref=float(ref), abs_err=err, norm_err=err / scale, err_in_ulps=(err / ulp if prod != 0 else None), scale=scale))
worst.sort(key=lambda w: -w["norm_err"])
print(len(worst), "entries above 2.3e-16 normalized")
for w in worst[:12]:
    print(json.dumps(w))
json.dump(worst, open(os.path.join(MYROOT, "validation", "g5c_worst_entries.json"), "w"), indent=1)
