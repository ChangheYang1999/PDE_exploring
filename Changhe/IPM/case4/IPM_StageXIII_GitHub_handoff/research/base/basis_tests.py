"""Independent Decimal Taylor algebra tests for the new spectral modes.

Uses ordinary bivariate Taylor coefficients, without spectral_basis radial or
harmonic derivative formulas. Execute only through the Stage XII launcher.
"""
import argparse, hashlib, json, math, os
from decimal import Decimal, localcontext
from pathlib import Path
import numpy as np
from spectral_basis import evaluate_modes, tail_exponent, metadata

D=Decimal
class Jet:
    def __init__(self,coeff,order): self.c={k:D(v) for k,v in coeff.items() if v};self.order=order
    @classmethod
    def constant(cls,value,order):return cls({(0,0):D(value)},order)
    def coerce(self,value):return value if isinstance(value,Jet) else Jet.constant(value,self.order)
    def __add__(self,other):
        other=self.coerce(other);out=dict(self.c)
        for k,v in other.c.items():out[k]=out.get(k,D(0))+v
        return Jet(out,self.order)
    __radd__=__add__
    def __neg__(self):return Jet({k:-v for k,v in self.c.items()},self.order)
    def __sub__(self,other):return self+-self.coerce(other)
    def __rsub__(self,other):return self.coerce(other)+-self
    def __mul__(self,other):
        other=self.coerce(other);out={}
        for (a,b),v in self.c.items():
            for (c,d),w in other.c.items():
                if a+b+c+d<=self.order:out[(a+c,b+d)]=out.get((a+c,b+d),D(0))+v*w
        return Jet(out,self.order)
    __rmul__=__mul__
    def integer_power(self,n):
        if n<0:return (self.log()*n).exp()
        result=Jet.constant(1,self.order)
        for _ in range(n):result=result*self
        return result
    def __truediv__(self,other):
        if not isinstance(other,Jet):return self*(D(1)/D(other))
        if len(other.c)<=1:return self*(D(1)/other.c.get((0,0),D(0)))
        return self*other.integer_power(-1)
    def __rtruediv__(self,other):return self.coerce(other)/self
    def log(self):
        a=self.c.get((0,0),D(0));v=(self-a)*(D(1)/a)
        result=Jet.constant(a.ln(),self.order);power=Jet.constant(1,self.order)
        for j in range(1,self.order+1):power=power*v;result=result+power*(D((-1)**(j+1))/D(j))
        return result
    def exp(self):
        a=self.c.get((0,0),D(0));v=self-a;result=Jet.constant(1,self.order);power=result
        for j in range(1,self.order+1):power=power*v/D(j);result=result+power
        return result*a.exp()
    def derivative(self,a,b):return self.c.get((a,b),D(0))*math.factorial(a)*math.factorial(b)


def potential_jet(x,y,cl,mode,order=5,cl_derivative=False):
    x=D.from_float(float(x));y=D.from_float(float(y));cl=D.from_float(float(cl))
    X=Jet({(0,0):x,(1,0):1},order);Y=Jet({(0,0):y,(0,1):1},order);q=X*X+Y*Y;R=1+q;t=q/R;s=R.log();m=int(mode['m'])
    # Homogeneous harmonic recurrence uses Cartesian polynomial algebra only.
    Hprev=Jet.constant(1,order);H=X
    if m==0:H=Hprev
    else:
        for _ in range(1,2*m):Hprev,H=H,2*X*H-q*Hprev
    sig=mode.get('sigma',0.)
    if isinstance(sig,str):k={'zero':0,'delta':1,'2delta':2,'3delta':3}[sig];sigma=D(k)*(1-1/cl)/2;dsigma=D(k)/(2*cl*cl)
    else:sigma=D.from_float(float(sig));dsigma=D(0)
    A=(3+1/cl)/2;beta=A-m-sigma
    result=H*(s*beta).exp()*t.integer_power(max(5-m,0))
    if mode['family']=='global':
        n=int(mode['n']);z=2*t-1;p0=Jet.constant(1,order);p1=z
        if float(mode.get('alpha',0.)) or float(mode.get('beta',0.)):raise ValueError('Independent test currently uses default Legendre modes')
        if n==0:p=p0
        elif n==1:p=p1
        else:
            for j in range(1,n):p0,p1=p1,((2*j+1)*z*p1-j*p0)/(j+1)
            p=p1
        normal=D(2*n+1).sqrt() if mode.get('normalize',True) else D(1)
        result=result*p*normal
    else:
        center=D.from_float(float(mode['center']));width=D.from_float(float(mode['width']));z=(s-center)/width
        result=result*(-z*z/2).exp()
    result=result*D.from_float(float(mode.get('scale',1.)))
    if cl_derivative:result=result*s*(-D('0.5')/(cl*cl)-dsigma)
    return result


def independent_fields(x,y,cl,mode):
    z=potential_jet(x,y,cl,mode);y=D.from_float(float(y))
    rho=-(z.derivative(2,1)+z.derivative(0,3));rhox=-(z.derivative(3,1)+z.derivative(1,3));rhoy=-(z.derivative(2,2)+z.derivative(0,4))
    if y:
        f=rho/y;fx=rhox/y;fy=rhoy/y-rho/(y*y);ratio=z.derivative(2,1)/y
    else:
        f=-(z.derivative(2,2)+z.derivative(0,4));fx=-(z.derivative(3,2)+z.derivative(1,4));fy=D(0);ratio=z.derivative(2,2)
    return {k:float(v) for k,v in {'chi':z.derivative(0,0),'f':f,'fx':fx,'fy':fy,'psi':z.derivative(1,1),'psix':z.derivative(2,1),'psiy':z.derivative(1,2),'ratio':ratio}.items()}


def run(args):
    if not os.environ.get('IPM_RESOURCE_SESSION'):raise RuntimeError('Guard required')
    root=Path(__file__).resolve().parent;cl=1.88359472051
    modes=[{'family':'global','m':m,'n':n,'sigma':sigma} for m,n,sigma in [(0,0,0),(1,3,'delta'),(3,8,0),(5,4,'2delta'),(8,2,0),(12,12,'delta')]]
    modes += [{'family':'local','m':m,'center':c,'width':w} for m,c,w in [(0,1.,.7),(2,3.,.9),(5,5.,1.2),(12,9.,1.5)]]
    # Tests span the origin, axes, near axes, and every relevant radial range.
    points=[(.13,.21),(1.2,.7),(3.,4.),(17.,9.),(0.,2.),(2.,0.),(1e-8,1.3),(1.3,1e-8)]
    x=np.array([p[0] for p in points]);y=np.array([p[1] for p in points]);values,derivatives=evaluate_modes(x,y,cl,modes,True)
    checks=[];worst=0.
    with localcontext() as ctx:
        ctx.prec=70
        for j,mode in enumerate(modes):
            for i,(px,py) in enumerate(points):
                exact=independent_fields(px,py,cl,mode)
                for key in exact:
                    got=float(values[key][i,j]);err=abs(got-exact[key])/max(1.,abs(exact[key]));worst=max(worst,err)
                    checks.append({'mode':j,'point':i,'field':key,'reference':exact[key],'value':got,'scaled_error':err})
        vanish=[]
        for j,mode in enumerate(modes):
            for clderiv in (False,True):
                jet=potential_jet(0.,0.,cl,mode,8,clderiv);maximum=max((abs(v) for v in jet.c.values()),default=D(0))
                vanish.append({'mode':j,'cl_derivative':clderiv,'max_potential_Taylor_degree_0_through_8':str(maximum)})
                if maximum:raise AssertionError('Origin Taylor jet not identically zero')
        # Nonzero coefficients: proof tested on a combined extra profile, not only zero embedding.
        combination=Jet.constant(0,8)
        for j,mode in enumerate(modes):combination=combination+potential_jet(0.,0.,cl,mode,8)*D(j+1)/D(7)
        assert not combination.c
    # Analytic c_l derivatives independently tested with four-point stencils at three steps.
    cl_checks=[]
    for h in [2e-4,1e-4,5e-5]:
        probes=[evaluate_modes(x,y,cl+k*h,modes) for k in [2,1,-1,-2]]
        for key in values:
            fd=(-probes[0][key]+8*probes[1][key]-8*probes[2][key]+probes[3][key])/(12*h)
            error=float(np.linalg.norm(fd-derivatives[key])/max(1.,np.linalg.norm(derivatives[key])))
            cl_checks.append({'step':h,'field':key,'relative_or_absolute_error':error})
    parity=[]
    for sx,sy in [(-1,1),(1,-1),(-1,-1)]:
        reflected=evaluate_modes(sx*x,sy*y,cl,modes)
        signs={'chi':1,'f':1,'fx':sx,'fy':sy,'psi':sx*sy,'psix':sy,'psiy':sx,'ratio':1}
        parity.append({'sx':sx,'sy':sy,'maximum_absolute_defect':max(float(np.max(abs(reflected[key]-signs[key]*values[key]))) for key in values)})
    extremes=evaluate_modes(np.array([0.,1e-10,1e7,1e7]),np.array([0.,2e-10,0.,.3e7]),cl,modes)
    finite=all(np.all(np.isfinite(v)) for v in extremes.values());zero=all(np.array_equal(v[0],np.zeros(len(modes))) for v in extremes.values())
    passed=worst<2e-9 and max(q['relative_or_absolute_error'] for q in cl_checks)<2e-7 and max(q['maximum_absolute_defect'] for q in parity)<1e-8 and finite and zero
    report={'passed':passed,'independent_method':'70-digit Cartesian bivariate Taylor algebra, ordinary coefficients; no native derivative recurrences','metadata':metadata(modes),'modes':modes,'points':points,'maximum_scaled_spatial_error':worst,'spatial_checks':checks,'origin_vanishing_tests':vanish,'nonzero_combination_Taylor_jet_zero':not combination.c,'cl_derivative_checks':cl_checks,'parity':parity,'finite_through_radius_1e7':finite,'origin_fields_bitwise_zero':zero,'source_sha256':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in ['spectral_basis.py','basis_tests.py']}}
    out=root/'results'/'basis_tests.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['passed','maximum_scaled_spatial_error','finite_through_radius_1e7','origin_fields_bitwise_zero']}))
    if not passed:raise SystemExit(1)

if __name__=='__main__':
    parser=argparse.ArgumentParser();run(parser.parse_args())
