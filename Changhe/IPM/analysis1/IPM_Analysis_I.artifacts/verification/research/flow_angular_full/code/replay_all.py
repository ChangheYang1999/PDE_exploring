"""Fresh exact-ancestry source regeneration and1536-bit every-box replay."""
from common import *
import argparse,time
import engine_complex

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);args=ap.parse_args();tag=safe_tag(args.tag);start=time.monotonic()
 nodes,keys,tables,dep,selected=load_geometry();startup=startup_remainders(nodes,keys,tables,selected)
 a=load(E/(tag+'_output_audit.json'));stream=E/(tag+'_rows.jsonl')
 assert a['status']=='PASS_STRUCTURE_REQUIRES_FULL_FRESH_REPLAY' and a['rows_sha256']==sha(stream) and a['summary_sha256']==sha(E/(tag+'_summary.json'))
 assert a['code_sha256']==sha(D/'code/audit_output.py') and a['restarts_sha256']==sha(E/(tag+'_restarts.jsonl'))
 cache=new_cache();checks=0;geochecks=0;rows=0;observed=set();old=0;recordhash=hashlib.sha256()
 with stream.open() as f:
  h=json.loads(next(f));indices=list(range(TOTAL)) if h['indices'] is None else h['indices'];assert h==header(indices,dep,startup);previous=digest(h);ended=False
  for line in f:
   assert line.endswith('\n') and not ended;row=json.loads(line)
   if row.get('type')=='footer':
    assert rows==len(indices) and row['final_chain']==previous and row['header_sha256']==digest(h);ended=True;continue
   index=indices[rows];node=tuple(map(int,nodes[index]));previous=validate_row(row,rows,index,node,previous,keys,tables,selected)
   left,right=ancestry_node(*node);m,r,g,packet=source_packet(cache,left,right,node,keys[index],tables,selected)
   for k,v in packet.items():assert row[k]==v,(index,k)
   assert row['witnesses']==witnesses(m,r)
   nc,ng=engine_complex.check(node,m,r,g);checks+=nc;geochecks+=ng;rows+=1;observed.add(packet['width_hex']);old+=packet['old_selected_agreement']
   recordhash.update(canon({'node_index':index,'source_box_sha256':packet['source_box_sha256'],'endpoint_record_sha256':packet['endpoint_record_sha256'],'checks':nc,'geometry':ng}).encode()+b'\n')
   if rows%500==0:print(canon({'utc':utc(),'replayed':rows,'seconds':time.monotonic()-start}),flush=True)
 assert ended and rows==a['cells_audited']==len(indices) and checks==rows*COEFF and geochecks==rows*7
 full=indices==list(range(TOTAL))
 if full:assert rows==TOTAL and observed==set(tables) and old==221
 out={'utc':utc(),'status':'PASS_EVERY_BOX_FRESH_REPLAY_REQUIRES_VERIFIER_CLOSURE','scope':h['scope'],'full_finite':full,'cells_replayed':rows,'coefficient_checks':checks,'geometry_checks':geochecks,'axis_predicates':rows,'actual_remainder_table_comparisons':rows,'startup_actual_remainders':startup,'exact_remainder_inequalities':4176,'observed_widths':sorted(observed),'old_selected_agreements':old,'replay_record_sha256':recordhash.hexdigest(),'rows_sha256':sha(stream),'output_audit_sha256':sha(E/(tag+'_output_audit.json')),'summary_sha256':sha(E/(tag+'_summary.json')),'restarts_sha256':sha(E/(tag+'_restarts.jsonl')),'source_files':h['files'],'runtime':h['runtime'],'code_sha256':sha(__file__),'seconds':time.monotonic()-start}
 write_json(E/(tag+'_replay.json'),out);print(canon(out),flush=True)
if __name__=='__main__':main()
