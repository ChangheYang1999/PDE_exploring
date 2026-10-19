"""Check of the orientation moment used in code/pfwd_parity.py: psi_yy(0) = -(1/pi) int rho r^-3 cos 3th dX (and psi_xy(0) = (1/pi) int rho r^-3 sin 3th),
against the ring estimate of DW(0) from the angular modes of W/r at small r, for a compactly supported asymmetric blob (class-S velocity of code/pfwd_batch.py).
CPU, small grid.  Also checks DW12 = -psi_yy(0) and DW21 = psi_xx(0) = -psi_yy(0) (Poisson at 0 with rho_x(0) = 0)."""
import sys, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
torch.set_default_dtype(torch.float64)
Nr, Nth, lo, hi, p = 721, 128, -14.0, 10.0, 0.35
SB = PFwdB(Nr, Nth, lo, hi, p, dev='cpu'); S = SB.S
r = S.r[:, None]; th = S.th[None, :]
x = r * torch.cos(th); y = r * torch.sin(th)
for (x0, y0, w) in [(3.0, 2.0, 0.6), (-2.0, 1.5, 0.5), (1.0, -3.0, 0.7)]:
    rho = torch.exp(-((x - x0) ** 2 + (y - y0) ** 2) / (2 * w ** 2))
    pB = torch.tensor([p])
    Wr, Wt = SB.velocity(rho[None], pB)
    # moments (grid only; the blob is compactly supported away from 0 and r_max)
    wl = torch.full((Nr,), S.d); wl[0] = wl[-1] = 0.5 * S.d
    wgt = (S.r ** (-1) * wl)[:, None] * S.dth / math.pi
    c_xy = float((rho * torch.sin(3 * S.th)[None, :] * wgt).sum())
    m_c3 = float((rho * torch.cos(3 * S.th)[None, :] * wgt).sum())
    out = dict(blob=(x0, y0, w), psi_xy_moment=c_xy, psi_yy_moment=-m_c3)
    lrn = S.lr.numpy()
    for L in (-12.0, -8.0, -4.0):
        i = int(np.argmin(np.abs(lrn - L))); rr = float(S.r[i])
        vr = (Wr[0, i] / rr).numpy(); vt = (Wt[0, i] / rr).numpy()
        fr = np.fft.rfft(vr) / Nth; ft = np.fft.rfft(vt) / Nth
        alpha0 = fr[0].real; alpha2 = 2 * fr[2].real; beta2 = -2 * fr[2].imag; gamma0 = ft[0].real
        DW11, DW22, DW12, DW21 = alpha0 + alpha2, alpha0 - alpha2, beta2 - gamma0, beta2 + gamma0
        out['ring_lr%g' % L] = dict(psi_xy=-DW11, psi_yy=-DW12, psi_xx=DW21, div=2 * alpha0)
    print(out)
