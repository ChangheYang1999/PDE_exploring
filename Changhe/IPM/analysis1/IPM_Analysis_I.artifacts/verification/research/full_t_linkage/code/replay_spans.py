"""Fresh same-engine whole-span replay, separately labelled diagnostic."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from datetime import datetime,timezone
from time import monotonic
import argparse,gzip,hashlib,json,resource,sys
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
import check_coefficients as c

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full');args=ap.parse_args();assert args.tag.replace('_','').isalnum();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=monotonic()
 summary=c.load(c.E/(args.tag+'_summary.json'));audit=c.load(c.E/(args.tag+'_output_audit.json'));output=c.E/(args.tag+'_spans.jsonl')
 assert audit['status'] in ('PASS_FULL_OUTPUT_AND_EXACT_NEWTON_AUDIT','OPEN_PARTIAL_AUDIT_PASSED') and audit['output_sha256']==summary['output_sha256']==c.sha(output)
 assert audit['producer_sha256']==summary['source_sha256']==c.sha(c.D/'code/check_coefficients.py') and audit['source_sha256']==c.sha(c.D/'code/audit_coefficients.py')
 with output.open() as f:records=[c.strict_json(line) for line in f]
 header,*rows,footer=records;assert footer['type']=='complete';original={r['span']:r for r in rows};assert len(original)==len(rows)
 paths,pins,knots,S,nonempty,parts=c.inspect_inputs();assert pins==header['files']
 selected=header['selected_spans'];wanted={selected[0],selected[-1]}|set(audit['replay_required_spans'])
 for j in range(2):
  raw=hashlib.sha256((header['sample_seed']+':whole-span:'+str(j)).encode()).digest();wanted.add(selected[int.from_bytes(raw[:8],'big')%len(selected)])
 assert wanted<=set(selected)
 with np.load(header['green_path'],allow_pickle=False) as g:arrays={k:g[k] for k in ('T_mid','T_rad','tb','tb_rad','parent')}
 assert c.sha(header['green_path'])==c.GREEN_SHA;seed,sample=c.sample_triples();assert seed==header['sample_seed'];results=[]
 with gzip.open(paths['archive'],'rt') as f:
  ah=c.strict_json(next(f));assert ah['type']=='header';last=-1
  for line in f:
   rec=c.strict_json(line)
   if rec['type']=='complete':assert last==1557 and rec['spans']==1558 and rec['cells']==7809 and not f.read();break
   assert rec['span']==last+1;last+=1
   if last in wanted:
    fresh=c.calculate_span(rec,parts[last],knots,S,nonempty[last][0],arrays,sample);old=original[last]
    for key in ('stream_sha256','H_stream_sha256','counts','worst_margins','selected_records'):assert fresh[key]==old[key],(last,key)
    results.append({'span':last,'stream_sha256':fresh['stream_sha256'],'H_stream_sha256':fresh['H_stream_sha256'],'counts':fresh['counts']})
   if last>=max(wanted) and max(wanted)<1557:break
 assert {r['span'] for r in results}==wanted
 result={'utc':c.utc(),'status':'PASS_DIAGNOSTIC_WHOLE_SPAN_REPLAY','full_input_run':header['full_run'],'spans_replayed':results,'mandatory_restart_spans':audit['replay_required_spans'],'source_sha256':c.sha(Path(__file__)),'producer_sha256':c.sha(c.D/'code/check_coefficients.py'),'auditor_sha256':c.sha(c.D/'code/audit_coefficients.py'),'input_stream_sha256':c.sha(output),'seconds':monotonic()-start,'scope':'Complete same-producer replay with fresh data; not a third complete independent reconstruction or a final verdict.'};(c.E/(args.tag+'_replay.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
