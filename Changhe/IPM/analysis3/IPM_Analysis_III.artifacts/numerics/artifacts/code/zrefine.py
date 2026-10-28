"""Hypothesis (Z), part (Zb) (lead note 14): refine the boxes near the source point P = (x_P, 0) until every leaf either has a certified
positive lower bound of |V|/r or lies inside the disc B_P = B_{rP}(P) (lead: rP = 99/2000, the V017/V024 source data give |V| >= 0.992 |X - P|
there). Leaves are sub-boxes [t1, t2] x [th1, th2] of the production boxes; bisection in theta or in t (whichever is longer in arc length),
depth <= DEPTH. Radial ranges of the background modes on a sub-interval: encl.range_finite of the shifted ExpPoly (mid cells: no near-resonance).
|V|/r >= sqrt(min|q|^2 + min|u|^2), q = c_l - sum Pe_n cos 2n theta, u = V_theta/r = sum Qe_n sin 2n theta (balls).
Usage: python3 zrefine.py <tag> [mode rect|disc] [xP] [rP] [vlo_thr]  (single process; uses runs/MARGIN/margin.npz to select the boxes with VLO < vlo_thr)
"""
import sys, os, json, math, time
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background
from encl import range_finite
from run_section import HERE
from outward import fup, flo

DEPTH = 9


def main(tag, mode="rect", xP=8.600064, rP=99 / 2000, thr=0.1, prec=160, hx=0.5, hy=0.5):
    """mode 'rect': the excluded set is the verifier's certified source rectangle Q = [xP - hx, xP + hx] x [-hy, hy] (V070: uniqueness of the zero
    in Q, ||D^2 V||_F < 1.159484, S(DV) > 0.1801 I); mode 'disc': the lead's disc B_P = B_rP(P) (Lemma Z, rP = 99/2000)."""
    ctx.prec = prec; t0 = time.time()
    T = ExactTrial(prec=prec); T.build_green(verbose=False)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    bg = Background(T, cells, nmax=None)
    c_l = 1 / T.k; Nf = T.Nf
    z = np.load(os.path.join(HERE, "runs", "MARGIN", "margin.npz")); VLO = z["VLO"]; th_edges = z["theta_edges"]; ntheta = len(th_edges) - 1
    targets = [(int(i), int(j)) for i, j in np.argwhere(np.isfinite(VLO) & (VLO < thr))]
    print("boxes with VLO < %.3f: %d (cells %d..%d)" % (thr, len(targets), min(i for i, _ in targets), max(i for i, _ in targets)), flush=True)
    th_q = [fmpq(i, 2 * ntheta) for i in range(ntheta + 1)]          # theta = pi * f, f exact rational
    PI = arb.pi()
    SHRINK = 1e-3                                                      # containment margin (absolute, in x and y): covers the center uncertainty of P

    def inside_Q(t1, t2, th1, th2):
        """the polar box lies inside the rectangle Q: x = r cos th in [xP - hx, xP + hx], |y| = r sin th <= hy (V071 test: r- cos th+ >= x-,
        r+ cos th- <= x+, r+ sin th+ <= hy), with an absolute margin SHRINK for the center uncertainty and float evaluation"""
        r1, r2 = math.exp(t1), math.exp(t2)
        xmin = r1 * math.cos(th2); xmax = r2 * math.cos(th1); ymax = r2 * math.sin(th2)
        return xmin >= xP - hx + SHRINK and xmax <= xP + hx - SHRINK and ymax <= hy - SHRINK

    def inside_BP(t1, t2, th1, th2):
        """the polar box lies inside the disc B_P iff its four corners do (the disc is convex and the box is... not convex in the plane: check the
        corners and the two arc midpoints of the outer arc as well, and require the box diagonal to be small; conservative: corners + outer arc samples)"""
        r1, r2 = math.exp(t1), math.exp(t2)
        pts = [(r1, th1), (r1, th2), (r2, th1), (r2, th2)] + [(r2, th1 + (th2 - th1) * s / 8) for s in range(1, 8)] + [(r1, th1 + (th2 - th1) * s / 8) for s in range(1, 8)]
        return all(math.hypot(r * math.cos(th) - xP, r * math.sin(th)) <= rP - SHRINK for r, th in pts)

    cache = {}
    def radial_ranges(ic, s1_q, s2_q):
        """balls of Pe_n, Qe_n on sigma in [s1, s2] (sub-interval of cell ic, exact rationals)"""
        key = (ic, s1_q, s2_q)
        if key in cache: return cache[key]
        cl = cells.cells[ic]; d = bg.get(ic)
        sub = dict(kind="mid", h=q2arb(s2_q - s1_q), hq=s2_q - s1_q, ta=cl["ta"] + q2arb(s1_q))
        Pe = [range_finite(d["Pe"][n].shift(q2arb(s1_q)) if s1_q != 0 else d["Pe"][n], sub) for n in range(Nf)]
        Qe = [range_finite(d["Qe"][n].shift(q2arb(s1_q)) if s1_q != 0 else d["Qe"][n], sub) for n in range(Nf)]
        cache[key] = (Pe, Qe)
        if len(cache) > 400: cache.pop(next(iter(cache)))
        return Pe, Qe

    def vlo(ic, s1_q, s2_q, f1, f2):
        """theta in [pi f1, pi f2] (f exact rationals); returns (lower bound of |V|/r, directed [q_lo, q_hi], [u_lo, u_hi])"""
        Pe, Qe = radial_ranges(ic, s1_q, s2_q)
        tb = PI * q2arb((f1 + f2) / 2) + arb(0, fup(PI * q2arb((f2 - f1) / 2)))
        q = c_l - sum((Pe[n] * (2 * (n + 1) * tb).cos() for n in range(Nf)), arb(0))
        u = sum((Qe[n] * (2 * (n + 1) * tb).sin() for n in range(Nf)), arb(0))
        def minabs(b): return 0.0 if b.contains(arb(0)) else min(abs(flo(b)), abs(fup(b)))
        mq = minabs(q); mu_ = minabs(u)
        return flo((arb(mq) * mq + arb(mu_) * mu_).sqrt()), [flo(q), fup(q)], [flo(u), fup(u)]

    results = dict(positive_min=math.inf, positive_min_at=None, inside=[], unresolved=[], positive=[], nodes=0)
    def leaf_record(ic, s1_q, s2_q, f1, f2, extra):
        cl = cells.cells[ic]
        return dict(cell=ic, t1=str(cl["tq"] + s1_q), t2=str(cl["tq"] + s2_q), theta1_over_pi=str(f1), theta2_over_pi=str(f2), **extra)
    def refine(ic, s1_q, s2_q, f1, f2, depth):
        results["nodes"] += 1
        cl = cells.cells[ic]; ta = float(cl["ta"].mid())
        t1 = ta + float(s1_q); t2 = ta + float(s2_q); th1 = math.pi * float(f1); th2 = math.pi * float(f2)
        if (inside_Q if mode == "rect" else inside_BP)(t1, t2, th1, th2):
            results["inside"].append(leaf_record(ic, s1_q, s2_q, f1, f2, {})); return
        v, qb, ub = vlo(ic, s1_q, s2_q, f1, f2)
        if v > 0:
            results["positive"].append(leaf_record(ic, s1_q, s2_q, f1, f2, dict(vlo=v, q=qb, u=ub)))
            if v < results["positive_min"]: results["positive_min"] = v; results["positive_min_at"] = (ic, t1, t2, th1, th2)
            return
        if depth >= DEPTH:
            results["unresolved"].append(leaf_record(ic, s1_q, s2_q, f1, f2, dict(q=qb, u=ub))); return
        r = math.exp((t1 + t2) / 2)
        if (th2 - th1) * r >= (t2 - t1) * r:     # angular arc length vs radial extent: bisect the longer
            mid = (f1 + f2) / 2
            refine(ic, s1_q, s2_q, f1, mid, depth + 1); refine(ic, s1_q, s2_q, mid, f2, depth + 1)
        else:
            mid_q = (s1_q + s2_q) / 2
            refine(ic, s1_q, mid_q, f1, f2, depth + 1); refine(ic, mid_q, s2_q, f1, f2, depth + 1)

    for n_, (ic, ib) in enumerate(targets):
        cl = cells.cells[ic]
        refine(ic, fmpq(0), cl["hq"], th_q[ib], th_q[ib + 1], 0)
        if n_ % 20 == 0: print("  box %d/%d (cell %d, theta box %d): nodes %d, terminal leaves: inside %d, positive %d, unresolved %d, positive min %.3e (%.0fs)" % (
            n_, len(targets), ic, ib, results["nodes"], len(results["inside"]), len(results["positive"]), len(results["unresolved"]), results["positive_min"], time.time() - t0), flush=True)
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    nleaf = len(results["inside"]) + len(results["positive"]) + len(results["unresolved"])
    out = dict(tag=tag, mode=mode, excluded_set=("Q = [xP - %.3f, xP + %.3f] x [-%.3f, %.3f] (V070), containment margin %.0e" % (hx, hx, hy, hy, SHRINK)) if mode == "rect" else ("B_P = B_{%.5f}(P) (Lemma Z), containment margin %.0e" % (rP, SHRINK)),
               xP=xP, rP=rP, vlo_threshold=thr, boxes_refined=len(targets), nodes=results["nodes"], terminal_leaves=nleaf,
               leaves_inside=len(results["inside"]), leaves_positive=len(results["positive"]), unresolved_count=len(results["unresolved"]),
               positive_min_outside=results["positive_min"], positive_min_at=results["positive_min_at"], depth=DEPTH, seconds=time.time() - t0,
               note="every terminal leaf is inside the excluded set (list 'inside'), or has the listed positive lower bound of |V|/r (list 'positive': exact t endpoints, theta/pi endpoints as exact rationals, directed q and u = V_theta/r bounds), or is unresolved (list 'unresolved'; would break (Zb))",
               inside=results["inside"], positive=results["positive"], unresolved=results["unresolved"])
    json.dump(out, open(os.path.join(outdir, "zrefine.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k not in ("inside", "positive", "unresolved")}, indent=1))
    print("unresolved (first 10):", results["unresolved"][:10])


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2] if len(a) > 2 else "rect", float(a[3]) if len(a) > 3 else 8.600064, float(a[4]) if len(a) > 4 else 99 / 2000, float(a[5]) if len(a) > 5 else 0.1)
