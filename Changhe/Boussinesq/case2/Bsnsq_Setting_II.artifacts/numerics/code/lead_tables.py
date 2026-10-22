"""Lead request 14:21Z: for a family of states, tabulate x*, mu-(beta+2), f(x*) = Theta_y(x*,0), max f on [0.9x*,1.1x*],
locations of the top-5 desingularized residual maxima; and the correlation of normalized residual vectors between
consecutive states on a FIXED evaluation grid."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state, problem_from_state, dev, DT, make_model, rad_of_r
from diag_state import eval_state
from charcheck import build, find_xstar, evalW

def table(paths):
    print(f"{'state':30s} {'N':>4s} {'beta':>7s} {'x*':>9s} {'mu-(b+2)':>10s} {'f(x*)':>10s} {'max f [.9,1.1]x*':>16s}  top-5 residual maxima (r, phi, |Ra| or |RG|)")
    resid_vecs = {}
    for p in paths:
        d = load_state(p); prob, z = problem_from_state(d); ca, cG, beta = prob.unpack(z); beta = float(beta)
        B = build(d, nr=3000); xs, lam = find_xstar(B)
        xx = np.linspace(0.9 * xs, 1.1 * xs, 201)
        o = evalW(B, xx, np.full_like(xx, 1e-9), need_fields=True); fvals = xx ** 2 * o['a']
        fstar = float(np.interp(xs, xx, fvals))
        f = prob.model.fields(ca, cG, beta)
        R = np.hypot(f['x'].cpu().numpy(), f['y'].cpu().numpy()); PH = np.arctan2(f['y'].cpu().numpy(), f['x'].cpu().numpy())
        Ra = np.abs(f['Ra'].cpu().numpy()); RG = np.abs(f['RG'].cpu().numpy())
        tops = []
        for arr, nm in [(Ra, 'Ra'), (RG, 'RG')]:
            idx = np.argsort(arr.ravel())[::-1][:5]
            tops += [(arr.ravel()[i], R.ravel()[i], PH.ravel()[i], nm) for i in idx]
        tops = sorted(tops, key=lambda t: -t[0])[:5]
        tstr = "; ".join(f"({t[1]:.2f},{t[2]:.2f},{t[3]} {t[0]:.1e})" for t in tops)
        print(f"{p.split('/')[-1][:-4]:30s} {int(d['N']):4d} {beta:7.4f} {xs:9.4f} {lam-(beta+2):+10.5f} {fstar:10.4f} {fvals.max():16.4f}  {tstr}")
        # residual vector on a fixed grid: r in geomspace(0.1, 60, 40) x 16 angles, desingularized Ra and RG
        rg = np.geomspace(0.1, 60, 40); tg = np.linspace(0.05, np.pi / 2 - 0.05, 16)
        m2, f2 = eval_state(d, rg, tg)
        resid_vecs[p] = np.concatenate([f2['Ra'].cpu().numpy().ravel(), f2['RG'].cpu().numpy().ravel()])
    keys = list(resid_vecs.keys())
    for i in range(len(keys) - 1):
        a, b = resid_vecs[keys[i]], resid_vecs[keys[i + 1]]
        corr = float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
        print(f"  residual-direction correlation {keys[i].split('/')[-1][:-4]} -> {keys[i+1].split('/')[-1][:-4]}: {corr:+.4f}  (|r| {np.linalg.norm(a):.3e} -> {np.linalg.norm(b):.3e})")

if __name__ == '__main__':
    print("## better family beta = 3"); table(['runs/I5_fix3_gauss.npz', 'runs/R1_fix3_N64M16_fromI5.npz', 'runs/R2_fix3_N80M20_fromR1.npz', 'runs/R4_fix3_N112M28.npz', 'runs/R5_fix3_N144M36.npz'])
    print("## control beta = 1.9431 (excluded)"); table(['runs/K0_fix1.94_N48M12.npz', 'runs/K1_fix1.94_N64M16.npz', 'runs/K2_fix1.94_N80M20.npz', 'runs/K3_fix1.94_N112M28.npz'])
    print("## interior-only fits beta = 3"); table(['runs/W1_fix3_N64_wmax1.npz', 'runs/W3_fix3_N80_wmax1.npz', 'runs/W4_fix3_N112_wmax1.npz'])
