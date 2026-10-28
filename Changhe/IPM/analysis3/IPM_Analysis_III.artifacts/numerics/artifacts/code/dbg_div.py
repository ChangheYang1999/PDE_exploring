"""How does the cos^4 quotient of a (compensated) column image depend on the angular truncation N? Compare N = 19, 40, 80 and the complete
mode set at a few nodes and cells, for one far-from-support column and one in-support column."""
import sys, os, time, math
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial
from opimage import Cells, Background, Operator
from basis import cutoff_chi
from section import Weights, Section
import fsec_ang as ang
from eta2 import A_half_fast
ctx.prec = 256
T = ExactTrial(prec=256); T.build_green(verbose=False)
CELLS = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
bg = Background(T, CELLS, nmax=None)
k = T.k_q; W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
SEC = Section(T, CELLS, bg, W, Mh=4, stride=60, Mout=12, stride_test=30, verbose=False)
OPfull = Operator(T, CELLS, bg, Nmax=None)
c_l = 1 / T.k; denom = 3 * c_l + T.k * SEC.cKP
KP = SEC.KP[0]
def full_image_vals(col, ic, s):
    """complete mode vector (all N) of the compensated image at sigma = s, as floats from balls"""
    dk = -(col.c) * T.k / denom
    img = OPfull.image(col, ic); imgK = OPfull.image(KP, ic)
    Nmax = max(max(img), max(imgK)); out = np.zeros(Nmax + 1)
    for N in range(Nmax + 1):
        v = arb(0)
        if N in img: v += img[N](arb(s))
        if N in imgK: v += imgK[N](arb(s)) * dk
        out[N] = float(v.mid())
    return out
for ic in (600, 1300, 1567):
    cl = CELLS.cells[ic]; ta = float(cl["ta"].mid()); h = float(cl["h"].mid()); s = h / 2; t = ta + s
    for lab, m in (("sp9", 1), ("sp20", 2)):
        j = [i for i, cd in enumerate(SEC.cols) if cd["label"] == lab and cd["m"] == m][0]; col = SEC.cols[j]["col"]
        t0 = time.time(); G = full_image_vals(col, ic, s); nfull = len(G)
        wR = math.exp(8 * t + (-8.5 * t if t < 0 else -1.25 * t))
        line = "cell %d t=%.2f col %s m=%d (in support %s): %d modes, |G|max %.2e, |G[-5:]| max %.1e, time %.0fs | " % (ic, t, lab, m, ic in col.pieces, nfull, np.max(np.abs(G)), np.max(np.abs(G[-5:])), time.time() - t0)
        for N in (19, 40, 80, nfull - 1):
            nm = N + 1; Gt = G[:nm].copy() if nm <= nfull else np.concatenate([G, np.zeros(nm - nfull)])
            gam, R, a0 = ang.jet_split(Gt); M4, DIV = ang.div_cos4(nm); Q, res = DIV(R); AH = A_half_fast(nm - 2)
            line += " N=%d: gamma %.3e axis %.1e |Q|max %.2e res %.1e wR*QAQ %.3e |" % (N, gam, a0, np.max(np.abs(Q)), res, wR * float(Q @ AH @ Q))
        print(line, flush=True)
