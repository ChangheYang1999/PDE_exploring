"""Complete inner annulus, both interval constructions on every rational cell."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,time,hashlib,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];E=B/'research/inner_cells/evidence';sys.path.insert(0,str(Path(__file__).resolve().parent))
import cell_arb as ca
import cell_integer_iv as ci
import tail_disk
assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def partition():
 cells=[]
 for a,b,h in [(F(-7),F(-2),F(1,5)),(F(-2),F(-1,10),F(1,10)),(F(-1,10),F(0),F(1,100))]:
  n=(b-a)/h;assert n.denominator==1
  cells.extend((a+j*h,a+(j+1)*h) for j in range(int(n)))
 assert len(cells)==54 and cells[0][0]==-7 and cells[-1][1]==0 and all(a<b and (j==0 or cells[j-1][1]==a) for j,(a,b) in enumerate(cells));return cells

def run(tag,limit=None):
 assert tag.replace('_','').isalnum();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
 paths=['research/inner_cells/'+p for p in ['PROOF.md','code/cell_arb.py','code/cell_integer_iv.py','code/tail_disk.py','code/run_covering.py','code/audit_covering.py','code/check_contracts.py','evidence/contracts.json']]+['research/middle_residual/code/cell_core.py','research/inner_majorant/evidence/verdict.json','research/inner_majorant/evidence/inner_result.json','research/inner_majorant/evidence/inner_iv_audit.json','research/inner_majorant/evidence/exact_inner_coefficients.json','research/outer_cells/evidence/verdict.json','research/outer_cells/PROOF.md']
 pins={p:sha(B/p) for p in paths};contracts=json.loads((E/'contracts.json').read_text());assert contracts['status']=='PASS_CONTRACTS' and contracts['exact_Green_scalar_checks']==7845 and contracts['integral_contract_checks']==7
 for p,h in contracts['dependency_pins'].items():assert sha(B/p)==h
 ad=ca.setup();id=ci.setup();cells=partition();manifest={'utc':utc(),'status':'PREPARED_EXACT_PARTITION','pins':pins,'cells':[[str(a),str(b)] for a,b in cells],'Q':16,'Pint':512,'exact_Green_scalar_checks':7845,'integral_contract_checks':7,'runtime':{'pid':os.getpid(),'argv':sys.argv,'executable':sys.executable,'optimize':sys.flags.optimize,'PYTHONOPTIMIZE':os.environ.get('PYTHONOPTIMIZE','unset'),'python':sys.version}}
 mp=E/(tag+'_manifest.json');assert not mp.exists();mp.write_text(json.dumps(manifest,indent=2)+'\n');fp=E/(tag+'_cells.jsonl');assert not fp.exists();maxima={};l2=F(0);count=0;checks=0
 with fp.open('x') as f:
  for index,(a,b) in enumerate(cells):
   if limit is not None and index>=limit:break
   ar=ca.bound_cell(ad,a,b,True);ir=ci.bound_cell(id,a,b,ar);assert ir['coefficient_overlap_checks']==17226 and ar['max_abs_ODE_lambda_h_exact']==str(261*(b-a)) and ir['max_abs_ODE_lambda_h_exact']==str(263*(b-a));checks+=17226;ar.pop('coefficients');joint={key:str(max(F(r[key]['upper_exact']) for r in [ar,ir])) for key in ['W','W_over_m','L2_squared']}
   for delta in ['0','1/2','2888063583571445/9007199254740992']:joint['weighted_'+delta]=str(max(F(r['weighted'][delta]['upper_exact']) for r in [ar,ir]))
   for key,val in joint.items():
    if key=='L2_squared':l2+=F(val)
    elif key not in maxima or F(val)>F(maxima[key]['upper_exact']):maxima[key]={'upper_exact':val,'cell':index,'left_exact':str(a),'right_exact':str(b)}
   f.write(json.dumps({'cell':index,'left_exact':str(a),'right_exact':str(b),'arb':ar,'independent_iv_integer':ir,'joint_upper_exact':joint},separators=(',',':'))+'\n');f.flush();count+=1
   prog={'utc':utc(),'status':'RUNNING_NON_EVIDENCE_PROGRESS','cells_complete':count,'cells_required':54,'coefficient_overlap_checks':checks,'seconds':time.monotonic()-start,'last_cell_seconds':ar['seconds']+ir['seconds'],'maxima':maxima};(E/(tag+'_progress.json')).write_text(json.dumps(prog,indent=2)+'\n');print(json.dumps({k:v for k,v in prog.items() if k!='maxima'}),flush=True)
 result={'utc':utc(),'status':'COMPUTED_COMPLETE_REQUIRES_OUTPUT_AUDIT' if count==54 else 'PARTIAL_SMOKE_ONLY','manifest_sha256':sha(mp),'cell_file_sha256':sha(fp),'cells_complete':count,'cells_required':54,'coefficient_overlap_checks':checks,'exact_Green_scalar_checks':7845,'integral_contract_checks':7,'pins':pins,'maxima':maxima,'finite_inner_L2_squared_upper_exact':str(l2),'seconds':time.monotonic()-start}
 if count==54:
  t=tail_disk.run(F(7));tp=E/(tag+'_tail.json');tp.open('x').write(json.dumps(t,indent=2)+'\n');result['tail_sha256']=sha(tp);result['tail_L2_squared_upper_exact']=t['values']['L2_squared']['upper_exact'];result['full_inner_L2_squared_upper_exact']=str(l2+F(result['tail_L2_squared_upper_exact']))
 for p,h in pins.items():assert sha(B/p)==h,('source changed during run',p)
 (E/(tag+'_summary.json')).open('x').write(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':utc(),'status':result['status'],'seconds':time.monotonic()-start}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);ap.add_argument('--limit',type=int);args=ap.parse_args();run(args.tag,args.limit)
