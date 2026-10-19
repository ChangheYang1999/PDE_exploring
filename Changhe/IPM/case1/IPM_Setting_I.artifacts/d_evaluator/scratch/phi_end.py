import sys
exec(open('scratch/b3_clean_run.py').read().split("res = {}")[0])
be2 = 2 / A
print('   u        x      phi_mine        phi_lead     w            (x grid spacing %.3f at x*)' % (x[np.searchsorted(x, xs)] - x[np.searchsorted(x, xs) - 1]))
for u in np.concatenate([np.arange(0.5, 0.9, 0.05), np.arange(0.9, 1.0, 0.01), [0.995, 0.998]]):
    t = xs * u
    print('%6.3f %8.4f %14.6e %14.6e %10.4f' % (u, t, q_my(t) * (1 - u) ** (1 - be2), q_ld(t) * (1 - u) ** (1 - be2), np.interp(t, x, w)))
