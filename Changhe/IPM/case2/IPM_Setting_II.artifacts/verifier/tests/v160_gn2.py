"""V160: FR item 23 (b891b886, the GN2_e3 sentence of 5.8 Scope). Recomputes from the stored iterates of the numerical researcher
(read-only: numerics/runs/pfwd/gn/GN2_e3_it0..5.npz, GN2_e3_H1..5.npz, GN2_e3.log, runs/pfwd/bn/DF256_a2-1.000_it0.npz)
with own numpy code: the residual 2-norm |(g - Tg)/scale| (scale = (r^2/(1 + r^2))^(1 - p/2) per radius, as defined in
the run), the masked relative defect, the x-odd part of g relative to the x-even part (own reflection th -> pi - th on
the stored angle grid), the start perturbation g_0 = g_fix (1 + 1e-3 cos th), the line-search factors and the linear
predictions |R + f J d| from the saved Hessenberg matrices.
"""
import json, math
import numpy as np
NUM = '../numerics/'
ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

logrec = [json.loads(l) for l in open(NUM + 'runs/pfwd/gn/GN2_e3.log') if l.startswith('{')]
head = logrec[0]; st = [r for r in logrec[1:] if 'R2' in r]; steps = [r for r in logrec[1:] if 'gmres_k' in r]
p = head['p']
rep('L0 run options: 256 angles, kmax 30, eps_rel 1e-2, maxit 5, eps_odd 1e-3, odd_mode 1 (cos th)',
    head['Nth'] == 256 and head['opt']['kmax'] == 30 and head['opt']['eps_rel'] == 0.01 and head['opt']['maxit'] == 5
    and head['opt']['eps_odd'] == 1e-3 and head['opt']['odd_mode'] == 1, head['opt'])
fix = np.load(NUM + head['state'], allow_pickle=True)
hfix = json.loads(str(fix['hist']))[-1]
rep('L1 start state %s: exit_defect %.3g (FR "8e-5"), m1 %.4f' % (head['state'], hfix['exit_defect'], hfix['m1']), abs(hfix['exit_defect'] - 8e-5) < 0.5e-5)
th = fix['th']; N = len(th); dth = 2*math.pi/N
# reflection x -> -x: th -> pi - th (mod 2 pi) on the grid th_j = th_0 + j dth
jj = np.arange(N); tgt = (math.pi - th) % (2*math.pi); flip = np.rint((tgt - th[0])/dth).astype(int) % N
rep('L2 grid closed under th -> pi - th', np.allclose(np.cos(th[flip]), np.cos(math.pi - th)) and np.allclose(np.sin(th[flip]), np.sin(math.pi - th)), 'th_0 = %.6f' % th[0])
gfix = fix['g']
oddfix = 0.5*(gfix - gfix[:, flip]); evfix = 0.5*(gfix + gfix[:, flip])
print('   x-odd part of the fixed point: %.2e (relative rms)' % math.sqrt((oddfix**2).mean()/(evfix**2).mean()))
R2 = []; drm = []; godd = []; exits = []
for it in range(6):
    d = np.load(NUM + 'runs/pfwd/gn/GN2_e3_it%d.npz' % it, allow_pickle=True)
    g = d['g']; Tg = d['Tg']; lr = d['lr']; r = np.exp(lr)
    if it == 0:
        g0 = gfix*(1 + 1e-3*np.cos(th))[None, :]
        rep('L3 it0 = fixed point x (1 + 1e-3 cos th)', np.abs(g - np.clip(g0, 0, None)).max() <= 1e-12*np.abs(g0).max(), '%.1e' % np.abs(g - g0).max())
    scale = ((r**2/(1 + r**2))**(1 - p/2))[:, None]
    R2.append(float(np.linalg.norm((g - Tg)/scale)))
    rowmax = g.max(axis=1, keepdims=True); msk = g > 1e-3*rowmax
    dd = np.where(msk, np.abs(Tg - g)/rowmax, 0.0); drm.append(float(math.sqrt((dd**2).sum()/msk.sum())))
    go = 0.5*(g - g[:, flip]); ge = 0.5*(g + g[:, flip]); godd.append(float(math.sqrt((go**2).mean()/(ge**2).mean())))
    info = json.loads(str(d['info'])); exits.append((info['th1_deg'], info['th2_deg']))
    print('   it %d: |R|_2 %.2f (log %.2f), defect rms %.3e (log %.3e), x-odd rel rms %.3e (log %.3e), exits %.3f / %.3f'
          % (it, R2[-1], st[it]['R2'], drm[-1], st[it]['defect_rms'], godd[-1], st[it]['godd_rel_rms'], *exits[-1]), flush=True)
rep('L4 |R|_2, defect rms, x-odd rms recomputed = logged (relative 1e-6)',
    all(abs(R2[i] - st[i]['R2']) < 1e-6*st[i]['R2'] and abs(drm[i] - st[i]['defect_rms']) < 1e-6*st[i]['defect_rms']
        and abs(godd[i] - st[i]['godd_rel_rms']) < 1e-6*st[i]['godd_rel_rms'] for i in range(6)))
rep('L5 residual norm 17411 -> 10140 in five steps: -%.1f %% (FR "42 %%")' % (100*(1 - R2[5]/R2[0])), round(100*(1 - R2[5]/R2[0])) == 42)
rep('L6 final defect rms %.3e (FR "2.05e-3")' % drm[5], round(drm[5], 5) == 0.00205)
rep('L7 x-odd part: start %.2e, max %.2e (it %d), final %.2e (FR "4.3e-4 rms after a rise to 2.2e-3")' % (godd[0], max(godd), int(np.argmax(godd)), godd[5]),
    round(godd[5], 5) == 0.00043 and round(max(godd), 4) == 0.0022)
rep('L8 final strong exits %.4f / %.4f deg: within 0.02 deg of 90 / 270' % exits[5], abs(exits[5][0] - 90) < 0.02 and abs(exits[5][1] - 270) < 0.02)
# linear predictions from the saved Hessenberg matrices: |R + f J d|/|R| = |beta e1 (1 - f) + f (beta e1 - H y)|/beta (GMRES model)
fr = []
for k, s in enumerate(steps, start=1):
    H = np.load(NUM + 'runs/pfwd/gn/GN2_e3_H%d.npz' % k)
    Hk = H['H']; beta = float(H['beta']); y = H['y']; e1 = np.zeros(Hk.shape[0]); e1[0] = beta
    res = e1 - Hk @ y
    f = s['step_fac']; pred_f = np.linalg.norm((1 - f)*e1 + f*res)/beta; pred_1 = np.linalg.norm(res)/beta
    real = s['R2_new']/st[k - 1]['R2']
    fr.append((f, pred_1, pred_f, real))
    print('   step %d: accepted factor %.3g (full step rejected: %s), linear model |R_new|/|R| %.3f at the full step, %.3f at the accepted factor, realised %.3f'
          % (k, f, f < 1, pred_1, pred_f, real))
rep('L9 in every step the full Newton step was rejected (accepted factors %s)' % [x[0] for x in fr], all(x[0] < 1 for x in fr))
rep('L10 realised decrease below the GMRES linear model at the accepted factor in every step', all(x[3] > x[2] for x in fr),
    ['%.2f vs %.2f' % (1 - x[3], 1 - x[2]) for x in fr])
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
