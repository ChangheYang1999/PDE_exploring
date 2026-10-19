"""Verifier scratch (shift 8): readings of 49 dom9000g2 (lead NOTES 2026-10-18T23:22:40Z item 2) and 50 c6h9000 (lead NOTES
2026-10-19T00:16:58Z item 2) on my audits. Prints, per configuration and file pair, the N_f / N_v maxima with argmax (r in L
units and theta) for the regions given, and ratios A/B.
Usage: python3 read4950.py A sufA B sufB cfg[,cfg...] region[;region...]"""
import sys, json, os
A, sA, B, sB, cf, rg = sys.argv[1:7]
D = 'runs/audit/'


def load(t, c, s):
    f = D + '%s_%s_R7.652e6%s.json' % (t, c, s)
    return json.load(open(f)) if os.path.exists(f) else None


def L_of(d):
    return d.get('vcand', {}).get('L') if isinstance(d.get('vcand'), dict) else None


for c in cf.split(','):
    a, b = load(A, c, sA), load(B, c, sB)
    if a is None or b is None:
        print('%s: missing %s%s %s %s%s %s' % (c, A, sA, a is None, B, sB, b is None)); continue
    ra = {r['region']: r for r in a['residual']}; rb = {r['region']: r for r in b['residual']}
    print('== %s  %s%s / %s%s' % (c, A, sA, B, sB))
    for g in rg.split(';'):
        # region names of bands contain the physical radii; match by prefix of the L-unit band if given as 'band:a:b'
        if g.startswith('band:'):
            lo, hi = g.split(':')[1:3]
            def find(rr):
                for k in rr:
                    if '<r<=' in k:
                        p, q = k.split('<r<=')
                        q2 = q.split(',')[0]
                        tail = k[len(p) + 4 + len(q2):]
                        if tail == (',ya>=0.006' if g.endswith(':ya') else ''):
                            try:
                                if abs(float(p) / 7.6514 - float(lo)) < 0.01 * float(lo) and (q2 == hi == 'inf' or (hi != 'inf' and q2 != 'inf' and abs(float(q2) / 7.6514 - float(hi)) < 0.01 * float(hi))):
                                    return rr[k]
                            except ValueError:
                                pass
                return None
            x, y = find(ra), find(rb)
        else:
            x, y = ra.get(g), rb.get(g)
        if x is None or y is None:
            print('  %-28s missing' % g); continue
        print('  %-28s Nf %.4e / %.4e = %.3f (A at r %.4g th %.4f; B at r %.4g th %.4f)   Nv %.4e / %.4e = %.3f (A at r %.4g th %.4f)' % (
            g, x['flux_max'], y['flux_max'], x['flux_max'] / y['flux_max'], x['flux_argmax_r'], x['flux_argmax_theta'],
            y['flux_argmax_r'], y['flux_argmax_theta'], x['Nv_max'], y['Nv_max'], x['Nv_max'] / y['Nv_max'], x['Nv_argmax_r'],
            x['Nv_argmax_theta']))
