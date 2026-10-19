"""Verifier scratch (shift 6): union of the unshifted map <tag>512 and the three phase-shifted maps <tag>ph0.25/0.5/0.75
(scratch/phase_scan.sh; same theta columns, radial grids offset by quarter steps). Per region (near P |X - P| < 0.5; lobe
r 8.5-9.0, theta 0.12-0.30): the sampled maximum of |R| / N_f on each map, and on the union per theta column the maximum
with a three-point parabolic refinement in r of the signed R / N_f around the largest |value|.
Usage: python3 phase_sup.py tag [tag ...]"""
import sys
import numpy as np
for tag in sys.argv[1:]:
    fs = [tag + '512'] + [tag + 'ph%s' % f for f in ('0.25', '0.5', '0.75')]
    D = [np.load('runs/audit/%s_resmap.npz' % f) for f in fs]
    th = D[0]['th']; P = float(D[0]['x_star'])
    for d in D[1:]:
        assert np.allclose(d['th'], th)
    lines = []
    for lab, rr, tt in (('nearP', (8.0, 9.2), (0.0, 0.06)), ('lobe', (8.5, 9.0), (0.12, 0.30))):
        per = []
        for f, d in zip(fs, D):
            r = d['r']; Nf = d['Nf']
            q = np.where(Nf > 0, np.abs(d['R']) / np.where(Nf > 0, Nf, 1), 0.0)
            X, Y = r[:, None] * np.cos(th)[None, :], r[:, None] * np.sin(th)[None, :]
            if lab == 'nearP':
                m = (X - P) ** 2 + Y ** 2 < 0.25
            else:
                m = (r[:, None] >= rr[0]) & (r[:, None] <= rr[1]) & (th[None, :] >= tt[0]) & (th[None, :] <= tt[1])
            per.append(float(np.where(m, q, -1).max()))
        best = (0, 0, 0)
        for j in np.where((th >= tt[0]) & (th <= tt[1]))[0]:
            if j == 0:
                continue
            rs = np.concatenate([d['r'] for d in D]); qs = np.concatenate([np.where(d['Nf'][:, j] > 0, d['R'][:, j] / np.where(d['Nf'][:, j] > 0, d['Nf'][:, j], 1), 0) for d in D])
            o = np.argsort(rs); rs, qs = rs[o], qs[o]
            X, Y = rs * np.cos(th[j]), rs * np.sin(th[j])
            m = ((X - P) ** 2 + Y ** 2 < 0.25) if lab == 'nearP' else ((rs >= rr[0]) & (rs <= rr[1]))
            idx = np.where(m)[0]
            if len(idx) < 3:
                continue
            i = idx[np.argmax(np.abs(qs[idx]))]
            v = abs(qs[i])
            if 0 < i < len(rs) - 1:
                a, b, c = qs[i - 1], qs[i], qs[i + 1]
                den = a - 2 * b + c
                if den != 0:
                    v = abs(b - (a - c) ** 2 / (8 * den))
            if v > best[0]:
                best = (v, rs[i], th[j])
        lines.append('%s per-map %s spread %.1f%% | union+parab %.4e (r %.4f th %.4f)' % (
            lab, ' '.join('%.4e' % x for x in per), 100 * (max(per) - min(per)) / max(per), *best))
    print(tag, ' || '.join(lines))
