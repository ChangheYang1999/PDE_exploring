"""Summarize a cert_resid.py middle-region output file (any trial): sup W/m, the two multiplier forms and the shells. Float post-processing of
certified per-cell bounds (max is exact; weights were bounded per cell inside cert_resid).
Usage: python3 resid_summary_any.py runs/cert_resid_middle_X.json"""
import sys, json
import numpy as np


def _jopen(path):
    """Open a JSON result file for reading; falls back to path + '.gz' (the artifacts folder stores JSON files above 1 MB gzipped)."""
    import os, gzip
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"):
        return gzip.open(str(path) + ".gz", "rt")
    return open(path)
d = json.load(_jopen(sys.argv[1])); rows = d["rows"] if isinstance(d, dict) and "rows" in d else d
ra = np.exp(np.array([r["t_a"] for r in rows])); Wm = np.array([r["W_over_m"] for r in rows]); W = np.array([r["W"] for r in rows])
Wf = np.array([r.get("W_over_m_far", np.nan) for r in rows]); L2 = np.array([r.get("L2piece", 0.0) for r in rows])
print("%s: %d cells, done=%s" % (sys.argv[1], len(rows), d.get("done") if isinstance(d, dict) else "?"))
i = int(np.argmax(Wm)); print("sup W/m = %.4e at r = %.4g ; sup W = %.4e ; sup W(1+u)^0.5/m = %.4e ; sum L2 pieces = %.4e" % (Wm[i], ra[i], W.max(), np.nanmax(Wf), L2.sum()))
for lo, hi in [(0.00765, 0.0156), (0.0156, 0.0625), (0.0625, 0.25), (0.25, 1), (1, 4), (4, 16), (16, 64), (64, 256), (256, 1024), (1024, 3413.1)]:
    sel = (ra >= lo) & (ra < hi)
    if sel.any():
        j = np.argmax(np.where(sel, Wm, -1)); print("  shell [%g, %g): max W/m = %.4e at r = %.4g ; max W = %.3e" % (lo, hi, Wm[j], ra[j], W[sel].max()))
