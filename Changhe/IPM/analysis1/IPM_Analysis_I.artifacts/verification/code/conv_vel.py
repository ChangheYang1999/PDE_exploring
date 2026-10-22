import numpy as np, time
from x3rho import Trial
from x3vel import Modes, velocity_at
T = Trial()
rt = np.array([1e-2, 0.5, 3.0, 8.6, 20.0, 300.0, 1e4, 1e6, 7.65e6])
tht = np.array([0.0, 0.1, 0.7, 1.3, 1.55, np.pi / 2])
ref = None
for nth, nm, npt in ((512, 200, 12), (1024, 400, 16), (2048, 800, 16), (1024, 400, 24)):
    M = Modes(T, nth=nth, nmodes=nm)
    t0 = time.time()
    o = velocity_at(M, rt, tht, npt=npt)
    U = np.stack([o['U1'], o['U2']])
    if ref is None:
        ref = U
    else:
        print('nth=%d nm=%d npt=%d: max |U - U_prev| / (1+|U|) per radius:' % (nth, nm, npt),
              ' '.join('%.1e' % v for v in (np.abs(U - ref) / (1 + np.abs(ref))).max(axis=(0, 2))), ' (%.1fs)' % (time.time() - t0))
        ref = U
np.set_printoptions(precision=15, linewidth=200)
print('U1 at theta=0 (axis):', ref[0][:, 0])
print('U2 at theta=pi/2:', ref[1][:, -1])
print('U2 at theta=0 (must be 0):', ref[1][:, 0], ' U1 at pi/2 (must be 0):', ref[0][:, -1])
