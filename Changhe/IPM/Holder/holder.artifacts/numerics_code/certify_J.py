"""Certified enclosure of the lead's constant J(b) (the lead work NOTES Note 3, request N8):
   J(b) = int_{H minus B_{1/2}(x)} |nu_b| dw + int_{B_{1/2}(x)} (|nu_b| - |K_b(x-w)|) dw,
with x = e1/2, y = -e1/2, H = {w1 > 0}, K_b(z) = cos(2 arg z - 2b)/(2 pi |z|^2), nu_b(w) = K_b(x-w) - K_b(y-w).
In coordinates z = w + e1/2 (poles at 0 and e1): nu_b = k(z) := K_b(z - e1) - K_b(z), H = {z1 > 1/2}, ball = B(e1, 1/2).
Method: polar cells about e1; midpoint value plus Lipschitz deviation bound (|.| is 1-Lipschitz, so the deviation of
|k| is bounded by sup|grad k| * r_Q, using |grad K| = 1/(pi |w|^3) and the dipole bound 3/(pi (|z-m|-1/2)^4));
cells in B(e1, rho_1) bounded trivially by |K_b(z)| <= 1/(2 pi (1-rho)^2); half-plane clipping handled with
exact/partial cell logic in cos(theta); tail |z - e1| > rho_max bounded by the mean-value estimate.
Expected exact value (if lead's and verifier's decompositions are consistent): J(pi/4) = 1/2 + 2 log 2/pi = 0.94127...
"""
import sys, json, time, math, argparse
from flint import arb, ctx, fmpq
import multiprocessing as mp
ctx.prec = 80

def setup(b_q):
    global PI, B, SIN2B, COS2B
    PI = arb.pi(); B = PI*arb(b_q)   # b given as a rational multiple of pi
    SIN2B = (2*B).sin(); COS2B = (2*B).cos()

def Kb(zx, zy):
    # cos(2 th - 2b)/(2 pi r^2) = [cos 2th cos 2b + sin 2th sin 2b]/(2 pi r^2), cos 2th = (x^2-y^2)/r^2, sin 2th = 2xy/r^2
    r2 = zx*zx + zy*zy
    return ((zx*zx - zy*zy)*COS2B + 2*zx*zy*SIN2B)/(2*PI*r2*r2)

def k_tot(zx, zy):
    return Kb(zx - 1, zy) - Kb(zx, zy)

def lower_dist(cx, cy, rQ, qx, qy):
    d = ((cx - qx)**2 + (cy - qy)**2).sqrt() - rQ
    lo = d.lower()
    return arb(lo) if lo > 0 else None

def grad_bound(cx, cy, rQ, d1, d0):
    g = 1/(PI*d1**3) + 1/(PI*d0**3)
    dm = lower_dist(cx, cy, rQ, arb(1)/2, arb(0))
    if dm is not None and dm > arb(1)/2:
        e = dm - arb(1)/2
        g = arb.min(g, 3/(PI*e**4))
    return g

def cell_geom(rho1, rho2, l, ntheta):
    # polar cell about e1, angles measured from the positive x-axis, theta in [-pi, pi): l-th cell
    th1 = -PI + 2*PI*l/ntheta; th2 = -PI + 2*PI*(l + 1)/ntheta; thc = -PI + PI*(2*l + 1)/ntheta
    rhoc = (rho1 + rho2)/2
    cx = 1 + rhoc*thc.cos(); cy = rhoc*thc.sin()
    area = (rho2*rho2 - rho1*rho1)/2*(th2 - th1)
    rQ = arb(((rhoc*rhoc + rho2*rho2 - 2*rhoc*rho2*(PI/ntheta).cos()).sqrt()).upper())
    return cx, cy, rQ, area, th1, th2

def worker(task):
    setup(task['b_q'])
    edges = [arb(s) for s in task['rho_edges']]; ntheta = task['ntheta']; kind = task['kind']
    total = arb(0); n = 0
    pm = arb(0).union(arb(1)).union(arb(-1))
    for j in range(len(edges) - 1):
        r1, r2 = edges[j], edges[j+1]
        for l in range(ntheta):
            cx, cy, rQ, area, th1, th2 = cell_geom(r1, r2, l, ntheta)
            d1 = arb(r1.lower()); d0 = lower_dist(cx, cy, rQ, arb(0), arb(0))
            if kind == 'ball':
                # integrand |k| - |K_b(z - e1)|; deviation <= (sup|grad k| + sup|grad K(.-e1)|) rQ
                gb = grad_bound(cx, cy, rQ, d1, d0) + 1/(PI*d1**3)
                val = abs(k_tot(cx, cy)) - abs(Kb(cx - 1, cy))
                total += area*(val + gb*rQ*pm); n += 1
            else:
                # half plane z1 > 1/2  <=>  rho cos theta > -1/2. For rho >= 1/2: need cos theta > -1/(2 rho).
                c_lo = arb.min(th1.cos(), th2.cos())
                c_hi = arb.max(th1.cos(), th2.cos())
                if th1 <= 0 <= th2: c_hi = arb(1)
                # cos has its min at the endpoint farthest from 0 (|theta| largest) on [-pi, pi]: endpoints only, except if range contains +-pi (not possible except boundary)
                thr_lo = -1/(2*r2); thr_hi = -1/(2*r1)   # cos theta > -1/(2 rho) is easiest at rho = r2
                if c_lo >= thr_hi:      # whole cell inside H
                    gb = grad_bound(cx, cy, rQ, d1, d0)
                    total += area*(abs(k_tot(cx, cy)) + gb*rQ*pm); n += 1
                elif c_hi <= thr_lo:    # whole cell outside H
                    continue
                else:                   # partial: 0 <= contribution <= area * sup|k|
                    kb = 1/(2*PI*d1*d1) + 1/(2*PI*d0*d0)
                    dm = lower_dist(cx, cy, rQ, arb(1)/2, arb(0))
                    if dm is not None and dm > arb(1)/2:
                        kb = arb.min(kb, 1/(PI*(dm - arb(1)/2)**3))
                    total += area*kb*arb(0).union(arb(1)); n += 1
    return (total.str(40, radius=True), n)

def geometric_edges(r_lo, r_hi, delta):
    nseg = max(1, int(math.ceil(math.log(r_hi/r_lo)/math.log(1 + delta))))
    e = [r_lo*(r_hi/r_lo)**(i/nseg) for i in range(nseg + 1)]; e[0] = r_lo; e[-1] = r_hi
    return [repr(v) for v in e]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--b', type=str, default='1/4', help='b as rational multiple of pi')
    ap.add_argument('--delta_ball', type=float, default=0.01)
    ap.add_argument('--delta_out', type=float, default=0.005)
    ap.add_argument('--rho_1', type=float, default=0.01)
    ap.add_argument('--rho_max', type=float, default=1e6)
    ap.add_argument('--nproc', type=int, default=6)
    ap.add_argument('--out', type=str, default=None)
    a = ap.parse_args()
    b_q = fmpq(*[int(x) for x in a.b.split('/')]) if '/' in a.b else fmpq(int(a.b))
    setup(b_q)
    t0 = time.time(); tasks = []
    def chunk(edges, kind, ntheta):
        step = max(1, 4000 // ntheta)
        for i in range(0, len(edges) - 1, step):
            tasks.append(dict(kind=kind, rho_edges=edges[i:i + step + 1], ntheta=ntheta, b_q=str(b_q)))
    nth = int(math.ceil(2*math.pi/a.delta_ball)); nth += nth % 2
    chunk(geometric_edges(a.rho_1, 0.5, a.delta_ball), 'ball', nth)
    rlo = 0.5
    while rlo < a.rho_max:
        rhi = min(rlo*10, a.rho_max)
        dk = min(0.2, a.delta_out*math.sqrt(rlo/0.5))
        nth = int(math.ceil(2*math.pi/dk)); nth += nth % 2
        chunk(geometric_edges(rlo, rhi, dk), 'out', nth)
        rlo = rhi
    print(f"tasks {len(tasks)}", flush=True)
    with mp.Pool(a.nproc) as pool:
        res = pool.map(worker, tasks, chunksize=1)
    total = arb(0); n = 0
    for s, m in res:
        total += arb(s); n += m
    pm = arb(0).union(arb(1)).union(arb(-1))
    r1 = arb(repr(a.rho_1))
    inner = PI*r1*r1/(2*PI*(1 - r1)**2)*pm          # | |k| - |K(z-e1)| | <= |K_b(z)| <= 1/(2 pi (1-rho)^2) on B(e1, rho_1)
    R = arb(repr(a.rho_max))
    tail = (R/(R - 1))**3/R*arb(0).union(arb(1))     # int_{rho>R, half plane} |k| <= int pi rho /(pi (rho-1)^3) drho <= (R/(R-1))^3 / R
    J = total + inner + tail
    el = time.time() - t0
    print(f"cells {n} time {el:.0f}s   J({a.b} pi) = {J.str(15, radius=True)}   [inner {inner.str(3, radius=True)}, tail {tail.str(3, radius=True)}]")
    print(f"candidate exact 1/2 + 2 log2/pi = {(arb(1)/2 + 2*arb(2).log()/PI).str(20)}")
    if a.out:
        json.dump(dict(b=str(b_q), params=vars(a), cells=n, time_s=el, J=J.str(25, radius=True), J_lower=J.lower().str(20), J_upper=J.upper().str(20)), open(a.out, 'w'), indent=1)

if __name__ == "__main__":
    main()
