"""V232: adds the kmax-40 repeat PLM1024Ak6 / PLM1024Ak7 (notes of the numerical researcher 23:40Z; notes of the lead analyst 23:32Z (4)).
V225 (extends tests/v215_plm256.py, V211): adds the 1024-angle pair PLM1024Ae6 / PLM1024Ae7 (base ES1024_base);
V211: the numerics core-frozen slaved b1 columns at 256 angles PLM256e6 / PLM256e7 (eps_rel 3e-6 / 1e-6, lrcut -8,
lrw 1; notes of the numerical researcher 22:21Z item 2) against the 512-angle pair PLM1e6 / PLM1e7 (V193), read only:
Hessenberg least-squares residual recomputed from the stored H, y, beta; band shares of v = dg/scale; column values and
their row-subset agreement under both reference columns; the acceptance rule (true residual < 0.1 and agreement within
10 % between the two eps)."""
import numpy as np, json, os
P = 'runs/pfwd/'
B = {256: np.load(P + 'par/ES256_base.npz', allow_pickle=True), 512: np.load(P + 'bn/DR512_a2-1.000_it0.npz'),
     1024: np.load(P + 'par/ES1024_base.npz', allow_pickle=True)}
tags = [(t, n) for t, n in (('PLM256e6', 256), ('PLM256e7', 256), ('PLM1e6', 512), ('PLM1e7', 512), ('PLM1024Ae6', 1024),
                            ('PLM1024Ae7', 1024), ('PLM1024Ak6', 1024), ('PLM1024Ak7', 1024))
        if os.path.exists(P + 'par/%s_resp_b1.npz' % t) and os.path.exists(P + 'par/%s.out' % t)]
C, R = {}, {}
for t, n in tags:
    b = B[n]; lr = b['lr']; r = np.exp(lr)
    p = float(b['x'][-1]) if n in (256, 1024) else float(json.loads(str(b['args']))['p'])
    scale = (r**2 / (1 + r**2))**(1 - p / 2)
    d = np.load(P + 'par/%s_resp_b1.npz' % t)
    out = [json.loads(l) for l in open(P + 'par/%s.out' % t) if l.startswith('{')]
    lc = [o['lin_col'] for o in out if 'lin_col' in o]
    cv = [o['col_values'] for o in out if 'col_values' in o]
    if not lc or not cv:
        print(t, 'record incomplete'); continue
    R[t] = lc[0]; C[t] = np.array(cv[0])
    H, y, be = d['H'], d['y'], float(d['beta'])
    e1 = np.zeros(H.shape[0]); e1[0] = be
    sv = np.linalg.svd(H, compute_uv=False)
    print('%s (%d angles, p %.6f): eps_rel %g resid_true %.4f resid_tsvd %.4f (recomputed %.4f) resid_full %.4f '
          'resid_core %.4f n_kept %d H_sv %.4g .. %.4g (record %s .. %s)' % (t, n, p, R[t]['eps_rel'], R[t]['resid_true'],
          R[t]['resid_tsvd'], np.linalg.norm(e1 - H @ y) / be, R[t]['resid_full'], R[t]['resid_core'], R[t]['n_kept'],
          sv[0], sv[-1], R[t]['H_sv'][0], R[t]['H_sv'][-1]))
    v = d['dg'].astype(float) / scale[:, None]; tot = (v**2).sum()
    sh = [(v[(lr >= lo) & (lr < hi)]**2).sum() / tot for lo, hi in [(-14, -12), (-12, -10), (-10, -8.5), (-8.5, -8),
          (-8, -4), (-4, 0), (0, 4), (4, 10.01)]]
    vm = v[:, ::-1]; ev = ((v + np.roll(vm, 1, axis=1))**2).sum() / 4 / tot
    print('   |v| %.4e (record v_norm %.4e); |v|^2 by lr band [-14,-12) [-12,-10) [-10,-8.5) [-8.5,-8) [-8,-4) [-4,0) '
          '[0,4) [4,10]:' % (np.sqrt(tot), R[t]['v_norm']), ' '.join('%.4f' % s for s in sh))
    c = C[t]
    print('   rows: x-even 0-16 share %.4f; b_1..b_16 (17-32) norm %.4f; D_ax %.4f M_up %.4f M_dn %.4f psi_yy0 %.4f'
          % ((c[:17]**2).sum() / (c**2).sum(), np.linalg.norm(c[17:33]), c[33], c[34], c[35], c[36]))
def cmp(a, c):
    x, y = C[a], C[c]
    out = []
    for nm, sl in (('all 37', slice(0, 37)), ('b rows 17-32', slice(17, 33)), ('moment rows 33-36', slice(33, 37))):
        xa, ya = x[sl], y[sl]
        out.append('%s: |a-c|/|a| %.3f, |a-c|/|c| %.3f, cos %.4f' % (nm, np.linalg.norm(xa - ya) / np.linalg.norm(xa),
                   np.linalg.norm(xa - ya) / np.linalg.norm(ya), xa @ ya / np.linalg.norm(xa) / np.linalg.norm(ya)))
    flips = [i for i in range(17, 37) if x[i] * y[i] < 0 and max(abs(x[i]), abs(y[i])) > 0.1 * np.abs(x[17:]).max()]
    print('%s vs %s:' % (a, c), '; '.join(out), '| sign changes in rows (|value| > 10 %% of max):', flips)
for a, c in (('PLM256e6', 'PLM256e7'), ('PLM1e6', 'PLM1e7'), ('PLM1024Ae6', 'PLM1024Ae7'), ('PLM256e6', 'PLM1e6'),
             ('PLM256e7', 'PLM1e7'), ('PLM1024Ae6', 'PLM1e6'), ('PLM1024Ae7', 'PLM1e7'), ('PLM1024Ae6', 'PLM256e6'), ('PLM1024Ae7', 'PLM256e7'),
             ('PLM1024Ak6', 'PLM1024Ak7'), ('PLM1024Ak6', 'PLM1024Ae6'), ('PLM1024Ak7', 'PLM1024Ae7')):
    if a in C and c in C: cmp(a, c)
for a, c in (('PLM256e6', 'PLM256e7'), ('PLM1e6', 'PLM1e7'), ('PLM1024Ae6', 'PLM1024Ae7'), ('PLM1024Ak6', 'PLM1024Ak7')):
    if a in C and c in C:
        ok_r = R[a]['resid_true'] < 0.1 and R[c]['resid_true'] < 0.1
        dd = np.linalg.norm(C[a] - C[c]) / min(np.linalg.norm(C[a]), np.linalg.norm(C[c]))
        print('rule for the pair %s / %s:' % (a, c), ' residuals < 0.1: %s; agreement %.3f (bar 0.10): %s' % (ok_r, dd, ok_r and dd < 0.1))
