"""Certified local diagonal plans, including an exact radial identity allocation."""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
from certify_local_circles_greedy import angular_data,UNIT
from local_circle_batch_exchange import transport_batch_exchange as transport_greedy
import argparse,json,hashlib,time
ctx.prec=160;PI=arb.pi();ROOT=Path(__file__).resolve().parents[1]
def up(x):return arb(x.upper())
def main():
    p=argparse.ArgumentParser();p.add_argument('--alphas',nargs='+',required=True)
    p.add_argument('--angles',type=int,default=256);p.add_argument('--radial',type=int,default=128)
    p.add_argument('--phases',type=int,default=16);p.add_argument('--delta',default='1/64');p.add_argument('--power',default='1')
    p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True)
    p.add_argument('--phase-start',type=int,default=0);p.add_argument('--phase-stop',type=int)
    p.add_argument('--out-stem',required=True);p.add_argument('--spacing',choices=['linear','square'],default='square');args=p.parse_args()
    n=args.angles;nr=args.radial;m=args.phases;alphas=[arb(s) for s in args.alphas]
    delta=arb(args.delta);R=arb(1)/2;power=arb(args.power);end=2*m+1 if args.phase_stop is None else args.phase_stop
    assert n>=16 and n%8==0 and 0<delta<R and power>0 and all(0<x<1 for x in alphas)
    assert 0<=args.start<args.stop<=nr and 0<=args.phase_start<end<=2*m+1
    phases=range(args.phase_start,end)
    chords=[2*(PI*min(k+1,n//2)/n).sin() for k in range(n//2+1)]
    powers=[[chord**alpha for chord in chords] for alpha in alphas]
    totals=[{k:arb(0) for k in phases} for _ in alphas]
    residuals=[{k:arb(0) for k in phases} for _ in alphas]
    count=0;started=time.monotonic()
    for row in range(args.start,args.stop):
        if args.spacing=='linear':
            a=delta+(R-delta)*row/nr;b=delta+(R-delta)*(row+1)/nr
        else:
            a=(delta.sqrt()+(R.sqrt()-delta.sqrt())*row/nr)**2
            b=(delta.sqrt()+(R.sqrt()-delta.sqrt())*(row+1)/nr)**2
        logratio=(b/a).log();radial=[(b**alpha-a**alpha)/alpha for alpha in alphas]
        residfactors=[(1+2*b)**alpha*logratio for alpha in alphas]
        atom=int((arb((power/2*(2*a)**power).lower())*UNIT).floor().unique_fmpz())
        atomres=((2*b)**power-(2*a)**power)/2-arb(atom)/UNIT*logratio
        assert atom>=0 and atomres>=0
        for j in phases:
            phase=PI*j/(2*m);masses,tv,arcs,mids=angular_data(a,b,phase,n)
            extracted=arb(sum(abs(v) for v in masses[:n]))/UNIT
            masses=masses+[-atom,atom]
            rm=float(((a+b)/2).mid());points=[.5+rm*complex(float(z.real.mid()),float(z.imag.mid())) for z in mids];points+= [-z for z in points];points += [.5,-.5]
            plan,info=transport_greedy(masses,points,.5);assert info['repairs']==0;count+=1
            same={};variable=[];own=0;center=0
            for (i,k),mass in plan.items():
                if i<2*n and k<2*n:
                    ii,kk=i%n,k%n
                    if i//n==k//n:
                        diff=abs(ii-kk);d=min(diff,n-diff);same[d]=same.get(d,0)+mass
                    else:
                        t=arcs[ii]+arcs[kk];dist=arb.max(up(abs(1+a*t)),up(abs(1+b*t)))
                        variable.append((arb(mass)/UNIT,dist))
                elif i>=2*n and k>=2*n:
                    assert i!=k;center+=mass
                else:
                    arc=i if i<2*n else k;cen=k if i<2*n else i
                    if arc//n==cen-2*n:own+=mass
                    else:
                        t=arcs[arc%n];dist=arb.max(up(abs(1+a*t)),up(abs(1+b*t)))
                        variable.append((arb(mass)/UNIT,dist))
            remaining=tv-extracted;assert remaining>=0
            for ai,alpha in enumerate(alphas):
                cost=(sum((arb(mass)/UNIT*powers[ai][d] for d,mass in same.items()),arb(0))+arb(own)/UNIT)*radial[ai]
                cost+=(sum((mass*dist**alpha for mass,dist in variable),arb(0))+arb(center)/UNIT)*logratio
                residual=remaining*residfactors[ai]+atomres;assert cost>=0 and residual>=0
                totals[ai][j]+=cost+residual;residuals[ai][j]+=residual
        if row%4==0:print(row,args.stop,round(time.monotonic()-started,2),flush=True)
    paths=['code/certify_local_diagonal_batch.py','code/local_circle_batch_exchange.py','code/certify_local_circles_greedy.py','code/local_circle_greedy.py','08_improved_upper_bounds/paired_local_diagonal/PROOF.md','08_improved_upper_bounds/paired_local_circles/PROOF.md']
    hashes={s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in paths}
    for ai,alpha in enumerate(alphas):
        a2=2**(1+alpha/2)/(PI*(alpha+2));small=2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
        out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=args.alphas[ai],power=args.power,spacing=args.spacing,precision_bits=ctx.prec,angles_per_circle=n,radial_cells=nr,phase_half_intervals=m,delta=args.delta,row_start=args.start,row_stop=args.stop,phase_start=args.phase_start,phase_stop=end,integer_unit=UNIT,partial_phase_intervals={str(k):v.str(40,more=True) for k,v in totals[ai].items()},residual_phase_intervals={str(k):v.str(35,more=True) for k,v in residuals[ai].items()},small_disk_upper=small.str(40,more=True),small_identity_mass=((2*delta)**power/2).str(40,more=True),plan_counts={'batch_exchange':count},repair_integer_mass=0,elapsed_seconds=time.monotonic()-started,source_hashes=hashes,status='Partial diagonal local-circle upper bound. Needs exact coverage, middle/exterior pieces and phase correction.')
        name=args.out_stem+'_'+args.alphas[ai].replace('/','_')+'.json';(ROOT/name).write_text(json.dumps(out,indent=2)+'\n');print(name,flush=True)
if __name__=='__main__':main()
