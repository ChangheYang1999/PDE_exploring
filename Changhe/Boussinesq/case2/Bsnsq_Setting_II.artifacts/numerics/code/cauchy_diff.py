"""Cauchy differences between successive fitted states on fixed evaluation grids (do the fitted fields converge as N grows?).
For each state the fields are evaluated directly from the spectral basis on seven polar product grids:
  patch  : r in [11, 17] x th in [0.25, 0.55] rad (61 x 41 points; contains the located Q+ of the four negative-branch beta = 2
           states N112-N208, NOT the positive-branch Q+ at r = 10.1-10.3),
  core   : r in [0.01, 30] (log-spaced, 120) x th in (0, pi/2) (48 midpoints),
  inner  : r in [0.01, 2] (60) x th (32 midpoints), and the bands r in [2, 5], [5, 15], [15, 30], [30, 100] (48 midpoint angles).
'sup' is a maximum over the finite grid; vector fields use Euclidean lengths pointwise in numerator and denominator; the W
denominator includes the dilation beta X. If a denominator vanishes the relative value is reported as undefined (absolute kept).
DW is not compared (not a C^1 comparison of W); the grids omit the origin, the axes and r > 100 (external referee).
For successive pairs (N, N') the relative sup differences  sup|F_N' - F_N| / sup|F_N'|  over each grid are printed for
F = Theta, grad Theta (Euclidean norm of the difference), Omega, W (Euclidean norm of the difference), together with sup|F_N'|.
Sampled, fitted-state data: a decreasing sequence of differences is consistent with convergence, it does not prove it, and
it says nothing about profiles."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

GRIDS = {
 'patch': (np.linspace(11, 17, 61), np.linspace(0.25, 0.55, 41)),
 'core':  (np.geomspace(0.01, 30, 120), (np.arange(48) + 0.5) * (np.pi / 2) / 48),
 'inner': (np.geomspace(0.01, 2, 60), (np.arange(32) + 0.5) * (np.pi / 2) / 32),
 'band 2-5':   (np.linspace(2, 5, 40), (np.arange(48) + 0.5) * (np.pi / 2) / 48),
 'band 5-15':  (np.linspace(5, 15, 60), (np.arange(48) + 0.5) * (np.pi / 2) / 48),
 'band 15-30': (np.linspace(15, 30, 60), (np.arange(48) + 0.5) * (np.pi / 2) / 48),
 'band 30-100': (np.geomspace(30, 100, 40), (np.arange(48) + 0.5) * (np.pi / 2) / 48),
}

def fields_on(d, r, th):
    m, f = eval_state(d, r, th)
    F = {k: f[k].cpu().numpy() for k in ('a', 'a_x', 'a_y', 'G', 'W1', 'W2')}
    R, T = np.meshgrid(r, th, indexing='ij'); X = R * np.cos(T); Y = R * np.sin(T)
    Th = X**2 * Y * F['a']; Tx = 2 * X * Y * F['a'] + X**2 * Y * F['a_x']; Ty = X**2 * F['a'] + X**2 * Y * F['a_y']
    return dict(Theta=Th, gradTheta=np.stack([Tx, Ty]), Omega=X * Y * F['G'], W=np.stack([F['W1'], F['W2']]))

def main(paths):
    ds = [load_state(p) for p in paths]; names = [p.split('/')[-1].replace('.npz', '') for p in paths]
    print("states:", ", ".join(f"{n} (N={int(d['N'])}, M={int(d['M'])}, beta={float(d['beta']):.4f})" for n, d in zip(names, ds)))
    for gname, (r, th) in GRIDS.items():
        vals = [fields_on(d, r, th) for d in ds]
        print(f" grid {gname}: r in [{r[0]:.3g}, {r[-1]:.3g}] ({len(r)}), th in [{th[0]:.3f}, {th[-1]:.3f}] ({len(th)})")
        print("   pair                         Theta: rel.sup.diff (sup|F|)   gradTheta            Omega                W")
        for i in range(1, len(ds)):
            row = []
            for key in ('Theta', 'gradTheta', 'Omega', 'W'):
                A, B = vals[i - 1][key], vals[i][key]
                if A.ndim == 3: diff = np.linalg.norm(B - A, axis=0).max(); supB = np.linalg.norm(B, axis=0).max()
                else: diff = np.abs(B - A).max(); supB = np.abs(B).max()
                row.append(f"{diff/supB:9.3e} ({supB:8.3e})" if supB > 0 else f"undefined (abs {diff:8.3e})")
            print(f"   {names[i-1][:12]:>12} -> {names[i][:12]:<12} " + "  ".join(row))

if __name__ == '__main__': main(sys.argv[1:])
