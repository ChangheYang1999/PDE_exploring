"""Independent journal, exact-cover and exact-sum audit; optional replay.

This checker never modifies the integration journal. All numerical input is
loaded from the read-only original or previously verified interval artifacts.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, bisect, hashlib, importlib.util, json, time, math
import numpy as np
from flint import arb, ctx
TOP = Path(__file__).resolve().parents[1]
LANE = TOP.parents[1]
RUN = LANE/'proofs/134_residual_green_taylor/evidence/production_28'
ORIGINAL = LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()
def a(q):
    q=Q(q)
    return arb(q.numerator)/q.denominator

def rational_ends(record):
    lo, hi = Q(record['lower_exact']), Q(record['upper_exact'])
    assert lo <= hi
    return lo, hi

def ball(record):
    lo, hi = rational_ends(record)
    return a(lo).union(a(hi))

def rebuild_partition(knots):
    # Deliberately independent of the integrator's partition routine.
    points = {Q(-40), Q(20), Q(0), *knots}
    left, right = min(knots), max(knots)
    delta = Q(1,125)
    while left > -40:
        left = max(Q(-40),left-delta)
        points.add(left)
        delta = min(Q(1,2),delta*2)
    delta = Q(1,125)
    while right < 20:
        right = min(Q(20),right+delta)
        points.add(right)
        delta = min(Q(1,10),delta*2)
    points=sorted(points)
    return list(zip(points,points[1:]))

def check_seed(meta, rows):
    seed=meta['seed_provenance']
    old=Path(seed['previous_directory'])
    assert sha(old/'metadata.json')==seed['previous_metadata_sha256']
    assert sha(old/'leaves.jsonl')==seed['previous_journal_sha256']
    prev=[json.loads(s) for s in (old/'leaves.jsonl').read_text().splitlines()]
    assert len(prev)==seed['seed_count']
    assert prev==rows[:len(prev)]
    old_meta=json.loads((old/'metadata.json').read_text())
    assert old_meta['code_sha256']==seed['previous_code_sha256']
    assert old_meta['proof_sha256']==seed['previous_proof_sha256']
    assert sha(LANE/'proofs/127_residual_interval_norm/code/integrate_abs.py')==seed['previous_code_sha256']
    assert sha(LANE/'proofs/127_residual_interval_norm/PROOF.md')==seed['previous_proof_sha256']
    original=LANE/'proofs/127_residual_interval_norm/evidence/production_28'
    earlier=seed['previous_seed_provenance']
    assert sha(original/'metadata.json')==earlier['previous_metadata_sha256']
    assert sha(original/'leaves.jsonl')==earlier['previous_journal_sha256']
    first=[json.loads(s) for s in (original/'leaves.jsonl').read_text().splitlines()]
    assert len(first)==earlier['seed_count']
    assert first==prev[:len(first)]
    assert sha(LANE/'proofs/127_residual_interval_norm/code/integrate.py')==earlier['previous_code_sha256']
    return {'first_count':len(first),'second_count':len(prev),'unchanged_records':'PASS'}

def audit(prefix=False):
    ctx.prec=512;ctx.threads=1
    meta=json.loads((RUN/'metadata.json').read_text())
    raw=ORIGINAL.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==meta['source_sha256']
    assert str(ORIGINAL)==meta['source_path']
    with np.load(ORIGINAL,allow_pickle=False) as source:
        assert int(source['M'])==260 and int(source['p'])==7
        knots=[Q.from_float(float(v)) for v in source['knots']]
    intervals=rebuild_partition(knots)
    assert [[str(x),str(y)] for x,y in intervals]==meta['base_partition']
    expected={
        'code_sha256':LANE/'proofs/134_residual_green_taylor/code/integrate.py',
        'proof_sha256':LANE/'proofs/134_residual_green_taylor/PROOF.md',
        'green_sha256':LANE/'proofs/68_independent_global_coefficients/evidence/boundaries.json.gz',
        'scalar_sha256':LANE/'proofs/04_modal_scalar/evidence/recomputed.json',
        'outer_source_sha256':LANE/'proofs/122_full_regular_far_tail/evidence/check.json',
    }
    for field,path in expected.items(): assert sha(path)==meta[field],field
    # Read one complete snapshot. A live journal may end in an incomplete line.
    data=(RUN/'leaves.jsonl').read_bytes()
    if prefix and not data.endswith(b'\n'):data=data[:data.rfind(b'\n')+1]
    rows=[json.loads(line) for line in data.splitlines()]
    provenance=check_seed(meta,rows)
    ids=set();counts={};arithmetic_checks=0
    for row in rows:
        key=row['leaf_id'];assert key not in ids;ids.add(key)
        parts=key.split('.');index=int(parts[0]);l,r=intervals[index]
        for digit in parts[1:]:
            assert digit in ('0','1')
            mid=(l+r)/2
            if digit=='0':r=mid
            else:l=mid
        assert len(parts)-1==row['depth']<=12
        assert l==Q(row['left']) and r==Q(row['right']) and l<r
        assert r<=0 or l>=0
        if r<=knots[0]:kind='inner'
        elif l>=knots[-1]:kind='outer'
        else:
            kind='spline';j=bisect.bisect_right(knots,(l+r)/2)-1
            assert knots[j]<=l<r<=knots[j+1]
        assert row['kind']==kind
        assert row['degree']==meta['degree']
        assert row['center_overlap']=='PASS'
        if index>=int(rows[provenance['second_count']-1]['leaf_id'].split('.')[0])+1 or 'algorithm' in row:
            assert row.get('algorithm')=='green_ode_taylor'
            assert row.get('velocity_derivative_overlap')=='PASS'
        counts[kind]=counts.get(kind,0)+1
        for label in ('energy_lower','energy_upper','center_norm','variation_bound','raw_remainder','angular_remainder_bound'):
            lo,hi=rational_ends(row[label]);assert lo>=0
        low=Q(row['energy_lower']['lower_exact'])
        high=Q(row['energy_upper']['upper_exact'])
        assert 0<=low<=high
        er=Q(row['angular_remainder_bound']['upper_exact'])
        cn=Q(row['center_norm']['lower_exact'])
        assert er<max(Q(1,10**40),cn/200) or high<Q(1,10**6)
        # Reconstruct the norm-squared arithmetic from exact stored intervals.
        cn_ball=ball(row['center_norm']);var_ball=ball(row['variation_bound'])
        beta=Q(-1,2) if r<=0 else Q(27,4)
        weight=(a(beta*l).exp())*a(beta*(r-l)).expm1()/a(beta)
        assert ball(row['energy_upper']).overlaps((cn_ball+var_ball)**2*weight)
        lo_candidate=cn_ball-var_ball
        if lo_candidate.upper()<=0:lo_candidate=arb(0)
        elif lo_candidate.lower()<0:lo_candidate=arb(0).union(lo_candidate.upper())
        assert ball(row['energy_lower']).overlaps(lo_candidate**2*weight)
        arithmetic_checks+=2
    ordered=sorted(rows,key=lambda row:Q(row['left']))
    assert Q(ordered[0]['left'])==-40
    assert all(Q(x['right'])==Q(y['left']) for x,y in zip(ordered,ordered[1:]))
    coverage_end=Q(ordered[-1]['right'])
    if not prefix:
        assert coverage_end==20
        assert meta['status']=='COMPUTED_PENDING_AUDIT'
        assert meta['leaf_count']==len(rows)
        assert hashlib.sha256(data).hexdigest()==meta['journal_sha256']
    outer_data=json.loads(expected['outer_source_sha256'].read_text())
    outer=next(row['full_Y'] for row in outer_data['rows'] if Q(row['T'])==20)
    assert outer==meta['outer_tail']
    totals={side:sum((Q(row['energy_'+side][side+'_exact']) for row in rows),Q(0)) for side in ('lower','upper')}
    if not prefix:
        for tail in (meta['inner_tail'],outer):
            for side in totals:totals[side]+=Q(tail['energy_'+side][side+'_exact'])
        for side,value in totals.items():
            assert str(value)==meta['energy_sum_'+side+'_exact']
            assert ball(meta['norm_'+side]).overlaps(a(value).sqrt())
        # Rational decimal bounds need no floating-point conversion.
        lo_int=math.isqrt(totals['lower'].numerator//totals['lower'].denominator)
        hi_int=math.isqrt(totals['upper'].numerator//totals['upper'].denominator)+1
        assert Q(lo_int*lo_int)<totals['lower']
        assert totals['upper']<Q(hi_int*hi_int)
        final_norm={'strict_integer_lower':lo_int,'strict_integer_upper':hi_int,
                    'lower_ball':str(a(totals['lower']).sqrt()),'upper_ball':str(a(totals['upper']).sqrt()),
                    'energy_lower_exact':str(totals['lower']),'energy_upper_exact':str(totals['upper'])}
    else:final_norm=None
    out={'date':now(),'status':'PREFIX_CHECK_PASS' if prefix else 'JOURNAL_AUDIT_PASS',
         'source_sha256':meta['source_sha256'],'journal_sha256':hashlib.sha256(data).hexdigest(),
         'metadata_sha256':sha(RUN/'metadata.json'),'checker_sha256':sha(Path(__file__)),
         'base_interval_count':len(intervals),'leaf_count':len(rows),'branch_counts':counts,
         'coverage_end':str(coverage_end),'arithmetic_checks':arithmetic_checks,
         'seed_provenance':provenance,'final_norm':final_norm,
         'scope':'Journal coverage, provenance and arithmetic. Algorithm proof and higher-precision replay are separate.'}
    dest=TOP/'evidence'/('prefix_audit.json' if prefix else 'journal_audit.json')
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='final_norm'},indent=2),flush=True)
    if final_norm:print(json.dumps(final_norm,indent=2),flush=True)
    return rows,meta

def replay(rows,meta):
    spec=importlib.util.spec_from_file_location('replay_integrator',LANE/'proofs/134_residual_green_taylor/code/integrate.py')
    I=importlib.util.module_from_spec(spec);spec.loader.exec_module(I)
    ctx.prec=640;ctx.threads=1
    I.M.SOURCE=ORIGINAL;d=I.M.Data();cache=I.G.load_cache(d)
    ends={'inner':I.inner_eps(d,cache),'outer':(I.G.density_eps(d,'outer'),*I.G.outer_eps(d,cache)[:2])}
    moments=I.ANG.moments(1044);mass=I.ANG.beta_mass()
    byid={row['leaf_id']:row for row in rows}
    targets=[Q(-35),Q(-10),d.tm,Q(-4),Q(0),Q(215,100),Q(4),Q(68,10),d.tp,Q(99,10),Q(12),Q(16),Q(1999,100)]
    chosen=[]
    for target in targets:
        row=min(rows,key=lambda r:abs((Q(r['left'])+Q(r['right']))/2-target))
        if row['leaf_id'] not in chosen:chosen.append(row['leaf_id'])
    results=[];start=time.monotonic()
    for key in chosen:
        saved=byid[key];fresh=I.window(d,cache,Q(saved['left']),Q(saved['right']),36,ends,moments,mass)
        assert ball(saved['center_norm']).overlaps(ball(fresh['center_norm'])),key
        old_interval=a(Q(saved['energy_lower']['lower_exact'])).union(a(Q(saved['energy_upper']['upper_exact'])))
        new_interval=a(Q(fresh['energy_lower']['lower_exact'])).union(a(Q(fresh['energy_upper']['upper_exact'])))
        assert old_interval.overlaps(new_interval),key
        results.append({'leaf_id':key,'saved_date':saved['date'],'saved_kind':saved['kind'],'replay':fresh,'overlap':'PASS'})
        print(json.dumps({'date':now(),'leaf_id':key,'replay':'PASS','seconds':time.monotonic()-start}),flush=True)
        (TOP/'evidence/replay.json').write_text(json.dumps({'date':now(),'status':'IN_PROGRESS','bits':640,'degree':36,'rows':results},indent=2)+'\n')
    inner=I.inner_tail(d,ends,Q(-40),mass)
    assert ball(inner['energy_upper']).overlaps(ball(meta['inner_tail']['energy_upper']))
    (TOP/'evidence/replay.json').write_text(json.dumps({'date':now(),'status':'REPLAY_PASS','bits':640,'degree':36,
        'source_sha256':d.sha,'checker_sha256':sha(Path(__file__)),'rows':results,'inner_tail':inner,'seconds':time.monotonic()-start},indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--prefix',action='store_true');p.add_argument('--replay',action='store_true');args=p.parse_args()
    rows,meta=audit(args.prefix)
    if args.replay:replay(rows,meta)
