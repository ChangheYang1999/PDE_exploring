"""Float (NOT certified) evaluation of the verification work's rotated axis D witness family
(11_lattice_pole_constraints/rotated_axis_family/PROOF.md, 10:59Z request).
Coordinates of this lane: poles e1 = (1,0) (value -1/2) and 0 (value +1/2), midpoint m = (1/2, 0); w = z - m are the verification work's
coordinates (poles x = (1/2,0), y = -x). Kernel K_phi(u) = [cos phi (u1^2 - u2^2) + 2 sin phi u1 u2]/(2 pi |u|^4) = cos(2 theta - phi)/(2 pi r^2),
nu_phi(w) = K_phi(w - x) - K_phi(w - y) = K_phi(z - e1) - K_phi(z).  Witness on H = {w1 > 0}:
   F(w) = min(g_b(Q_delta w) + c, -1/2 + lam P_phi(w - x)),  f = clamp(F, -h, h),  h = 2^(a-1) w1^a,
   P_phi(u) = P_0(Q_{-phi/2} u),  P_0(u) = (1/2)|u|^a (1 + sgn(cos 2 theta)|cos 2 theta|^a),
   g_b = this lane's axis polygon witness f0_val (structured_lb; polygon Z0(b) in z-coordinates, i.e. g_b(v) = f0_val(v + m)),
   central oddness f(-w) = -f(w)  (NOT the midline reflection used for phi = delta = 0).
Value: |I_phi| + 1/2, I_phi = pv int nu_phi f (own-pole kernel against f - f(pole) in the pole disks).
Quadrature: as note14_float.integrate_fun (log-polar near disks of radius 1/2, Cartesian leftover, log-polar far field about m
to rho_max with a last-ring tail estimate). For phi = delta = 0 this reproduces note14_float (2.4562 at alpha 1/2, b 3/4, c -.15, lam 1000/1021).
Usage: python3 rotated_float.py alpha b c lam phi_list delta_rule [rho_max]
   phi_list: comma separated;  delta_rule: 'm3' (delta = -phi/3), 'p3' (delta = +phi/3), '0' (delta = 0) or a number (fixed delta)."""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from structured_lb import make_Z0, f0_val

def K_phi(x, y, phi):
    r2 = x*x + y*y
    return (np.cos(phi)*(x*x - y*y) + 2*np.sin(phi)*x*y)/(2*np.pi*r2*r2)

def P_cusp(wx, wy, alpha):
    r2 = wx*wx + wy*wy; r = np.sqrt(r2)
    c2 = np.where(r2 > 0, (wx*wx - wy*wy)/np.where(r2 > 0, r2, 1), 0.0)
    return 0.5*r**alpha*(1 + np.sign(c2)*np.abs(c2)**alpha)

def f_rot(px, py, alpha, b, Z, c, lam, phi, delta):
    wx = px - 0.5; wy = py
    right = wx > 0
    qx = np.where(right, wx, -wx); qy = np.where(right, wy, -wy)          # central reflection into H
    cd, sd = np.cos(delta), np.sin(delta)
    rx = cd*qx - sd*qy; ry = sd*qx + cd*qy                                 # Q_delta q
    g = f0_val(rx + 0.5, ry, alpha, b, Z)                                  # g_b(Q_delta q) in z-coordinates
    ux = qx - 0.5; uy = qy                                                 # u = q - x
    ch, sh = np.cos(phi/2), np.sin(phi/2)
    vx = ch*ux + sh*uy; vy = -sh*ux + ch*uy                                # Q_{-phi/2} u
    P = P_cusp(vx, vy, alpha)
    h = 2**(alpha - 1)*qx**alpha
    F = np.minimum(g + c, -0.5 + lam*P)
    f = np.maximum(-h, np.minimum(h, F))
    return np.where(right, f, -f)

def integrate_fun(alpha, fval, phi, fp1=-0.5, fp0=0.5, nr=50, nth=720, rho_min=1e-7, rho_max=1e9, nrf=30, nthf=720, h=0.004, Rn=0.5, Rf=1.0):
    Kf = lambda x, y: K_phi(x, y, phi)
    tot = 0.0; parts = {}
    for (cx, cy, name, fpole) in [(1.0, 0.0, 'near1', fp1), (0.0, 0.0, 'near0', fp0)]:
        lr = np.linspace(np.log(rho_min), np.log(Rn), int(nr*np.log(Rn/rho_min)) + 1)
        lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
        th = np.linspace(0, 2*np.pi, nth + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
        RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
        px = cx + RR*np.cos(TT); py = cy + RR*np.sin(TT)
        own = Kf(px - cx, py - cy) if cx == 1.0 else -Kf(px, py)
        other = -Kf(px, py) if cx == 1.0 else Kf(px - 1.0, py)
        fv = fval(px, py)
        val = np.sum((own*(fv - fpole) + other*fv)*RR*RR)*dlr*dth
        parts[name] = val; tot += val
    ktot = lambda px, py: Kf(px - 1.0, py) - Kf(px, py)
    lr = np.linspace(np.log(Rf), np.log(rho_max), int(nrf*np.log(rho_max/Rf)) + 1)
    lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
    th = np.linspace(0, 2*np.pi, nthf + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
    far = 0.0; last = None
    for idx in np.array_split(np.arange(len(lrc)), 16):
        RR, TT = np.meshgrid(np.exp(lrc[idx]), thc, indexing='ij')
        px = 0.5 + RR*np.cos(TT); py = RR*np.sin(TT)
        v = ktot(px, py)*fval(px, py)*RR*RR*dlr*dth
        far += v.sum(); last = (np.exp(lrc[idx][-1]), v[-1].sum()/dlr)
    parts['far'] = far; tot += far
    rl, vl = last; cc = vl/rl**(alpha - 1)
    tail = cc*rho_max**(alpha - 1)/(1 - alpha); parts['far_tail_est'] = tail; tot += tail
    xs = np.arange(0.5 - Rf, 0.5 + Rf, h) + h/2; ys = np.arange(-Rf, Rf, h) + h/2
    PX, PY = np.meshgrid(xs, ys, indexing='ij')
    inside = ((PX - 0.5)**2 + PY**2 < Rf*Rf) & ((PX - 1)**2 + PY**2 >= Rn*Rn) & (PX**2 + PY**2 >= Rn*Rn)
    val = np.sum(np.where(inside, ktot(PX, PY)*fval(PX, PY), 0.0))*h*h; parts['leftover'] = val; tot += val
    parts['I_phi'] = tot
    return abs(tot) + 0.5, parts

if __name__ == '__main__':
    alpha = float(sys.argv[1]); b = float(sys.argv[2]); c = float(sys.argv[3]); lam = eval(sys.argv[4])
    phis = [float(s) for s in sys.argv[5].split(',')]; rule = sys.argv[6]
    rho_max = float(sys.argv[7]) if len(sys.argv) > 7 else 1e9
    Z = make_Z0(b)
    for phi in phis:
        delta = {'m3': -phi/3, 'p3': phi/3, '0': 0.0}.get(rule)
        if delta is None: delta = float(rule)
        fv = lambda px, py: f_rot(px, py, alpha, b, Z, c, lam, phi, delta)
        v, parts = integrate_fun(alpha, fv, phi, rho_max=rho_max)
        print(f"alpha={alpha} b={b} c={c} lam={lam:.6f} phi={phi:.3f} delta={delta:+.4f}: D witness value = {v:.5f}  "
              + " ".join(f"{k}={x:+.4f}" for k, x in parts.items()), flush=True)
