"""Independent source, coverage, node, adaptive chord and endpoint audit.

The correction g is increasing at every exponent by its distance-moment
representation. The chord check uses adaptive dyadic rational pieces and a
stable exponential formula for g, not the submitted fixed4000 grid.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/closed_form37_lead';SRC=BASE/'source'
ctx.prec=320;pi=arb.pi();delta=arb(1)/64

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(x):return arb(str(x))
def rec(v):
    assert v.is_finite()
    return dict(lower=str(v.lower().fmpq()),upper=str(v.upper().fmpq()),display=v.str(30,more=True))
def a2(a):return 2*arb(2)**(a/2)/(pi*(a+2))
def small(a):return 2*a2(a)*delta**a/a+(1+2*delta)**a*delta**2/(2*(1-delta)**2)
def correction(x):
    a=aq(x)
    integral=arb(32).log() if x==0 else -arb(2)**(-a)*(-a*arb(32).log()).expm1()/a
    return -2*a2(a)*integral+(1+2*delta)**a*delta**2/(2*(1-delta)**2)
def a3(a,N=100):
    coeff=arb(1);value=arb(0)
    for k in range(N):
        value+=coeff*arb(4)**(-k-1)*2*(a+5+2*k)/((a+2+2*k)*(a+4+2*k))
        coeff*=arb(2*k+1)/(2*k+2)
    tail=3*arb(4)**(-N)/(pi*(a+2+2*N))
    return 3*value/pi+arb(0).union(tail)
def finite_array(values,n):
    assert len(values)==n
    out=[arb(x) for x in values]
    assert all(x.is_finite() and x>=0 for x in out)
    return out

def main():
    snapshot=json.loads((SRC/'snapshot_manifest.json').read_text())
    for p,h in snapshot['sha256'].items():assert sha(SRC/p)==h,('snapshot',p)
    for name in ['uniform_result_thm35_pass3.json','uniform_result_thm37_pass3.json']:
        assert sha(SRC/'data'/name)==sha(ROOT/'09_uniform_comparison/pass3/data'/name)
    for g in [0,1,7]:
        name=f'far2_g{g}.json'
        assert sha(SRC/'data'/name)==sha(ROOT/'09_uniform_comparison/lead_certificate/data'/name)
    for name in ['certify_far_circles.py','certify_local_circles_greedy.py','local_circle_greedy.py','middle_circle_plan.py','circle_transport_plan.py']:
        assert sha(SRC/'code'/name)==sha(ROOT/'09_uniform_comparison/pass3/source'/name),(name,'changed dependency')
    data=json.loads((SRC/'data/remainders37.json').read_text());nodes=json.loads((SRC/'data/nodes2.json').read_text())
    for p,h in data['source_sha256'].items():assert sha(SRC/p)==h
    assert data['delta']=='1/64'
    old=json.loads((SRC/'data/uniform_result_thm37_pass3.json').read_text())['nodal_upper']
    middle={};coverage_records=[]
    for folder in ['mid','mid7']:
        paths=sorted((SRC/folder).glob('n512_*.json'));assert paths
        seen={};reference=None
        for path in paths:
            obj=json.loads(path.read_text())
            params={k:obj[k] for k in ['precision_bits','angles_per_half','radial_cells','phase_intervals','integer_unit','plan_trials','groups','source_hashes']}
            if reference is None:reference=params
            else:assert params==reference
            assert params['angles_per_half']==512 and params['radial_cells']==512 and params['phase_intervals']==16
            assert params['precision_bits']>=160 and params['integer_unit']==2**44 and params['plan_trials']==17
            for name,h in params['source_hashes'].items():assert sha(SRC/'code'/name)==h
            wanted=set()
            for group in params['groups'].split(';'):
                ref,aa=group.split(':');wanted.update((Q(ref),Q(a)) for a in aa.split(','))
            keys=[(Q(row['plan_reference_alpha']),Q(row['alpha'])) for row in obj['rows']]
            assert len(keys)==len(set(keys)) and set(keys)==wanted
            start,stop=obj['row_start'],obj['row_stop'];assert 0<=start<stop<=512
            for key,row in zip(keys,obj['rows']):
                arr=finite_array(row['middle_phase_intervals'],17)
                for r in range(start,stop):
                    assert (key,r) not in seen;seen[(key,r)]=path.name
                if key not in middle:middle[key]=[arb(0) for _ in range(17)]
                middle[key]=[a+b for a,b in zip(middle[key],arr)]
        assert len(seen)==len(wanted)*512
        coverage_records.append(dict(kind=folder,files=len(paths),keys=len(wanted),radial_rows=512))
    local_cache={}
    def local(x,folder):
        if (x,folder) in local_cache:return local_cache[(x,folder)]
        suffix=str(x).replace('/','_');paths=sorted((SRC/folder).glob(f'r*_{suffix}.json'));assert paths
        seen=set();totals=[arb(0) for _ in range(17)];reference=None
        for path in paths:
            obj=json.loads(path.read_text())
            params={k:obj[k] for k in ['alpha','precision_bits','angles_per_circle','radial_cells','phase_intervals','delta','integer_unit','source_hashes']}
            if reference is None:reference=params
            else:assert params==reference
            assert Q(params['alpha'])==x and Q(params['delta'])==Q(1,64)
            assert params['angles_per_circle']==512 and params['radial_cells']==256 and params['phase_intervals']==16
            assert params['precision_bits']>=160 and params['integer_unit']==2**44
            for name,h in params['source_hashes'].items():assert sha(SRC/'code'/name)==h
            r0,r1=obj['row_start'],obj['row_stop'];j0,j1=obj['phase_start'],obj['phase_stop']
            assert 0<=r0<r1<=256 and 0<=j0<j1<=17
            assert set(map(int,obj['partial_phase_intervals']))==set(range(j0,j1))
            assert obj['repair_integer_mass']==0
            if x==0:assert obj['small_disk_upper'] is None
            else:assert small(aq(x)).overlaps(arb(obj['small_disk_upper']))
            for r in range(r0,r1):
                for j in range(j0,j1):assert (r,j) not in seen;seen.add((r,j))
            for text,value in obj['partial_phase_intervals'].items():
                v=arb(value);assert v.is_finite() and v>=0;totals[int(text)]+=v
        assert len(seen)==256*17
        coverage_records.append(dict(kind=folder,alpha=str(x),files=len(paths),row_phase_cells=len(seen)))
        local_cache[(x,folder)]=totals;return totals
    node_checks=[];groups=[]
    for g in range(8):
        rows=data['groups'][str(g)];xs=[Q(r['alpha']) for r in rows]
        expected=([Q(0)] if g==0 else [])+[Q(x) for x in nodes['groups'][g]['upper_nodes']]
        assert xs==expected and xs==sorted(set(xs))
        if g:assert xs[0]==groups[-1][-1][0]
        groups.append([(Q(r['alpha']),Q(r['R'])) for r in rows]);assert all(r['kind']=='thm37' for r in rows)
        far={};ref=Q(nodes['groups'][g]['far_ref'])
        if g in [0,1,7]:
            files=[f'far2_g{g}.json']+(['far_a0.json'] if g==0 else [])
            for name in files:
                f=json.loads((SRC/'data'/name).read_text());assert Q(f['plan_reference_alpha'])==ref and f['phase_intervals']==16
                for row in f['rows']:
                    x=Q(row['alpha']);arr=row['far_phase_intervals']
                    if x in far:assert far[x]==arr
                    far[x]=arr
        for row in rows:
            x=Q(row['alpha']);target=aq(Q(row['R']));assert target>0
            if g in [0,1,7]:
                l=local(x,'local7' if g==7 else 'local');m=middle[(ref,x)];e=finite_array(far[x],17)
                values=[a+b+c for a,b,c in zip(l,m,e)];bound=values[0]
                for value in values[1:]:bound=arb.max(bound,value)
                bound/=(pi/64).cos()
            else:bound=arb(old[str(g)]['C'][str(x)])-small(aq(x))
            assert target>=bound,('node',g,x,target,bound)
            node_checks.append(dict(group=g,alpha=str(x),margin=rec(target-bound)))
    assert groups[0][0][0]==0 and groups[-1][-1][0]==Q(199,200)
    kap=arb(209)/500;c=arb(1353)/2500;checks=[]
    for g,rows in enumerate(groups):
        for (x,rx),(y,ry) in zip(rows,rows[1:]):
            left=aq(rx).log();slope=(aq(ry).log()-left)/aq(y-x)
            def exponential(t):return (left+slope*aq(t-x)).exp()
            pending=[(x,y,0)];passed=[]
            while pending:
                p,q,depth=pending.pop();assert depth<30
                bound=arb.max(exponential(p),exponential(q))+correction(q)
                margin=kap/(1-aq(p))+c-bound
                if margin>0:passed.append((p,q,margin));continue
                mid=(p+q)/2;pending.extend([(mid,q,depth+1),(p,mid,depth+1)])
            passed.sort(key=lambda z:z[0]);cursor=x
            for p,q,v in passed:assert p==cursor;cursor=q
            assert cursor==y
            worst=passed[0][2]
            for _,_,v in passed[1:]:worst=arb.min(worst,v)
            checks.append(dict(group=g,a=str(x),b=str(y),pieces=len(passed),margin=rec(worst)))
    end=[]
    for i in range(100):
        x=Q(199,200)+Q(i,20000);y=x+Q(1,20000);a=aq(x).union(aq(y));d=1-a
        numerator=2*a3(a)+d*arb(2)**(a+1)/(3*pi)
        scaled=(2*a2(a))**(1-a)*numerator**a/a
        lc=arb(2)**(1-a)*a2(a)/a
        margin=d*lc+kap+c*d-scaled;assert margin>0
        end.append(dict(a=str(x),b=str(y),margin=rec(margin)))
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=320,coverage=coverage_records,node_checks=node_checks,
                adaptive_chords=checks,endpoint_intervals=end,snapshot_sha256=sha(SRC/'snapshot_manifest.json'),auditor_sha256=sha(Path(__file__)),
                verdict='CONFIRMED for all source, exact coverage, nodal recombination, adaptive chord and endpoint checks. Full independent alpha-zero geometry is recorded separately.')
    out=BASE/'verification/independent_audit.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print(result['time_utc'],'nodes',len(node_checks),'segments',len(checks),'adaptive pieces',sum(x['pieces'] for x in checks),'PASS')
if __name__=='__main__':main()
