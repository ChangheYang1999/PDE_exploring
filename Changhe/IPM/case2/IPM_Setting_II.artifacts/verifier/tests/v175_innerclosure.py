# Size of the pfwd.py inner closure discrepancy (notes of the numerical researcher 17:08Z item 3(f)): the inward kernel's inner term
# h_0/(|m|+2) (exact for f_m = const below r_min) against h_0/(|m|+3) (exact for f_m ~ r, the m = +-1 modes of rho_x
# for the quadratic jet), and the m = 1 renormalised integral's inner term hq_0 against hq_0/2.  The class is imported
# read-only on the CPU; only the two inner closure entries are changed in a copy.  Test density rho = x^2 exp(-r^2).
import sys, math, numpy as np, torch
torch.set_num_threads(1)
sys.path.insert(0, 'code')
from pfwd import PFwd
for lo in (-14.0, -8.0):
    P = PFwd(Nr=int(round((6.0-lo)/0.05))+1, Nth=64, lo=lo, hi=6.0, p=0.34, dev='cpu')
    R = P.r[:, None]; X = R*P.cos[None, :]; Y = R*P.sin[None, :]
    rho = X**2*torch.exp(-R**2)
    Wr0, Wt0 = P.velocity(rho)
    a = P.m
    # rebuild the inward recursion of pfwd.py with the inner term h_0/(a+3) in row 0
    Nr = P.Nr; d = P.d; z = a*d; small = z < 1e-8; zz = torch.where(small, torch.ones_like(z), z)
    wprev = torch.where(small, torch.full_like(z, d/2), d*(1-torch.exp(-zz)*(1+zz))/zz**2)
    wcur = torch.where(small, torch.full_like(z, d/2), d*(zz-1+torch.exp(-zz))/zz**2)
    lam = torch.exp(-z); I = torch.eye(Nr, dtype=torch.float64)
    Kin = torch.zeros_like(P.Kin); Kin[:, 0, :] = (1.0/(a+3.0))[:, None]*I[0][None, :]
    for k in range(1, Nr):
        Kin[:, k, :] = lam[:, None]*Kin[:, k-1, :] + wprev[:, None]*I[k-1][None, :] + wcur[:, None]*I[k][None, :]
    P.Kin = Kin
    P.K1 = P.K1.clone(); P.K1 -= 0.5*torch.outer(torch.ones(Nr, dtype=torch.float64), I[0])   # inner term hq_0 -> hq_0/2
    Wr1, Wt1 = P.velocity(rho)
    dW = torch.sqrt((Wr1-Wr0)**2 + (Wt1-Wt0)**2).max(dim=1).values
    Wn = torch.sqrt(Wr0**2 + Wt0**2).max(dim=1).values
    r0 = math.exp(lo)
    print(f'lo={lo}: r_min={r0:.3e}, r_min^2/4={r0**2/4:.3e}')
    for rr in (r0, 10*r0, 1e-3, 1e-1, 1.0, 3.0):
        i = int(torch.argmin(torch.abs(P.r - rr)))
        print(f'   r={float(P.r[i]):.3e}: max_th |dW| = {float(dW[i]):.3e}, max_th |W| = {float(Wn[i]):.3e}, rel = {float(dW[i]/max(Wn[i],1e-300)):.3e}')
