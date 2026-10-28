"""Lead's request N8: J(b) = int_{H minus B_{1/2}(x)} |nu_b| dw + int_{B_{1/2}(x)} (|nu_b| - |K_b(x - w)|) dw,
x = e1/2, y = -e1/2, H = {w1 > 0}, K_b(z) = cos(2 arg z - 2b)/(2 pi |z|^2), nu_b(w) = K_b(x-w) - K_b(y-w).
Float, midpoint rule in polar coordinates about x (log-spaced radii), fine angular grid; two resolutions for error estimate."""
import numpy as np, sys
def Kb(zx, zy, b):
    r2 = zx*zx + zy*zy
    return np.cos(2*np.arctan2(zy, zx) - 2*b)/(2*np.pi*r2)
def J(b, nr=400, nth=4000, rho_min=1e-7, rho_max=1e6):
    # ball part: rho in [rho_min, 1/2] about x: integrand |nu| - |K_b(x-w)| ; bounded by |K_b(y-w)| <= 1/(2pi (1/2)^2) near x
    def polar(r_lo, r_hi, nr_, func, clip=False):
        lr = np.linspace(np.log(r_lo), np.log(r_hi), nr_ + 1); lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
        th = np.linspace(-np.pi, np.pi, nth + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
        RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
        wx = 0.5 + RR*np.cos(TT); wy = RR*np.sin(TT)
        vals = func(wx, wy)
        if clip:
            vals = np.where(wx > 0, vals, 0.0)
        return np.sum(vals*RR*RR)*dlr*dth
    nu = lambda wx, wy: Kb(0.5 - wx, -wy, b) - Kb(-0.5 - wx, -wy, b)
    ball = polar(rho_min, 0.5, int(nr*np.log(0.5/rho_min)/np.log(1e6)) + 1, lambda wx, wy: np.abs(nu(wx, wy)) - np.abs(Kb(0.5 - wx, -wy, b)))
    # inner ball rho<rho_min: ||nu| - |K(x-w)|| <= |K(y-w)| <= 1/(2 pi (1-rho_min)^2): area pi rho_min^2 -> negligible
    outer = polar(0.5, rho_max, int(nr*np.log(rho_max/0.5)/np.log(1e6)) + 1, lambda wx, wy: np.abs(nu(wx, wy)), clip=True)
    # tail beyond rho_max: |nu| <= 1/(pi (rho-1/2)^3) * 1 (mean value), half plane: ~ int_{rho_max}^inf pi rho /(pi rho^3) = 1/rho_max
    return ball + outer, ball, outer, 1.0/rho_max
if __name__ == "__main__":
    for b in np.linspace(0, np.pi/4, 9):
        v, ball, outer, tail = J(b)
        v2, _, _, _ = J(b, nr=200, nth=2000)
        print(f"b={b:.5f} ({b/np.pi*180:5.2f} deg): J = {v:.6f}  (ball {ball:+.6f}, outer {outer:.6f}, tail<{tail:.0e}; coarser grid {v2:.6f})", flush=True)
