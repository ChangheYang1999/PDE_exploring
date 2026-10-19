import sys, numpy as np
for fn in sys.argv[1:]:
    z = np.load(fn)
    r, th = z['r'], z['theta']; rr = r[:, None] + 0*th; T = th[None, :] + 0*rr
    nr = z['residual'] / np.where(z['denominator'] > 0, z['denominator'], np.inf)
    if "rho_x" not in z.files:
        R = z["residual"]; den2 = z["denominator"]
    else:
        R = z["W1"]*z["rho_x"] + z["W2"]*z["rho_y"] - z["rho"]
        den2 = np.abs(z["W1"]*z["rho_x"]) + np.abs(z["W2"]*z["rho_y"]) + np.abs(z["rho"])
    alt = np.where(den2 > 0, R / np.where(den2>0, den2, 1), 0)
    inside = (T > 0) & (T < np.pi/2 - 1e-12)
    out = []
    for m in [rr <= 2, (rr >= 2) & (rr <= 10), (rr >= 10) & (rr <= 1000)]:
        mm = m & inside
        out.append(f'{np.abs(nr[mm]).max():.1e}/{np.abs(alt[mm]).max():.1e}')
    print(f'{fn.split("/")[-1]:38s} nr={len(r)} nt={len(th)} c_l={float(z["c_l"]):.7f}  max elog/dlog | FD-alt  [r<=2] {out[0]}  [2,10] {out[1]}  [10,1000] {out[2]}')
