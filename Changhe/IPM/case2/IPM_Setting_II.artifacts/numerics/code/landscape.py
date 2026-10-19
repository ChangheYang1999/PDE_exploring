"""Residual landscape: for each fixed c_l in a list, minimise the weighted least-squares residual of the zeta
formulation over zeta (LM with c_l frozen, fixed jet), from the consistent family start.  Reports the final
normalised residual, the identity defect c_l - 1/2 - psi_xy(0), psi_yy(0), and asymmetry fractions."""
import sys, os, time, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import torch, numpy as np
from ipm2polar import Disc
from zetasolve import lm_solve, initial_zeta, weight_zeta
torch.set_default_dtype(torch.float64)
dev = 'cuda'
Nr, Nth, R = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
cls = [float(s) for s in sys.argv[4].split(',')]
maxit = int(sys.argv[5]) if len(sys.argv) > 5 else 25
eps = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
tag = "landscape_%d_%d_%g%s" % (Nr, Nth, R, "_eps%g" % eps if eps else "")
d = Disc(Nr, Nth, R, K=2, tail='power2', device=dev)
print("# %s unknowns %d %s" % (tag, d.nunk(), time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())), flush=True)
rows = []
for cl in cls:
    # consistent start: family A with c = cl - 1/2 ; strain of family A at exponent p: c = ay * s(p); calibrate ay numerically
    p = 1.0 / cl
    v = initial_zeta(d, cl, eps=0.0, ay=1.0)
    qz, _ = d.unpack(v)
    out = d.zeta_residual_modes(qz, torch.tensor(cl, device=dev), return_all=True)
    c_unit = float(d.taylor_psi(out['p'])[2])
    ay = (cl - 0.5) / c_unit
    v0 = initial_zeta(d, cl, eps=eps, ay=ay)
    t0 = time.time()
    v, r, hist = lm_solve(d, v0, p, maxit=maxit, lam0=1e-2, logf=None, jet_mode='fixed', fix_cl=True)
    h = hist[-1]
    row = dict(cl=cl, ay=ay, res_norm=h['res_norm'], Rz_max_norm=h['Rz_max_norm'], Rz_L2_rel=h['Rz_L2_rel'],
               R_wsup=h['R_wsup'], R_wsup_central=h.get('R_wsup_central'), identity=h['cl_identity'], psi_xy0=h['psi_xy0'],
               psi_yy0=h['psi_yy0'], asym_x=h['asym_x'], asym_y=h['asym_y'], slope_m0=h['slope_rho_m0'], its=len(hist),
               time=time.time() - t0, res_hist=[hh['res_norm'] for hh in hist])
    rows.append(row)
    print("cl=%.3f ay=%.3f | final |res|=%.3e Rz_n=%.2e Rz_L2=%.2e R_wsup=%.2e (central %.2e) | identity=%.3e psi_xy0=%.4f psi_yy0=%.1e | asym_x=%.1e asym_y=%.2e slope=%.3f | its=%d %.0fs" %
          (cl, ay, row['res_norm'], row['Rz_max_norm'], row['Rz_L2_rel'], row['R_wsup'], row['R_wsup_central'] or 0, row['identity'], row['psi_xy0'], row['psi_yy0'], row['asym_x'], row['asym_y'], row['slope_m0'], row['its'], row['time']), flush=True)
    json.dump(rows, open("runs/%s.json" % tag, "w"), indent=1, default=float)
