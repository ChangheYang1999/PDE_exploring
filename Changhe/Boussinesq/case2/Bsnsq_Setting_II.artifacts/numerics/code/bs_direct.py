"""Independent physical-space checks of a saved state (prompt Section 4, item 2):
 (A) velocity at sample points by direct 2D quadrature of the Biot-Savart kernel with the fourfold parity images
     (polar grid about the origin for the far part, polar grid about the target for the near disc), compared with the
     modal Green inverse of the state;
 (B) Poisson residual E = -Delta Psi - Omega from second finite differences of the state's Psi (modal inverse)."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from charcheck import build, evalW
from diag_state import eval_state

def omega_at(B, x, y):
    """Omega on the full plane from the first-quadrant evaluator via parity (odd in x, odd in y)."""
    sx = np.sign(x); sy = np.sign(y)
    o = evalW(B, np.abs(x) + 1e-300, np.abs(y) + 1e-300, need_fields=True)
    return sx * sy * o['Omega']

def velocity_direct(B, X, delta=0.3, nr=1200, nth=720, rmax=1e13, nrho=200, nphi=256):
    """U(X) = (1/2pi) int Omega(Y) ((y - y2), -(x - y1)) / |X-Y|^2 dY  (U = (-Psi_y, Psi_x), Psi = -(1/2pi) int log|X-Y| Omega)."""
    x0, y0 = X
    # far part: polar grid about the origin over the whole plane (all four quadrants via parity), excluding |Y-X|<delta
    r = np.geomspace(1e-4, rmax, nr); th = (np.arange(nth) + 0.5) * 2 * np.pi / nth
    R, TH = np.meshgrid(r, th, indexing='ij'); Y1 = R * np.cos(TH); Y2 = R * np.sin(TH)
    Om = omega_at(B, Y1.ravel(), Y2.ravel()).reshape(R.shape)
    d2 = (x0 - Y1) ** 2 + (y0 - Y2) ** 2
    mask = d2 > delta ** 2
    w = R * np.gradient(r)[:, None] * (2 * np.pi / nth)       # area element r dr dth (trapezoid-like in r)
    k1 = (y0 - Y2) / d2; k2 = -(x0 - Y1) / d2
    U1 = np.sum((Om * k1 * w)[mask]) / (2 * np.pi); U2 = np.sum((Om * k2 * w)[mask]) / (2 * np.pi)
    # near disc |Y - X| < delta: polar grid about X; the 1/rho kernel singularity is cancelled by rho drho
    rho = np.geomspace(1e-7, delta, nrho); phi = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    RHO, PHI = np.meshgrid(rho, phi, indexing='ij'); Y1n = x0 + RHO * np.cos(PHI); Y2n = y0 + RHO * np.sin(PHI)
    Omn = omega_at(B, Y1n.ravel(), Y2n.ravel()).reshape(RHO.shape)
    wn = RHO * np.gradient(rho)[:, None] * (2 * np.pi / nphi)
    U1 += np.sum(Omn * (-np.sin(PHI)) / RHO * wn) / (2 * np.pi); U2 += np.sum(Omn * (np.cos(PHI)) / RHO * wn) / (2 * np.pi)
    # correction: the far grid excluded a disc of radius delta that is not exactly a union of cells; refine by
    # subtracting far-grid cells inside the disc is already done via mask; the mismatch region is O(cell size): report delta
    return U1, U2

if __name__ == '__main__':
    path = sys.argv[1]; d = load_state(path); B = build(d, rmin=1e-4, rmax=1e13, nr=12000)
    rmax_list = [float(v) for v in sys.argv[2:]] or [3e3, 1e6, 1e9, 1e13]
    print(f"=== {path}: beta={B['beta']}")
    pts = [(0.5, 0.3), (2.0, 1.0), (5.0, 5.0), (10.0, 2.0), (18.0, 0.5), (30.0, 20.0)]
    print("  (A) direct Biot-Savart vs modal inverse (U1, U2):")
    for (x0, y0) in pts:
        o = evalW(B, np.array([x0]), np.array([y0]))
        for rmax in rmax_list:
            nr = int(100 * np.log10(rmax / 1e-4)); nth = 720; delta = 0.2
            U1d, U2d = velocity_direct(B, (x0, y0), delta=delta, nr=nr, nth=nth, rmax=rmax)
            print(f"    X=({x0:5.1f},{y0:5.1f}) rmax={rmax:.0e} grid {nr}x{nth}: direct U=({U1d:+.7e},{U2d:+.7e}) modal U=({o['U1'][0]:+.7e},{o['U2'][0]:+.7e}) rel diff ({(U1d-o['U1'][0])/o['U1'][0]:+.2e},{(U2d-o['U2'][0])/o['U2'][0]:+.2e})", flush=True)
    # (B) Poisson residual by finite differences of Psi (modal) at a few points
    print("  (B) E = -Delta Psi - Omega by central differences of the state's Psi (h = 1e-3 r):")
    for (x0, y0) in pts[:5]:
        r0 = np.hypot(x0, y0); h = 1e-3 * r0
        def psi(x, y):
            m, f = eval_state(d, np.array([np.hypot(x, y)]), np.array([np.arctan2(y, x)])); return f['Psi'][0, 0].item()
        lap = (psi(x0 + h, y0) + psi(x0 - h, y0) + psi(x0, y0 + h) + psi(x0, y0 - h) - 4 * psi(x0, y0)) / h ** 2
        om = omega_at(B, np.array([x0]), np.array([y0]))[0]
        print(f"    X=({x0:5.1f},{y0:5.1f}): -Lap Psi = {-lap:+.7e}, Omega = {om:+.7e}, E/|Omega| = {(-lap-om)/abs(om):+.2e}")
