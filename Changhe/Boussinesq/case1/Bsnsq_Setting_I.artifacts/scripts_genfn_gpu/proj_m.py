"""Project a genfn state (m_src) onto the basis of another compactification exponent m_dst (beta = 2m/(m-1)), same J, Kw, alpha, se:
least-squares fit of the generating function G(x, eta) of the source state at the destination collocation grid, with the H(0,0) = 1 row.
The far field changes (E^(1/beta) prefactor), so the fit is a START for the LM, not a reinterpretation. Reports fit error and min A.
Usage: proj_m.py src.npz dst.npz m_dst [J Kw Nt Ns tmin]"""
import sys, math, numpy as np, torch
import jets
from jets import Jet, monos, DT
from model import Model, fields, ts_to_xeta
DEV = jets.DEV
src, dst, m_dst = sys.argv[1], sys.argv[2], int(sys.argv[3])
d = np.load(src); J0, K0 = int(d['J']), int(d['Kw']); m_src = int(d['m']) if 'm' in d.files else 3
J = int(sys.argv[4]) if len(sys.argv) > 4 else J0; Kw = int(sys.argv[5]) if len(sys.argv) > 5 else K0
Nt = int(sys.argv[6]) if len(sys.argv) > 6 else 2 * J + 8; Ns = int(sys.argv[7]) if len(sys.argv) > 7 else 2 * Kw + 8
tmin = float(sys.argv[8]) if len(sys.argv) > 8 else float(d['tmin'])
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
msrc = Model(J0, K0, m=m_src, alpha=alpha, se=se, gam=gam); mdst = Model(J, Kw, m=m_dst, alpha=alpha, se=se, gam=gam)
c0 = torch.tensor(d['c'], dtype=DT, device=DEV)
def t_of_tau(tau, alpha):
    if alpha <= 0: return tau
    return 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1)
it = (np.arange(Nt) + 0.5) / Nt; is_ = (np.arange(Ns) + 0.5) / Ns
t = tmin + (1 - tmin) * t_of_tau(0.5 * (1 - np.cos(np.pi * it)), alpha); s = 0.5 * (1 - np.cos(np.pi * is_))
T, S = np.meshgrid(t, s, indexing='ij'); x, eta = ts_to_xeta(T.ravel(), S.ravel(), m_dst, se)
keep = (x > 1e-12) & (eta > 1e-12); x = torch.tensor(x[keep], dtype=DT, device=DEV); eta = torch.tensor(eta[keep], dtype=DT, device=DEV)
# source G and A at these points (order-2 jets for A = G_x,eta)
ix2 = monos(2)[1]
Bs = torch.cat([msrc.basis_matrix(x[i:i + 2048], eta[i:i + 2048], p=2) for i in range(0, x.shape[0], 2048)], 1)
Gs = Bs @ c0; G_src = Gs[0]; A_src = Gs[ix2[(1, 1)]]
Bd = torch.cat([mdst.basis_matrix(x[i:i + 2048], eta[i:i + 2048], p=2) for i in range(0, x.shape[0], 2048)], 1)
# weighted fit of G (relative weights 1/|G|) plus heavy H00 row
w = 1.0 / (G_src.abs() + 1e-6 * G_src.abs().max())
A = Bd[0] * w[:, None]; b = G_src * w
h00 = torch.tensor(mdst.h00_row(), dtype=DT, device=DEV)
A = torch.cat([A, 1e4 * h00[None, :]]); b = torch.cat([b, torch.tensor([1e4], dtype=DT, device=DEV)])
c1 = torch.linalg.lstsq(A, b[:, None], driver='gels').solution[:, 0]
Gd = Bd @ c1
print('fit of G: max rel error %.3e (rms %.3e); H00 = %.12f' % (float(((Gd[0] - G_src) * w).abs().max()), float(((Gd[0] - G_src) * w).norm() / math.sqrt(len(w))), float(h00 @ c1)))
print('A: source min %.4f, destination fit min %.4f (must be > 0); max rel diff of A %.3e' % (float(A_src.min()), float(Gd[ix2[(1, 1)]].min()), float(((Gd[ix2[(1, 1)]] - A_src).abs() / A_src.abs()).max())))
np.savez(dst, c=c1.cpu().numpy(), a0=float(d['a0']), J=J, Kw=Kw, m=m_dst, beta=mdst.beta, hist='[]', Nt=Nt, Ns=Ns, tmin=tmin, gauge=1, alpha=alpha, se=se, gam=gam, l=float(d['l']) if 'l' in d.files else 1.0, src=src, note='projection of the source generating function onto the m=%d basis' % m_dst)
print('saved', dst)
