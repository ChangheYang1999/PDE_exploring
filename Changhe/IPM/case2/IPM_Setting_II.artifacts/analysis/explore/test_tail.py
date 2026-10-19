import numpy as np, sys
sys.path.insert(0,'explore')
import dynres as D
p=0.5
for t1 in [6., 9., 12., 16.]:
    Nt = int(round((t1+10)/0.04))+1
    G = D.Grid(-10., t1, Nt, 128, p)
    r = G.r[:,None]; X=r*G.cos; Y=r*G.sin
    rho = X**2*(1+0.5*Y+0.3*X)**2*(1+r**2)**((p-4)/2)
    q = rho/G.w
    Wr_r, Wt_r, c, bp, *_ = D.velocity(G, q, p)
    it = np.argmin(abs(G.t-1.0))
    # direct I2 quadrature on the same grid (+ analytic tail of r^p A: int r^{p-1} dt)
    integ = (rho/r*np.sin(3*G.th)[None,:]).sum(axis=1)*(2*np.pi/G.Nth)
    cI2 = np.trapz(integ, G.t)/np.pi
    print(t1, 'c', c, 'cI2(trunc)', cI2, 'bp', bp, 'Wr/r at r=e', Wr_r[it,5], Wt_r[it,40])
