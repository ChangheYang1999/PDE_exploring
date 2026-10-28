from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
from flint import arb, ctx
ctx.prec=256
ctx.threads=1
root=Path(__file__).resolve().parents[3]
k=arb(1615536043799051)/arb(9007199254740992)
ell=1/k; A=2*ell-1; D=4*ell-1; S=A+D
sigma=arb(25)/4; s0=arb(41)/20; delta=arb(9)/5
values={
'k':k,'ell':ell,'A':A,'D':D,'Sigma':S,
'm_x':S*(arb(3)/2-s0)+delta*A,
'm_y_bulk_constant':1+ell-(4+delta)*D,
'm_y_bulk_characteristic':1+ell-(4+delta)*D+sigma*S,
'm_y_cofactor_constant':1+ell-(4+delta)*D+2*S,
'm_y_cofactor_characteristic':1+ell-(4+delta)*D+(sigma+2)*S,
'm_infinity':1+ell/2,
'D_squared':D*D,
'L_bulk_at_mu_half':(-(1+ell-(4+delta)*D)+arb(1)/2)/(D*D),
'L_cofactor_at_mu_half':(-(1+ell-(4+delta)*D+2*S)+arb(1)/2)/(D*D)
}
assert values['m_x']>arb('0.9726')
assert values['m_y_cofactor_characteristic']>values['m_y_bulk_characteristic']>values['m_infinity']>values['m_x']
assert values['m_y_bulk_constant']<values['m_y_cofactor_constant']<0
out={'date':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'values':{k:str(v) for k,v in values.items()},'scope':'Exact-rational k arithmetic; source margin imported only from independent topic132 interval.'}
p=root/'proofs/142_global_symbol_inequality/evidence/check.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
