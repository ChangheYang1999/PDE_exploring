"""Certified finite transports on the truncated middle circles.
See 08_improved_upper_bounds/middle_circle_transport/PROOF.md.
Copy of the verifier's certify_middle_chunks.py for the uniform-in-alpha comparison. Changes: --groups lists shape groups
as REF:ALPHA1,ALPHA2,...;REF:...; for each (radial bin, phase, group) one exact integer plan is selected by best_plan with
the float costs at the group's reference exponent REF and then evaluated exactly at every exponent of the group (an
admissible plan need not be optimal). With a single group whose list is its reference exponent this is the original
computation. The output path is relative to the working directory.
"""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,acb,ctx
from certify_far_circles import cell_measures,upper_decimal
from middle_circle_plan import best_plan,edge_kind
import argparse,json,time,hashlib
ctx.prec=160
PI=arb.pi();ROOT=Path(__file__).resolve().parents[1]

def bin_data(index,nr,n):
    lo=PI*index/(2*nr);hi=PI*(index+1)/(2*nr);tt=lo.union(hi)
    rr=tt.sin();jac=tt*rr*tt.cos()
    radius_upper=arb(rr.upper());jac_upper=arb(abs(jac).upper());angle_upper=arb(hi.upper())
    M1=jac_upper*angle_upper*16*radius_upper/PI
    M2=jac_upper*angle_upper**2*(16*radius_upper+96*radius_upper**2)/PI
    values=[]
    for j in range(n):
        ss=-1+(arb(2*j)+1)/n;theta=PI/2+tt*ss
        z=acb(rr*theta.cos(),rr*theta.sin())
        value=jac*z/(PI*(z*z-arb(1)/4)**2)
        assert value.is_finite()
        values.append(value)
    return lo,hi,radius_upper,values,M1,M2

def main():
    p=argparse.ArgumentParser();p.add_argument('--angles',type=int,default=256);p.add_argument('--radial',type=int,default=128)
    p.add_argument('--phases',type=int,default=16);p.add_argument('--groups',required=True);p.add_argument('--tries',type=int,default=17)
    p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True)
    p.add_argument('--out',required=True);args=p.parse_args()
    n=args.angles;nr=args.radial;m=args.phases;assert n>=8 and nr>=8 and m>0 and 0<=args.start<args.stop<=nr
    groups=[(g.split(':')[0],g.split(':')[1].split(',')) for g in args.groups.split(';')]
    texts=[x for _,xs in groups for x in xs];alphas=[arb(x) for x in texts];assert all(a>0 and a<1 for a in alphas)
    owner=[gi for gi,(_,xs) in enumerate(groups) for _ in xs];refs=[arb(r) for r,_ in groups]
    phases=[((PI*k/(2*m)).cos(),(PI*k/(2*m)).sin()) for k in range(m+1)]
    totals=[[arb(0) for _ in phases] for _ in alphas];residuals=[[arb(0) for _ in phases] for _ in alphas]
    counts={'adjacent':0,'antipodal':0,'zero':0};unit=2**44;started=time.monotonic()
    for index in range(args.start,args.stop):
        lo,hi,rmax,values,M1,M2=bin_data(index,nr,n)
        costs=[];proxies=[]
        for alpha in alphas:
            same=[(2*rmax*(hi*(k+1)/n).sin())**alpha for k in range(n)]
            opposite=[(2*rmax*(lo*max(0,k-1)/n).cos())**alpha for k in range(n)]
            costs.append((same,opposite))
        for alpha in refs:
            same=[(2*rmax*(hi*(k+1)/n).sin())**alpha for k in range(n)]
            opposite=[(2*rmax*(lo*max(0,k-1)/n).cos())**alpha for k in range(n)]
            proxies.append(([float(v.mid()) for v in same],[float(v.mid()) for v in opposite]))
        for phase_index,(cc,ss) in enumerate(phases):
            masses,tv=cell_measures(values,cc,ss,M1,M2,arb(2)/n,unit)
            extracted=arb(sum(abs(v) for v in masses[:n]))/unit
            remainder=tv-extracted;assert remainder>=0
            groupedplans=[]
            for fs,fo in proxies:
                plan,info=best_plan(masses,fs,fo,tries=args.tries);counts[info['kind']]+=1
                grouped={}
                for (i,j),mass in plan.items():
                    key=edge_kind(i,j,n);grouped[key]=grouped.get(key,0)+mass
                groupedplans.append(grouped)
            for alpha_index,alpha in enumerate(alphas):
                same,opposite=costs[alpha_index];grouped=groupedplans[owner[alpha_index]]
                cost=sum((arb(mass)*(same[k] if is_same else opposite[k]) for (is_same,k),mass in grouped.items()),arb(0))/unit
                residual=(2*rmax)**alpha*remainder
                totals[alpha_index][phase_index]+=(cost+residual)*(hi-lo)
                residuals[alpha_index][phase_index]+=residual*(hi-lo)
        if index%8==0:print(index,nr,round(time.monotonic()-started,2),flush=True)
    rows=[dict(alpha=text,plan_reference_alpha=groups[gi][0],middle_phase_intervals=[v.str(36,more=True) for v in vv],safe_middle_upper=[upper_decimal(v) for v in vv],residual_intervals=[v.str(30,more=True) for v in rr]) for text,gi,vv,rr in zip(texts,owner,totals,residuals)]
    HERE=Path(__file__).resolve().parent;paths=[HERE/'mid_nodes.py',HERE/'middle_circle_plan.py',HERE/'circle_transport_plan.py',HERE/'certify_far_circles.py']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,angles_per_half=n,radial_cells=nr,phase_intervals=m,row_start=args.start,row_stop=args.stop,integer_unit=unit,plan_trials=args.tries,plan_counts=counts,rows=rows,elapsed_seconds=time.monotonic()-started,groups=args.groups,source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Partial middle-region bound. Requires exact row coverage merge, plus other regions and phase interpolation.')
    Path(args.out).write_text(json.dumps(out,indent=2)+'\n')
    for row in rows:print(row['alpha'],row['safe_middle_upper'],flush=True)
if __name__=='__main__':main()
