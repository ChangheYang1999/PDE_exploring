"""Reconstruct credited elapsed chunks, with explicit rounding and scope.

Independent of the numerics and lead ledger implementations. This does not turn
inter-step elapsed intervals into certified eligible numerical work.
"""
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
import argparse,datetime,hashlib,json,math
from ledger_bounds import stamp,merged,length,bounded
ROOT=Path(__file__).resolve().parents[1]
Q=.000502

def audit(path):
    data=Path(path).read_bytes()
    rows=[json.loads(x) for x in data.splitlines() if x.strip()]
    by_worker=defaultdict(list); nominal=[];legacy=0;chunk_records=0;chunks=0;seen=set()
    invalid_display=[]
    for i,r in enumerate(rows):
        k=json.dumps(r,sort_keys=True)
        if k in seen:raise ValueError('Duplicate record: '+str(i))
        seen.add(k)
        worker=(r['host'],r['pid'])
        field='chunks' if 'chunks' in r else 'active_intervals' if 'active_intervals' in r else None
        if field is not None:
            chunk_records+=1
            if r[field] is None:raise ValueError('Null explicit interval field')
            for j,pair in enumerate(r[field]):
                s,e=map(stamp,pair)
                if not (math.isfinite(s) and math.isfinite(e) and e>=s):raise ValueError('Invalid explicit interval')
                # All current sources round to milliseconds. This conservative
                # allowance also contains finer-resolution epoch endpoints.
                by_worker[worker].append(dict(record=i,chunk=j,outer=[s-Q,e+Q],active_lower_seconds=max(0.,e-s-2*Q)))
                nominal.append([s,e]);chunks+=1
        else:
            legacy+=1;s,e=stamp(r['interval_start']),stamp(r['interval_end']);a=float(r['active_seconds'])
            if not (math.isfinite(s) and math.isfinite(e) and e>=s and math.isfinite(a) and a>=0):raise ValueError('Invalid legacy record')
            by_worker[worker].append(dict(record=i,outer=[s-30.,e+1.],active_lower_seconds=max(0.,a-.0005001)))
            if a>e-s:invalid_display.append(i)
    groups=[dict(host=host,pid=pid,outer_intervals=merged([p['outer'] for p in pieces]),active_lower_seconds=sum(p['active_lower_seconds'] for p in pieces),pieces=pieces) for (host,pid),pieces in by_worker.items()]
    per_piece=[dict(outer_intervals=[p['outer']],active_lower_seconds=p['active_lower_seconds']) for pieces in by_worker.values() for p in pieces]
    return dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),ledger_sha256=hashlib.sha256(data).hexdigest(),records=len(rows),legacy_records=legacy,chunk_records=chunk_records,explicit_chunks=chunks,endpoint_padding_seconds=Q,nominal_serialized_chunk_union_seconds=length(nominal),legacy_display_containment_violations=invalid_display,credited_elapsed_union_bounds=bounded(groups),ungrouped_bounds=bounded(per_piece),groups=groups,scope='Bounds on underlying credited elapsed pieces under the audited disjoint-per-worker protocol and ordered epoch clock. Includes inter-step I/O/pauses. Omits unrecorded first steps. This is NOT a measurement or enclosure of all eligible numerical activity.',proof='research/ledger-bounds/PROOF.md')

def main():
    p=argparse.ArgumentParser();p.add_argument('ledger',type=Path);a=p.parse_args();r=audit(a.ledger)
    out=ROOT/'evidence'/('ledger-reconstruction-'+r['ledger_sha256'][:16]+'.json');out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='groups'},indent=2));print(out)
if __name__=='__main__':main()
