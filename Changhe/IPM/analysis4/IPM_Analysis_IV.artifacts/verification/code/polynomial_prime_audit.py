"""Exact Cartesian recurrence over a polynomial amplitude ring."""
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from hashlib import sha256
import json
import time
from flint import fmpq as Q, fmpq_poly as Poly

@dataclass
class Field:
    q:object
    a:dict
    def __post_init__(self):
        self.q=Q(self.q)
        self.a={k:v for k,v in self.a.items() if v}
    def __add__(self,b):
        assert self.q==b.q
        return Field(self.q,{k:self.a.get(k,Poly([]))+b.a.get(k,Poly([])) for k in self.a.keys()|b.a.keys()})
    def scale(self,v):return Field(self.q,{k:p*v for k,p in self.a.items()})
    def __sub__(self,b):return self+b.scale(-1)
    def __mul__(self,b):
        d={}
        for i,v in self.a.items():
            for j,w in b.a.items():d[i+j]=d.get(i+j,Poly([]))+v*w
        return Field(self.q+b.q,d)
    def derivative(self,y=False):
        d={}
        for k,v in self.a.items():
            d[k-1]=d.get(k-1,Poly([]))+v*((self.q+k)/2)
            d[k+1]=d.get(k+1,Poly([]))+v*((self.q-k)/2)*(-1 if y else 1)
        return Field(self.q-1,d)
    def X(self):return self.derivative()
    def Y(self):return self.derivative(True)


def run(p,a,family):
    delta=Q(a,p); c=1/(1-delta)
    u=Poly([0,1])
    initial={1:Poly([1]),3:u,5:u*u} if family=='fixed_first' else {1:u,3:Poly([1])}
    inp={}
    for k,v in initial.items():inp[k]=v/2;inp[-k]=-v/2
    F={1:Field(1-delta,inp)};G={};XF={};YF={};XG={};YG={}
    for n in range(1,p+1):
        exponent=1-n*delta
        if n>1:
            non=Field(exponent,{})
            for i in range(1,n):non=non+XG[i]*YF[n-i]-YG[i]*XF[n-i]
            F[n]=non.scale(1/((n-1)*(c-1)))
        if n==p:break
        XF[n],YF[n]=F[n].X(),F[n].Y()
        P=exponent+1
        dd={}
        for k,v in XF[n].a.items():
            divisor=k*k-P*P
            assert divisor
            dd[k]=v/divisor
        G[n]=Field(P,dd)
        XG[n],YG[n]=G[n].X(),G[n].Y()
        assert not (XG[n].X().scale(-1)+YG[n].Y()-XF[n]).a
    kappa=F[p].a.get(a-3,Poly([]))*2
    residues=[]
    for v in kappa.coeffs():
        assert int(v.q)%p
        residues.append(int(v.p)*pow(int(v.q),-1,p)%p)
    sign=(-1)**((a-4)//2)%p
    expected=Poly([sign]) if family=='fixed_first' else Poly([0]*p+[sign])
    assert Poly(residues)==expected,(p,a,family,residues)
    return dict(prime=p,a=a,delta=str(delta),family=family,
                kappa_coefficients=[str(v) for v in kappa.coeffs()],
                residues_mod_p=residues,expected_residues=[str(v) for v in expected.coeffs()],
                polynomial_congruence=True,exact_cartesian_poisson=True)


def main():
    start=time.monotonic(); rows=[]
    for p,a in [(5,4),(7,4),(7,6),(11,4),(11,8),(13,6),(13,12)]:
        for family in ['fixed_first','variable_first']:
            rows.append(run(p,a,family))
            print(json.dumps(dict(p=p,a=a,family=family,pass_congruence=True,elapsed_s=time.monotonic()-start)),flush=True)
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),method='Exact Cartesian derivatives over Q[u]',
             families={'fixed_first':'sin(theta)+u sin(3theta)+u^2 sin(5theta)','variable_first':'u sin(theta)+sin(3theta)'},
             results=rows,actual_elapsed_s=time.monotonic()-start)
    Path('research/42_real_profile_prime_obstruction/verification/polynomial_checks.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
