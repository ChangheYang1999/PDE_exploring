"""Float (NOT certified) evaluation of the lead's Note 14 axis-direction D witness with the polygon zero set Z0(b):
   F = min(g0 + c, -1/2 + lam P(z - e1)),  f = clamp(F, +-h) on H = {z1 > 1/2}, f(Mz) = -f(z),
   g0 = axis polygon C witness (structured_lb.f0_val with Z0(b)), h = (1/2)(2(z1 - 1/2))^alpha,
   P(w) = (1/2)|w|^alpha (1 + sgn(cos 2 theta)|cos 2 theta|^alpha), theta = arg w  (rotated projection cusp; zero on the vertical through e1).
Value: |int k0 f| + 1/2 (lattice lemma, Note 12 / V072). Same quadrature as structured_lb.integrate_axis plus a far-tail estimate
c rho_max^(alpha-1)/(1-alpha) from the last far ring (c = ring value / rho^(alpha-2)); the pre-06:11Z axis values omitted this tail
(negligible for alpha <= 3/4 at rho_max 1e9, about 0.1 at alpha 9/10).
Usage: python3 note14_float.py alpha b c lam [rho_max] ;  lam=None -> plain lattice witness clamp(g0 - 1/2) (t = 1/2) for comparison."""
import sys, numpy as np
sys.path.insert(0, '.')
from structured_lb import K0, k0_tot, make_Z0, f0_val, f0_lattice

def P_cusp(wx, wy, alpha):
    r2 = wx*wx + wy*wy; r = np.sqrt(r2)
    c2 = np.where(r2 > 0, (wx*wx - wy*wy)/np.where(r2 > 0, r2, 1), 0.0)
    return 0.5*r**alpha*(1 + np.sign(c2)*np.abs(c2)**alpha)

def f_note14(px, py, alpha, b, Z, c, lam):
    right = px > 0.5
    qx = np.where(right, px, 1 - px)
    g = f0_val(qx, py, alpha, b, Z)
    h = 0.5*(2*np.maximum(qx - 0.5, 0))**alpha
    F = np.minimum(g + c, -0.5 + lam*P_cusp(qx - 1.0, py, alpha))
    f = np.maximum(-h, np.minimum(h, F))
    return np.where(right, f, -f)

def integrate_fun(alpha, fval, fp1=-0.5, fp0=0.5, nr=50, nth=720, rho_min=1e-7, rho_max=1e9, nrf=30, nthf=720, h=0.004, Rn=0.5, Rf=1.0):
    tot = 0.0; parts = {}
    for (cx, cy, name, fpole) in [(1.0, 0.0, 'near1', fp1), (0.0, 0.0, 'near0', fp0)]:
        lr = np.linspace(np.log(rho_min), np.log(Rn), int(nr*np.log(Rn/rho_min)) + 1)
        lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
        th = np.linspace(0, 2*np.pi, nth + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
        RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
        px = cx + RR*np.cos(TT); py = cy + RR*np.sin(TT)
        own = K0(px - cx, py - cy) if cx == 1.0 else -K0(px, py)
        other = -K0(px, py) if cx == 1.0 else K0(px - 1.0, py)
        fv = fval(px, py)
        val = np.sum((own*(fv - fpole) + other*fv)*RR*RR)*dlr*dth
        parts[name] = val; tot += val
    lr = np.linspace(np.log(Rf), np.log(rho_max), int(nrf*np.log(rho_max/Rf)) + 1)
    lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
    th = np.linspace(0, 2*np.pi, nthf + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
    far = 0.0; last = None
    for idx in np.array_split(np.arange(len(lrc)), 16):
        RR, TT = np.meshgrid(np.exp(lrc[idx]), thc, indexing='ij')
        px = 0.5 + RR*np.cos(TT); py = RR*np.sin(TT)
        v = k0_tot(px, py)*fval(px, py)*RR*RR*dlr*dth
        far += v.sum(); last = (np.exp(lrc[idx][-1]), v[-1].sum()/dlr)   # ring value per unit log-radius
    parts['far'] = far; tot += far
    rl, vl = last; cc = vl/rl**(alpha - 1)          # ring value per d(log rho) = c rho^(alpha-1)  (per d rho: c rho^(alpha-2))
    tail = cc*rho_max**(alpha - 1)/(1 - alpha); parts['far_tail_est'] = tail; tot += tail
    xs = np.arange(0.5 - Rf, 0.5 + Rf, h) + h/2; ys = np.arange(-Rf, Rf, h) + h/2
    PX, PY = np.meshgrid(xs, ys, indexing='ij')
    inside = ((PX - 0.5)**2 + PY**2 < Rf*Rf) & ((PX - 1)**2 + PY**2 >= Rn*Rn) & (PX**2 + PY**2 >= Rn*Rn)
    val = np.sum(np.where(inside, k0_tot(PX, PY)*fval(PX, PY), 0.0))*h*h; parts['leftover'] = val; tot += val
    parts['transport'] = tot
    return abs(tot) + 0.5, parts

if __name__ == '__main__':
    alpha = float(sys.argv[1]); b = float(sys.argv[2]); c = float(sys.argv[3]); lam = sys.argv[4]
    rho_max = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9
    Z = make_Z0(b)
    if lam == 'None':
        fv = lambda px, py: f0_lattice(px, py, alpha, b, Z, 0.5, 1.0); tag = 'clamp(g0-1/2)'
    else:
        lam = float(lam); fv = lambda px, py: f_note14(px, py, alpha, b, Z, c, lam); tag = f'min(g0+{c}, -1/2+{lam:.6f}P)'
    v, parts = integrate_fun(alpha, fv, rho_max=rho_max)
    print(f"alpha={alpha} b={b} {tag} rho_max={rho_max:.0e}: D witness value = {v:.5f}  " + " ".join(f"{k}={x:+.4f}" for k, x in parts.items()), flush=True)
