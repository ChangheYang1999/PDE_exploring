"""Recompute the exactified coefficients (Ei, Eo, A00) of a trial in Arb and export them with the enclosing format."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb
from cert_green import Cert
trial, out, prec = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 256
C = Cert(trial, prec, 0.0); info = C.exactify()
from cert_green import ball_dyadic as ball
coeffs = dict(prec=prec, A00=ball(info["A00_new"]), Ei=[[ball(x) for x in row] for row in C.Ei], Eo=[[ball(x) for x in row] for row in C.Eo],
              c=ball(info["c_after"]), target=ball(info["target"]), format="exact dyadic: mid = man*2^exp, rad = rman*2^rexp",
              note="Ei, Eo, A00 are defined by the C^6 join equations and c = 3/k - 1; the other coefficients are the stored floats of the trial file")
json.dump(coeffs, open(out, "w"))
print("exported", out, "A00 =", info["A00_new"].str(30), "c after:", info["c_after"].str(30))
