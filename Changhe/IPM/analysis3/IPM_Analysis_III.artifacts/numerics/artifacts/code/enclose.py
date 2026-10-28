"""Rigorous box enclosures of pointwise coefficient functions of the exact modal trial (s2-num):
   q(X) = V.X/|X|^2 = c_l - sum_n Pe_n(t) cos(2n theta)             (radial rate of the flow; Pe_n = e^{-2t} 2n psi_n)
   b_+(X) = (|grad rho~| - d_y rho~)/2,  with  rho~_r = e^{2t} sum_j dR_j(t) sin((2j+1) theta),  rho~_theta / r = e^{2t} sum_j (2j+1) Rhat_j(t) cos((2j+1) theta),
         d_y rho~ = rho~_r sin theta + (rho~_theta/r) cos theta,
   U_r/r and U_theta/r (the velocity modes) on boxes [t_a, t_b] x [theta_1, theta_2] of the first quadrant (the other quadrants follow by parity).
Radial enclosure of an exponential polynomial f on a finite cell: f(mid) +/- sup|f'| h/2 (mean value theorem; sup by coefficient sums);
on the half-lines: [-sup|f|, sup|f|] (plus the exact constants of the inner cell: Rhat_0 = Rhat_1 = 1/4 etc. appear automatically).
Angular enclosure: arb cos/sin of the theta interval as a ball.  Output: float lower/upper bounds per box (outward).
Usage: python3 enclose.py <tag> ntheta [prec]   (2 workers max are respected by the caller; this program is single-process)
"""
import sys, os, time, json
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background
from tailbound import sup_bound
from run_section import HERE


def range_on_cell(ep, cl):
    """arb ball enclosing the range of the exponential polynomial on the cell"""
    if cl["kind"] in ("minf", "pinf"):
        s0, _ = sup_bound(ep, cl); return arb(0, float(s0.upper()) + 1e-300)
    h = cl["h"]; mid = h / 2
    v = ep(mid); _, sd = sup_bound(ep, cl)
    return v + arb(0, float((sd * h / 2).upper()))


def main(tag, ntheta=64, prec=192):
    ctx.prec = prec; t0 = time.time()
    T = ExactTrial(prec=prec); T.build_green(verbose=False)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    bg = Background(T, cells, nmax=None)
    c_l = 1 / T.k; Nf = T.Nf; Mj = T.Mj
    th = [arb.pi() / 2 * i / ntheta for i in range(ntheta + 1)]
    thbox = [th[i] + arb(0, float(((th[i + 1] - th[i]) / 2).upper())) + (th[i + 1] - th[i]) / 2 - (th[i + 1] - th[i]) / 2 for i in range(ntheta)]
    thbox = [(th[i] + th[i + 1]) / 2 + arb(0, float(((th[i + 1] - th[i]) / 2).upper()) * (1 + 1e-15)) for i in range(ntheta)]
    cosn = [[(2 * n * tb).cos() for n in range(1, Nf + 1)] for tb in thbox]            # cos(2n theta) ranges
    sinj = [[((2 * j + 1) * tb).sin() for j in range(Mj)] for tb in thbox]
    cosj = [[((2 * j + 1) * tb).cos() for j in range(Mj)] for tb in thbox]
    sinth = [tb.sin() for tb in thbox]; costh = [tb.cos() for tb in thbox]
    nc = cells.n
    Q = np.zeros((nc, ntheta, 2)); BP = np.zeros((nc, ntheta, 2)); GR = np.zeros((nc, ntheta, 2)); UR = np.zeros((nc, ntheta, 2)); UT = np.zeros((nc, ntheta, 2))
    cellinfo = []
    for ic in range(nc):
        cl = cells.cells[ic]; d = bg.get(ic)
        Pe_r = [range_on_cell(d["Pe"][ni], cl) for ni in range(Nf)]
        Qe_r = [range_on_cell(d["Qe"][ni], cl) for ni in range(Nf)]
        dR_r = [range_on_cell(d["dR"][j], cl) for j in range(Mj)]
        R_r = [range_on_cell(d["Rhat"][j], cl) for j in range(Mj)]
        # e^{2t} over the cell
        if cl["kind"] == "minf": e2 = arb(0, float((2 * cl["ta"]).exp().upper()))          # (0, e^{2 t_a}]
        elif cl["kind"] == "pinf": e2 = None
        else: e2 = ((2 * cl["ta"]).exp() + (2 * (cl["ta"] + cl["h"])).exp()) / 2; e2 = e2 + arb(0, float((((2 * (cl["ta"] + cl["h"])).exp() - (2 * cl["ta"]).exp()) / 2).upper()))
        for ib in range(ntheta):
            q = c_l - sum((Pe_r[ni] * cosn[ib][ni] for ni in range(Nf)), arb(0))
            ur = -sum((Pe_r[ni] * cosn[ib][ni] for ni in range(Nf)), arb(0))       # U_r / r
            ut = sum((Qe_r[ni] * ((2 * (ni + 1)) * thbox[ib]).sin() for ni in range(Nf)), arb(0))   # U_theta / r = e^{-2t} dpsi/dt sum ... = sum Qe_n sin 2n theta
            Q[ic, ib] = [float(q.lower()), float(q.upper())]; UR[ic, ib] = [float(ur.lower()), float(ur.upper())]; UT[ic, ib] = [float(ut.lower()), float(ut.upper())]
            if e2 is not None:
                rr = e2 * sum((dR_r[j] * sinj[ib][j] for j in range(Mj)), arb(0))
                rt = e2 * sum((R_r[j] * (2 * j + 1) * cosj[ib][j] for j in range(Mj)), arb(0))
                gr = (rr * rr + rt * rt).sqrt(); dy = rr * sinth[ib] + rt * costh[ib]
                bp = (gr - dy) / 2
                BP[ic, ib] = [float(bp.lower()), float(bp.upper())]; GR[ic, ib] = [float(gr.lower()), float(gr.upper())]
            else:
                BP[ic, ib] = [0.0, np.inf]; GR[ic, ib] = [0.0, np.inf]      # outer half-line: |grad rho~| ~ r^{k-1} -> 0 but unbounded weight; handled analytically by the lead
        cellinfo.append(dict(kind=cl["kind"], t_a=float(cl["ta"]), h=(float(cl["h"]) if cl["h"] is not None else None)))
        if ic % 100 == 0: print("cell %d/%d (%.0fs)" % (ic, nc, time.time() - t0), flush=True)
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    np.savez(os.path.join(outdir, "enclosures.npz"), Q=Q, BP=BP, GR=GR, UR=UR, UT=UT, theta_edges=np.array([float(x) for x in th]))
    json.dump(dict(cells=cellinfo, ntheta=ntheta, prec=prec, note="box enclosures [lower, upper] of q, b_+, |grad rho~|, U_r/r, U_theta/r on [t_a, t_a+h] x [theta_i, theta_{i+1}] for the exact modal trial; outer half-line b_+ not enclosed (inf)"), open(os.path.join(outdir, "enclosures.json"), "w"))
    fin = np.isfinite(BP[:, :, 1])
    print("done %.0fs: max b_+ upper %.4f (finite boxes), min q lower %.4f, max q upper %.4f" % (time.time() - t0, BP[:, :, 1][fin].max(), Q[:, :, 0].min(), Q[:, :, 1].max()))


if __name__ == "__main__":
    a = sys.argv
    main(a[1], int(a[2]) if len(a) > 2 else 64, int(a[3]) if len(a) > 3 else 192)
