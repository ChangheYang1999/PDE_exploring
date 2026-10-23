"""Full-plane multiprecision inverse from factored source-mode primitives.

Derivation: research/smooth_full_inverse_primitives/PROOF.md.
Independent of the optimizer, double angular inverse and Cartesian inverse.
"""
from fractions import Fraction as F
from math import factorial,comb
import mpmath as mp


def rational(v):
    if isinstance(v,dict):return F(int(v['numerator']),int(v['denominator']))
    return F(v)

def number(v):
    if isinstance(v,F):return mp.mpf(v.numerator)/v.denominator
    if isinstance(v,dict):return number(rational(v))
    return mp.mpf(v)

def chebyshev_polynomial_w(coeff):
    """Closed Chebyshev monomial formula, separately implemented from result83."""
    out=[F(0)]*len(coeff)
    for n,value in enumerate(coeff):
        value=rational(value)
        if n==0:out[0]+=value;continue
        for h in range(n//2+1):
            d=n-2*h
            scale=F(n*factorial(n-h-1),factorial(h)*factorial(d))*F(2)**(d-1)*(-1)**h
            for l in range(d+1):out[l]+=value*scale*comb(d,l)*(-2)**l
    return out


class SmoothMP:
    def __init__(self,inputs,digits=75):
        self.inputs=inputs;self.alpha=rational(inputs['alpha']);self.L=rational(inputs['length']);self.ell=rational(inputs['cl'])
        self.coeff=[[rational(v)for v in row]for row in inputs['chebyshev_coefficients']]
        self.M=len(self.coeff);self.N=max(map(len,self.coeff))-1
        assert self.M>0 and 0<self.alpha<F(1,2)and self.L>0 and self.ell>1
        self.digits=digits;self.working_digits=digits+50+self.M+self.N
        self.C=[chebyshev_polynomial_w(row)for row in self.coeff]
        self.a0=sum(((-1)**n*v for n,v in enumerate(self.coeff[0])),F(0))
        self.p=1-2*self.alpha
        def C(k,l):return self.C[k][l]if 0<=k<self.M and l<len(self.C[k])else F(0)
        self.sources=[]
        for j in range(1,self.M+1):
            terms=[]
            for l in range(self.N+1):
                a=self.alpha*(l+1)
                A=j*C(j,l)-(F(1)if j==1 else F(1,2))*(a+j-1)*C(j-1,l)
                B=-(j+1)*C(j+1,l);E=(a+j+1)*C(j+1,l)/2
                for k,v in [(j,A),(j+1,B),(j+2,E)]:
                    if v:terms.append((k,a,v))
            self.sources.append(terms)
        # An exact source-tail evaluation at zero, independent of the density
        # boundary-moment formula in result83.
        c=F(0)
        for k,a,v in self.sources[0]:
            d=k-1
            c+=v*sum((F((-1)**(d-h)*comb(d,h),1)/(a+k-h-1)for h in range(d+1)),F(0))/4
        self.c=c;self.delta=self.ell+c-1

    def density(self,x,y):
        x=number(x);y=number(y);L=number(self.L);alpha=number(self.alpha)
        r2=x*x+y*y;den=L*L+r2;w=(1+r2/(L*L))**(-alpha);t=1-2*w
        zz=(x+mp.j*y)**2/den;power=mp.mpc(1);total=mp.mpf(0)
        for co in self.coeff:
            b1=b2=mp.mpf(0)
            for ck in co[:0:-1]:b1,b2=number(ck)+2*t*b1-b2,b1
            pk=number(co[0])+t*b1-b2
            total+=mp.re(power)*pk;power*=zz
        return y*w*total

    def source_modes(self,r):
        z=(number(r)/number(self.L))**2
        return [mp.fsum(number(c)*z**k*(1+z)**(-number(a)-k)for k,a,c in terms)for terms in self.sources]

    def modal_integrals(self,r):
        """Return scaled inner/exterior source integrals at current mp precision."""
        z=(number(r)/number(self.L))**2
        if not z>0:raise ValueError('Positive radius required')
        log1=mp.log1p(z);exps={};antiderivatives={};primitives={}
        def exponential(e):
            if e not in exps:exps[e]=mp.exp(number(e)*log1)
            return exps[e]
        def primitive(e):
            if e not in antiderivatives:
                antiderivatives[e]=mp.expm1(number(e)*log1)/number(e)if e else log1
            return antiderivatives[e]
        def pq(j,k,a):
            key=(j,k,a)
            if key in primitives:return primitives[key]
            N=j+k;b=a+k
            if z<mp.mpf('.25'):
                P=z**k*mp.hyp2f1(number(b),N+1,N+2,-z)/(2*(N+1))
            else:
                P=mp.fsum((-1)**(N-h)*comb(N,h)*primitive(F(h+1)-b)for h in range(N+1))/(2*z**(j+1))
            d=k-j
            Q=z**(j-1)*mp.fsum((-1)**(d-h)*comb(d,h)*exponential(F(h+1)-b)/number(b-h-1)for h in range(d+1))/2
            primitives[key]=(P,Q);return P,Q
        out=[]
        for j,terms in enumerate(self.sources,1):
            ps=[];qs=[]
            for k,a,c in terms:
                p,q=pq(j,k,a);cc=number(c);ps.append(cc*p);qs.append(cc*q)
            out.append((mp.fsum(ps),mp.fsum(qs)))
        return out

    def stream_velocity(self,x,y):
        x=number(x);y=number(y);r=mp.hypot(x,y)
        if not r:return mp.mpf(0),mp.mpf(0),mp.mpf(0)
        theta=mp.atan2(y,x);rows=self.modal_integrals(r)
        stream=[];urs=[];uts=[]
        for j,(P,Q)in enumerate(rows,1):
            sn=mp.sin(2*j*theta);cs=mp.cos(2*j*theta)
            stream.append((P+Q)*sn/(4*j));urs.append(-(P+Q)*cs/2);uts.append((-P+Q)*sn/2)
        ur=mp.fsum(urs)*r;ut=mp.fsum(uts)*r
        ux=(ur*x-ut*y)/r;uy=(ur*y+ut*x)/r;psi=mp.fsum(stream)*r*r
        if not x:ux=mp.mpf(0);psi=mp.mpf(0)
        if not y:uy=mp.mpf(0);psi=mp.mpf(0)
        return psi,ux,uy

    def field_working_digits(self,x,y):
        # Guard cancellation of the affine center or leading far transport.
        # It is a conditioning allowance, not an interval error certificate.
        with mp.workdps(40):
            radius=mp.hypot(number(x),number(y))/number(self.L)
            if not radius:return self.working_digits
            lr=mp.log10(radius)
            extra=mp.ceil(max(mp.mpf(0),-2*lr,2*number(self.alpha)*lr))
        return self.working_digits+int(extra)

    def fields(self,x,y):
        working_digits=self.field_working_digits(x,y)
        with mp.workdps(working_digits):
            x=number(x);y=number(y);rho=self.density(x,y)
            radius=mp.hypot(x,y)
            if radius:
                # Differentiate in dimensionless Cartesian coordinates. An
                # absolute mp.diff step at x~1e250 may be lost even though the
                # desired derivative is well resolved in relative coordinates.
                gx=mp.diff(lambda q:self.density(radius*q,y)/radius,x/radius)
                gy=mp.diff(lambda q:self.density(x,radius*q)/radius,y/radius)
            else:
                gx=mp.mpf(0);gy=number(self.a0)
            psi,ux,uy=self.stream_velocity(x,y);ell=number(self.ell)
            tx=(ell*x+ux)*gx;ty=(ell*y+uy)*gy;R=tx+ty-rho
            nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*gx+y*gy)+abs(ux*gx+uy*gy)
            raw=dict(x=x,y=y,radius=mp.hypot(x,y),rho=rho,psi=psi,U1=ux,U2=uy,rho_x=gx,rho_y=gy,R=R,abs_R=abs(R),Nf=nf,Nv=nv,R_Nf=abs(R)/nf if nf else None,R_Nv=abs(R)/nv if nv else None)
            out={k:mp.nstr(v,self.digits)if v is not None else None for k,v in raw.items()}
            out['working_digits']=working_digits
            return out
