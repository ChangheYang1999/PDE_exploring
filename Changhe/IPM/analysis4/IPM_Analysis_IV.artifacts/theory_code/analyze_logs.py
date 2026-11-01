"""Growth diagnostics for the logarithmic series (lead). Input: jsonl from logseries.py."""
import sys, json, math
from math import lgamma, log, exp


def load(fn):
    return [json.loads(l) for l in open(fn)]


def main(fn, delta):
    rows = load(fn)
    print('n  K  root(a0)  root(E(t)) for t=1,10,100,1000  root(sum k! c_k)  max_k log10(k! c_k / c_0)')
    for r in rows:
        n = r['n']
        col = r['col']
        if n % 10 and n != rows[-1]['n']:
            continue
        a0 = col[0]
        out = []
        for t in (1.0, 10.0, 100.0, 1000.0):
            lE = max(log(c) + k * log(t) for k, c in enumerate(col) if c > 0)
            s = sum(exp(log(c) + k * log(t) - lE) for k, c in enumerate(col) if c > 0)
            lE += log(s)
            out.append(exp(lE / n))
        lk = [log(c) + lgamma(k + 1) for k, c in enumerate(col) if c > 0]
        m = max(lk)
        lF = m + log(sum(exp(x - m) for x in lk))
        rel = max((log(c) + lgamma(k + 1) - log(a0)) / log(10) for k, c in enumerate(col) if c > 0)
        print('%3d %2d  %.4f  %s  %.4f  %.2f' % (n, r['Kt'], a0 ** (1 / n), ' '.join('%.4f' % v for v in out),
                                                exp(lF / n), rel))
    print('needed for convergence at r = e^t: root(E(t)) < e^{delta t}:',
          ' '.join('%.3g' % math.exp(delta * t) for t in (1, 10, 100, 1000)))


if __name__ == '__main__':
    main(sys.argv[1], float(eval(sys.argv[2])))
