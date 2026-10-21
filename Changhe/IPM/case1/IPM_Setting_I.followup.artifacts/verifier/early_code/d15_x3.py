"""D15 on a stored trial with this lane's own w: g(P) = rho_y(x*, 0) from the trial's axis trace and from the w-only
construction g_w ((log g_w)' = (w' - A)/w, g_w ~ x^2 at 0, i.e. a(0) = 1), lambda_P = g(P)/A, (1 + g(P))/A,
w'(x*), w''(x*), h(P) - 1.
usage: python3 d15_x3.py trial.npz eval.npz Nth tag"""
import sys, math, json
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from vgen import Trial
from vaxis import AxisData, B3
trial, evnpz, Nth, tag = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
tr = Trial(trial, 'cuda')
ad0 = AxisData(tr, evnpz, Nth=Nth, K=4)
d = np.load(evnpz, allow_pickle=True)
c_lint = json.loads(str(d['summary']))['cl_identity_int']
c_lP, adP = ad0.c_l, ad0
for it in range(3):
    c_lP = 1 - c_lP + float(adP.interp('w', [adP.xs])[1][0])
    adP = AxisData(tr, evnpz, c_l=c_lP, Nth=Nth, K=4)
out = dict(tag=tag)
for lab, ad in [('cl_1/k', ad0), ('cl_P', adP), ('cl_0', AxisData(tr, evnpz, c_l=c_lint, Nth=Nth, K=4))]:
    xs = ad.xs
    A = 2 * ad.c_l - 1
    W = ad.interp('w', [xs])[:, 0]
    G = ad.interp('g', [xs])[:, 0]
    b = B3(ad)
    gw = xs ** 2 * math.exp(float(b.cumval('e', [xs])[0]))
    out[lab] = dict(c_l=ad.c_l, A=A, xstar=xs, w1=W[1], w1_minus_A=W[1] - A, w2=2 * W[2], hP_minus_1=2 * ad.c_l - W[1] - 1,
                    g_trial=G[0], g_trial_prime=G[1], g_w=gw, lam_trial=G[0] / A, lam_w=gw / A,
                    one_plus_g_over_A_trial=(1 + G[0]) / A, one_plus_g_over_A_w=(1 + gw) / A, threeA_minus_g=3 * A - G[0])
print(json.dumps(out, indent=1))
