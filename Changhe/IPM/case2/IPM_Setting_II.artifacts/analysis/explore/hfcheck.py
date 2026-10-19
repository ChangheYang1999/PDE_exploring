# Lead exploration (2026-10-18): finite-difference test of the high-frequency symbol of hfsym.py.
# Perturb log A by h * phi_j (x-even mode j) on a converged state, evolve to dg/ds < tol, and compare
#     D_j(theta) = [log Gt(a + h e_j) - log Gt(a)] / h      (log Gt = log A - 2 log|Xi|, mean removed)
# with the predicted principal part s(theta) phi_j(theta), s = 1 - 2 m1 (1 - exp(-Q)), after removing the low-frequency
# content (Fourier modes |n| < j/2) from both. Reports the relative L2 mismatch on |cos| > cut and the regression slope.
# Usage: python3 hfcheck.py state.npz p j1,j2,... [h=0.02] [Nmax=16]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); js = [int(v) for v in sys.argv[3].split(',')]
h = float(sys.argv[4]) if len(sys.argv) > 4 else 0.02
Nmax = int(sys.argv[5]) if len(sys.argv) > 5 else 16
hf = np.load(sys.argv[1].replace('.npz', '_hfsym.npz'))
lr, th = st['lr'], st['th']; g0 = st['g']; nA = len(hf['thA'])
cut = 0.05


def run(a):
    Af = FE.datum_fn(a, Nmax)
    g1, i1 = FE.evolve(p, Af, g0, lr, th, 300)
    steps = i1['steps']; dg = i1['dgds']
    while dg > 1e-8 and steps < 4000:
        g1, i2 = FE.evolve(p, Af, g1, lr, th, 100, tol=1e-8)
        steps += i2['steps']; dg = i2['dgds']
    ng = FE.node_and_G(p, Af, g1, lr, th, nA=nA)
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
    return lgt, ng['m1'], steps


def highpass(f, nmin):
    F = np.fft.rfft(f); F[:nmin] = 0
    return np.fft.irfft(F, len(f))


t0 = time.time()
base, m10, _ = run(np.zeros(Nmax))
thA = hf['thA']; s = hf['s']; w = np.abs(np.cos(thA)) > cut
for j in js:
    a = np.zeros(Nmax); a[j - 1] = h
    lj, m1j, steps = run(a)
    D = (lj - base) / h
    D = np.where(np.isfinite(D), D, 0.0)
    phi = FE.basis(thA, Nmax)[j - 1]
    pred = s * phi
    # the zeros of A make D singular-ish at +-90 deg; window by w before filtering (smooth taper)
    tap = np.clip((np.abs(np.cos(thA)) - cut) / 0.1, 0, 1)
    Dh = highpass(D * tap, j // 2); Ph = highpass(pred * tap, j // 2)
    slope = float(np.sum(Dh * Ph) / np.sum(Ph * Ph))
    mis = float(np.linalg.norm(Dh - Ph) / np.linalg.norm(Ph))
    # local comparison of the envelope: least squares fit D ~ s_fd(theta) phi in sliding windows of 2 periods
    print(json.dumps(dict(j=j, dm1=(m1j - m10) / h, steps=steps, slope=round(slope, 4), rel_mismatch=round(mis, 4),
                          wall=round(time.time() - t0))), flush=True)
    np.savez('runs/hfcheck_j%d.npz' % j, thA=thA, D=D, pred=pred, s=s)
