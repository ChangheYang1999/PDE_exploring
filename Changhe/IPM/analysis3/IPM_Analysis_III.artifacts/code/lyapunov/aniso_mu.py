import numpy as np, sys
a = 3.5; bmax = 1.2
w = np.load('aniso_window_a%.2f_b%.2f.npz' % (a, bmax)); t, lo, hi = w['t'], w['lo'], w['hi']
target = -1.8 + (-8.5 + 1.8) * 0.5 * (1 - np.tanh((t - 1.6) / 0.6))
mup = np.minimum(np.maximum(target, lo + 0.4), hi - 0.4)
dt = t[1] - t[0]; n = 40; ker = np.exp(-0.5 * (np.arange(-n, n + 1) * dt / 0.15) ** 2); ker /= ker.sum()
mup = np.convolve(np.r_[np.full(n, mup[0]), mup, np.full(n, mup[-1])], ker, mode='valid')
np.save('aniso_mup.npy', mup)
print('mu\' range', mup.min(), mup.max(), 'violations lo:', (mup < lo).sum(), 'hi:', (mup > hi).sum())
