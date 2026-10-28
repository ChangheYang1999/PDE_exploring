"""Outward values of the independently verified sharper closed form."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import json, hashlib
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/closed_form37_lead'
ctx.prec=320
rows=[]
for text in ['1/1000','1/100','1/20','1/10','1/5','3/10','1/2','3/4','9/10','99/100']:
    a=arb(text)
    value=4*arb(2)**(-a/2)/(arb.pi()*a*(a+2))+arb(209)/(500*(1-a))+arb(1353)/2500
    k=int((arb(value.upper())*10**10).ceil().unique_fmpz())
    rows.append(dict(alpha=text,lower=str(value.lower().fmpq()),upper=str(value.upper().fmpq()),
                     ball=value.str(40,more=True),safe_upper_C=f'{k//10**10}.{k%10**10:010d}'))
result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=320,rows=rows,
            auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(BASE/'verification/closed_form_values.json').write_text(json.dumps(result,indent=2)+'\n')
for row in rows:print(row['alpha'],row['safe_upper_C'])
