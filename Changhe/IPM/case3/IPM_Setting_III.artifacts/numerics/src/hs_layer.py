"""hs_layer.py -- near-axis structure of the canonical hydrostatic residual of the saved TRIAL STATES (lead 11:47Z item (3); diagnostic only, nothing about solutions).
Question: at several radii y, is |R_h|/N_f near the vertical axis a function of the inner variable z = xi / y^((p+1)/2) (an angular layer of shrinking width
delta ~ y^((p-1)/2), as in the lead's inner problem) or of the angle delta = pi/2 - theta (a fixed angular profile)?  For each y the residual is sampled on a
z-grid and on a delta-grid; the row shapes (normalised by the row maximum) are compared between consecutive radii in both variables, and the row maxima,
their locations (z_max, delta_max) and the log-log growth of the maxima with y are printed.
Inverse: V_1 = -int_y^inf g_xi dt, V_2 = int_0^y t g_xixi dt + y int_y^inf g_xixi dt with the inner integral by Gauss-Legendre on [0, min(1, y)] PLUS a composite
log-spaced Gauss rule on [1, y] (the default hs.hydro_V inner rule, n Gauss points on [0, y], misses the core t ~ 1 when y >> 1: errors 6e-3 at y = 1e3 and 0.3 at
y = 1e4 in V_2(0, y) for the 96x24 c = 3 state, hs_m0 check), tail by the algebraic map of hs.hydro_V, g_xixi by central differences with the r-scaled step.
Validation: manufactured field (exact V), the exact axis primitive at xi = 0 (hs_m0.AxisPrimitive), and hs.hydro_V with n_in = 1024.
Usage: python3 src/hs_layer.py runs/hsE_c3.0_N128_hr.pt ..."""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve, hs, hs_m0
torch.set_default_dtype(torch.float64)

def hydro_V_log(gfun, X, Y, n0=32, per_decade=10, ngl=16, n_tail=400, q=3, hrel=1e-5, ymax_dec=None):
    # NOTE (shift 6, 19:50Z): with q = 3 the tail rule is converged to about 4e-7 absolute in V_1 at n_tail = 400 but becomes UNRELIABLE for n_tail >= 1600 (far-node
    # contributions at t beyond about 1e18 drift: inner V_1 moves by 3e-4 from 400 to 3200 points); q = 2 is stable to 3e-8 for 400 .. 3200 points.  Do not 'refine' q = 3 by adding points.
    shp = np.asarray(X).shape; X = np.asarray(X, dtype=np.float64).reshape(-1); Y = np.asarray(Y, dtype=np.float64).reshape(-1); sy = np.where(Y < 0, -1.0, 1.0); y = np.abs(Y); npts = len(X)
    def gx_gxx(xx, tt):
        h = hrel * (1 + np.hypot(xx, tt)); _, gxp, _ = gfun(xx + h, tt); _, gxm, _ = gfun(xx - h, tt); _, gx0, _ = gfun(xx, tt); return gx0, (gxp - gxm) / (2 * h)
    # inner: [0, min(1, y)] Gauss (n0) + log panels on [1, y] (n_pan panels, ngl points each; weights zero when y <= 1)
    u0, w0 = np.polynomial.legendre.leggauss(n0); u0 = 0.5 * (u0 + 1); w0 = 0.5 * w0
    y1 = np.minimum(1.0, y); T0 = y1[:, None] * u0[None, :]; W0 = y1[:, None] * w0[None, :]
    dec = np.log10(max(y.max(), 10.0)) if ymax_dec is None else ymax_dec; n_pan = int(math.ceil(per_decade * dec)); xg, wg = np.polynomial.legendre.leggauss(ngl)
    ly = np.log(np.maximum(y, 1.0)); edges = ly[:, None] * np.linspace(0, 1, n_pan + 1)[None, :]                      # (npts, n_pan+1) in log t
    a = edges[:, :-1]; b = edges[:, 1:]; XL = 0.5 * (b - a)[:, :, None] * xg[None, None, :] + 0.5 * (a + b)[:, :, None]; TL = np.exp(XL)
    WL = (0.5 * (b - a))[:, :, None] * wg[None, None, :] * TL                                                             # dt = t dx
    T_in = np.concatenate([T0, TL.reshape(npts, -1)], 1); W_in = np.concatenate([W0, WL.reshape(npts, -1)], 1); nin = T_in.shape[1]
    _, gxx_in = gx_gxx(np.repeat(X[:, None], nin, 1).reshape(-1), T_in.reshape(-1)); I_in = (W_in * T_in * gxx_in.reshape(npts, nin)).sum(1)
    ut, wt = np.polynomial.legendre.leggauss(n_tail); ut = 0.5 * (ut + 1); wt = 0.5 * wt
    Lt = 1.0 + y; s = (ut / (1 - ut)) ** q; ds = q * ut ** (q - 1) / (1 - ut) ** (q + 1)
    T_t = y[:, None] + Lt[:, None] * s[None, :]; W_t = Lt[:, None] * (wt * ds)[None, :]
    gx_t, gxx_t = gx_gxx(np.repeat(X[:, None], n_tail, 1).reshape(-1), T_t.reshape(-1)); gx_t = gx_t.reshape(npts, n_tail); gxx_t = gxx_t.reshape(npts, n_tail)
    return (-(W_t * gx_t).sum(1)).reshape(shp), ((I_in + y * (W_t * gxx_t).sum(1)) * sy).reshape(shp)      # shapes of the input (sampled_table passes 2-D grids)

def residual(ge, c, X, Y):
    V1, V2 = hydro_V_log(ge, X, Y); g, gx, gy = ge(X, Y)
    R = (c * X + V1) * gx + (c * Y + V2) * gy - g; Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g)
    return R, Nf, V1, V2

def validate(m, u, c, ap):
    from scipy.special import erf
    tau = 1.0
    def gfun(X, Y):
        X = np.asarray(X, dtype=np.float64); Y = np.asarray(Y, dtype=np.float64); e = np.exp(-X ** 2) * np.exp(-tau * Y ** 2); return e * Y, -2 * X * e * Y, e * (1 - 2 * tau * Y ** 2)
    xs = np.array([0.0, 0.3, 0.7, 1.0, 1.5, 2.5]); ys = np.array([0.0, 0.2, 0.6, 1.0, 1.7, 3.0, 6.0]); XX, YY = np.meshgrid(xs, ys, indexing='ij')
    V1, V2 = hydro_V_log(gfun, XX, YY); V1e = XX * np.exp(-XX ** 2) * np.exp(-tau * YY ** 2) / tau; V2e = -(1 - 2 * XX ** 2) * np.exp(-XX ** 2) * math.sqrt(math.pi) * erf(math.sqrt(tau) * YY) / (2 * tau ** 1.5)
    out = dict(manufactured=(float(np.abs(V1 - V1e).max()), float(np.abs(V2 - V2e).max())))
    ge = hs.GEval(m, m.beta_full(u)); ya = np.array([10.0, 1e2, 1e3, 1e4, 1e5]); _, V2a = hydro_V_log(ge, np.zeros(5), ya); ye, V2e_, _ = ap.V2_axis(ymax=1e6)
    out['axis_vs_primitive'] = [(float(yy), float(a), float(b)) for yy, a, b in zip(ya, V2a, np.interp(np.log(ya), np.log(ye), V2e_))]
    Xc = np.array([30.0, 300.0, 1.0]); Yc = np.array([1e3, 1e4, 1e2]); V1l, V2l = hydro_V_log(ge, Xc, Yc); V1h, V2h = hs.hydro_V(ge, Xc, Yc, n_in=1024, n_tail=400, hrel=1e-5, hstep='r')
    out['vs_hydroV_1024'] = [(float(xx), float(yy), float(a), float(b), float(a2), float(b2)) for xx, yy, a, b, a2, b2 in zip(Xc, Yc, V1l, V1h, V2l, V2h)]
    return out

def analyse(f, radii=(10.0, 1e2, 3e2, 1e3, 3e3, 1e4, 3e4, 1e5, 1e6), verbose=True):
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev); p = 1.0 / c; tag = f.split('/')[-1][:-3]; alpha = (p + 1) / 2
    ge = hs.GEval(m, m.beta_full(u)); ap = hs_m0.AxisPrimitive(m, u); val = validate(m, u, c, ap)
    zs = np.array([0.0, 0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]); ds = np.array([0.0, 0.0005, 0.001, 0.002, 0.003, 0.005, 0.007, 0.01, 0.015, 0.02, 0.03, 0.05, 0.07, 0.1, 0.2, 0.5, 1.0])
    rows_z = []; rows_d = []
    for y in radii:
        X = zs * y ** alpha; Y = np.full_like(X, y); R, Nf, _, _ = residual(ge, c, X, Y); rows_z.append((y, R / Nf, np.abs(R)))
        X = y * np.tan(ds); Y = np.full_like(X, y); R, Nf, _, _ = residual(ge, c, X, Y); rows_d.append((y, R / Nf, np.abs(R)))
    out = dict(tag=tag, N=N, M=M, c=c, p=p, alpha=alpha, val=val, zs=zs, ds=ds, rows_z=rows_z, rows_d=rows_d)
    # shape comparison: normalise |R/N_f| rows by their maximum; distance between consecutive radii = max abs difference of the normalised rows (same grid in z, resp. delta)
    def shapes(rows): 
        S = [np.abs(q) / np.abs(q).max() for _, q, _ in rows]; return [float(np.abs(S[i + 1] - S[i]).max()) for i in range(len(S) - 1)], [float(np.abs(q).max()) for _, q, _ in rows], [int(np.argmax(np.abs(q))) for _, q, _ in rows]
    out['dist_z'], out['max_z'], out['arg_z'] = shapes(rows_z); out['dist_d'], out['max_d'], out['arg_d'] = shapes(rows_d)
    # location of the maximum in both variables for the z-rows: z_max and the corresponding delta = atan(z y^alpha / y); for the delta rows: delta_max and z = y tan(delta)/y^alpha
    out['loc_z'] = [(float(y), float(zs[i]), float(math.atan(zs[i] * y ** alpha / y))) for (y, _, _), i in zip(rows_z, out['arg_z'])]
    out['loc_d'] = [(float(y), float(ds[i]), float(y * math.tan(ds[i]) / y ** alpha)) for (y, _, _), i in zip(rows_d, out['arg_d'])]
    # widths: first grid position where |R/N_f| falls below half its axis value (linear interpolation) and first sign change, in z and in delta
    def widths(grid, rows):
        res = []
        for y, q, _ in rows:
            a = np.abs(q); half = 0.5 * a[0]
            if (a < half).any() and a[0] > 0:
                i = int(np.argmax(a < half)); wh = grid[i - 1] + (grid[i] - grid[i - 1]) * (a[i - 1] - half) / (a[i - 1] - a[i])     # interpolated crossing (a[i-1] >= half > a[i])
            else: wh = float('nan')                                                                                               # no crossing on the grid: undefined (referee m0ref)
            sc = np.where(np.sign(q[1:]) * np.sign(q[:-1]) < 0)[0]; j = sc[0] + 1 if len(sc) else None
            ws = grid[j - 1] + (grid[j] - grid[j - 1]) * q[j - 1] / (q[j - 1] - q[j]) if j is not None else float('nan')
            res.append((float(y), float(wh), float(ws)))
        return res
    out['width_z'] = widths(zs, rows_z); out['width_d'] = widths(ds, rows_d)
    def slope(ws, idx, ymin=1e3):
        yy = np.array([w[0] for w in ws]); vv = np.array([w[idx] for w in ws]); ok = np.isfinite(vv) & (vv > 0) & (yy >= ymin)
        return float(np.polyfit(np.log(yy[ok]), np.log(vv[ok]), 1)[0]) if ok.sum() >= 2 else float('nan')
    out['slope_half_z'], out['slope_sign_z'], out['slope_half_d'], out['slope_sign_d'] = slope(out['width_z'], 1), slope(out['width_z'], 2), slope(out['width_d'], 1), slope(out['width_d'], 2)
    ly = np.log(np.array(radii)); out['slope_max_z'] = float(np.polyfit(ly, np.log(np.array(out['max_z'])), 1)[0]); out['slope_max_d'] = float(np.polyfit(ly, np.log(np.array(out['max_d'])), 1)[0])
    if verbose:
        v = val
        print(f"\n=== {tag}  {N}x{M}  c = {c:.6f}  p = {p:.6f}  layer exponent (p+1)/2 = {alpha:.6f} (z = xi / y^{alpha:.4f}; layer angle delta ~ y^{(p-1)/2:+.4f})")
        print(f"  validation of hydro_V_log: manufactured max|V1 err| {v['manufactured'][0]:.1e}, max|V2 err| {v['manufactured'][1]:.1e};  axis V_2(0,y) vs exact primitive: " + "  ".join(f"y={yy:g}: {a:+.6e}/{b:+.6e}" for yy, a, b in v['axis_vs_primitive'])
              + ";  vs hs.hydro_V(n_in 1024): " + "  ".join(f"({xx:g},{yy:g}): V1 {a:+.5e}/{b:+.5e} V2 {a2:+.5e}/{b2:+.5e}" for xx, yy, a, b, a2, b2 in v['vs_hydroV_1024']))
        print("  R_h/N_f (signed) on the z-grid z = " + " ".join(f"{z:g}" for z in zs))
        for y, q, _ in rows_z: print(f"    y = {y:7.0e}: " + " ".join(f"{x:+.2e}" for x in q))
        print("  R_h/N_f (signed) on the delta-grid delta = " + " ".join(f"{d:g}" for d in ds))
        for y, q, _ in rows_d: print(f"    y = {y:7.0e}: " + " ".join(f"{x:+.2e}" for x in q))
        print("  |R_h| (absolute) on the z-grid:"); 
        for y, _, a in rows_z: print(f"    y = {y:7.0e}: " + " ".join(f"{x:.1e}" for x in a))
        print(f"  row maxima of |R_h|/N_f: z-rows " + " ".join(f"{x:.2e}" for x in out['max_z']) + f" (log-log slope in y {out['slope_max_z']:+.3f}); delta-rows " + " ".join(f"{x:.2e}" for x in out['max_d']) + f" (slope {out['slope_max_d']:+.3f})")
        print("  location of the row maximum: z-rows (y, z_max, delta at z_max): " + " ".join(f"({y:.0e}, {z:g}, {d:.2e})" for y, z, d in out['loc_z']) + ";  delta-rows (y, delta_max, z at delta_max): " + " ".join(f"({y:.0e}, {d:g}, {z:.2e})" for y, d, z in out['loc_d']))
        print("  half-width (|R/N_f| = half the axis value) and first sign change, in z: " + " ".join(f"(y={y:.0e}: {wh:.3g}, {ws:.3g})" for y, wh, ws in out['width_z']) + f"  -> log-log slopes over y >= 1e3: half {out['slope_half_z']:+.3f}, sign {out['slope_sign_z']:+.3f} (layer prediction 0)")
        print("  half-width and first sign change, in delta: " + " ".join(f"(y={y:.0e}: {wh:.3g}, {ws:.3g})" for y, wh, ws in out['width_d']) + f"  -> slopes over y >= 1e3: half {out['slope_half_d']:+.3f}, sign {out['slope_sign_d']:+.3f} (layer prediction (p-1)/2 = {(p-1)/2:+.4f}; fixed angular profile 0; first zero of the highest mode cos(2(M-1)theta) from the axis: pi/(4(M-1)) = {math.pi/(4*(M-1)):.4f})")
        print(f"  shape distance between consecutive radii (max |difference| of the rows normalised by their maxima): in z: " + " ".join(f"{x:.2f}" for x in out['dist_z']) + ";  in delta: " + " ".join(f"{x:.2f}" for x in out['dist_d']) + "   (small = collapse in that variable)")
    return out

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    print("# near-axis residual structure of hydrostatic TRIAL STATES (lead 11:47Z item (3)); z = xi / y^((p+1)/2) vs delta = pi/2 - theta; diagnostic only")
    for f in args: analyse(f)
