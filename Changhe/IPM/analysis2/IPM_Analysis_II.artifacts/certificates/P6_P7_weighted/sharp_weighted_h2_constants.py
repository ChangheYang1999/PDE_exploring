"""Exact arithmetic for the smaller weighted H2 hierarchy."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
HERE=Path(__file__).resolve().parent
assert Q(2,1)<Q(10,7)**2
assert Q(64,7)+Q(64,75)<10
assert Q(256,75)<4
A=Q(644,15);Z=Q(72,5)
assert 2*A*A+Z<2**12
loss=2**27+25*2**12
assert Q(loss)<Q(2**31,10)
assert 26<=2**31
assert Q(198)+Q(512,3)<370
assert 370**2+352<140000
assert Q(140000)<Q(2**22,20)
proof=HERE.parent/'SHARP_WEIGHTED_H2_PROOF.md'
low=json.loads((HERE/'radial_commutator_constants.json').read_text())
assert low['status']=='CONFIRMED' and low['rows'][2]['R']=='2^35'
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'CONFIRMED','ledger':'V073','low_reference':'V072','source_sha256':low['state131_source_sha256'],'radius':'2^35','E1_low_squared_coefficient':str(2**31),'E2_E1_squared_coefficient':str(2**22),'E2_low_squared_coefficient':str(2**53),'first_cross_coefficient':str(A),'first_scalar_coefficient':str(Z),'first_absorbed_coefficient':str(2*A*A+Z),'low_interpolation_debt':loss,'second_cross_coefficient_before_rounding':str(Q(198)+Q(512,3)),'second_absorbed_debt':370**2+352,'semigroup_rates':['1/10','1/20'],'inverse_bounds':[10,20],'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
