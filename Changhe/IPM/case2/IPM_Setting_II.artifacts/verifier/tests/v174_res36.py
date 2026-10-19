# Independent check of the formulas of the lead's draft 4.17(b), 9.13 Steps 2-3, 7 and referee result 36 (4.5), by direct
# quadrature of the canonical law W[h](X) = int (K(X-Y) - K(-Y)) h(Y) dY - (h(X) - h(0))/2 e_2 with
# K(Z) = (-2 Z1 Z2, Z1^2 - Z2^2)/(2 pi |Z|^4) (my own code; targets X outside supp h, so no principal value).
# Test densities: h = chi(r)(5 cos th - cos 5th)/4 and g = chi(r) cos 3th, chi(s) = exp(-1/((s-1)(2-s))) on (1,2).
import numpy as np
def chi(s):
    out=np.zeros_like(s); m=(s>1)&(s<2); out[m]=np.exp(-1/((s[m]-1)*(2-s[m]))); return out
Nr,Nt=400,2048
u,w=np.polynomial.legendre.leggauss(Nr); rq=1.5+0.5*u; wq=0.5*w
tq=2*np.pi*np.arange(Nt)/Nt; R,T=np.meshgrid(rq,tq,indexing='ij'); Y1=R*np.cos(T); Y2=R*np.sin(T)
dA=(wq[:,None]*R)*(2*np.pi/Nt)
def K(Z1,Z2):
    q=Z1*Z1+Z2*Z2; return -2*Z1*Z2/(2*np.pi*q*q), (Z1*Z1-Z2*Z2)/(2*np.pi*q*q)
def W(dens,X):
    a1,a2=K(X[0]-Y1,X[1]-Y2); b1,b2=K(-Y1,-Y2)
    return np.array([np.sum((a1-b1)*dens*dA),np.sum((a2-b2)*dens*dA)])
fh=lambda t:(5*np.cos(t)-np.cos(5*t))/4
H=chi(R)*fh(T); G=chi(R)*np.cos(3*T)
# 1d integrals of chi by high-order quadrature
uu,ww=np.polynomial.legendre.leggauss(2000); s=1.5+0.5*uu; ws=0.5*ww
I=lambda k:np.sum(ws*s**k*chi(s))
C1=(5/8)*I(2); C5=-(1/40)*I(6); D1=2*C1; D5=30*C5; A5=-(1/40)*I(-4); B=I(-2)
print('D1=(5/4)int s^2 chi =',D1,' D5=-(3/4)int s^6 chi =',D5)
ok=True
def rep(name,num,ex,tol=1e-9):
    global ok
    e=np.max(np.abs(np.asarray(num)-np.asarray(ex))); sc=max(1e-300,np.max(np.abs(ex)))
    flag='OK' if e<=tol*max(1,sc) or e<=tol else 'FAIL'; ok&=(flag=='OK')
    print(f'{name:58s} num={np.array2string(np.asarray(num),precision=10)} exact={np.array2string(np.asarray(ex),precision=10)} err={e:.2e} {flag}')
# angular identity
t=np.linspace(0,2*np.pi,1001); rep('cos^3(1+4sin^2) - (5cos-cos5)/4',np.max(np.abs(np.cos(t)**3*(1+4*np.sin(t)**2)-fh(t))),0.0,1e-13)
rep('min of f on |th|<=pi/2 (>=0)',min(0,np.min(fh(np.linspace(-np.pi/2,np.pi/2,1001)))),0.0,1e-15)
# far field r>2: W_r = -D1 r^-3 sin2th - D5 r^-7 sin6th, W_th = D1 r^-3 cos2th + D5 r^-7 cos6th
for r in (2.5,3.0,4.0,7.0):
    for th in (-np.pi/4,np.pi/4,0.3,1.1,2.0,np.pi/2):
        X=np.array([r*np.cos(th),r*np.sin(th)]); v=W(H,X)
        vr=v[0]*np.cos(th)+v[1]*np.sin(th); vt=-v[0]*np.sin(th)+v[1]*np.cos(th)
        ex=[-D1*r**-3*np.sin(2*th)-D5*r**-7*np.sin(6*th), D1*r**-3*np.cos(2*th)+D5*r**-7*np.cos(6*th)]
        rep(f'h: (W_r,W_th) at r={r}, th={th:+.4f}',[vr,vt],ex,1e-10)
        if abs(abs(th)-np.pi/4)<1e-12: print('    ray th=%+.4f: W_th=%.2e, W_r=%.6e (expected sign %s)'%(th,vt,vr,'+' if th<0 else '-'))
# inner region r<1: W[h] = 20 A5 r^3 (sin3th, cos3th) (homogeneous cubic, so DW[h](0)=0 and c[h]=d[h]=0)
for r in (0.2,0.5,0.8):
    for th in (0.0,0.7,np.pi/2,2.5,-1.0):
        X=np.array([r*np.cos(th),r*np.sin(th)]); rep(f'h: W at r={r}, th={th:+.4f} vs 20A5 r^3(sin3th,cos3th)',W(H,X),20*A5*r**3*np.array([np.sin(3*th),np.cos(3*th)]),1e-10)
# moments by quadrature (9.8 Step 1): pi c = int h r^-3 sin3th, -pi d = int h r^-3 cos3th
mom=lambda D,f: np.sum(D*R**-3*f(3*T)*dA)
rep('h: c[h] = (1/pi) int h r^-3 sin3th',mom(H,np.sin)/np.pi,0.0,1e-13)
rep('h: d[h] = -(1/pi) int h r^-3 cos3th',-mom(H,np.cos)/np.pi,0.0,1e-13)
# (4.5): v_1(0,y) = (y^3/2) int_y^inf chi s^-4 ds + (1/(4y^3)) int_0^y chi s^2 (5-3(s/y)^4) ds, y>0, odd in y
def ex45(y):
    m=s>=y; a=0.5*y**3*np.sum(ws[m]*chi(s[m])*s[m]**-4); m2=s<y; b=np.sum(ws[m2]*chi(s[m2])*s[m2]**2*(5-3*(s[m2]/y)**4))/(4*y**3); return a+b
for y in (0.3,0.9,2.2,3.5,6.0):
    rep(f'h: (4.5) v_1(0,{y})',W(H,np.array([0,y]))[0],ex45(y),1e-10)
    rep(f'h: v_1(0,-{y}) = -v_1(0,{y})',W(H,np.array([0,-y]))[0],-ex45(y),1e-10)
# g = chi cos3th: W[g] = B (y, x) on r<1, so DW[g](0) = [[0,B],[B,0]] = [[-c,-d],[-d,c]], d[g] = -B = -int chi r^-2 dr
rep('g: d[g] by moment = -int chi r^-2 dr',-mom(G,np.cos)/np.pi,-B,1e-12)
rep('g: c[g] by moment = 0',mom(G,np.sin)/np.pi,0.0,1e-13)
for X in ([0.0,0.4],[0.4,0.0],[0.3,-0.5],[-0.6,0.2]):
    X=np.array(X); rep(f'g: W[g]({X}) = B (y, x)',W(G,X),B*np.array([X[1],X[0]]),1e-10)
print('d[g] =',-B,'< 0')
print('ALL OK' if ok else 'SOME FAIL')
