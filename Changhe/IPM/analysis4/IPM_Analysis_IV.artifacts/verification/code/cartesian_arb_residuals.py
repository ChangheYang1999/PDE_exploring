"""Independent Cartesian Arb enclosure of finite far-field residuals.

All nonlinear products use Cartesian differentiation. No numerics-lane module
is imported. Exact rational radial exponents are kept separate from balls.
Known S1 symmetry and finite support are projected only after interval checks.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse
import json
from flint import arb, acb, fmpq, ctx
import cartesian_verify as exact


def rb(x):
    if isinstance(x,arb): return x
    x=Fraction(x)
    return arb(fmpq(x.numerator,x.denominator))


def addto(d,k,v):
    d[k]=d.get(k,acb(0))+v


@dataclass
class Field:
    q: Fraction
    modes: dict

    def __post_init__(self):
        self.q=Fraction(self.q)
        self.modes={k:acb(v) for k,v in self.modes.items() if not acb(v).is_zero()}

    def scale(self,x):
        return Field(self.q,{k:v*rb(x) for k,v in self.modes.items()})

    def __add__(self,o):
        assert self.q==o.q
        d=dict(self.modes)
        for k,v in o.modes.items(): addto(d,k,v)
        return Field(self.q,d)

    def __sub__(self,o): return self+o.scale(-1)

    def __mul__(self,o):
        d={}
        for k,v in self.modes.items():
            for l,w in o.modes.items(): addto(d,k+l,v*w)
        return Field(self.q+o.q,d)

    def dx(self):
        d={}
        for k,v in self.modes.items():
            addto(d,k+1,v*rb((self.q-k)/2))
            addto(d,k-1,v*rb((self.q+k)/2))
        return Field(self.q-1,d)

    def dy(self):
        d={}
        for k,v in self.modes.items():
            addto(d,k+1,acb(0,1)*v*rb((k-self.q)/2))
            addto(d,k-1,acb(0,1)*v*rb((self.q+k)/2))
        return Field(self.q-1,d)

    def lap(self): return self.dx().dx()+self.dy().dy()
    def zero_enclosure(self): return all(v.contains(0) for v in self.modes.values())

    def sine(self,maxfreq,parity):
        out={}
        for k,v in self.modes.items():
            if k<=0: continue
            assert v.real.contains(0)
            assert (v+self.modes.get(-k,acb(0))).contains(0)
            if k>maxfreq or k%2!=parity:
                assert v.contains(0)
            else:
                out[k]=-2*v.imag
        assert self.modes.get(0,acb(0)).contains(0)
        return out


def sinefield(q,a):
    d={}
    for k,v in a.items():
        d[k]=acb(0,-v/2); d[-k]=acb(0,v/2)
    return Field(q,d)


def cosfield(q,a):
    d={}
    for k,v in a.items():
        if k==0: d[0]=acb(v)
        else: d[k]=d[-k]=acb(v/2)
    return Field(q,d)


def poisson(rho,B,n):
    q=rho.q+1
    h=rho.dx()
    d={}
    for k,v in h.modes.items():
        den=k*k-q*q
        if den==0:
            raise ArithmeticError('exact stream resonance')
        d[k]=v/rb(den)
    psi=Field(q,d)
    psi=sinefield(q,psi.sine(B*n,0))
    assert (psi.lap().scale(-1)-h).zero_enclosure()
    return psi


def potential(rho,B,n):
    a=rho.sine(B*n-1,1)
    remaining=dict(a)
    out={}
    for l in range(B*n-2,-1,-2):
        basis=exact.cos_field(exact.Q(str(rho.q+3)),{l:exact.Q(1)})
        image=exact.from_potential(basis)[0].sine()
        diag=image.get(l+1,exact.Q(0))
        assert diag!=0
        value=remaining.get(l+1,arb(0))/rb(Fraction(str(diag)))
        out[l]=value
        for k,v in image.items():
            remaining[k]=remaining.get(k,arb(0))-value*rb(Fraction(str(v)))
    assert all(v.contains(0) for v in remaining.values())
    chi=cosfield(rho.q+3,out)
    rr=chi.lap().dy().scale(-1)
    pp=chi.dx().dy()
    assert (rr-rho).zero_enclosure()
    return chi,pp


def encode_arb(x):
    m,e=x.mid().man_exp()
    r,re=x.rad().man_exp()
    return [str(m),int(e),str(r),int(re)]


def encode_field(f):
    return {'q':str(f.q),'modes':{str(k):[encode_arb(v.real),encode_arb(v.imag)] for k,v in sorted(f.modes.items())}}


def real_projection(modes):
    assert modes.get(0,acb(0)).imag.contains(0)
    for k,v in modes.items():
        if k>0: assert (v.conjugate()-modes.get(-k,acb(0))).contains(0)
    return {k:v for k,v in modes.items() if k>=0}


def certified_sup(modes,grid):
    coeff=real_projection(modes)
    degree=max(coeff,default=0)
    dense=[coeff.get(k,acb(0)) for k in range(degree+1)]
    deriv=sum((2*k*abs(v) for k,v in coeff.items() if k),arb(0))
    lower=arb(0); grid_upper=arb(0)
    for j in range(grid):
        theta=2*arb.pi()*j/grid
        z=acb(theta.cos(),theta.sin())
        val=acb(0)
        for k in range(degree,0,-1): val=(val+dense[k])*z
        value=dense[0].real+2*val.real
        lower=lower.max(value.abs_lower())
        grid_upper=grid_upper.max(value.abs_upper())
    upper=grid_upper+arb.pi()*deriv/grid
    assert lower>=0 and upper>0
    return {'degree':degree,'grid_points':grid,'sup_lower':str(lower),'sup_upper':str(upper),'grid_max_upper':str(grid_upper),'angular_lipschitz_bound':str(deriv),'upper_to_lower':str(upper/lower) if lower>0 else None}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--order',type=int,default=21)
    ap.add_argument('--truncations',default='10,20')
    ap.add_argument('--radii',default='1,2,4,8')
    ap.add_argument('--bits',type=int,default=512)
    ap.add_argument('--grid',type=int,default=2048)
    ap.add_argument('--output',default='research/16_certified_residuals/verification/reference_sin_residuals.json')
    args=ap.parse_args()
    ctx.prec=args.bits
    profile_path=Path('research/02_candidate007/data/leading_exact.json')
    data=json.loads(profile_path.read_text())
    c=Fraction(data['c']); delta=Fraction(data['delta'])
    B=2; rho={};psi={};chi={};vel={};grad={};checks=[]
    for n in range(1,args.order+1):
        p=1-n*delta
        forcing=Field(p,{})
        if n==1: cur=sinefield(p,{1:arb(1)})
        else:
            for i in range(1,n):
                j=n-i
                forcing=forcing+vel[i][0]*grad[j][0]+vel[i][1]*grad[j][1]
            cur=forcing.scale(1/((n-1)*(c-1)))
            cur=sinefield(p,cur.sine(B*n-1,1))
        rho[n]=cur;psi[n]=poisson(cur,B,n)
        chi[n],pp=potential(cur,B,n)
        assert (pp-psi[n]).zero_enclosure()
        ux=chi[n].dx().dy().dy().scale(-1)
        uy=chi[n].dx().dx().dy()
        assert (ux-psi[n].dy().scale(-1)).zero_enclosure()
        assert (uy-psi[n].dx()).zero_enclosure()
        vel[n]=(ux,uy);grad[n]=(cur.dx(),cur.dy())
        assert (cur.scale(c*p-1)+forcing).zero_enclosure()
        checks.append({'n':n,'cartesian_potential_poisson_stationary_enclosures':True})
        print('Cartesian Arb order',n,'verified',flush=True)
    target=Path(args.output)
    coeff_target=target.with_name(target.stem+'_coefficients.json')
    coeff_target.write_text(json.dumps({'encoding':'[midpoint integer, midpoint power of 2, radius integer, radius power of 2]','bits':args.bits,'c':str(c),'delta':str(delta),'f1':'sin(theta)','rho':{str(n):encode_field(f) for n,f in rho.items()},'psi':{str(n):encode_field(f) for n,f in psi.items()},'chi':{str(n):encode_field(f) for n,f in chi.items()}},indent=2)+'\n')
    rows=[]
    for N in [int(s) for s in args.truncations.split(',')]:
        assert N+1<=args.order
        residual={}
        for i in range(1,N+1):
            for j in range(max(1,N+1-i),N+1):
                n=i+j
                term=vel[i][0]*grad[j][0]+vel[i][1]*grad[j][1]
                residual[n]=residual.get(n,Field(1-n*delta,{}))+term
        assert (residual[N+1]-rho[N+1].scale(N*(c-1))).zero_enclosure()
        for radius in [Fraction(s) for s in args.radii.split(',')]:
            z=(-rb(delta)*rb(radius).log()).exp()
            totals={name:{} for name in ['residual','angular_derivative','weighted_dx','weighted_dy','next_density_term']}
            for n,f in residual.items():
                weight=z**(n-1)
                variants={'residual':f,'angular_derivative':Field(f.q,{k:v*acb(0,k) for k,v in f.modes.items()}),'weighted_dx':f.dx(),'weighted_dy':f.dy()}
                for name,variant in variants.items():
                    for k,v in variant.modes.items(): addto(totals[name],k,weight*v)
            totals['next_density_term']={k:(z**N)*v for k,v in rho[N+1].modes.items()}
            result={name:certified_sup(v,args.grid) for name,v in totals.items()}
            rows.append({'N':N,'R':str(radius),'bounds':result})
            print('Certified residual',N,str(radius),result['residual']['sup_lower'][:25],result['residual']['sup_upper'][:25],flush=True)
            partial={'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'scope':'Finite truncations at the exact stored rational parameter; not an infinite convergence proof.','code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'exact_cartesian_engine_sha256':sha256(Path('code/cartesian_verify.py').read_bytes()).hexdigest(),'bits':args.bits,'c':str(c),'delta':str(delta),'f1':'sin(theta)','coefficient_artifact':coeff_target.as_posix(),'coefficient_artifact_sha256':sha256(coeff_target.read_bytes()).hexdigest(),'checks':checks,'rows':rows}
            target.write_text(json.dumps(partial,indent=2)+'\n')
    print('All finite residual bounds written.',flush=True)

if __name__=='__main__': main()
