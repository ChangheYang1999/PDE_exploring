"""Read-only arithmetic audit of the local LP's omitted inner disks; no LP run."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib,json
from flint import arb,ctx
R=Path(__file__).resolve().parents[1]
D=R/'08_improved_upper_bounds/local_functional_audit/verification'
ctx.prec=256

def aq(q):
 q=Q(q);return arb(q.numerator)/q.denominator

def saveball(v):
 return {'display':str(v),'lower':str(v.lower().fmpq()),'upper':str(v.upper().fmpq())}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

cut=Q(2**43,3**44)
rows=[]
for a in [Q(3,10),Q(1,2),Q(3,4)]:
 aa=aq(a);a2=arb(2)**(1+aa/2)/(arb.pi()*(aa+2))
 U=arb(2)**(1-aa)*a2/aa
 old=U*aq(Q(1,10**8))**aa
 missing=2*a2*aq(cut)**aa/aa
 assert missing>old
 rows.append({'alpha':str(a),'U':saveball(U),'program_inner':saveball(old),'nominal_inner_angular_upper':saveball(missing),'undercount':saveball(missing-old)})
paths=[Path(__file__),R/'../numerics_code/locD_lp.py',*[R/f'../the numerics work/runs/locD/locD_a{a}.log' for a in ['03','05','075']],D.parent/'PROOF.md']
out={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'nominal_exact_cutoff':str(cut),'rows':rows,'scope':'The exact formula for the two omitted own-kernel disk upper bounds on the nominal rational grid. The LP uses floating endpoints; it remains uncertified. Adding this upper bound to an LP objective is not a certified discretization correction.','sha256':{str(p.relative_to(R)):sha(p) for p in paths}}
(D/'inner_cutoff.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print(r['alpha'],r['program_inner']['display'],r['nominal_inner_angular_upper']['display'])
