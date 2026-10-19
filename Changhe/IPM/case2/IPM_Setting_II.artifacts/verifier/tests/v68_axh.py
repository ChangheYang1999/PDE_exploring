"""V68: axis profile of h = r^(p-2) g_thth on both half-axes of a saved own-format state (rho, r, th, p), by FFT (spectral) and by
the local second difference over +-1, +-2 grid angles (no global spectral sum), next to g on the axis and max g in the window.
CPU only. Usage: python3 tests/v68_axh.py STATE.npz"""
import sys, math, json, numpy as np
d = np.load(sys.argv[1], allow_pickle=True)
rho, r, th, p = d['rho'], d['r'], d['th'], float(d['p']); nt = len(th); dth = 2*math.pi/nt
g = rho/r[:, None]**p
mm = np.fft.fftfreq(nt, 1.0/nt); mm[nt//2] = 0
out = dict(state=sys.argv[1].split('/')[-1], nt=nt)
for name, ths in (('upper', math.pi/2), ('lower', 3*math.pi/2)):
    j0 = int(round((ths - th[0])/dth)) % nt
    assert abs((th[j0] - ths + math.pi) % (2*math.pi) - math.pi) < 1e-9, 'axis not on the grid'
    fh = np.fft.fft(g, axis=1)/nt; fh[:, nt//2] = 0
    gtt_sp = np.real(fh @ (np.exp(1j*mm*(ths - th[0]))*(1j*mm)**2))
    gm1, g0, gp1 = g[:, (j0 - 1) % nt], g[:, j0], g[:, (j0 + 1) % nt]
    gm2, gp2 = g[:, (j0 - 2) % nt], g[:, (j0 + 2) % nt]
    gtt_1 = (gp1 - 2*g0 + gm1)/dth**2
    gtt_2 = (gp2 - 2*g0 + gm2)/(2*dth)**2
    rows = []
    for t in (-11.5, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, 0, 4, 9):
        i = int(np.argmin(np.abs(np.log(r) - t)))
        sc = r[i]**(p - 2)
        rows.append(dict(t=round(float(np.log(r[i])), 2), log_h_sp=None if gtt_sp[i] <= 0 else round(math.log(sc*gtt_sp[i]), 3),
                         sign_sp=int(np.sign(gtt_sp[i])), log_h_fd1=None if gtt_1[i] <= 0 else round(math.log(sc*gtt_1[i]), 3),
                         log_h_fd2=None if gtt_2[i] <= 0 else round(math.log(sc*gtt_2[i]), 3),
                         g_axis_over_g1=float('%.3g' % (g0[i]/max(abs(gp1[i]), 1e-300))),
                         min_g_row=float('%.3g' % (g[i].min()/max(g[i].max(), 1e-300)))))
    out[name] = rows
print(json.dumps(out, indent=0), flush=True)
