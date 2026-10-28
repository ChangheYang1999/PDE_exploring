import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, fmpq, ctx
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Column, Operator
FIX = os.path.join(os.path.dirname(__file__), "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "numerics", "data", "trial_small_M20.npz")
T = ExactTrial.from_npz(FIX, prec=200); T.build_green(verbose=False)
cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(3, 2)], outer_extra=[fmpq(1), fmpq(3)])
bg = Background(T, cells); op = Operator(T, cells, bg)
cols = []
for m in range(T.M):
    pieces = {}
    for ic, cl in enumerate(cells.cells):
        if cl["kind"] == "mid": pieces[ic] = ExpPoly([(fmpq(0), [T.cell_a[cl["trial_cell"]][r_, m] for r_ in range(T.p + 1)])])
        elif cl["kind"] in ("minf", "inner"): pieces[ic] = bg.a_in[m].shift(q2arb(cl["shift"]))
        else: pieces[ic] = bg.a_out[m].shift(q2arb(cl["shift"]))
    cols.append(Column(m, pieces, T, cells))
    print("col", m, "built", flush=True)
fm = cells.first_mid
for ic, ci in [(fm, 0), (fm + 1, 1), (fm + 7, 7), (fm + 779, 779)]:
    for n in (1, 2, 3, 4):
        sA = sum((c.A_left[ic][n] for c in cols if n in c.hmodes), arb(0)); sB = sum((c.B_right[ic][n] for c in cols if n in c.hmodes), arb(0))
        dA = sA - T.A[ci][n - 1]; dB = sB - T.B[ci + 1][n - 1]
        print("cell %d n=%d: sumA - T.A = %s (|T.A| %.3e)   sumB - T.B = %s (|T.B| %.3e)" % (ic, n, dA.str(5, radius=True), abs(float(T.A[ci][n - 1].mid())), dB.str(5, radius=True), abs(float(T.B[ci + 1][n - 1].mid()))), flush=True)
# parts split at the first mid cell
fac = T.c / 3 - op.c_l
for ic in (fm, fm + 779):
    d = bg.get(ic); eps = op.residual_modes(ic)
    tab = {}; tcd = {}
    for col in cols:
        a, b = op.image(col, ic, parts=True)
        for N, ep in a.items(): tab[N] = tab[N] + ep if N in tab else ep
        for N, ep in b.items(): tcd[N] = tcd[N] + ep if N in tcd else ep
    s = d["h"] / 2
    for N in range(0, 6):
        e_ab = (tab.get(N, ExpPoly())(s) - eps.get(N, ExpPoly())(s))
        ref_cd = eps.get(N, ExpPoly())(s) - op.c_l * d["dR"][N](s) + d["Rhat"][N](s) + (T.c / 3) * d["dR"][N](s)
        e_cd = tcd.get(N, ExpPoly())(s) - ref_cd
        print("cell %d N=%d: transport part err %s ; nonlocal part err %s ; eps %s" % (ic, N, e_ab.str(5, radius=True), e_cd.str(5, radius=True), eps.get(N, ExpPoly())(s).str(8)), flush=True)
