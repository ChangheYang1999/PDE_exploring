"""All finite angular cells, two interval engines, durable restartable stream."""
from common import *
import argparse,time,fcntl
import engine_arb,engine_iv

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);ap.add_argument('--indices',default='all');ap.add_argument('--resume',action='store_true');ap.add_argument('--stop-after',type=int);args=ap.parse_args()
 tag=safe_tag(args.tag);indices=list(range(TOTAL)) if args.indices=='all' else list(map(int,args.indices.split(',')))
 assert indices and indices==sorted(set(indices)) and all(0<=j<TOTAL for j in indices)
 if args.stop_after is not None:assert args.stop_after>=0
 lock=(E/(tag+'.lock')).open('w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 start=time.monotonic();nodes,keys,tables,dep,selected=load_geometry();startup=startup_remainders(nodes,keys,tables,selected);head=header(indices,dep,startup)
 path=E/(tag+'_rows.jsonl');summary=E/(tag+'_summary.json');restart=E/(tag+'_restarts.jsonl')
 if path.exists():
  assert args.resume,'existing output without resume'
  rows,previous,end=read_stream(path,head,nodes,keys,tables,selected,tag)
  log_event(tag,{'action':'authenticated_resume','complete_rows':len(rows),'last_chain':previous,'source_header_sha256':digest(head),'startup_actual_remainders':startup})
 else:
  rows=[];previous=digest(head);end=None
  with path.open('x') as f:f.write(canon(head)+'\n');f.flush();os.fsync(f.fileno())
  log_event(tag,{'action':'new_run','source_header_sha256':digest(head),'startup_actual_remainders':startup})
 resume_from=len(rows);cache=new_cache();wanted=set(indices[len(rows):]);seen=set()
 with path.open('a') as f:
  if end is None:
   for index,(a,b,node) in enumerate(actual_nodes()):
    if index not in wanted:continue
    if args.stop_after is not None and len(rows)-resume_from>=args.stop_after:break
    assert node==tuple(map(int,nodes[index]));slot=len(rows);assert index==indices[slot]
    m,r,g,record=source_packet(cache,a,b,node,keys[index],tables,selected)
    assert engine_arb.check(node,m,r,g)==engine_iv.check(node,m,r,g)==(COEFF,7)
    row=append_chain(row_payload(slot,index,node,record,m,r),previous)
    f.write(canon(row)+'\n');f.flush();os.fsync(f.fileno());rows.append(row);previous=row['chain'];seen.add(record['width_hex'])
    if len(rows)%100==0:print(canon({'utc':utc(),'cells_complete':len(rows),'planned':len(indices),'seconds':time.monotonic()-start}),flush=True)
   if len(rows)==len(indices):
    end=footer(rows,previous,head)
    if indices==list(range(TOTAL)):assert end['totals']['distinct_widths']==sorted(tables) and end['totals']['old_selected_agreements']==221
    f.write(canon(end)+'\n');f.flush();os.fsync(f.fileno())
 value={'utc':utc(),'status':'COMPUTED_REQUIRES_OUTPUT_AUDIT' if end else 'PARTIAL_OPEN','scope':head['scope'],'cells_complete':len(rows),'planned_cells':len(indices),'footer_read':end is not None,'totals':totals(rows),'rows_sha256':sha(path),'header_sha256':digest(head),'last_chain':previous,'runtime':head['runtime'],'source_files':head['files'],'restarts_sha256':sha(restart),'resumed_from':resume_from,'seconds':time.monotonic()-start}
 write_json(summary,value);print(canon(value),flush=True)
if __name__=='__main__':main()
