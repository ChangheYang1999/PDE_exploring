"""Selected complete-cell replay, with separately auditable short pieces."""
from protocol import *
import argparse,resource
import engine_arb as a,engine_iv as b
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);ap.add_argument('--cell',type=int);ap.add_argument('--collect',action='store_true');args=ap.parse_args();assert not(args.collect and args.cell is not None)
 started=now();p,deps=source();s=load(OUT/(args.tag+'_summary.json'));audit=load(OUT/(args.tag+'_audit.json'));sh=sha(OUT/(args.tag+'_summary.json'));ah=sha(OUT/(args.tag+'_audit.json'));assert audit['summary_sha256']==sh;selected=audit['required_replay_cells'];assert selected==(SMOKE if args.tag=='smoke' else sorted(set(REPLAY+audit['maximum_contribution_cells'])))
 rows={}
 with (OUT/(args.tag+'_rows.jsonl')).open() as f:
  next(f)
  for line in f:
   z=parse(line)
   if z['cell'] in selected:rows[z['cell']]=z
 assert sorted(rows)==selected and (args.cell is None or args.cell in selected);cs=cells();indices=[] if args.collect else ([args.cell] if args.cell is not None else selected)
 if indices:ad=a.setup();bd=b.setup()
 for i in indices:
  target=OUT/(args.tag+'_replay_cell_'+str(i)+'.json');assert not target.exists()
  x=a.cell(ad,*cs[i],True);y=b.cell(bd,*cs[i],x);x.pop('coefficients')
  for e,z in [('arb',x),('iv',y)]:assert {k:v for k,v in z.items() if k!='seconds'}=={k:v for k,v in rows[i][e].items() if k!='seconds'},('replay mismatch',i,e)
  rehash(s['files']);rehash(p)
  result={'start_utc':started,'utc':now(),'status':'PASS_ONE_COMPLETE_EXTERIOR_DERIVATIVE_CELL_REPLAY','cell':i,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'summary_sha256':sh,'audit_sha256':ah,'coefficient_overlap_checks':y['coefficient_overlap_checks'],'derivative_input_checks':y['derivative_input_checks'],'integer_coefficient_sha256':y['integer_coefficient_sha256']};write(target,result);print(json.dumps({'utc':now(),'replayed_cell':i}),flush=True)
 if args.cell is not None:return
 results=[];pieces={};starts=[]
 for i in selected:
  target=OUT/(args.tag+'_replay_cell_'+str(i)+'.json');r=load(target)
  assert r['status']=='PASS_ONE_COMPLETE_EXTERIOR_DERIVATIVE_CELL_REPLAY' and r['cell']==i and r['source_freeze_sha256']==sha(OUT/'source_freeze.json') and r['summary_sha256']==sh and r['audit_sha256']==ah
  assert when(audit['utc'])<when(r['start_utc'])<when(r['utc'])<datetime.now(timezone.utc)
  assert r['coefficient_overlap_checks']==17226 and r['derivative_input_checks']==445005 and r['integer_coefficient_sha256']==rows[i]['iv']['integer_coefficient_sha256']
  results.append(r);pin(pieces,target);starts.append(r['start_utc'])
 rehash(s['files']);rehash(p);write(OUT/(args.tag+'_replay.json'),{'start_utc':min(starts,key=when),'utc':now(),'status':'PASS_SELECTED_COMPLETE_EXTERIOR_DERIVATIVE_REPLAY','full_exterior':s['full_exterior'],'required_cells':selected,'results':results,'pieces':pieces,'summary_sha256':sh,'audit_sha256':ah})
if __name__=='__main__':main()
