import sys, os, time
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, q2arb
from opimage import Cells, Background, Operator
from basis import cutoff_chi
from section import Weights, Section
ctx.prec = 256
T = ExactTrial(prec=256); T.build_green(verbose=False)
CELLS = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
full = set(cutoff_chi(T, CELLS).keys()) | set(ic for ic, cl in enumerate(CELLS.cells) if cl["kind"] in ("outer", "pinf"))
bg = Background(T, CELLS, nmax=19 + 4 + 3, full_cells=full)
k = T.k_q; W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
SEC = Section(T, CELLS, bg, W, Mh=4, stride=60, Mout=20, stride_test=30, verbose=False)
OP = SEC.op; c_l = 1 / T.k; denom = 3 * c_l + T.k * SEC.cKP
print("outer exponents alpha_q:", [str(a) for a in T.alpha_q[:6]], "outer_jl:", T.outer_jl[:6])
ic = 1567; cl = CELLS.cells[ic]; ta = float(cl["ta"].mid()); print("cell", ic, cl["kind"], "t_a", ta, "h", float(cl["h"].mid()))
KP = SEC.KP[0]; imgKP = OP.image(KP, ic); 
for lab, m in (("sp32+out", 3), ("sp32+out", 0), ("sp31+out", 3), ("out6", 3), ("sp20", 3)):
    j = [i for i, cd in enumerate(SEC.cols) if cd["label"] == lab and cd["m"] == m][0]; col = SEC.cols[j]["col"]
    dk = -(col.c) * T.k / denom
    insup = ic in col.pieces
    print("== %s m=%d: in support %s, c = %s, dk = %s, pieces exps: %s" % (lab, m, insup, col.c.str(5), dk.str(5), [str(e) for e in col.pieces[ic].terms] if insup else "-"))
    if insup:
        imT, imC = OP.image(col, ic, parts=True)
        for s in (0.5, 2.0, 3.9):
            sa = arb(s); t = ta + s
            vT = max((abs(float(ep(sa).mid())) for ep in imT.values()), default=0.0); vC = max((abs(float(ep(sa).mid())) for ep in imC.values()), default=0.0)
            vK = max((abs(float((ep(sa) * dk).mid())) for ep in imgKP.values()), default=0.0)
            tot = {}
            for N in set(imT) | set(imC) | set(imgKP):
                v = arb(0)
                if N in imT: v += imT[N](sa)
                if N in imC: v += imC[N](sa)
                if N in imgKP: v += imgKP[N](sa) * dk
                tot[N] = v
            Nmx = max(tot, key=lambda N: abs(float(tot[N].mid()))); vb = abs(float(col.pieces[ic](sa).mid()))
            print("   t=%.2f: |b|=%.2e  |T|max %.2e  |C|max %.2e  |dk KP|max %.2e  |total|max %.2e (mode %d, rad %.1e)  C modes top: %s" % (t, vb, vT, vC, vK, abs(float(tot[Nmx].mid())), Nmx, float(tot[Nmx].rad()),
                  sorted(((abs(float(ep(sa).mid())), N) for N, ep in imC.items()), reverse=True)[:3]))
