"""regauge_table.py -- lead 07:10Z diagnostic on saved fixed-c_l chain states: re-gauge each state by the dilation rho_l(X) = l rho(X/l) to L_K = 1 (K = a0,
i.e. l^(1-gamma) K = a0), then tabulate (i) a0, the cubic coefficients b, e in that gauge (b_l = b/l^2, e_l = e/l^2), e/a0; (ii) half-widths: the x at which
rho_y(x, 0)/a0 (= w b at theta = 0) first drops to 1/2 along the x-axis and the y at which rho(0, y)/(a0 y) drops to 1/2 along the y-axis, in the re-gauged
physical variables and in xi = x/sqrt(a0); (iii) sup over the box xi in [0, 3], y in (0, 3] of |g_N - g_ref| with g = rho_l/a0 evaluated at (x = sqrt(a0) xi, y),
ref = the last state given.  usage: python3 src/regauge_table.py ref.pt other1.pt other2.pt ..."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3ql, dr
torch.set_default_dtype(torch.float64); dev = 'cuda'
files = sys.argv[1:]; ref = files[0]
def load(f):
    st = torch.load(f, weights_only=False); cl = st['cl']
    if st.get('rep', '').startswith('DR'):
        m = dr.DR(st['N'], st['M'], st['C'], device=dev, basis=st.get('basis', 'local'), rcond=st.get('rcond', 1e-8)); u = st['u'].to(dev); beta = m.beta_full(u); cl = st['C']
    else:
        m = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=st.get('L', 1.0), gamma=1 / cl, device=dev, Lf=st.get('Lf', 1.0)); beta = st['beta'].to(dev); u = None
    flds = m.fields(beta); gam = 1 / cl
    if u is not None:                                   # DR state: basis-aware evaluation of beta_k(1), beta_k'(-1), beta_1(-1) through the coefficients
        K = m.farfield(u)['K'].item(); a0, b, e = [z.item() for z in m.jets(u)]
    else:
        bk1 = (m.rad.ext1_R @ beta * torch.cos(math.pi * m.kk)[None, :]).sum().item(); K = 0.5 * m.L ** (1 - gam) * bk1
        a0 = beta[0, 0].item()
        # cubic coefficients from the Radau representation (same formula as dr.jets, via beta_0'(-1) and beta_1(-1))
        d0 = (m.rad.DR[0, :] @ beta[:, 0]).item(); b1 = beta[0, 1].item(); ellc2 = m.L ** 2 * 2.0 ** (-2 * m.p)
        b = (2 * d0 - a0 + b1) / ellc2; e = (2 * d0 - a0 - b1) / ellc2
    lam = (a0 / K) ** (1 / (1 - gam)) if K / a0 > 0 else float('nan')     # l^(1-gamma) K = a0
    return dict(m=m, beta=beta, flds=flds, cl=cl, a0=a0, K=K, b=b, e=e, lam=lam, name=f, N=st['N'], M=st['M'])
def rho_regauged(S, x, y):
    """rho_l(x, y) = l rho(x/l, y/l) and rho_y (invariant under the dilation: rho_l,y(x, y) = rho_y(x/l, y/l)); theta = 0 is evaluated EXACTLY
    (evaluate() has no division by sin theta: at theta = 0, rho_y = w b(t, 0) = w sum_k b_k(t))."""
    l = S['lam']; r = np.hypot(x, y) / l; th = np.arctan2(y, x); th = np.clip(th, 0.0, np.pi / 2 - 1e-12)
    ev = S['m'].evaluate(S['beta'], S['cl'], S['flds'], r, th)
    return l * ev['rho'], ev['rho_y']
def _first_half(f, xs, lo_hi_bisect=40):
    """first x in the geometric scan xs where f(x) <= 1/2, refined by bisection on [x_{i-1}, x_i] to a relative width 1e-9 (f evaluated vectorised)."""
    vals = f(xs); idx = np.where(vals <= 0.5)[0]
    if len(idx) == 0: return float('nan'), float('nan')
    i = idx[0]
    if i == 0: return xs[0], float('nan')
    a, b = xs[i - 1], xs[i]
    for _ in range(lo_hi_bisect):
        mid = math.sqrt(a * b); v = f(np.array([mid]))[0]
        if v <= 0.5: b = mid
        else: a = mid
    return b, (b - a) / b
def halfwidths(S):
    a0 = S['a0']; xs = np.geomspace(1e-3, 1e4, 1400)
    fx = lambda x: rho_regauged(S, x, 0.0 * x)[1] / a0                              # rho_y(x, 0)/a0 along the x-axis, exact theta = 0
    fy = lambda y: rho_regauged(S, 0.0 * y, y)[0] / (a0 * y)                        # rho(0, y)/(a0 y) along the y-axis
    wx, ex = _first_half(fx, xs); wy, ey = _first_half(fy, xs)
    return wx, wy
R = load(ref); xi = np.linspace(0, 3, 61); yy = np.linspace(0.05, 3, 60); XI, YY = np.meshgrid(xi, yy, indexing='ij')
def gbox(S):
    rr, _ = rho_regauged(S, np.sqrt(S['a0']) * XI, YY); return rr / S['a0']
gref = gbox(R)
print(f"# re-gauged to L_K = 1 (K = a0) by the dilation l = (a0/K)^(1/(1-gamma)); reference for (iii): {ref}")
print("# half-widths refined by bisection to 1e-9 relative (first crossing of 1/2 of the geometric scan 1e-3 .. 1e4, 1400 points); x-axis evaluated exactly at theta = 0; box statistic = sampled max over a 61 x 60 grid xi in [0, 3], y in [0.05, 3] with each state's own xi = x/sqrt(a0)")
print("# state                      N    M   c_l   a0        K(orig)   l         b_l         e_l         e_l/a0      w_x        w_x/sqrt(a0)  w_y        max_box|g - g_ref|")
for f in files:
    S = load(f); wx, wy = halfwidths(S); g = gbox(S); sup = np.abs(g - gref).max() if g.shape == gref.shape else float('nan')
    l = S['lam']; bl = S['b'] / l ** 2; el = S['e'] / l ** 2
    print(f"{S['name']:28s} {S['N']:4d} {S['M']:3d}  {S['cl']:.2f}  {S['a0']:8.4f}  {S['K']:8.4f}  {l:8.4f}  {bl:+.4e}  {el:+.4e}  {el/S['a0']:+.4e}  {wx:.4e}  {wx/math.sqrt(S['a0']):.4e}   {wy:.4e}  {sup:.3e}", flush=True)
