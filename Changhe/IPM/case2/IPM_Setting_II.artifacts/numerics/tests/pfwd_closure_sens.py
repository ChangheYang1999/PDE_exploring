#!/usr/bin/env python3
"""Sensitivity of the nonlocal class-S velocity of a saved state to (i) the inner closure of the Green inverse at the grid boundary
r = e^lo (default lo = -14) and (ii) the outer tail model beyond r = e^hi (one-term r^(p-1) vs the two-term closure of specification 2).
(i) The grid is extended inward by 'ext' log-units (default 2, i.e. to e^-16) with rho continued as rho(lr, th) = rho(lo, th) exp(2 (lr - lo)) (the r^2
    scaling of the quadratic node at fixed angle; alternative cont=0: rho = 0 below lo; cont=p: scaling r^p), the velocity is recomputed and compared on
    the original rows.  (ii) tail2=1 recomputes the velocity with the two-term outer closure on the original grid.  Differences are reported by band as
    max |dW| / max_ring |W| and max |dW| / max_ring (c_l r), i.e. relative to the nonlocal part and to the full transport velocity.
Usage: python3 tests/pfwd_closure_sens.py runs/pfwd/par/ES512_base.npz [ext=2] [cont=2|0|p]
"""
import sys, json, math, numpy as np, torch
sys.path.insert(0, 'code')
from pfwd import PFwd

def bands_report(dWr, dWt, Wr, Wt, r, lr, cl, label, bands):
    out = {}
    W = torch.sqrt(Wr ** 2 + Wt ** 2); dW = torch.sqrt(dWr ** 2 + dWt ** 2)
    sW = W.amax(dim=1) + 1e-300; sV = cl * r
    for lo, hi in bands:
        m = (lr >= lo) & (lr < hi)
        if not bool(m.any()):
            continue
        out['[%g,%g)' % (lo, hi)] = dict(dW_over_maxW=float((dW[m] / sW[m][:, None]).max()), dW_over_clr=float((dW[m] / sV[m][:, None]).max()),
                                       dW_over_maxW_rms=float(torch.sqrt(((dW[m] / sW[m][:, None]) ** 2).mean())))
    print(label)
    print('  band          max|dW|/max_ring|W|   rms   max|dW|/(c_l r)')
    for k, v in out.items():
        print('  %-12s  %9.2e  %9.2e  %9.2e' % (k, v['dW_over_maxW'], v['dW_over_maxW_rms'], v['dW_over_clr']))
    return out

def main():
    f = sys.argv[1]; kw = dict(a.split('=', 1) for a in sys.argv[2:])
    dev = 'cuda' if torch.cuda.is_available() else 'cpu'
    ext = float(kw.get('ext', '2')); cont = kw.get('cont', '2')
    d = np.load(f, allow_pickle=True)
    g = torch.tensor(d['g'], device=dev, dtype=torch.float64); lr = d['lr']; Nr, Nth = g.shape
    p = float(json.loads(str(d['args']))['p']); cl = 1 / p
    dl = float(lr[1] - lr[0]); lo, hi = float(lr[0]), float(lr[-1])
    S = PFwd(Nr, Nth, lo, hi, p, dev=dev)
    r = S.r; lrt = torch.tensor(lr, device=dev)
    rho = (r[:, None] ** p) * g
    Wr0, Wt0 = S.velocity(rho)
    bands = [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -2), (-2, 2), (2, 6), (6, 10.01)]
    res = dict(file=f, p=p, Nr=Nr, Nth=Nth, lo=lo, hi=hi)
    # (i) inner extension
    next_ = int(round(ext / dl)); lo2 = lo - next_ * dl
    S2 = PFwd(Nr + next_, Nth, lo2, hi, p, dev=dev)
    lr2 = S2.lr
    if cont == '0':
        rho2 = torch.zeros(Nr + next_, Nth, device=dev, dtype=torch.float64); rho2[next_:] = rho
    else:
        q = 2.0 if cont == '2' else p
        rho2 = torch.zeros(Nr + next_, Nth, device=dev, dtype=torch.float64); rho2[next_:] = rho
        rho2[:next_] = rho[0][None, :] * torch.exp(q * (lr2[:next_] - lo))[:, None]
    Wr2, Wt2 = S2.velocity(rho2)
    res['inner_ext'] = dict(ext=ext, cont=cont, bands=bands_report(Wr2[next_:] - Wr0, Wt2[next_:] - Wt0, Wr0, Wt0, r, lrt, cl,
                            'INNER CLOSURE: grid extended to lr = %g with rho continued as r^%s below %g; dW on the original rows' % (lo2, '2' if cont == '2' else ('0' if cont == '0' else 'p'), lo), bands))
    # (ii) outer two-term tail
    S3 = PFwd(Nr, Nth, lo, hi, p, dev=dev, tail2=True)
    Wr3, Wt3 = S3.velocity(rho)
    res['tail2'] = bands_report(Wr3 - Wr0, Wt3 - Wt0, Wr0, Wt0, r, lrt, cl, 'OUTER TAIL: two-term closure (specification 2) against the one-term r^(p-1) tail beyond lr = %g' % hi, bands)
    # (iii) the m = 1 strain moment / psi_xy(0) sensitivity: c = psi_xy(0) from DW at small r: DW11 = -c
    def dw11(Wr, Wt, k):
        ar = Wr[k] / r[k]; at = Wt[k] / r[k]
        M = S.node_matrix(ar, at); return float(M[0, 0]), float(M[1, 1])
    k = int(np.argmin(np.abs(lr + 12)))
    res['DW_at_lr-12'] = dict(base=dw11(Wr0, Wt0, k), inner_ext=dw11(Wr2[next_:], Wt2[next_:], k), tail2=dw11(Wr3, Wt3, k))
    print('DW(0) estimate at lr = -12 (ring fit; entries 11, 22): base %s, inner-extended %s, tail2 %s' % (res['DW_at_lr-12']['base'], res['DW_at_lr-12']['inner_ext'], res['DW_at_lr-12']['tail2']))
    # (iv) the induced change of the transport residual, delta R = delta W . grad rho (grad rho fixed: 6th-order FD in lr, spectral and local 6th-order in theta)
    from pfwd import fd_dlr
    rho_lr = fd_dlr(rho, S.d)
    def dth_local(F):
        return (torch.roll(F, -3, 1) - 9 * torch.roll(F, -2, 1) + 45 * torch.roll(F, -1, 1) - 45 * torch.roll(F, 1, 1) + 9 * torch.roll(F, 2, 1) - torch.roll(F, 3, 1)) / (60 * S.dth)
    srho = rho.abs().amax(dim=1) + 1e-300
    res['deltaR'] = {}
    for name, (dWr, dWt) in (('inner_ext', (Wr2[next_:] - Wr0, Wt2[next_:] - Wt0)), ('tail2', (Wr3 - Wr0, Wt3 - Wt0))):
        for stencil, rho_t in (('spectral', S.d_theta(rho)), ('local', dth_local(rho))):
            dR = dWr * rho_lr / r[:, None] + dWt * rho_t / r[:, None]
            row = {}; row_rms = {}; row_off = {}
            thd = S.th * 180 / math.pi
            offaxis = ~((torch.abs((thd + 180) % 360 - 180) <= 10) | (torch.abs((thd - 180 + 180) % 360 - 180) <= 10))
            for lo_, hi_ in bands:
                m = (lrt >= lo_) & (lrt < hi_)
                if bool(m.any()):
                    X = dR[m].abs() / srho[m][:, None]
                    row['[%g,%g)' % (lo_, hi_)] = float(X.max()); row_rms['[%g,%g)' % (lo_, hi_)] = float(torch.sqrt((X ** 2).mean()))
                    row_off['[%g,%g)' % (lo_, hi_)] = float(X[:, offaxis].max())
            res['deltaR'][name + '_' + stencil] = dict(max=row, rms=row_rms, max_offaxis=row_off)
            print('delta R / max_ring|rho| for %s, grad rho with the %s theta-derivative: max per band %s' % (name, stencil, ', '.join('%s %.1e' % kv for kv in row.items())))
            print('    rms per band %s' % ', '.join('%s %.1e' % kv for kv in row_rms.items()))
            print('    max outside the weak-axis sectors (10 deg) %s' % ', '.join('%s %.1e' % kv for kv in row_off.items()))
    print(json.dumps(res))

if __name__ == '__main__':
    main()
