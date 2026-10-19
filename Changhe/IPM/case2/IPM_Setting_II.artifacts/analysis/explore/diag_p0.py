# Lead exploration: where does the forward (P0) evolution fail to settle? Loads a saved state and continues, recording
# the location (r, theta) of max |d_s f| and the upper/lower-half split. Exploratory.
import sys, json
import numpy as np
import p0_forward as P
from scipy.ndimage import map_coordinates
d = np.load(sys.argv[1]); order = int(sys.argv[2]); nsteps = int(sys.argv[3]); ds = float(sys.argv[4])
f, rho, th = d['f'], d['rho'], d['th']
args = json.loads(str(d['args']))
Nr, Nth = f.shape; drho = rho[1] - rho[0]; r = np.exp(rho)
def interp(g, ci, cj):
    Pd = 4
    gp = np.concatenate([g[:, -Pd:], g, g[:, :Pd]], axis=1)
    return map_coordinates(gp, [np.clip(ci, 0, Nr - 1), np.mod(cj, Nth) + Pd], order=order, mode='nearest')
upper = (np.sin(th) > 0)[None, :]
for n in range(nsteps):
    wr, wt = P.velocity(f, rho, th)
    ar = 1.0 + wr / r[:, None]; at = wt / r[:, None]
    ci0 = np.arange(Nr)[:, None] + 0.5 * ds * ar / drho
    cj0 = np.arange(Nth)[None, :] + 0.5 * ds * at / (2 * np.pi / Nth)
    arm = interp(ar, ci0, cj0); atm = interp(at, ci0, cj0)
    ci = np.arange(Nr)[:, None] + ds * arm / drho
    cj = np.arange(Nth)[None, :] + ds * atm / (2 * np.pi / Nth)
    fn = interp(f, ci, cj)
    out = ci > Nr - 1
    if out.any():
        fn[out] = P.data_A(cj[out] * (2 * np.pi / Nth), args['kind'], args['par'])
    df = np.abs(fn - f) / ds
    f = fn
    if n % 25 == 0 or n == nsteps - 1:
        i, j = np.unravel_index(np.argmax(df), df.shape)
        print('n %4d max|f_s| %.3g at r=%.3g th=%.3f | upper %.3g lower %.3g | fmin %.3g fmax %.4f' % (
            n, df.max(), r[i], th[j], df[np.broadcast_to(upper, df.shape)].max(), df[~np.broadcast_to(upper, df.shape)].max(), f.min(), f.max()), flush=True)
np.savez(sys.argv[5], f=f, rho=rho, th=th, A=d['A'], hist='[]', args=json.dumps(args))
