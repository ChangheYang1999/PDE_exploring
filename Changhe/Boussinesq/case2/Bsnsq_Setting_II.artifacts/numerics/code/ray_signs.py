"""Sampled ray sign diagnostics for supplied stored states (their beta range and rejected-state status are not checked here; the states
quoted in the numerical study are rejected fitted states, not profiles), for the hypotheses of the Theorems 64(b), 79 and 80: 'no ray
from the origin carries vorticity of signs (sigma, -sigma, sigma) at three increasing radii' (sigma = sgn(a0)) and 'the zero set
{Theta = 0} intersected with the open first quadrant Q1 has empty interior relative to Q1' (a continuous sign reversal of Theta along a ray
forces a zero inside Q1 but not an interior point of the zero set). Grid: 400 log radii in [0.5, 1e6] x 90 interior angles
theta_j = (j + 1/2) (pi/2)/90 (the grid of code/signs_beta3.py). sigma is the sign of the fitted a(0) (the origin coefficient of the state,
printed next to the target a0). For each angle the sign sequence of sigma G (= sign of sigma Omega, since x y > 0 at every sample) along
the sampled radii is scanned for the subsequence (+, -, +) (strict signs, increasing radii) and for (-, +, -); reported: the number of angles
whose sampled sequence contains each pattern, the min/max matching sampled angle, for (+, -, +) the earliest sampled third radius per matching
angle (min and max over those angles); the number of adjacent strict sign reversals along each ray (min / median / max over angles; transitions
through exact zeros are not counted). The same for sigma a (= sign of sigma Theta). Also the counts and fractions of sampled points with
negative sign by radial band and the fraction of angles with negative sign at the sampled radii nearest to selected values. Detected patterns
are numerical witnesses at sampled radii; their floating-point signs are uncertified; nondetection excludes neither unsampled patterns nor
patterns outside the sampled domain. These diagnostics do not establish properties of exact PDE profiles. Code reviewed by an external
referee; its repairs applied. Usage: python3 -u code/ray_signs.py state1.npz [...]"""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def has_pattern(s, pat):
    """does the sign sequence s (values in {-1, 0, 1}) contain pat as a subsequence (strict signs, increasing index)?"""
    if len(pat) == 0: return True
    i = 0
    for v in s:
        if v == pat[i]:
            i += 1
            if i == len(pat): return True
    return False

def main(paths):
    R = np.geomspace(0.5, 1e6, 400); T = (np.arange(90) + 0.5) * (np.pi / 2) / 90
    bands = ((0.5, 10), (10, 20), (20, 50), (50, 100), (100, 1e3), (1e3, 1e4), (1e4, 1e6 * (1 + 1e-12)))
    for p in paths:
        d = load_state(p); beta = float(d['beta']); a0_target = float(d['a0_target']); name = p.split('/')[-1].replace('.npz', '')
        m, f = eval_state(d, R, T); G = f['G'].detach().cpu().numpy(); a = f['a'].detach().cpu().numpy()
        a0 = float(f['a0'].detach().cpu())
        if not np.isfinite(a0) or a0 == 0: raise ValueError("sigma requires finite nonzero a(0)")
        if not (np.isfinite(G).all() and np.isfinite(a).all()): raise ValueError("nonfinite sampled field")
        sg = np.sign(a0)
        sOm = sg * np.sign(G); sTh = sg * np.sign(a)     # x y > 0 and x^2 y > 0 at every sample, so these are the signs of sigma Omega, sigma Theta
        print(f"\n=== {name}: beta = {beta:.4f}, a0 target = {a0_target:+.17g}, fitted a(0) = {a0:+.17g}, sigma = {sg:+.0f}, N = {int(d['N'])}, M = {int(d['M'])}; {len(R)} log radii in [0.5, 1e6] x {len(T)} interior angles")
        for lab, S in (('sigma Omega', sOm), ('sigma Theta', sTh)):
            pmp = np.array([has_pattern(S[:, j], (1, -1, 1)) for j in range(len(T))]); mpm = np.array([has_pattern(S[:, j], (-1, 1, -1)) for j in range(len(T))])
            nch = np.array([int((S[1:, j] * S[:-1, j] < 0).sum()) for j in range(len(T))])
            print(f"  {lab}: angles (of {len(T)}) whose sampled sequence contains (+,-,+): {int(pmp.sum())}" + (f"  (min/max matching sampled theta: [{T[pmp].min():.3f}, {T[pmp].max():.3f}] rad)" if pmp.any() else '') +
                  f"; contains (-,+,-): {int(mpm.sum())}" + (f"  (min/max matching sampled theta: [{T[mpm].min():.3f}, {T[mpm].max():.3f}] rad)" if mpm.any() else ''))
            print(f"      adjacent strict sign reversals along a ray: min {nch.min()}, median {np.median(nch):.1f}, max {nch.max()}; angles with no adjacent strict reversal: {int((nch == 0).sum())}; zero samples: {int((S == 0).sum())}")
            if pmp.any():
                r3 = []
                for j in np.where(pmp)[0]:
                    s = S[:, j]; i1 = np.argmax(s == 1); i2 = i1 + np.argmax(s[i1:] == -1); i3 = i2 + np.argmax(s[i2:] == 1); r3.append(R[i3])
                print(f"      (+,-,+): earliest sampled third radius per matching angle: min {min(r3):.4g}, max {max(r3):.4g}")
            neg = (S < 0)
            fr = []
            for lo, hi in bands:
                bneg = neg[(R >= lo) & (R < hi), :]; fr.append(f"{int(bneg.sum())}/{bneg.size} ({bneg.mean():.3f})")
            print(f"      sampled points with {lab} < 0 by band [0.5,10) [10,20) [20,50) [50,100) [100,1e3) [1e3,1e4) [1e4,1e6]: {'  '.join(fr)}")
            fr_r = neg.mean(axis=1); idx = [int(np.argmin(np.abs(R - r0))) for r0 in (0.5, 1, 10, 100, 1e3, 1e4, 1e5, 1e6)]
            print(f"      fraction of angles with {lab} < 0 at the sampled radii nearest to r = 0.5 / 1 / 10 / 100 / 1e3 / 1e4 / 1e5 / 1e6 (sampled r = " +
                  ', '.join(f'{R[i]:.4g}' for i in idx) + "): " + ' / '.join('%.3f' % fr_r[i] for i in idx))

if __name__ == '__main__':
    if len(sys.argv) < 2: raise SystemExit("provide at least one state file")
    main(sys.argv[1:])
