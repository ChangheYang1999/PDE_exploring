# Sum the referee-question wall times (unrounded seconds summed, then rounded) in RESOURCES.md (question-file creation to exit-file creation) from the referee directories.
import os, json, datetime
base='referee/'
rows=[]
for tag in sorted(os.listdir(base)):
    d=base+tag
    q=d+'/question.md'; x=d+'/exit'
    if not os.path.isfile(q): continue
    t0=os.path.getmtime(q) if not os.path.exists(d+'/running') or os.path.exists(x) else os.path.getmtime(q)
    t1=os.path.getmtime(x) if os.path.exists(x) else None
    f=lambda t: datetime.datetime.fromtimestamp(t,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') if t else None
    rows.append(dict(tag=tag,launched=f(t0),finished=f(t1),wall_min=round((t1-t0)/60,1) if t1 else None,
                     wall_s=(t1-t0) if t1 else None))
done=[r for r in rows if r['wall_min'] is not None]
out=dict(generated=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),n_completed=len(done),
         sum_wall_min=round(sum(r['wall_s'] for r in done)/60,1),min_wall=round(min(r['wall_s'] for r in done)/60,1),
         max_wall=round(max(r['wall_s'] for r in done)/60,1),last_finished=max(r['finished'] for r in done),
         running=[r['tag'] for r in rows if r['wall_min'] is None],rows=rows)
json.dump(out,open('author_checks/lead_resource_totals_output.json','w'),indent=1)
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=1))
