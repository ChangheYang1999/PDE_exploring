"""Exact arithmetic support for the standalone result90 proof.

The contraction, global continuation and regularity proofs remain informal.
No producer code or floating point arithmetic is used.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

class D:
    def __init__(self,v,d=F(0)):self.v=F(v);self.d=F(d)
    def __add__(self,o):
        o=o if isinstance(o,D)else D(o);return D(self.v+o.v,self.d+o.d)
    __radd__=__add__
    def __neg__(self):return D(-self.v,-self.d)
    def __sub__(self,o):return self+-o if isinstance(o,D)else self+D(-o)
    def __rsub__(self,o):return D(o)+-self
    def __mul__(self,o):
        o=o if isinstance(o,D)else D(o);return D(self.v*o.v,self.d*o.v+self.v*o.d)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,D)else D(o);return D(self.v/o.v,(self.d*o.v-self.v*o.d)/o.v**2)
    def __rtruediv__(self,o):return D(o)/self

checks=[]
def check(name,condition,**kw):
    assert condition,(name,kw)
    checks.append(dict(name=name,**kw))
for ell in [F(6,5),F(3,2),F(2),F(3),F(5),F(10)]:
    strain=ell-1;a=4*strain;p=1/ell;lam=2*strain/(ell+1);d0=2*ell+2
    check('exponents and denominator',0<lam<2 and a/d0==lam and 4*ell-2*strain==d0,ell=str(ell))
    for ff in [a/10,a/2,4*a/5]:
        for qq in [F(13,50),F(2,7),F(8,25)]:
            jj=qq*ff
            if not jj<strain:continue
            k=(a-ff)/(4*ell-2*jj);fd=-k*ff;jd=ff-4*jj
            f=D(ff,fd);j=D(jj,jd);kd=(a-f)/(4*ell-2*j);q=j/f
            check('chain derivatives',q.d==1-(4-k)*qq and kd.d==k*(3*ff-8*jj)/(4*ell-2*jj),ell=str(ell),f=str(ff),J=str(jj))
            h=a-f;v=strain-j
            nonlin=-h*(h+2*lam*v)/(d0+2*v)
            check('desingularized origin equations',h.d==(lam*h+nonlin).v and v.d==(h-4*v).v)
            gap=(1-p)-k
            check('strict growth rate gap',gap==ff*(ell-2*strain*qq)/(ell*(4*ell-2*jj)) and gap>0 and kd.d>0)
            E=1/(4-kd)-q
            check('positive kernel equation',E.d+(4-k)*E.v==kd.d/(4-k)**2)
            check('negative third-mode bound algebra',(1-k/2)/(4-k)-F(1,4)==-k/(4*(4-k)) and 0<k<1)
            C1=(ell-jj/2)*fd+strain*ff-ff**2/4
            C3=jj*ff+jj*fd/2-ff**2/4
            check('first projection equation',C1==0 and C3==ff**2*(qq*(1-k/2)-F(1,4)))
            for cs,sn in [(F(3,5),F(4,5)),(F(5,13),F(12,13))]:
                # Independent Cartesian gradient and polar velocity product.
                gx=cs*sn*fd;gy=ff+sn**2*fd
                c2=cs**2-sn**2;s2=2*cs*sn
                ur=jj*c2;ut=(jj-ff/2)*s2
                ux=ur*cs-ut*sn;uy=ur*sn+ut*cs
                residual=(ell*cs+ux)*gx+(ell*sn+uy)*gy-sn*ff
                check('direct angular transport multiplication',residual==C1*sn+C3*(3*sn-4*sn**3))
    for ff in [a/5,a/2,9*a/10]:
        kl=(a-ff)/(4*ell-ff/2)
        ku=(a-ff)/(4*ell-2*ff/3)
        check('inward boundary signs',kl*ff/4>0 and ff*(ku-1)/3<0 and ff-a<0)
    h=D(0,1);f=a-h;j=strain-h/(lam+4)
    C3=j*f+j*(-lam*h)/2-f*f/4
    coeff=-strain*lam*(1+lam/2)/(4+lam)
    check('near origin third coefficient',C3.v==0 and C3.d==coeff and coeff<0)
    qinf=1/(3+p);kinf=1-p
    check('far third coefficient',qinf*(1-kinf/2)-F(1,4)==(p-1)/(4*(p+3))<0)
    m=(F(2)+(2+lam/2))/2
    n=1+lam
    check('fractional moment interval',2<m<2+lam/2 and n+3-2*m>0 and 4-2*m<0)

# Global cap arithmetic and independent Cartesian strain differentiation.
for ell in [F(6,5),F(2),F(3),F(10)]:
    strain=ell-1;a=4*strain
    for k in [F(1,10),F(1,2),F(9,10)]:
        for v in [F(1,5),F(4,5)]:
            q=F(1,4)+v*(1/(4-k)-F(1,4))
            A=1-3*q;B=3*q-F(1,2)-k/4
            check('strict angular cap coefficients',0<A<F(1,4) and 0<B<F(1,4) and 3/(4-k)-F(3,4)-k/4==k*(k-1)/(4*(4-k)))
            # Arbitrary positive f<4D; k and q enter the differentiated radial
            # formulas through dot f=-k f, dot J=f-4J.
            ff=a/2;jj=q*ff;fd=-k*ff;jd=ff-4*jj
            for cs,sn in [(F(3,5),F(4,5)),(F(5,13),F(12,13))]:
                derivatives=[]
                for dx,dy in [(F(1),F(0)),(F(0),F(1))]:
                    x=D(cs,dx);y=D(sn,dy);rder=cs*dx+sn*dy
                    f=D(ff,fd*rder);j=D(jj,jd*rder);m=f-4*j
                    r2=x*x+y*y
                    u1=x*(j+m*y*y/r2);u2=-y*(j+m*x*x/r2)
                    derivatives.append((u1.d,u2.d))
                uxx,uyx=derivatives[0];uxy,uyy=derivatives[1]
                off=(uyx+uxy)/2;c2=cs**2-sn**2;s2=2*cs*sn
                exact_square=ff**2*(A*A*c2*c2+B*B*s2*s2)
                check('Cartesian strain norm and cap',uxx+uyy==0 and uxx*uxx+off*off==exact_square<strain**2)
                check('density gradient cap',ff**2*((1-k)**2*sn**2+cs**2)<=ff**2<a*a)

# Direct moment primitive from the revised self-contained Section5.
for ell in [F(6,5),F(2),F(3),F(8)]:
    a=4*(ell-1)
    for ff,jj in [(a/F(3),a/F(10)),(a/F(2),a/F(7))]:
        fd=ff*(ff-a)/(4*ell-2*jj);jd=ff-4*jj
        f=D(ff,fd);j=D(jj,jd);h=a-f
        for m in [F(21,10),F(9,4),F(5,2)]:
            primitive=(ell-j/2)*h
            target=h*((4-2*m)*ell+m*j-f/4)
            check('direct boundary-free moment primitive',primitive.d+(4-2*m)*primitive.v==target.v)
            # Independent angular integrals, divided by pi r^(2-2m)h/a.
            angular=a/4+(2*ell+1)+(1-2*m)*ell+m*jj-ff/4
            check('moment angular coefficient',angular==(4-2*m)*ell+m*jj-ff/4)

now=datetime.now(timezone.utc).isoformat()
out=dict(utc=now,status='PASS',count=len(checks),checks=checks,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256(Path('research/radial_projected_weak_branch/PROOF.md').read_bytes()).hexdigest(),scope='Exact arithmetic identities and strict inequalities at rational test parameters. The standalone proof establishes the general existence, asymptotics and regularity; this checker does not replace it. No full IPM profile is constructed.')
p=Path('research/radial_projected_weak_branch/verification/exact_checks.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['utc','status','count','scope']}))
