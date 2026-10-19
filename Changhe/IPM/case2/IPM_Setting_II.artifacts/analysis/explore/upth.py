# Lead: spectral angular upsampling of a lead-format state (g on lr x th) to Nnew angles; keeps the other keys.
# Usage: python3 upth.py in.npz out.npz Nnew
import sys, numpy as np
d = dict(np.load(sys.argv[1])); g = d['g']; N = g.shape[1]; M = int(sys.argv[3])
G = np.fft.rfft(g, axis=1); Gp = np.zeros((g.shape[0], M // 2 + 1), complex); Gp[:, :N // 2] = G[:, :N // 2]
d['g'] = np.maximum(np.fft.irfft(Gp, M, axis=1) * (M / N), 0.0); d['th'] = 2 * np.pi * np.arange(M) / M
np.savez(sys.argv[2], **d); print('upsampled', N, '->', M, 'min g', float(d['g'].min()))
