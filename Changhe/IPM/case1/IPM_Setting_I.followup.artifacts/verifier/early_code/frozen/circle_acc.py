# Accuracy control for the circle spectra: recompute v on r = 1 at doubled resolution, tol 1e-25, larger t cutoff.
import sys, json, numpy as np
sys.path.insert(0, 'code/frozen')
import vpacket as V
N = 128
res = {}
for (A, g) in [(3.0, 5.5), (10.15, 29.75)]:
    th = (np.arange(N)+0.5)*np.pi/(2*N)
    specs = []
    for (rs, tol, omc) in [(1.0, 1e-21, 1200.0), (2.0, 1e-25, 2000.0)]:
        V.OMC = omc
        P = V.Packet(A, g, tol=tol, res=rs)
        f = np.array([P.eval(np.cos(a), [np.sin(a)])[0][0] for a in th])
        full = np.concatenate([f, -f[::-1], f, -f[::-1]])
        c = np.fft.rfft(full)/len(full)
        specs.append((f, c))
    (f1, c1), (f2, c2) = specs
    ks = [10, 20, 40, 60, 100, 140, 200, 250]
    m = np.abs(c1).max()
    print('A=%g g=%g  max|f1-f2|/max|f| = %.2e' % (A, g, np.abs(f1-f2).max()/np.abs(f1).max()))
    print('   k      |c_k|/max (base)   |c_k|/max (fine)   |diff|/max')
    for k in ks:
        print('   %3d    %.4e        %.4e         %.2e' % (k, abs(c1[k])/m, abs(c2[k])/m, abs(c1[k]-c2[k])/m))
    # local power-law exponent of the tail
    kk = np.arange(20, 250); cc = np.abs(c2[kk])/m
    for (a, b2) in [(20, 40), (40, 80), (80, 160), (120, 240)]:
        sel1 = np.abs(c2[a-2:a+3]).max(); sel2 = np.abs(c2[b2-2:b2+3]).max()
        print('   envelope slope k=%d..%d: %.2f' % (a, b2, np.log(sel2/sel1)/np.log(b2/a)))
    res['%g_%g' % (A, g)] = dict(maxdiff=float(np.abs(f1-f2).max()/np.abs(f1).max()),
                                 spec_base=[float(abs(c1[k])/m) for k in ks], spec_fine=[float(abs(c2[k])/m) for k in ks], ks=ks)
json.dump(res, open('runs/frozen_circle_acc.json', 'w'), indent=1)
