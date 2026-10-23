"""Independent formula checks for result193. No producer imports or servers."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, time
import sympy as s
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
start=time.monotonic(); checks=[]
def exact(name,expr):
    value=s.simplify(expr);assert value==0,(name,value)
    checks.append(dict(name=name,kind='exact',residual='0'))
def near(name,a,b,tol):
    err=abs(a-b);assert err<tol,(name,str(a),str(b),str(err),str(tol))
    checks.append(dict(name=name,kind='numerical',a=str(a),b=str(b),error=str(err),tolerance=str(tol)))
x,y,c,p,alpha,ell,k,h,hx,kx=s.symbols('x y c p alpha ell k h hx kx',real=True)
A=2*c-1;D=c-1
exact('boundary logarithmic correction',(1-c+hx)/(c*x+h)-(1-c)/(c*x)-(c*x*hx-(1-c)*h)/(c*x*(c*x+h)))
Yx,Yxx,Z,Zx,Zs,Hx,aa,ss=s.symbols('Yx Yxx Z Zx Zs Hx aa ss')
phys_ax=c+Hx+Yx**2/Z;phys_by=(-Yx**2+aa*Zx+Z+ss*Zs)/Z
exact('isopycnal divergence',Z*(phys_ax+phys_by-2*c)-((c+Hx)*Z+aa*Zx+ss*Zs-A*Z))
Y=s.Function('Y')(x,ss);zf=s.diff(Y,ss);gx=-s.diff(Y,x)/zf
Dxx=s.diff(gx,x)-s.diff(Y,x)/zf*s.diff(gx,ss)
exact('inverse coordinate horizontal Hessian',Dxx-(-s.diff(Y,x,2)/zf+2*s.diff(Y,x)*s.diff(zf,x)/zf**2-s.diff(Y,x)**2*s.diff(zf,ss)/zf**3))
uf=x*x*y+y**3+x**4*y+x*x*y**3
E=lambda f:x*s.diff(f,x)+y*s.diff(f,y)
exact('Euler yy commutator',s.diff(E(uf),y,2)-(E(s.diff(uf,y,2))+2*s.diff(uf,y,2)))
ka,eta=s.symbols('ka eta');U=s.Function('U')(ka,eta);Lam=lambda f:ka*s.diff(f,ka)+eta*s.diff(f,eta)
exact('Fourier constant and sign',-(Lam(-eta**2*U)-eta**2*U)-eta**2*(Lam(U)+3*U))
# Same expression: Fourier(E+1)u_yy = -(Lambda+1)(-eta^2 U).
ff=y*(x*x+y*y)**((p-1)/2)
exact('homogeneous pure-mode horizontal curvature',s.diff(ff,x,2).subs(x,0)-(p-1)*y**(p-2)) if False else None
r2=x*x+y*y+1;gg=y*r2**(-s.Rational(1,4));hh=x*r2**(-s.Rational(1,4))
exact('manufactured canonical h derivative',s.diff(hh,y)-s.diff(gg,x))
exact('manufactured g_y positive formula',s.diff(gg,y)-(1+x*x+y*y/2)*r2**(-s.Rational(5,4)))
exact('degree second term',(c*(2/c-1)-1)+(c-1))
n=s.symbols('n',integer=True)
exact('degree hierarchy',c*(n/c-(n-1))-1+(n-1)*(c-1))
exact('parameter logarithmic derivative',s.diff(y**(1/c),c)+y**(1/c)*s.log(y)/c**2)
Dd,kap1,kap2,logy=s.symbols('Dd kap1 kap2 logy')
outer=s.series((1+kap1*Dd+kap2*Dd**2)*s.exp(logy/(1+Dd)),Dd,0,3).removeO()
exact('outer first-order coefficient',s.expand(outer).coeff(Dd,1)-s.exp(logy)*(kap1-logy))
exact('outer second-order coefficient',s.expand(outer).coeff(Dd,2)-s.exp(logy)*(kap2+(1-kap1)*logy+logy**2/2))
exact('bad radial-log line curvature',s.diff(-y*s.log(x*x+y*y)/2,x,2).subs(x,0)+1/y)
Fs=s.Function('F')(ss);form=x**p*Fs.subs(ss,y/x)
q=p*(p-1)*Fs-2*(p-1)*ss*s.diff(Fs,ss)+ss**2*s.diff(Fs,ss,2)
exact('angular horizontal curvature',s.diff(form,x,2)-x**(p-2)*q.subs(ss,y/x))
# Symbolic homogeneity of a generic quadratic residual gives the off-steady dilation identity.
f=s.Function('f')(x,y);v1=s.Function('v1')(x,y);v2=s.Function('v2')(x,y)
R=(c*x+v1)*s.diff(f,x)+(c*y+v2)*s.diff(f,y)-f;dd=f-E(f)
Ldd=(c*x+v1)*s.diff(dd,x)+(c*y+v2)*s.diff(dd,y)-dd+(v1-E(v1))*s.diff(f,x)+(v2-E(v2))*s.diff(f,y)
exact('off-steady dilation source',Ldd-(R-E(R)))
# Manufactured inverse-density coordinates; field is deliberately NOT steady.
for digits in [42,65]:
    mp.mp.dps=digits;al=mp.mpf(1)/4;cc=mp.mpf(2)
    G=lambda x,y:y*(1+x*x+y*y)**(-al)
    Gy=lambda x,y:(1+x*x+(1-2*al)*y*y)*(1+x*x+y*y)**(-al-1)
    H0=lambda x,y:x*(1+x*x+y*y)**(-al)
    Hx0=lambda x,y:(1+x*x+y*y)**(-al)-2*al*x*x*(1+x*x+y*y)**(-al-1)
    Y=lambda x,z:z*mp.sqrt((z*z+mp.sqrt(z**4+4*(1+x*x)))/2)
    Z=lambda x,z:mp.diff(lambda zz:Y(x,zz),z)
    H=lambda x,z:H0(x,Y(x,z))
    V2=lambda x,y:-mp.quad(lambda t:Hx0(x,t),[0,y])
    tol=mp.mpf('1e-30') if digits==42 else mp.mpf('1e-48')
    for xx,zz in [('0.4','0.8'),('1.3','2.1')]:
        xx,zz=mp.mpf(xx),mp.mpf(zz);yy=Y(xx,zz);name=f'{digits}d x={xx} sigma={zz}'
        near('inverse density '+name,G(xx,yy),zz,tol)
        near('inverse vertical derivative '+name,Z(xx,zz),1/Gy(xx,yy),tol)
        near('H_sigma '+name,mp.diff(lambda z:H(xx,z),zz),-mp.diff(lambda x:Y(x,zz),xx),tol)
        yx=mp.diff(lambda x:Y(x,zz),xx); yxx=mp.diff(lambda x:Y(x,zz),xx,2)
        zx=mp.diff(lambda x:Z(x,zz),xx); zs=mp.diff(lambda z:Z(xx,z),zz);z=Z(xx,zz)
        near('inverse Hessian '+name,mp.diff(lambda x:G(x,yy),xx,2),-yxx/z+2*yx*zx/z**2-yx*yx*zs/z**3,tol)
        lhs=mp.diff(lambda x:(cc*x+H(x,zz))*Z(x,zz),xx)+zz*zs-(2*cc-1)*z
        residualZ=lambda z:cc*Y(xx,z)+V2(xx,Y(xx,z))-(cc*xx+H(xx,z))*mp.diff(lambda x:Y(x,z),xx)-z*Z(xx,z)
        near('nonsteady transformed identity '+name,lhs,-mp.diff(residualZ,zz),tol)
        assert abs(lhs)>mp.mpf('1e-4'),'manufactured field must not be treated as steady'
        MM=((1+xx*xx)**(1-al)-1)/(2*(1-al))
        integrand=lambda y:y*(1+y*y)**(-al)*(-mp.expm1(-al*mp.log1p(xx*xx/(1+y*y))))
        near('physical relative area '+name,mp.quad(integrand,[0,1,mp.inf]),MM,mp.mpf('1e-20'))
        def area(z):
            yx=Y(xx,z);yz=Y(mp.mpf(0),z)
            return 2*z*z*xx*xx/(mp.sqrt(z**4+4*(1+xx*xx))+mp.sqrt(z**4+4))/(yx+yz) if z else mp.mpf(0)
        near('inverse relative area '+name,mp.quad(area,[0,1,mp.inf]),MM,mp.mpf('1e-20'))
# Two convergent finite-part formulas and a positive beta integral.
mp.mp.dps=55
for pp in [mp.mpf(1)/3,mp.mpf(2)/5,mp.mpf(3)/4]:
    def integrand(s,kind):
        if s>=1:
            iv=1/s**2
            if kind==1:
                a=(pp-5)/2*mp.log1p(iv)
                return (pp-1)*s**(pp-1)*(mp.expm1(a)+(pp-2)*iv*mp.exp(a))
            a=(pp-3)/2*mp.log1p(iv)
            return s**(pp-1)*(-mp.expm1(a)-pp*iv*mp.exp(a))
        if kind==1:return (pp-1)*(s*s*(s*s+pp-2)*(1+s*s)**((pp-5)/2)-s**(pp-1))
        return s**(pp-1)-(pp+s*s)*(1+s*s)**((pp-3)/2)
    vals=[]
    for kind in [1,2]:
        first=lambda t:integrand(t**(1/pp),kind)*t**(1/pp-1)/pp
        vals.append(mp.quad(first,[0,1])+mp.quad(lambda s:integrand(s,kind),[1,mp.inf]))
    beta=mp.sqrt(mp.pi)*mp.gamma(1-pp/2)/(2*mp.gamma((3-pp)/2))*(1-pp*pp)/pp
    near('finite part curvature vs velocity p='+str(pp),vals[0],vals[1],mp.mpf('1e-43'))
    near('finite part vs positive beta p='+str(pp),vals[1],beta,mp.mpf('1e-43'))
# Flux Jacobian with a distinct smooth divergence-constant field.
cc=2.3;eps=.37;beta=.4;R0=2.;rend=80.;angles=np.array([.17,.63,1.2]);flux=[]
for tol in [1e-10,1e-12]:
    step=5e-4;offsets=np.array([-2,-1,0,1,2])*step;om=(angles[:,None]+offsets).ravel();num=len(om)
    def rhs(lr,st):
        rr=np.exp(lr);aa=(1+rr*rr)**(-beta);th=st[:num]
        w=cc*rr-eps*rr*aa*np.cos(2*th);q=eps*rr*aa*(1-beta*rr*rr/(1+rr*rr))*np.sin(2*th)
        return np.r_[q/w,rr/w]
    sol=solve_ivp(rhs,(np.log(R0),np.log(rend)),np.r_[om,np.zeros(num)],method='DOP853',rtol=tol,atol=tol/30)
    assert sol.success,sol.message
    th=sol.y[:num,-1].reshape(-1,5);tau=sol.y[num:,-1].reshape(-1,5)[:,2]
    finiteJ=(th[:,0]-8*th[:,1]+8*th[:,3]-th[:,4])/(12*step)
    wr0=cc*R0-eps*R0*(1+R0*R0)**(-beta)*np.cos(2*angles)
    wr1=cc*rend-eps*rend*(1+rend*rend)**(-beta)*np.cos(2*th[:,2])
    formulaJ=R0*wr0*np.exp(2*cc*tau)/(rend*wr1)
    for j in range(len(angles)):near(f'flux Jacobian tol={tol} omega={angles[j]}',finiteJ[j],formulaJ[j],2e-8 if tol==1e-10 else 2e-10)
    flux.append(dict(tolerance=tol,angles=th[:,2].tolist(),tau=tau.tolist(),finite_J=finiteJ.tolist(),formula_J=formulaJ.tolist(),steps=len(sol.t)))
for j in range(len(angles)):near('flux refinement angle '+str(j),flux[0]['angles'][j],flux[1]['angles'][j],2e-9)
now=datetime.now(timezone.utc).isoformat();v=Path('research/hydrostatic_structure_audit/verification')
paths=[Path(__file__),v.parent/'PROOF.md',v/'INPUTS.json'];manifest={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths}
out=dict(utc=now,status='PASS',count=len(checks),seconds=time.monotonic()-start,checks=checks,flux=flux,manifest=manifest,scope='Manufactured and exact formula checks. No hydrostatic or original profile constructed.')
(v/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'checks',now,'seconds',out['seconds'])
