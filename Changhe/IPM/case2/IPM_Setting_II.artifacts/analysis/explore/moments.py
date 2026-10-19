# Lead check: strain moments c = (1/pi) int rho r^-3 sin 3th, psi_xx(0) = (1/pi) int rho r^-3 cos 3th for saved forward states.
import sys, json, numpy as np
for f in sys.argv[1:]:
    d = np.load(f); g, lr, th = d['g'], d['lr'], d['th']; args = json.loads(str(d['args'])); p = args['p']; l = 1 / p
    r = np.exp(lr); dl = lr[1] - lr[0]; dth = th[1] - th[0]
    wts = np.full(len(lr), dl); wts[0] = wts[-1] = dl / 2
    s3 = np.sin(3 * th); c3 = np.cos(3 * th)
    I_s = (wts[:, None] * (r ** (p - 1))[:, None] * g * s3[None, :]).sum() * dth / np.pi
    I_c = (wts[:, None] * (r ** (p - 1))[:, None] * g * c3[None, :]).sum() * dth / np.pi
    tail = r[-1] ** (p - 1) / (1 - p) / np.pi
    I_s += tail * (g[-1] * s3).sum() * dth; I_c += tail * (g[-1] * c3).sum() * dth
    print(f, 'p', p, 'c_moment', round(I_s, 5), 'm1 = l - c', round(l - I_s, 5), 'psi_xx(0) moment', round(I_c, 6))
