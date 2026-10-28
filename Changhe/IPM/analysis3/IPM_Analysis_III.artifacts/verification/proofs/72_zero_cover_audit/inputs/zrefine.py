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
    th_arb = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]

    def inside_Q(t1, t2, th1, th2):
        """the polar box lies inside the rectangle Q: x = r cos th in [xP - hx, xP + hx], y = r sin th <= hy (x decreases in th, increases in r;
        y increases in both): check the extreme corners (monotone in both variables on the first quadrant)"""
        r1, r2 = math.exp(t1), math.exp(t2)
        xmin = r1 * math.cos(th2); xmax = r2 * math.cos(th1); ymax = r2 * math.sin(th2)
        return xmin >= xP - hx * (1 - 1e-9) and xmax <= xP + hx * (1 - 1e-9) and ymax <= hy * (1 - 1e-9)

    def inside_BP(t1, t2, th1, th2):
        """the polar box lies inside the disc B_P iff its four corners do (the disc is convex and the box is... not convex in the plane: check the
        corners and the two arc midpoints of the outer arc as well, and require the box diagonal to be small; conservative: corners + outer arc samples)"""
        r1, r2 = math.exp(t1), math.exp(t2)
        pts = [(r1, th1), (r1, th2), (r2, th1), (r2, th2)] + [(r2, th1 + (th2 - th1) * s / 8) for s in range(1, 8)] + [(r1, th1 + (th2 - th1) * s / 8) for s in range(1, 8)]
        return all(math.hypot(r * math.cos(th) - xP, r * math.sin(th)) <= rP * (1 - 1e-9) for r, th in pts)

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

    def vlo(ic, s1_q, s2_q, th1, th2):
        Pe, Qe = radial_ranges(ic, s1_q, s2_q)
        tb = (th1 + th2) / 2 + arb(0, fup((th2 - th1) / 2))
        q = c_l - sum((Pe[n] * (2 * (n + 1) * tb).cos() for n in range(Nf)), arb(0))
        u = sum((Qe[n] * (2 * (n + 1) * tb).sin() for n in range(Nf)), arb(0))
        def minabs(b): return 0.0 if b.contains(arb(0)) else min(abs(flo(b)), abs(fup(b)))
        mq = minabs(q); mu_ = minabs(u)
        return flo((arb(mq) * mq + arb(mu_) * mu_).sqrt())

    results = dict(positive_min=math.inf, positive_min_at=None, inside=[], unresolved=[], leaves=0)
    def refine(ic, s1_q, s2_q, th1, th2, depth):
        cl = cells.cells[ic]; ta = float(cl["ta"].mid())
        t1 = ta + float(s1_q); t2 = ta + float(s2_q); f1 = float(th1.mid()); f2 = float(th2.mid())
        if (inside_Q if mode == "rect" else inside_BP)(t1, t2, f1, f2):
            results["inside"].append((ic, t1, t2, f1, f2)); results["leaves"] += 1; return
        v = vlo(ic, s1_q, s2_q, th1, th2); results["leaves"] += 1
        if v > 0:
            if v < results["positive_min"]: results["positive_min"] = v; results["positive_min_at"] = (ic, t1, t2, f1, f2)
            return
        if depth >= DEPTH:
            results["unresolved"].append((ic, t1, t2, f1, f2)); return
        r = math.exp((t1 + t2) / 2)
        if (f2 - f1) * r >= (t2 - t1) * r:     # angular arc length vs radial extent: bisect the longer
            mid = (th1 + th2) / 2
            refine(ic, s1_q, s2_q, th1, mid, depth + 1); refine(ic, s1_q, s2_q, mid, th2, depth + 1)
        else:
            mid_q = (s1_q + s2_q) / 2
            refine(ic, s1_q, mid_q, th1, th2, depth + 1); refine(ic, mid_q, s2_q, th1, th2, depth + 1)

    for n_, (ic, ib) in enumerate(targets):
        cl = cells.cells[ic]
        refine(ic, fmpq(0), cl["hq"], th_arb[ib], th_arb[ib + 1], 0)
        if n_ % 20 == 0: print("  box %d/%d (cell %d, theta box %d): leaves so far %d, inside %d, unresolved %d, positive min %.3e (%.0fs)" % (
            n_, len(targets), ic, ib, results["leaves"], len(results["inside"]), len(results["unresolved"]), results["positive_min"], time.time() - t0), flush=True)
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    out = dict(tag=tag, mode=mode, excluded_set=("Q = [xP - %.3f, xP + %.3f] x [-%.3f, %.3f] (V070)" % (hx, hx, hy, hy)) if mode == "rect" else ("B_P = B_{%.5f}(P) (Lemma Z)" % rP), xP=xP, rP=rP, vlo_threshold=thr, boxes_refined=len(targets), leaves=results["leaves"], positive_min_outside_BP=results["positive_min"],
               positive_min_at=results["positive_min_at"], leaves_inside_BP=len(results["inside"]), inside_BP=results["inside"], unresolved=results["unresolved"],
               unresolved_count=len(results["unresolved"]), depth=DEPTH, seconds=time.time() - t0,
               note="every refined leaf is either inside B_P (listed) or has the listed positive lower bound of |V|/r; unresolved leaves (if any) break (Zb)")
    json.dump(out, open(os.path.join(outdir, "zrefine.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k not in ("inside_BP", "unresolved")}, indent=1))
    print("unresolved (first 10):", results["unresolved"][:10])


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2] if len(a) > 2 else "rect", float(a[3]) if len(a) > 3 else 8.600064, float(a[4]) if len(a) > 4 else 99 / 2000, float(a[5]) if len(a) > 5 else 0.1)
