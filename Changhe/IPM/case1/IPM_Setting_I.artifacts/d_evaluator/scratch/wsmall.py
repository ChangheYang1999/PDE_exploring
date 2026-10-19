import numpy as np
for f in ('R1e7_N3520', 'R1e5_N2160'):
    a = np.load('../runs/b3w/%s_axis.npz' % f)
    x, w, wp, wf, wo, gw, a2 = a['x'], a['w'], a['wp'], a['wpp_fd'], a['wpp_ode'], a['gw'], a['a2w']
    A = 2 * float(a['c_l']) - 1
    sel = (x > 0.002) & (x < 0.08)
    # w = -A x + w3 x^3 + w5 x^5 + w7 x^7
    M = np.stack([x[sel] ** 3, x[sel] ** 5, x[sel] ** 7], 1)
    cf, *_ = np.linalg.lstsq(M, w[sel] + A * x[sel], rcond=None)
    print(f, 'w3 w5 w7', cf)
    for t in (0.001, 0.0015, 0.002, 0.003, 0.005, 0.008, 0.012, 0.02, 0.04, 0.08, 0.15):
        j = np.argmin(abs(x - t)); xx = x[j]
        wfit = -A * xx + cf[0] * xx ** 3 + cf[1] * xx ** 5 + cf[2] * xx ** 7
        print('  x %.4g  (w-wfit)/x^3 %.3e  wpp_fd/x %.10f  wpp_ode/x %.10f  (wp+A)/x^2 %.10f  a2/x %.10f' % (xx, (w[j] - wfit) / xx ** 3, wf[j] / xx, wo[j] / xx, (wp[j] + A) / xx ** 2, a2[j] / xx))
