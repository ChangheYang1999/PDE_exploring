"""Band variant of gphys_local.py (2026-10-22T00:5xZ): optional --phi phimin phimax (degrees) restricts the angular range of the polar grid.
Physical-space samples of a generating-function state (lead tool).
For physical points (x, y) = (r cos phi, r sin phi) of the quadrant, solve G_x(x, eta) = y for eta (G_x is increasing in
eta since A = G_x,eta > 0; bracketing bisection, then Newton), and evaluate the fields of model.fields there.
Optional --fdcheck: at a few points compare Omega with -Lap Psi_phys and the temperature residual W.grad Theta - b Theta
by centred finite differences of the root-inverted physical fields (Psi_phys(x, y) = Psi(x, eta(x, y))).
Usage: python3 gphys.py state.npz out.npz [rmin rmax nr nphi] [--fdcheck]"""
import sys, math, numpy as np, torch
torch.set_num_threads(1)
import jets
DEV = jets.DEV
from jets import monos, DT
# [GPU copy of the authors' gphys.py v2 (core-aware), run from this folder's directory: tensors on DEV]
from model import Model, fields
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = torch.tensor(d['c'], device=DEV); a0 = float(d['a0'])
alpha = float(d['alpha']) if 'alpha' in d.files else 0.0
se = float(sys.argv[sys.argv.index('--se') + 1]) if '--se' in sys.argv else (float(d['se']) if 'se' in d.files else 1.0)
gam = float(sys.argv[sys.argv.index('--gam') + 1]) if '--gam' in sys.argv else (float(d['gam']) if 'gam' in d.files else 0.0)
m_ = int(d['m']) if 'm' in d.files else 3
mod = Model(J, Kw, m=m_, alpha=alpha, se=se, gam=gam)
if 'core' in d.files:    # core patch (model_core.py)
    from model_core import ModelCore; q_ = d['core']
    mod = ModelCore(J, Kw, q_, m=m_, alpha=alpha, se=se, gam=gam)
    c = torch.tensor(np.concatenate([d['c'], d['cc']]), device=DEV)
args = [a for a in sys.argv[3:] if not a.startswith('--')]
rmin = float(args[0]) if len(args) > 0 else 1e-3
rmax = float(args[1]) if len(args) > 1 else 1e6
nr = int(args[2]) if len(args) > 2 else 91
nph = int(args[3]) if len(args) > 3 else 24
L1, ix1 = monos(1); L2, ix2 = monos(2)

def Gx_of(x, e):
    return (mod.basis_matrix(x, e, p=1)[ix1[(1, 0)]] @ c)

def eta_of(x, y):
    """eta with G_x(x, eta) = y (y > 0); vectorized bracketing + bisection in log eta, then Newton"""
    lo = torch.zeros_like(y); hi = torch.maximum(y, torch.ones_like(y)) * 1e-3
    for _ in range(200):
        g = Gx_of(x, hi); m = g < y
        if not m.any(): break
        lo = torch.where(m, hi, lo); hi = torch.where(m, hi * 4, hi)
    for _ in range(80):
        mid = 0.5 * (lo + hi); g = Gx_of(x, mid); m = g < y
        lo = torch.where(m, mid, lo); hi = torch.where(m, hi, mid)
    e = 0.5 * (lo + hi)
    for _ in range(4):
        B = mod.basis_matrix(x, e, p=2) @ c
        e = e - (B[ix2[(1, 0)]] - y) / B[ix2[(1, 1)]]
    return e

def phys_fields(x, y):
    e = eta_of(x, y)
    out = {}
    for ch in torch.split(torch.arange(x.shape[0], device=DEV), 4096):
        F = fields(mod.basis_matrix(x[ch], e[ch]) @ c, x[ch], e[ch], a0, mod.beta)
        for k, v in F.items(): out.setdefault(k, []).append(v.detach())
    out = {k: torch.cat(v) for k, v in out.items()}
    out['eta'] = e
    return out

if __name__ == '__main__':
    r = np.logspace(np.log10(rmin), np.log10(rmax), nr)
    if '--phi' in sys.argv:
        i_ = sys.argv.index('--phi'); p0, p1 = math.radians(float(sys.argv[i_ + 1])), math.radians(float(sys.argv[i_ + 2]))
        ph = p0 + (np.arange(nph) + 0.5) * (p1 - p0) / nph
    else:
        ph = (np.arange(nph) + 0.5) * (math.pi / 2) / nph
    R_, P_ = np.meshgrid(r, ph, indexing='ij')
    x = torch.tensor((R_ * np.cos(P_)).ravel(), dtype=DT, device=DEV); y = torch.tensor((R_ * np.sin(P_)).ravel(), dtype=DT, device=DEV)
    F = phys_fields(x, y)
    yerr = float(((F['y'] - y).abs() / y).max())
    print('state %s a0 %.5f  points %d  r [%g, %g] x %d, phi [%.3f, %.3f] deg x %d  max rel |G_x(x, eta) - y| / y = %.2e' % (sys.argv[1], a0, x.shape[0], rmin, rmax, nr, math.degrees(ph[0]), math.degrees(ph[-1]), nph, yerr))
    q = (F['R'].abs() / F['N']).cpu().numpy()
    print('max |R|/N on the physical polar grid: %.3e (r < 10: %.3e)' % (q.max(), q[(R_.ravel() < 10)].max()))
    beta_ = mod.beta; N2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (beta_ * (x * F['Ox'] + F['y'] * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
    q2 = (F['R'].abs() / N2).cpu().numpy(); rr = R_.ravel(); pp = np.degrees(P_.ravel())
    i = np.argmax(q2); j = np.argmax(q)
    print('max |R|/N2 on the physical polar grid: %.3e at r %.4f phi %.3f deg (r < 10: %.3e); max |R|/N at r %.4f phi %.3f deg' % (q2.max(), rr[i], pp[i], q2[rr < 10].max(), rr[j], pp[j]))
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e6), (1e6, 1e8)]:
        m = (rr >= lo) & (rr < hi)
        if m.any(): print('  r [%g, %g): max R/N %.2e  max R/N2 %.2e  (max R/N2 at phi %.3f deg)' % (lo, hi, q[m].max(), q2[m].max(), pp[m][np.argmax(q2[m])]))
    cpu = lambda t: t.cpu().numpy()
    np.savez(sys.argv[2], r=r, phi=ph, X=cpu(x), Y=cpu(y), Theta=cpu(a0 * F['eta']), Omega=cpu(F['Om']),
             Psi=cpu(F['Psi']), U1=cpu(F['U1']), U2=cpu(F['U2']), Theta_x=cpu(F['Thx']), Theta_y=cpu(F['Thy']),
             R_Omega=cpu(F['R']), N_Omega=cpu(F['N']), a0=a0, beta=mod.beta, src=sys.argv[1],
             note='genfn state sampled at physical points; arrays flattened in (r, phi) order with shape (nr, nphi)')
    if '--fdcheck' in sys.argv:
        pts = [(0.05, 0.3), (0.5, 0.5), (2.0, 1.0), (1.0, 6.0), (30.0, 4.0), (5.0, 80.0)]
        px = torch.tensor([p[0] for p in pts], dtype=DT, device=DEV); py = torch.tensor([p[1] for p in pts], dtype=DT, device=DEV)
        F0 = phys_fields(px, py)
        for h in [1e-2, 5e-3, 2.5e-3]:
            hh = h * torch.maximum(torch.ones_like(px), 0.2 * torch.hypot(px, py))
            def PE(xx, yy):
                Fq = phys_fields(xx, yy); return Fq['Psi'], Fq['eta']
            P0, e0 = PE(px, py); Pxp, exp_ = PE(px + hh, py); Pxm, exm = PE(px - hh, py)
            Pyp, eyp = PE(px, py + hh); Pym, eym = PE(px, py - hh)
            lap = (Pxp + Pxm + Pyp + Pym - 4 * P0) / hh ** 2
            U1 = -(Pyp - Pym) / (2 * hh); U2 = (Pxp - Pxm) / (2 * hh)
            Thx = a0 * (exp_ - exm) / (2 * hh); Thy = a0 * (eyp - eym) / (2 * hh)
            W1 = mod.beta * px + U1; W2 = mod.beta * py + U2
            RT = W1 * Thx + W2 * Thy - mod.b * a0 * e0
            NT = (W1 * Thx).abs() + (W2 * Thy).abs() + mod.b * a0 * e0.abs()
            print('h %.4f  max |Om + lap Psi| / |Om| %.2e   max |U - U_jet| / |U| %.2e   max |RT| / N_T %.2e' % (h,
                  float(((F0['Om'] + lap).abs() / F0['Om'].abs()).max()),
                  float((torch.hypot(U1 - F0['U1'], U2 - F0['U2']) / torch.hypot(F0['U1'], F0['U2'])).max()),
                  float((RT.abs() / NT).max())))
