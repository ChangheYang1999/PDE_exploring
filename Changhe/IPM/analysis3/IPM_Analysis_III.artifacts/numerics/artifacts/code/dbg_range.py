"""Diagnostic: why are the radial range enclosures of Pe_n wide on some cells? Prints term structure and values."""
import sys, os, time
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background
from tailbound import sup_bound
ctx.prec = 160
T = ExactTrial(prec=160); T.build_green(verbose=False)
cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
bg = Background(T, cells, nmax=None)
for ic in [int(x) for x in sys.argv[1].split(",")]:
    cl = cells.cells[ic]; d = bg.get(ic); h = cl["h"]
    print("=== cell", ic, cl["kind"], "t_a", float(cl["ta"]), "h", float(h) if h is not None else None)
    tot_rad = 0.0
    for n in [1, 2, 3, 5, 10, 20, 50, 100, 150, 200, 259, 260]:
        ep = d["Pe"][n - 1]
        s0, s1 = sup_bound(ep, cl)
        vals = [float(ep(h * k / 4).mid()) for k in range(5)] if h is not None else [float(ep(0).mid())]
        print("Pe_%d: terms:" % n, [(str(e), [("%.2e" % float(abs(c).upper())) for c in cs]) for e, cs in sorted(ep.terms.items(), key=lambda kv: float(kv[0]))][:8])
        print("     values at sigma = k h/4:", ["%.4e" % v for v in vals], " sup|f| bound %.3e, sup|f'| bound %.3e, mv-radius %.3e" % (float(s0.upper()), float(s1.upper()), float((s1 * h / 2).upper()) if h is not None else float("nan")))
    # total radius of d over all modes
    acc = 0.0
    for n in range(1, T.Nf + 1):
        s0, s1 = sup_bound(d["Pe"][n - 1], cl); acc += float((s1 * h / 2).upper()) if h is not None else 0.0
    print("sum over modes of mv-radius of Pe_n:", "%.3e" % acc)
