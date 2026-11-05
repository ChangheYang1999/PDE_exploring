#!/usr/bin/env python3
"""Qa(F) from inherited integer source tensors, without CE multipliers."""
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import json,sys
from pathlib import Path
from flint import arb,ctx,fmpq as Q
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'coercivity_residual'))
from fields013 import SOURCE_HASHES,C
ctx.prec=384
inherited=(HERE.parents[1]/'combined2/IPM.artifacts/theory_audit/research/'
           'source013_moment_refinement/verification/result_v01.json')
data=json.loads(inherited.read_text())
assert data['source']['id']=='C2-N1-013'
assert data['source']['raw_sha256']==SOURCE_HASHES['phi013']
assert Q(data['source']['fixed_c_exact'])==C
rounded=['0.0000018314','0.000004383','0.00001049','0.133465']
checks=[]
for row in data['tensor_energies']:
    j=row['order'];assert 0<=j<=3
    value=Fraction(rounded[j])
    assert Q(value.numerator,value.denominator)>=Q(row['upper_exact'])
    checks.append(j)
assert sorted(checks)==[0,1,2,3]
T0,T1,T2,T3=map(arb,rounded)
f=arb('0.0000007961207')
# Exact separate radial maxima for ||D^3(W^-1)||_F.
c3=768*arb(15).sqrt()/125+5760*arb(21).sqrt()/2401
assert c3<36
d3=T3.sqrt()+3*T2.sqrt()+18*T1.sqrt()+36*T0.sqrt()
d1=f**(arb(2)/3)*d3**(arb(1)/3)
d2=f**(arb(1)/3)*d3**(arb(2)/3)
H2=(T0+2*T1+T2).sqrt();H3=(T0+3*T1+3*T2+T3).sqrt()
A2=H2+4*d1+12*f
A3=H3+7*d2+130*d1+1391*f
n=A2**arb('.9')*A3**arb('.1')
assert n<arb('0.00759') and n<arb(1)/125
out={'status':'CERTIFIED_Q_SOURCE_FROM_INTEGER_TENSORS',
     'inherited_tensor_sha256':sha256(inherited.read_bytes()).hexdigest(),
     'source_hashes':SOURCE_HASHES,'fixed_c':str(C),
     'rounded_tensor_energies':rounded,'exact_tensor_upper_checks':True,
     'f2_upper':'0.0000007961207',
     'inverse_weight_third_derivative_upper':c3.str(80),
     'D3_F_upper':d3.str(80),'D1_F_upper':d1.str(80),
     'D2_F_upper':d2.str(80),'A2':A2.str(80),'A3':A3.str(80),
     'Q_F_upper':n.str(80),'rational_upper':'759/100000',
     'simpler_rational_upper':'1/125',
     'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'finished_utc':datetime.now(timezone.utc).isoformat(),
     'scope':'Forcing bound only. Uses inherited certified F L2 and '
             'integer WF tensors. No CE, weight multiplier, background '
             'matrix or existence assumption.'}
(HERE/'source_Q_from_integer_tensors.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
