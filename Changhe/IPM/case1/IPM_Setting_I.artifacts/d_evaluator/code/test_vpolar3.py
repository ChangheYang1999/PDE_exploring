# growing manufactured field: rho = x^2 y (1+r^2)^((k-3)/2) ~ r^k (sin t + sin 3t)/4 at infinity
import numpy as np
from vpolar import *
k = 0.6
def run(N, R, Nt=64, Mmax=31):
    g = LogGrid(N, 1e-3, R)
    th = 2*np.pi*np.arange(Nt)/Nt
    r = g.r; X = r[:,None]*np.cos(th)[None]; Y = r[:,None]*np.sin(th)[None]
    rho = X**2*Y*(1+r[:,None]**2)**((k-3)/2)
    fm, bad, hi = modes_from_samples(rho, Mmax)
    # exact far tail model: f_1 = f_3 = r^3 (1+r^2)^((k-3)/2)/4 ~ (1/4) r^k (1 + (k-3)/2 r^-2 + ...)
    # use 2-term asymptotics folded into one power: A r^k ; error O(R^{k-2}); good enough to test convergence in R
    th_ = {1:(0.25,k),3:(0.25,k)}
    pm = psi_modes(g, fm, 30, tail_hi=th_, tail_lo={1:(0.25,3),3:(0.25,3)})
    c = center_c(g, fm[3], tail_hi=(0.25,k), tail_lo=(0.25,3))
    return g, th, X, Y, rho, pm, c
# exact c: int_0^inf (1/4) r^3 (1+r^2)^((k-3)/2) r^-2 dr = (1/4) int r (1+r^2)^((k-3)/2) dr = (1/4)*(1/(1-k))
cex = 0.25/(1-k)
for N,R in [(300,1e2),(600,1e3),(900,1e4),(1200,1e5)]:
    g, th, X, Y, rho, pm, c = run(N,R)
    print('N=%d R=%.0e  c=%.12f  c-cex=%.2e'%(N,R,c,c-cex))
g, th, X, Y, rho, pm, c = run(900, 1e4)
psi, psr, pst = synth(pm, th)
r = g.r
puu = g.du(psi, 2); kk = np.fft.fftfreq(len(th), 1/len(th))
ptt = np.real(np.fft.ifft(-(kk**2)[None]*np.fft.fft(psi,axis=1),axis=1))
lap = (puu+ptt)/r[:,None]**2
# d_x rho exact
w = (1+r[:,None]**2)
drx = (2*X*Y*w**((k-3)/2) + X**2*Y*(k-3)*X*w**((k-5)/2))
E = -lap - drx
for a,b in [(1e-2,1),(1,10),(10,100),(100,1000)]:
    s=(r>a)&(r<b); print('E rel on r in [%g,%g]: %.2e'%(a,b, np.abs(E[s]).max()/np.abs(drx[s]).max()))
print('gauge: p_2/r^2 at r=1e2,1e3,1e4:', [pm[2][0][np.argmin(abs(r-x))]/x**2 for x in [1e2,1e3,9e3]])
print('p_2/r^(1+k) at r=1e2,1e3,1e4:', [pm[2][0][np.argmin(abs(r-x))]/x**(1+k) for x in [1e2,1e3,9e3]])
print('p_2/r^2 near 0 -> c/2:', pm[2][0][5]/r[5]**2, c/2)
