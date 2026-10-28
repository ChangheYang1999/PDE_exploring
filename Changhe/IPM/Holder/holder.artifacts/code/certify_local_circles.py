"""Arb enclosure of paired local-circle transports, with exact integer flows.
Only a phase-grid component is certified here. See paired_local_circles/PROOF.md.
"""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,acb,ctx
from local_circle_exact_plan import transport
from certify_far_circles import upper_decimal
import argparse,json,hashlib,time,math
ctx.prec=160
PI=arb.pi();ROOT=Path(__file__).resolve().parents[1];UNIT=2**44

def up(x):return arb(x.upper())
def nn(x):return arb.max(arb(0),x)

def angular_data(a,b,phase,n):
    r=a.union(b);width=2*PI/n
    angles=[phase/2+PI/4+width*j for j in range(n+1)]
    arcs=[acb(t.cos(),t.sin()) for t in [angles[j].union(angles[j+1]) for j in range(n)]]
    midpoints=[acb((t+width/2).cos(),(t+width/2).sin()) for t in angles[:-1]]
    e=acb(phase.cos(),phase.sin());mass=[];tv=arb(0)
    M2=b**3*(1+2*b)/(PI*(1-b)**4)
    error=arb(0,up(M2*width**3/24))
    for j,(arc,mid) in enumerate(zip(arcs,midpoints)):
        interval=angles[j].union(angles[j+1])
        domain=((2*interval-phase).cos()-(r*r*e/(1+r*arc)**2).real)/(2*PI)
        own=((2*angles[j+1]-phase).sin()-(2*angles[j]-phase).sin())/(4*PI)
        cross=(r*r*e/(1+r*mid)**2).real/(2*PI)
        integral=own-cross*width+error
        if domain>0:sign=1
        elif domain<0:sign=-1
        else:sign=0
        if sign:
            signed=sign*integral
            count=max(0,int((arb(signed.lower())*UNIT).floor().unique_fmpz()))
            mass.append(sign*count);tv+=up(signed)
        else:
            mass.append(0);tv+=width*up(abs(domain))
    assert tv>=arb(sum(abs(m) for m in mass))/UNIT
    return mass+[-m for m in mass],tv,arcs,midpoints

def edge_cost(i,j,a,b,alpha,n,arcs):
    side_i,side_j=i//n,j//n;ii,jj=i%n,j%n
    if side_i==side_j:
        k=min(abs(ii-jj),n-abs(ii-jj))
        chord=2*(PI*min(k+1,n//2)/n).sin()
        return chord**alpha*(b**alpha-a**alpha)/alpha
    # The squared distance is convex as a function of r for fixed angles;
    # its maximum is attained at a radial endpoint. Complex interval arcs
    # then enclose all angular pairs at each endpoint.
    t=arcs[ii]+arcs[jj]
    distance=arb.max(up(abs(1+a*t)),up(abs(1+b*t)))
    return distance**alpha*(b/a).log()

def main():
    p=argparse.ArgumentParser();p.add_argument('--angles',type=int,default=128)
    p.add_argument('--radial',type=int,default=64);p.add_argument('--phases',type=int,default=16)
    p.add_argument('--alpha',default='1/2');p.add_argument('--delta',default='1/64')
    p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True)
    p.add_argument('--phase-start',type=int,default=0);p.add_argument('--phase-stop',type=int)
    p.add_argument('--out',required=True);args=p.parse_args()
    n=args.angles;nr=args.radial;m=args.phases;alpha=arb(args.alpha);delta=arb(args.delta);R=arb(1)/2
    end=m+1 if args.phase_stop is None else args.phase_stop
    assert n>=16 and n%8==0 and nr>0 and 0<alpha<1 and 0<delta<R
    assert 0<=args.start<args.stop<=nr and 0<=args.phase_start<end<=m+1
    phases=range(args.phase_start,end);totals={k:arb(0) for k in phases};residuals={k:arb(0) for k in phases}
    counts={};repair_total=0;started=time.monotonic()
    for row in range(args.start,args.stop):
        a=delta+(R-delta)*row/nr;b=delta+(R-delta)*(row+1)/nr
        for k in phases:
            phase=PI*k/(2*m);masses,tv,arcs,mids=angular_data(a,b,phase,n)
            rm=float(((a+b)/2).mid());points=[.5+rm*complex(float(z.real.mid()),float(z.imag.mid())) for z in mids]
            points=points+[-z for z in points]
            plan,info=transport(masses,points,float(alpha.mid()));counts[info['status']]=counts.get(info['status'],0)+1;repair_total+=info['repairs']
            cost=sum((arb(v)/UNIT*edge_cost(i,j,a,b,alpha,n,arcs) for (i,j),v in plan.items()),arb(0))
            extracted=arb(sum(abs(v) for v in masses[:n]))/UNIT
            residual=(1+2*b)**alpha*(tv-extracted)*(b/a).log()
            assert residual>=0 and cost>=0
            totals[k]+=cost+residual;residuals[k]+=residual
        if row%4==0:print(row,nr,round(time.monotonic()-started,2),flush=True)
    a2=2**(1+alpha/2)/(PI*(alpha+2))
    small=2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
    paths=[Path(__file__),ROOT/'code/local_circle_exact_plan.py',ROOT/'08_improved_upper_bounds/paired_local_circles/PROOF.md']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=args.alpha,precision_bits=ctx.prec,angles_per_circle=n,radial_cells=nr,phase_intervals=m,delta=args.delta,row_start=args.start,row_stop=args.stop,phase_start=args.phase_start,phase_stop=end,integer_unit=UNIT,
             partial_phase_intervals={str(k):v.str(40,more=True) for k,v in totals.items()},residual_phase_intervals={str(k):v.str(35,more=True) for k,v in residuals.items()},small_disk_upper=small.str(40,more=True),plan_counts=counts,repair_integer_mass=repair_total,elapsed_seconds=time.monotonic()-started,
             source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Partial local-circle upper bound for C. Requires exact coverage merge and other spatial regions.')
    (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
if __name__=='__main__':main()
