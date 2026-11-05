#!/usr/bin/env python3
"""Consume all universal interval records and verify the stronger constant1/3."""
import json,hashlib
from pathlib import Path
from flint import arb,ctx,fmpq as Q
from certify_Cvs3_Gaussian_HS_constant import analytic_cases
HERE=Path(__file__).resolve().parent;ctx.prec=256
folder=HERE/'Cvs3_HS_universal_v01'
result=json.loads((folder/'result.json').read_text());config=result['configuration']
assert result['status']=='CERTIFIED_UNIVERSAL_GRADIENT_CVS3_HS_KERNEL_CONSTANT'
assert config==json.loads((folder/'configuration.json').read_text())
producer=HERE/'certify_Cvs3_Gaussian_HS_constant.py'
assert config['code_sha256']==hashlib.sha256(producer.read_bytes()).hexdigest()
target=arb(1)/3;lo=Q(config['amin']);end=Q(config['amax']);ratio=Q(config['parameter_ratio'])
mx=arb(0);rows=result['rows']
for i,row in enumerate(rows):
    hi=min(lo*ratio,end)
    assert row['index']==i and row['a_lower']==str(lo) and row['a_upper']==str(hi)
    assert row==json.loads((folder/f'parameter_{i:04d}.json').read_text())
    for name in ['parallel_uniform_upper','perpendicular_uniform_upper']:
        value=arb(row[name]);assert value.is_finite() and value<target
        if value.upper()>mx:mx=value.upper()
    lo=hi
assert lo==end
analytic=analytic_cases(config);assert analytic==result['analytic_cases']
for value in analytic.values():assert arb(value)<target
ctx.prec=256
out={'status':'CERTIFIED_UNIVERSAL_GRADIENT_CVS3_HS_CONSTANT_ONE_THIRD',
     'dimensionless_kernel_constant':'1/3','parameter_intervals':len(rows),
     'finite_parameter_maximum_upper':mx.str(70),'analytic_cases':analytic,
     'proved_formula':'||Cvs3 (I-P_mu)||_HS <= ||D^3 rho||_2/(4*pi*sqrt(3)*mu)',
     'multiplicative_constant':(1/(4*arb.pi()*arb(3).sqrt())).str(70),
     'quadratic_high_cross_formula':'|Cvs3[G]-Cvs3[P_mu G]| <= ||D^3 rho||_2/(2*pi*sqrt(3)*mu) ||G||_2^2',
     'bindings':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),producer,folder/'result.json',folder/'configuration.json']},
     'scope':'The universal operator estimate is verified. The actual Candidate013 derivative norm is a separate certificate input; total IPM closure is not asserted.'}
(HERE/'Cvs3_HS_one_third_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
