"""Verifier (verifier): direct effect of the fit-convention closure on the residual of one shape. Two field exports of the
same shape on the same grid, A without closure (formula to r = R) and B with gen_shape 'closure=<Rs>' (rho replaced by the
two-term exterior extension for r > Rs L). Each is evaluated by the verifier's own inverse (vcand.main). Inside Rs L the
densities agree, so R_B - R_A = (W_B - W_A).grad rho, with c_l from the identity on each field. Reports, per band of the
open first quadrant (axes excluded), max |R_B - R_A| / N_f and / N_v (N_f, N_v of field A), its split into the velocity part
(U_B - U_A).grad rho and the c_l part (c_l,B - c_l,A) X.grad rho, max |R_A| / N_f, and max |U_B - U_A|.
Usage: python3 clo_diff.py fieldA.npz fieldB.npz Mmax Rc_phys [cfgA_json cfgB_json]  (vcand cfg, e.g. {"k_self": true})
"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from vcand import main as vcand_main, load_modes


def ev_fields(path, Mmax, cfg):
    out, ev, ax = vcand_main(path, dict(cfg, Mmax=Mmax, b3=False))
    d, g, ms, F = load_modes(path, Mmax)
    Nt = out['Nt']
    th = 2 * np.pi * np.arange(Nt) / Nt
    rho = F @ np.sin(np.outer(ms, th))
    r = g.r[:, None]
    ct, st = np.cos(th)[None, :], np.sin(th)[None, :]
    rx = ct * ev.rho_r - st * ev.rho_t / r
    ry = st * ev.rho_r + ct * ev.rho_t / r
    U1 = ev.Ur * ct - ev.Ut * st
    U2 = ev.Ur * st + ev.Ut * ct
    cl = ev.c_l
    W1, W2 = cl * r * ct + U1, cl * r * st + U2
    Nf = np.abs(W1 * rx) + np.abs(W2 * ry) + np.abs(rho)
    return dict(r=g.r, th=th, R=np.array(ev.R), Nf=Nf, Nv=np.array(ev.Rnorm), U1=U1, U2=U2, rx=rx, ry=ry, c_l=cl, x_star=out['x_star'])


def main(pa, pb, Mmax, Rc, ca='{}', cb='{}'):
    A = ev_fields(pa, Mmax, json.loads(ca))
    B = ev_fields(pb, Mmax, json.loads(cb))
    r, th = A['r'], A['th']
    q = (th > 1e-12) & (th < np.pi / 2 - 1e-12)          # open first quadrant (rho = 0 on both axes, N = 0 there)
    X = r[:, None] * np.cos(th)[None, :]; Y = r[:, None] * np.sin(th)[None, :]
    dP = np.hypot(X - A['x_star'], Y)
    RR = np.repeat(r[:, None], len(th), 1)
    dR = np.abs(B['R'] - A['R'])
    dU = np.hypot(B['U1'] - A['U1'], B['U2'] - A['U2'])
    # split of R_B - R_A inside Rc L (same rho): (U_B - U_A).grad rho at fixed c_l, and (c_l,B - c_l,A) X.grad rho
    dRU = np.abs((B['U1'] - A['U1']) * A['rx'] + (B['U2'] - A['U2']) * A['ry'])
    dRc = np.abs((B['c_l'] - A['c_l']) * (X * A['rx'] + Y * A['ry']))
    bands = [('|X-P|<0.5', dP < 0.5), ('0.5<=|X-P|<2.5', (dP >= 0.5) & (dP < 2.5)), ('0.1<=r<2', (RR >= 0.1) & (RR < 2)),
             ('2<=r<10', (RR >= 2) & (RR < 10)), ('10<=r<20', (RR >= 10) & (RR < 20)), ('20<=r<100', (RR >= 20) & (RR < 100)),
             ('100<=r<300', (RR >= 100) & (RR < 300)), ('300<=r<1000', (RR >= 300) & (RR < 1000)),
             ('1000<=r<0.5Rc', (RR >= 1000) & (RR < 0.5 * Rc)), ('0.5Rc<=r<0.9Rc', (RR >= 0.5 * Rc) & (RR < 0.9 * Rc)),
             ('r<0.9Rc', RR < 0.9 * Rc)]
    print(json.dumps(dict(A=pa, B=pb, Rc=Rc, cfgA=ca, cfgB=cb, c_l_A=A['c_l'], c_l_B=B['c_l'], dcl=B['c_l'] - A['c_l'],
                          x_star_A=A['x_star'], x_star_B=B['x_star'])), flush=True)
    res = {}
    for name, m in bands:
        m = m & q[None, :] & (A['Nf'] > 0) & (A['Nv'] > 0)
        if not m.any():
            continue
        e_f = dR[m] / A['Nf'][m]; e_v = dR[m] / A['Nv'][m]; base = np.abs(A['R'][m]) / A['Nf'][m]
        i = np.argmax(e_f); ii = np.argwhere(m)[i]
        uf, uv = (dRU[m] / A['Nf'][m]).max(), (dRU[m] / A['Nv'][m]).max()
        cf, cv = (dRc[m] / A['Nf'][m]).max(), (dRc[m] / A['Nv'][m]).max()
        res[name] = dict(dR_Nf=float(e_f.max()), dR_Nv=float(e_v.max()), RA_Nf=float(base.max()), dU=float(dU[m].max()),
                         dRU_Nf=float(uf), dRU_Nv=float(uv), dRc_Nf=float(cf), dRc_Nv=float(cv),
                         at_r=float(r[ii[0]]), at_th=float(th[ii[1]]))
        print('%-16s max|dR|/N_f %.3e  /N_v %.3e | U part %.3e %.3e | c_l part %.3e %.3e | max|R_A|/N_f %.3e | max|dU| %.3e'
              ' | at r %.4g th %.4f' % (name, e_f.max(), e_v.max(), uf, uv, cf, cv, base.max(), dU[m].max(), r[ii[0]], th[ii[1]]),
              flush=True)
    return res


if __name__ == '__main__':
    a = sys.argv
    main(a[1], a[2], int(a[3]), float(a[4]), *a[5:7])
