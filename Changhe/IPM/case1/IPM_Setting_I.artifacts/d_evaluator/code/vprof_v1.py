"""Radial residual profiles of a construct1 export by the verifier's evaluation (vcand.main), saved next to the exporter's,
plus D10 and the y^3 axis-ODE residual of the verifier's own axis traces.
Usage: python3 vprof.py file.npz Mmax out.npz"""
import sys, json
import numpy as np
from scipy.interpolate import CubicSpline
import vcand
path, Mmax, outp = sys.argv[1], int(sys.argv[2]), sys.argv[3]
out, ev, ax = vcand.main(path, {'Mmax': Mmax, 'b3': True})
json.dump(out, open(outp.replace('.npz', '.json'), 'w'), indent=1, default=float)
d = np.load(path, allow_pickle=True)
r = d['r']
Rmax = np.abs(ev.R).max(1)
Nmax = ev.Rnorm.max(1)
iR = np.abs(ev.R).argmax(1)
Nt = out['Nt']
th_at = 2 * np.pi * iR / Nt
ex_R = np.abs(d['residual']).max(1) if 'residual' in d.files else np.full(len(r), np.nan)
ex_N = d['denominator'].max(1) if 'denominator' in d.files else np.full(len(r), np.nan)
# y^3 axis ODE with own traces: w G3' + (3h - 1) G3 + W1_2 G1' + W2_3 G1 = 0
x, w, h, G1, G1p, G3 = ax['x'], ax['w'], ax['h'], ax['G1'], ax['G1p'], ax['G3']
G3p = CubicSpline(np.log(x), G3)(np.log(x), 1) / x
terms = np.abs(w * G3p) + np.abs((3 * h - 1) * G3) + np.abs(ax['F3'])
R3 = (w * G3p + (3 * h - 1) * G3 - ax['F3']) / terms
R1 = (w * G1p - (1 - h) * G1) / (np.abs(w * G1p) + np.abs((1 - h) * G1))
np.savez(outp, r=r, Rmax=Rmax, Nmax=Nmax, th_at=th_at, ex_R=ex_R, ex_N=ex_N, R3=R3, R1=R1, x=x, D10=json.dumps(out['D10']))
print(json.dumps(dict(D10=out['D10'], c=out['c'], c_l=out['c_l'], ex_global_den=float(np.nanmax(ex_N)),
                      own_global_norm=float(Nmax.max()), r_at_own_norm_max=float(r[Nmax.argmax()]),
                      r_at_ex_den_max=float(r[np.nanargmax(ex_N)])), indent=1))
for rr in [1, 2, 5, 10, 30, 100, 300, 1000, 2000, 3000, 5000, 7000, r[-20], r[-9]]:
    j = min(np.searchsorted(r, rr), len(r) - 1)
    print('r=%9.3f own |R|/bandnorm(r) %.2e  own |R|/global %.2e  ex |R|/global %.2e  theta %.3f  R3 %.1e  R1 %.1e'
          % (r[j], Rmax[j] / Nmax[j], Rmax[j] / Nmax.max(), ex_R[j] / np.nanmax(ex_N), th_at[j], R3[j], R1[j]))
