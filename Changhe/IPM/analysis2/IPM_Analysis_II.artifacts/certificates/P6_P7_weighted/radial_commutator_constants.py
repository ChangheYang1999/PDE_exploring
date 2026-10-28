"""Exact/Arb arithmetic for the radial commutator and smaller weight radius.
The exterior bounds are the independently audited exact-sector enclosures;
the interior bounds use the completed V045 continuum tensor certificates.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
HERE=Path(__file__).resolve().parent
ctx.prec=512
assert 4**4*11**5 < 35**5
M=arb(4)**(arb(4)/5)/5
Csharp=22*M
assert Csharp<14
source=HERE/'state131_weighted_bounds.json'
d=json.loads(source.read_text())
assert d['state']==131 and d['split_radius']==100
assert d['delta']=='2/5'
sharp_path=HERE/'sharp_coefficient_audit.json'
sharp=json.loads(sharp_path.read_text())
assert sharp['verdict']=='CONFIRMED' and sharp['source_sha256']==d['input_sha256']
assert sharp['targets']['rho2_weighted']=='8' and sharp['targets']['u2_weighted']=='3'
components_path=HERE.parent.parent/'02_energy/verification/state131_coefficient_bounds.json'
components=json.loads(components_path.read_text())
assert components['input_sha256']==d['input_sha256']
for name in ('rho_x','rho_y'):
    assert arb(components['bounds'][name])<11
for name in ('chi22','chi31','chi13'):
    assert arb(components['bounds'][name])<arb(7)/5
assert 2*11**2<16**2
R0=arb(100);fac=R0**(arb(2)/5)
local={'C_rho':fac*24,'C_U':fac*arb(14)/5,'C_DU':fac*arb(14)/5,'C_D2U':fac*3}
far={k:arb(v) for k,v in d['exterior_bounds'].items()}
target={'C_rho':152,'C_U':18,'C_DU':18,'C_D2U':45}
for k in target:
    assert local[k]<target[k] and far[k]<target[k]
rows=[]
for sn,sd,mn,md,roundn,roundd in [(1,1,27,10,5,2),(2,1,4,5,3,5),(11,5,2,5,1,5)]:
    s=arb(sn)/sd
    C=target['C_DU']+15*target['C_rho']+s*(9*target['C_U']+2*target['C_DU']+arb(target['C_D2U'])/arb(2).sqrt())
    err=C/(arb(2)**14)
    margin=arb(mn)/md-err
    assert margin>arb(roundn)/roundd
    rational_C=Q(18)+15*152+Q(sn,sd)*(9*18+2*18+Q(45*5,7))
    rational_margin=Q(mn,md)-rational_C/2**14
    assert rational_margin>Q(roundn,roundd)
    threshold=((C/(arb(mn)/md-arb(roundn)/roundd)).log()/arb(2).log())*arb(5)/2
    rows.append({'s':f'{sn}/{sd}','R':'2^35','error_upper':err.str(70),'margin_lower':margin.str(70),'rounded_margin':f'{roundn}/{roundd}','inverse_bound':str(Q(roundd,roundn)),'rational_margin_lower':str(rational_margin),'log2_R_threshold_for_rounded_margin':threshold.str(70)})
oldC=32+15*65536+(arb(11)/5)*(9*32+2*32+arb(32768)/arb(2).sqrt())
olderr=oldC/(arb(2)**56)**(arb(2)/5)
assert olderr<arb(1)/5
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
 'M_delta':M.str(70),'commutator_factor_at_s_11over5':Csharp.str(70),'rounded_commutator_factor':14,
 'state131_source_sha256':d['input_sha256'],'exterior_record_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'local_bounds':{k:v.str(70) for k,v in local.items()},'exterior_bounds':{k:v.str(70) for k,v in far.items()},
 'state131_global_upper_bounds':target,'rows':rows,
 'both_states_with_older_coefficients_R':'2^56','both_states_error_upper':olderr.str(70),'dependency_hashes':{str(x.relative_to(HERE.parent.parent)):hashlib.sha256(x.read_bytes()).hexdigest() for x in (sharp_path,components_path)},'proof_sha256':hashlib.sha256((HERE.parent/'RADIAL_COMMUTATOR_PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'CONFIRMED','ledger':'V072'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
