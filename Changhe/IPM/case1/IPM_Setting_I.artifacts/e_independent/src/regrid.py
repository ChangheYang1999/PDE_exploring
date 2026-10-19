"""Transfer b between grids (possibly different N, M, beta, gamma, L): b is a function of (r, theta); interpolate the
bounded EE function in t (barycentric) and in s (exact EE basis of the old grid), then convert the weight w if gamma or L differ."""
import sys, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, charac

def regrid(b_old, m_old, m_new):
    fe = charac.FieldEval(m_old, b_old, 1.0)
    r_new = m_new.rad.rR[1:]
    t_old = fe.t_of_r(r_new)                                  # (Nn,)
    Pm = fe.radial_interp_matrix(t_old)                       # (Nn, No+1)
    C = m_old.ang.to_coef(b_old, 'EE')                        # (No+1, Mo)
    s_new = m_old.ang.s_of_theta(m_new.ang.theta)             # old-map s coordinates of the new angles
    k = torch.arange(m_old.M, device=b_old.device, dtype=torch.float64)
    E = torch.cos(s_new[:, None] * (2 * k)[None, :])          # (Mn, Mo)
    b_new = torch.ones(m_new.N + 1, m_new.M, device=b_old.device)
    b_new[1:] = (Pm @ C) @ E.T
    # weight conversion: a = w_old b_old = w_new b_new
    w_old = (1 + r_new ** 2 / m_old.L ** 2) ** ((m_old.gamma - 3) / 2)
    w_new = (1 + r_new ** 2 / m_new.L ** 2) ** ((m_new.gamma - 3) / 2)
    b_new[1:] *= (w_old / w_new)[:, None]
    return b_new

if __name__ == '__main__':
    # self-test: regrid a smooth field between grids and compare with the analytic values
    dev = 'cuda'
    m1 = ipm1.IPM1(N=48, M=10, L=1.0, gamma=0.4, device=dev, beta=0.0)
    m2 = ipm1.IPM1(N=72, M=20, L=1.0, gamma=0.4, device=dev, beta=0.8)
    f = lambda r, th: 1 + 0.5 * torch.cos(2 * th) * r ** 2 / (1 + r ** 2) + 0.3 * torch.cos(4 * th) * (r ** 2 / (1 + r ** 2)) ** 2
    b1 = f(m1.rad.rR[:, None], m1.ang.theta[None, :]); b2x = f(m2.rad.rR[:, None], m2.ang.theta[None, :])
    b2 = regrid(b1, m1, m2)
    print("regrid error (smooth field, 48x10 beta0 -> 72x20 beta0.8):", (b2 - b2x).abs().max().item())
