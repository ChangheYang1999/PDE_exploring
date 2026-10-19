# Lead: one-line band summary of c (lr<-6, -6..-2, >-2), half-disc model excess on lr<-8, log(G_lo/G_up) at lr -9, G_up at -11.
import sys, numpy as np
print('%-44s %6s %7s %7s %7s %7s %7s %8s %9s' % ('state', 'p', 'c', 'lr<-6', '-6..-2', '>-2', 'mod<-8', 'lGlo/up', 'G_up(-11)'))
for f in sys.argv[1:]:
    s = np.load(f, allow_pickle=True); g, lr, th, p = s['g'], s['lr'], s['th'], float(s['p']); r = np.exp(lr)
    up = np.sin(th) > 0; sel = np.abs(np.cos(th)) > 0.5
    rho = (r ** p)[:, None] * g; q = rho / np.maximum((r[:, None] * np.cos(th)[None, :]) ** 2, 1e-300)
    Gu = np.array([np.median(q[i][sel & up]) for i in range(len(lr))]); Gl = np.array([np.median(q[i][sel & ~up]) for i in range(len(lr))])
    net = 2 * (np.exp((p - 1) * lr)[:, None] * g * np.sin(3 * th)[None, :]).mean(axis=1)
    mod = 14 / (15 * np.pi) * (Gu - Gl) * r
    I = lambda a, b, y: np.trapz(y[(lr >= a) & (lr <= b)], lr[(lr >= a) & (lr <= b)])
    i11 = np.argmin(abs(lr + 11)); i9 = np.argmin(abs(lr + 9))
    print('%-44s %6.4f %7.4f %7.3f %7.3f %7.3f %7.3f %8.3f %9.3g' % (f.split('/')[-1][:44], p, np.trapz(net, lr), I(-15, -6, net), I(-6, -2, net), I(-2, 11, net), I(-15, -8, mod) - I(-15, -8, net), np.log(Gl[i9] / Gu[i9]), Gu[i11]))
