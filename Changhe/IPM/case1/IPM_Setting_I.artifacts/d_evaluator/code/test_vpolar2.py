# check -Lap psi = d_x rho and U against FFT (periodic big box) for the decaying test field
import numpy as np
from vpolar import *
rho = lambda x,y: x**2*y*np.exp(-x**2-y**2)
drx = lambda x,y: (2*x - 2*x**3)*y*np.exp(-x**2-y**2)
g = LogGrid(400, 1e-3, 14.0)
Nt = 64; th = 2*np.pi*np.arange(Nt)/Nt
r = g.r; X = r[:,None]*np.cos(th)[None]; Y = r[:,None]*np.sin(th)[None]
fm, bad, hi = modes_from_samples(rho(X,Y), 31)
pm = psi_modes(g, fm, 30, tail_lo={1:(0.25,3),3:(0.25,3)})
psi, psr, pst = synth(pm, th)
# Laplacian: r^-2 (psi_uu + psi_tt)
puu = g.du(psi, 2)
k = np.fft.fftfreq(Nt, 1/Nt)
ptt = np.real(np.fft.ifft(-(k**2)[None]*np.fft.fft(psi,axis=1),axis=1))
lap = (puu+ptt)/r[:,None]**2
E = -lap - drx(X,Y)
sel = (r>0.05)&(r<6)
print('max |E| (0.05<r<6):', np.abs(E[sel]).max(), ' max|d_x rho|', np.abs(drx(X,Y)).max())
U1, U2 = velocity_polar(r, th, psr, pst)
# FFT reference on a big periodic box
L = 60.0; M = 2048
xs = (np.arange(M)-M//2)*(2*L/M)
XX, YY = np.meshgrid(xs, xs, indexing='ij')
rh = np.fft.fft2(rho(XX,YY))
kk = 2*np.pi*np.fft.fftfreq(M, 2*L/M)
K1, K2 = np.meshgrid(kk, kk, indexing='ij'); K2s = K1**2+K2**2; K2s[0,0]=1
U1f = np.real(np.fft.ifft2(K1*K2/K2s*rh)); U2f = np.real(np.fft.ifft2(-K1**2/K2s*rh))
from scipy.interpolate import RegularGridInterpolator as RGI
# compare on a few radii via spectral interpolation is overkill; use points on the grid lines: choose polar points, interpolate FFT field (fine grid, cubic)
I1 = RGI((xs,xs),U1f,method='cubic'); I2 = RGI((xs,xs),U2f,method='cubic')
for rr in [0.1,0.5,1,2,4,8]:
    j = np.argmin(np.abs(r-rr))
    pts = np.stack([X[j],Y[j]],1)
    e1 = np.abs(I1(pts)-U1[j]).max(); e2 = np.abs(I2(pts)-U2[j]).max()
    print('r=%.3f  |U| max %.3e  diff U1 %.2e U2 %.2e'%(r[j], np.abs(U1[j]).max(), e1, e2))
# centre: c = psi_xy(0); U ~ (-c x, c y)
c = center_c(g, fm[3], tail_lo=(0.25,3)); print('c=',c)
j = 10; print('U1/(-c x) at small r:', (U1[j]/(-c*X[j]))[[1,5,9]], ' U2/(c y):', (U2[j]/(c*Y[j]))[[3,5,13]])
