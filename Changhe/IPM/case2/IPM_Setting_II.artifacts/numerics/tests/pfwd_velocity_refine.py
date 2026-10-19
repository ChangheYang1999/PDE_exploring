#!/usr/bin/env python3
"""R21(d): radial discretisation error of the solver's class-S velocity routine on a saved state, and its effect on the transport residual.
The density is interpolated in log r onto a grid with half the step (quintic spline per angle), the velocity recomputed with the same routine (PFwd.velocity,
product-integration kernels) on the fine grid, brought back to the original rows (every second fine row coincides), and compared with the velocity on the original
grid: |dW| relative to max_ring |W| and to c_l r per band, and the induced delta R = dW . grad rho (grad rho fixed, 6th-order FD in log r, local 6th-order in theta)
relative to max_ring |rho|.  Tests the verifier's inference (V255 (3)) that the 1e-5 outer floor of the transport residual with an independent velocity is the
solver routine's radial quadrature error.  Usage: python3 tests/pfwd_velocity_refine.py runs/pfwd/par/ES512_base.npz [refine=2]
"""
import sys, json, math, numpy as np, torch
from scipy.interpolate import make_interp_spline
sys.path.insert(0, 'code')
from pfwd import PFwd, fd_dlr

def main():
    f = sys.argv[1]; kw = dict(a.split('=', 1) for a in sys.argv[2:]); k = int(kw.get('refine', '2'))
    dev = 'cuda' if torch.cuda.is_available() else 'cpu'
    d = np.load(f, allow_pickle=True); g = d['g']; lr = d['lr']; Nr, Nth = g.shape
    p = float(json.loads(str(d['args']))['p']); cl = 1 / p
    lo, hi = float(lr[0]), float(lr[-1])
    rho_np = (np.exp(lr)[:, None] ** p) * g
    S = PFwd(Nr, Nth, lo, hi, p, dev=dev)
    rho = torch.tensor(rho_np, device=dev)
    Wr0, Wt0 = S.velocity(rho)
    Nr2 = k * (Nr - 1) + 1; lr2 = np.linspace(lo, hi, Nr2)
    spl = make_interp_spline(lr, rho_np, k=5, axis=0)
    rho2 = torch.tensor(spl(lr2), device=dev)
    S2 = PFwd(Nr2, Nth, lo, hi, p, dev=dev)
    Wr2, Wt2 = S2.velocity(rho2)
    Wr2 = Wr2[::k]; Wt2 = Wt2[::k]
    assert float(np.abs(lr2[::k] - lr).max()) < 1e-12
    r = S.r; lrt = torch.tensor(lr, device=dev)
    dWr, dWt = Wr2 - Wr0, Wt2 - Wt0
    W = torch.sqrt(Wr0 ** 2 + Wt0 ** 2); dW = torch.sqrt(dWr ** 2 + dWt ** 2)
    sW = W.amax(dim=1) + 1e-300
    rho_lr = fd_dlr(rho, S.d)
    rho_t = (torch.roll(rho, -3, 1) - 9 * torch.roll(rho, -2, 1) + 45 * torch.roll(rho, -1, 1) - 45 * torch.roll(rho, 1, 1) + 9 * torch.roll(rho, 2, 1) - torch.roll(rho, 3, 1)) / (60 * S.dth)
    dR = dWr * rho_lr / r[:, None] + dWt * rho_t / r[:, None]
    srho = rho.abs().amax(dim=1) + 1e-300
    thd = S.th * 180 / math.pi
    offaxis = ~((torch.abs((thd + 180) % 360 - 180) <= 10) | (torch.abs((thd - 180 + 180) % 360 - 180) <= 10))
    bands = [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -2), (-2, 2), (2, 6), (6, 10.01)]
    print(json.dumps(dict(file=f, Nr=Nr, Nr_fine=Nr2, Nth=Nth, p=p)))
    print('band          max|dW|/max_ring|W|  rms   max|dW|/(c_l r)   dR/max|rho|: rms   max   max off-axis(10deg)')
    out = {}
    for lo_, hi_ in bands:
        m = (lrt >= lo_) & (lrt < hi_)
        X = dW[m] / sW[m][:, None]; Y = dW[m] / (cl * r[m])[:, None]; Z = dR[m].abs() / srho[m][:, None]
        row = dict(dW_over_maxW=float(X.max()), dW_over_maxW_rms=float(torch.sqrt((X ** 2).mean())), dW_over_clr=float(Y.max()), dR_rms=float(torch.sqrt((Z ** 2).mean())), dR_max=float(Z.max()), dR_max_offaxis=float(Z[:, offaxis].max()))
        out['[%g,%g)' % (lo_, hi_)] = row
        print('%-13s %9.2e  %9.2e  %9.2e      %9.2e  %9.2e  %9.2e' % ('[%g,%g)' % (lo_, hi_), row['dW_over_maxW'], row['dW_over_maxW_rms'], row['dW_over_clr'], row['dR_rms'], row['dR_max'], row['dR_max_offaxis']))
    # ring-fit strain at lr = -12 and the moment c = psi_xy(0) from W's m = 2 component at small r? report the ring fit only
    def dw11(Wr, Wt, kk):
        M = S.node_matrix(Wr[kk] / r[kk], Wt[kk] / r[kk]); return float(M[0, 0])
    kk = int(np.argmin(np.abs(lr + 12)))
    print('ring-fit DW11 at lr = -12: original %.10f, refined %.10f' % (dw11(Wr0, Wt0, kk), dw11(Wr2, Wt2, kk)))
    print(json.dumps(out))

if __name__ == '__main__':
    main()
