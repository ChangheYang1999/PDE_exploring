"""Conservative historical elapsed-chunk bounds; see research/ledger-bounds/PROOF.md.
No trainer imports, process changes, or activity-time credit.
"""
from __future__ import annotations
import argparse,datetime,hashlib,json,math
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def stamp(x):
    if isinstance(x,(int,float)): return float(x)
    return datetime.datetime.fromisoformat(x.replace('Z','+00:00')).timestamp()

def merged(intervals):
    out=[]
    for a,b in sorted(intervals):
        if not (math.isfinite(a) and math.isfinite(b) and b>=a): raise ValueError('Invalid interval')
        if b==a: continue
        if not out or a>out[-1][1]:out.append([a,b])
        else:out[-1][1]=max(b,out[-1][1])
    return out

def length(intervals): return sum(b-a for a,b in merged(intervals))

def bounded(groups,exact=()):
    intervals=[p for g in groups for p in g['outer_intervals']]+list(exact)
    upper=length(intervals)
    missing=0.
    for g in groups:
        w=length(g['outer_intervals']);a=g['active_lower_seconds']
        if not 0<=a<=w+1e-7: raise ValueError('Activity violates outer containment: '+str(g))
        missing+=w-a
    lower=max([0.,length(exact),upper-missing]+[g['active_lower_seconds'] for g in groups])
    return dict(lower_seconds=lower,upper_seconds=upper,lower_hours=lower/3600,upper_hours=upper/3600,
                missing_measure_upper_seconds=missing)

def audit(path):
    data=Path(path).read_bytes();rows=[json.loads(x) for x in data.splitlines() if x.strip()]
    seen=set();grouped=defaultdict(list);naive=[];bad=[];exact=[]
    for i,r in enumerate(rows):
        key=json.dumps(r,sort_keys=True)
        if key in seen:raise ValueError('Duplicate record '+str(i))
        seen.add(key)
        if 'active_intervals' in r:
            exact.extend((stamp(a),stamp(b)) for a,b in r['active_intervals']);continue
        s,e=stamp(r['interval_start']),stamp(r['interval_end']);a=float(r['active_seconds'])
        if not (e>=s and a>=0 and math.isfinite(a)):raise ValueError('Invalid legacy record')
        outer=[s-30.,e+1.];lo=max(0.,a-.0005001)
        naive.append((s,e,a))
        if a>e-s:bad.append(dict(record_index=i,exp_id=r['exp_id'],displayed_wall_seconds=e-s,
                                active_seconds=a,excess_seconds=a-(e-s)))
        grouped[(r['host'],r['pid'])].append(dict(index=i,outer=outer,active_lower_seconds=lo,
            step_start=r.get('step_start'),step_end=r.get('step_end'),exp_id=r['exp_id']))
    groups=[]
    for (host,pid),items in grouped.items():
        groups.append(dict(host=host,pid=pid,record_indices=[i['index'] for i in items],
            outer_intervals=merged([i['outer'] for i in items]),
            active_lower_seconds=sum(i['active_lower_seconds'] for i in items)))
    per_record=[dict(outer_intervals=[i['outer']],active_lower_seconds=i['active_lower_seconds'])
                for items in grouped.values() for i in items]
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    return dict(observed_utc=now,ledger_sha256=hashlib.sha256(data).hexdigest(),records=len(rows),
        historical_records=len(naive),exact_subinterval_count=len(exact),
        rounded_endpoint_containment_violations=bad,
        uncorrected_lead_formula=dict(upper_seconds=length([(s,e) for s,e,a in naive]+exact),
          lower_seconds=length([(s,e) for s,e,a in naive]+exact)-sum(max(0,e-s-a) for s,e,a in naive)),
        conservative_per_record=bounded(per_record,exact),conservative_per_worker=bounded(groups,exact),groups=groups,
        scope='Bounds on the audited credited elapsed chunks, conditional on ordered non-jumping epoch clock, no duplicate records, and source protocol. Historical ledger does not certify exclusion of short pauses/checkpoint I/O. No 96-hour completion claim.',
        proof='research/ledger-bounds/PROOF.md')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('ledger',type=Path);args=parser.parse_args()
    result=audit(args.ledger);out=ROOT/'evidence'/('ledger-bounds-'+result['ledger_sha256'][:16]+'.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='groups'},indent=2));print(out)

if __name__=='__main__':main()
