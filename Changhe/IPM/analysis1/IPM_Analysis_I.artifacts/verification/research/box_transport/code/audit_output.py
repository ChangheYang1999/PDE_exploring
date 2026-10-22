"""Exact independent saved-output audit, including a direct factorial-series check."""
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/box_transport/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bounds(x):l,h=F(x['lower_exact']),F(x['upper_exact']);assert l<=h;return l,h
def main():
 r=json.loads((E/'checks.json').read_text());assert r['status']=='PASS_CONDITIONAL_CONSTANTS'
 assert r['source_sha256']==sha(B/'research/box_transport/code/check_constants.py') and r['proof_sha256']==sha(B/'research/box_transport/PROOF.md') and r['lead_snapshot_sha256']==sha(E/'lead_global_flow_v2.md')
 assert r['box_exact']=={'x_lower':'24/5','x_upper':'341/50','y_upper':'57/20','negative_speed':'13','inside_T_upper':'123/100','outside_T_upper':'-11/50','residence_upper':'101/650'}
 assert r['runtime']=={'python_flint':'0.9.0','mpmath':'1.3.0','arb_bits':512,'iv_decimal_digits':180}
 assert r['checks']=={'endpoint_containments':10,'nonfinite_rejections':3,'exponential_overlaps':2,'public_two_sided_enclosures':4,'semigroup_factor_identities':48,'overlapping_history_segment_inequalities':252}
 assert [x['kappa_exact'] for x in r['rows']]==['1/5','11/50'];checks=0
 exact_rows=[]
 for row,pl,ph in zip(r['rows'],[F('6.244'),F('5.694')],[F('6.245'),F('5.695')]):
  kap=F(row['kappa_exact']);cost=(F(123,100)+kap)*F(101,650);assert cost==F(row['K_exact']) and 2*cost==F(row['C_upper_exact'])
  s=row['series'];N=s['degree'];assert N==128 and F(s['argument_exact'])==cost
  total=sum(cost**j/F(math.factorial(j)) for j in range(N+1));ratio=cost/(N+2);tail=cost**(N+1)/F(math.factorial(N+1))/(1-ratio)
  assert total==F(s['sum_exact']) and tail==F(s['tail_majorant_exact']) and ratio==F(s['maximum_tail_ratio_exact']) and 0<ratio<1
  sl,sh=total/kap,(total+tail)/kap;assert list(map(F,row['exact_series_scaled_interval']))==[sl,sh]
  bs=[bounds(row[m]) for m in ['arb','iv']]
  for l,h in bs:assert pl<l<=sl<=sh<=h<ph;checks+=1
  joint=[min(x[0] for x in bs),max(x[1] for x in bs)];assert joint==list(map(F,row['joint_enclosure']))
  exact_rows.append({'kappa_exact':str(kap),'strict_public_lower':str(pl),'strict_public_upper':str(ph)})
 assert F(r['allowed_kappa_upper_exact'])==F(11,50) and F(r['log_bound_derivative_upper_exact'])==F(101,650)-F(50,11)<0
 assert len(r['public_comparisons'])==4
 expected=[{'kappa_exact':row['kappa_exact'],'method':m,'strict_public_lower_exact':lo,'strict_public_upper_exact':hi} for row,lo,hi in zip(r['rows'],['1561/250','2847/500'],['1249/200','1139/200']) for m in ['arb','iv']]
 assert r['public_comparisons']==expected
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'checks_sha256':sha(E/'checks.json'),'proof_sha256':r['proof_sha256'],'two_sided_checks':checks,'public_bounds':exact_rows,'verdicts':{'lead_enlarged_box_bound_expression_le_6_2':'REFUTED','same_hypotheses_conditional_inverse_lt_5_695_at_kappa_11_50':'CONFIRMED_CONDITIONAL','actual_trial_box_and_complement_inequalities':'OPEN'},'scope':'Self-contained exact rational factorial-series and geometric-tail certificate for the two scalar expressions. Saved Arb/iv endpoints and source hashes are checked, but their core execution is not repeated here; the execution claim is separately bound by the completed-run record.'}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
