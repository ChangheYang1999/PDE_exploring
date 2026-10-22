"""Packet184 exact controls. Exterior transport manufacture is not a coupled profile."""
from pathlib import Path
from datetime import datetime,timezone
import time,json
import sympy as s
r=Path('research/184_beta2_endpoint_sign_and_critical_flux/verification');begin=time.monotonic();utc=datetime.now(timezone.utc).isoformat();checks=[];neg=[]
def eq(name,a,b=0):
    z=s.simplify(a-b);assert z==0,(name,z);checks.append(name)
def no(name,a,b=0):
    z=s.simplify(a-b);assert z!=0,name;neg.append(name)
u,v,R,lam=s.symbols('u v R lam',real=True);q=u*u-v*v;w=-2*u*v+4*v
# A nonflat harmonic local component, for the first-order algebra only.
eq('harmonic divergence',s.diff(q,u)+s.diff(w,v),4)
eq('harmonic curl',s.diff(w,u)-s.diff(q,v))
eq('q harmonic',s.diff(q,u,2)+s.diff(q,v,2))
eq('w harmonic',s.diff(w,u,2)+s.diff(w,v,2))
M=s.Matrix([[0,0],[0,4]]);eq('endpoint tangential derivative annihilated',(s.Matrix([[1,0]])*M).norm(),0)
h=s.exp(-lam*(u*u+v*v))-s.exp(-lam*R*R)
eq('barrier Laplacian sign formula',s.diff(h,u,2)+s.diff(h,v,2),4*lam*(lam*(u*u+v*v)-1)*s.exp(-lam*(u*u+v*v)))
for j in range(1,9):
    rr=1/(4*s.pi**2*j*j);phase=s.sqrt(1/rr)*s.sin(s.pi/6)
    eq('flat example phase '+str(j),phase,j*s.pi)
    eq('flat example alternating sign '+str(j),s.cos(phase),(-1)**j)
# Exact polynomial profile equations, but violates sublinear/canonical class.
x,y=s.symbols('x y',real=True);W=s.Matrix([0,4*y-x*x]);T=x*x;O=2*x;P=2*x*y-x**3/3
adv=lambda f:W[0]*s.diff(f,x)+W[1]*s.diff(f,y)
eq('polynomial manufacture divergence',s.diff(W[0],x)+s.diff(W[1],y),4)
eq('polynomial manufacture thermal',adv(T))
eq('polynomial manufacture vorticity',adv(O)+O,s.diff(T,x))
eq('polynomial manufacture elliptic',-s.diff(P,x,2)-s.diff(P,y,2),O)
for k in [0,1,3,4,5,6]:
    for power in [0,1,2]:
        G=T**power;vec=G*O**(k+1)*W;div=s.diff(vec[0],x)+s.diff(vec[1],y)
        rhs=(k+1)*G*O**k*s.diff(T,x)+(3-k)*G*O**(k+1)
        eq(f'local weighted divergence k{k} G{power}',div,rhs)
no('critical finite boundary cannot be discarded',O**3*s.diff(T,x),0)
# Exterior exact transport manufacture in polar r=s0^2: h=cos^2, a=cos,
# c=-sin(theta)h'=2sin^2*cos and Omega=a/s0-c/s0^2.
c,a,z=s.symbols('c a z',real=True);om=a/z-c/z**2
# 2r d_r = z d_z; Theta_x=c/z^2.
eq('exterior vorticity transport',z*s.diff(om,z)+om,c/z**2)
no('exterior coupled curl fails',om,0)
for k in [3,4,5,6,7]:
    src=sum(2*s.binomial(k,j)*a**(k-j)*(-c)**j*c/s.Integer(k+j-2)for j in range(k+1))
    inner=2*(a-c)**(k+1)
    if k==3:
        eq('critical exterior flux identity',src,(2*a**4-inner)/4)
        no('critical infinite flux is nonzero',2*a**4)
    else:
        mass=sum(2*s.binomial(k+1,j)*a**(k+1-j)*(-c)**j/s.Integer(k+j-3)for j in range(k+2))
        eq('supercritical exterior flux k'+str(k),src,s.Rational(k-3,k+1)*mass-inner/(k+1))
# Integrate actual angular polynomial exactly over full and right circles.
C,S=s.symbols('C S',real=True)
def angular(poly,half):
    ans=0
    for (m,n),co in s.Poly(s.expand(poly),C,S).terms():
        assert n%2==0
        if not half and m%2:continue
        ans+=co*(1 if half else 2)*s.gamma(s.Rational(n+1,2))*s.gamma(s.Rational(m+1,2))/s.gamma(s.Rational(m+n+2,2))
    return s.simplify(ans)
rows=[]
for power in [0,1,2]:
    for half in [False,True]:
        G=C**(2*power);c0=2*S*S*C
        outer=angular(G*C**4/2,half)
        inner=angular(G*(C-c0)**4/2,half)
        src=sum(2*s.binomial(3,j)*C**(3-j)*(-c0)**j*c0/s.Integer(j+1)for j in range(4))
        total=angular(G*src,half)
        eq(f'angular critical balance weight{power} half{half}',total,outer-inner)
        assert outer>0 and inner>0 and total>0
        rows.append({'weight_power':power,'domain':'right exterior half-plane'if half else'whole exterior','volume_integral':str(total),'outer_flux_divided4':str(outer),'inner_flux_divided4':str(inner)})
eq('unweighted full critical coefficient',s.sympify(rows[0]['outer_flux_divided4']),3*s.pi/8)
no('wrong critical factor caught',s.sympify(rows[0]['outer_flux_divided4']),3*s.pi/4)
no('wrong sign of inner flux caught',s.sympify(rows[0]['volume_integral']),s.sympify(rows[0]['outer_flux_divided4'])+s.sympify(rows[0]['inner_flux_divided4']))
# Thresholds checked from radial measure, not from convergence of a numerical integral.
for k in [3,4,5,6]:
    assert s.Rational(-k,2)<-1;checks.append('source radial exponent k'+str(k))
    if k>3:assert s.Rational(1-k,2)<-1;checks.append('mass radial exponent k'+str(k))
eq('critical mass radial exponent',s.Rational(1-3,2),-1)
result={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-begin,'verdict':'PASS','exact_count':len(checks),'negative_count':len(neg),'exact_controls':checks,'negative_controls':neg,'exterior_angular_integrals':rows,'scope':'Exact algebra and manufactures only. Harmonic boundary principle, smooth flat extension and global B2 applicability are proved separately in PROOF.md.'}
(r/'controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k]for k in ['started_utc','ended_utc','elapsed_seconds','verdict','exact_count','negative_count']},indent=2))
