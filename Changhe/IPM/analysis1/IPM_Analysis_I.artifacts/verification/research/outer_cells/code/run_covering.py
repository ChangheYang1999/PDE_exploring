"""Joint independent complete exterior covering; no claim before output audit."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,time,hashlib,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];E=B/'research/outer_cells/evidence';sys.path.insert(0,str(Path(__file__).resolve().parent))
import cell_arb as ca
import cell_integer_iv as ci
import tail_l2

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def partition():
 segments=[(F(0),F(1,10),F(1,100)),(F(1,10),F(1,5),F(1,40)),(F(1,5),F(1,2),F(1,20)),(F(1,2),F(5),F(1,10)),(F(5),F(17),F(1,2))];out=[]
 for a,b,h in segments:
  n=(b-a)/h;assert n.denominator==1
  for j in range(int(n)):out.append((a+j*h,a+(j+1)*h))
 assert len(out)==89 and out[0][0]==0 and out[-1][1]==17 and all(a<b and (j==0 or out[j-1][1]==a) for j,(a,b) in enumerate(out));return out

def run(tag,limit=None):
 assert tag.replace('_','').isalnum();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
 paths=['research/outer_cells/PROOF.md','research/outer_cells/code/cell_arb.py','research/outer_cells/code/cell_integer_iv.py','research/outer_cells/code/tail_l2.py','research/outer_cells/code/run_covering.py','research/outer_cells/code/audit_covering.py','research/middle_residual/code/cell_core.py','research/outer_majorant/evidence/verdict.json','research/outer_majorant/evidence/outer_result.json','research/outer_majorant/evidence/exact_outer_coefficients.json'];pins={p:sha(B/p) for p in paths};cells=partition();ad=ca.setup(16);id=ci.setup(16,512);assert ad['old_result_sha256']==id['old_result_sha256'] and ad['coefficient_sha256']==id['coefficient_sha256']
 manifest={'utc':utc(),'status':'PREPARED_EXACT_PARTITION','pins':pins,'old_result_sha256':ad['old_result_sha256'],'coefficient_sha256':ad['coefficient_sha256'],'cells':[[str(a),str(b)] for a,b in cells],'Q':16,'Pint':512,'exact_Green_scalar_checks':id['exact_Green_scalar_checks']};mp=E/(tag+'_manifest.json');assert not mp.exists(),('existing tag',tag);mp.write_text(json.dumps(manifest,indent=2)+'\n');fp=E/(tag+'_cells.jsonl');assert not fp.exists();maxima={};l2sum=F(0);count=0;coefficientchecks=0
 with fp.open('x') as f:
  for index,(a,b) in enumerate(cells):
   if limit is not None and index>=limit:break
   r=ca.bound_cell(ad,a,b,True);s=ci.bound_cell(id,a,b,r);assert s['coefficient_overlap_checks']==17226 and r['max_abs_lambda_h_exact']==s['max_abs_lambda_h_exact']==str(524*(b-a)/2)
   coefficientchecks+=s['coefficient_overlap_checks'];r.pop('coefficients');joint={}
   for key in ['W','W_over_m','L2_squared']:
    joint[key]=str(max(F(x[key]['upper_exact']) for x in [r,s]))
   for delta in ['0','1/2','2888063583571445/9007199254740992']:joint['weighted_'+delta]=str(max(F(x['weighted'][delta]['upper_exact']) for x in [r,s]))
   for key,value in joint.items():
    if key=='L2_squared':l2sum+=F(value)
    elif key not in maxima or F(value)>F(maxima[key]['upper_exact']):maxima[key]={'upper_exact':value,'cell':index,'left_exact':str(a),'right_exact':str(b)}
   row={'cell':index,'left_exact':str(a),'right_exact':str(b),'arb':r,'independent_iv_integer':s,'joint_upper_exact':joint};f.write(json.dumps(row,separators=(',',':'))+'\n');f.flush();count+=1
   progress={'utc':utc(),'status':'RUNNING','cells_complete':count,'cells_required':len(cells),'coefficient_overlap_checks':coefficientchecks,'seconds':time.monotonic()-start,'last_cell_seconds':r['seconds']+s['seconds'],'maxima':maxima};(E/(tag+'_progress.json')).write_text(json.dumps(progress,indent=2)+'\n');print(json.dumps({k:v for k,v in progress.items() if k!='maxima'}),flush=True)
 result={'utc':utc(),'status':'COMPUTED_COMPLETE_REQUIRES_OUTPUT_AUDIT' if count==89 else 'PARTIAL_SMOKE_ONLY','manifest_sha256':sha(mp),'cell_file_sha256':sha(fp),'cells_complete':count,'cells_required':89,'coefficient_overlap_checks':coefficientchecks,'exact_Green_scalar_checks':id['exact_Green_scalar_checks'],'pins':pins,'maxima':maxima,'finite_exterior_L2_squared_upper_exact':str(l2sum),'seconds':time.monotonic()-start}
 if count==89:
  tail=tail_l2.run(F(17));tp=E/(tag+'_tail_l2.json');tp.write_text(json.dumps(tail,indent=2)+'\n');result['tail_l2_sha256']=sha(tp);result['tail_L2_upper_exact']=tail['published_upper_exact'];result['full_exterior_L2_squared_upper_exact']=str(l2sum+F(tail['published_upper_exact'])**2)
 for p,h in pins.items():assert sha(B/p)==h,('source changed during run',p)
 rp=E/(tag+'_summary.json');rp.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':utc(),'status':result['status'],'summary_sha256':sha(rp),'seconds':time.monotonic()-start}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);ap.add_argument('--limit',type=int);args=ap.parse_args();run(args.tag,args.limit)
