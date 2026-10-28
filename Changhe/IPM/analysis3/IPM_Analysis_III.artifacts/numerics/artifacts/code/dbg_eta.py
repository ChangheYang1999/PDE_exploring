import sys, os, math, pickle
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial
from opimage import Cells, Background
from run_section import HERE
from fsec import mu_a, gG, ep_eval
import fsec_ang as ang
from eta2 import A_half_fast
ctx.prec = 256
T = ExactTrial(prec=256); T.build_green(verbose=False)
CELLS = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
bg = Background(T, CELLS, nmax=None)
NODES = pickle.load(open(os.path.join(HERE, "runs", "fsec_prep_L40_ng3_8_16.pkl"), "rb"))[0]
c_l = float((1 / T.k).mid()); Nf = T.Nf; Mj = T.Mj; M = 4096; NM = 800; nm = NM + 1
th = np.arange(M) * (2 * np.pi / M); n_ = np.arange(1, Nf + 1); j_ = np.arange(Mj)
COS2n = np.cos(np.outer(2 * n_, th)); SIN2n = np.sin(np.outer(2 * n_, th)); SINj = np.sin(np.outer(2 * j_ + 1, th)); COSj = np.cos(np.outer(2 * j_ + 1, th))
AH = A_half_fast(nm - 2); M4, DIV = ang.div_cos4(nm)
for ic in (0, 2, 300):
    cl = CELLS.cells[ic]; ctx.prec = 512 if cl["kind"] != "mid" else 256
    d = bg.get(ic); s_nodes, t_nodes, w_nodes = NODES[ic]
    for a_, s in list(enumerate(s_nodes))[::max(1, len(s_nodes) // 4)]:
        t = t_nodes[a_]
        Pe = np.array([ep_eval(d["Pe"][i], s) for i in range(Nf)]); Qe = np.array([ep_eval(d["Qe"][i], s) for i in range(Nf)])
        dR = np.array([ep_eval(d["dR"][j], s) for j in range(Mj)]); Rh = np.array([ep_eval(d["Rhat"][j], s) for j in range(Mj)])
        F = (c_l - Pe @ COS2n) * (dR @ SINj) + (Qe @ SIN2n) * (((2 * j_ + 1) * Rh) @ COSj) - Rh @ SINj
        fft = np.fft.rfft(F); G = np.zeros(nm); kk = 2 * np.arange(nm) + 1; kk = kk[kk < len(fft)]; G[:len(kk)] = -2.0 * fft[kk].imag / M
        gam, R, a0 = ang.jet_split(G); Q, res = DIV(R)
        wR = math.exp(8 * t + mu_a(t))
        print("cell %d t=%.2f: |F|max %.2e |G|max %.2e (N of max %d) |G[:3]| %s gamma %.2e axis %.2e |Q|max %.2e res %.2e  Q^TAQ %.2e  wR %.2e  -> w*wR*QAQ %.2e" % (
            ic, t, np.max(np.abs(F)), np.max(np.abs(G)), int(np.argmax(np.abs(G))), np.array2string(np.abs(G[:3]), precision=2), gam, a0, np.max(np.abs(Q)), res, float(Q @ AH @ Q), wR, w_nodes[a_] * wR * float(Q @ AH @ Q)), flush=True)
