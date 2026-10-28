"""Shared exact local-circle plans for several exponents.
The plans depend only on cell masses and distance ordering, not the exponent.
All costs and residuals are still enclosed separately with Arb.
Copy of the verifier's certify_local_circles_multi.py for the uniform-in-alpha comparison. Changes: source hashes of the
local copies, and output paths relative to the working directory. The computation is unchanged.
"""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
from certify_local_circles_greedy import angular_data,UNIT
from local_circle_greedy import transport_greedy
import argparse,json,hashlib,time
ctx.prec=160;PI=arb.pi();ROOT=Path(__file__).resolve().parents[1]
def up(x):return arb(x.upper())
def main():
    p=argparse.ArgumentParser();p.add_argument('--alphas',nargs='+',required=True)
    p.add_argument('--angles',type=int,default=512);p.add_argument('--radial',type=int,default=256)
    p.add_argument('--phases',type=int,default=16);p.add_argument('--delta',default='1/64')
    p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True)
    p.add_argument('--phase-start',type=int,default=0);p.add_argument('--phase-stop',type=int)
    p.add_argument('--out-stem',required=True);args=p.parse_args()
    n=args.angles;nr=args.radial;m=args.phases;alphas=[arb(s) for s in args.alphas]
    delta=arb(args.delta);R=arb(1)/2;end=m+1 if args.phase_stop is None else args.phase_stop
    assert n>=16 and n%8==0 and 0<delta<R and all(0<x<1 for x in alphas)
    assert 0<=args.start<args.stop<=nr and 0<=args.phase_start<end<=m+1
    phases=range(args.phase_start,end)
    chords=[2*(PI*min(k+1,n//2)/n).sin() for k in range(n//2+1)]
    powers=[[chord**alpha for chord in chords] for alpha in alphas]
    totals=[{k:arb(0) for k in phases} for _ in alphas]
    residuals=[{k:arb(0) for k in phases} for _ in alphas]
    count=0;started=time.monotonic()
    for row in range(args.start,args.stop):
        a=delta+(R-delta)*row/nr;b=delta+(R-delta)*(row+1)/nr
        logratio=(b/a).log();radial=[(b**alpha-a**alpha)/alpha for alpha in alphas]
        residfactors=[(1+2*b)**alpha*logratio for alpha in alphas]
        for phase_index in phases:
            phase=PI*phase_index/(2*m);masses,tv,arcs,mids=angular_data(a,b,phase,n)
            rm=float(((a+b)/2).mid());points=[.5+rm*complex(float(z.real.mid()),float(z.imag.mid())) for z in mids];points+= [-z for z in points]
            plan,info=transport_greedy(masses,points,.5);assert info['repairs']==0;count+=1
            same={};cross=[]
            for (i,j),mass in plan.items():
                ii,jj=i%n,j%n
                if i//n==j//n:
                    k=min(abs(ii-jj),n-abs(ii-jj));same[k]=same.get(k,0)+mass
                else:
                    t=arcs[ii]+arcs[jj];dist=arb.max(up(abs(1+a*t)),up(abs(1+b*t)))
                    cross.append((arb(mass)/UNIT,dist))
            remaining=tv-arb(sum(abs(v) for v in masses[:n]))/UNIT;assert remaining>=0
            for ai,alpha in enumerate(alphas):
                cost=sum((arb(mass)/UNIT*powers[ai][k] for k,mass in same.items()),arb(0))*radial[ai]
                cost+=sum((mass*dist**alpha for mass,dist in cross),arb(0))*logratio
                residual=remaining*residfactors[ai];assert cost>=0 and residual>=0
                totals[ai][phase_index]+=cost+residual;residuals[ai][phase_index]+=residual
        if row%4==0:print(row,args.stop,round(time.monotonic()-started,2),flush=True)
    HERE=Path(__file__).resolve().parent;paths=['local_nodes.py','certify_local_circles_greedy.py','local_circle_greedy.py']
    hashes={s:hashlib.sha256((HERE/s).read_bytes()).hexdigest() for s in paths}
    for ai,alpha in enumerate(alphas):
        a2=2**(1+alpha/2)/(PI*(alpha+2));small=2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
        out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=args.alphas[ai],precision_bits=ctx.prec,angles_per_circle=n,radial_cells=nr,phase_intervals=m,delta=args.delta,row_start=args.start,row_stop=args.stop,phase_start=args.phase_start,phase_stop=end,integer_unit=UNIT,partial_phase_intervals={str(k):v.str(40,more=True) for k,v in totals[ai].items()},residual_phase_intervals={str(k):v.str(35,more=True) for k,v in residuals[ai].items()},small_disk_upper=small.str(40,more=True),plan_counts={'greedy':count},repair_integer_mass=0,elapsed_seconds=time.monotonic()-started,source_hashes=hashes,status='Partial local-circle upper bound for C. Requires exact coverage merge and other spatial regions.')
        name=args.out_stem+'_'+args.alphas[ai].replace('/','_')+'.json';Path(name).write_text(json.dumps(out,indent=2)+'\n');print(name,flush=True)
if __name__=='__main__':main()
