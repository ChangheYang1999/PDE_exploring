"""Independent Cartesian Taylor jets for exact canonical IPM potentials."""
from pathlib import Path
from math import comb, factorial
from fractions import Fraction
from datetime import datetime, timezone
import json, sys, hashlib, time
from flint import arb, acb, fmpq, ctx
ROOT=Path(__file__).resolve().parents[3]
sys.set_int_max_str_digits(0)

def q(v):
    v=Fraction(str(v)); return fmpq(v.numerator,v.denominator)
def ar(v): return arb(v.numerator)/arb(v.denominator)
def binom(v,n):
    out=fmpq(1)
    for k in range(n): out=out*(v-k)/(k+1)
    return out

def multiply(A,B,order):
    out={}
    for (a,b),x in A.items():
        for (c,d),y in B.items():
            key=a+c,b+d
            if sum(key)<=order:out[key]=out.get(key,arb(0))+x*y
    return out

class CartesianJet:
    def __init__(self,path,x,y,order=4):
        self.raw=json.loads(Path(path).read_text()); self.c=q(self.raw['cl'])
        self.x,self.y=ar(q(x)),ar(q(y)); self.s=self.x*self.x+self.y*self.y
        assert self.s>0
        self.order=order; R=1+self.s; z=acb(self.x,self.y)
        maxm=max(m for j,m,k in self.raw['order']); zp=[acb(1)]
        for i in range(2*maxm):zp.append(zp[-1]*z)
        S={(1,0):2*self.x,(0,1):2*self.y,(2,0):arb(1),(0,2):arb(1)}
        Sp=[{(0,0):arb(1)}]
        for n in range(order):Sp.append(multiply(Sp[-1],S,order))
        H={};HS={}
        for m in set(m for j,m,k in self.raw['order']):
            jet={}
            for a in range(order+1):
                for b in range(order+1-a):
                    d=a+b
                    if d<=2*m:jet[a,b]=comb(2*m,d)*comb(d,a)*(zp[2*m-d]*acb(0,1)**b).real
            H[m]=jet
            for n in range(order+1):HS[m,n]=multiply(jet,Sp[n],order)
        g=1/self.c; delta=1-g
        self.values={(a,b):arb(0) for a in range(order+1) for b in range(order+1-a)}
        radial={}
        for (j,m,k),coefficient in zip(self.raw['order'],self.raw['coefficients']):
            A=q(coefficient)
            if not A:continue
            d=k-m; alpha=(3+g-j*delta)/2-k
            assert d>=0
            key=j,m,k
            if key not in radial:
                base=self.s**d*R**ar(alpha)
                radial[key]=[base*sum((ar(binom(fmpq(d),i)*binom(alpha,n-i))*self.s**(-i)*R**(-(n-i)) for i in range(n+1)),arb(0)) for n in range(order+1)]
            for n,C in enumerate(radial[key]):
                v=ar(A)*C
                for key2,w in HS[m,n].items():self.values[key2]+=v*w
    def chi(self,a,b):return self.values[a,b]*factorial(a)*factorial(b)
    def fields(self):
        rho=-self.chi(2,1)-self.chi(0,3)
        u1=-self.chi(1,2);u2=self.chi(2,1)
        rx=-self.chi(3,1)-self.chi(1,3);ry=-self.chi(2,2)-self.chi(0,4)
        vx=ar(self.c)*self.x+u1;vy=ar(self.c)*self.y+u2
        return {'rho':rho,'u1':u1,'u2':u2,'rho_x':rx,'rho_y':ry,
                'residual':vx*rx+vy*ry-rho,'velocity_norm':(vx*vx+vy*vy).sqrt(),
                'gradient_norm':(rx*rx+ry*ry).sqrt()}

def run():
    ctx.prec=1024;start=time.monotonic()
    sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
    from radial import Radial
    prior=ROOT/'research/point_witness/data/T4_uniform_gap_witnesses.json'
    old=json.loads(prior.read_text()); rows=[]; models={}
    selected={'C1-A2-d2':(0,1),'C1-A2-Mpen2':(0,2),'C1-A2-b6':(0,1)}
    for entry in old['results']:
        name=entry['candidate']
        if tuple(entry['point'])!=selected.get(name):continue
        slug=name.removeprefix('C1-A2-');path=ROOT/f'research/refit_audit/data/{slug}_canonical.json'
        x,y=entry['point'];jet=CartesianJet(path,x,y);fields=jet.fields()
        model=models.setdefault(slug,Radial(path)); other=model.evaluate(x,y)
        checks={key:bool(value.overlaps(other[key])) for key,value in fields.items() if key in other}
        assert checks and all(checks.values()),checks
        F=abs(fields['residual']);V=fields['velocity_norm'];D=fields['gradient_norm']
        upper=V/240+ar(fmpq(3,100000))*(1+D)+ar(fmpq(1,8000000));gap=F-upper
        assert gap>0 and gap.overlaps(arb(entry['gap']))
        row={'candidate':name,'point':[x,y],'canonical_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
             'fields':{k:v.str(80) for k,v in fields.items()},'radial_fourier_overlap':checks,
             'necessary_upper':upper.str(80),'gap':gap.str(80),'T4_gap_overlap':True,'strictly_positive':True}
        rows.append(row);print(name,'gap',gap.str(60),'seconds',time.monotonic()-start,flush=True)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
         'method':'Independent Cartesian Taylor jets; no radial derivative recurrence used in the primary evaluator.',
         'T4_source_sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),'rows':rows,'elapsed_seconds':time.monotonic()-start}
    (ROOT/'research/point_witness/verification/cartesian_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
