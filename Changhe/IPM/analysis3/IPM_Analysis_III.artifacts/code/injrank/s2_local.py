# NUMERICAL (float64 grid data, not a bound): radially localized second-order cutoffs. Partition t into cells of width
# h with cutoffs chi_k (sum chi_k^2 = 1) and wider plateaus chit_k = 1 on supp chi_k. For each cell the principal error
# on chi_k u with chi_k u = Q_(Lambda_k) chi_k u is eta/2 + [sum_ij S2(B_ij chit_k) + S2(b_eta chit_k)]/(2 Lambda_k^2)
# (topic 94 applied to the localized coefficients). Required Lambda_k^2 = S2_k / (2 (E - eta/2)); local low-mode count
# N_k ~ |supp chi_k| Lambda_k^2 / 2 on the full circle, divided by 4 for the parity class. IMS localization errors
# ((1/2) sum_k [chi_k, [chi_k, C]]) and the singular axis strip are NOT included.
import numpy as np, json, sys
exec(open('s2_estimate.py').read().split('out = {}')[0])
eta = 0.1
beta = (np.sqrt(G1**2 + G2**2 + eta**2) - G2) / 2
dt_ = t[1] - t[0]; nn = np.fft.fftfreq(n_th, d=1.0 / n_th)
def bump(x):
    y = np.zeros_like(x); i = (x > 0) & (x < 1)
    y[i] = 1 / (1 + np.exp(1 / x[i] - 1 / (1 - x[i]))); y[x >= 1] = 1; return y
def S2win(a, lo, hi, w):
    msk = (t >= lo - w) & (t <= hi + w); tt = t[msk]
    chit = bump((tt - (lo - w)) / w) * bump((hi + w - tt) / w)
    xi = 2 * np.pi * np.fft.fftfreq(len(tt), d=dt_)
    Q2 = xi[:, None]**2 + nn[None, :]**2
    return float((Q2 * abs(np.fft.fft2(a[msk] * chit[:, None]) / (len(tt) * n_th))).sum())
out = {}
for h, w in [(1.0, 0.5), (0.5, 0.5), (2.0, 0.5)]:
    for E in [1.0, 1.5]:
        rows = []; Ntot = 0
        for lo in np.arange(-3.0, 11.0, h):
            hi = lo + h
            S2k = S2win(B11, lo, hi, w) + S2win(B22, lo, hi, w) + 2 * S2win(B12, lo, hi, w) + S2win(beta, lo, hi, w)
            L2 = S2k / (2 * (E - eta / 2)); Nk = (h + 2 * 0.25) * L2 / 8   # supp chi_k ~ cell plus overlap
            Ntot += Nk; rows.append([float(lo), float(np.sqrt(L2)), float(Nk)])
        out['h=%g,w=%g,E=%g' % (h, w, E)] = dict(N_total=float(Ntot), cells_t_Lambda_N=rows)
print(json.dumps(out, indent=1))
