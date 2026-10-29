"""Exact symbolic audit. No numerical solvers, network, threads, or servers."""
import sympy as s

r, z = s.symbols("r z", positive=True)
c, a, b, p, m, d, l = s.symbols("c a b p m d l")
alpha = s.symbols("alpha", positive=True)
phi = s.Function("phi")(r, z)
q = s.Function("q")(r, z)
P = s.Function("P")(r, z)

def check(name, expression):
    ans = s.simplify(s.expand(expression))
    assert ans == 0, (name, ans)
    print(name + ": 0")

def show(name, expression):
    print(name + ": " + str(s.factor(expression)))

def adv(vr, vz, f):
    return vr * s.diff(f, r) + vz * s.diff(f, z)

def div3(fr, fz):
    return s.diff(fr, r) + fr / r + s.diff(fz, z)

def div5(fr, fz):
    return s.diff(fr, r) + 3 * fr / r + s.diff(fz, z)

def lap5(f):
    return div5(s.diff(f, r), s.diff(f, z))

ur, ut, uz = -r * s.diff(phi, z), r*q, 2*phi+r*s.diff(phi, r)
wr, wz = c*r+ur, c*z+uz
v = ur/r
eta = -lap5(phi)
gamma = r*ut
omr, omt, omz = -s.diff(ut, z), r*eta, s.diff(ut, r)+ut/r
Mr = (1-c)*ur+adv(wr,wz,ur)-ut**2/r+s.diff(P,r)
Mt = (1-c)*ut+adv(wr,wz,ut)+ur*ut/r
Mz = (1-c)*uz+adv(wr,wz,uz)+s.diff(P,z)
Rq = q+adv(wr,wz,q)+2*v*q
Re = (1+c)*eta+adv(wr,wz,eta)-s.diff(q*q,z)
check("div U", div3(ur,uz))
check("div5 W", div5(wr,wz)-(5*c+2*v))
check("swirl residual", Mt-r*Rq)
check("eta residual", s.diff(Mr,z)-s.diff(Mz,r)-r*Re)
check("Gamma transport", adv(wr,wz,gamma)-(2*c-1)*gamma-r*r*Rq)
check("nonlinear phi cancellation", adv(ur,uz,phi)+2*v*phi)
check("v eta divergence", v*eta-div5(s.diff(phi,z)*s.diff(phi,r),
                                      s.diff(phi,z)**2)
      +s.diff((s.diff(phi,r)**2+s.diff(phi,z)**2)/2,z))

e = (ur**2+ut**2+uz**2)/2
h = ur*omr+ut*omt+uz*omz
check("energy local law",
      div3(e*wr+P*ur,e*wz+P*uz)-(5*c-2)*e
      -(ur*Mr+ut*Mt+uz*Mz))
cmr, cmt, cmz = -s.diff(Mt,z), s.diff(Mr,z)-s.diff(Mz,r), s.diff(Mt,r)+Mt/r
check("helicity local law",
      div3(h*wr+(P-e)*omr,h*wz+(P-e)*omz)-(4*c-2)*h
      -(omr*Mr+omt*Mt+omz*Mz+ur*cmr+ut*cmt+uz*cmz))
check("helicity 5D conversion",
      h-2*r*r*q*eta-div3(r*q*uz,-r*q*ur))
Yu = r*ur+z*uz
check("trace virial local law",
      div3(Yu*wr+P*r,Yu*wz+P*z)-(5*c-1)*Yu
      -(2*e+3*P)-(r*Mr+z*Mz))
check("axial virial local law",
      div3(z*uz*wr,z*uz*wz+P*z)-(5*c-1)*z*uz
      -(uz*uz+P)-z*Mz)
Bernoulli=e+P+c*Yu+c*(2*c-1)*(r*r+z*z)/2
check("Bernoulli local law",
      adv(wr,wz,Bernoulli)-(2*c-1)*(wr*wr+ut*ut+wz*wz)
      -(wr*Mr+ut*Mt+wz*Mz))
Du = [adv(r,z,u) for u in (ur,ut,uz)]
Nv = [adv(ur,uz,ur)-ut*ut/r,
      adv(ur,uz,ut)+ur*ut/r,adv(ur,uz,uz)]
check("divergence of dilation velocity",div3(Du[0],Du[2]))
check("dilation multiplier local law",
      sum(x*y for x,y in zip((Mr,Mt,Mz),Du))
      -(1-c)*adv(r,z,e)-c*sum(x*x for x in Du)
      -sum(x*y for x,y in zip(Nv,Du))-div3(P*Du[0],P*Du[2]))
Vr,Vt,Vz=[s.Function(name)(r,z) for name in ("Vr","Vt","Vz")]
UV=ur*Vr+ut*Vt+uz*Vz
UUDV=ur*(adv(ur,uz,Vr)-ut*Vt/r)+ut*(adv(ur,uz,Vt)+ut*Vr/r)+uz*adv(ur,uz,Vz)
UDV=sum(ui*adv(r,z,vi) for ui,vi in zip((ur,ut,uz),(Vr,Vt,Vz)))
check("general momentum test identity",
      div3(UV*wr+P*Vr,UV*wz+P*Vz)+(1-4*c)*UV-c*UDV
      -UUDV-P*div3(Vr,Vz)-(Vr*Mr+Vt*Mt+Vz*Mz))
for degree, H, stress in [
    (0,s.Integer(1),s.Integer(0)),
    (1,z,s.Integer(0)),
    (2,z*z-r*r/2,2*uz*uz-ur*ur-ut*ut)]:
    UgH=adv(ur,uz,H)
    check("pressure stress moment degree "+str(degree),
          H*div3(Nv[0],Nv[2])
          -div3(H*Nv[0]-ur*UgH,H*Nv[2]-uz*UgH)-stress)
    check("pressure Green moment degree "+str(degree),
          -H*div3(s.diff(P,r),s.diff(P,z))
          -div3(P*s.diff(H,r)-H*s.diff(P,r),
                P*s.diff(H,z)-H*s.diff(P,z)))

# General scalar transport identity, without imposing a power at its zeros.
f = s.Function("f")(r,z)
w = r**a*z**b
lam = s.symbols("lam")
check("weighted transport product rule",
      div3(w*f*wr,w*f*wz)
      -(3*c+c*(a+b)+lam)*w*f
      -f*adv(ur,uz,w)-w*(adv(wr,wz,f)-lam*f))
check("eta weighted stress product rule",
      2*w*v*eta
      -div5(2*w*s.diff(phi,z)*s.diff(phi,r),
            2*w*s.diff(phi,z)**2-w*(s.diff(phi,r)**2+s.diff(phi,z)**2))
      +2*s.diff(phi,z)*adv(s.diff(phi,r),s.diff(phi,z),w)
      -(s.diff(phi,r)**2+s.diff(phi,z)**2)*s.diff(w,z))
check("q squared 5D law",
      div5(q*q*wr,q*q*wz)+(2-5*c)*q*q+2*v*q*q-2*q*Rq)
check("eta squared 5D law",
      div5(eta**2*wr,eta**2*wz)+(2-3*c)*eta**2
      -2*v*eta**2-2*eta*s.diff(q*q,z)-2*eta*Re)

# Pohozaev pointwise divergence identity in dimension five.
grad2 = s.diff(phi,r)**2+s.diff(phi,z)**2
Dphi = adv(r,z,phi)
check("5D elliptic Pohozaev",
      eta*Dphi+s.Rational(3,2)*grad2
      -div5(r*grad2/2-Dphi*s.diff(phi,r),
            z*grad2/2-Dphi*s.diff(phi,z)))
# Identity needed for the z eta moment.
uzphi_grad = adv(s.diff(phi,r),s.diff(phi,z),2*phi+r*s.diff(phi,r))
check("z eta bulk reduction",
      uzphi_grad-s.diff(phi,r)**2
      -div5(r*grad2/2,0))
check("kinetic energy 5D conversion",
      (ur*ur+uz*uz)/r**2-grad2-div5(2*phi*phi/r,0))
check("eta times phi local identity",
      (1-4*c)*phi*eta-c*eta*Dphi
      +div5(phi*eta*wr,phi*eta*wz-phi*q*q)-v*q*q-phi*Re)
check("q general power local identity",
      div5(q**p*wr,q**p*wz)+(p-5*c)*q**p
      +(2*p-2)*v*q**p-p*q**(p-1)*Rq)

# Coefficients, radial degrees, and the critical exponents.
cc = 1/(1+alpha)
for name, expr in [
    ("energy coefficient",5*c-2), ("helicity coefficient",4*c-2),
    ("momentum degree m coefficient",(4+m)*c-1),
    ("Gamma weighted coefficient",c*(3+a+b)+p*(2*c-1)),
    ("eta weighted coefficient",1-(4+m)*c),
    ("phi energy coefficient",1-s.Rational(5,2)*c),
    ("eta squared coefficient",2-3*c)]:
    show(name,expr)
beta=alpha+1
sigma=3-2*alpha
tau=2-3*alpha
check("energy leading powers", (5*c-2-c*sigma).subs(c,cc))
check("energy correction gap", (5*c-2-c*tau-1).subs(c,cc))
check("helicity leading powers",(4*c-2-c*(2-2*alpha)).subs(c,cc))
check("Gamma characteristic powers",(c*(1-alpha)-(2*c-1)).subs(c,cc))
check("q characteristic powers",(c*(alpha+1)-1).subs(c,cc))
check("eta characteristic powers",(c*(alpha+2)-(1+c)).subs(c,cc))
check("forcing characteristic gap",(c*(2*alpha+3)-(2+c)).subs(c,cc))
for name,expr in [
    ("energy leading R exponent",sigma),
    ("energy correction / cubic flux R exponent",tau),
    ("next energy R exponent",1-4*alpha),
    ("helicity leading R exponent",2-2*alpha),
    ("helicity correction / flux R exponent",1-3*alpha),
    ("Gamma moment leading R exponent",3+a+b+p*(1-alpha)),
    ("eta integral leading R exponent",3-alpha),
    ("eta integral first nonlinear R exponent",2-2*alpha),
    ("eta integral next nonlinear R exponent",1-3*alpha),
    ("eta squared leading R exponent",1-2*alpha),
    ("eta squared nonlinear integral tail R exponent",-3*alpha),
    ("degree-l pressure moment boundary exponent",l+1-d)]:
    show(name,expr)
show("energy critical c",s.solve(tau.subs(alpha,(1-c)/c),c)[0])
show("eta squared critical c",s.solve((1-2*alpha).subs(alpha,(1-c)/c),c)[0])

# Symbolic far field, retaining generic A and B.
mu=s.symbols("mu",real=True)
t=1-mu**2
A=s.Function("A")(mu)
B=s.Function("B")(mu)
FR=2*mu*A-t*s.diff(A,mu)
FV=(alpha-2)*A  # actual polar component is sqrt(t)*FV
FT=B           # actual azimuthal component is sqrt(t)*FT
E=-(alpha*(alpha-3)*A+t*s.diff(A,mu,2)-4*mu*s.diff(A,mu))
check("far-field divergence",(2-alpha)*FR+2*mu*FV-t*s.diff(FV,mu))
ell=s.symbols("ell",nonnegative=True)
check("5D eigenvalue factorization",
      ell*(ell+3)-alpha*(alpha-3)-(ell+alpha)*(ell+3-alpha))

# Angular algebra can be done with polynomials; sqrt(t) is factored out.
NR=-alpha*FR**2-t*FV*s.diff(FR,mu)-t*FV**2-t*FT**2
NV=(1-alpha)*FR*FV+FV*(mu*FV-t*s.diff(FV,mu))-mu*FT**2
NT=(1-alpha)*FR*FT+FV*(mu*FT-t*s.diff(FT,mu))+mu*FV*FT
fsource=(1-2*alpha)*NR+2*mu*NV-t*s.diff(NV,mu)
def avg(expr):
    return s.integrate(s.expand(expr),(mu,-1,1))/2

print("Angular example: A=1+mu/5, B=1+mu/3; sphere averages = integral/(4*pi)")
for av in [s.Rational(3,4),s.Rational(2,3),s.Rational(1,2)]:
    def ex(expr):
        return s.expand(expr.subs({A:1+mu/5,B:1+mu/3}).doit().subs(alpha,av))
    nr,nv,nt,fr,fv,ft,src=map(ex,[NR,NV,NT,FR,FV,FT,fsource])
    Q=0
    for k in range(s.degree(src,mu)+1):
        pk=s.legendre(k,mu)
        sk=(2*k+1)*avg(src*pk)
        denominator=k*(k+1)-2*av*(2*av-1)
        qk=avg(nr)/(2*av) if denominator==0 and k==0 else sk/denominator
        Q+=qk*pk
    Q=s.expand(Q)
    gr=nr-2*av*Q
    gv=nv-s.diff(Q,mu)
    gt=nt
    check("G divergence alpha="+str(av),(1-2*av)*gr+2*mu*gv-t*s.diff(gv,mu))
    e0=(fr*fr+t*fv*fv+t*ft*ft)/2
    e1=avg(fr*gr+t*fv*gv+t*ft*gt)
    j0=avg((e0+Q)*fr)
    check("energy angular relation alpha="+str(av),e1-(2-3*av)*j0)
    show("  <F.G>",e1)
    show("  <(e0+Q)FR>",j0)
    if av==s.Rational(2,3):
        fz=mu*fr-t*fv
        gz=mu*gr-t*gv
        stress1=avg(6*fz*gz-2*(fr*gr+t*fv*gv+t*ft*gt))
        show("  quadrupole log L2 = <cross stress>",stress1)

# Alternative dipole proof: velocity=-d0 grad(z/R^3), P=p1*z/R^3.
d0,p1=s.symbols("d0 p1")
show("dipole mean Uz divided by 4pi",2*d0/3)
show("dipole local pressure coefficient",(1-4*c)*d0)
check("dipole global contradiction coefficient",
      ((4*c-1)*2*d0/3-p1/3).subs(p1,(1-4*c)*d0)-(4*c-1)*d0)
# Radial harmonic pressure identity, also checking the resonant log sign.
R=s.symbols("R",positive=True)
def radlap(v,degree):
    return s.diff(v,R,2)+2*s.diff(v,R)/R-degree*(degree+1)*v/R**2
check("quadrupole logarithmic Laplacian",-radlap(R**-3*s.log(R),2)-5*R**-5)
L2=s.symbols("L2")
show("quadrupole Green flux divided by 4pi",
     s.simplify((2*R*(R**-3*(p1+L2*s.log(R)))
                 -R**2*s.diff(R**-3*(p1+L2*s.log(R)),R))*R**2/5))
print("ALL SYMBOLIC CHECKS PASSED")
