"""Corrupt reviewed smoke artifacts and require structural rejection."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,shutil
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];sys.path.insert(0,str(Path(__file__).resolve().parent));import audit_covering as audit
E=B/'research/inner_cells/evidence';tag='assembly_smoke2';assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=E;rows=[json.loads(l) for l in (source/(tag+'_cells.jsonl')).read_text().splitlines()];summary=json.loads((source/(tag+'_summary.json')).read_text());manifest=json.loads((source/(tag+'_manifest.json')).read_text());assert len(rows)==2
results=[]
for test in ['duplicate','gap','negative_weight','L2_understatement','missing_row','partial_as_full','NaN']:
 dest=E/'rejection_fixtures'/test;dest.mkdir(parents=True,exist_ok=True);rr=json.loads(json.dumps(rows));ss=json.loads(json.dumps(summary));mm=json.loads(json.dumps(manifest));smoke=True
 if test=='duplicate':rr[1]=rr[0]
 elif test=='gap':rr[1]['left_exact']='-67/10'
 elif test=='negative_weight':rr[0]['arb']['weighted']['0']['upper_exact']='-1'
 elif test=='L2_understatement':ss['finite_inner_L2_squared_upper_exact']='0'
 elif test=='missing_row':rr.pop()
 elif test=='partial_as_full':ss['status']='COMPUTED_COMPLETE_REQUIRES_OUTPUT_AUDIT';smoke=False
 elif test=='NaN':rr[0]['arb']['W']['upper_exact']=float('nan')
 mp=dest/(tag+'_manifest.json');mp.write_text(json.dumps(mm)+'\n');fp=dest/(tag+'_cells.jsonl');fp.write_text(''.join(json.dumps(r)+'\n' for r in rr));ss['manifest_sha256']=sha(mp);ss['cell_file_sha256']=sha(fp);sp=dest/(tag+'_summary.json');sp.write_text(json.dumps(ss)+'\n');shutil.copyfile(source/'contracts.json',dest/'contracts.json');audit.E=dest
 try:audit.run(tag,smoke=smoke)
 except (AssertionError,ValueError,KeyError) as exc:results.append({'test':test,'status':'REJECTED','error_type':type(exc).__name__,'error':str(exc),'manifest_sha256':sha(mp),'summary_sha256':sha(sp),'cells_sha256':sha(fp)})
 else:raise RuntimeError('invalid fixture accepted: '+test)
audit.E=source
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_REJECTIONS','count':len(results),'auditor_sha256':sha(B/'research/inner_cells/code/audit_covering.py'),'source_sha256':sha(__file__),'fixtures':results};(E/'rejections.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'count':len(results)}))
