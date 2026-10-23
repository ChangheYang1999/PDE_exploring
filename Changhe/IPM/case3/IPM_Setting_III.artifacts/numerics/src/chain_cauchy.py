"""
chain_cauchy.py -- function-space test for the fixed-c_l chain states of the FULL problem (4L(c12)-(c25), runs/r1C_cl3.0_N*.pt), the analogue of
hs_cauchy.py / hs_centre_reg.py: consecutive saved states evaluated with the producer's evaluator (qdiag.State.ev: rho, grad rho, U, R, N_f) at 19649 common
points (401 log radii 1e-3 .. 1e7 x 49 quadrant angles incl. both axes); max |d rho|/(1 + r)^gamma (gamma = 1/c_l, the far-field growth), max |d rho|/|rho_b|,
max |d grad rho|/(1 + r)^(gamma - 1), max |dU|/(1 + r)^gamma by region; the residual |R|/N_f of every state on the same points; the local jets
(rho(0, y)/(a0 y) - 1)/y^2 and (rho_y(x, 0)/a0 - 1)/x^2 at y, x = 1e-4 .. 1 against the first node radius.  Diagnostic of trial states only.
usage: python3 src/chain_cauchy.py runs/r1C_cl3.0_N64.pt runs/r1C_cl3.0_N96.pt ...
"""
import sys, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
files = sys.argv[1:]; S = [qdiag.State(f) for f in files]; g = S[0].gamma
print("state           N    L     a0           K            first node r_1")
for f, s in zip(files, S): print(f"{f.split('/')[-1]:>22s} {s.N:3d} {s.L:4g} {s.a0:12.6f} {s.K:12.6f}   {float(s.rad.rR[1]) if hasattr(s.rad,'rR') else float(s.rad.rmap_np(s.rad.tR_np[1:2])[0]):.3e}")
r = np.logspace(-3, 7, 401); th = np.concatenate([[0.0], np.linspace(0, np.pi / 2, 49)[1:-1], [np.pi / 2]]); RR, TT = np.meshgrid(r, th, indexing='ij'); R = RR.reshape(-1); T = TT.reshape(-1)
O = [s.ev(R, T) for s in S]
regs = [(0, 0.1), (0.1, 1), (1, 100), (100, 1e4), (1e4, 1e7)]
print(f"\ngamma = {g:.4f}; {len(R)} common points; columns per region: max|d rho|/(1+r)^g, max|d rho|/|rho_b|, max|d grad rho|/(1+r)^(g-1), max|dU|/(1+r)^g")
print("pair                    " + "  ".join(f"[{lo:g},{hi:g})".ljust(42) for lo, hi in regs))
for a, b, fa, fb in zip(O[:-1], O[1:], files[:-1], files[1:]):
    d = np.abs(a['rho'] - b['rho']); dg = np.hypot(a['rho_x'] - b['rho_x'], a['rho_y'] - b['rho_y']); dU = np.hypot(a['U1'] - b['U1'], a['U2'] - b['U2'])
    line = f"{fa.split('_N')[-1][:-3]:>4s} -> {fb.split('_N')[-1][:-3]:<4s}".ljust(24)
    for lo, hi in regs:
        m = (R >= lo) & (R < hi)
        line += f"{(d[m] / (1 + R[m]) ** g).max():9.2e} {(d[m] / (np.abs(b['rho'][m]) + 1e-300)).max():9.2e} {(dg[m] / (1 + R[m]) ** (g - 1)).max():9.2e} {(dU[m] / (1 + R[m]) ** g).max():9.2e}   "
    print(line)
b = O[-1]; line = "scale of last: |rho|, |grad rho|, |U| ".ljust(24)
for lo, hi in regs:
    m = (R >= lo) & (R < hi); line += f"{(np.abs(b['rho'][m]) / (1 + R[m]) ** g).max():9.2e}           {(np.hypot(b['rho_x'][m], b['rho_y'][m]) / (1 + R[m]) ** (g - 1)).max():9.2e} {(np.hypot(b['U1'][m], b['U2'][m]) / (1 + R[m]) ** g).max():9.2e}   "
print(line)
print("\nresidual |R|/N_f of each state on the common points (producer's evaluator; x-axis excluded where N_f = 0), max by region:")
for f, o in zip(files, O):
    line = f"{f.split('/')[-1]:>22s}: "
    for lo, hi in regs:
        m = (R >= lo) & (R < hi) & (o['Nf'] > 0); line += f"{(np.abs(o['R'][m]) / o['Nf'][m]).max():9.2e}   "
    print(line)
ys = np.array([1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1.0])
print("\nlocal jets: (rho(0,y)/(a0 y) - 1)/y^2 [row 1] and (rho_y(x,0)/a0 - 1)/x^2 [row 2] at y, x = " + " ".join(f"{v:g}" for v in ys))
for f, s in zip(files, S):
    oy = s.ev(ys, np.full_like(ys, np.pi / 2)); ox = s.ev(ys, np.zeros_like(ys))
    print(f"{f.split('/')[-1]:>22s}: " + " ".join(f"{v:+9.4f}" for v in (oy['rho'] / (s.a0 * ys) - 1) / ys ** 2))
    print(f"{'':>22s}  " + " ".join(f"{v:+9.4f}" for v in (ox['rho_y'] / s.a0 - 1) / ys ** 2))
