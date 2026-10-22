"""Floating-point (non-rigorous) evaluation of the X3 residual on a log-polar grid with my own inverse (src/inverse.py).
Usage: python3 x3_resid.py Nr Nt rmin_L rmax_L out.json [tail_decades=1.0] [tailmode=four|lead|two]
(tail_decades: length in decades of the fit window of the power-law far continuation at the outer grid end; tailmode: powers used: four =
r^{k-1}, r^{2k-2}, r^{k-3}, r^{3k-3} (default, as in the saved tables), lead = the exact leading power r^{k-1} only, two = the first two)
rho and grad rho from the exact formula (x3.py), U from the modal inverse with a power-law tail fit,
c = psi_xy(0), c_l_id = (1+c)/3, residual eps = (c_l X + U).grad rho - rho with c_l = stored value (and with c_l_id),
N_f = |V1 rho_x| + |V2 rho_y| + |rho|, N_v = |rho| + |X.grad rho| + |U.grad rho|. Regional maxima as in the published table.
"""
import sys, json, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import CubicSpline
from x3 import X3
from inverse import ModalInverse


def main(Nr, Nt, rmin_L, rmax_L, out, p=6, tail_decades=1.0, tailmode="four"):
    X = X3(); L = X.L; k = X.k
    r = np.exp(np.linspace(np.log(rmin_L * L), np.log(rmax_L * L), Nr))
    th = np.linspace(0, np.pi / 2, Nt + 1)
    t0 = time.time()
    F = X.rho(r, th)
    rho, rho_x, rho_y = F["rho"], F["rho_x"], F["rho_y"]
    rho_x[:, -1] = 0.0          # exact: rho even in x => rho_x(0,y) = 0
    t1 = time.time()
    tail_powers = {"four": [k - 1, 2 * k - 2, k - 3, 3 * k - 3], "lead": [k - 1], "two": [k - 1, 2 * k - 2]}[tailmode]   # far continuation of the modes beyond rmax
    inv = ModalInverse(r, th, p=p, tail_powers=tail_powers, k=k, tail_decades=tail_decades)
    psi, dpsi, c = inv.solve(rho_x)
    V = inv.velocity()
    t2 = time.time()
    Ux, Uy = V["Ux"], V["Uy"]
    cl_store = X.stored["c_l"]; cl_id = (1 + c) / 3
    Xc = r[:, None] * np.cos(th)[None, :]; Yc = r[:, None] * np.sin(th)[None, :]
    R = r[:, None] * np.ones_like(th)[None, :]
    cut = (np.pi / 2 - th) >= 0.006
    res = {}
    for label, cl in (("stored", cl_store), ("identity", cl_id)):
        V1 = cl * Xc + Ux; V2 = cl * Yc + Uy
        eps = V1 * rho_x + V2 * rho_y - rho; eps[:, -1] = 0.0; eps[:, 0] = 0.0   # exact zeros on both axes by parity
        Nf = np.abs(V1 * rho_x) + np.abs(V2 * rho_y) + np.abs(rho)
        Nv = np.abs(rho) + np.abs(Xc * rho_x + Yc * rho_y) + np.abs(Ux * rho_x + Uy * rho_y)
        with np.errstate(divide='ignore', invalid='ignore'):
            qf = np.where(Nf > 0, np.abs(eps) / Nf, 0.0); qv = np.where(Nv > 0, np.abs(eps) / Nv, 0.0)
        w = V1[:, 0]; i = np.flatnonzero((w[:-1] * w[1:] < 0) & (r[:-1] > 1))[0]
        sl = slice(max(i - 3, 0), i + 5)
        cs = CubicSpline(np.log(r[sl]), w[sl]); roots = cs.roots()
        roots = roots[(roots > np.log(r[i])) & (roots < np.log(r[i + 1]))]
        xstar = float(np.exp(roots[0])) if len(roots) else float('nan')
        n = inv.n
        h_axis = cl + ((2 * n[None, :]) * (dpsi / r[:, None] - psi / r[:, None] ** 2)).sum(1)
        hP = float(CubicSpline(np.log(r[sl]), h_axis[sl])(np.log(xstar)))
        wprime = float(CubicSpline(np.log(r[sl]), w[sl])(np.log(xstar), 1) / xstar)
        regions = {"r<=0.1": R <= 0.1, "0.1<=r<=2": (R >= 0.1) & (R <= 2), "2<=r<=10": (R >= 2) & (R <= 10),
                   "|X-P|<0.5": np.hypot(Xc - xstar, Yc) < 0.5, "10<=r<=100": (R >= 10) & (R <= 100),
                   "100<=r<=1000": (R >= 100) & (R <= 1000), "1000<=r<=1000L": (R >= 1000) & (R <= 1000 * L),
                   "r>1000L": R > 1000 * L, "r<=1000": R <= 1000, "all": R > 0}
        rows = []
        def mx(a, m):
            if not m.any(): return (0.0, 0.0, 0.0)
            j = np.argmax(np.where(m, a, -1.0)); i0, j0 = np.unravel_index(j, a.shape)
            return (float(a[i0, j0]), float(r[i0]), float(th[j0]))
        for name, mask in regions.items():
            m2 = mask & cut[None, :]
            rows.append(dict(region=name, Nf_max=mx(qf, mask), Nf_max_cut=mx(qf, m2), Nv_max=mx(qv, mask), Nv_max_cut=mx(qv, m2),
                             abs_max=mx(np.abs(eps), mask), rho_max=float(np.abs(rho[mask]).max()) if mask.any() else 0.0))
        res[label] = dict(c_l=cl, x_star=xstar, hP_minus_1=hP - 1, wprime_P=wprime, two_cl_minus_1=2 * cl - 1, rows=rows)
    outd = dict(Nr=Nr, Nt=Nt, rmin=float(r[0]), rmax=float(r[-1]), tail_decades=tail_decades, tailmode=tailmode, tail_powers=tail_powers, c=float(c), c_l_identity=cl_id, c_l_stored=cl_store,
                c_stored=X.stored["c"], t_fields=t1 - t0, t_inverse=t2 - t1, p=p, results=res)
    json.dump(outd, open(out, "w"), indent=1)
    print(json.dumps({k_: v for k_, v in outd.items() if k_ != "results"}, indent=1))
    for label in res:
        print("==", label, "c_l=%.12f x*=%.9f hP-1=%.3e w'(P)-(2c_l-1)=%.3e" % (res[label]["c_l"], res[label]["x_star"], res[label]["hP_minus_1"], res[label]["wprime_P"] - res[label]["two_cl_minus_1"]))
        for row in res[label]["rows"]:
            print("  %-16s Nf %.3e (cut %.3e)  Nv %.3e (cut %.3e)  abs %.3e @r=%.4g th=%.4f  rhomax %.4g" % (
                row["region"], row["Nf_max"][0], row["Nf_max_cut"][0], row["Nv_max"][0], row["Nv_max_cut"][0], row["abs_max"][0], row["abs_max"][1], row["abs_max"][2], row["rho_max"]))


if __name__ == "__main__":
    a = sys.argv; main(int(a[1]), int(a[2]), float(a[3]), float(a[4]), a[5], 6, float(a[6]) if len(a) > 6 else 1.0, a[7] if len(a) > 7 else "four")
