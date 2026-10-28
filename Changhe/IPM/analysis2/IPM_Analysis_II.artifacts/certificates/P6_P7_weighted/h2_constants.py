from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,sys
from flint import arb,ctx
ctx.prec=384
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'02_energy'/'verification'))
from compact_matrix import A
s=json.loads((BASE/'source_audit'/'state131_exact.json').read_text())
d=json.loads((BASE/'05_tails'/'verification'/'state131_residual_hessian_lower.json').read_text())
c=Q(s['exact_parameters']['cl']);gamma=1/c;r=arb(100);q=1+r*r
M={k:arb(d['potential_component_bounds'][str(k)])+arb(d['potential_tail_bounds'][str(k)]) for k in (4,5,6)}
local={'B1':11*arb(2).sqrt(),'B2':77*q.sqrt(),'B3':94*q,'BV2':35*q.sqrt(),'BV3_1':104*q.sqrt(),'B3_1':94*q.sqrt()}
far={'B2':4*M[5]*r**A(gamma-2)*q.sqrt(),'B3':arb(2)**A(Q(5,2))*M[6]*r**A(gamma-3)*q,'BV2':arb(2)**A(Q(3,2))*M[5]*r**A(gamma-2)*q.sqrt(),'BV3_1':4*M[6]*r**A(gamma-3)*q.sqrt(),'B3_1':arb(2)**A(Q(5,2))*M[6]*r**A(gamma-3)*q.sqrt()}
targets={'B1':16,'B2':2**13,'B3':2**20,'BV2':2**12,'BV3_1':2**14,'B3_1':2**14}
for key,value in local.items():assert value<targets[key],(key,value)
for key,value in far.items():assert value<targets[key],(key,value)
assert 1-arb(2)**(-arb(1)/5)>arb(1)/8
assert 12+2*12*8<256
assert 18+1152+128<2048
D=2**13+4*16;Z=8*16+2*2**13
assert D*256+2**13*2048<2**25 and Z<2**15
assert Q(2**50,4*Q(1,8))+2**15<2**52
assert 2**52*(25+2**55)<2**108
assert Q(2**112,5)-2**108>Q(2**112,10)
assert 2*D*256+2*2**12+4*2**13*256<2**24
assert 2*2**20*2048+2**24<2**33 and 4*Z<2**17
assert 2**66+2**17<2**67
assert Q(2**72,10)-2**67>Q(2**72,20)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'input_sha256':s['canonical_serialization_sha256'],'local_bounds':{k:v.str(50) for k,v in local.items()},'far_bounds':{k:v.str(50) for k,v in far.items()},'certified_targets':targets,'energy_arithmetic':'all exact rational inequalities pass','generic_weighted_Riesz':256,'parity_P0_Riesz':2048,'E1_low_weight':str(2**112),'E2_E1_weight':str(2**72),'E1_inverse':10,'E2_inverse':20,'scope':'high inverse additionally requires completed M1,M2 certificates'}
HERE.joinpath('h2_constants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
