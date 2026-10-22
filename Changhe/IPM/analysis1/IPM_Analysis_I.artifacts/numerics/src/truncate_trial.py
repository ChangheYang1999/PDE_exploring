"""Truncate a modal trial file to its first M angular modes (test fixture for test_cert_small.py, test_cert_deriv.py, lin_assembly.py).
All per-mode arrays (D, Ei, Eo, S, Aout) are sliced to [:M]; every other key (k, L, rmin, R0, knots, p, bi, bo, kappa, h, h_in, c_target) is
copied unchanged and M is set to the new value. The dependent coefficients are NOT recomputed, so the truncated trial is a test object only
(its normalization c = 3/k - 1 no longer holds exactly).  data/trial_small_M20.npz = this script on data/trial_v2_h0.008.npz with M = 20.
Usage: python3 truncate_trial.py trial.npz M out.npz
"""
import sys
import numpy as np

def main(path, M, out):
    d = dict(np.load(path))
    for key in ("D", "Ei", "Eo", "S", "Aout"):
        d[key] = np.ascontiguousarray(d[key][:M])
    d["M"] = np.array(M)
    order = ["k", "L", "rmin", "R0", "knots", "D", "Ei", "S", "Aout", "Eo", "bi", "bo", "h", "h_in", "M", "p", "c_target", "kappa"]   # the stored key order
    rest = [k for k in d if k not in order]
    np.savez_compressed(out, **{k: d[k] for k in order + rest if k in d})
    print("wrote %s: M = %d, S %s" % (out, M, d["S"].shape))

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
