"""FLOAT: best G0 requirement eta/sqrt(w2) of the T2-R3 family over continuous weights (notes/T2_T4L2_sharp.md section 4).
Run from artifacts/: python3 -B arith/t4l2_g0_weight_opt.py  (numpy; about a minute). FLOAT only, not a proof."""
import numpy as np, math
# FLOAT: kernel constants (T2-R2) and the 3x3 block as functions of (w1, w2)
m1=1.57230396775; wc=1.22099598145
k1u=m1; k1w=m1+1.6; cru=1.5*m1; crw=1.5*m1+32/15; c8=1+wc*3*math.pi/4; dtop=1+wc*math.pi/2
C,U1,U2,U3,R1,R2,R3,R4=2,6,24,160,22,32,80,2048
def Cp(w1,w2):
    K00=dtop*C+c8*U1+(crw+2*k1w)*U2+k1w*R2; K01=k1w*(U3+2*R3)/math.sqrt(w1); K02=k1w*R4/math.sqrt(w2)
    K11=C+U1+(cru+k1u)*U2+k1u*R2; K12=k1u*R3*math.sqrt(w1/w2); K22=C+U1+cru*U2+k1u*R2
    return max(K00+K01/2+K02/2, K01/2+K11+K12/2, K02/2+K12/2+K22)
def mumax(w1,w2,margin=2.0):
    lo,hi=0.0,0.5
    for _ in range(60):
        m=(lo+hi)/2
        G=np.array([[0.5-m,-34.7,-5],[-34.7,w1*(0.9-m)-40,-3*w1],[-5,-3*w1,w2*(margin-m)]])
        lo,hi=(m,hi) if np.linalg.eigvalsh(G).min()>=0 else (lo,m)
    return lo
def eta(w1,w2,margin=2.0):
    m=mumax(w1,w2,margin); c=Cp(w1,w2)
    return (4/(25*math.sqrt(5)))*m**2.5/(1.6*math.sqrt(c)), m, c
best=None
for l1 in np.arange(13,19.01,0.25):
    for l2 in np.arange(l1+2,l1+8.01,0.25):
        e,m,c=eta(2**l1,2**l2); g0=e/math.sqrt(2**l2)
        if best is None or g0>best[0]: best=(g0,l1,l2,e,m,c)
print("max G0 requirement over weights (L2 margin 2): G0 %.4e at log2 w = (%.2f, %.2f), eta %.4e, mu0 %.4f, C' %.1f"%best)
for margin in (2.0,2.5,3.0,4.0):
    best=None
    for l1 in np.arange(12,19.01,0.25):
        for l2 in np.arange(l1+1,l1+8.01,0.25):
            e,m,c=eta(2**l1,2**l2,margin); g0=e/math.sqrt(2**l2)
            if best is None or g0>best[0]: best=(g0,l1,l2,e,m,c)
    print("margin %.1f: max G0 req %.4e at (%.2f, %.2f), eta %.4e, mu0 %.4f"%((margin,)+best[:5]))
