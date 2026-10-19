"""
Homotopy (forced continuation) by dynamic rescaling, lead's exploratory code (CPU).
  rho_s = rho - V_h . grad rho,   V_h = c_l X + h W[rho] + (1-h) E,
  E = curl-perp of psi_E = mu x y chi(r), chi = exp(-r^2/LE^2)  (E = mu(-x,y) near 0, E -> 0 at infinity),
  c_l = 1/2 + h c[rho] + (1-h) mu   (jet compatibility for the total strain at 0).
h = 0: linear transport, unique attracting profile rho = xi^2.  h = 1: the IPM profile system.
h is raised in steps of dh every `hold` units of s (quasi-static continuation of the attractor).
Uses the grid / velocity routines of dynres.py (validated).
"""
import numpy as np, json, time, argparse
import dynres as D

def rhs(G, q, p, h, mu, LE):
    Wr_r, Wt_r, c, bp, rho_t, rho_th, g = D.velocity(G, q, p)
    r = G.r[:, None]
    chi = np.exp(-r**2/LE**2)
    cos2 = G.cos**2 - G.sin**2; sin2 = 2*G.sin*G.cos
    Er_r = -mu*cos2*chi
    Et_r = mu*sin2*chi*(1 - r**2/LE**2)
    cl = 0.5 + h*c + (1-h)*mu
    a = cl + h*Wr_r + (1-h)*Er_r
    b = h*Wt_r + (1-h)*Et_r
    left, right = D.ghosts(G, q, p)
    qt = D.upwind_dt(G, q, a, left, right)
    qth = G.dth(q)
    dq = q - a*(qt + G.om*q) - b*qth
    return dq, dict(c=c, bp=bp, cl=cl, amin=float(a.min()))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--mu', type=float, default=1.0)
    ap.add_argument('--LE', type=float, default=2.0)
    ap.add_argument('--dh', type=float, default=0.1)
    ap.add_argument('--hold', type=float, default=8.0)
    ap.add_argument('--hmax', type=float, default=1.0)
    ap.add_argument('--h0', type=float, default=0.0)
    ap.add_argument('--p0', type=float, default=0.6)
    ap.add_argument('--ds', type=float, default=0.004)
    ap.add_argument('--Nt', type=int, default=451)
    ap.add_argument('--Nth', type=int, default=128)
    ap.add_argument('--t0', type=float, default=-9.)
    ap.add_argument('--t1', type=float, default=10.)
    ap.add_argument('--out', type=str, default='runs/hom0')
    ap.add_argument('--init', type=str, default='')
    args = ap.parse_args()
    G = D.Grid(args.t0, args.t1, args.Nt, args.Nth, args.p0)
    r = G.r[:, None]; X = r*G.cos; Y = r*G.sin
    if args.init:
        d = np.load(args.init); q = d['q']; p = float(d['p'])
    else:
        rho0 = X**2*(1+r**2)**((args.p0-2)/2)
        q = rho0/G.w; p = args.p0
    s = 0.0; k = 0; tw = time.time()
    h = args.h0
    nsteps_hold = int(round(args.hold/args.ds))
    while True:
        k1, info = rhs(G, q, p, h, args.mu, args.LE)
        q1 = q + args.ds*k1
        k2, _ = rhs(G, q1, p, h, args.mu, args.LE)
        q2 = 0.75*q + 0.25*(q1 + args.ds*k2)
        k3, _ = rhs(G, q2, p, h, args.mu, args.LE)
        q = q/3 + 2/3*(q2 + args.ds*k3)
        q = D.filt(G, q)
        s += args.ds; k += 1
        if info['cl'] > 1: p = 1.0/info['cl']
        if k % 125 == 0:
            mask = (G.t > -6) & (G.t < 6)
            rk = float(np.abs(k1[mask]).max()/np.abs(q[mask]).max())
            idx = (G.Nth//2 - np.arange(G.Nth)) % G.Nth
            odd = float(np.abs(q - q[:, idx]).max()/np.abs(q).max())
            print(json.dumps(dict(s=round(s, 3), h=round(h, 4), cl=info['cl'], c=info['c'], bp=info['bp'],
                                  amin=info['amin'], res=rk, odd=odd, qmax=float(np.abs(q).max()))), flush=True)
            if not np.isfinite(q).all() or np.abs(q).max() > 1e8:
                print('blew up'); break
        if k % nsteps_hold == 0:
            np.savez(args.out+'_h%.3f.npz' % h, q=q, p=p, s=s, h=h, t=G.t, th=G.th, p0=G.p0)
            if h >= args.hmax - 1e-12: break
            h = min(args.hmax, h + args.dh)
    print('wall', time.time()-tw)
