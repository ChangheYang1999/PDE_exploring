"""Growth diagnostics for the logarithmic series with amplitude rescaling (lead).
Input: jsonl from run_logseries_amp.py (coefficients of the series with f_1 = amp*sin(theta)); unit-amplitude
coefficients are col/amp^n. Usage: analyze_logs2.py file.jsonl a b amp"""
import sys, json, math
from math import lgamma, log, exp, log10


def lse(xs):
    m = max(xs)
    return m + log(sum(exp(x - m) for x in xs))


def main(fn, a, b, amp, every=20):
    rows = [json.loads(l) for l in open(fn)]
    delta = a / b
    s = 4 * b
    nr = 2 * b // math.gcd(a, 2)
    h = a // math.gcd(a, 2)
    eps = 1 if h == 1 else 0
    print('delta=%d/%d n_r=%d eps=%d s=4b=%d amp=%g' % (a, b, nr, eps, s, amp))
    print('  n  K kap  M^(1/n)  a0^(1/n)  !s^(1/n)  maxk_log10(k!s^k c_k/c_0)  log10(c_K/c_0)  slope  beta')
    out = []
    for r in rows:
        n, col = r['n'], r['col']
        lc = [(k, log(c) - n * log(amp)) for k, c in enumerate(col) if c > 0]
        kap = max(0, (n - 1) // nr - eps)
        lM = lse([x for _, x in lc])
        la0 = lc[0][1] if lc[0][0] == 0 else float('-inf')
        lfs = lse([x + lgamma(k + 1) + k * log(s) for k, x in lc])
        rel = max((x + lgamma(k + 1) + k * log(s) - la0) / log(10) for k, x in lc)
        K = r['Kt']
        lK = dict(lc).get(K, float('nan'))
        # fit log c_k - log c_0 = k*log q - beta*log k!  (least squares over k>=1)
        pts = [(k, x - la0) for k, x in lc if k >= 1]
        beta = slope = float('nan')
        if len(pts) >= 3:
            # two-parameter fit y = k*u - beta*lgamma(k+1)
            S11 = sum(k * k for k, _ in pts); S12 = sum(k * lgamma(k + 1) for k, _ in pts)
            S22 = sum(lgamma(k + 1) ** 2 for k, _ in pts)
            T1 = sum(k * y for k, y in pts); T2 = sum(lgamma(k + 1) * y for k, y in pts)
            det = S11 * S22 - S12 * S12
            u = (T1 * S22 - T2 * S12) / det
            mb = (S11 * T2 - S12 * T1) / det
            slope, beta = u / log(10), -mb
        rec = dict(n=n, K=K, kappa=kap, M_root=exp(lM / n), a0_root=exp(la0 / n), fact_root=exp(lfs / n),
                   max_rel_fact=rel, top_rel=(lK - la0) / log(10), slope=slope, beta=beta)
        out.append(rec)
        if n % every == 0 or n == rows[-1]['n']:
            print('%4d %2d %3d  %.4f  %.4f  %.4f  %8.2f  %9.2f  %6.3f %6.3f' % (n, K, kap, rec['M_root'], rec['a0_root'],
                  rec['fact_root'], rel, rec['top_rel'], slope, beta))
    return out


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))
