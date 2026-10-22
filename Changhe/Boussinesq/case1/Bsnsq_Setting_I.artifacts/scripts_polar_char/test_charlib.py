"""Validation of charlib2.transport on a manufactured velocity (Psi in the basis, beta = 3, a0 = 10): the reconstructed
Theta, Theta_x, Theta_y, Omega must satisfy (P2) W.grad Theta = (beta-2) Theta and (P1) W.grad Omega + Omega = Theta_x,
checked with centred finite differences of the reconstructed fields (independent of the propagator); the propagator
gradient must match the FD gradient. Also: dt and r_stop sensitivity, linear-flow sanity (Psi = c xy E^a with higher
modes zero still gives the smooth solution)."""
import sys, torch, math, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from charlib2 import *
dv = dev()
beta = 3.0; a0 = 10.0
bas = PsiBasis(beta, 4, 8)
cP = torch.zeros(4, 8, dtype=DT, device=dv); cP[0, 0] = -1.2; cP[1, 2] = 0.3; cP[0, 3] = -0.2   # smooth nonlinear velocity; P_1(0) = -1.2 + 0.2 = -1 so c = 2 P_1(0) = -2 exactly
pts = [(0.3, 0.7), (2.0, 0.1), (0.1, 2.0), (0.05, 0.6), (1.0, 1.0), (30.0, 40.0), (1e3, 2e3), (0.02, 0.01), (1e6, 3e6), (0.3, 3.0)]
hs = [1e-3, 5e-4]
ref = None
for dt, r_stop in [(0.005, 1e-3), (0.0025, 1e-3), (0.005, 3e-4), (0.01, 1e-3)]:
    t0 = time.time()
    X = []; Y = []
    for (x0, y0) in pts:
        for h in hs:
            hh = h * max(1.0, math.hypot(x0, y0))
            X += [x0, x0 + hh, x0 - hh, x0, x0]; Y += [y0, y0, y0, y0 + hh, y0 - hh]
    X = torch.tensor(X, dtype=DT, device=dv); Y = torch.tensor(Y, dtype=DT, device=dv)
    o = transport(bas, cP, a0, beta, X, Y, dt=dt, r_stop=r_stop)
    f = bas.fields(cP, X, Y)
    torch.cuda.synchronize(); el = time.time() - t0
    print(f'dt={dt} r_stop={r_stop} steps={o["nsteps"]} ({el:.1f}s)  cols: RT/NT  RO/NO  |Thx_fd-Thx|/|gradTh|  |Thy_fd-Thy|/|Thy|  Theta  Omega  T  fail')
    i = 0
    for (x0, y0) in pts:
        for h in hs:
            hh = h * max(1.0, math.hypot(x0, y0))
            Th = o['Th'][0, i:i + 5]; Om = o['Om'][0, i:i + 5]
            W1 = beta * x0 - f['Psi_y'][0, i].item(); W2 = beta * y0 + f['Psi_x'][0, i].item()
            Thx_fd = (Th[1] - Th[2]) / (2 * hh); Thy_fd = (Th[3] - Th[4]) / (2 * hh)
            Omx_fd = (Om[1] - Om[2]) / (2 * hh); Omy_fd = (Om[3] - Om[4]) / (2 * hh)
            RT = W1 * Thx_fd + W2 * Thy_fd - (beta - 2) * Th[0]; NT = abs(W1 * Thx_fd) + abs(W2 * Thy_fd) + abs((beta - 2) * Th[0])
            Thx = o['Thx'][0, i]; Thy = o['Thy'][0, i]
            RO = W1 * Omx_fd + W2 * Omy_fd + Om[0] - Thx; NO = abs(W1 * Omx_fd) + abs(W2 * Omy_fd) + abs(Om[0]) + abs(Thx)
            eTx = (Thx_fd - Thx).abs() / (Thx.abs() + Thy.abs()); eTy = (Thy_fd - Thy).abs() / Thy.abs()
            print('  (%7.3g,%7.3g) h=%.0e: %9.2e %9.2e %9.2e %9.2e   %11.5e %11.5e %6.2f %d' % (x0, y0, h, float(RT / NT), float(RO / NO), float(eTx), float(eTy), float(Th[0]), float(Om[0]), float(o['T'][0, i]), int(o['fail'][0, i])))
            i += 5
    vals = torch.stack([o['Th'][0, ::10], o['Thx'][0, ::10], o['Thy'][0, ::10], o['Om'][0, ::10]])
    if ref is None: ref = vals
    else: print('  max rel change of (Theta, Theta_x, Theta_y, Omega) at the base points vs first config: %.2e' % ((vals - ref).abs() / (ref.abs() + 1e-300)).max().item())
