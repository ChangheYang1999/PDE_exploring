"""Summary of the rigorous derivative certificate (runs/cert_deriv_middle.json from src/cert_resid_deriv.py): per dyadic shell the maxima
of W_i_j / m (W_i_j = sum_N (2N+1)^j sup_cell |d_t^i eps_N|, i + j <= 2), W_K / m (K~ = rho~ - X.grad rho~ modes), W_eps_minus_dteps / m,
and on the P-disc cells (nder = 5) the maxima of W_i_j for i + j <= 5. Float post-processing of certified per-cell numbers (max is exact;
the division by m uses the certified lower bound m_inf of each cell if present, else the left-end value).
Usage: python3 cert_deriv_summary.py runs/cert_deriv_middle.json
"""
import sys, json
import numpy as np


def _jopen(path):
    """Open a JSON result file for reading; falls back to path + '.gz' (the artifacts folder stores JSON files above 1 MB gzipped)."""
    import os, gzip
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"):
        return gzip.open(str(path) + ".gz", "rt")
    return open(path)
d = json.load(_jopen(sys.argv[1]))
rows = d["rows"] if isinstance(d, dict) and "rows" in d else d
print("cells:", len(rows)); print("keys of a row:", sorted(rows[0].keys()))
r_a = np.array([row.get("r_a", np.exp(row["t_a"])) for row in rows])
m_inf = np.array([row.get("m_inf", np.nan) for row in rows])
def col(key):
    return np.array([row.get(key, np.nan) for row in rows], float)
shells = [(0.00765, 0.0156), (0.0156, 0.0625), (0.0625, 0.25), (0.25, 1), (1, 4), (4, 16), (16, 64), (64, 256), (256, 1024), (1024, 3413.1)]
keys = [k for k in rows[0].keys() if k.startswith("W_") and k != "W_over_m"]
print("\nmax over shell of W_key / m_inf (rigorous per-cell upper bounds divided by the certified cell minimum of m):")
hdr = ["shell"] + keys
print(" | ".join(hdr))
for lo, hi in shells:
    sel = (r_a >= lo) & (r_a < hi)
    if not sel.any(): continue
    vals = []
    for k in keys:
        v = col(k)[sel] / m_inf[sel]
        vals.append("%.3e" % np.nanmax(v) if np.isfinite(v).any() else "-")
    print(" | ".join(["[%g, %g)" % (lo, hi)] + vals))
# P-disc cells
pd = [row for row in rows if row.get("nder", 2) >= 5]
if pd:
    print("\nP-disc cells (nder = 5): %d cells, r in [%.4f, %.4f]; max over cells of W_i_j (absolute, not divided by m):" % (len(pd), min(np.exp(row["t_a"]) for row in pd), max(np.exp(row["t_a"]) for row in pd)))
    for k in sorted(pd[0].keys()):
        if k.startswith("W_"):
            print("  %-22s max %.3e   (at r = %.4f)" % (k, max(row[k] for row in pd), np.exp(max(pd, key=lambda row: row[k])["t_a"])))
