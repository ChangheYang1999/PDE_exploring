"""SPEC v1 item C1 (floating point): map of the weighted-L^2 dissipativity function of F4,
   D_w(X) = 1 + c_l + (1/2) V.grad log w - (|grad rho| - rho_y)/2,
for w in {1, m^-2, m^-2 (1+u)^(-2 delta)} with m = u^3 (1+u^2)^((k-3)/2), u = r/L, delta = 0.5, on the X3 fields
(own generator and inverse; floating point estimate). Reports min D_w, the fraction of the sampled quadrant area (dX = r dr dtheta)
with D_w < 0 by radial band, and the locations. Usage: python3 dw_map.py Nr Nt out.json"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from x3 import X3
from inverse import ModalInverse


def main(Nr, Nt, out):
    X = X3(); L = X.L; k = X.k; c_l = X.c_l
    r = np.exp(np.linspace(np.log(1e-4 * L), np.log(1e6 * L), Nr)); th = np.linspace(0, np.pi / 2, Nt + 1)
    F = X.rho(r, th); rho_x, rho_y = F["rho_x"], F["rho_y"]; rho_x[:, -1] = 0
    inv = ModalInverse(r, th, p=6, tail_powers=[k - 1, 2 * k - 2, k - 3, 3 * k - 3], k=k); inv.solve(rho_x); V = inv.velocity()
    Vr = c_l * r[:, None] + V["Ur"]
    u = r / L
    grad = np.sqrt(rho_x ** 2 + rho_y ** 2); coup = (grad - rho_y) / 2
    dlogm = (3 / u + (k - 3) * u / (1 + u ** 2)) / L                   # d/dr log m
    weights = {"w=1": np.zeros_like(r), "w=m^-2": -2 * dlogm, "w=m^-2(1+u)^-1": -2 * dlogm - 1.0 / (L * (1 + u))}
    res = {}
    area = (r[:, None] ** 2 * np.gradient(np.log(r))[:, None]) * (th[1] - th[0]) * np.ones_like(th)[None, :]   # r dr dtheta = r^2 dt dtheta
    for name, dlw in weights.items():
        D = 1 + c_l + 0.5 * Vr * dlw[:, None] - coup
        rows = []
        for lo, hi in [(0, 0.1), (0.1, 2), (2, 10), (10, 100), (100, 1000), (1000, 1e4), (1e4, 1e7)]:
            m = (r >= lo) & (r < hi)
            Dm = D[m]; am = area[m]
            neg = Dm < 0
            i = np.unravel_index(np.argmin(Dm), Dm.shape)
            rows.append(dict(band=[lo, hi], min_D=float(Dm.min()), r_at_min=float(r[m][i[0]]), theta_at_min=float(th[i[1]]),
                             neg_area_fraction=float(am[neg].sum() / am.sum()), max_coupling=float(coup[m].max())))
        res[name] = rows
        print("== %s" % name)
        for row in rows:
            print("  r in [%g,%g): min D = %+.4f at r=%.4g th=%.3f ; negative-area fraction %.3f ; max (|grad rho|-rho_y)/2 = %.3f" % (
                row["band"][0], row["band"][1], row["min_D"], row["r_at_min"], row["theta_at_min"], row["neg_area_fraction"], row["max_coupling"]))
    json.dump(dict(Nr=Nr, Nt=Nt, c_l=c_l, results=res), open(out, "w"), indent=1)


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
