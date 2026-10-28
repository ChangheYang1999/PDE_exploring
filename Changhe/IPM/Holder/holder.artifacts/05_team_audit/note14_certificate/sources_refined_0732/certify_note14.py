"""Certified enclosure of the lead's Note 14 axis-direction D witness (lattice lemma, Note 12 / the verification work V072); extends certify_lattice.py.

Witness (H = {z1 > 1/2}, poles e1 = (1,0) with f = -1/2 and 0 with f = +1/2, midline reflection M(z) = (1 - z1, z2)):
   g0 = 2^(alpha-1) sigma0 dist(z, Z0(b))^alpha    (axis polygon C witness, zcurve.Z0Geom, own component signs)
   P(w) = (1/2)|w|^alpha (1 + sgn(cos 2 theta)|cos 2 theta|^alpha),  w = z - e1 = |w| e^{i theta}   (rotated projection cusp)
   F = min(g0 + c, -1/2 + lam P),   f = max(-h, min(h, F)) on H,  h = (1/2)(2(z1 - 1/2))^alpha,   f(Mz) = -f(z),  f = 0 on the midline.
Admissibility (not checked here): [g0]_H <= 1 (polygon witness), [lam P] <= 1 i.e. lam <= 1/[P]_alpha (certified by the verification work: V064 gives
[P]_(1/2) <= 1021/1000, V082 gives [P]_(3/4) <= 53/50), c real; then [F]_H <= 1 and F(e1) = min(c, -1/2) <= -1/2 for c <= 0 (c > 0 also
gives F(e1) = -1/2); the lemma yields [f] <= 1, f(e1) = -1/2, f(0) = 1/2 and D_alpha >= |int k0 f dz| + 1/2.
The first-order cell rule uses only [f] <= 1 (and, for the fallback variation bound of the P branch, [lam P] <= 1).
Cell rule (centroid c, rQ, |Q|, M2 as in certify_lb): first order always valid; second order when one smooth branch is certified on
B(c, rQ):  branches 'un' (f = g0 + c; needs sigma decided, unique nearest piece, D > rQ), 'P' (f = -1/2 + lam P; needs |w_c| > rQ and
sgn(cos 2 theta) constant on the ball; gradient/Hessian bounds from the polar homogeneity formulas evaluated on the (r, theta) ranges of
the ball in ball arithmetic), 'hi'/'lo' (f = +-h). Branch separation uses variation bounds: Lipschitz*rQ on a smooth branch, else rQ^alpha.
Kernel bounds, tails, symmetry and the near-field treatment (own kernel against f - f(e1)) are those of certify_lattice.py.
Definition of I0: the integral int k0 f is NOT absolutely convergent at the poles (the constant f(pole) against K0(z - pole) diverges
logarithmically in absolute value); I0 is the principal value with centred disks deleted at both poles, which equals the implemented
decomposition (own kernel against f - f(pole) over full annuli, where the constant integrates to zero) and is the quantity in the lattice
lemma (the verification work V072/V076). Output: I0 enclosure and D_lower = |I0|.lower() + 1/2. Audit: external-review 2026-10-28 (an external review note; items 5, 8, 11 repaired here), the verification work V094 (method).
"""
import sys, json, time, math, argparse
from flint import arb, ctx, fmpq
import multiprocessing as mp
import zcurve
import certify_lb as CL
ctx.prec = 80

G = None; ALPHA = None; CC = None; LAM = None; PI = None; C = None; BQ = None
ERR = {}

def setup(alpha_q, b_q, c_q, lam_q):
    global G, ALPHA, CC, LAM, PI, C, BQ
    PI = arb.pi(); ALPHA = arb(fmpq(alpha_q)); CC = arb(fmpq(c_q)); LAM = arb(fmpq(lam_q)); C = arb(2)**(ALPHA - 1); BQ = fmpq(b_q)
    G = zcurve.Z0Geom(BQ)
    CL.setup(alpha_q, '1/2', 'poly')

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

def P_val(wx, wy):
    """enclosure of P(w) (ball inputs allowed)"""
    r2 = wx*wx + wy*wy
    r = zcurve.sqrt_nonneg(r2)
    ra = CL.pow_nonneg(r, ALPHA)
    if not (r2 > 0):
        return ra*arb(0).union(arb(1))          # 0 <= P <= |w|^alpha
    c2 = (wx*wx - wy*wy)/r2
    if c2 > 0:
        q = c2**ALPHA
    elif c2 < 0:
        q = -((-c2)**ALPHA)
    else:
        q = pm()*CL.pow_nonneg(abs(c2), ALPHA)
    return ra*(1 + q)/2

def P_bounds(wx, wy, rQ):
    """(L, F2): upper bounds of |grad P| and |Hess P| (Frobenius) on B(w, rQ), or None if the ball may meet the origin or a diagonal.
    P = r^alpha Phi(theta), Phi = (1 + q_s)/2, q_s = s (s cos 2theta)^alpha with s = sgn(cos 2theta) constant on the ball.
    |grad P|^2 = r^(2alpha-2) (alpha^2 Phi^2 + Phi'^2);  |Hess P|_F^2 = r^(2alpha-4) [alpha^2 (alpha-1)^2 Phi^2 + 2 (alpha-1)^2 Phi'^2 + (alpha Phi + Phi'')^2]."""
    rho = zcurve.sqrt_nonneg(wx*wx + wy*wy)
    if not (rho > rQ):
        return None
    R = (rho - rQ).union(rho + rQ)
    dth = (rQ/rho).asin()
    th = arb.atan2(wy, wx); th2 = arb.atan2(-wy, -wx)      # two representations (cuts on the negative / positive axis); 2theta is what matters
    if th2.rad() < th.rad(): th = th2
    TH = (th - dth).union(th + dth)
    c2 = (2*TH).cos()
    if c2 > 0: s = arb(1)
    elif c2 < 0: s = arb(-1)
    else: return None
    Cq = s*c2
    if not (Cq > 0):
        return None
    S2 = (2*TH).sin()
    # signed profile q_s = s Cq^alpha (= sgn(cos 2theta)|cos 2theta|^alpha), derivatives in theta (Cq' = -2 s sin 2theta, Cq'' = -4 Cq)
    q = s*Cq**ALPHA; qp = -2*ALPHA*S2*Cq**(ALPHA - 1); qpp = s*(4*ALPHA*(ALPHA - 1)*S2*S2*Cq**(ALPHA - 2) - 4*ALPHA*Cq**ALPHA)
    Phi = (1 + q)/2; Php = qp/2; Phpp = qpp/2
    a1 = ALPHA*(ALPHA - 1)*Phi; a3 = ALPHA*Phi + Phpp; am1 = ALPHA - 1
    grad = R**(ALPHA - 1)*zcurve.sqrt_nonneg(ALPHA*ALPHA*Phi*Phi + Php*Php)
    hess = R**(ALPHA - 2)*zcurve.sqrt_nonneg(a1*a1 + 2*am1*am1*Php*Php + a3*a3)
    if not (grad.is_finite() and hess.is_finite()):
        return None
    return arb(grad.upper()), arb(hess.upper())

def witness(cx, cy, rQ):
    """returns dict: f (arb enclosure of f(c)), branch in {'un','P','hi','lo','mix','mid'}, and L, F2 for a certified smooth branch."""
    half = arb(1)/2
    if not (cx - half > rQ) and not (half - cx > rQ):
        fb = half*CL.pow_nonneg(2*(abs(cx - half) + rQ), ALPHA)*pm()   # |f| <= h on the ball; f odd across the midline
        return dict(f=fb, branch='mid')
    s = arb(1) if cx > half else arb(-1)
    qx = cx if cx > half else 1 - cx; qy = cy
    # g branch
    D = arb.max(G.dist(qx, qy), arb(0)); sg = G.sigma(qx, qy)
    Da = CL.pow_nonneg(D, ALPHA)
    g = C*(sg if sg is not None else pm())*Da
    Fg = g + CC
    smooth_g = False; gvar = rQ**ALPHA
    if sg is not None and D > rQ and G.unique_nearest(qx, qy, rQ, D):
        Dmin = D - rQ; Lg = C*ALPHA*Dmin**(ALPHA - 1); F2g = C*ALPHA*Dmin**(ALPHA - 2)
        smooth_g = True; gvar = Lg*rQ
    # P branch
    wx = qx - 1; wy = qy
    FP = -half + LAM*P_val(wx, wy)
    smooth_P = False; Pvar = rQ**ALPHA
    pb = P_bounds(wx, wy, rQ)
    if pb is not None:
        LP, F2P = LAM*pb[0], LAM*pb[1]
        smooth_P = True; Pvar = LP*rQ
    # clamp band
    h = h_of(qx); Xmin = qx - half - rQ
    Lh = C*ALPHA*Xmin**(ALPHA - 1); F2h = C*ALPHA*(1 - ALPHA)*Xmin**(ALPHA - 2)
    F = arb.min(Fg, FP)
    f = arb.max(-h, arb.min(h, F))
    out = dict(f=s*f, branch='mix')
    if smooth_g and smooth_P:
        # all branches (g0 + c, -1/2 + lam P, +-h) are Lipschitz on the convex ball; min/max preserve the Lipschitz constant
        out['Lmix'] = arb.max(arb.max(Lg, LP), Lh)
    hi_thr = h + Lh*rQ; lo_thr = -h - Lh*rQ
    if (Fg - gvar > hi_thr) and (FP - Pvar > hi_thr):
        out.update(branch='hi', L=Lh, F2=F2h)
    elif (Fg + gvar < lo_thr) or (FP + Pvar < lo_thr):
        out.update(branch='lo', L=Lh, F2=F2h)
    elif smooth_g and (Fg + gvar < FP - Pvar) and (Fg + gvar < h - Lh*rQ) and (Fg - gvar > -h + Lh*rQ):
        out.update(branch='un', L=Lg, F2=F2g)
    elif smooth_P and (FP + Pvar < Fg - gvar) and (FP + Pvar < h - Lh*rQ) and (FP - Pvar > -h + Lh*rQ):
        out.update(branch='P', L=LP, F2=F2P)
    return out

FPOLE = -arb(1)/2   # f(e1)
PARTIAL_EXTRA_DEPTH = 2   # partial cells (meeting a pole-disk boundary) are refined 2 levels deeper than full cells

def cell_value(cx, cy, rQ, area, M2, d1, d0, region):
    w = witness(cx, cy, rQ)
    fc = w['f']
    if region == 'near':
        own = K0(cx - 1, cy); cross = -K0(cx, cy)
        kb_own, kb1_own, kb2_own = 1/(2*PI*d1*d1), 1/(PI*d1**3), 3/(PI*d1**4)
        kb_cr, kb1_cr, kb2_cr = 1/(2*PI*d0*d0), 1/(PI*d0**3), 3/(PI*d0**4)
        val = own*(fc - FPOLE) + cross*fc
        Df = rQ**ALPHA
        if 'Lmix' in w: Df = arb.min(Df, w['Lmix']*rQ)
        err = (kb_own*Df + abs(fc - FPOLE)*kb1_own*rQ + kb_cr*Df + abs(fc)*kb1_cr*rQ)*area
        cat = 'o1_' + w['branch']
        if w['branch'] in ('un', 'P', 'hi', 'lo'):
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
        if 'Lmix' in w: Df = arb.min(Df, w['Lmix']*rQ)
        err = (kb*Df + abs(fc)*kb1*rQ)*area
        cat = 'o1_' + w['branch']
        if w['branch'] in ('un', 'P', 'hi', 'lo'):
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
        if not (q < th1 or q > th2): amax = arb(1)      # extremum applied unless certified outside the angular range
    for q in (PI/2, 3*PI/2):
        if not (q < th1 or q > th2): amin = arb(0)
    if r2 <= amin:
        return arb(0), 0
    cx, cy, rQ, area, _, _, M2 = CL.cell_geom_ang(center, r1, r2, th1, th2)
    d1 = CL.lower_dist(cx, cy, rQ, arb(1), arb(0)); d0 = CL.lower_dist(cx, cy, rQ, arb(0), arb(0))
    if r1 >= amax and d1 is not None and d0 is not None:
        return polar_value(center, r1, r2, th1, th2, depth, maxdepth, 'm')
    if depth < maxdepth + PARTIAL_EXTRA_DEPTH:
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
    fb = arb(1)/2*CL.pow_nonneg(2*(abs(cx - arb(1)/2) + rQ), ALPHA)     # |f| <= h  (NaN-safe power of a nonnegative base)
    e = area*kb*fb
    if not e.is_finite():
        raise ValueError("nonfinite partial cell")
    ERR['partial'] = ERR.get('partial', arb(0)) + e
    return e*pm(), 1

def worker(arg):
    idx, task = arg
    setup(task['alpha_q'], task['b_q'], task['c_q'], task['lam_q'])
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
    if not total.is_finite():
        raise ValueError("nonfinite task total")
    return idx, (total.mid().str(30), total.rad().str(10), n, {k: v.str(10, radius=True) for k, v in ERR.items()})

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--alpha', required=True); ap.add_argument('--b', default='3/4'); ap.add_argument('--c', default='-3/20'); ap.add_argument('--lam', required=True)
    ap.add_argument('--delta', type=float, default=0.02); ap.add_argument('--delta_far0', type=float, default=0.02)
    ap.add_argument('--rho_min', type=float, default=1e-6); ap.add_argument('--rho_m', type=float, default=0.01)
    ap.add_argument('--rho_max', type=float, default=1e8); ap.add_argument('--nproc', type=int, default=3)
    ap.add_argument('--maxdepth', type=int, default=3); ap.add_argument('--out', default=None)
    a = ap.parse_args()
    setup(a.alpha, a.b, a.c, a.lam); alpha = float(fmpq(a.alpha))
    t0 = time.time(); tasks = []
    def chunk(edges, kind, ntheta):
        step = max(1, 4000 // ntheta)
        for i in range(0, len(edges) - 1, step):
            tasks.append(dict(kind=kind, rho_edges=edges[i:i + step + 1], ntheta=ntheta, alpha_q=a.alpha, b_q=a.b, c_q=a.c, lam_q=a.lam, maxdepth=a.maxdepth))
    nth = int(math.ceil(2*math.pi/a.delta)); nth += nth % 2
    chunk(CL.geometric_edges(a.rho_min, 0.5, a.delta), 'near_e1', nth)
    nthm = int(math.ceil(2*math.pi/a.delta_far0)); nthm += nthm % 2
    chunk(CL.geometric_edges(a.rho_m, 1.0, a.delta_far0), 'm_system', nthm)
    rlo = 1.0
    while rlo < a.rho_max:
        rhi = min(rlo*10, a.rho_max); dk = min(0.2, a.delta_far0*rlo**((1 - alpha)/4))
        nt = int(math.ceil(2*math.pi/dk)); nt += nt % 2
        chunk(CL.geometric_edges(rlo, rhi, dk), 'm_system', nt); rlo = rhi
    print(f"tasks: {len(tasks)} (alpha={alpha}, b={a.b}, c={a.c}, lam={a.lam})", flush=True)
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
    inner = (rm**ALPHA/ALPHA + PI*rm*rm/(2*PI*(1 - rm)**2)*(arb(1)/2 + rm**ALPHA))*pm()
    rmm = arb(repr(a.rho_m)); C2 = arb(2)**(ALPHA - 1)
    sliver = 16*C2*rmm**(ALPHA + 3)/(PI*(ALPHA + 3)*(1 - rmm*rmm).sqrt())*pm()
    R = arb(repr(a.rho_max))
    tail = arb(2)**ALPHA*(R/(R - arb(1)/2))**3*R**(ALPHA - 1)/(1 - ALPHA)*pm()
    I0 = 2*(near + inner) + rest + sliver + tail
    if not (I0.is_finite() and near.is_finite() and rest.is_finite() and inner.is_finite() and sliver.is_finite() and tail.is_finite()):
        raise ValueError("nonfinite final enclosure")
    el = time.time() - t0
    print(f"cells {ncells} time {el:.0f}s")
    print(f"near (B(e1,1/2), own against f - f(e1), cross against f) = {near.str(10, radius=True)}; rest = {rest.str(10, radius=True)}; inner {inner.str(4, radius=True)} sliver {sliver.str(4, radius=True)} tail {tail.str(4, radius=True)}")
    print(f"exact radii: near {near.rad().str(5)}, rest {rest.rad().str(5)}, I0 {I0.rad().str(5)} (the bracket displays above round the midpoint and inflate the shown radius)")
    print(f"I0 = int k0 f = {I0.str(12, radius=True)} = [{I0.lower().str(12)}, {I0.upper().str(12)}]   =>   D_alpha >= |I0| + 1/2 >= {(abs(I0).lower() + arb(1)/2).str(12)}")
    if a.out:
        import hashlib, os
        here = os.path.dirname(os.path.abspath(__file__))
        hashes = {fn: hashlib.sha256(open(os.path.join(here, fn), 'rb').read()).hexdigest() for fn in ('certify_note14.py', 'certify_lb.py', 'zcurve.py')}
        json.dump(dict(alpha=a.alpha, b=a.b, c=a.c, lam=a.lam, params=vars(a), cells=ncells, time_s=el, near=near.str(20, radius=True), rest=rest.str(20, radius=True),
                       near_mid=near.mid().str(40), near_rad=near.rad().str(10), rest_mid=rest.mid().str(40), rest_rad=rest.rad().str(10),
                       inner=inner.str(20, radius=True), sliver=sliver.str(20, radius=True), tail=tail.str(20, radius=True),
                       I0=I0.str(20, radius=True), I0_lower=I0.lower().str(20), I0_upper=I0.upper().str(20), D_lower=(abs(I0).lower() + arb(1)/2).str(20),
                       errors={k: v.str(10, radius=True) for k, v in errsum.items()}, source_sha256=hashes, prec_bits=ctx.prec,
                       sidecar=a.out + '.tasks.json'), open(a.out, 'w'), indent=1)
        # sidecar (the verification work request 06:58Z): every task specification with the worker's full returned tuple (mid, rad strings, cell count, error categories)
        json.dump([dict(task=tk, mid=res[0], rad=res[1], cells=res[2], errors=res[3]) for tk, res in zip(tasks, results)], open(a.out + '.tasks.json', 'w'))

if __name__ == "__main__":
    main()
