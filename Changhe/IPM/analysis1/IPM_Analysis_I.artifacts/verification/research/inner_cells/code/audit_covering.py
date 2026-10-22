"""Independent exact partition/aggregation audit with fresh iv192 weights."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/inner_cells/evidence';iv.dps=192
IV='69923605fab0dad07205705e32b52f26770053cf7392cfd919d1fb2ff415a0fc';OV='9a3d6cdce158574bd532f44c27b83aecb5007c985bdefa35e4f95e4f81dac9d6'
assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bad(x):raise ValueError(('nonfinite',x))
def load(p):return json.loads(Path(p).read_bytes(),parse_constant=bad)
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def rf(t):s,m,e,b=t;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 assert not iv.isnan(x) and not iv.isinf(x);lo,hi=map(rf,x._mpi_);assert lo<=hi;return lo,hi

def up(x):return ends(x)[1]
def interval(v):a,b=F(v['lower_exact']),F(v['upper_exact']);assert 0<=a<=b;return a,b

def run(tag,smoke=False):
 start=time.monotonic();assert tag.replace('_','').isalnum();mp=E/(tag+'_manifest.json');sp=E/(tag+'_summary.json');fp=E/(tag+'_cells.jsonl');m=load(mp);s=load(sp)
 assert s['status']==('PARTIAL_SMOKE_ONLY' if smoke else 'COMPUTED_COMPLETE_REQUIRES_OUTPUT_AUDIT') and s['manifest_sha256']==sha(mp) and s['cell_file_sha256']==sha(fp) and s['pins']==m['pins']
 for p,h in m['pins'].items():assert sha(B/p)==h
 assert sha(__file__)==m['pins']['research/inner_cells/code/audit_covering.py']
 assert m['pins']['research/inner_majorant/evidence/verdict.json']==IV and m['pins']['research/outer_cells/evidence/verdict.json']==OV
 assert m['runtime']['optimize']==0 and m['runtime']['PYTHONOPTIMIZE']=='unset' and m['Q']==16 and m['Pint']==512
 c=load(E/'contracts.json');assert c['status']=='PASS_CONTRACTS' and c['exact_Green_scalar_checks']==m['exact_Green_scalar_checks']==s['exact_Green_scalar_checks']==7845 and c['integral_contract_checks']==m['integral_contract_checks']==s['integral_contract_checks']==7
 for p,h in c['dependency_pins'].items():assert sha(B/p)==h
 v=load(B/'research/inner_majorant/evidence/verdict.json');assert v['status']=='CONFIRMED'
 for p in ['research/inner_majorant/evidence/inner_result.json','research/inner_majorant/evidence/exact_inner_coefficients.json','research/inner_majorant/evidence/inner_iv_audit.json']:assert sha(B/p)==v['files'][p]==m['pins'][p]
 # This formula constructs endpoints independently from the driver's segments.
 ep=[F(-35+j,5) for j in range(26)]+[F(-20+j,10) for j in range(1,20)]+[F(-10+j,100) for j in range(1,11)]
 assert len(ep)==55 and ep[0]==-7 and ep[-1]==0 and all(a<b for a,b in zip(ep,ep[1:]));expected=[[str(a),str(b)] for a,b in zip(ep,ep[1:])];assert expected==m['cells']
 old=load(B/'research/inner_majorant/evidence/inner_result.json');co=load(B/'research/inner_majorant/evidence/exact_inner_coefficients.json');k=F(old['k_exact']);L=F(old['L_exact']);ta=F(co['ta_exact']);assert k==F(1615536043799051,9007199254740992) and L>0
 delta=[F(0),F(1,2),F(1,2)-k];sums=F(0);asums=F(0);maxima={};amax={};count=0;checks=0
 def update(target,values,index,a,b):
  for key,val in values.items():
   if key not in target or val>F(target[key]['upper_exact']):target[key]={'upper_exact':str(val),'cell':index,'left_exact':str(a),'right_exact':str(b)}
 with fp.open() as f:
  for index,line in enumerate(f):
   r=json.loads(line,parse_constant=bad);assert index<54 and r['cell']==index and [r['left_exact'],r['right_exact']]==expected[index];a,b=ep[index],ep[index+1];ar,ir=r['arb'],r['independent_iv_integer'];assert ir['Pint']==512 and ir['coefficient_overlap_checks']==17226 and ir['exact_integer_convolutions']==8
   for x,rate in [(ar,522),(ir,526)]:
    assert [x['left_exact'],x['right_exact']]==expected[index] and F(x['tc_exact'])==(a+b)/2 and F(x['h_exact'])==(b-a)/2 and x['Q']==16 and F(x['max_abs_ODE_lambda_h_exact'])==rate*(b-a)/2
    for key in ['W','W_over_m','L2_squared','retained_Bernstein_sum','discarded_polynomial_remainder','nonpolynomial_remainder']:interval(x[key])
    assert set(x['weighted'])==set(map(str,delta))
    for w in x['weighted'].values():interval(w)
   assert F(ar['W']['upper_exact'])>=sum(F(ar[key]['upper_exact']) for key in ['retained_Bernstein_sum','discarded_polynomial_remainder','nonpolynomial_remainder'])
   assert F(ir['W']['upper_exact'])>=F(ir['retained_Bernstein_sum_exact'])+F(ir['discarded_polynomial_remainder_exact'])+F(ir['nonpolynomial_remainder']['upper_exact'])
   assert F(ir['retained_Bernstein_sum_exact'])>=0 and F(ir['discarded_polynomial_remainder_exact'])>=0
   joint={key:max(F(x[key]['upper_exact']) for x in [ar,ir]) for key in ['W','W_over_m','L2_squared']}
   for d in delta:joint['weighted_'+str(d)]=max(F(x['weighted'][str(d)]['upper_exact']) for x in [ar,ir])
   assert {key:str(val) for key,val in joint.items()}==r['joint_upper_exact'];sums+=joint.pop('L2_squared');update(maxima,joint,index,a,b)
   W=iq(joint['W']);ul=iv.exp(iq(ta+a))/iq(L);ur=iv.exp(iq(ta+b))/iq(L);ml=iv.exp(3*iv.log(ul)+iq((k-3)/2)*iv.log1p(ul*ul));assert ends(ml)[0]>0;wm=W/ml
   fresh={'W':joint['W'],'W_over_m':up(wm)}
   for d in delta:fresh['weighted_'+str(d)]=up(wm*iv.exp(iq(d)*iv.log1p(ur)))
   a2=up(iv.pi*wm**2*iq(L*L/2)*(iv.log1p(ur*ur)-iv.log1p(ul*ul)));assert a2>=0;asums+=a2;update(amax,fresh,index,a,b);count+=1;checks+=17226
 assert count==s['cells_complete'] and s['cells_required']==54 and (0<count<54 if smoke else count==54) and checks==s['coefficient_overlap_checks'] and sums==F(s['finite_inner_L2_squared_upper_exact']) and maxima==s['maxima']
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PARTIAL_SMOKE' if smoke else 'PASS_COMPLETE_REQUIRES_FINAL_REVIEW','source_sha256':sha(__file__),'manifest_sha256':sha(mp),'summary_sha256':sha(sp),'cell_file_sha256':sha(fp),'pins':m['pins'],'cells_checked':count,'coefficient_overlap_checks':checks,'exact_Green_scalar_checks':7845,'integral_contract_checks':7,'finite_inner_maxima':amax,'finite_inner_L2_squared_upper_exact':str(asums),'runtime':{'pid':os.getpid(),'executable':sys.executable,'optimize':sys.flags.optimize,'PYTHONOPTIMIZE':os.environ.get('PYTHONOPTIMIZE','unset')},'iv_dps':192}
 if not smoke:
  tp=E/(tag+'_tail.json');assert sha(tp)==s['tail_sha256'];t=load(tp);assert t['status']=='PASS_REQUIRES_SOURCE_REVIEW' and t['T_exact']=='7' and t['base_majorant_T_exact']=='5/2' and t['inner_verdict_sha256']==IV and t['source_sha256']==sha(B/'research/inner_cells/code/tail_disk.py') and t['proof_sha256']==m['pins']['research/inner_cells/PROOF.md'] and t['overlap_checks']==6
  for p,h in t['dependency_pins'].items():assert sha(B/p)==h==v['files'][p]
  base=max(F(next(q for q in load(B/p)['cases'] if q['T_exact']=='5/2')['values']['B5']['upper_exact']) for p in ['research/inner_majorant/evidence/inner_result.json','research/inner_majorant/evidence/inner_iv_audit.json']);assert base==F(t['B5_upper_exact'])
  assert t['ta_exact']==str(ta) and t['k_exact']==str(k) and t['L_exact']==str(L)
  for key,row in t['values'].items():
   aa=interval(row['arb']);ii=interval(row['iv']);assert max(aa[0],ii[0])<=min(aa[1],ii[1]) and F(row['upper_exact'])==max(aa[1],ii[1])
  assert set(t['values'])==set(amax)|{'L2_squared'}
  whole={key:{'upper_exact':str(max(F(arow['upper_exact']),F(maxima[key]['upper_exact']),F(t['values'][key]['upper_exact']))),'finite_audit':arow,'finite_driver':maxima[key],'tail_upper_exact':t['values'][key]['upper_exact']} for key,arow in amax.items()}
  tail=F(t['values']['L2_squared']['upper_exact']);assert tail==F(s['tail_L2_squared_upper_exact']) and sums+tail==F(s['full_inner_L2_squared_upper_exact']);total=max(sums,asums)+tail
  result.update(full_inner_maxima=whole,tail_L2_squared_upper_exact=str(tail),full_inner_L2_squared_upper_exact=str(total),full_inner_L2_upper_exact=str(up(iv.sqrt(iq(total)))),tail_sha256=sha(tp))
 result['seconds']=time.monotonic()-start;(E/(tag+'_audit.json')).open('x').write(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k in ['utc','status','cells_checked','coefficient_overlap_checks','seconds']}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);ap.add_argument('--smoke',action='store_true');args=ap.parse_args();run(args.tag,args.smoke)
