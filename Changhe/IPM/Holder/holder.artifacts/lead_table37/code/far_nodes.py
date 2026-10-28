"""Exterior-circle transport bound (Theorem 3.5) at a list of exponents with ONE plan per (radial bin, phase),
selected by its float cost at a fixed reference exponent and then evaluated exactly at every listed exponent.
Copy of the verifier's certify_far_circles.py; changes: --ref (plan-selection exponent), plan computed once per
(bin, phase), inline a3 (same series as check_explicit_bounds.py). Any exact plan with the checked marginals is
admissible at every exponent, so each output value is an upper bound for the exterior functional; with the plan
fixed, every term is a positive constant times a fixed distance to the power alpha times a positive moment in u,
so the bound is a log-convex function of alpha (needed for the chord interpolation).
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from flint import arb,acb,ctx,fmpq
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from circle_transport_plan import best_plan,check_plan
from refl_nodes import a3_of
import argparse,json,hashlib,time
ctx.prec=160
PI=arb.pi()
def upper_decimal(x,places=10):
    k=int((arb(x.upper())*10**places).ceil().unique_fmpz())
    return f'{k//10**places}.{k%10**places:0{places}d}'
def cell_measures(values,c,s,M1,M2,width,unit):
    masses=[];tv=arb(0)
    spread=arb(0,(M1*width/2).upper());error=arb(0,(M2*width**3/24).upper())
    for value in values:
        mid=value.real*c-value.imag*s
        domain=mid+spread
        if domain>0:sign=1
        elif domain<0:sign=-1
        else:sign=0
        if sign:
            mass=sign*(mid*width+error)
            lower=arb(mass.lower())
            count=max(0,int((lower*unit).floor().unique_fmpz()))
            tv+=arb(mass.upper())
            masses.append(sign*count)
        else:
            masses.append(0);tv+=width*arb(abs(domain).upper())
    assert tv>=arb(sum(abs(x) for x in masses))/unit
    return masses+[-x for x in masses],tv
def main():
    p=argparse.ArgumentParser();p.add_argument('--angles',type=int,default=512);p.add_argument('--radial',type=int,default=128)
    p.add_argument('--phases',type=int,default=16);p.add_argument('--umin',default='1/4');p.add_argument('--alphas',required=True)
    p.add_argument('--ref',required=True);p.add_argument('--out',required=True);p.add_argument('--tries',type=int,default=9)
    args=p.parse_args();n=args.angles;nr=args.radial;m=args.phases
    assert n>=12 and n%2==0 and nr>0 and m>0 and args.tries>=2
    fv=Fraction(args.umin);v=arb(fmpq(fv.numerator,fv.denominator));assert v>0 and v<1
    alpha_strings=args.alphas.split(',');fa=[Fraction(t) for t in alpha_strings];aa=[arb(fmpq(f.numerator,f.denominator)) for f in fa]
    assert all(0<f<1 for f in fa);fr=Fraction(args.ref);ar=arb(fmpq(fr.numerator,fr.denominator))
    unit=2**44;width=2*PI/n;start=time.monotonic()
    points=[]
    for j in range(n//2):
        th=2*PI*(arb(j)+arb(1)/2)/n
        points.append(acb(th.cos(),th.sin()))
    phases=[((PI*k/(2*m)).cos(),(PI*k/(2*m)).sin()) for k in range(m+1)]
    costs=[[(2*(PI*min(j+1,n//2)/n).sin())**a for j in range(n//2+1)] for a in aa]
    refcost=[float(((2*(PI*min(j+1,n//2)/n).sin())**ar).mid()) for j in range(n//2+1)]
    totals=[[arb(0) for _ in phases] for _ in aa]
    counts={'adjacent':0,'antipodal':0,'zero':0}
    for b in range(nr):
        ul=v+(1-v)*b/nr;uh=v+(1-v)*(b+1)/nr
        q=(ul*ul/4).union(uh*uh/4);Q=arb(q.upper())
        M1=3*(1+Q)/(PI*(1-Q)**3);M2=9*(1+4*Q+Q*Q)/(PI*(1-Q)**4)
        values=[z**(-3)/(PI*(1-q*z**(-2))**2) for z in points]
        weights=[(uh**(1-a)-ul**(1-a))/(1-a) for a in aa]
        for k,(c,s) in enumerate(phases):
            masses,tv=cell_measures(values,c,s,M1,M2,width,unit)
            mh=arb(sum(abs(z) for z in masses[:n//2]))/unit
            remainder=tv-mh
            plan,info=best_plan(masses,refcost,tries=args.tries);counts[info['kind']]+=1
            check_plan(masses,plan)
            bydistance={}
            for (i,j),mass in plan.items():
                d=min(abs(i-j),n-abs(i-j));bydistance[d]=bydistance.get(d,0)+mass
            for l,a in enumerate(aa):
                value=sum((arb(mass)*costs[l][d] for d,mass in bydistance.items()),arb(0))/unit
                residual=arb(2)**a*remainder
                totals[l][k]+=(value+residual)*weights[l]
        if b%8==0:print(b,nr,round(time.monotonic()-start,2),flush=True)
    rows=[];N=24
    for text,a,values in zip(alpha_strings,aa,totals):
        a3=a3_of(a)
        tail=2*a3*v**(1-a)/(1-a)
        for k in range(1,N):
            h=2*k+3;ak=(2*h*(PI/(2*h)).cos()/(h*h-1))**a/PI
            tail+=2*(k+1)*arb(4)**(-k)*ak*v**(2*k+1-a)/(2*k+1-a)
        err=(1+arb(1)/N)/PI*arb(4)**(-N)/(1-arb(1)/4)*v**(2*N+1-a)
        tail+=arb(0).union(err)
        final=[z+tail for z in values]
        rows.append(dict(alpha=text,far_phase_intervals=[z.str(36,more=True) for z in final],
                         safe_far_phase_upper=[upper_decimal(z) for z in final],tail_interval=tail.str(36,more=True)))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,angles=n,radial_cells=nr,
             phase_intervals=m,umin=args.umin,integer_unit=unit,plan_trials=args.tries,plan_reference_alpha=args.ref,plan_counts=counts,rows=rows,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,
             status='Upper bounds for the exterior functional at each stated phase, one fixed plan per (bin, phase) for all listed exponents.')
    Path(args.out).write_text(json.dumps(out,indent=2)+'\n')
    for row in rows:print(row['alpha'],max(float(x) for x in row['safe_far_phase_upper']),flush=True)
if __name__=='__main__':main()
