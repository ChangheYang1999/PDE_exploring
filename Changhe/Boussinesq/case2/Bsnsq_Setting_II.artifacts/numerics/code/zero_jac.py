"""Exact pointwise diagnostics (refereed by an external referee: formulas confirmed; axis parity, spiral case, tolerances and heuristic labels repaired) at the zeros of W of a saved state (analysis 22:45Z and 00:03Z requests).
 For every zero Q of W in the closed first quadrant (axis zeros and interior zeros, r < 300):
   Omega(Q), Theta_x(Q), Omega(Q) - Theta_x(Q)  [equation (V) gives Omega(Q) = Theta_x(Q) exactly at a zero of W],
   |grad Theta(Q)|, Theta(Q), DW(Q) (polar 3x3 stencil of the exact spectral evaluation, central differences, relative
   step h), its eigenvalues (exact trace 2 beta), the FD trace defect, and the eigenvectors.
 For the interior zero Q+ closest to the x-axis stagnation segment (beta = 2: the numerical endpoint of the arc):
   centre direction e_c = eigenvector of the eigenvalue of smaller modulus, oriented away from P = (x*, 0);
   W(Q+ + eps e_c).e_c for several eps (> 0: outgoing, < 0: incoming) on both sides; Omega and Theta - Theta(Q+) on a small
   half-disc beyond Q+ (angles within pi/2 of e_c), radii 0.05 .. 1.
 For a companion zero P' within distance 2 of P: eigenvalues as above and a transversal test of the zero curve P -> P':
   min |W| along perpendicular transversals through the segment, relative to |W| at the transversal ends.
 Nothing here is a solution test by itself; it measures the fitted states against the exact structural identities."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state
from charcheck import build, evalW
from scipy.optimize import fsolve, brentq

def point_data_batch(d, pts, h=1e-5):
    """exact fields at the points pts = [(x, y), ...] and DW by central differences on polar 3x3 stencils (relative step h);
    one model build for all points (the product grid of all stencil radii and angles)"""
    beta = float(d['beta']); n = len(pts)
    if n == 0: return []
    r0 = np.array([np.hypot(x, y) for (x, y) in pts]); t0 = np.array([np.arctan2(y, x) for (x, y) in pts])
    rr = np.concatenate([[r * (1 - h), r, r * (1 + h)] for r in r0]); tt = np.concatenate([[t - h, t, t + h] for t in t0])
    tt = np.clip(tt, 1e-12, np.pi / 2 - 1e-12)
    m, f = eval_state(d, rr, tt)
    g = {k: f[k].cpu().numpy() for k in ('W1', 'W2', 'a', 'a_x', 'a_y', 'G', 'w1', 'w2')}
    out = []
    for k in range(n):
        axis = 'x' if pts[k][1] < 1e-6 else ('y' if pts[k][0] < 1e-6 else None)
        sl = slice(3 * k, 3 * k + 3); r_ = rr[sl]; t_ = tt[sl]; c, s = np.cos(t0[k]), np.sin(t0[k])
        X = r0[k] * c; Y = r0[k] * s
        def grad(F):
            F = F[sl, sl]
            F_r = (F[2, 1] - F[0, 1]) / (r_[2] - r_[0]); F_t = (F[1, 2] - F[1, 0]) / (t_[2] - t_[0])
            return c * F_r - s * F_t / r0[k], s * F_r + c * F_t / r0[k]
        W1x, W1y = grad(g['W1']); W2x, W2y = grad(g['W2'])
        if axis == 'x':   # parity: W1 even in y, W2 odd in y; d_y W2(x,0) = w2(x,0) = W2/y exactly (angular stencil clipped at the axis)
            W1y = 0.0; W2x = 0.0; W2y = g['w2'][sl, sl][1, 1]
        elif axis == 'y':
            W1y = 0.0; W2x = 0.0; W1x = g['w1'][sl, sl][1, 1]
        DW = np.array([[W1x, W1y], [W2x, W2y]])
        a = g['a'][sl, sl][1, 1]; ax = g['a_x'][sl, sl][1, 1]; ay = g['a_y'][sl, sl][1, 1]; G = g['G'][sl, sl][1, 1]
        Theta = X * X * Y * a; Theta_x = 2 * X * Y * a + X * X * Y * ax; Theta_y = X * X * a + X * X * Y * ay
        Omega = X * Y * G
        ev, V = np.linalg.eig(DW)
        out.append(dict(x=X, y=Y, W1=g['W1'][sl, sl][1, 1], W2=g['W2'][sl, sl][1, 1], Theta=Theta, Theta_x=Theta_x, Theta_y=Theta_y,
                        Omega=Omega, a=a, G=G, DW=DW, ev=ev, V=V, tr_defect=np.trace(DW) - 2 * beta, det=np.linalg.det(DW)))
    return out

def newton_polish(B, x, y):
    """Newton on the spline evaluator with FD Jacobian (relative step 1e-6)"""
    for it in range(12):
        o = evalW(B, np.array([x]), np.array([y])); F = np.array([o['W1'][0], o['W2'][0]])
        hx = 1e-6 * max(x, 1e-3); hy = 1e-6 * max(y, 1e-3)
        ox = evalW(B, np.array([x + hx, x - hx]), np.array([y, y])); oy = evalW(B, np.array([x, x]), np.array([y + hy, y - hy]))
        J = np.array([[(ox['W1'][0] - ox['W1'][1]) / (2 * hx), (oy['W1'][0] - oy['W1'][1]) / (2 * hy)],
                      [(ox['W2'][0] - ox['W2'][1]) / (2 * hx), (oy['W2'][0] - oy['W2'][1]) / (2 * hy)]])
        dx = np.linalg.solve(J, -F); x += dx[0]; y += dx[1]
        if np.hypot(*dx) < 1e-14 * max(1.0, np.hypot(x, y)): break
    return x, y

def find_zeros(d, B):
    r = np.geomspace(0.05, 300, 260); th = np.linspace(0.0, np.pi / 2, 181)
    m, f = eval_state(d, r, th)
    W1 = f['W1'].cpu().numpy(); W2 = f['W2'].cpu().numpy(); X = f['x'].cpu().numpy(); Y = f['y'].cpu().numpy()
    w1ax = f['w1'][:, 0].cpu().numpy(); w2ax = f['w2'][:, -1].cpu().numpy()
    W1x = lambda x: evalW(B, np.array([x]), np.array([1e-12]))['W1'][0] / x
    W2y = lambda y: evalW(B, np.array([1e-12]), np.array([y]))['W2'][0] / y
    zx = [float(brentq(W1x, r[i], r[i + 1], xtol=1e-12)) for i in np.where(np.diff(np.sign(w1ax)) != 0)[0]]
    zy = [float(brentq(W2y, r[i], r[i + 1], xtol=1e-12)) for i in np.where(np.diff(np.sign(w2ax)) != 0)[0]]
    s1 = np.sign(W1); s2 = np.sign(W2); cand = []
    for i in range(len(r) - 1):
        for j in range(1, len(th) - 2):
            c1 = (s1[i, j] != s1[i + 1, j]) or (s1[i, j] != s1[i, j + 1])
            c2 = (s2[i, j] != s2[i + 1, j]) or (s2[i, j] != s2[i, j + 1])
            if c1 and c2: cand.append((X[i, j], Y[i, j]))
    def Wfun(p):
        o = evalW(B, np.array([max(p[0], 1e-9)]), np.array([max(p[1], 1e-9)])); return [o['W1'][0], o['W2'][0]]
    pts = []
    for (x0, y0) in cand[:300]:
        sol, info, ier, msg = fsolve(Wfun, [x0, y0], full_output=True, xtol=1e-12)
        if ier == 1 and sol[0] > 1e-3 and sol[1] > 1e-3 and np.hypot(*Wfun(sol)) < 1e-8:
            if not any(np.hypot(sol[0] - p[0], sol[1] - p[1]) < 1e-3 for p in pts): pts.append((float(sol[0]), float(sol[1])))
    # polish each interior zero with the exact evaluator (Newton on the spectral fields)
    out = [newton_polish(B, x, y) for (x, y) in pts]
    return zx, zy, out

def report(d, B, name):
    beta = float(d['beta']); a0 = float(np.sign(float(d['a0_target']))) if 'a0_target' in d else 1.0
    zx, zy, zs = find_zeros(d, B)
    print(f"=== {name}: N={int(d['N'])} M={int(d['M'])} beta={beta}  a0 sign={a0:+.0f}")
    print(f"  x-axis zeros: {np.round(zx, 5)};  y-axis zeros: {np.round(zy, 5)}")
    allpts = [(x1, 1e-9) for x1 in zx] + [(1e-9, y1) for y1 in zy] + list(zs)
    Q = point_data_batch(d, allpts)
    qx = Q[:len(zx)]; qy = Q[len(zx):len(zx) + len(zy)]; qz = Q[len(zx) + len(zy):]
    P = np.array([zx[0], 0.0]) if zx else None
    for k, (x1, q) in enumerate(zip(zx, qx)):
        print(f"  P{k+1}=({x1:.5f}, 0): DW eigen = {np.sort(q['ev'].real)} (exact at a zero with Theta_y != 0 there: {beta+2:.4f} and {beta-2:.4f}); d_xW1={q['DW'][0,0]:+.5f} d_yW2={q['DW'][1,1]:+.5f} d_yW1={q['DW'][0,1]:+.2e} d_xW2={q['DW'][1,0]:+.2e}; tr-2beta={q['tr_defect']:+.2e}; Theta_y(P)={q['Theta_y']:+.4e}")
    for k, (y1, q) in enumerate(zip(zy, qy)):
        print(f"  Y{k+1}=(0, {y1:.5f}): DW eigen = {np.sort(q['ev'].real)}; d_yW2={q['DW'][1,1]:+.5f} (exact if y a(0,y) vanishes to finite order m there: -(3beta+2)/(m-2)); tr-2beta={q['tr_defect']:+.2e}; Theta_xx(0,y1)=2 y a={2*y1*q['a']:+.4e}")
    print(f"  interior zeros FOUND (grid search r in [0.05, 300], 181 angles, fsolve + Newton polish on the spline evaluator; |W| below is the exact spectral value at the polished point): {len(zs)}")
    rows = []
    for (x, y), q in zip(zs, qz):
        ev = q['ev']
        cplx = np.abs(ev.imag).max() > 1e-6 * np.abs(ev).max()
        evs = np.sort_complex(ev) if cplx else np.sort(ev.real)
        gT = np.hypot(q['Theta_x'], q['Theta_y'])
        tol = 1e-6 * max(np.abs(ev).max(), 1.0)
        if np.abs(ev.real).min() < tol: kind = 'nonhyperbolic (a real part within tolerance of 0)'
        elif cplx: kind = 'spiral ' + ('source' if ev.real[0] > 0 else 'sink')
        elif ev.real.min() < 0 < ev.real.max(): kind = 'saddle'
        elif (ev.real > 0).all(): kind = 'source'
        else: kind = 'sink'
        print(f"   Q=({x:.5f},{y:.5f}) r={np.hypot(x,y):.3f}: Theta={q['Theta']:+.4e} Omega={q['Omega']:+.4e} Theta_x={q['Theta_x']:+.4e} "
              f"Omega-Theta_x={q['Omega']-q['Theta_x']:+.4e} |gradTheta|={gT:.4e} (Theta_y={q['Theta_y']:+.4e}); "
              f"DW eig={np.array2string(np.asarray(evs), precision=5)} [{kind}] det={q['det']:+.4e} tr-2beta={q['tr_defect']:+.2e} |W|={np.hypot(q['W1'],q['W2']):.1e}")
        rows.append((x, y, q))
    far = [(x, y, q) for (x, y, q) in rows if P is None or np.hypot(x - P[0], y - P[1]) > 2.0]
    if far:
        # Q+ := the interior zero farther than 2 from P with the largest |Theta| (at beta = 2 this is the numerical endpoint of the arc)
        x, y, q = max(far, key=lambda t: abs(t[2]['Theta']))
        ev = q['ev']; cplx = np.abs(ev.imag).max() > 1e-6 * np.abs(ev).max()
        print(f"  Q+ := interior zero with the largest |Theta| farther than 2 from P: ({x:.5f},{y:.5f}); DW eigenvalues {np.array2string(ev, precision=5)}")
        print("   radial outward projection W(Q+ + rho e(phi)).e(phi) on sampled circles (72 angles, those inside Q1): min / max (> 0 everywhere: outgoing in every direction)")
        for rho in [0.01, 0.03, 0.1, 0.3, 1.0]:
            ang = np.linspace(0, 2 * np.pi, 72, endpoint=False); xx = x + rho * np.cos(ang); yy = y + rho * np.sin(ang); ok = (xx > 0) & (yy > 0)
            o = evalW(B, xx[ok], yy[ok], need_fields=True); pr = o['W1'] * np.cos(ang[ok]) + o['W2'] * np.sin(ang[ok])
            print(f"     rho={rho:.2f}: W.e_r in [{pr.min():+.3e}, {pr.max():+.3e}] (min at phi={np.degrees(ang[ok][np.argmin(pr)]):.0f} deg);  Omega in [{o['Omega'].min():+.3e}, {o['Omega'].max():+.3e}];  Theta-Theta(Q+) in [{(o['Theta']-q['Theta']).min():+.3e}, {(o['Theta']-q['Theta']).max():+.3e}]  (sampled circle, not a disc bound)")
        if not cplx:
            evr = ev.real; V = q['V'].real
            ic = int(np.argmin(np.abs(evr))); ec = V[:, ic] / np.linalg.norm(V[:, ic])
            if P is not None and np.dot(ec, np.array([x, y]) - P) < 0: ec = -ec
            eo = V[:, 1 - ic] / np.linalg.norm(V[:, 1 - ic])
            print(f"   real spectrum: weaker eigendirection e_w={np.round(ec,5)} (eigenvalue {evr[ic]:+.5f}; a centre direction only if this eigenvalue is 0), oriented away from P; other {evr[1-ic]:+.5f}, e={np.round(eo,5)}")
            print("   along e_w (+ = beyond Q+, away from P; - = towards P); signed outward projection > 0 means the flow points away from Q+ there:")
            for eps in [0.01, 0.03, 0.1, 0.3, 1.0, 3.0]:
                for sgn in (+1, -1):
                    xx, yy = x + sgn * eps * ec[0], y + sgn * eps * ec[1]
                    if xx <= 0 or yy <= 0: print(f"     eps={sgn*eps:+.2f}: outside Q1"); continue
                    o = evalW(B, np.array([xx]), np.array([yy]), need_fields=True)
                    wc = (o['W1'][0] * ec[0] + o['W2'][0] * ec[1]) * sgn
                    print(f"     eps={sgn*eps:+.2f}: W.e_w(signed outward)={wc:+.3e} |W|={np.hypot(o['W1'][0],o['W2'][0]):.2e} Omega={o['Omega'][0]:+.3e} Theta-Theta(Q+)={o['Theta'][0]-q['Theta']:+.3e}")
        else:
            print("   complex spectrum (spiral): no centre or eigendirection exists; the circle projections above answer the outgoing/incoming question.")
    near = [(x, y, q) for (x, y, q) in rows if P is not None and np.hypot(x - P[0], y - P[1]) <= 2.0]
    for (x, y, q) in near:
        seg = np.array([x, y]) - P; Ls = np.linalg.norm(seg); tvec = seg / Ls; nvec = np.array([-tvec[1], tvec[0]])
        print(f"  companion zero P'=({x:.5f},{y:.5f}) at distance {Ls:.4f} from P; DW eig {np.sort(q['ev'].real)} (exact on an arc: 0 and {2*beta:.1f})")
        print("   transversal test (HEURISTIC: a resolved zero curve gives min|W| ~ evaluation error along every transversal; a small but nonzero ratio does not decide) of a zero curve P -> P' (perpendicular transversals of half-length 0.25|PP'| at fractions s):")
        for sfr in [0.25, 0.5, 0.75]:
            C = P + sfr * seg; tt = np.linspace(-0.25 * Ls, 0.25 * Ls, 101)
            xx = C[0] + tt * nvec[0]; yy = C[1] + tt * nvec[1]; ok = (xx > 0) & (yy > 0)
            o = evalW(B, xx[ok], yy[ok]); aw = np.hypot(o['W1'], o['W2'])
            i0 = int(np.argmin(aw)); oc = evalW(B, np.array([C[0]]), np.array([max(C[1], 1e-12)]))
            print(f"     s={sfr:.2f}: |W| on the segment point={np.hypot(oc['W1'][0],oc['W2'][0]):.3e}; min|W| along the transversal={aw.min():.3e} at offset {tt[ok][i0]:+.4f}; |W| at the ends={aw[0]:.3e}/{aw[-1]:.3e}; ratios min/end={aw.min()/aw[0]:.3f}, {aw.min()/aw[-1]:.3f}")
        tt = np.linspace(0, 1, 11); xx = P[0] + tt * seg[0]; yy = P[1] + tt * seg[1]
        o = evalW(B, np.maximum(xx, 1e-9), np.maximum(yy, 1e-9))
        print("     |W| along P -> P' at s=0..1: " + " ".join(f"{v:.1e}" for v in np.hypot(o['W1'], o['W2'])))
    sys.stdout.flush()

if __name__ == '__main__':
    for path in sys.argv[1:]:
        d = load_state(path); B = build(d, rmin=1e-3, rmax=1e4, nr=4000)
        report(d, B, path)
