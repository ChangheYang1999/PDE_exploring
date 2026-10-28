"""Directed recheck of the whole-plane lower bound of the decoupled-family margin m_fam(a_ang, Delta) = m_a + (a_ang - 17/4) tang - Delta q 1_{t>=0}
from the certified per-box data of runs/MARGIN_REF2/margin.npz (MA_ref lower bounds, TANG upper ends, Q upper ends) with the refined MF_ref of the
margin.py MARGIN_FAMILY runs listed in the family json substituted where finite. Differences from family_combine.py (astra referee 16:05Z):
every float operation is rounded toward the valid side with nextafter (c = a_ang - 17/4 <= 0 required, Delta >= 0 required, Delta rounded up),
no 1e-12 slack, every box of the plane must carry a finite bound (abort otherwise), refinement arrays must have the base geometry, the printed
bound is truncated toward -infinity.   Usage: python3 family_recheck.py a_ang Delta family_json"""
import sys, json, os, math
import numpy as np
def fail(m): raise SystemExit("INVALID: " + m)
def lo(x): return np.nextafter(x, -np.inf)
def up(x): return np.nextafter(x, np.inf)
a_ang, Delta = float(sys.argv[1]), float(sys.argv[2]); fam = json.load(open(sys.argv[3]))
if not (Delta >= 0 and a_ang <= 17.0 / 4): fail("need Delta >= 0 and a_ang <= 17/4")
base = np.load("runs/MARGIN_REF2/margin.npz", allow_pickle=True)
MA = base["MA_ref"]; TANG_hi = base["TANG"][:, :, 1]; Q_hi = base["Q"][:, :, 1]; bt = base["cell_ta"].astype(float); kind = base["cell_kind"]
bh = np.array([float(x) if x is not None and np.isfinite(float(x)) else np.inf for x in base["cell_h"]])
for name, arr in (("MA_ref", MA), ("TANG_hi", TANG_hi), ("Q_hi", Q_hi)):
    if not np.isfinite(arr).all(): fail("non-finite %s boxes: %s" % (name, np.argwhere(~np.isfinite(arr))[:5].tolist()))
c = a_ang - 17.0 / 4; Delta_up = up(Delta) if Delta != 0 else 0.0
whole = np.array([k == "pinf" or (k != "minf" and t >= 0) for k, t in zip(kind, bt)]); part = np.array([(not w) and k != "minf" and (t + h) >= 0 for w, k, t, h in zip(whole, kind, bt, bh)])
fam_q = np.where(whole[:, None], Q_hi, np.where(part[:, None], np.maximum(Q_hi, 0.0), 0.0))
# upper bound of Delta * q from the upper end q_hi of q (q may be negative): Delta_up * q_hi if q_hi >= 0, Delta_lo * q_hi if q_hi < 0, rounded up
Delta_lo = Delta   # the decimal Delta as parsed is the nearest double; for 0.3 it is below 3/10 (checked below), so it is a valid lower bound of Delta
from fractions import Fraction
if Fraction(Delta) > Fraction(sys.argv[2]): Delta_lo = lo(Delta)
if Fraction(Delta_up) < Fraction(sys.argv[2]): fail("Delta_up below the decimal Delta")
dq = up(np.where(fam_q >= 0, Delta_up * fam_q, Delta_lo * fam_q))
MF = lo(lo(MA + lo(c * TANG_hi)) - dq); before = MF.copy()
for rd in fam.get("refdirs", []):
    z = np.load(os.path.join(rd, "margin.npz"), allow_pickle=True)
    if z["MF_ref"].shape != MF.shape or not np.array_equal(z["cell_ta"].astype(float), bt): fail("%s: refinement arrays not on the base geometry" % rd)
    R = z["MF_ref"]; ok = np.isfinite(R); MF[ok] = np.maximum(MF[ok], R[ok])
i = np.unravel_index(np.argmin(MF), MF.shape); j = np.unravel_index(np.argmin(before), before.shape)
print("m_fam(%g, %g): directed whole-plane lower bound >= %.6f (float %r; before refinement %r at cell %d box %d), attained at cell %d (t_a %.4f, kind %s) box %d; refdirs %d; negative boxes %d"
      % (a_ang, Delta, math.floor(MF[i] * 1e6) / 1e6, float(MF[i]), float(before[j]), j[0], j[1], i[0], bt[i[0]], kind[i[0]], i[1], len(fam.get("refdirs", [])), int((MF < 0).sum())))
