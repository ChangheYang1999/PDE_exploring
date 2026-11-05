"""Certified R J^-0.1 of normalized angular Gaussians.

psi_m=sqrt(2/(pi*m!))*a^(-m-1)*r^m*sin(m theta)*exp(-r²/(2a²)).
All special-function evaluations use Arb. The heat quadrature remainder is
proved uniformly in real spatial x by the inverse Fourier L1 bound, avoiding
large intermediate Kummer bounds at high angular order.
"""
import argparse,json,math
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from flint import arb,ctx,fmpq as Q


def aq(x):
    x=Q(x);return arb(x.numerator)/x.denominator


class AngularGaussianHeat:
    def __init__(self,width='1471/10000',m=115,nodes=768,bits=384):
        ctx.prec=bits;assert m>=1;self.m=m;self.bits=bits;self.a=aq(width);self.nodes=nodes
        a=self.a;A=a*a;b=arb(1)/25;small=(arb(9)/25+b*b)**10
        Dmin=A-2*small;assert Dmin>0
        assert 20*(b/(arb(3)/5)).atan()<arb.pi()/2
        C=(arb(2)/(arb.pi()*math.factorial(m))).sqrt()*a**(m+1)
        # Unitary inverse Fourier in dimension2 has factor1/(2pi).
        # Angular |sin(m theta)| integral4, and the Gaussian radial moment
        # is .5*(2/Dmin)^((m+2)/2)*Gamma((m+2)/2).
        l1=C/arb.pi()*(2/Dmin)**(arb(m+2)/2)*(arb(m+2)/2).gamma()
        # Extracting any nonzero Fourier coefficient costs <=4/pi<2.
        M=2*l1*small.exp()/(arb(21)/20).gamma()
        rho=b+(1+b*b).sqrt()
        self.gauss_error=8*M*rho**(-2*nodes)/(1-1/rho)
        T=arb(2)**20;Dtail=A+2*T
        l1tail=C/arb.pi()*(2/Dtail)**(arb(m+2)/2)*(arb(m+2)/2).gamma()
        assert l1tail<1 and (arb(1)/20).gamma()>1
        self.tail_error=2*(-T).exp()
        self.error=(self.gauss_error+self.tail_error).abs_upper()
        self.prepared=[]
        lower_prefactor=C/arb(2).sqrt()*(arb(m)+arb(1)/2).gamma()/math.factorial(m-1)
        upper_prefactor=C/(2*arb(2).sqrt())*(arb(m)+arb(3)/2).gamma()/math.factorial(m+1)
        for j in range(nodes):
            z,weight=arb.legendre_p_root(nodes,j,weight=True);z+=1;t=z**20;D=A+2*t
            ww=weight*(-t).exp()/(arb(21)/20).gamma()
            self.prepared.append((-1/(2*D),
                ww*lower_prefactor*D**(-arb(m)-arb(1)/2),
                ww*upper_prefactor*D**(-arb(m)-arb(3)/2)))
        self.metadata={'status':'CERTIFIED_UNIFORM_ANGULAR_GAUSSIAN_HEAT_VECTOR',
            'width':str(Q(width)),'m':m,'nodes':nodes,'bits':bits,
            'Dmin':Dmin.str(60),'ellipse_semiminor':'1/25',
            'Fourier_L1_complex_heat_bound':l1.str(60),
            'uniform_Gauss_error':self.gauss_error.str(60),
            'uniform_heat_tail_error':self.tail_error.str(20),
            'uniform_radial_coefficient_error':self.error.str(60),
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

    def modes(self,r):
        ctx.prec=self.bits;r=arb(r);assert r>=0;m=self.m
        rm=r**(m-1);rp=rm*r*r;low=arb(0);high=arb(0)
        for factor,aa,bb in self.prepared:
            z=factor*r*r
            def kummer(a,b):
                work=self.bits
                while True:
                    ctx.prec=work;value=z.hypgeom_1f1(a,b)
                    if value.is_finite():return value
                    work*=2
                    assert work<=4096, ("hypergeometric evaluation unresolved",m,r,z)
            low+=aa*rm*kummer(arb(m)+arb(1)/2,m)
            high+=bb*rp*kummer(arb(m)+arb(3)/2,m+2)
            ctx.prec=self.bits
        low+=arb(0,self.error);high+=arb(0,self.error)
        assert low.is_finite() and high.is_finite()
        out={('r2','c',m-1):low,('r2','c',m+1):high,('r1','s',m+1):-high}
        if m>1:out['r1','s',m-1]=low
        return out

    def radial_derivative_bound(self,j):
        ctx.prec=self.bits;m=self.m;a=self.a
        C=(arb(2)/(arb.pi()*math.factorial(m))).sqrt()*a**(m+1)
        return 2*C/arb.pi()*(2/a**2)**(arb(m+j+2)/2)*(arb(m+j+2)/2).gamma()

    def gram(self):
        ctx.prec=self.bits;m=self.m;A=self.a**2
        return A**(m+1)*A.hypgeom_u(m+1,arb(m)+arb(19)/10)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--width',default='1471/10000');ap.add_argument('--m',type=int,default=115);ap.add_argument('--nodes',type=int,default=768);ap.add_argument('--bits',type=int,default=384);args=ap.parse_args()
    h=AngularGaussianHeat(args.width,args.m,args.nodes,args.bits)
    result={**h.metadata,'gram':h.gram().str(80),'derivative11_bound':h.radial_derivative_bound(11).str(50),
        'point_checks':{r:{str(k):v.str(50)for k,v in h.modes(r).items()}for r in ['.5','1','1.5','2','3']},
        'finished_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'Certified uniform real-space smooth Riesz test vector and exact Gram only. Source coordinate and actual matrix inverse integration remain separate.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
