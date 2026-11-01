"""Fit the growth of alpha_n = ||f_n||_l1 (and l2) from a run log.
Hypotheses: (G) geometric with power correction  alpha_n ~ C L^n n^{-a}  => ratio_n = L (1 - a/n + O(1/n^2))
            (F) factorial-type                   ratio_n ~ c n^s         => log ratio_n = log c + s log n
Reports L, a from a linear fit of ratio_n against 1/n on the last half of the data, the slope s of log ratio vs log n,
the smoothed 10-step ratio, and the root test. All quantities for the raw amplitude and normalized by alpha_1."""
import json, sys, math, numpy as np
def load(path):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    hdr = rows[0]; st = {r['n']: r for r in rows if 'n' in r and 'L2' in r}
    return hdr, st
def fit(path, key='l1', verbose=True):
    hdr, st = load(path); N = max(st); ns = np.array(sorted(st))
    lk = 'log10_' + key
    if all(lk in st[n] for n in ns):
        lv = np.array([st[n][lk] for n in ns]) * math.log(10); a1 = 10 ** st[1][lk]
        good = np.isfinite(lv); ns = ns[good]; lv = lv[good]; v = np.exp(np.clip(lv, -700, 700))
    else:
        v = np.array([st[n][key] for n in ns]); a1 = st[1][key]
        good = v > 0; ns = ns[good]; v = v[good]
        lv = np.log(v)
    ratio = np.exp(np.diff(lv)); rn = ns[1:]
    half = rn >= max(10, N // 2)
    # (G): ratio = L + B/n
    A = np.vstack([np.ones(half.sum()), 1.0 / rn[half]]).T
    (L, B), *_ = np.linalg.lstsq(A, ratio[half], rcond=None); a = -B / L if L != 0 else float('nan')
    resid_G = np.sqrt(np.mean((ratio[half] - (L + B / rn[half])) ** 2))
    # (F): log ratio = logc + s log n
    A2 = np.vstack([np.ones(half.sum()), np.log(rn[half])]).T
    (lc, s_), *_ = np.linalg.lstsq(A2, np.log(np.abs(ratio[half])), rcond=None)
    resid_F = np.sqrt(np.mean((np.log(np.abs(ratio[half])) - (lc + s_ * np.log(rn[half]))) ** 2))
    # smoothed ratio over 10 steps and root tests at the end
    lvd = dict(zip(ns.tolist(), lv.tolist()))
    def sm(n, w=10):
        if n in lvd and n - w in lvd: return math.exp((lvd[n] - lvd[n - w]) / w)
        return float('nan')
    root = math.exp(lv[-1] / ns[-1])
    out = {'file': path, 'N': int(N), 'key': key, 'alpha1': a1, 'L_fit': float(L), 'a_fit': float(a), 'rms_G': float(resid_G),
           's_fit(loglog slope of ratio)': float(s_), 'rms_F': float(resid_F), 'L_fit_normalized': float(L / a1),
           'ratio_last': float(ratio[-1]), 'smooth10_ratio_at_N': sm(int(ns[-1])), 'smooth10_ratio_at_N/2': sm(int(ns[-1]) // 2 + 0),
           'root_at_N': float(root), 'root_at_N_normalized': float(root / a1)}
    if verbose:
        print(f"{path}: N={N} key={key}  alpha1={a1:.4g}")
        print(f"   (G) ratio = L(1 - a/n): L={L:.6f}  a={a:.4f}  rms={resid_G:.2e}   normalized L/alpha1={L/a1:.6f}")
        print(f"   (F) ratio ~ c n^s      : s={s_:.4f}  rms(log)={resid_F:.2e}   [s near 0: geometric; s near 1: factorial]")
        print(f"   ratio_N={ratio[-1]:.6f}  smooth10 at N/2={sm(int(ns[-1])//2):.6f} at N={sm(int(ns[-1])):.6f}  root_N={root:.6f} (normalized {root/a1:.6f})")
    return out
if __name__ == '__main__':
    for p in sys.argv[1:]:
        for key in ('l1', 'l2'):
            try: fit(p, key)
            except Exception as e: print(p, key, 'ERR', e)
