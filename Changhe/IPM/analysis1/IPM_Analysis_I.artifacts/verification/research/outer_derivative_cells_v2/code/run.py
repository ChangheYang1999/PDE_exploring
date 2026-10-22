"""Complete independent exterior-cell enclosures with exact reduction."""
from protocol import *
import argparse,time,resource
import engine_arb as a,engine_iv as b
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);ap.add_argument('--resume',action='store_true');ap.add_argument('--max-new-cells',type=int);args=ap.parse_args();assert args.max_new_cells is None or args.max_new_cells>0
 started=now();p,deps=source();cs=cells();indices=SMOKE if args.tag=='smoke' else list(range(89))
 if args.tag=='full':
  prep=load(OUT/'preparation_acceptance.json');assert prep['status']=='CONFIRMED_OUTER_DERIVATIVE_CELL_PREPARATION_ONLY';rehash(prep['files']);pin(p,OUT/'preparation_acceptance.json')
 path=OUT/(args.tag+'_rows.jsonl');summary=OUT/(args.tag+'_summary.json');assert not summary.exists();done=[];sums=[F(0),F(0)]
 if path.exists():
  assert args.resume
  with path.open() as f:
   header=parse(next(f));assert header['type']=='header' and header['source_freeze_sha256']==sha(OUT/'source_freeze.json') and header['indices']==indices and header['files']==dict(sorted(p.items()))
   for line in f:
    r=parse(line);i=indices[len(done)];check_record(r,i,cs);done.append(i)
    for q in range(2):sums[q]+=max(interval(r[e]['norm_squares'][q])[1] for e in ['arb','iv'])
 else:
  with path.open('x') as f:f.write(json.dumps({'type':'header','utc':started,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'indices':indices,'files':dict(sorted(p.items()))},sort_keys=True)+'\n');f.flush();os.fsync(f.fileno())
 with (OUT/(args.tag+'_restarts.jsonl')).open('a') as f:f.write(json.dumps({'utc':started,'resume':args.resume,'existing_cells':len(done),'source_freeze_sha256':sha(OUT/'source_freeze.json')})+'\n')
 ad=a.setup();bd=b.setup();initial_done=len(done)
 with path.open('a') as f:
  for i in indices[len(done):]:
   assert datetime.now(timezone.utc)<datetime(2026,10,22,12,35,tzinfo=timezone.utc),'run deadline'
   left,right=cs[i];x=a.cell(ad,left,right,True);y=b.cell(bd,left,right,x);x.pop('coefficients');r={'type':'cell','utc':now(),'cell':i,'arb':x,'iv':y};check_record(r,i,cs)
   f.write(json.dumps(r,sort_keys=True,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno());done.append(i)
   for q in range(2):sums[q]+=max(interval(r[e]['norm_squares'][q])[1] for e in ['arb','iv'])
   print(json.dumps({'utc':now(),'completed_cell':i,'completed_count':len(done),'arb_seconds':x['seconds'],'iv_seconds':y['seconds'],'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
   if args.max_new_cells is not None and len(done)-initial_done>=args.max_new_cells and done!=indices:
    rehash(p);print(json.dumps({'utc':now(),'status':'PARTIAL_CHECKPOINT_NO_SUMMARY','completed_cells':len(done)}),flush=True);return
 assert done==indices;tails=tail_squares();total=[x+y for x,y in zip(sums,tails)];roots=root_bounds(total);rehash(p)
 z={'start_utc':started,'utc':now(),'status':'COMPUTED_OUTER_DERIVATIVE_CELLS_REQUIRES_AUDIT_AND_REVIEW','full_exterior':args.tag=='full','cells':len(done),'indices':indices,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'rows_sha256':sha(path),'all_coefficient_overlap_checks':len(done)*17226,'all_derivative_input_checks':len(done)*445005,'cell_squares_upper_exact':[str(v) for v in sums],'accepted_tail_squares_upper_exact':[str(v) for v in tails],'combined_squares_upper_exact':[str(v) for v in total],'norms':roots,'parents':deps,'files':dict(sorted(p.items())),'scope':'Complete exterior only if full_exterior is true. Smoke includes three separated cells and accepted tail, not a cover. No historicalW validation, inverse or endpoint.'}
 write(summary,z);print(json.dumps({k:z[k] for k in ['utc','status','full_exterior','cells','norms']}),flush=True)
if __name__=='__main__':main()
