"""Closure arithmetic for the conditional two-norm theorem (fractional high norm N_s).

Model: for k in the N_s ball of radius r the frozen operator A_k has
    ||exp(t A_k)||_{N_s -> N_s} <= exp(-t (mu(s) - C_W(s) r)),
    mu(s) = mu0 - s*C_bg,   C_W(s) = c_U / sqrt(s),
so K_H(r) = 1/(mu - C_W r).  The two-norm conditions K_H(r) eta <= r and
K_L C_B K_H eta < 1 are both met when eta <= eta0(s) = mu^2/(4 C_W) with
r = mu/(2 C_W), K_L = 1/(19/5 - c_s r), C_B = c_s, c_s = [2 sqrt(pi s (1+s))]^-1,
provided c_s r < 19/10.  The optimal s is mu0/(5 C_bg) (if <= 1/2; the constant c_U = 5 needs s <= 1/1024).

All arithmetic below is done in mpmath interval arithmetic; the reported
eta0 values are lower bounds for the stated formula with the stated inputs.
The inputs themselves are scenario parameters, not certified constants,
unless the scenario says so.
"""
from mpmath import iv, mpf
iv.dps = 40

def eta0(mu0, Cbg, cU, s=None):
    mu0, Cbg, cU = iv.mpf(mu0), iv.mpf(Cbg), iv.mpf(cU)
    if s is None:
        s = mu0 / (5 * Cbg)
        if s.b > 0.5:
            s = iv.mpf(0.5)
    s = iv.mpf(s)
    mu = mu0 - s * Cbg
    CW = cU / iv.sqrt(s)
    e0 = mu**2 / (4 * CW)
    r = mu / (2 * CW)
    cs = 1 / (2 * iv.sqrt(iv.pi * s * (1 + s)))
    return dict(s=s, mu=mu, CW=CW, eta0=e0, r=r, cs_r=cs * r, cs=cs)

def fmt(x):
    return "%.4g" % float(x.a)

mu0 = iv.mpf(1) / 10            # proved E_2 decay (sharp Route U weights)
scen = []
# (label, mu0, C_bg, c_U, s or None for the optimal s)
scen.append(("proved constants, C_bg = 2^22, c_U = 128, s = 2^-28 (stated choice)", mu0, 2**22, 128, iv.mpf(2)**-28))
scen.append(("proved constants, C_bg = 2^22, c_U = 128, optimal s", mu0, 2**22, 128, None))
scen.append(("C_bg = 1024 * 2374 (component-sum bound), c_U = 128, optimal s", mu0, 1024 * 2374, 128, None))
# component-resolved constants (valid for 0 < s <= 1/1024 under the separate coefficient bounds (B9c))
scen.append(("component bounds, C_bg = 4800, c_U = 5, s = 2^-18 (stated choice)", mu0, 4800, 5, iv.mpf(2)**-18))
scen.append(("component bounds, C_bg = 4800, c_U = 5, optimal s", mu0, 4800, 5, None))

print("%-72s %10s %10s %10s %10s" % ("scenario", "s", "mu", "eta0", "c_s r"))
for lab, m0, Cbg, cU, s0 in scen:
    d = eta0(m0, Cbg, cU, s0)
    print("%-72s %10s %10s %10s %10s" % (lab, fmt(d["s"]), fmt(d["mu"]), fmt(d["eta0"]), fmt(d["cs_r"])))
    assert d["cs_r"].b < 1.9
    if cU == 5:
        assert d["s"].b <= iv.mpf(1) / 1024
# the stated choice: rate at N_s(k) <= r = 2^-27 and the admissible eta = r/20
s = iv.mpf(2)**-28; r = iv.mpf(2)**-27
rate = mu0 - 2**22 * s - 128 * r / iv.sqrt(s)
print("stated choice: rate lower bound", rate, "(11/160 =", iv.mpf(11)/160, "), eta = r/20 =", r / 20)
# the component-resolved choice: s = 2^-18, r = 2^-16, rate at N_s(k) <= r and eta = r/24
s = iv.mpf(2)**-18; r = iv.mpf(2)**-16
rate = mu0 - 4800 * s - 5 * r / iv.sqrt(s)
assert rate.a > iv.mpf(1) / 24
print("component choice: rate lower bound", rate, "(873/20480 =", iv.mpf(873)/20480, "), eta = r/24 =", r / 24)
