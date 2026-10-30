#!/usr/bin/env python3
"""Per-probe FLOAT statement (registered 25 probes) new vs old: value_old -> value_new (xfactor). Values = m lower-bound proxy of weak_tests3."""
import json, sys
def load(tag): return json.load(open(f'candD2/{tag}_weaktests3.json'))
def val(d, n, K):
    p = d['probes'][f'{n}:{K}']
    return p['m_lower_bound']
old_tag, new_tag, label = sys.argv[1], sys.argv[2], sys.argv[3]
o, nw = load(old_tag), load(new_tag)
k0 = list(o['probes'].values())[0].keys()
out = []; dec = inc = 0; facs = []
for n in (19, 23, 25, 29, 31):
    for K in (600, 900, 1200, 1800, 2400):
        a, b = val(o, n, K), val(nw, n, K)
        f = b / a; facs.append(((n, K), f))
        dec += f < 1; inc += f > 1
        out.append(f'({n}, {K}) {a:.2e} -> {b:.2e} (x{f:.2f})')
print(f'{label}: ' + '; '.join(out))
fs = sorted(facs, key=lambda t: t[1])
print(f'  decreases {dec}, increases {inc}; min factor {fs[0][1]:.4f} at {fs[0][0]}, max {fs[-1][1]:.4f} at {fs[-1][0]}')
hi = [(k, f) for k, f in facs if k[1] >= 1800]
print('  K >= 1800 factors: ' + ', '.join(f'{k} {f:.4f}' for k, f in hi))
largest = max((((n, K), val(nw, n, K)) for n in (19, 23, 25, 29, 31) for K in (600, 900, 1200, 1800, 2400)), key=lambda t: t[1])
print(f'  largest new value {largest[1]:.3e} at {largest[0]}; keys: {list(k0)}')
