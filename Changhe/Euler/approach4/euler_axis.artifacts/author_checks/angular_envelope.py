"""Lead check: relative angular coefficient envelopes of the frozen T1 ladder exports L1 and L2.

Envelope(n) = max over radial columns of |native coefficient(n, .)| in each element, divided by the element maximum.
Native normalizations differ between elements, so only within-element ratios are compared. Reads the frozen exports
(read only) and writes checks/angular_envelope_output.json.
"""
import json, numpy as np
BASE = 'independent_validation/external_exports/'
EXPORTS = {'L1': 'T1_ladder_L1_20261028T232238Z', 'L2': 'T1_ladder_L2_20261028T235434Z'}
out = {}
for tag, d in EXPORTS.items():
    z = np.load(BASE + d + '/coeffs.npz')
    meta = json.loads(str(z['meta_json']))
    els = meta['elements']
    res = {}
    for i, el in enumerate(els):
        labels = el['labels']
        for f in ('phi', 'q'):
            c = z[f'{f}_el{i}']
            cols = el.get(f + '_cols')
            lab = [labels[j] for j in cols] if cols is not None else labels
            assert len(lab) == len(c), (tag, i, f, len(lab), len(c))
            env = {}
            for (n, k), v in zip(lab, c):
                env[int(n)] = max(env.get(int(n), 0.0), abs(float(v)))
            m = max(env.values())
            nmax = max(env)
            rel = {n: env[n] / m for n in sorted(env)}
            # dominant parity: phi odd, q even in the leading part
            par = 1 if f == 'phi' else 0
            top = [n for n in rel if n % 2 == par]
            res[f'{f}_el{i}'] = dict(nmax=nmax, max=m,
                                     rel_at_top_dominant=max(rel[n] for n in top if n >= nmax - 4),
                                     rel_at_top_other=max(rel[n] for n in rel if n % 2 != par and n >= nmax - 4),
                                     rel_mid_dominant=max(rel[n] for n in top if nmax // 2 - 2 <= n <= nmax // 2 + 2),
                                     rel=rel)
    out[tag] = res
for tag, res in out.items():
    for k, v in res.items():
        print(tag, k, 'nmax', v['nmax'], 'top4 dominant %.2e other %.2e  mid %.2e' % (v['rel_at_top_dominant'], v['rel_at_top_other'], v['rel_mid_dominant']))
json.dump(out, open('checks/angular_envelope_output.json', 'w'), indent=1)
