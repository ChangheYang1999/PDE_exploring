# Numerical check: 2F2 solutions of the inner layer system, their z -> 0 even/odd coefficients (Gamma formulas).
import mpmath as mp
mp.mp.dps=40
def run(p,K=1):
    p=mp.mpf(p); c=1/p; al=(p+1)/2; lam=p*K/(2*al**2*c*(1-al))
    a1=-p/2; a2=(1-p)/2; b1=p/(p+1); b2=mp.mpf(2)
    def B1(z): t=z**-2; return t**(-p/2)*mp.hyp2f2(a1,a2,b1,b2,-lam*t)
    def B2(z): t=z**-2; return t**(-p/2+1-b1)*mp.hyp2f2(a1-b1+1,a2-b1+1,2-b1,b2-b1+1,-lam*t)
    out=[]
    for B in (B1,B2):
        # residual of system at a few z
        res=0
        for z in (mp.mpf('0.7'),mp.mpf('1.3'),mp.mpf('3.1')):
            bz=B(z); b1d=mp.diff(B,z); b2d=mp.diff(B,z,2)
            V=lambda s: -((p**2+p-2)*B(s)+(1-p)*s*mp.diff(B,s))/(2*K*p**2)
            v0=V(z); v1=mp.diff(V,z); v2=mp.diff(V,z,2)
            E2=(p**4/4+p**3/2-p**2/4-p/2)*v0+(-p**3/2-3*p**2/4+p/2+mp.mpf(3)/4)*z*v1+(p**2/4+p/2+mp.mpf(1)/4)*z**2*v2+b2d
            res=max(res,abs(E2)/(abs(b2d)+abs(v0)))
        out.append(res)
    # Gamma-formula coefficients at z -> 0 (t -> inf): t^{-p/2}(lam t)^{-a_k} terms
    def coeffs(A1,A2,BB1,BB2,shift):
        pre=mp.gamma(BB1)*mp.gamma(BB2)
        CE=pre*mp.gamma(A2-A1)/(mp.gamma(A2)*mp.gamma(BB1-A1)*mp.gamma(BB2-A1))*lam**(-A1)
        CO=pre*mp.gamma(A1-A2)/(mp.gamma(A1)*mp.gamma(BB1-A2)*mp.gamma(BB2-A2))*lam**(-A2)
        return CE,CO
    CE1,CO1=coeffs(a1,a2,b1,b2,0); CE2,CO2=coeffs(a1-b1+1,a2-b1+1,2-b1,b2-b1+1,0)
    # numeric fit at small z: b(z) ~ CE*(1+e2 z^2) + CO*z*(1+o2 z^2)
    fit=[]
    for B,CE,CO in ((B1,CE1,CO1),(B2,CE2,CO2)):
        zs=[mp.mpf('0.02'),mp.mpf('0.03'),mp.mpf('0.04'),mp.mpf('0.05')]
        M=mp.matrix([[1,zz,zz**2,zz**3] for zz in zs]); rhs=mp.matrix([B(zz) for zz in zs])
        sol=mp.lu_solve(M,rhs); fit.append((sol[0],CE,sol[1],CO))
    return out,fit,(p**2+2*p-1)/(2*(p+1))
for p in ('0.75','0.5','0.4142135623730950488','0.3333333333333333','0.25'):
    out,fit,bm=run(p)
    print('p',p,'ODE resid',[mp.nstr(r,3) for r in out],'b1-a2',mp.nstr(bm,6))
    for k,(fe,ce,fo,co) in enumerate(fit):
        print('  sol',k+1,'even fit/gamma',mp.nstr(fe,10),mp.nstr(ce,10),' odd fit/gamma',mp.nstr(fo,10),mp.nstr(co,10))
