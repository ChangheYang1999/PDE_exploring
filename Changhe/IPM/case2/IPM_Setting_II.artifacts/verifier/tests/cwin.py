"""Window log-factor of the lead's winpic.py data: A(th) = cos^2 th exp(F0(th) + c(th)), c periodic-linear on th_k = 2 pi k / nA
(the lead's np.interp form). cwin_fn(npz_path) returns a function of th giving exp(c(th)), or None if the file has no cwin."""
import math, numpy as np
def cwin_fn(fn):
    d = np.load(fn, allow_pickle=True)
    if 'cwin' not in d.files:
        return None
    cw = np.asarray(d['cwin'], float); nA = len(cw); thf = 2*math.pi*np.arange(nA)/nA
    xp = np.concatenate([thf, [2*math.pi]]); fp = np.concatenate([cw, [cw[0]]])
    return lambda t: np.exp(np.interp(np.mod(t, 2*math.pi), xp, fp))
