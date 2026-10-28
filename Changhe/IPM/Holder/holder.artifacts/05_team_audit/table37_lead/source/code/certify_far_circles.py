"""Rigorous exterior-circle bound using exact integer transport plans.
Proof: 08_improved_upper_bounds/far_circle_transport/PROOF.md.
All plan row/column sums are checked exactly in circle_transport_plan.py.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from flint import arb,acb,ctx
from circle_transport_plan import best_plan
import argparse,json,hashlib,time,math
ctx.prec=160
PI=arb.pi();ROOT=Path(__file__).resolve().parents[1]

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
    p=argparse.ArgumentParser();p.add_argument('--angles',type=int,default=256);p.add_argument('--radial',type=int,default=64)
    p.add_argument('--phases',type=int,default=16);p.add_argument('--umin',default='1/4');p.add_argument('--alphas',default='1/2')
    p.add_argument('--out',default='data/far_circle_certificate_coarse.json');p.add_argument('--tries',type=int,default=9)
    args=p.parse_args();n=args.angles;nr=args.radial;m=args.phases
    assert n>=12 and n%2==0 and nr>0 and m>0 and args.tries>=2
    v=arb(args.umin);assert v>0 and v<1
    alpha_strings=args.alphas.split(',');aa=[arb(a) for a in alpha_strings]
    assert all(a>0 and a<1 for a in aa)
    unit=2**44;width=2*PI/n;start=time.monotonic()
    points=[]
    for j in range(n//2):
        th=2*PI*(arb(j)+arb(1)/2)/n
        points.append(acb(th.cos(),th.sin()))
    phases=[((PI*k/(2*m)).cos(),(PI*k/(2*m)).sin()) for k in range(m+1)]
    costs=[];floats=[]
    for a in aa:
        cc=[(2*(PI*min(j+1,n//2)/n).sin())**a for j in range(n//2+1)]
        costs.append(cc);floats.append([float(z.mid()) for z in cc])
    totals=[[arb(0) for _ in phases] for _ in aa]
    residuals=[[arb(0) for _ in phases] for _ in aa]
    counts={'adjacent':0,'antipodal':0,'zero':0};steps=[]
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
            for l,a in enumerate(aa):
                plan,info=best_plan(masses,floats[l],tries=args.tries);counts[info['kind']]+=1
                bydistance={}
                for (i,j),mass in plan.items():
                    d=min(abs(i-j),n-abs(i-j));bydistance[d]=bydistance.get(d,0)+mass
                value=sum((arb(mass)*costs[l][d] for d,mass in bydistance.items()),arb(0))/unit
                residual=arb(2)**a*remainder
                totals[l][k]+=(value+residual)*weights[l]
                residuals[l][k]+=residual*weights[l]
        if b%8==0:print(b,nr,round(time.monotonic()-start,2),flush=True)
    base=json.loads((ROOT/'data/explicit_bounds_intervals.json').read_text())['rows'];base={Fraction(r['alpha']):r for r in base}
    rows=[];N=24
    for text,a,values,resid in zip(alpha_strings,aa,totals,residuals):
        b=base[Fraction(text)];a3=arb(b['intervals']['a3'])
        tail=2*a3*v**(1-a)/(1-a)
        for k in range(1,N):
            h=2*k+3;ak=(2*h*(PI/(2*h)).cos()/(h*h-1))**a/PI
            tail+=2*(k+1)*arb(4)**(-k)*ak*v**(2*k+1-a)/(2*k+1-a)
        err=(1+arb(1)/N)/PI*arb(4)**(-N)/(1-arb(1)/4)*v**(2*N+1-a)
        tail+=arb(0).union(err)
        final=[z+tail for z in values]
        rows.append(dict(alpha=text,far_phase_intervals=[z.str(36,more=True) for z in final],
                         safe_far_phase_upper=[upper_decimal(z) for z in final],
                         residual_phase_intervals=[z.str(30,more=True) for z in resid],
                         tail_interval=tail.str(36,more=True)))
    paths=[Path(__file__),ROOT/'code/circle_transport_plan.py']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,angles=n,radial_cells=nr,
             phase_intervals=m,umin=args.umin,integer_unit=unit,plan_trials=args.tries,plan_counts=counts,rows=rows,
             source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
             input_hashes={'data/explicit_bounds_intervals.json':hashlib.sha256((ROOT/'data/explicit_bounds_intervals.json').read_bytes()).hexdigest()},
             elapsed_seconds=time.monotonic()-start,status='Upper bounds for the exterior functional at each stated phase; combine with local and regular bounds and a proved phase interpolation.')
    (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n')
    for row in rows:print(row['alpha'],row['safe_far_phase_upper'],flush=True)
if __name__=='__main__':main()
