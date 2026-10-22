"""Independent full output structure, exact grid and ancestry audit."""
from common import *
import argparse,time

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);args=ap.parse_args();tag=safe_tag(args.tag);start=time.monotonic()
 nodes,keys,tables,dep,selected=load_geometry();startup=startup_remainders(nodes,keys,tables,selected)
 stream=E/(tag+'_rows.jsonl');s=load(E/(tag+'_summary.json'))
 with stream.open() as f:h=json.loads(f.readline())
 indices=list(range(TOTAL)) if h['indices'] is None else h['indices'];assert h==header(indices,dep,startup)
 # Different set-based grid construction plus independent right-before-left recursion.
 expected={(l,l+w,7-(w.bit_length()-1)) for w in (1,2,4,8,16,32,64,128) for l in range(0,25600,w)}
 assert len(expected)==TOTAL and set(map(tuple,nodes))==expected
 def visit(a,b,d):
  yield (a,b,d)
  if d<7:
   mid=(a+b)//2;yield from visit(mid,b,d+1);yield from visit(a,mid,d+1)
 reconstructed=[n for base in range(199,-1,-1) for n in visit(base*128,(base+1)*128,0)]
 assert reconstructed==list(map(tuple,nodes))
 rows=[];previous=digest(h);finished=False
 with stream.open() as f:
  assert json.loads(next(f))==h
  for line in f:
   assert line.endswith('\n') and not finished
   item=json.loads(line)
   if item.get('type')=='footer':
    assert len(rows)==len(indices) and item==footer(rows,previous,h);finished=True
   else:
    slot=len(rows);assert slot<len(indices);index=indices[slot];previous=validate_row(item,slot,index,reconstructed[index],previous,keys,tables,selected);rows.append(item)
 assert finished and s['status']=='COMPUTED_REQUIRES_OUTPUT_AUDIT' and s['footer_read'] is True
 t=totals(rows)
 assert s['cells_complete']==s['planned_cells']==len(rows)==len(indices) and s['totals']==t and s['rows_sha256']==sha(stream)
 assert s['header_sha256']==digest(h) and s['last_chain']==previous and s['source_files']==h['files'] and s['runtime']==h['runtime']
 assert s['restarts_sha256']==sha(E/(tag+'_restarts.jsonl'))
 full=indices==list(range(TOTAL))
 if full:assert t['coefficients_per_engine']==119799000 and t['geometry_per_engine']==357000 and t['distinct_widths']==sorted(tables) and t['old_selected_agreements']==221
 out={'utc':utc(),'status':'PASS_STRUCTURE_REQUIRES_FULL_FRESH_REPLAY','scope':h['scope'],'full_finite':full,'cells_audited':len(rows),'totals':t,'rows_sha256':sha(stream),'summary_sha256':sha(E/(tag+'_summary.json')),'restarts_sha256':sha(E/(tag+'_restarts.jsonl')),'source_files':h['files'],'runtime':h['runtime'],'code_sha256':sha(__file__),'seconds':time.monotonic()-start}
 write_json(E/(tag+'_output_audit.json'),out);print(canon(out),flush=True)
if __name__=='__main__':main()
