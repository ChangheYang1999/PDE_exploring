"""Values of the canonical logarithmic coefficients on the real t = log r axis (lead).
Runs the unmodified long-double recursion of code/logseries_ld.py with f_1 = amp*sin(theta) at delta = A/B to order N,
then for every order n and every t in a fixed grid writes (unit amplitude, i.e. divided by amp^n):
  lF[t]   : log10 sum_m |sum_k f_{n,m,k} t^k|   (l1 norm over the complex Fourier modes of f_n(t, .)),
  lFabs[t]: log10 sum_m sum_k |f_{n,m,k}| |t|^k (no cancellation; lFabs - lF measures the cancellation),
  lG, lGabs: the same for the stream g_n.
The arrays f_n, g_n at the orders listed in SAVE are written as long-double .npy files for later analysis.
Usage: logseries_tprofile.py A B N amp out.jsonl savedir [dbl]
(with the optional argument dbl the double-precision recursion of code/logseries.py is used instead, as a precision check)"""
import sys, json, time, os
import numpy as np
sys.path.insert(0, 'code')
import logseries_ld as LS
if len(sys.argv) > 7 and sys.argv[7] == 'dbl':
    import logseries as LS

A, Bd, N, amp, out, savedir = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5], sys.argv[6]
TS = [-40.0, -20.0, -10.0, -5.0, -2.0, -1.0, 0.0, 1.0, 2.0, 5.0, 10.0, 20.0, 40.0]
SAVE = set(range(20, N + 1, 20)) | {N}
os.makedirs(savedir, exist_ok=True)
t0 = time.time()
F, G, st, res = LS.run(A, Bd, {1: amp}, N, out=None)
print('run time', time.time() - t0, flush=True)
la = np.log10(amp)


def tvals(h, t):
    K = h.shape[1]
    acc = np.zeros(h.shape[0], dtype=np.clongdouble)
    for k in range(K - 1, -1, -1):
        acc = acc * np.longdouble(t) + h[:, k]
    ab = np.zeros(h.shape[0], dtype=np.longdouble)
    for k in range(K - 1, -1, -1):
        ab = ab * np.longdouble(abs(t)) + np.abs(h[:, k])
    return float(np.log10(np.abs(acc).sum())), float(np.log10(ab.sum()))


with open(out, 'w') as fh:
    for n in range(2, N + 1):
        d = dict(n=n, t=TS, lF=[], lFabs=[], lG=[], lGabs=[])
        for t in TS:
            a, b = tvals(F[n], t)
            d['lF'].append(a - n * la); d['lFabs'].append(b - n * la)
            if n in G:
                a, b = tvals(G[n], t)
                d['lG'].append(a - n * la); d['lGabs'].append(b - n * la)
        fh.write(json.dumps(d) + '\n')
        if n in SAVE:
            np.save(os.path.join(savedir, 'F_%d.npy' % n), F[n])
            if n in G:
                np.save(os.path.join(savedir, 'G_%d.npy' % n), G[n])
print('done', time.time() - t0, flush=True)
