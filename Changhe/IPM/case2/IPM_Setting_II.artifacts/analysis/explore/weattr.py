# Lead (2026-10-18): attribution of the axis even velocity w_e (y-even part of W_2 on the axis) to the y-even density
# rho_e by radius (smooth partition chi_R = 1/(1 + (r/R)^4)) and the first-order share of 2L = 4n int w_e/b_o^2 dr from each part.
# Also the cusp part: rho_e - x^2 Cbar(r) with Cbar from the axis (rho_xx/2 averaged over the two half-axes at radius r).
# Usage: python3 weattr.py state.npz p m1
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); p = float(sys.argv[2]); m1 = float(sys.argv[3]); l = 1 / p; n = 2 * l - m1
g, lr, th = d['g'], d['lr'], d['th']; Nth = len(th); r = np.exp(lr); ju, jd = Nth // 4, 3 * Nth // 4
rho = (r ** p)[:, None] * g
refl = (-np.arange(Nth)) % Nth                 # th -> -th on the uniform grid th_j = 2 pi j / Nth
assert abs(th[0]) < 1e-12
rho_e = 0.5 * (rho + rho[:, refl]); rho_o = 0.5 * (rho - rho[:, refl])
wr, _ = PF.velocity_p(rho, lr, th, p)
bo = l * r + 0.5 * (wr[:, ju] + wr[:, jd])
def we_of(f):
    w, _ = PF.velocity_p(f, lr, th, p)
    return 0.5 * (w[:, ju] - w[:, jd]), 0.5 * (w[:, ju] + w[:, jd])
def share(we, lo=-99, hi=99):
    dens = 4 * n * we / bo ** 2 * r; m = (lr >= lo) & (lr < hi)
    return float(np.trapezoid(dens[m], lr[m]))
we_full, wo_full = we_of(rho)
we_e, wo_e = we_of(rho_e); we_o, wo_o = we_of(rho_o)
out = dict(check_parity=dict(we_from_rho_o_max=float(np.abs(we_o).max()), wo_from_rho_e_max=float(np.abs(wo_e).max()), we_max=float(np.abs(we_full).max())),
           twoL_first_order=share(we_full), parts={})
for LR in (-8, -6, -4, -2, 0, 2):
    chi = 1 / (1 + (r / np.exp(LR)) ** 4)
    wi, _ = we_of(rho_e * chi[:, None])
    out['parts']['inner_R=e^%d' % LR] = dict(total=round(share(wi), 4), near_lt_m4=round(share(wi, -99, -4), 4), mid=round(share(wi, -4, 2), 4), far=round(share(wi, 2, 99), 4))
x2 = (r * np.cos(th)[None, :]) ** 2 if False else (r[:, None] * np.cos(th)[None, :]) ** 2
kk = np.fft.rfftfreq(Nth, 1.0 / Nth)
gtt = np.fft.irfft(-(kk ** 2) * np.fft.rfft(g, axis=1), Nth, axis=1)
h_up, h_dn = r ** (p - 2) * gtt[:, ju], r ** (p - 2) * gtt[:, jd]
Cbar = 0.25 * (h_up + h_dn)
cusp = rho_e - Cbar[:, None] * x2
for LR in (-6, -4):
    chi = 1 / (1 + (r / np.exp(LR)) ** 4)
    wc, _ = we_of(cusp * chi[:, None]); ws, _ = we_of((Cbar[:, None] * x2) * chi[:, None])
    out['parts']['cusp_R=e^%d' % LR] = dict(total=round(share(wc), 4), near_lt_m4=round(share(wc, -99, -4), 4))
    out['parts']['Cbar_x2_R=e^%d' % LR] = dict(total=round(share(ws), 4), near_lt_m4=round(share(ws, -99, -4), 4))
sel = [int(np.argmin(np.abs(lr - L))) for L in (-10, -8, -6, -5, -4, -3)]
out['axis'] = [dict(lr=round(float(lr[i]), 1), Cup=float('%.4g' % (h_up[i] / 2)), Cdn=float('%.4g' % (h_dn[i] / 2)), we_over_r=float('%.4g' % (we_full[i] / r[i]))) for i in sel]
print(json.dumps(out, indent=1))
