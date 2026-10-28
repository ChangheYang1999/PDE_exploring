"""Prototype (floating point, NOT certified) of a structured lower-bound test function.

beta = pi/4 convention: K(z) = sin(2 arg z)/(2 pi |z|^2) = z1 z2/(pi |z|^4);  k(z) = K(z - e1) - K(z).
Test function  f(z) = 2^(alpha-1) sigma(z) dist(z, Z)^alpha,  Z a closed polygonal set, sigma = +-1 constant
on components of the complement  =>  [f]_alpha <= 1 (signed-distance lemma, the verification work 02_upper_bounds/PROOF.md).
Z = {z2 = 0} u Gamma_1 u Gamma_0 u mirror images (point reflection through m = e1/2):
  Gamma_1: segment (1,0)-(1,a) then ray from (1,a) in direction 60 deg;
  Gamma_0: segment (0,0)-(0,a) then ray from (0,a) in direction 120 deg.
sigma: + on the component containing {z1>1, z2>0 small}, - on the strip component above the axis, + on the
left component above the axis; odd under point reflection.
Value: I = int k f dz = T f(e1) - T f(0) (f(0) = f(e1) = 0), a lower bound for C_alpha.
"""
import numpy as np, sys

def seg_dist(px, py, ax, ay, bx, by):
    """distance from points (px,py) to segment a-b"""
    vx, vy = bx - ax, by - ay
    L2 = vx*vx + vy*vy
    t = np.clip(((px - ax)*vx + (py - ay)*vy)/L2, 0.0, 1.0)
    return np.hypot(px - ax - t*vx, py - ay - t*vy)

def ray_dist(px, py, ax, ay, dx, dy):
    t = np.maximum(((px - ax)*dx + (py - ay)*dy), 0.0)
    return np.hypot(px - ax - t*dx, py - ay - t*dy)

def make_Z(a, ang1=np.pi/3, ang0=2*np.pi/3):
    """pieces: list of ('seg', ax, ay, bx, by) or ('ray', ax, ay, dx, dy). Includes mirror images."""
    P = []
    P.append(('line_y0',))
    P.append(('seg', 1.0, 0.0, 1.0, a)); P.append(('ray', 1.0, a, np.cos(ang1), np.sin(ang1)))
    P.append(('seg', 0.0, 0.0, 0.0, a)); P.append(('ray', 0.0, a, np.cos(ang0), np.sin(ang0)))
    # mirror through m: (x,y) -> (1-x, -y); direction (dx,dy) -> (-dx,-dy)
    P.append(('seg', 0.0, 0.0, 0.0, -a)); P.append(('ray', 0.0, -a, -np.cos(ang1), -np.sin(ang1)))
    P.append(('seg', 1.0, 0.0, 1.0, -a)); P.append(('ray', 1.0, -a, -np.cos(ang0), -np.sin(ang0)))
    return P

def dist_Z(px, py, Z):
    d = np.full(px.shape, np.inf)
    for p in Z:
        if p[0] == 'line_y0':
            d = np.minimum(d, np.abs(py))
        elif p[0] == 'seg':
            d = np.minimum(d, seg_dist(px, py, *p[1:]))
        else:
            d = np.minimum(d, ray_dist(px, py, *p[1:]))
    return d

def sigma(px, py, a, ang1=np.pi/3, ang0=2*np.pi/3):
    """sign on components: upper half plane split by Gamma_1 (right of it: +), Gamma_0 (left of it: +), between: -.
    Lower half plane by odd symmetry."""
    s = np.ones(px.shape)
    up = py > 0
    # for upper half: determine whether point is right of Gamma_1, left of Gamma_0, or between
    # Gamma_1: x = 1 for y<=a; for y>a: x = 1 + (y-a)/tan(ang1)
    x1 = np.where(py <= a, 1.0, 1.0 + (py - a)/np.tan(ang1))
    x0 = np.where(py <= a, 0.0, 0.0 + (py - a)/np.tan(ang0))
    between = (px < x1) & (px > x0)
    s_up = np.where(between, -1.0, 1.0)
    # lower half: mirror point (1-px, -py) is in upper half; sigma(z) = -sigma(mirror)
    mx, my = 1.0 - px, -py
    x1m = np.where(my <= a, 1.0, 1.0 + (my - a)/np.tan(ang1))
    x0m = np.where(my <= a, 0.0, 0.0 + (my - a)/np.tan(ang0))
    betweenm = (mx < x1m) & (mx > x0m)
    s_lo = -np.where(betweenm, -1.0, 1.0)
    return np.where(up, s_up, s_lo)

def f_val(px, py, alpha, a, Z, ang1=np.pi/3, ang0=2*np.pi/3):
    return 2**(alpha - 1)*sigma(px, py, a, ang1, ang0)*dist_Z(px, py, Z)**alpha

def K(px, py):
    return px*py/(np.pi*(px*px + py*py)**2)

def k_tot(px, py):
    return K(px - 1.0, py) - K(px, py)

def integrate(alpha, a, ang1=np.pi/3, ang0=2*np.pi/3, nr=60, nth=720, rho_min=1e-9, rho_max=1e9, nrf=40, nthf=720, h=0.004, Rn=0.5, Rf=1.0):
    Z = make_Z(a, ang1, ang0)
    tot = 0.0; parts = {}
    # near fields: polar about p in {e1, 0}, own kernel + other kernel, rho in [rho_min, Rn], log-spaced midpoint
    for (cx, cy, name) in [(1.0, 0.0, 'near1'), (0.0, 0.0, 'near0')]:
        lr = np.linspace(np.log(rho_min), np.log(Rn), int(nr*np.log(Rn/rho_min)) + 1)
        lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
        th = np.linspace(0, 2*np.pi, nth + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
        RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
        px = cx + RR*np.cos(TT); py = cy + RR*np.sin(TT)
        fv = f_val(px, py, alpha, a, Z, ang1, ang0)
        val = np.sum(k_tot(px, py)*fv*RR*RR)*dlr*dth
        # inner exact part: locally Z = two perpendicular lines through p, f = 2^(a-1) sigma rho^a min(|cos|,|sin|)^a,
        # own-kernel integral over rho<rho_min = (a_2/alpha) rho_min^alpha (sign: contributions positive by construction)
        a2 = 2**(1 + alpha/2)/(np.pi*(alpha + 2))
        inner = a2/alpha*rho_min**alpha
        parts[name] = val; parts[name + '_inner'] = inner
        tot += val + inner
    # far field: polar about m, rho in [Rf, rho_max]
    lr = np.linspace(np.log(Rf), np.log(rho_max), int(nrf*np.log(rho_max/Rf)) + 1)
    lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
    th = np.linspace(0, 2*np.pi, nthf + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
    RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
    px = 0.5 + RR*np.cos(TT); py = RR*np.sin(TT)
    fv = f_val(px, py, alpha, a, Z, ang1, ang0)
    val = np.sum(k_tot(px, py)*fv*RR*RR)*dlr*dth
    parts['far'] = val; tot += val
    # tail beyond rho_max (estimate): per-circle n=3 extremizer value 2 a_3 rho^(alpha-2) integrated
    from scipy.integrate import quad
    a3 = 3/np.pi*quad(lambda t: np.sin(3*t)*(2*np.sin(t))**alpha, 0, np.pi/6)[0]
    tail = 2*a3/(1 - alpha)*rho_max**(alpha - 1)
    parts['far_tail_est'] = tail; tot += tail
    # leftover: B(m,Rf) minus the two near disks, Cartesian midpoint with subsampling of indicator
    xs = np.arange(0.5 - Rf, 0.5 + Rf, h) + h/2; ys = np.arange(-Rf, Rf, h) + h/2
    PX, PY = np.meshgrid(xs, ys, indexing='ij')
    inside = ((PX - 0.5)**2 + PY**2 < Rf*Rf) & ((PX - 1)**2 + PY**2 >= Rn*Rn) & (PX**2 + PY**2 >= Rn*Rn)
    fv = f_val(PX, PY, alpha, a, Z, ang1, ang0)
    val = np.sum(np.where(inside, k_tot(PX, PY)*fv, 0.0))*h*h
    parts['leftover'] = val; tot += val
    return tot, parts

if __name__ == "__main__":
    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    for a in [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5]:
        tot, parts = integrate(alpha, a)
        print(f"alpha={alpha} a={a:.2f}: I = {tot:.5f}   " + " ".join(f"{k}={v:+.4f}" for k, v in parts.items()), flush=True)

# ---- exact zero curve of nu (beta = pi/4), verifier's parametrisation (t > 1, half-distance a0 = 1/2):
#      y = 2 a0 sqrt(t (t^2+t+1))/(t^2-1),  b = a0 (t^2+1)/(t^2-1);  curve from the pole (1,0): (1/2 + b, y).
def make_Z_exact(npts=400, t_lo=1 + 1e-3, t_hi=1e7):
    a0 = 0.5
    t = np.exp(np.linspace(np.log(t_hi - 1), np.log(t_lo - 1), npts)) + 1.0   # from near the pole outward
    y = 2*a0*np.sqrt(t*(t*t + t + 1))/(t*t - 1); b = a0*(t*t + 1)/(t*t - 1)
    P = [('line_y0',)]
    def add_curve(sx, sy):
        # sx, sy = +-1: curve from pole (1,0) if sx=+1 (points (1/2 + b, sy*y)), from pole (0,0) if sx=-1 (points (1/2 - b, sy*y))
        xs = 0.5 + sx*b; ys = sy*y
        P.append(('seg', 1.0 if sx > 0 else 0.0, 0.0, xs[0], ys[0]))
        for i in range(len(xs) - 1):
            P.append(('seg', xs[i], ys[i], xs[i+1], ys[i+1]))
        P.append(('ray', xs[-1], ys[-1], sx*0.5, sy*np.sqrt(3)/2))
    add_curve(+1, +1); add_curve(+1, -1); add_curve(-1, +1); add_curve(-1, -1)
    return P

def sigma_exact(px, py):
    """sign = sgn(nu) with nu = K(z - e1) - K(z), K = z1 z2/(pi|z|^4); exact-zero-set version."""
    nu = K(px - 1.0, py) - K(px, py)
    return np.sign(nu)

def integrate_exact(alpha, nr=50, nth=720, rho_min=1e-9, rho_max=1e9, nrf=30, nthf=720, h=0.004, Rn=0.5, Rf=1.0, npts=400):
    Z = make_Z_exact(npts)
    fval = lambda px, py: 2**(alpha - 1)*sigma_exact(px, py)*dist_Z(px, py, Z)**alpha
    tot = 0.0; parts = {}
    for (cx, cy, name) in [(1.0, 0.0, 'near1'), (0.0, 0.0, 'near0')]:
        lr = np.linspace(np.log(rho_min), np.log(Rn), int(nr*np.log(Rn/rho_min)) + 1)
        lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
        th = np.linspace(0, 2*np.pi, nth + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
        RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
        px = cx + RR*np.cos(TT); py = cy + RR*np.sin(TT)
        val = np.sum(k_tot(px, py)*fval(px, py)*RR*RR)*dlr*dth
        a2 = 2**(1 + alpha/2)/(np.pi*(alpha + 2)); inner = a2/alpha*rho_min**alpha
        parts[name] = val; tot += val + inner
    lr = np.linspace(np.log(Rf), np.log(rho_max), int(nrf*np.log(rho_max/Rf)) + 1)
    lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
    th = np.linspace(0, 2*np.pi, nthf + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
    RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
    px = 0.5 + RR*np.cos(TT); py = RR*np.sin(TT)
    val = np.sum(k_tot(px, py)*fval(px, py)*RR*RR)*dlr*dth; parts['far'] = val; tot += val
    from scipy.integrate import quad
    a3 = 3/np.pi*quad(lambda t: np.sin(3*t)*(2*np.sin(t))**alpha, 0, np.pi/6)[0]
    tail = 2*a3/(1 - alpha)*rho_max**(alpha - 1); parts['far_tail_est'] = tail; tot += tail
    xs = np.arange(0.5 - Rf, 0.5 + Rf, h) + h/2; ys = np.arange(-Rf, Rf, h) + h/2
    PX, PY = np.meshgrid(xs, ys, indexing='ij')
    inside = ((PX - 0.5)**2 + PY**2 < Rf*Rf) & ((PX - 1)**2 + PY**2 >= Rn*Rn) & (PX**2 + PY**2 >= Rn*Rn)
    val = np.sum(np.where(inside, k_tot(PX, PY)*fval(PX, PY), 0.0))*h*h; parts['leftover'] = val; tot += val
    return tot, parts

# ---- asymmetric clamped witness for D_alpha (the verification work 07_diagonal_identity_term/asymmetric_cusps, with the polygon zero set):
#   v = sigma * dist(., Z(a)) (1-Lipschitz); A + B = 1, p = 1/(1-alpha), M = (A^p + B^p)^(-1/p), c = 1/2 - A;
#   on H = {z1 > 1/2}: h = (1/2)(2 (z1 - 1/2))^alpha, u = c + M (A v_+^alpha - B v_-^alpha), f = clamp(u, -h, h); f(1 - z1, -z2) = -f(z).
#   [f]_alpha <= 1; f(e1) = c, f(0) = -c.  D-functional: (T - I/2) increment = int k f dz - c.
def f_asym(px, py, alpha, a, A, Z):
    B = 1 - A; p = 1/(1 - alpha); M = (A**p + B**p)**(-1/p); c = 0.5 - A
    right = px > 0.5
    qx = np.where(right, px, 1 - px); qy = np.where(right, py, -py)      # map to H
    v = sigma(qx, qy, a)*dist_Z(qx, qy, Z)
    u = c + M*(A*np.maximum(v, 0)**alpha - B*np.maximum(-v, 0)**alpha)
    h = 0.5*(2*np.maximum(qx - 0.5, 0))**alpha
    f = np.maximum(-h, np.minimum(h, u))
    return np.where(right, f, -f)

def integrate_asym(alpha, a, A, nr=50, nth=720, rho_min=1e-9, rho_max=1e9, nrf=30, nthf=720, h=0.004, Rn=0.5, Rf=1.0):
    Z = make_Z(a)
    fval = lambda px, py: f_asym(px, py, alpha, a, A, Z)
    B = 1 - A; p = 1/(1 - alpha); M = (A**p + B**p)**(-1/p); c = 0.5 - A
    tot = -c; parts = {'identity': -c}
    for (cx, cy, name) in [(1.0, 0.0, 'near1'), (0.0, 0.0, 'near0')]:
        lr = np.linspace(np.log(rho_min), np.log(Rn), int(nr*np.log(Rn/rho_min)) + 1)
        lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
        th = np.linspace(0, 2*np.pi, nth + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
        RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
        px = cx + RR*np.cos(TT); py = cy + RR*np.sin(TT)
        val = np.sum(k_tot(px, py)*fval(px, py)*RR*RR)*dlr*dth
        a2 = 2**(1 + alpha/2)/(np.pi*(alpha + 2)); inner = M*2**(-alpha)*a2/alpha*rho_min**alpha   # unclamped near the pole (checked by the clamp test below)
        parts[name] = val; tot += val + inner
    lr = np.linspace(np.log(Rf), np.log(rho_max), int(nrf*np.log(rho_max/Rf)) + 1)
    lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
    th = np.linspace(0, 2*np.pi, nthf + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
    RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
    px = 0.5 + RR*np.cos(TT); py = RR*np.sin(TT)
    val = np.sum(k_tot(px, py)*fval(px, py)*RR*RR)*dlr*dth; parts['far'] = val; tot += val
    xs = np.arange(0.5 - Rf, 0.5 + Rf, h) + h/2; ys = np.arange(-Rf, Rf, h) + h/2
    PX, PY = np.meshgrid(xs, ys, indexing='ij')
    inside = ((PX - 0.5)**2 + PY**2 < Rf*Rf) & ((PX - 1)**2 + PY**2 >= Rn*Rn) & (PX**2 + PY**2 >= Rn*Rn)
    val = np.sum(np.where(inside, k_tot(PX, PY)*fval(PX, PY), 0.0))*h*h; parts['leftover'] = val; tot += val
    # clamp check at the pole: |c| + M max(A,B) rho_min^alpha <= (1/2)(1 - 2 rho_min)^alpha
    parts['clamp_ok_inner'] = bool(abs(c) + M*max(A, B)*rho_min**alpha <= 0.5*(1 - 2*rho_min)**alpha)
    return tot, parts

# ---- lead's lattice D witness (Note 12, N10): H = {z1 > 1/2} (contains the pole e1), h = (1/2)(2(z1 - 1/2))^alpha on H,
#   F = lambda*g - t with g = polygon C witness (odd under P z = (1 - z1, -z2), g(e1) = 0), t >= 1/2;
#   f = max(-h, min(h, F)) on H, f(Pz) = -f(z); f(e1) = -1/2, f(0) = +1/2; D_alpha >= |int k f| + 1/2.
def f_lattice(px, py, alpha, a, Z, t, lam=1.0):
    right = px > 0.5
    qx = np.where(right, px, 1 - px); qy = np.where(right, py, -py)      # map to H
    g = lam*f_val(qx, qy, alpha, a, Z)
    h = 0.5*(2*np.maximum(qx - 0.5, 0))**alpha
    f = np.maximum(-h, np.minimum(h, g - t))
    return np.where(right, f, -f)

def integrate_lattice(alpha, a, t, lam=1.0, nr=50, nth=720, rho_min=1e-7, rho_max=1e9, nrf=30, nthf=720, h=0.004, Rn=0.5, Rf=1.0):
    Z = make_Z(a)
    fval = lambda px, py: f_lattice(px, py, alpha, a, Z, t, lam)
    tot = 0.0; parts = {}
    for (cx, cy, name, fpole) in [(1.0, 0.0, 'near1', -0.5), (0.0, 0.0, 'near0', 0.5)]:
        lr = np.linspace(np.log(rho_min), np.log(Rn), int(nr*np.log(Rn/rho_min)) + 1)
        lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
        th = np.linspace(0, 2*np.pi, nth + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
        RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
        px = cx + RR*np.cos(TT); py = cy + RR*np.sin(TT)
        # own kernel against (f - f(pole)) (p.v. cancellation of the constant), cross kernel against f
        own = K(px - cx, py - cy) if cx == 1.0 else -K(px, py)
        other = -K(px, py) if cx == 1.0 else K(px - 1.0, py)
        fv = fval(px, py)
        val = np.sum((own*(fv - fpole) + other*fv)*RR*RR)*dlr*dth
        parts[name] = val; tot += val
    lr = np.linspace(np.log(Rf), np.log(rho_max), int(nrf*np.log(rho_max/Rf)) + 1)
    lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
    th = np.linspace(0, 2*np.pi, nthf + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
    RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
    px = 0.5 + RR*np.cos(TT); py = RR*np.sin(TT)
    val = np.sum(k_tot(px, py)*fval(px, py)*RR*RR)*dlr*dth; parts['far'] = val; tot += val
    xs = np.arange(0.5 - Rf, 0.5 + Rf, h) + h/2; ys = np.arange(-Rf, Rf, h) + h/2
    PX, PY = np.meshgrid(xs, ys, indexing='ij')
    inside = ((PX - 0.5)**2 + PY**2 < Rf*Rf) & ((PX - 1)**2 + PY**2 >= Rn*Rn) & (PX**2 + PY**2 >= Rn*Rn)
    val = np.sum(np.where(inside, k_tot(PX, PY)*fval(PX, PY), 0.0))*h*h; parts['leftover'] = val; tot += val
    parts['transport'] = tot; parts['D_value'] = abs(tot) + 0.5
    return abs(tot) + 0.5, parts

# ============ AXIS direction (beta = 0): kernel K0(z) = cos(2 theta)/(2 pi r^2) = (z1^2 - z2^2)/(2 pi |z|^4), k0 = K0(. - e1) - K0(.)
# k0 is odd under the midline reflection M: (z1,z2) -> (1 - z1, z2) and even under z2 -> -z2.
# Axis polygon zero set Z0(b): midline {z1 = 1/2}; the X: segments e1 -> (1/2, +-1/2) and 0 -> (1/2, +-1/2);
#   from e1: segments e1 -> e1 + b(1, +-1), then rays in directions (cos 30, +-sin 30); from 0: segments 0 -> -b(1, -+1)... i.e. 0 -> (-b, +-b),
#   then rays in directions (cos 150, +-sin 150).  sigma: for z1 > 1/2 with w = z - e1: + if |w2| < B(w1) else -, where
#   B(w1) = -w1 for -1/2 < w1 <= 0 (the X), = w1 for 0 <= w1 <= b, = b + (w1 - b) tan 30 for w1 > b;  sigma(Mz) = -sigma(z).
#   This matches the signs of K0(z - e1) near e1 (positive in the right/left sectors) and of the far dipole cos(3 theta).
def K0(x, y):
    return (x*x - y*y)/(2*np.pi*(x*x + y*y)**2)
def k0_tot(px, py):
    return K0(px - 1.0, py) - K0(px, py)
T30 = np.tan(np.pi/6)
def make_Z0(b):
    c30, s30 = np.cos(np.pi/6), np.sin(np.pi/6)
    P = [('line_x05',)]
    P += [('seg', 1.0, 0.0, 0.5, 0.5), ('seg', 1.0, 0.0, 0.5, -0.5), ('seg', 0.0, 0.0, 0.5, 0.5), ('seg', 0.0, 0.0, 0.5, -0.5)]
    P += [('seg', 1.0, 0.0, 1.0 + b, b), ('ray', 1.0 + b, b, c30, s30), ('seg', 1.0, 0.0, 1.0 + b, -b), ('ray', 1.0 + b, -b, c30, -s30)]
    P += [('seg', 0.0, 0.0, -b, b), ('ray', -b, b, -c30, s30), ('seg', 0.0, 0.0, -b, -b), ('ray', -b, -b, -c30, -s30)]
    return P
def dist_Z0(px, py, Z):
    d = np.full(px.shape, np.inf)
    for p in Z:
        if p[0] == 'line_x05': d = np.minimum(d, np.abs(px - 0.5))
        elif p[0] == 'seg': d = np.minimum(d, seg_dist(px, py, *p[1:]))
        else: d = np.minimum(d, ray_dist(px, py, *p[1:]))
    return d
def sigma0(px, py, b):
    right = px > 0.5
    qx = np.where(right, px, 1 - px); w1 = qx - 1.0; w2 = np.abs(py)
    B = np.where(w1 <= 0, -w1, np.where(w1 <= b, w1, b + (w1 - b)*T30))
    s = np.where(w2 < B, 1.0, -1.0)
    return np.where(right, s, -s)
def f0_val(px, py, alpha, b, Z):
    return 2**(alpha - 1)*sigma0(px, py, b)*dist_Z0(px, py, Z)**alpha
def f0_lattice(px, py, alpha, b, Z, t, lam=1.0):
    right = px > 0.5
    qx = np.where(right, px, 1 - px)
    g = lam*f0_val(qx, py, alpha, b, Z)
    h = 0.5*(2*np.maximum(qx - 0.5, 0))**alpha
    f = np.maximum(-h, np.minimum(h, g - t))
    return np.where(right, f, -f)
def integrate_axis(alpha, b, t=None, lam=1.0, nr=50, nth=720, rho_min=1e-7, rho_max=1e9, nrf=30, nthf=720, h=0.004, Rn=0.5, Rf=1.0):
    """t=None: C witness f0 (value int k0 f0); else lattice D witness (value |int k0 f| + 1/2). Pole values: C: 0,0; D: -1/2 at e1, +1/2 at 0."""
    Z = make_Z0(b)
    if t is None:
        fval = lambda px, py: f0_val(px, py, alpha, b, Z); fp1, fp0 = 0.0, 0.0
    else:
        fval = lambda px, py: f0_lattice(px, py, alpha, b, Z, t, lam); fp1, fp0 = -0.5, 0.5
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
    RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
    px = 0.5 + RR*np.cos(TT); py = RR*np.sin(TT)
    val = np.sum(k0_tot(px, py)*fval(px, py)*RR*RR)*dlr*dth; parts['far'] = val; tot += val
    xs = np.arange(0.5 - Rf, 0.5 + Rf, h) + h/2; ys = np.arange(-Rf, Rf, h) + h/2
    PX, PY = np.meshgrid(xs, ys, indexing='ij')
    inside = ((PX - 0.5)**2 + PY**2 < Rf*Rf) & ((PX - 1)**2 + PY**2 >= Rn*Rn) & (PX**2 + PY**2 >= Rn*Rn)
    val = np.sum(np.where(inside, k0_tot(PX, PY)*fval(PX, PY), 0.0))*h*h; parts['leftover'] = val; tot += val
    parts['transport'] = tot
    return (abs(tot) + 0.5 if t is not None else tot), parts
