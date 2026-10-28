"""Certified uniform comparison of an upper plan U(alpha) with the fixed-shape polygonal witness I(alpha, a0)
(Theorem 4.5) on [1/200, 199/200], by the log-convexity procedure (verifier's 09_uniform_comparison).
mode thm34: U = right side of Theorem 3.4 (reflection orbits, m = 16).
mode thm35: U = right side of Theorem 3.5 (local term, compact reflection-orbit part, exterior circles), with one
exact exterior plan per (radial bin, phase) and shape group, chosen at the group's reference exponent.

For an upper segment [aU, bU] (consecutive upper nodes) with certified U(aU) <= A, U(bU) <= B, convexity of log U gives
log U(t) <= E(t) = ((bU-t) log A + (t-aU) log B)/(bU-aU).  For a lower sub-segment [x1, x2] of it, with neighbours
x0 < x1 < x2 < x3 in the same shape group and safe enclosures l(x) <= I(x,a0)/x <= u(x), convexity of log(I/x) gives
  log(I(t)/t) >= L1(t) = log l(x1) + (t-x1)/(x1-x0) (log l(x1) - log u(x0))   (t >= x1),
  log(I(t)/t) >= L2(t) = log l(x2) + (x2-t)/(x3-x2) (log l(x2) - log u(x3))   (t <= x2).
With a rational split point c in [x1, x2], phi_i(t) = E(t) - log t - L_i(t) is convex (affine minus log), so
max over [x1, c] of phi_1 and over [c, x2] of phi_2 are attained at the endpoints. Every evaluation is an Arb ball;
the bound is exp of the largest upper endpoint.  log(U(t)/I(t,a0)) <= that maximum for all t in [x1, x2].
"""
from flint import arb, fmpq, ctx
from fractions import Fraction as F
import json, sys, math
ctx.prec = 200
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('mode', choices=['thm34', 'thm35']); ap.add_argument('--nodes', default='nodes.json')
ap.add_argument('--upper', default='upper_n384.json', help='comma list of reflection-orbit node certificates')
ap.add_argument('--lower', default='lower_g', help='prefix of the polygon group certificates')
ap.add_argument('--far', default='far_g', help='prefix of the fixed-plan exterior-circle group certificates')
ap.add_argument('--tag', default='')
ARGS = ap.parse_args(); MODE = ARGS.mode
nodes = json.load(open(ARGS.nodes))
_rows = {}; _m = set()
for fn in ARGS.upper.split(','):
    _d = json.load(open(fn)); _m.add(_d['phase_intervals'])
    for r in _d['rows']: _rows[F(r['alpha'])] = r
assert len(_m) == 1
up = dict(phase_intervals=_m.pop(), rows=[_rows[k] for k in sorted(_rows)], cells_per_axis=ARGS.upper)
def q(f): return arb(fmpq(f.numerator, f.denominator))
UPN = [F(x) for x in nodes['upper']]
def upper_tables(gi):
    """Certified upper values at the upper nodes, for the plan family used in shape group gi."""
    if MODE == 'thm34':
        UPC = {F(r['alpha']): arb(r['safe_upper_C']) for r in up['rows']}
        UPD = {F(r['alpha']): arb(r['safe_upper_D']) for r in up['rows']}
        return UPC, UPD
    # Theorem 3.5: local term + phase-uniform (compact reflection-orbit part + exterior circles with the group's fixed plans)
    far = json.load(open(f'{ARGS.far}{gi}.json')); fr = {F(r['alpha']): r for r in far['rows']}
    m = up['phase_intervals']; assert far['phase_intervals'] == m and far['plan_reference_alpha'] == nodes['groups'][gi]['far_ref']
    sec = 1 / (arb.pi() / (4 * m)).cos(); UPC = {}; UPD = {}
    for r in up['rows']:
        x = F(r['alpha'])
        if x not in fr: continue
        a = q(x); f = fr[x]
        assert len(r['regular_grid']) == len(f['far_phase_intervals']) == m + 1
        vals = [arb(y) + arb(z) for y, z in zip(r['regular_grid'], f['far_phase_intervals'])]
        mx = vals[0]
        for v in vals[1:]: mx = arb.max(mx, v)
        A = ((a + 2) / 2).gamma() / (2 * arb.pi().sqrt() * ((a + 3) / 2).gamma())
        nearC = arb(r['near']); nearD = 2 * A * arb(2) ** (-a) / a + arb(1) / 2
        UPC[x] = arb((nearC + mx * sec).upper()); UPD[x] = arb((nearD + mx * sec).upper())
    return UPC, UPD
results = []
overall = {'C': None, 'D': None}
for gi, g in enumerate(nodes['groups']):
    d = json.load(open(f'{ARGS.lower}{gi}.json'))
    assert F(d['a']) == F(g['shape'])
    low = {F(r['alpha']): (arb(r['safe_decimal_lower_10_places']), arb(r['safe_decimal_upper_10_places'])) for r in d['rows']}
    X = [F(x) for x in g['nodes']]
    assert set(X) <= set(low) and all(x < y for x, y in zip(X, X[1:]))
    lh = {x: (low[x][0] / q(x)).lower() for x in X}; uh = {x: (low[x][1] / q(x)).upper() for x in X}
    lh = {x: arb(v) for x, v in lh.items()}; uh = {x: arb(v) for x, v in uh.items()}
    assert all(v > 0 for v in lh.values())
    s, e = F(g['start']), F(g['end'])
    UPC, UPD = upper_tables(gi)
    useg = [(a, b) for a, b in zip(UPN, UPN[1:]) if s <= a and b <= e]
    assert useg[0][0] == s and useg[-1][1] == e   # the upper segments cover the group interval
    gmax = {'C': None, 'D': None}
    for aU, bU in useg:
        for kind, UP in (('C', UPC), ('D', UPD)):
            lA, lB = UP[aU].log(), UP[bU].log()
            def E(t): return ((q(bU) - q(t)) * lA + (q(t) - q(aU)) * lB) / q(bU - aU)
            seg_best = None
            sub = [x for x in X if aU <= x <= bU]
            assert sub[0] == aU and sub[-1] == bU and len(sub) >= 2   # the lower sub-segments cover [aU, bU]
            for x1, x2 in zip(sub, sub[1:]):
                i = X.index(x1); assert 1 <= i and i + 2 < len(X)       # neighbours x0 < x1 and x3 > x2 exist
                x0 = X[i - 1]; x3 = X[i + 2]
                s1 = (lh[x1].log() - uh[x0].log()) / q(x1 - x0)
                s2 = (lh[x2].log() - uh[x3].log()) / q(x3 - x2)
                def L1(t): return lh[x1].log() + q(t - x1) * s1
                def L2(t): return lh[x2].log() + q(x2 - t) * s2
                # float crossing point, rounded to a rational inside [x1, x2]
                f1 = lambda t: float(L1(t).mid()); f2 = lambda t: float(L2(t).mid())
                lo_, hi_ = x1, x2
                if f1(x2) <= f2(x2): c = x2
                elif f1(x1) >= f2(x1): c = x1
                else:
                    for _ in range(40):
                        mid = (lo_ + hi_) / 2
                        if f1(mid) < f2(mid): lo_ = mid
                        else: hi_ = mid
                    c = F(float((lo_ + hi_) / 2)).limit_denominator(10**9)
                    c = min(max(c, x1), x2)
                vals = []
                for t, L in ((x1, L1), (c, L1), (c, L2), (x2, L2)):
                    phi = E(t) - q(t).log() - L(t)
                    vals.append((arb(phi.upper()), t))
                m, tm = max(vals, key=lambda p: float(p[0].mid()))
                assert all(not (v[0] > m) for v in vals)
                if seg_best is None or m > seg_best[0]: seg_best = (m, tm, x1, x2)
            ratio = seg_best[0].exp()
            results.append(dict(group=gi, shape=g['shape'], kind=kind, upper_segment=[str(aU), str(bU)],
                                log_ratio_upper=seg_best[0].str(20, more=True), ratio_upper=arb(ratio.upper()).str(15, more=True),
                                worst_point=str(seg_best[1]), worst_float=float(seg_best[1]),
                                nodal_ratio=[float((UP[aU] / q(aU) / lh[aU]).upper()), float((UP[bU] / q(bU) / lh[bU]).upper())]))
            if gmax[kind] is None or seg_best[0] > gmax[kind][0]: gmax[kind] = (seg_best[0], seg_best[1])
    for kind in 'CD':
        print(f'group {gi} [{g["start"]}, {g["end"]}] shape {g["shape"]}: {kind} ratio <= {float(arb(gmax[kind][0].exp().upper())):.6f} at t = {float(gmax[kind][1]):.5f}')
        if overall[kind] is None or gmax[kind][0] > overall[kind][0]: overall[kind] = (gmax[kind][0], gmax[kind][1], gi)
out = dict(method=__doc__, mode=MODE, reflection_cells=up.get('cells_per_axis'), rows=results,
           uniform={k: dict(log_ratio_upper=v[0].str(20, more=True), ratio_upper=float(arb(v[0].exp().upper())), at=float(v[1]), group=v[2]) for k, v in overall.items()})
json.dump(out, open(f'uniform_result_{MODE}{ARGS.tag}.json', 'w'), indent=1)
for k, v in overall.items(): print('UNIFORM', k, float(arb(v[0].exp().upper())), 'at', float(v[1]))
