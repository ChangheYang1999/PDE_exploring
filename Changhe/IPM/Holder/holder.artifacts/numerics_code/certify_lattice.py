"""Certified enclosure of the axis-direction lattice D witness (lead Notes 12-13, the verification work V072); adapted from certify_lb.py v2.

Witness. beta = 0: K0(w) = (w1^2 - w2^2)/(2 pi |w|^4) = Re(1/(2 pi conj(w)^2)), k0(z) = K0(z - e1) - K0(z) (cancellation-free closed form).
Z0(b) = zcurve.Z0Geom(b) (midline, X segments, +-45 deg segments of length b sqrt2 bending to +-30/150 deg); g0 = 2^(alpha-1) sigma0 D^alpha.
H = {z1 > 1/2}, h = (1/2)(2(z1 - 1/2))^alpha, F = g0 - t (t >= 1/2), f = max(-h, min(h, F)) on H, f(Mz) = -f(z), M(z) = (1 - z1, z2), f = 0 on
the midline.  Lemma: [f]_alpha <= 1, f(e1) = -1/2, f(0) = +1/2, D_alpha >= |int k0 f dz| + 1/2.
Symmetry: k0(Mz) = -k0(z), f(Mz) = -f(z) => g = k0 f is M-even: int_{B(0,1/2)} g = int_{B(e1,1/2)} g.  I0 = 2 int_{B(e1,1/2)} g + int_{rest} g.
Near field about e1: own kernel K0(z - e1) integrated against f - f(e1) (the constant integrates to 0 over full annuli and is kept out of
the error bounds), cross kernel -K0(z) against f.  Cell rule (centroid c, rQ, |Q|, M2 as in certify_lb): first order always valid
(|f(z) - f(c)| <= rQ^alpha since [f] <= 1; |f(z) - f(e1)| <= (rho_2)^alpha), second order when one smooth branch is certified on B(c, rQ):
 unclamped f = g0 - t (sigma decided, unique nearest point, g0(c) - t +- L rQ strictly inside (-h(c) + L_h rQ, h(c) - L_h rQ)):
    F0 = |f(c)| + L rQ (or |f(c) - f(e1)| + L rQ for the own part), F1 = L = C alpha Dmin^(alpha-1), F2 = C alpha Dmin^(alpha-2);
 clamped f = +-h (g0(c) - t -+ L rQ beyond +-(h(c) + L_h rQ)): F1 = L_h = C alpha Xmin^(alpha-1), F2 = C alpha (1-alpha) Xmin^(alpha-2),
    with X = z1 - 1/2 >= Xmin = c1 - 1/2 - rQ > 0 on the ball, C = 2^(alpha-1).
 Cells with c1 - 1/2 <= rQ (midline) or undecided: first order; refined up to maxdepth.
Kernel bounds: the derivative moduli of K0 equal those of K_xy (same |h^(j)|), so certify_lb.kernel_bounds applies verbatim.
Tails: inner ball B(e1, rho_min): |K0(z-e1)| |f - f(e1)| <= rho^(alpha-2)/(2 pi) => <= rho_min^alpha/alpha; cross part as in certify_lb;
sliver and far tail as in certify_lb (|f| <= h <= (1/2)(2|z - m|)^alpha still holds since |z1 - 1/2| <= |z - m|).
Repairs after the external-review audit of certify_note14.py (2026-10-28 ~06:55Z; items 5, 8, 11 apply here too): interval-safe sigma (zcurve), conservative
extremum test in m_cell, NaN-safe partial-cell power, finiteness checks. The runs lat_a34_b34 and lat_a910_b720 were made with the previous code; see
NUM_REPORT sec. 7 for why those defects could not have affected their enclosures.
"""
import sys, json, time, math, argparse
from flint import arb, ctx, fmpq
import multiprocessing as mp
import zcurve
import certify_lb as CL
ctx.prec = 80

G = None; ALPHA = None; TT = None; PI = None; C = None; BQ = None
ERR = {}

def setup(alpha_q, b_q, t_q):
    global G, ALPHA, TT, PI, C, BQ
    PI = arb.pi(); ALPHA = arb(fmpq(alpha_q)); TT = arb(fmpq(t_q)); C = arb(2)**(ALPHA - 1); BQ = fmpq(b_q)
    G = zcurve.Z0Geom(BQ)
    CL.setup(alpha_q, '1/2', 'poly')   # for cell_geom_ang / lower_dist / kernel_bounds (they use CL.PI only)

def K0(px, py):
    r2 = px*px + py*py
    return (px*px - py*py)/(2*PI*r2*r2)

def k0(px, py):
    A = px*px + py*py; B = (px - 1)*(px - 1) + py*py; u = 1 - 2*px
    return u*(A*(3*py*py - px*px) - u*(px*px - py*py))/(2*PI*A*A*B*B)

def pm():
    return arb(0).union(arb(1)).union(arb(-1))

def h_of(qx):
    return arb(1)/2*(2*(qx - arb(1)/2))**ALPHA

def witness(cx, cy, rQ):
    """returns dict: f (arb), branch in {'un','hi','lo','mix','mid'}, and bounds for the certified branch:
    L (Lipschitz const of f on the ball), F2 (Hessian bound), decided sigma flag. Uses the M-symmetry to map to H."""
    half = arb(1)/2
    if not (cx - half > rQ) and not (half - cx > rQ):
        # ball meets the midline: f is odd across it and |f| <= h; first order only
        fb = half*CL.pow_nonneg(2*(abs(cx - half) + rQ), ALPHA)*pm()   # |f| <= h on the ball (NaN-safe)
        return dict(f=fb, branch='mid')
    s = arb(1) if cx > half else arb(-1)
    qx = cx if cx > half else 1 - cx; qy = cy
    D = arb.max(G.dist(qx, qy), arb(0)); sg = G.sigma(qx, qy)
    Da = CL.pow_nonneg(D, ALPHA)
    h = h_of(qx); Xmin = qx - half - rQ
    Lh = C*ALPHA*Xmin**(ALPHA - 1)
    if sg is None:
        g = C*Da*pm(); F = g - TT
        f = arb.max(-h, arb.min(h, F))
        return dict(f=s*f, branch='mix')
    g = C*sg*Da; F = g - TT
    f = arb.max(-h, arb.min(h, F))
    out = dict(f=s*f, branch='mix')
    if D > rQ and G.unique_nearest(qx, qy, rQ, D):
        Dmin = D - rQ
        L = C*ALPHA*Dmin**(ALPHA - 1)
        if (F + L*rQ < h - Lh*rQ) and (F - L*rQ > -h + Lh*rQ):
            out.update(branch='un', L=L, F2=C*ALPHA*Dmin**(ALPHA - 2))
        elif F - L*rQ > h + Lh*rQ:
            out.update(branch='hi', L=Lh, F2=C*ALPHA*(1 - ALPHA)*Xmin**(ALPHA - 2))
        elif F + L*rQ < -h - Lh*rQ:
            out.update(branch='lo', L=Lh, F2=C*ALPHA*(1 - ALPHA)*Xmin**(ALPHA - 2))
    else:
        # sigma decided but nearest point not certified unique: the clamped branches may still be certified (they do not involve g0)
        if D > rQ:
            Dmin = D - rQ; L = C*ALPHA*Dmin**(ALPHA - 1)
            if F - L*rQ > h + Lh*rQ:
                out.update(branch='hi', L=Lh, F2=C*ALPHA*(1 - ALPHA)*Xmin**(ALPHA - 2))
            elif F + L*rQ < -h - Lh*rQ:
                out.update(branch='lo', L=Lh, F2=C*ALPHA*(1 - ALPHA)*Xmin**(ALPHA - 2))
    return out

FPOLE = -arb(1)/2   # f(e1)

def cell_value(cx, cy, rQ, area, M2, d1, d0, region):
    """enclosure of int_Q g over a full cell. region 'near': own kernel K0(z-e1) against f - f(e1) plus cross kernel -K0(z) against f;
    region 'm': k0 against f.  Returns (value ball, category, error)."""
    w = witness(cx, cy, rQ)
    fc = w['f']
    if region == 'near':
        own = K0(cx - 1, cy); cross = -K0(cx, cy)
        kb_own, kb1_own, kb2_own = 1/(2*PI*d1*d1), 1/(PI*d1**3), 3/(PI*d1**4)
        kb_cr, kb1_cr, kb2_cr = 1/(2*PI*d0*d0), 1/(PI*d0**3), 3/(PI*d0**4)
        val = own*(fc - FPOLE) + cross*fc
        # first order
        Df = rQ**ALPHA
        err = (kb_own*Df + abs(fc - FPOLE)*kb1_own*rQ + kb_cr*Df + abs(fc)*kb1_cr*rQ)*area
        cat = 'o1_' + w['branch']
        if w['branch'] in ('un', 'hi', 'lo'):
            L, F2 = w['L'], w['F2']
            F0o = abs(fc - FPOLE) + L*rQ; F0c = abs(fc) + L*rQ
            Ho = F0o*kb2_own + 2*kb1_own*L + kb_own*F2
            Hc = F0c*kb2_cr + 2*kb1_cr*L + kb_cr*F2
            e2 = (Ho + Hc)*M2/2
            if e2 < err:
                err = e2; cat = 'o2'
        return area*val + err*pm(), cat, err
    else:
        kb, kb1, kb2 = CL.kernel_bounds(cx, cy, rQ, d1, d0)
        val = k0(cx, cy)*fc
        Df = rQ**ALPHA
        err = (kb*Df + abs(fc)*kb1*rQ)*area
        cat = 'o1_' + w['branch']
        if w['branch'] in ('un', 'hi', 'lo'):
            L, F2 = w['L'], w['F2']
            H = (abs(fc) + L*rQ)*kb2 + 2*kb1*L + kb*F2
            e2 = H*M2/2
            if e2 < err:
                err = e2; cat = 'o2'
        return area*val + err*pm(), cat, err

def polar_value(center, r1, r2, th1, th2, depth, maxdepth, region):
    cx, cy, rQ, area, _, _, M2 = CL.cell_geom_ang(center, r1, r2, th1, th2)
    if region == 'near':
        h = (th2 - th1)/2
        d1 = arb((r1*h.cos()).lower()); d0 = CL.lower_dist(cx, cy, rQ, arb(0), arb(0))
    else:
        d1 = CL.lower_dist(cx, cy, rQ, arb(1), arb(0)); d0 = CL.lower_dist(cx, cy, rQ, arb(0), arb(0))
    if d1 is None or d0 is None or not (d1 > 0 and d0 > 0):
        raise ValueError("pole inside a full cell")
    val, cat, err = cell_value(cx, cy, rQ, area, M2, d1, d0, region)
    if cat != 'o2' and depth < maxdepth:
        rm = (r1 + r2)/2; tm = (th1 + th2)/2
        tot = arb(0); n = 0
        for (a1, a2) in ((r1, rm), (rm, r2)):
            for (b1, b2) in ((th1, tm), (tm, th2)):
                v, m = polar_value(center, a1, a2, b1, b2, depth + 1, maxdepth, region)
                tot += v; n += m
        return tot, n
    if not (val.is_finite() and err.is_finite()):
        raise ValueError("nonfinite cell")
    ERR[cat] = ERR.get(cat, arb(0)) + err
    return val, 1

def m_cell(center, r1, r2, th1, th2, depth, maxdepth):
    c1 = th1.cos(); c2 = th2.cos()
    amax = arb.max(abs(c1), abs(c2)); amin = arb.min(abs(c1), abs(c2))
    for q in (arb(0), PI, 2*PI):
        if not (q < th1 or q > th2): amax = arb(1)      # extremum applied unless certified outside (external-review audit of certify_note14, item 8)
    for q in (PI/2, 3*PI/2):
        if not (q < th1 or q > th2): amin = arb(0)
    if r2 <= amin:
        return arb(0), 0
    cx, cy, rQ, area, _, _, M2 = CL.cell_geom_ang(center, r1, r2, th1, th2)
    d1 = CL.lower_dist(cx, cy, rQ, arb(1), arb(0)); d0 = CL.lower_dist(cx, cy, rQ, arb(0), arb(0))
    if r1 >= amax and d1 is not None and d0 is not None:
        return polar_value(center, r1, r2, th1, th2, depth, maxdepth, 'm')
    if depth < maxdepth:
        rm = (r1 + r2)/2; tm = (th1 + th2)/2
        tot = arb(0); n = 0
        for (a1, a2) in ((r1, rm), (rm, r2)):
            for (b1, b2) in ((th1, tm), (tm, th2)):
                v, m = m_cell(center, a1, a2, b1, b2, depth + 1, maxdepth)
                tot += v; n += m
        return tot, n
    if d1 is None: d1 = arb(1)/2
    if d0 is None: d0 = arb(1)/2
    kb, _, _ = CL.kernel_bounds(cx, cy, rQ, d1, d0)
    # |f| <= h <= (1/2)(2 (|c1 - 1/2| + rQ))^alpha
    fb = arb(1)/2*CL.pow_nonneg(2*(abs(cx - arb(1)/2) + rQ), ALPHA)     # NaN-safe (external-review item 11)
    e = area*kb*fb
    if not e.is_finite():
        raise ValueError("nonfinite partial cell")
    ERR['partial'] = ERR.get('partial', arb(0)) + e
    return e*pm(), 1

def worker(arg):
    idx, task = arg
    setup(task['alpha_q'], task['b_q'], task['t_q'])
    ERR.clear()
    edges = [arb(s) for s in task['rho_edges']]; ntheta = task['ntheta']; md = task['maxdepth']
    total = arb(0); n = 0
    if task['kind'] == 'near_e1':
        center = (arb(1), arb(0))
        for j in range(len(edges) - 1):
            for l in range(ntheta):
                th1 = 2*PI*l/ntheta; th2 = 2*PI*(l + 1)/ntheta
                v, m = polar_value(center, edges[j], edges[j+1], th1, th2, 0, md, 'near'); total += v; n += m
    else:
        center = (arb(1)/2, arb(0))
        for j in range(len(edges) - 1):
            for l in range(ntheta):
                th1 = 2*PI*l/ntheta; th2 = 2*PI*(l + 1)/ntheta
                v, m = m_cell(center, edges[j], edges[j+1], th1, th2, 0, md); total += v; n += m
    return idx, (total.mid().str(30), total.rad().str(10), n, {k: v.str(10, radius=True) for k, v in ERR.items()})

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--alpha', required=True); ap.add_argument('--b', default='3/4'); ap.add_argument('--t', default='1/2')
    ap.add_argument('--delta', type=float, default=0.02); ap.add_argument('--delta_far0', type=float, default=0.02)
    ap.add_argument('--rho_min', type=float, default=1e-6); ap.add_argument('--rho_m', type=float, default=0.01)
    ap.add_argument('--rho_max', type=float, default=1e8); ap.add_argument('--nproc', type=int, default=6)
    ap.add_argument('--maxdepth', type=int, default=3); ap.add_argument('--out', default=None)
    a = ap.parse_args()
    setup(a.alpha, a.b, a.t); alpha = float(fmpq(a.alpha))
    t0 = time.time(); tasks = []
    def chunk(edges, kind, ntheta):
        step = max(1, 4000 // ntheta)
        for i in range(0, len(edges) - 1, step):
            tasks.append(dict(kind=kind, rho_edges=edges[i:i + step + 1], ntheta=ntheta, alpha_q=a.alpha, b_q=a.b, t_q=a.t, maxdepth=a.maxdepth))
    nth = int(math.ceil(2*math.pi/a.delta)); nth += nth % 2
    chunk(CL.geometric_edges(a.rho_min, 0.5, a.delta), 'near_e1', nth)
    nthm = int(math.ceil(2*math.pi/a.delta_far0)); nthm += nthm % 2
    chunk(CL.geometric_edges(a.rho_m, 1.0, a.delta_far0), 'm_system', nthm)
    rlo = 1.0
    while rlo < a.rho_max:
        rhi = min(rlo*10, a.rho_max); dk = min(0.2, a.delta_far0*rlo**((1 - alpha)/4))
        nt = int(math.ceil(2*math.pi/dk)); nt += nt % 2
        chunk(CL.geometric_edges(rlo, rhi, dk), 'm_system', nt); rlo = rhi
    print(f"tasks: {len(tasks)} (alpha={alpha}, b={a.b}, t={a.t})", flush=True)
    results = [None]*len(tasks)
    with mp.Pool(a.nproc) as pool:
        done = 0
        for idx, res in pool.imap_unordered(worker, list(enumerate(tasks)), chunksize=1):
            results[idx] = res; done += 1
            if done % max(1, len(tasks)//20) == 0 or done == len(tasks):
                print(f"  progress {done}/{len(tasks)} tasks, {time.time()-t0:.0f}s", flush=True)
    near = arb(0); rest = arb(0); ncells = 0; errsum = {}
    for (mid, rad, n, errs), tk in zip(results, tasks):
        v = arb(mid) + arb(0, rad); ncells += n
        if tk['kind'] == 'near_e1': near += v
        else: rest += v
        for k, e in errs.items(): errsum[k] = errsum.get(k, arb(0)) + arb(e)
    print("error by category: " + ", ".join(f"{k}: {float(v.mid()):.3e}" for k, v in sorted(errsum.items())))
    rm = arb(repr(a.rho_min))
    inner = (rm**ALPHA/ALPHA + PI*rm*rm/(2*PI*(1 - rm)**2)*(arb(1)/2 + rm**ALPHA))*pm()   # own: int |K0||f-f(e1)| <= rho^alpha/alpha; cross: |K0(z)| <= 1/(2pi(1-rho)^2), |f| <= 1/2 + rho^alpha
    rmm = arb(repr(a.rho_m)); C2 = arb(2)**(ALPHA - 1)
    sliver = 16*C2*rmm**(ALPHA + 3)/(PI*(ALPHA + 3)*(1 - rmm*rmm).sqrt())*pm()
    R = arb(repr(a.rho_max))
    tail = arb(2)**ALPHA*(R/(R - arb(1)/2))**3*R**(ALPHA - 1)/(1 - ALPHA)*pm()
    I0 = 2*(near + inner) + rest + sliver + tail
    if not (I0.is_finite() and near.is_finite() and rest.is_finite()):
        raise ValueError("nonfinite final enclosure")
    el = time.time() - t0
    print(f"cells {ncells} time {el:.0f}s")
    print(f"near (B(e1,1/2), own against f - f(e1), cross against f) = {near.str(10, radius=True)}; rest = {rest.str(10, radius=True)}; inner {inner.str(4, radius=True)} sliver {sliver.str(4, radius=True)} tail {tail.str(4, radius=True)}")
    print(f"I0 = int k0 f = {I0.str(12, radius=True)}   =>   D_alpha >= |I0| + 1/2 >= {(abs(I0).lower() + arb(1)/2).str(12)}")
    if a.out:
        json.dump(dict(alpha=a.alpha, b=a.b, t=a.t, params=vars(a), cells=ncells, time_s=el, near=near.str(20, radius=True), rest=rest.str(20, radius=True),
                       I0=I0.str(20, radius=True), I0_lower=I0.lower().str(20), I0_upper=I0.upper().str(20), D_lower=(abs(I0).lower() + arb(1)/2).str(20)), open(a.out, 'w'), indent=1)

if __name__ == "__main__":
    main()
