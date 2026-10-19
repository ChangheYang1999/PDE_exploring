"""V64(d): own axis rows (alpha = V_r/r, a_dir, a_div, log k with a_dir, h) at the lead's adir/axcheck radii, for a direct
rows from near tmin outward (deep-grid check of the approach to the node regime). Usage: python3 tests/v64_axdeep.py STATE.npz [m1]"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
from charsolve import lagrange_diff
d = np.load(sys.argv[1], allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); th = d['th']; nt = len(th)
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)),
            q=8, nt=nt, dti=0.01, nstep=800)
rho = torch.tensor(d['rho'], dtype=torch.float64, device='cuda')
nd = F.node(rho); m1 = nd['m1'] if len(sys.argv) < 3 else float(sys.argv[2]); l = 1/p
al, be, _, _ = [x.cpu().numpy() for x in F.fields(rho)]
g = (rho/F.R**p).cpu().numpy(); r = F.r.cpu().numpy(); q = F.q; P = len(r)//q; e = F.S.edges
Dg = lagrange_diff(np.polynomial.legendre.leggauss(q)[0]); dal = np.zeros_like(al)
for k in range(P):
    dal[k*q:(k+1)*q] = Dg @ al[k*q:(k+1)*q]/((e[k+1]-e[k])/2)
dtal = r[:, None]*dal
mm = np.fft.fftfreq(nt, 1.0/nt); mm[nt//2] = 0
dthb = np.real(np.fft.ifft(1j*mm*np.fft.fft(be, axis=1), axis=1))
def at(f, ths, deriv=0):
    fh = np.fft.fft(f, axis=1)/nt; fh[:, nt//2] = 0
    return np.real(fh @ (np.exp(1j*mm*(ths - th[0]))*((1j*mm)**deriv)))
Imat = F.Imat.cpu().numpy(); tu = F.tu.cpu().numpy(); dti = F.dti
print('state', sys.argv[1], 'm1', round(m1, 4), 'own m1', round(nd['m1'], 4))
for name, ths in (('up', math.pi/2), ('down', 3*math.pi/2)):
    A = Imat @ at(al, ths); adir = Imat @ (at(al, ths) + at(dthb, ths)); adiv = Imat @ (2*l - at(al, ths) - at(dtal, ths))
    gtt = Imat @ at(g, ths, 2)
    f = (m1 - adir)/A; logk = np.concatenate([[0], np.cumsum(0.5*(f[1:] + f[:-1])*dti)])
    print(name, '  lr    Vr/r     a_dir    a_div    logk(dir)  h  g_thth')
    for lr in (-15.5, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -4):
        i = int(np.argmin(np.abs(tu - lr)))
        h = np.exp((p - 2)*tu[i])*gtt[i]
        print('     %5g  %7.4f  %7.4f  %7.4f  %8.4f  %.4g  %.4g' % (lr, A[i], adir[i], adiv[i], logk[i], h, gtt[i]))
