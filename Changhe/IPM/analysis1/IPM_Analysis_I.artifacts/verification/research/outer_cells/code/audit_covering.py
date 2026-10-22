"""Independent exact coverage, provenance, aggregation and iv192 weight audit."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,argparse,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/outer_cells/evidence';iv.dps=192
OV='7857fb1b2347ec5ec1e1206db7272c5144d903b0209f23e2a5d46cad9664d1ac'
CORE='a7679c9586f83e203d09fe3f8028e150f7da41082d769fa495840a82be71fdc1'
LV='6a56059e5b9e2041ad94aed5be982b19b94d0b23f0c00563a20452b314ba89f9'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bad(x):raise ValueError(('nonfinite JSON constant',x))
def load(p):return json.loads(Path(p).read_bytes(),parse_constant=bad)
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def rf(t):s,m,e,b=t;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 assert not iv.isnan(x) and not iv.isinf(x);a,b=map(rf,x._mpi_);assert a<=b;return a,b
def up(x):return ends(x)[1]
def endpoints():
 r=[F(j,100) for j in range(11)]+[F(j,40) for j in range(5,9)]+[F(j,20) for j in range(5,11)]+[F(j,10) for j in range(6,51)]+[F(j,2) for j in range(11,35)]
 assert len(r)==90 and r[0]==0 and r[-1]==17 and all(a<b for a,b in zip(r,r[1:]));return r

def run(tag,smoke=False):
 assert tag.replace('_','').isalnum();start=time.monotonic();rp=E/(tag+'_summary.json');mp=E/(tag+'_manifest.json');fp=E/(tag+'_cells.jsonl');res=load(rp);man=load(mp)
 assert res['status']==('PARTIAL_SMOKE_ONLY' if smoke else 'COMPUTED_COMPLETE_REQUIRES_OUTPUT_AUDIT')
 assert res['manifest_sha256']==sha(mp) and res['cell_file_sha256']==sha(fp);assert res['pins']==man['pins']
 for p,h in res['pins'].items():assert sha(B/p)==h,('source changed',p)
 assert res['pins']['research/middle_residual/code/cell_core.py']==CORE and res['pins']['research/outer_majorant/evidence/verdict.json']==OV
 ovp=B/'research/outer_majorant/evidence/verdict.json';assert sha(ovp)==OV;ov=load(ovp);assert ov['status']=='CONFIRMED'
 for dep in ['research/outer_majorant/evidence/outer_result.json','research/outer_majorant/evidence/exact_outer_coefficients.json']:assert sha(B/dep)==ov['files'][dep]==res['pins'][dep]
 assert man['Q']==16 and man['Pint']==512 and man['exact_Green_scalar_checks']==res['exact_Green_scalar_checks']==17748
 ep=endpoints();expected=[[str(a),str(b)] for a,b in zip(ep,ep[1:])];assert man['cells']==expected
 old=load(B/'research/outer_majorant/evidence/outer_result.json');assert sha(B/'research/outer_majorant/evidence/outer_result.json')==man['old_result_sha256'];assert sha(B/'research/outer_majorant/evidence/exact_outer_coefficients.json')==man['coefficient_sha256']
 k=F(old['scalars_exact']['k']);L=F(old['scalars_exact']['L']);tb=F(old['tb_exact']);assert k==F(1615536043799051,9007199254740992) and L>0
 def interval(row):
  lo,hi=F(row['lower_exact']),F(row['upper_exact']);assert 0<=lo<=hi;return lo,hi
 sums=F(0);maxima={};audit_sums=F(0);audit_maxima={};count=0;checks=0
 with fp.open() as f:
  for index,line in enumerate(f):
   row=json.loads(line,parse_constant=bad);assert index<89 and row['cell']==index and [row['left_exact'],row['right_exact']]==expected[index];a,b=ep[index],ep[index+1]
   ar=row['arb'];ir=row['independent_iv_integer'];assert ir['Pint']==512 and ir['coefficient_overlap_checks']==17226 and ir['exact_integer_convolutions']==8
   for c in [ar,ir]:
    assert [c['left_exact'],c['right_exact']]==expected[index] and c['tc_exact']==str((a+b)/2) and c['h_exact']==str((b-a)/2) and c['Q']==16 and c['max_abs_lambda_h_exact']==str(262*(b-a))
    for key in ['W','W_over_m','L2_squared','retained_Bernstein_sum','discarded_polynomial_remainder','nonpolynomial_remainder']:interval(c[key])
    assert set(c['weighted'])=={'0','1/2',str(F(1,2)-k)}
    for val in c['weighted'].values():interval(val)
   apoly=F(ar['retained_Bernstein_sum']['upper_exact']);ahigh=F(ar['discarded_polynomial_remainder']['upper_exact']);arem=F(ar['nonpolynomial_remainder']['upper_exact']);assert F(ar['W']['upper_exact'])>=apoly+ahigh+arem
   ipoly=F(ir['retained_Bernstein_sum_exact']);ihigh=F(ir['discarded_polynomial_remainder_exact']);irem=F(ir['nonpolynomial_remainder']['upper_exact']);assert 0<=ipoly and 0<=ihigh and F(ir['W']['upper_exact'])>=ipoly+ihigh+irem
   for key,v in [('retained_Bernstein_sum',ipoly),('discarded_polynomial_remainder',ihigh)]:
    lo,hi=interval(ir[key]);assert lo<=v<=hi
   vals={key:max(F(c[key]['upper_exact']) for c in [ar,ir]) for key in ['W','W_over_m','L2_squared']}
   vals.update({'weighted_'+delta:max(F(c['weighted'][delta]['upper_exact']) for c in [ar,ir]) for delta in ar['weighted']});assert row['joint_upper_exact']=={key:str(value) for key,value in vals.items()}
   sums+=vals['L2_squared']
   for key,value in vals.items():
    if key!='L2_squared' and (key not in maxima or value>F(maxima[key]['upper_exact'])):maxima[key]={'upper_exact':str(value),'cell':index,'left_exact':str(a),'right_exact':str(b)}
   # New scalar bounds from the larger common W, without importing either W/m.
   W=iq(vals['W']);ul=iv.exp(iq(tb+a))/iq(L);ur=iv.exp(iq(tb+b))/iq(L);m=iv.exp(3*iv.log(ul)+iq((k-3)/2)*iv.log(1+ul*ul));assert ends(m)[0]>0;wm=W/m
   anew={'W':vals['W'],'W_over_m':up(wm)}
   for delta in [F(0),F(1,2),F(1,2)-k]:anew['weighted_'+str(delta)]=up(wm*iv.exp(iq(delta)*iv.log(1+ur)))
   a2=up(iv.pi*wm*wm*iq(L*L/2)*(iv.log(1+ur*ur)-iv.log(1+ul*ul)));assert a2>=0;audit_sums+=a2
   for key,value in anew.items():
    if key not in audit_maxima or value>F(audit_maxima[key]['upper_exact']):audit_maxima[key]={'upper_exact':str(value),'cell':index,'left_exact':str(a),'right_exact':str(b)}
   count+=1;checks+=ir['coefficient_overlap_checks']
 assert count==res['cells_complete'] and res['cells_required']==89 and (0<count<89 if smoke else count==89)
 assert checks==res['coefficient_overlap_checks']==17226*count and sums==F(res['finite_exterior_L2_squared_upper_exact']) and maxima==res['maxima']
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PARTIAL_SMOKE' if smoke else 'PASS_COMPLETE_REQUIRES_FINAL_REVIEW','source_sha256':sha(__file__),'summary_sha256':sha(rp),'manifest_sha256':sha(mp),'cell_file_sha256':sha(fp),'pins':res['pins'],'cells_checked':count,'coefficient_overlap_checks':checks,'exact_Green_scalar_checks':17748,'iv_dps':iv.dps,'finite_exterior_maxima':audit_maxima,'finite_exterior_L2_squared_upper_exact':str(audit_sums)}
 if not smoke:
  vp=B/'research/outer_leading_cancellation/evidence/verdict.json';assert sha(vp)==LV;v=load(vp);assert v['status']=='CONFIRMED';lp=B/'research/outer_leading_cancellation/evidence/leading_result.json';li=B/'research/outer_leading_cancellation/evidence/leading_iv_audit.json'
  for p in [lp,li]:assert sha(p)==v['files'][str(p.relative_to(B))]
  cases=[next(c for c in load(p)['cases'] if c['T_exact']=='17')['values'] for p in [lp,li]]
  mapping={'W':'absolute_W','W_over_m':'weighted_delta_0','weighted_0':'weighted_delta_0','weighted_1/2':'weighted_delta_1/2','weighted_'+str(F(1,2)-k):'weighted_delta_'+str(F(1,2)-k)}
  whole={}
  for key,tailkey in mapping.items():
   tail=max(F(c[tailkey]['upper_exact']) for c in cases);finite=F(audit_maxima[key]['upper_exact']);whole[key]={'upper_exact':str(max(tail,finite)),'where':'tail_tau_ge_17' if tail>finite else audit_maxima[key]}
  tp=E/(tag+'_tail_l2.json');assert sha(tp)==res['tail_l2_sha256'];t=load(tp);assert t['status']=='PASS_REQUIRES_SOURCE_REVIEW' and t['T_exact']=='17' and t['leading_verdict_sha256']==LV and t['moment_overlap_checks']==3508
  assert t['source_sha256']==sha(B/'research/outer_cells/code/tail_l2.py') and t['proof_sha256']==sha(B/'research/outer_cells/PROOF.md');assert t['leading_result_sha256']==sha(lp) and t['outer_result_sha256']==man['old_result_sha256']
  tails=[interval(t[key]) for key in ['arb_L2_bound','iv_L2_bound']];assert max(x[0] for x in tails)<=min(x[1] for x in tails);tail=max(x[1] for x in tails);assert tail==F(t['published_upper_exact'])==F(res['tail_L2_upper_exact'])
  assert sums+tail*tail==F(res['full_exterior_L2_squared_upper_exact']);total=max(audit_sums,sums)+tail*tail
  result.update(full_exterior_maxima=whole,tail_L2_upper_exact=str(tail),full_exterior_L2_squared_upper_exact=str(total),full_exterior_L2_upper_exact=str(up(iv.sqrt(iq(total)))),tail_l2_sha256=sha(tp),leading_verdict_sha256=LV)
 result['seconds']=time.monotonic()-start;(E/(tag+'_audit.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':result['utc'],'status':result['status'],'cells':count,'coefficient_checks':checks,'seconds':result['seconds']}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);ap.add_argument('--smoke',action='store_true');args=ap.parse_args();run(args.tag,args.smoke)
