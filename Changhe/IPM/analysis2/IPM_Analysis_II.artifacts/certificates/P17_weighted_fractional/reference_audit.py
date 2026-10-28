"""Bind the weighted reference contract to previously audited exact certificates."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[2]
load=lambda r:json.loads((root/r).read_text())
hashfile=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=load('source_audit/state131_exact.json')
canonical=source['canonical_serialization_sha256']
assert canonical=='4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01'
e={k:Q(v) for k,v in source['exact_parameters'].items()}
assert Q(9,5)<e['cl']<Q(37,20) and e['a0']>1
assert e['cl']+e['strain']==1
assert e['gamma']==1/e['cl'] and Q(1,5)<e['gamma']<1
assert e['residual_leading_power']==2*e['gamma']-1
assert 0<e['residual_leading_power']<Q(1,5)
mat=load('02_energy/verification/compact_certificate_audit.json')
assert mat['verdict']=='CONFIRMED'
mat131=next(v for v in mat['states'] if v['state']==131)
assert mat131['input_sha256']==canonical and mat131['minimum_claim']=='19/5'
aux=load('02_energy/verification/auxiliary_certificate_audit.json')
assert aux['verdict']=='CONFIRMED'
a131=next(v for v in aux['records'] if v['state']==131)
assert a131['derivative_bounds']['G']==11 and Q(a131['derivative_bounds']['J'])==Q(7,5)
assert 2*11**2<16**2 and 4*Q(7,5)**2==Q(14,5)**2
assert a131['coefficient_file_sha256']==hashfile(root/'02_energy/verification/state131_coefficient_bounds.json')
hi=load('07_weighted/verification/high_symbol_certificate_audit.json')
assert hi['verdict']=='CONFIRMED' and hi['source_sha256']==canonical
for k,r,leaves in [(1,'1',131),(2,'1/2',201)]:
 h=next(v for v in hi['results'] if v['k']==k)
 assert h['radius']==r and h['sigma']=='1/5' and h['target']=='1/2' and h['leaves']==leaves
 assert h['certificate_sha256']==hashfile(root/f'07_weighted/verification/state131_high_symbol_k{k}_adaptive.json')
sharp=load('07_weighted/verification/sharp_coefficient_audit.json')
assert sharp['verdict']=='CONFIRMED' and sharp['source_sha256']==canonical
for k,v in {'rho2':'3','rho2_weighted':'8','rho3_weighted':'32','u2_weighted':'3'}.items():assert sharp['targets'][k]==v
assert sharp['certificate_sha256']==hashfile(root/'07_weighted/verification/sharp_coefficient_certificate.json')
assert sharp['polynomial_sha256']==hashfile(root/'07_weighted/verification/sharp_coefficient_polynomials.json')
r2=load('07_weighted/verification/r2_extra_audit.json')
assert r2['status']=='CONFIRMED' and r2['source_sha256']==canonical
assert r2['safe_power_two_bounds']=={'r2_rho4':512,'r1_u3':16}
assert len(r2['leaves'])==315
for k,v in r2['input_hashes'].items():assert v==hashfile(root/'07_weighted/verification'/k)
rad=load('07_weighted/verification/radial_commutator_constants.json')
assert rad['status']=='CONFIRMED' and rad['state131_source_sha256']==canonical
assert rad['state131_global_upper_bounds']=={'C_rho':152,'C_U':18,'C_DU':18,'C_D2U':45}
radrow=next(v for v in rad['rows'] if v['s']=='11/5')
assert Q(radrow['rational_margin_lower'])>Q(1,5) and radrow['R']=='2^35'
gap=load('16_weighted_fractional/verification/state131_weighted_gap.json')
assert gap['verdict']=='CONFIRMED' and gap['canonical_sha256']==canonical
arith=load('16_weighted_fractional/verification/sharp_weighted_constants.json')
assert arith['status']=='ARITHMETIC_PASS' and arith['proof_audit']=='CONFIRMED V080-V081'
for rel,v in arith['dependencies'].items():assert hashfile(root/rel)==v
proofs=['16_weighted_fractional/REFERENCE_AUDIT.md','16_weighted_fractional/PROOF.md','16_weighted_fractional/ROUGH_INVERSE_PROOF.md','16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md','16_weighted_fractional/SHARP_ROUGH_INVERSE_PROOF.md','16_weighted_fractional/RESIDUAL_GAP_PROOF.md','01_operator/PROOF.md','05_tails/PROOF.md','07_weighted/SHARP_WEIGHTED_H2_PROOF.md','07_weighted/RADIAL_COMMUTATOR_PROOF.md','07_weighted/LOW_INVERSE_FAMILY_PROOF.md','07_weighted/LOW_INVERSE_PROOF.md','07_weighted/HIGH_SYMBOL_CERTIFICATE_PROOF.md','07_weighted/SHARP_COEFFICIENT_PROOF.md','07_weighted/R2_DERIVATIVE_PROOF.md','14_homogeneous_weight/REGULARIZED_PROOF.md','02_energy/COMPACT_CERTIFICATE_PROOF.md','02_energy/AUXILIARY_CERTIFICATE_PROOF.md']
records=['source_audit/state131_exact.json','02_energy/verification/compact_certificate_audit.json','02_energy/verification/auxiliary_certificate_audit.json','02_energy/verification/state131_coefficient_bounds.json','07_weighted/verification/high_symbol_certificate_audit.json','07_weighted/verification/sharp_coefficient_audit.json','07_weighted/verification/r2_extra_audit.json','07_weighted/verification/state131_weighted_bounds.json','07_weighted/verification/radial_commutator_constants.json','16_weighted_fractional/verification/state131_weighted_gap.json','16_weighted_fractional/verification/sharp_weighted_constants.json']
data={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','scope':'Dependency and exact arithmetic audit of reference contract, not a fresh full certificate recomputation. The source certificate recomputations are retained in their own audit records.','canonical_sha256':canonical,'conditions':{k:('REFUTED' if k=='Ws' else 'CONFIRMED') for k in ['W0','Wn','W1','W2','W3','Wm','Ws','Wt']},'new_reference_scope':'All W conditions must be checked anew; no finite-potential assumption is used by the analytical theorem.','dependencies':{p:hashfile(root/p) for p in proofs+records},'code_sha256':hashfile(Path(__file__))}
(root/'16_weighted_fractional/verification/reference_audit.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k!='dependencies'},indent=2))
