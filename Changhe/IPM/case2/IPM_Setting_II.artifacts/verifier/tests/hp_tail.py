"""angular-tail resolution measure (as in V14(d)): max over |m| >= nt/2 - 6 of |xi_m| / max_m |xi_m| per radial decade."""
import sys, torch, numpy as np
sys.path.insert(0, 'code')
from polar_inverse import PolarGrid
for f in sys.argv[1:]:
    d = torch.load(f, weights_only=False)
    xi = d['xi'].cpu().numpy(); nt = d['nt']; G = PolarGrid(d['edges'], d['q'], nt)
    Xm = np.abs(np.fft.fft(xi, axis=1))/nt
    m = np.fft.fftfreq(nt, 1/nt)
    tail = Xm[:, np.abs(m) >= nt//2 - 6].max(1)/Xm.max(1)
    out = []
    for lo in (1e-6, 1e-4, 1e-2, 1, 1e2):
        i = (G.r >= lo) & (G.r < lo*100)
        if i.any(): out.append('[%.0e,%.0e) %.1e' % (lo, lo*100, tail[i].max()))
    print(f, 's=%.4f' % d['s'], ' '.join(out))
