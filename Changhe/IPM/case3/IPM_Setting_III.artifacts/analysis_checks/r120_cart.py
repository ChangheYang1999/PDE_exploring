# Lead check of verifier result 120, part 2: end-to-end Cartesian Taylor solve. rho, psi as polynomials in x, y;
# projections R_1, R_3, R_5 of each homogeneous degree solved order by order for (f_j, g_j, k_j); compares with (7)
# and checks that the order-j linear system is invertible (a outside E_c) and the quotient sign.
import sympy as s, sys
x,y,th=s.symbols('x y th',real=True)
cc=s.Rational(sys.argv[1]) if len(sys.argv)>1 else s.Integer(2)
aa=s.Rational(sys.argv[2]) if len(sys.argv)>2 else s.Integer(1000)+s.Rational(1,7)
Hh=s.Integer(1); N=int(sys.argv[3]) if len(sys.argv)>3 else 4
D=cc-1; z=x**2+y**2
im=lambda m: s.expand(s.im(s.expand((x+s.I*y)**m)))
P1,P3,P4,P5,P6=y,im(3),im(4),im(5),im(6)
fj=[aa]+[s.Symbol('f%d'%i) for i in range(1,N+1)]
gj=[0]+[s.Symbol('g%d'%i) for i in range(1,N+1)]
kj=[0,0]+[s.Symbol('k%d'%i) for i in range(2,N+1)]
known={}
def fields():
    fz=sum(fj[i]*z**i for i in range(N+1)); gz=sum(gj[i]*z**(i-1) for i in range(1,N+1)); kz=sum(kj[i]*z**(i-2) for i in range(2,N+1))
    rho=P1*fz+P3*gz+P5*kz
    T=aa/4-D-sum(gj[i]*z**i/(2*i) for i in range(1,N+1))
    J=sum(fj[i]*z**i/(2*i+4) for i in range(N+1))
    # S/z, K/z, L/z^2 as polynomials
    Soz=Hh-sum(kj[i]*z**(i-1)/(2*i-2) for i in range(2,N+1))
    Koz=sum(gj[i]*z**(i-1)/(2*i+6) for i in range(1,N+1))
    Loz2=sum(kj[i]*z**(i-2)/(2*i+8) for i in range(2,N+1))
    psi=2*x*y*(T-J)/2+P4*(Soz-Koz)/2-P6*Loz2/2
    return s.expand(rho),s.expand(psi)
def hom(e,n):
    p=s.Poly(e,x,y); return s.Integer(0)+sum(cf*x**i*y**jj for (i,jj),cf in p.terms() if i+jj==n)
def proj(h,m):
    return s.integrate(s.expand(s.expand_trig(h.subs({x:s.cos(th),y:s.sin(th)})*s.sin(m*th))),(th,0,2*s.pi))/s.pi
rho,psi=fields()
U1=-s.diff(psi,y); U2=s.diff(psi,x)
R=s.expand((cc*x+U1)*s.diff(rho,x)+(cc*y+U2)*s.diff(rho,y)-rho)
pois=s.expand(-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(rho,x))
sol={}
for jj in range(1,N+1):
    h=hom(R,2*jj+1).subs(sol)
    eqs=[s.expand(proj(h,m)) for m in (1,3,5)]
    unk=[fj[jj],gj[jj]]+([kj[jj]] if jj>=2 else [])
    if jj==1: assert s.simplify(eqs[2])==0, eqs[2]
    use=eqs if jj>=2 else eqs[:2]
    Mj=s.Matrix([[s.diff(q,u) for u in unk] for q in use])
    print('order',jj,'det of linear system:',s.simplify(Mj.det()))
    sj=s.solve(use,unk,dict=True); assert len(sj)==1; sol.update(sj[0])
    sol={kk:s.nsimplify(s.simplify(vv.subs(sol))) for kk,vv in sol.items()}
Fa=aa**2-(4*cc+20)*aa+128*cc-64
print('f1 vs (7):',s.simplify(sol[fj[1]]+24*Hh*aa*(aa-4*cc+4)/Fa),' g1 vs (7):',s.simplify(sol[gj[1]]-8*Hh*aa*(aa-4*cc-4)/Fa))
# all three projections vanish at every degree <= 2N+1; Poisson exact up to degree 2N-1
Rs=s.expand(R.subs(sol)); ps=s.expand(pois.subs(sol))
print('max |proj| through degree 2N+1:',max(abs(proj(hom(Rs,n),m)) for n in range(1,2*N+2,2) for m in (1,3,5)))
print('Poisson residual through degree 2N-1:',[hom(ps,n) for n in range(0,2*N)].count(0)==2*N)
print('psi_xy(0)=',s.diff(psi,x,y).subs({x:0,y:0}),' (should be',-D,')')
b=sol[fj[1]]+3*sol[gj[1]]; e=sol[fj[1]]-sol[gj[1]]
print('b, e:',float(b),float(e))
for i in range(2,N+1): print('k%d ='%i,float(sol[kj[i]]))
