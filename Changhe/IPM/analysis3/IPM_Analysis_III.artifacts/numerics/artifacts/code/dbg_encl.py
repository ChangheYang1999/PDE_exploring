"""Compare the merged Taylor enclosure (encl.range_finite) with the crude mean-value enclosure and sampled values on given cells.
Everything at 512 bits so that the near-resonant inner-cell representation (lambda^-7 coefficients, V054) is meaningful."""
import sys, os, time
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background
from tailbound import sup_bound
from encl import range_finite, range_on_cell, merge_resonant
PREC = 512
ctx.prec = PREC
T = ExactTrial(prec=PREC); T.build_green(verbose=False)
cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
bg = Background(T, cells, nmax=None)
for ic in [int(x) for x in sys.argv[1].split(",")]:
    cl = cells.cells[ic]; d = bg.get(ic); h = cl["h"]
    print("=== cell", ic, cl["kind"], "t_a", float(cl["ta"]), "h", float(h) if h is not None else None, flush=True)
    if h is None: continue
    t0 = time.time(); tot_new = 0.0; tot_old = 0.0; nviol = 0; worst_mode = None; worst_rad = -1
    for n in range(1, T.Nf + 1):
        ep = d["Pe"][n - 1]
        new = range_finite(ep, cl)
        s0, s1 = sup_bound(ep, cl); old_rad = float((s1 * h / 2).upper())
        tot_new += float(new.rad()); tot_old += old_rad
        if float(new.rad()) > worst_rad: worst_rad = float(new.rad()); worst_mode = n
        for kk in range(9):
            v = ep(h * kk / 8)
            if not new.contains(v): nviol += 1; print("  VIOLATION mode", n, "k", kk, v.str(10), new.str(10))
        if n in (1, 3, 10, 27, 50, 100, 200, 260):
            epm, rem = merge_resonant(ep, h)
            print("  Pe_%d: new %s (rad %.3e) old rad %.3e; merge: %d->%d exps, rem %.2e; values %s" % (n, new.str(8), float(new.rad()), old_rad, len(ep.terms), len(epm.terms), float(rem.upper()), [("%.4e" % float(ep(h * kk / 4).mid())) for kk in range(5)]), flush=True)
    print("  sum of radii: new %.3e old %.3e; worst mode %d (rad %.3e); violations %d (%.1fs)" % (tot_new, tot_old, worst_mode, worst_rad, nviol, time.time() - t0), flush=True)
    dEP = ExpPoly()
    for n in range(1, T.Nf + 1): dEP = dEP + d["Pe"][n - 1].scale(arb((-1) ** (n + 1)))
    print("  d - c_l: new %s ; values %s" % (range_finite(dEP, cl).str(10), [("%.6f" % float(dEP(h * kk / 4).mid())) for kk in range(5)]), flush=True)
