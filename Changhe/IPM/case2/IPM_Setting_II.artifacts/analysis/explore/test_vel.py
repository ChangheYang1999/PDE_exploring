import numpy as np, sys
sys.path.insert(0,'explore')
import dynres as D
# test 1: rho = x^2 (1+a y)^2 e^{-r^2}: c = a/4, psi_xx(0) = 0 (referee closed form)
for Nt in [301, 601]:
    G = D.Grid(-10., 3.5, Nt, 128, 0.5)
    r = G.r[:,None]; X=r*G.cos; Y=r*G.sin
    a=0.7
    rho = X**2*(1+a*Y)**2*np.exp(-r**2)
    q = rho/G.w
    Wr_r, Wt_r, c, bp, *_ = D.velocity(G, q, 0.5)
    print(Nt, 'c', c, 'exact', a/4, 'bp', bp)
# test 2: general test density vs FFT (check_cformula density), compare W at some points
def rhof(X,Y):
    return (X**2+0.7*X*Y-0.4*Y**2+0.9*X**2*Y+0.5*Y**3-0.3*X**3)*np.exp(-((X-0.3)**2+(Y+0.2)**2)/2)
L=40.; N=1024
x = (np.arange(N)-N//2)*(L/N); XX,YY = np.meshgrid(x,x,indexing='ij')
R = rhof(XX,YY)
k = 2*np.pi*np.fft.fftfreq(N, L/N); KX,KY = np.meshgrid(k,k,indexing='ij'); K2=KX**2+KY**2; K2[0,0]=1
Rh = np.fft.fft2(R)
psih = 1j*KX*Rh/K2; psih[0,0]=0
U1 = np.real(np.fft.ifft2(-1j*KY*psih)); U2 = np.real(np.fft.ifft2(1j*KX*psih))
i0 = N//2
from scipy.interpolate import RectBivariateSpline
s1 = RectBivariateSpline(x,x,U1); s2=RectBivariateSpline(x,x,U2)
G = D.Grid(-10., 3.6, 701, 256, 0.5)
r = G.r[:,None]; X=r*G.cos; Y=r*G.sin
q = rhof(X,Y)/G.w
Wr_r, Wt_r, c, bp, *_ = D.velocity(G, q, 0.5)
Wr = Wr_r*r; Wt = Wt_r*r
W1 = Wr*G.cos - Wt*G.sin; W2 = Wr*G.sin + Wt*G.cos
u0 = np.array([s1(0,0)[0,0], s2(0,0)[0,0]])
for (it, ith) in [(400,10),(500,77),(550,200),(600,130)]:
    xx=X[it,ith]; yy=Y[it,ith]
    uf = np.array([s1(xx,yy)[0,0], s2(xx,yy)[0,0]]) - u0
    print('pt',xx,yy,'polar',W1[it,ith],W2[it,ith],'fft',uf)
# c from FFT derivative
psi = np.real(np.fft.ifft2(psih))
sp = RectBivariateSpline(x,x,psi)
print('c polar', c, 'fft', sp(0,0,dx=1,dy=1)[0,0], 'bp polar', bp, 'fft psixx', sp(0,0,dx=2)[0,0])
