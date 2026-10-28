"""Test of the exact operator-image machinery: sum_m L(a_m column) = L rho~ = 2 eps~ + rho~ + (c/3 - c_l) d_t rho~ (in e^{-3t} factor modes)."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, fmpq, ctx
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Column, Operator
FIX = os.path.join(os.path.dirname(__file__), "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "numerics", "data", "trial_small_M20.npz")
T = ExactTrial.from_npz(FIX, prec=200)
T.build_green()
print("c =", T.c.str(30), " 3/k-1 =", (3 / T.k - 1).str(30))
cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(3, 2)], outer_extra=[fmpq(1), fmpq(3)])
print("cells:", cells.n, "kinds:", cells.cells[0]["kind"], cells.cells[1]["kind"], cells.cells[-1]["kind"])
bg = Background(T, cells)
op = Operator(T, cells, bg)
# the trial's own modes as columns on all cells
t0 = time.time()
cols = []
for m in range(T.M):
    pieces = {}
    for ic, cl in enumerate(cells.cells):
        if cl["kind"] == "mid": pieces[ic] = bg.get(ic)["Rhat"] and ExpPoly([(fmpq(0), [T.cell_a[cl["trial_cell"]][r_, m] for r_ in range(T.p + 1)])])
        elif cl["kind"] in ("minf", "inner"): pieces[ic] = bg.a_in[m].shift(q2arb(cl["shift"]))
        else: pieces[ic] = bg.a_out[m].shift(q2arb(cl["shift"]))
    cols.append(Column(m, pieces, T, cells, label="a_%d" % m))
print("columns built: %.1fs; sum of column strains = %s (c = %s)" % (time.time() - t0, sum((c.c for c in cols), arb(0)).str(25), T.c.str(25)))
fac = T.c / 3 - op.c_l
for ic in [0, 1, cells.first_mid, cells.first_mid + 3, cells.first_mid + T.nc // 2, cells.first_mid + T.nc - 1, cells.n - 2, cells.n - 1]:
    cl = cells.cells[ic]; t0 = time.time()
    d = bg.get(ic)
    tot = {}
    for col in cols:
        for N, ep in op.image(col, ic).items():
            tot[N] = tot[N] + ep if N in tot else ep
    eps = op.residual_modes(ic)
    ref = {}
    for N in range(T.Mj):
        ref[N] = eps.get(N, ExpPoly()).scale(arb(2)) + d["Rhat"][N] + d["dR"][N].scale(fac)
    for N in eps:
        if N >= T.Mj: ref[N] = eps[N].scale(arb(2))
    # evaluate at a few sigma in the cell
    if cl["kind"] == "minf": sig = [arb(-3), arb(-1), arb(0)]
    elif cl["kind"] == "pinf": sig = [arb(0), arb(1), arb(5)]
    else: sig = [arb(0), cl["h"] / 3, cl["h"]]
    worst = 0.0; scale = 0.0; contained = True; maxrad = 0.0
    for N in sorted(set(tot) | set(ref)):
        for s in sig:
            v1 = tot[N](s) if N in tot else arb(0); v2 = ref[N](s) if N in ref else arb(0)
            diff = v1 - v2
            contained = contained and diff.contains(arb(0)); maxrad = max(maxrad, float(diff.rad()))
            worst = max(worst, abs(float(diff.mid())) + float(diff.rad())); scale = max(scale, abs(float(v2.mid())))
    print("   zero containment of every difference ball: %s (max radius %.2e)" % (contained, maxrad))
    print("cell %4d (%5s, t_a=%8.4f): max |sum L a_m - (2eps + rho + (c/3-c_l) d_t rho)| = %.3e  (scale %.3e; %d modes; %.1fs)" % (ic, cl["kind"], float(cl["ta"]), worst, scale, len(ref), time.time() - t0), flush=True)
