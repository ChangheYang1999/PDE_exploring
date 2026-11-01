# Lead check of verifier topics 122 and 124: componentwise box B=2*Y0 for the Theorem T majorant system,
# G(z0,B) = Y0 + Q*(Phi(z0,B)-c-J*B) <= B, exact rational arithmetic, with the lead's own Phi (as in majorant_disk_check.py).
import sympy as sp
def system(a,kap,sig):
    z,W,U,V,E=sp.symbols('z W U V E')
    d=sp.Rational(3,2)*kap*a**2; e=3*kap*a*d; P=a*z+d*z**2+e*z**3; h=sp.Rational(3,2)
    Phi=[h*kap*(d**2+2*a*e+2*d*e*z+e**2*z**2)+3*kap*P*W+h*kap*z**4*W**2+kap*E*(P+z**4*W),
         h*kap*(2*d*e+e**2*z)+3*kap*sp.expand(P/z)*W+h*kap*z**3*W**2+kap*z**3*E*W,
         h*kap*(e**2+2*(d+e*z)*W+z**2*W**2)+kap*z**2*E*W+3*kap*a*U,
         (kap/sig)*(3*e*W+h*z*W**2+z*E*W+3*a*V+3*d*U)]
    return (z,W,U,V,E),[sp.expand(f) for f in Phi]
cases=[('both roots, common',sp.Integer(2),sp.Integer(10),sp.Rational(1,100000),42),
       ('root 1 refined',sp.Rational(1281,1000),sp.Rational(28,3),sp.Rational(38124,10**9),38),
       ('root 2 refined',sp.Rational(1647,1000),sp.Rational(28,3),sp.Rational(15683,10**7),34),
       ('three-mode family',sp.Integer(3),sp.Integer(14),sp.Rational(1,200000),48)]
for name,a,kap,sig,q in cases:
    (z,W,U,V,E),Phi=system(a,kap,sig); Y=[W,U,V,E]; zero={z:0,W:0,U:0,V:0,E:0}
    c=sp.Matrix([f.subs(zero) for f in Phi]); J=sp.Matrix([[sp.diff(f,y).subs(zero) for y in Y] for f in Phi])
    assert J**4==sp.zeros(4,4); Q=sp.eye(4)+J+J**2+J**3; Y0=Q*c; B=2*Y0
    res=[]
    for qq in (q-2,q):
        z0=sp.Integer(2)**-qq; sub=dict(zip([z]+Y,[z0]+list(B)))
        Pv=sp.Matrix([f.subs(sub) for f in Phi]); G=Y0+Q*(Pv-c-J*B)
        ratios=[G[i]/B[i] for i in range(4)]; res.append((qq,max(ratios)<=1,float(max(ratios))))
    print('%-20s z0=2^-%d: ok=%s max ratio %.5f; z0=2^-%d: ok=%s max ratio %.5f; R > 2^%.1f'%(name,res[1][0],res[1][1],res[1][2],res[0][0],res[0][1],res[0][2],1.5*q))
# topic 122 scalar box for the family: M=2^70, z0=2^-160
a,kap,sig=sp.Integer(3),sp.Integer(14),sp.Rational(1,200000)
(z,W,U,V,E),Phi=system(a,kap,sig); Y=[W,U,V,E]; zero={z:0,W:0,U:0,V:0,E:0}
c=sp.Matrix([f.subs(zero) for f in Phi]); J=sp.Matrix([[sp.diff(f,y).subs(zero) for y in Y] for f in Phi]); Q=sp.eye(4)+J+J**2+J**3; Y0=Q*c
Psi=[sp.expand((Phi[i]-c[i]-sum(J[i,j]*Y[j] for j in range(4)))/z) for i in range(4)]
M=sp.Integer(2)**70; QP=Q*sp.Matrix([p.subs({z:1,W:2*M,U:2*M,V:2*M,E:2*M}) for p in Psi])
print('topic 122 family: d,e =',3*kap*a**2/2,3*kap*a*(3*kap*a**2/2),' max Y0<=2^70:',max(Y0)<=M,' 2^-160*max QPsi<=M:',max(QP)<=M*2**160,' log2 max QPsi=%.2f'%float(sp.log(max(QP),2)))
