"""Independent FLOAT scan of theta = ess sup (|grad rho| - rho_y)/2 and of kappa-related integrals for (B-L2) of
FW-T-T4L2-v1 (theory_v01 section 8), from the exact compactified polynomials of rho_x, rho_y (lane c1-n3).
FLOAT only: the sup is sampled on a polar grid (t and theta); not a bound."""
from pathlib import Path
from fractions import Fraction as Q
import json, sys, time
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E

def radial_values(Dfield, delta, ts, has_r, prec=1500):
    """For each key (ell, kind, n) of a compactified field and each t in ts, the radial factor
    (1-t)^(ell delta/2) P(t) [times r for degree-3 fields], evaluated in ball arithmetic (the polynomials have
    coefficients with thousands of digits and cancel massively; float64 evaluation is meaningless). Returns
    {key: numpy array of float64 midpoints} and the maximal radius of the balls (as a float)."""
    from flint import arb, ctx
    old = ctx.prec; ctx.prec = prec
    out = {}; maxrad = 0.0
    tsa = [arb(str(t)) for t in ts]
    for key, p in Dfield.items():
        ell = key[0]
        co = [arb(str(c.p)) / arb(str(c.q)) for c in p.coeffs()]
        vals = []
        for ta in tsa:
            v = arb(0)
            for c in reversed(co): v = v * ta + c
            v *= (1 - ta) ** (arb(ell) * arb(str(delta.numerator)) / arb(str(delta.denominator)) / 2)
            if has_r: v *= (ta / (1 - ta)).sqrt()
            maxrad = max(maxrad, float(v.rad()))
            vals.append(float(v.mid()))
        out[key] = np.array(vals)
    ctx.prec = old
    return out, maxrad

def field_grid(Dfield, delta, ts, th, has_r, prec=1500):
    rv, maxrad = radial_values(Dfield, delta, ts, has_r, prec)
    vals = np.zeros((len(ts), len(th)))
    for (ell, kind, n), pv in rv.items():
        ang = np.sin(n * th) if kind == 's' else np.cos(n * th)
        vals += np.outer(pv, ang)
    return vals, maxrad

def run(source, ID, outdir, nt=240, nth=91):
    t0 = time.monotonic(); c, A, src_sha, can_sha, meta = E.load_reference(source); delta = 1 - 1 / c
    gamma = 1 / c
    j4 = {nx: E.chi_compact(A, c, 4, nx) for nx in range(4)}
    rx = E.plus((-1, j4[1]), (-1, j4[3])); ry = E.plus((-1, j4[0]), (-1, j4[2]))
    # grid: t in (0,1) dense near both ends: use s = log r uniformly in [-6, 12] plus the origin limit
    rs = np.exp(np.linspace(-4, 9, nt)); ts = [Q(float(r)) ** 2 / (1 + Q(float(r)) ** 2) for r in rs]; th = np.linspace(0, np.pi / 2, nth)
    RX, radx = field_grid(rx, delta, ts, th, False); RY, rady = field_grid(ry, delta, ts, th, False)
    print(f'radial ball radii at most {radx:.2e}, {rady:.2e}', flush=True)
    grad = np.sqrt(RX ** 2 + RY ** 2); theta_field = (grad - RY) / 2
    i, j = np.unravel_index(np.argmax(theta_field), theta_field.shape)
    out = {'id': ID, 'source_sha256': src_sha, 'canonical_sha256': can_sha, 'label': 'FLOAT (sampled sup on a polar grid, quadrant, s = log r in [-4, 9] x theta in [0, pi/2]; radial factors in 1500-bit ball arithmetic, angular synthesis float64)',
           'grid': [nt, nth], 'theta_sampled_sup': float(theta_field.max()), 'at_r': float(rs[i]), 'at_theta': float(th[j]),
           'rho_y_min_sampled': float(RY.min()), 'rho_y_min_at_r': float(rs[np.unravel_index(np.argmin(RY), RY.shape)[0]]),
           'sup_grad_rho_sampled': float(grad.max()), 'a0_from_axis_limit_check': float(RY[0, nth - 1]), 'radial_ball_radius_max': max(radx, rady),
           'elapsed': time.monotonic() - t0}
    Path(outdir, f'{ID}_theta_scan.json').write_text(json.dumps(out, indent=1) + '\n')
    print(json.dumps(out, indent=1))

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3])
