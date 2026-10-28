"""Independent endpoint/coverage recombination and grouped-cost checks."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,random
import mpmath as mp
from flint import arb,ctx
from certify_local_circles_greedy import angular_data,edge_cost,UNIT
from local_circle_greedy import transport_greedy
ctx.prec=256;mp.mp.dps=90
ROOT=Path(__file__).resolve().parents[1]
def endpoint(text):
    q=arb(text).upper().fmpq()
    return mp.mpf(str(q.numerator))/mp.mpf(str(q.denominator))
def check_final(finalname):
    final=json.loads((ROOT/finalname).read_text());m=final['phase_intervals']
    chunks=[p for p in final['input_hashes'] if p.startswith('data/local_circle_chunks/')]
    for name,digest in final['input_hashes'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
    counts=[[0]*(m+1) for _ in range(final['radial_cells'])];local=[mp.mpf(0) for _ in range(m+1)]
    for name in chunks:
        c=json.loads((ROOT/name).read_text())
        for source,h in c['source_hashes'].items():assert hashlib.sha256((ROOT/source).read_bytes()).hexdigest()==h
        for i in range(c['row_start'],c['row_stop']):
            for j in range(c['phase_start'],c['phase_stop']):counts[i][j]+=1
        for j,value in c['partial_phase_intervals'].items():local[int(j)]+=endpoint(value)
    assert all(v==1 for row in counts for v in row)
    row=final['rows'][0];q=Fraction(row['alpha']);alpha=mp.mpf(q.numerator)/q.denominator
    qd=Fraction(final['delta']);delta=mp.mpf(qd.numerator)/qd.denominator
    middle=json.loads((ROOT/'data/middle_circle_certificate_n512.json').read_text())
    exterior=json.loads((ROOT/'data/far_circle_certificate_fine.json').read_text())
    mr=next(x for x in middle['rows'] if Fraction(x['alpha'])==q)
    er=next(x for x in exterior['rows'] if Fraction(x['alpha'])==q)
    vals=[local[j]+endpoint(mr['middle_phase_intervals'][j])+endpoint(er['far_phase_intervals'][j]) for j in range(m+1)]
    a2=mp.power(2,1+alpha/2)/(mp.pi*(alpha+2))
    small=2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
    value=small+max(vals)/mp.cos(mp.pi/(4*m))
    assert value<mp.mpf(row['safe_upper_C'])
    return dict(alpha=str(q),independent_upper=mp.nstr(value,80),small_disks=mp.nstr(small,70),maximizing_phase_index=max(range(m+1),key=lambda j:vals[j]),safe_upper_C=row['safe_upper_C'],final_source=finalname)
def check_grouping():
    rng=random.Random(20261028);n=512;nr=256;m=16;pi=arb.pi();cases=0
    for _ in range(24):
        i=rng.randrange(nr);j=rng.randrange(m+1)
        a=arb(1)/64+(arb(1)/2-arb(1)/64)*i/nr;b=arb(1)/64+(arb(1)/2-arb(1)/64)*(i+1)/nr
        masses,tv,arcs,mids=angular_data(a,b,pi*j/(2*m),n)
        rm=float(((a+b)/2).mid());pts=[.5+rm*complex(float(z.real.mid()),float(z.imag.mid())) for z in mids];pts+=[-z for z in pts]
        plan,info=transport_greedy(masses,pts,.5);balance=[0]*len(masses)
        grouped={};cross=[]
        for (ii,jj),mass in plan.items():
            balance[ii]+=mass;balance[jj]-=mass
            if ii//n==jj//n:
                diff=abs(ii%n-jj%n);k=min(diff,n-diff);grouped[k]=grouped.get(k,0)+mass
            else:cross.append(((ii,jj),mass))
        assert balance==masses
        for text in ['3/10','1/2','3/4','9/10']:
            alpha=arb(text)
            direct=sum((arb(mass)*edge_cost(ii,jj,a,b,alpha,n,arcs)/UNIT for (ii,jj),mass in plan.items()),arb(0))
            # Recompute the grouped formula independently, with no imported multi-alpha helper.
            other=sum((arb(mass)/UNIT*(2*(pi*min(k+1,n//2)/n).sin())**alpha for k,mass in grouped.items()),arb(0))*(b**alpha-a**alpha)/alpha
            other+=sum((arb(mass)*edge_cost(ii,jj,a,b,alpha,n,arcs)/UNIT for ((ii,jj),mass) in cross),arb(0))
            assert direct.overlaps(other);cases+=1
    old=json.loads((ROOT/'data/local_circle_chunks/a50_p8_17.json').read_text())
    new=json.loads((ROOT/'data/local_circle_chunks/multi_pilot_1_2.json').read_text())
    assert arb(old['partial_phase_intervals']['10']).overlaps(arb(new['partial_phase_intervals']['10']))
    return cases
files=[f'data/local_circle_composite_a{tag}.json' for tag in ['30','75','90']]
rows=[check_final(name) for name in files];n=check_grouping()
paths=files+['code/check_local_composites_more.py','code/certify_local_circles_multi.py','data/local_circle_chunks/multi_pilot_1_2.json','data/local_circle_chunks/a50_p8_17.json']
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_decimal_digits=90,rows=rows,independent_grouped_cost_checks=n,pilot_phase10_overlap=True,status='All exact coverage, source hashes, independent endpoint recombinations, integer balances and grouped-cost checks passed',input_hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in paths})
(ROOT/'data/local_composites_more_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
