#!/usr/bin/env python3
import json
from pathlib import Path
from flint import arb,ctx
ctx.prec=256
mu=arb(1)/10;q=arb(21)/10
B0=arb(1);B1=(mu*mu/arb(1).exp()).sqrt();B2=2*mu*mu/arb(1).exp()
A2=A3=arb(1)
D2=mu**-2/(arb(1).exp()*(mu**-2-2)).sqrt();D3=mu**-2/(arb(1).exp()*(mu**-2-3)).sqrt()
rows=[]
for R in [1000,10000,30000,100000]:
 L2=(1+2*R)*A2+2*D2;L3=(1+2*R)*A3+2*D3
 N2=L2+4*B1+8*B0;N3=L3+arb(8).sqrt()*A2+24*B1+4*B2+40*B0
 C=N2**(3-q)*N3**(q-2)
 rows.append({'R':R,'A2_star':N2.str(50),'A3_star':N3.str(50),'C_low':C.str(50),'C_low_squared':(C*C).str(50)})
z={'status':'RIGOROUS_ARB_OPERATOR_PRICE','mu':'1/10','definition':'||chi_R Pmu WJq g||<=C_low||g||, Pmu symbol exp(-|xi|²/(2mu²)), |chi|<=1,supportr<=R','rows':rows,'warning':'No claim that all commutator low/high cross terms have been bounded.'}
p=Path(__file__).resolve().parent/'Qnorm_interior_lowpass_price.json';p.write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z,indent=2))
