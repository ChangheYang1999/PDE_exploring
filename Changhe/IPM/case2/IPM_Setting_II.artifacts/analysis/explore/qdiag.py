"""Q(rho) = int rho W.grad(r^-3 sin 3th) dX on the dynres log-polar grid (tail beyond t1 neglected:
integrand ~ r^{2p-3}, relative tail error ~ r1^{2p-2}). Used to test the exact moment law
dc/ds = (1 - c_l) c + Q/pi of the dynamic rescaling (I3 in time-dependent form)."""
import numpy as np, sys
sys.path.insert(0, 'explore')
import dynres as D

def Qfun(G, q, p):
    Wr_r, Wt_r, c, bp, rho_t, rho_th, g = D.velocity(G, q, p)
    rho = q*G.w
    r = G.r[:,None]
    th = G.th[None,:]
    # grad(r^-3 sin3th) = r^-4 (-3 sin3th, 3 cos3th) in (r, th) components
    integrand = rho * r**-3 * (-3*Wr_r*np.sin(3*th) + 3*Wt_r*np.cos(3*th))
    f = (integrand*r**2).sum(axis=1)*(2*np.pi/G.Nth)      # dX = r^2 dt dth
    Q = np.trapz(f, G.t)
    cm = np.trapz(((rho*r**-3*np.sin(3*th))*r**2).sum(axis=1)*(2*np.pi/G.Nth), G.t)/np.pi
    return Q, c, cm

if __name__ == "__main__":
    for a, L, p0 in [(0.0,1.0,0.6),(0.5,1.0,0.6),(0.8,2.33,0.6),(0.9,5.0,0.6),(0.99,1.0,0.3),(0.99,1.0,0.9)]:
        G = D.Grid(-10, 12, 551, 256, p0); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
        F = (1+r**2/L**2)**((p0-2)/2)
        rho0 = X**2*(1+a*Y/np.sqrt(L**2+r**2))*F
        Q, c, cm = Qfun(G, rho0/G.w, p0)
        print(f"pos a={a} L={L} p0={p0}: c={c:.6f} (moment {cm:.6f}) Q/pi={Q/np.pi:.6f}  Q/(pi c^2)={Q/np.pi/max(c*c,1e-30):.4f}", flush=True)
    G = D.Grid(-10, 4, 551, 256, 0.6); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
    for a in [0.0, 0.5, 1.0, 2.0]:
        rho0 = X**2*(1+a*Y)**2*np.exp(-r**2)
        Q, c, cm = Qfun(G, rho0/G.w, 0.6)
        ex = 3*a**4/512 + (51*np.log(2)/32 - 265/256)*a**2 + 3*np.log(2)/8 - 21/64
        print(f"rho_a a={a}: c={c:.8f} (exact {a/4}) Q/pi={Q/np.pi:.8f} exact {ex:.8f}", flush=True)
