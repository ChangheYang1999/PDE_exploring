"""Independent exact endpoint audit of the two exterior-flow upper bounds."""
import json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/exterior_flow/evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for q in iter(lambda:f.read(1<<20),b''):h.update(q)
 return h.hexdigest()
def main():
 rp=E/'checks.json';r=json.loads(rp.read_text());assert r['status']=='PASS_COMPUTATION_REQUIRES_ADVERSARIAL_AUDIT'
 assert r['source_sha256']==sha(B/'research/exterior_flow/code/check_tail.py') and r['proof_sha256']==sha(B/'research/exterior_flow/PROOF.md')
 for p,h in r['dependencies_sha256'].items():assert sha(B/p)==h
 assert r['runtime']=={'python_flint':'0.9.0','mpmath':'1.3.0','arb_bits':512,'iv_decimal_digits':180,'endpoint_rational_contracts':5,'nonfinite_rejections':3}
 c=r['checks'];assert c=={'exact_affine_identities':17748,'velocity_coefficient_overlaps':8874,'boundary_overlaps':261,'density_ode_coefficients':8874,'angular_Laurent_identities':261,'radius_overlaps':6,'minimum_abs_denominator_exact':'929519035745737/9007199254740992'}
 k=F(r['parameters_exact']['k']);cl=1/k;om=1-k;assert F(r['parameters_exact']['cl'])==cl and F(r['parameters_exact']['omega'])==om and om>0
 assert [F(x['T_exact']) for x in r['cases']]==list(map(F,['0','1/16','1/8','1/4','1','9']))
 rows={F(x['T_exact']):x for x in r['cases']};comparisons=[]
 def lo(x):q=F(x['lower_exact']);assert q<=F(x['upper_exact']);return q
 def hi(x):lo(x);return F(x['upper_exact'])
 for x in rows.values():
  p=max(hi(x['P_arb']),hi(x['P_iv']));q=max(hi(x['Q_arb']),hi(x['Q_iv']));assert p==F(x['joint_P_upper_exact']) and q==F(x['joint_Q_upper_exact']) and 0<=p<=q
  assert cl-p==F(x['radial_drift_lower_exact']) and cl-q==F(x['both_component_drift_lower_exact'])
  assert max(lo(x['radius_arb']),lo(x['radius_iv']))<=min(hi(x['radius_arb']),hi(x['radius_iv']))
 for T,key,value in [(F(1,16),'P',F('1.744311')),(F(1,16),'radius',F(3634)),(F(1,8),'P',F('0.104')),(F(1,8),'Q',F('0.313')),(F(1,8),'radius',F(4000))]:
  x=rows[T]
  for method in ['arb','iv']:
   got=hi(x[key+'_'+method]);assert got<value;comparisons.append({'T_exact':str(T),'quantity':key,'method':method,'upper_exact':str(got),'strict_public_upper_exact':str(value)})
 for T,key,value in [(F(1,16),'radial_drift_lower_exact',F('3.83')),(F(1,8),'radial_drift_lower_exact',F('5.47')),(F(1,8),'both_component_drift_lower_exact',F('5.26'))]:
  got=F(rows[T][key]);assert got>value;comparisons.append({'T_exact':str(T),'quantity':key,'joint_lower_exact':str(got),'strict_public_lower_exact':str(value)})
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'checks_sha256':sha(rp),'proof_sha256':r['proof_sha256'],'comparison_count':len(comparisons),'comparisons':comparisons,'public_conclusions':{'radial_drift':{'radius':'3634','strict_lower_coefficient':'3.83'},'axis_quotients':{'radius':'4000','P_strict_upper':'0.104','Q_strict_upper':'0.313','decay_exponent_exact':str(om),'radial_drift_strict_lower':'5.47','component_drift_strict_lower':'5.26'}},'scope':'Saved finite interval bounds and exact public rounding only; does not re-execute the coefficient recurrence or certify the bounded interior.'}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='comparisons'}),flush=True)
if __name__=='__main__':main()
