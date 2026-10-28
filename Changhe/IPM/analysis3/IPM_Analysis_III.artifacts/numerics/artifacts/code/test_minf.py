"""Guard test: on the inner half-line no column image may carry a non-decaying term (exponent <= 0 in sigma, cell minf) and no far
column may have a nonzero Bt_1 coefficient there; also the far-field compensated image has no e^{alpha_0 sigma} degree-0 term."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, fmpq, ctx
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Column, Operator
from basis import CoarseSplines, build_mode_columns, tail_columns, cutoff_chi
from section import Weights, Section
FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "numerics", "data", "trial_small_M20.npz")
# 04:35Z: default background is the EXACT trial. On the fixture the J column image has a genuine constant (3 c_l - 1 - c[rho_fixture]) x^2 y
# near 0 because the fixture is not exactly normalized; for the exact trial that constant is an exact zero (V005), so an exponent-0 term is
# accepted iff its coefficient ball contains 0 with radius < 1e-25 (printed).
USE_FIXTURE = len(sys.argv) > 1 and sys.argv[1] == "fixture"
T = ExactTrial.from_npz(FIX, prec=200) if USE_FIXTURE else ExactTrial(prec=200)
T.build_green(verbose=False)
cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
full = set(cutoff_chi(T, cells).keys()) | set(ic for ic, cl in enumerate(cells.cells) if cl["kind"] in ("outer", "pinf"))
bg = Background(T, cells, nmax=6 + 2 + 3, full_cells=full)
k = T.k_q; W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
S = Section(T, cells, bg, W, Mh=2, stride=60, Mout=6, stride_test=30, verbose=False)
ok = True
ic0 = 0; icp = cells.n - 1
for cd in S.cols + [dict(col=S.TAU[0], label="TAU", m=0), dict(col=S.KP[0], label="KP", m=0)]:
    c = cd["col"]
    if ic0 in c.pieces:
        img = S.op.image(c, ic0)
        for N, ep in img.items():
            for e, cs in ep.terms.items():
                if q2arb(e) < 0: print("FAIL non-decaying term", cd["label"], N, e); ok = False
                elif q2arb(e) == 0:
                    v = cs[0]; tiny = v.contains(arb(0)) and float(v.rad()) < 1e-25 and all(x == 0 for x in cs[1:])
                    print("exponent-0 term", cd["label"], "mode", N, "coefficient", v.str(5), "-> exact-zero ball" if tiny else "-> FAIL (genuine constant)")
                    if not tiny: ok = False
    else:
        fc = S.op.far_coefficients(c, ic0)
        if 1 in fc and fc[1][1] != 0: print("FAIL Bt_1 nonzero left of support", cd["label"]); ok = False
print("minf checks:", "OK" if ok else "FAILED")
# far-field: compensated image of one column + dk KP on the outer half-line must have no alpha_0 degree-0 term
denom = 3 * S.op.c_l + T.k * S.cKP; al0 = T.alpha_q[0]
for cd in S.cols[:3] + [dict(col=S.TAU[0], label="TAU")]:
    c = cd["col"]; dk = -c.c * T.k / denom
    img = S.op.image(c, icp); imgK = S.op.image(S.KP[0], icp)
    worst = 0.0
    for N in set(img) | set(imgK):
        ep = img.get(N, ExpPoly()) + imgK.get(N, ExpPoly()).scale(dk)
        if al0 in ep.terms:
            v = ep.terms[al0][0]
            if not v.contains(arb(0)): print("FAIL far tail not cancelled", cd["label"], N, v.str(5)); ok = False
            worst = max(worst, float(v.rad()))
    print("far cancellation", cd["label"], "max radius of the cancelled coefficient %.2e" % worst)
print("ALL OK" if ok else "SOME CHECKS FAILED")
