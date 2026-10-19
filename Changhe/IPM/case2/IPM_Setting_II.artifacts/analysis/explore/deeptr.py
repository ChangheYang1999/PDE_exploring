# Lead: backward-tracer log Gt with several stop radii lr0 (V59: stop e^-9 biases log Gt near the lower zero).
# Usage: python3 withpf2.py deeptr.py state.npz K lr0list [nA=1024]
# Prints, per lr0: m1, D_samp = logGt(269 deg) - logGt(89 deg), logGt at 89 / 269 / 0 / 180 deg relative to the bulk mean (|cos| > 0.3).
import sys, json, time, numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
st = np.load(sys.argv[1]); K = int(sys.argv[2]); lrs = [float(v) for v in sys.argv[3].split(',')]
nA = int(sys.argv[4]) if len(sys.argv) > 4 else 1024
g, lr, th, x, p = st['g'], st['lr'], st['th'], st['x'], float(st['p'])
Af = lambda t: np.cos(t) ** 2 * np.exp(x[:K] @ FE.basis(np.atleast_1d(t).ravel(), K)).reshape(np.shape(t))
for lr0 in lrs:
    t0 = time.time(); ng = FE.node_and_G(p, Af, g, lr, th, nA=nA, lr0=lr0)
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']; deg = np.degrees(ng['thA'])
    pk = lambda a: float(lgt[np.argmin(np.abs(deg - a))]); bulk = float(np.mean(lgt[np.abs(np.cos(ng['thA'])) > 0.3]))
    print(json.dumps(dict(lr0=lr0, m1=round(ng['m1'], 5), D_samp=round(pk(269) - pk(89), 4),
        up89=round(pk(89) - bulk, 4), low269=round(pk(269) - bulk, 4), at0=round(pk(0) - bulk, 4), at180=round(pk(180) - bulk, 4),
        up85=round(pk(85) - bulk, 4), low275=round(pk(275) - bulk, 4), nlive=ng['nlive'], wall=round(time.time() - t0))), flush=True)
