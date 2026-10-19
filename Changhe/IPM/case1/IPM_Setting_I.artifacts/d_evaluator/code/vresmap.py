"""Verifier (verifier): local residual map of one field export near P. One evaluation (vcand.main, own inverse), then
saves R, N_f, N_v, rho, W on the window r in [r_lo, r_hi], theta in [0, th_hi] to an npz for structure analysis.
Usage: python3 vresmap.py field.npz Mmax out.npz [r_lo r_hi th_hi]
"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from vcand import main as vcand_main, load_modes


def main(path, Mmax, outp, r_lo=6.0, r_hi=12.0, th_hi=0.6):
    out, ev, ax = vcand_main(path, {'Mmax': Mmax, 'b3': False})
    d, g, ms, F = load_modes(path, Mmax)
    Nt = out['Nt']
    th = 2 * np.pi * np.arange(Nt) / Nt
    rho = F @ np.sin(np.outer(ms, th))
    r = g.r
    cl = ev.c_l
    ir = (r >= r_lo) & (r <= r_hi)
    it = th <= th_hi
    R2 = r[ir][:, None]
    ct, st = np.cos(th[it])[None, :], np.sin(th[it])[None, :]
    sub = lambda A: A[np.ix_(ir, it)]
    rr_, rt_ = sub(ev.rho_r), sub(ev.rho_t)
    rx = ct * rr_ - st * rt_ / R2
    ry = st * rr_ + ct * rt_ / R2
    Ur, Ut = sub(ev.Ur), sub(ev.Ut)
    U1 = Ur * ct - Ut * st
    U2 = Ur * st + Ut * ct
    W1, W2 = cl * R2 * ct + U1, cl * R2 * st + U2
    rh = sub(rho)
    Nf = np.abs(W1 * rx) + np.abs(W2 * ry) + np.abs(rh)
    np.savez(outp, r=r[ir], th=th[it], R=sub(ev.R), Nf=Nf, Nv=sub(ev.Rnorm), rho=rh, W1=W1, W2=W2, rx=rx, ry=ry,
             c_l=cl, x_star=out['x_star'])
    print(json.dumps(dict(file=path, c_l=cl, x_star=out['x_star'], n_r=int(ir.sum()), n_th=int(it.sum()))), flush=True)


if __name__ == '__main__':
    a = sys.argv
    main(a[1], int(a[2]), a[3], *(float(v) for v in a[4:7]))
