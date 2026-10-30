from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
import hashlib,json,time
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
start=time.monotonic();ctx.prec=512
mu,C,b,d=F(97,250),F(397),F(8,5),F(48,25)
sf,smax=F(1,5184),F(1,1024);ss=mu/(3*C);q=F(361,1024)
assert sf<ss<smax and 1-d*smax>0
A=(arb(1601)**ar(F(4,5))*ar(q*q)+arb(2)**15*ar(q)+arb(2)**20).sqrt()
Rs=ar(2*mu/(3*b))*ar(mu/(3*C)).sqrt()
fixed=ar(F(1351,10**6))/(ar(1-d*sf)*A)
incorrect=Rs/(ar(1-d*sf)*A)
at_star=Rs/(ar(1-d*ss)*A)
repaired=Rs/(ar(1-d*smax)*A)
assert fixed<ar(F(13127,10**10)) and incorrect<at_star<repaired
assert repaired<ar(F(284,10**8))
rows={'A':A,'R_star':Rs,'fixed_mass_upper':fixed,'draft_family_bound':incorrect,'envelope_at_s_star':at_star,'repaired_family_upper':repaired}
out={'utc':datetime.now(timezone.utc).isoformat(),'parameters':{k:str(v) for k,v in dict(mu=mu,C=C,b=b,d=d,s_fixed=sf,s_max=smax,s_star=ss,q=q).items()},'intervals':{k:v.str(80) for k,v in rows.items()},'strict_family_deduction_mismatch':True,'fixed_upper_decimal':'0.0000013127','repaired_family_upper_decimal':'0.00000284','inputs':{str(p.relative_to(B)):sha(p) for p in [B/'PROOF.md',Path(__file__),B/'source/theory_v04.p3.md',B/'source/annulus_admissible.py']},'elapsed_seconds':time.monotonic()-start}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
for k,v in rows.items():print(k,v.str(28))
