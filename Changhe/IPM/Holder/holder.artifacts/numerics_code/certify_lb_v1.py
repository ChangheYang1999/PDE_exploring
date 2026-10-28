"""CERTIFIED lower bound for C_alpha (and D_alpha) from the explicit signed-distance test function.

Convention (beta = pi/4): K(z) = z1 z2 / (pi |z|^4) = sin(2 arg z)/(2 pi |z|^2);  k(z) = K(z - e1) - K(z).
Zero set Z (closed, polygonal; parameter a > 0):
   axis {z2 = 0};  Gamma_1 = [(1,0),(1,a)] u ray((1,a), dir 60deg);  Gamma_0 = [(0,0),(0,a)] u ray((0,a), dir 120deg);
   and the images of Gamma_1, Gamma_0 under the point reflection P(z) = (1 - z1, -z2) (through m = e1/2).
sigma = +1 on the upper-half-plane components right of Gamma_1 and left of Gamma_0, -1 between; sigma(Pz) = -sigma(z).
f(z) = 2^(alpha-1) sigma(z) D(z)^alpha,  D = dist(., Z).   [f]_alpha <= 1 (signed-distance lemma), f(0)=f(e1)=0.
I = int k f dz = T f(e1) - T f(0)  is a lower bound for C_alpha = ||T_xy|| = ||T_xx|| and for D_alpha.

Symmetry: k(Pz) = -k(z), f(Pz) = -f(z), so g = k f is P-even and  I = 2 int_{B(e1,1/2)} g + int_{R^2 minus two disks} g.

Enclosure method (all arithmetic in arb balls, python-flint):
 * polar cells about e1 (rho in [rho_min, 1/2]) and about m (rho in [rho_m, rho_max], cells inside the two
   near disks skipped, partial cells bounded crudely by sup|g| * area);
 * on each full cell Q with centre c and r_Q = max_{z in Q} |z - c|:
       int_Q g in |Q| * ( g(c) + [-1,1] * dev ),
       dev = kbar * Delta_f + |f(c)| * kbar' * r_Q,
       kbar  >= sup_{B(c,r_Q)} |k|  via |K(w)| <= 1/(2 pi |w|^2),
       kbar' >= sup_{B(c,r_Q)} |grad k| via |grad K(w)| = 1/(pi |w|^3),
       Delta_f >= sup_{B(c,r_Q)} |f(z) - f(c)|: r_Q^alpha always (since [f]_alpha <= 1); if D(c) > r_Q also
                  2^(alpha-1) alpha (D(c) - r_Q)^(alpha-1) r_Q (sigma constant on B(c,r_Q), D 1-Lipschitz).
 * about e1, for rho_2 < a/2 the nearest part of Z is one of the two local lines, so the own-kernel integral
   over the annulus is exactly (a_2/alpha)(rho_2^alpha - rho_1^alpha); only the cross kernel -K(z) is quadratured there;
 * inner ball |z - e1| < rho_min: own kernel exact (a_2/alpha) rho_min^alpha, cross kernel bounded;
 * tail |z - m| > rho_max: |k| <= 1/(pi (rho - 1/2)^3), |f| <= 2^(alpha-1) rho^alpha (m in Z);
 * sliver |z - m| < rho_m outside the disks: area <= (4/3) rho_m^3, |g| bounded.
"""
import sys, json, time, math
from flint import arb, ctx, fmpq
import multiprocessing as mp

ctx.prec = 80

def A(x): return arb(x)
PI = None

def setup(alpha_q, a_q):
    global PI, ALPHA, AA, C60, S60, C120, S120, TWO_AM1, A2
    PI = arb.pi()
    ALPHA = arb(alpha_q); AA = arb(a_q)
    C60 = arb(1)/2; S60 = arb(3).sqrt()/2; C120 = -arb(1)/2; S120 = S60
    TWO_AM1 = arb(2)**(ALPHA - 1)
    A2 = arb(2)**(1 + ALPHA/2)/(PI*(ALPHA + 2))

def seg_dist(px, py, ax, ay, bx, by):
    vx = bx - ax; vy = by - ay; L2 = vx*vx + vy*vy
    t = ((px - ax)*vx + (py - ay)*vy)/L2
    t = arb.max(arb.min(t, arb(1)), arb(0))
    dx = px - ax - t*vx; dy = py - ay - t*vy
    return (dx*dx + dy*dy).sqrt()

def ray_dist(px, py, ax, ay, dx, dy):
    t = arb.max((px - ax)*dx + (py - ay)*dy, arb(0))
    ex = px - ax - t*dx; ey = py - ay - t*dy
    return (ex*ex + ey*ey).sqrt()

def dist_Z(px, py):
    d = abs(py)
    one = arb(1); zero = arb(0)
    d = arb.min(d, seg_dist(px, py, one, zero, one, AA))
    d = arb.min(d, ray_dist(px, py, one, AA, C60, S60))
    d = arb.min(d, seg_dist(px, py, zero, zero, zero, AA))
    d = arb.min(d, ray_dist(px, py, zero, AA, C120, S120))
    d = arb.min(d, seg_dist(px, py, zero, zero, zero, -AA))
    d = arb.min(d, ray_dist(px, py, zero, -AA, -C60, -S60))
    d = arb.min(d, seg_dist(px, py, one, zero, one, -AA))
    d = arb.min(d, ray_dist(px, py, one, -AA, -C120, -S120))
    return d

def sigma_upper(px, py):
    """sign for a point with py > 0 (certified), or None if undecidable."""
    # x1(y): boundary Gamma_1 ; x0(y): boundary Gamma_0
    if py <= AA:
        x1 = arb(1); x0 = arb(0)
    elif py > AA:
        x1 = 1 + (py - AA)*C60/S60; x0 = (py - AA)*C120/S120
    else:
        return None
    if px > x1 or px < x0:
        return arb(1)
    if px < x1 and px > x0:
        return arb(-1)
    return None

def sigma(px, py):
    if py > 0:
        return sigma_upper(px, py)
    if py < 0:
        s = sigma_upper(1 - px, -py)
        return None if s is None else -s
    return None

def Kf(px, py):
    r2 = px*px + py*py
    return px*py/(PI*r2*r2)

def k_tot(px, py):
    return Kf(px - 1, py) - Kf(px, py)

def pow_nonneg(D, e):
    """D^e for a ball D known to be >= 0 mathematically; if the ball straddles 0 return [0, upper^e]"""
    if D > 0:
        return D**e
    up = arb(D.upper())
    return arb(0).union(up**e) if up > 0 else arb(0)

def f_val(px, py):
    """returns (f(c) as arb ball, D(c), decided:bool)"""
    D = arb.max(dist_Z(px, py), arb(0))
    s = sigma(px, py)
    Da = pow_nonneg(D, ALPHA)
    if s is None:
        return TWO_AM1*Da*arb(0).union(arb(1)).union(arb(-1)), D, False  # [-1,1] * 2^(a-1) D^a
    return TWO_AM1*s*Da, D, True

def kernel_bounds(cx, cy, rQ, d1, d0, cross_only=False):
    """upper bounds for sup |k| and sup |grad k| over B(c, rQ); d1, d0 lower bounds of distances to e1, 0.
    Uses the direct bounds and, outside |z-m| > 1/2 + rQ, the dipole (mean value) bounds
    |k| <= 1/(pi (dm-1/2)^3), |grad k| <= 3/(pi (dm-1/2)^4), dm = lower bound of |z - m|."""
    if cross_only:
        return 1/(2*PI*d0*d0), 1/(PI*d0*d0*d0)
    kbar = 1/(2*PI*d1*d1) + 1/(2*PI*d0*d0)
    kbar1 = 1/(PI*d1*d1*d1) + 1/(PI*d0*d0*d0)
    dm = lower_dist(cx, cy, rQ, arb(1)/2, arb(0))
    if dm is not None and dm > arb(1)/2:
        e = dm - arb(1)/2
        kbar = arb.min(kbar, 1/(PI*e*e*e)); kbar1 = arb.min(kbar1, 3/(PI*e*e*e*e))
    return kbar, kbar1

def cell_enclosure(cx, cy, rQ, area, d1, d0, cross_only=False):
    """Enclosure of int_Q g for a cell contained in B(c, rQ) with area `area`;
    d1, d0: lower bounds for the distance from B(c,rQ) to e1 and to 0 (arb, > 0).
    cross_only: integrand is -K(z) f(z) only (own-kernel part handled exactly)."""
    fc, D, decided = f_val(cx, cy)
    kc = -Kf(cx, cy) if cross_only else k_tot(cx, cy)
    kbar, kbar1 = kernel_bounds(cx, cy, rQ, d1, d0, cross_only)
    Df = rQ**ALPHA
    if decided and (D > rQ):
        Df = arb.min(Df, TWO_AM1*ALPHA*(D - rQ)**(ALPHA - 1)*rQ)
    dev = kbar*Df + abs(fc)*kbar1*rQ
    g = kc*fc
    return area*(g + dev*arb(0).union(arb(1)).union(arb(-1)))

def polar_cells(center, rho_edges, ntheta):
    """yield (rho1, rho2, theta1, theta2, j, l)"""
    for j in range(len(rho_edges) - 1):
        for l in range(ntheta):
            yield (rho_edges[j], rho_edges[j+1], l, ntheta)

def cell_geom(center, rho1, rho2, l, ntheta):
    cx0, cy0 = center
    th1 = 2*PI*l/ntheta; th2 = 2*PI*(l + 1)/ntheta; thc = PI*(2*l + 1)/ntheta
    rhoc = (rho1 + rho2)/2
    cx = cx0 + rhoc*thc.cos(); cy = cy0 + rhoc*thc.sin()
    area = (rho2*rho2 - rho1*rho1)/2*(th2 - th1)
    # r_Q = distance from centre to the far corner (rho2, th1): sqrt(rhoc^2 + rho2^2 - 2 rhoc rho2 cos(dth/2))
    dth2 = PI/ntheta
    rQ = (rhoc*rhoc + rho2*rho2 - 2*rhoc*rho2*dth2.cos()).sqrt()
    # make rQ an upper bound: take upper endpoint of the ball
    rQ = arb(rQ.upper()) if hasattr(rQ, 'upper') else rQ
    return cx, cy, rQ, area, th1, th2

def lower_dist(cx, cy, rQ, qx, qy):
    """lower bound for dist(B(c,rQ), q) = max(|c-q| - rQ, 0) (lower endpoint)"""
    d = ((cx - qx)**2 + (cy - qy)**2).sqrt() - rQ
    lo = d.lower() if hasattr(d, 'lower') else d
    return arb(lo) if lo > 0 else None

def worker(task):
    """task: dict with kind, params; returns (sum enclosure as (mid, rad) strings, count)"""
    setup(task['alpha_q'], task['a_q'])
    kind = task['kind']
    total = arb(0); n = 0
    rho_edges = [arb(s) for s in task['rho_edges']]
    ntheta = task['ntheta']
    if kind == 'near_e1':
        center = (arb(1), arb(0)); cross = task['cross_only']
        for j in range(len(rho_edges) - 1):
            r1, r2 = rho_edges[j], rho_edges[j+1]
            for l in range(ntheta):
                cx, cy, rQ, area, _, _ = cell_geom(center, r1, r2, l, ntheta)
                d1 = arb(r1.lower()) if r1 > 0 else None
                d0 = lower_dist(cx, cy, rQ, arb(0), arb(0))
                total += cell_enclosure(cx, cy, rQ, area, d1, d0, cross_only=cross); n += 1
    elif kind == 'm_system':
        center = (arb(1)/2, arb(0))
        gbar_partial = arb(0)
        for j in range(len(rho_edges) - 1):
            r1, r2 = rho_edges[j], rho_edges[j+1]
            for l in range(ntheta):
                th1 = 2*PI*l/ntheta; th2 = 2*PI*(l + 1)/ntheta
                # |cos theta| range on [th1, th2]
                c1 = th1.cos(); c2 = th2.cos()
                amax = arb.max(abs(c1), abs(c2))
                # if the interval contains 0 or pi, max |cos| = 1
                if (th1 <= 0 <= th2) or (th1 <= PI <= th2) or (th1 <= 2*PI <= th2):
                    amax = arb(1)
                amin = arb.min(abs(c1), abs(c2))
                if (th1 <= PI/2 <= th2) or (th1 <= 3*PI/2 <= th2):
                    amin = arb(0)
                if r2 <= amin:
                    continue  # entirely inside a near disk
                cx, cy, rQ, area, _, _ = cell_geom(center, r1, r2, l, ntheta)
                d1 = lower_dist(cx, cy, rQ, arb(1), arb(0)); d0 = lower_dist(cx, cy, rQ, arb(0), arb(0))
                if d1 is None or d0 is None:
                    # cell touches a singular point: must be partial/inside; bound crudely using distance >= 1/2 outside disks
                    d1 = arb(1)/2; d0 = arb(1)/2
                if r1 >= amax:
                    total += cell_enclosure(cx, cy, rQ, area, d1, d0); n += 1
                else:
                    # partial cell: |int_{Q cap L} g| <= area * sup |g|, sup|g| <= kbar * 2^(a-1) (D(c)+rQ)^alpha
                    kbar, _ = kernel_bounds(cx, cy, rQ, d1, d0)
                    D = arb.max(dist_Z(cx, cy), arb(0))
                    gb = kbar*TWO_AM1*pow_nonneg(D + rQ, ALPHA)
                    total += area*gb*arb(0).union(arb(1)).union(arb(-1)); n += 1
    return (total.mid().str(30), total.rad().str(10), n)

def geometric_edges(r_lo, r_hi, delta):
    """edges from r_lo to r_hi with ratio about (1+delta); returned as strings of exact rationals? use arb-exact doubles."""
    nseg = max(1, int(math.ceil(math.log(r_hi/r_lo)/math.log(1 + delta))))
    edges = [r_lo*(r_hi/r_lo)**(i/nseg) for i in range(nseg + 1)]
    edges[0] = r_lo; edges[-1] = r_hi
    return [repr(e) for e in edges]  # parsed by arb(str) exactly as the printed double

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--alpha', type=str, required=True, help='exact rational, e.g. 1/2')
    ap.add_argument('--a', type=str, default='1/2')
    ap.add_argument('--delta', type=float, default=0.02, help='relative cell size in the high-resolution regions')
    ap.add_argument('--delta_cross', type=float, default=0.1)
    ap.add_argument('--delta_far0', type=float, default=0.02)
    ap.add_argument('--rho_min', type=float, default=1e-6)
    ap.add_argument('--rho_m', type=float, default=0.01)
    ap.add_argument('--rho_max', type=float, default=1e8)
    ap.add_argument('--nproc', type=int, default=6)
    ap.add_argument('--out', type=str, default=None)
    args = ap.parse_args()
    alpha_q = fmpq(*[int(x) for x in args.alpha.split('/')]) if '/' in args.alpha else fmpq(int(args.alpha))
    a_q = fmpq(*[int(x) for x in args.a.split('/')]) if '/' in args.a else fmpq(int(args.a))
    setup(alpha_q, a_q)
    alpha = float(alpha_q.p)/float(alpha_q.q); a = float(a_q.p)/float(a_q.q)
    t0 = time.time()
    tasks = []
    # near e1: exact own kernel for rho < a/2 (cross-only quadrature, coarse), full quadrature for rho in [a/2, 1/2]
    r_split = a/2 if a/2 < 0.5 else 0.5
    ntheta_c = int(math.ceil(2*math.pi/args.delta_cross)); ntheta_c += ntheta_c % 2
    edges_c = geometric_edges(args.rho_min, r_split, args.delta_cross)
    # chunk radial edges into tasks of ~ 20 shells
    def chunk(edges, kind, ntheta, extra):
        step = max(1, 4000 // ntheta)
        for i in range(0, len(edges) - 1, step):
            sub = edges[i:i + step + 1]
            tasks.append(dict(kind=kind, rho_edges=sub, ntheta=ntheta, alpha_q=str(alpha_q), a_q=str(a_q), **extra))
    chunk(edges_c, 'near_e1', ntheta_c, dict(cross_only=True))
    ntheta_n = int(math.ceil(2*math.pi/args.delta)); ntheta_n += ntheta_n % 2
    if r_split < 0.5:
        edges_n = geometric_edges(r_split, 0.5, args.delta)
        chunk(edges_n, 'near_e1', ntheta_n, dict(cross_only=False))
    # m system: [rho_m, 1] at delta_far0; [1, rho_max] with growing delta
    edges_m0 = geometric_edges(args.rho_m, 1.0, args.delta_far0)
    ntheta_m0 = int(math.ceil(2*math.pi/args.delta_far0)); ntheta_m0 += ntheta_m0 % 2
    chunk(edges_m0, 'm_system', ntheta_m0, dict())
    # far: blocks of one decade each, delta_k = delta_far0 * (rho_block)^((1-alpha)/2) capped
    rlo = 1.0
    while rlo < args.rho_max:
        rhi = min(rlo*10, args.rho_max)
        dk = min(0.2, args.delta_far0*rlo**((1 - alpha)/4))
        nth = int(math.ceil(2*math.pi/dk)); nth += nth % 2
        chunk(geometric_edges(rlo, rhi, dk), 'm_system', nth, dict())
        rlo = rhi
    print(f"tasks: {len(tasks)}  (alpha={alpha}, a={a})", flush=True)
    with mp.Pool(args.nproc) as pool:
        results = pool.map(worker, tasks, chunksize=1)
    total = arb(0); ncells = 0
    for mid, rad, n in results:
        total += arb(mid, rad) if False else (arb(mid) + arb(0, rad))
        ncells += n
    # the m-system covers the plane outside the two near disks (except sliver + tail); near_e1 covers B(e1,1/2) minus inner ball
    # and by symmetry B(0,1/2) contributes the same as B(e1,1/2): total = 2*near + rest
    near = arb(0); rest = arb(0)
    for (mid, rad, n), t in zip(results, tasks):
        v = arb(mid) + arb(0, rad)
        if t['kind'] == 'near_e1': near += v
        else: rest += v
    # exact inner own-kernel pieces: annuli rho in [rho_min, r_split] and inner ball [0, rho_min]: total (a_2/alpha) r_split^alpha
    exact_own = A2/ALPHA*arb(repr(r_split))**ALPHA
    # inner ball cross term: |K(z)| <= 1/(2 pi (1-rho_min)^2), |f| <= 2^(a-1) rho_min^a, area pi rho_min^2
    rm = arb(repr(args.rho_min))
    inner_cross = PI*rm*rm/(2*PI*(1 - rm)**2)*TWO_AM1*rm**ALPHA*arb(0).union(arb(1)).union(arb(-1))
    near_total = near + exact_own + inner_cross
    # sliver about m: area <= (4/3) rho_m^3, |g| <= (1/(2 pi (1/2)^2))*2 * 2^(a-1) (rho_m + 1/2)^a ... use |k| <= 4/pi (both terms), D <= |z-m|+... D <= |z - m| <= rho_m
    rmm = arb(repr(args.rho_m))
    sliver = arb(4)/3*rmm**3*(4/PI)*TWO_AM1*rmm**ALPHA*arb(0).union(arb(1)).union(arb(-1))
    # tail beyond rho_max: int_{rho>R} 2 pi rho * 2^(a-1) rho^a /(pi (rho-1/2)^3) drho <= 2^a (R/(R-1/2))^3 R^(alpha-1)/(1-alpha)
    R = arb(repr(args.rho_max))
    tail = arb(2)**ALPHA*(R/(R - arb(1)/2))**3*R**(ALPHA - 1)/(1 - ALPHA)*arb(0).union(arb(1)).union(arb(-1))
    I = 2*near_total + rest + sliver + tail
    el = time.time() - t0
    print(f"cells {ncells}  time {el:.0f}s")
    print(f"near (B(e1,1/2)) = {near_total.str(12, radius=True)}  [quadrature {near.str(10, radius=True)}, exact own {exact_own.str(10)}]")
    print(f"rest (outside disks) = {rest.str(12, radius=True)}   sliver {sliver.str(5, radius=True)}   tail {tail.str(5, radius=True)}")
    print(f"I = {I.str(15, radius=True)}   lower bound = {I.lower().str(15)}")
    if args.out:
        json.dump(dict(alpha=str(alpha_q), a=str(a_q), params=vars(args), cells=ncells, time_s=el,
                       near=near_total.str(20, radius=True), rest=rest.str(20, radius=True), sliver=sliver.str(8, radius=True),
                       tail=tail.str(8, radius=True), I=I.str(20, radius=True), I_lower=I.lower().str(20), I_upper=I.upper().str(20),
                       prec_bits=ctx.prec), open(args.out, 'w'), indent=1)

if __name__ == "__main__":
    main()
