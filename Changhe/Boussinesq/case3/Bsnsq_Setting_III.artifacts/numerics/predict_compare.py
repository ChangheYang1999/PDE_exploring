"""predict_compare.py -- interpolate the (lambda, Q_R) pairs of the beta-parameterized path (runs/axis_blamB32_beta*.json + state lambdas) and
of the lambda path at the lead's pre-registered lambdas 0.935, 0.93, 0.925 (lead 06:35Z: pole 231/337/521, exp-quad 224/307/429, exp-cubic
229/327/481), log-linear in lambda between neighbouring stages. Usage: python3 code/predict_compare.py"""
import glob, json, numpy as np, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pairs = [(0.99, 19.47), (0.98, 26.80), (0.97, 38.98), (0.965, 47.85), (0.96, 59.14), (0.955, 74.25), (0.95, 94.67), (0.945, 123.27), (0.94, 166.27)]
for f in sorted(glob.glob(f'{HERE}/runs/axis_blamB32*_beta*.json')):
    tag = os.path.basename(f)[5:-5]; st = f'{HERE}/runs/{tag}.npz'
    if not os.path.exists(st): continue
    d = np.load(st); A = json.load(open(f))
    pairs.append((float(d['lam']), A['axis']['up']['Q_closed_form_est'])); print(f'{tag}: lambda {float(d["lam"]):.6f} beta {float(d["beta"]):.6f} Q_R {pairs[-1][1]:.2f}')
pairs = sorted(set(pairs), key=lambda p: -p[0])
lam = np.array([p[0] for p in pairs]); Q = np.array([p[1] for p in pairs])
pred = {0.935: (231, 224, 229), 0.93: (337, 307, 327), 0.925: (521, 429, 481)}
print('lambda   measured Q_R (log-linear interpolation between stages; "extrap" if outside)   pole / exp-quad / exp-cubic (lead 06:35Z)')
for l0, pr in pred.items():
    if l0 < lam.min() - 1e-12:
        print(f'{l0:.3f}   not reached (smallest lambda on the path {lam.min():.4f})   {pr}'); continue
    # path may be non-monotone in lambda (fold): use the first crossing in path order
    for i in range(len(lam) - 1):
        a, b = lam[i], lam[i + 1]
        if (a - l0) * (b - l0) <= 0 and a != b:
            t = (l0 - a) / (b - a); Qi = float(np.exp(np.log(Q[i]) + t * (np.log(Q[i + 1]) - np.log(Q[i]))))
            print(f'{l0:.3f}   {Qi:.1f}  (between stages lambda {a:.4f} Q {Q[i]:.1f} and {b:.4f} Q {Q[i+1]:.1f})   {pr}'); break
