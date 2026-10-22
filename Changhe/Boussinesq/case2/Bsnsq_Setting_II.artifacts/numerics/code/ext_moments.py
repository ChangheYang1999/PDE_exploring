"""Exterior Biot-Savart moments (external referee's diagnostic 4; repaired after the referee's audit: trapezoid half weights, tail normalization,
all modes of the finer state; the Psi check (nine points, k <= 24) is a sanity check, not a bound on velocity errors; the referee's direct
polynomial-moment values (audit results, not included) supersede the first logs): how much of the velocity change between two fitted states on r < R is
induced by their vorticity difference OUTSIDE r = R? For a vorticity mode b_k(s) (Omega = sum_k b_k(s) sin(k th), even k), the
stream function on r < R induced by the exterior vorticity is harmonic there: Psi_ext = sum_k (r^k / 2k) m_k sin(k th) with
m_k = int_R^inf s^(1-k) b_k(s) ds (modal Green formula of the numerical study). For states A, B the fields are evaluated
directly from the basis; b_k by Gauss-Legendre quadrature in the angle on (0, pi/2) (b_k = (4/pi) int_0^(pi/2) Omega sin(k th) dth
by the odd-odd parity), m_k by the trapezoidal rule in log s on [R, 1e6] plus the analytic tail of a s^(-1/2) decay. The velocity
U_ext = (-d_y, d_x) Psi_ext is compared with the total velocity change W_B - W_A (same beta) on fixed grids inside r < R.
Check: the same quadrature applied on [1e-3, 1e6] to the full modal formula reproduces the state's own Psi (printed).
Fitted-state data; this attributes a velocity difference to regions, nothing more."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def modes(d, s, th, wth, K):
    m, f = eval_state(d, s, th)
    X = f['x'].cpu().numpy(); Y = f['y'].cpu().numpy(); Om = X * Y * f['G'].cpu().numpy()      # (ns, nth)
    ks = np.arange(2, K + 1, 2)
    S = np.sin(np.outer(th, ks))                                                                # (nth, nk)
    b = (4 / np.pi) * (Om * wth[None, :]) @ S                                                   # (ns, nk)
    return ks, b, f

def psi_check(d, ks, b, s, r_pts, th_pts):
    """full modal Psi at (r_pts, th_pts) from b_k on the grid s (log-trapezoid), against the state's Psi"""
    ls = np.log(s); dl = np.diff(ls); w = np.zeros_like(s); w[:-1] += 0.5 * dl; w[1:] += 0.5 * dl; w = w * s      # trapezoid weights (ds)
    m, f = eval_state(d, r_pts, th_pts); Psi_state = f['Psi'].cpu().numpy()
    out = np.zeros((len(r_pts), len(th_pts)))
    for j, k in enumerate(ks):
        if k > 24: break      # higher modes are below 1e-20 here; avoids s^(k+1) overflow at s = 1e6
        for i, r in enumerate(r_pts):
            inner = np.sum((w * s**(k + 1) * b[:, j])[s <= r]); outer = np.sum((w * s**(1 - k) * b[:, j])[s > r])
            h = (r**(-k) * inner + r**k * outer) / (2 * k)
            out[i, :] += h * np.sin(k * th_pts)
    return out, Psi_state

def main(pa, pb, R=30.0):
    dA, dB = load_state(pa), load_state(pb); K = 2 * max(int(dA['M']), int(dB['M']))     # all modes of the finer state (external referee)
    s = np.geomspace(R, 1e6, 240); x_gl, w_gl = np.polynomial.legendre.leggauss(48); th = (x_gl + 1) * np.pi / 4; wth = w_gl * np.pi / 4
    ksA, bA, _ = modes(dA, s, th, wth, K); ksB, bB, _ = modes(dB, s, th, wth, K)
    ls = np.log(s); dl = np.diff(ls); w = np.zeros_like(s); w[:-1] += 0.5 * dl; w[1:] += 0.5 * dl; w = w * s      # trapezoid in log s (half weights at the ends)
    def mom(b):
        mk = np.array([np.sum(w * s**(1 - k) * b[:, j]) for j, k in enumerate(ksA)])
        tail = np.array([b[-1, j] * s[-1]**(2 - k) / (k - 1.5) for j, k in enumerate(ksA)])       # continuation b_k(s) = b_k(S) (s/S)^(-1/2) beyond S: int_S^inf s^(1-k) b ds = b(S) S^(2-k)/(k - 3/2) (a model; external referee)
        return mk + tail, tail
    mA, tA = mom(bA); mB, tB = mom(bB)
    print(f"A = {pa}, B = {pb}; exterior radius R = {R}; modes k = 2..{K}; radial grid [R, 1e6] x 240, 48 GL angles")
    print("  k :  m_k(A)       m_k(B)       m_k(B)-m_k(A)   |tail part of m_k(B)|")
    for j in range(min(8, len(ksA))):
        print(f"  {ksA[j]:2d}: {mA[j]:+.4e}  {mB[j]:+.4e}  {mB[j]-mA[j]:+.4e}   {abs(tB[j]):.1e}")
    # check of the modal quadrature on a full grid [1e-3, 1e6] for state B at a few points
    s_full = np.geomspace(1e-3, 1e6, 600); ksF, bF, _ = modes(dB, s_full, th, wth, K)
    r_pts = np.array([3.0, 10.0, 20.0]); th_pts = np.array([0.3, 0.8, 1.3])
    Pq, Ps = psi_check(dB, ksF, bF, s_full, r_pts, th_pts)
    print(f"  check (state B): max |Psi_quadrature - Psi_state| / max|Psi_state| at r = 3, 10, 20 = {np.abs(Pq - Ps).max() / np.abs(Ps).max():.2e}")
    # exterior-induced velocity difference on grids inside r < R
    grids = {'band 5-15': (np.linspace(5, 15, 41), (np.arange(32) + 0.5) * (np.pi / 2) / 32),
             'band 15-30': (np.linspace(15, 30, 41), (np.arange(32) + 0.5) * (np.pi / 2) / 32),
             'patch r11-17 th.25-.55': (np.linspace(11, 17, 31), np.linspace(0.25, 0.55, 21)),
             'inner r<=2': (np.geomspace(0.01, 2, 30), (np.arange(16) + 0.5) * (np.pi / 2) / 16)}
    print("  grid                      sup|dW| (total)  sup|dU_ext|   sup|dW - dU_ext|  sup|W_B|   sup|U_B| : dU_ext / dW ratio")
    for g, (rg, tg) in grids.items():
        if rg[-1] > R + 1e-9: continue      # only grids inside the exterior radius
        mA_, fA = eval_state(dA, rg, tg); mB_, fB = eval_state(dB, rg, tg)
        dW1 = (fB['W1'] - fA['W1']).cpu().numpy(); dW2 = (fB['W2'] - fA['W2']).cpu().numpy()
        Rg, Tg = np.meshgrid(rg, tg, indexing='ij')
        dm = mB - mA
        dPsi_r = sum(0.5 * Rg**(k - 1) * dm[j] * np.sin(k * Tg) for j, k in enumerate(ksA))
        dPsi_t = sum(0.5 * Rg**k * dm[j] * np.cos(k * Tg) for j, k in enumerate(ksA))
        dUx = -(np.sin(Tg) * dPsi_r + np.cos(Tg) / Rg * dPsi_t); dUy = np.cos(Tg) * dPsi_r - np.sin(Tg) / Rg * dPsi_t
        n = lambda a, b: np.hypot(a, b).max()
        UB = n(fB['U1'].cpu().numpy(), fB['U2'].cpu().numpy()); WB = n(fB['W1'].cpu().numpy(), fB['W2'].cpu().numpy())
        print(f"  {g:24s}  {n(dW1, dW2):9.3e}      {n(dUx, dUy):9.3e}     {n(dW1 - dUx, dW2 - dUy):9.3e}      {WB:8.3e}  {UB:8.3e} : {n(dUx, dUy)/n(dW1, dW2):.2f}")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 30.0)
