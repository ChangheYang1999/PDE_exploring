from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,re,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];ctx.prec=512;started=time.monotonic()
def a(x):
 x=Q(x);return arb(x.numerator)/x.denominator
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
mu,C,b,d=Q(97,250),Q(397),Q(8,5),Q(48,25)
sf,smax,q=Q(1,5184),Q(1,1024),Q(361,1024)
A=(arb(1601)**a(Q(4,5))*a(q*q)+a(2**15*q+2**20)).sqrt()
Rstar=a(2*mu/(3*b))*a(mu/(3*C)).sqrt()
fixed=a(Q(1351,10**6))/(a(1-d*sf)*A)
family=Rstar/(a(1-d*smax)*A)
s,t=Q(1,262144),Q(1,5184)
kappa=2*(a(2*10**12+16410)**a(t/2)+a(34*t))/a(1-34*s)
checks=[('fixed',fixed,'1.312585971e-6','1.312585972e-6'),('family',family,'2.839272408e-6','2.839272409e-6'),('kappa',kappa,'2.01885','2.018851')]
rounding=[]
for name,x,lo,hi in checks:
 assert a(lo)<x<a(hi)
 rounding.append({'name':name,'exact_expression_interval':x.str(90),'printed_value':lo,'safe_upper':hi,'printed_strictly_below_expression':True,'safe_upper_strict':True})
assert Q('2.018851')*Q('163.88')/1572864<Q(4207,20000000)
source=(B/'source/theory_v04.md').read_text();rows=[]
for line in source.splitlines():
 if not line.startswith('| '):continue
 cols=[x.strip() for x in line.split('|')[1:-1]]
 if len(cols)!=6 or cols[0] not in ['d2','Mpen2','005','006','007','008','009','010','012','013','014']:continue
 floor=Q(cols[1].split()[0]);ratios=[]
 for label,col,den in zip(['TB-sharp','sharpw','graded'],cols[2:5],[Q('3.7930e-6'),Q('2.8496e-6'),Q(25,54684)]):
  claim=Q(col);true=floor/den
  assert claim<true,(cols[0],label,str(claim),str(true))
  ratios.append({'budget':label,'budget_exact':str(den),'claimed_factor':str(claim),'true_lower_ratio_exact':str(true),'claim_strictly_lower':True})
 rows.append({'candidate':cols[0],'distance_lower_exact':str(floor),'ratios':ratios})
assert len(rows)==11
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':h(B/'source/theory_v04.md'),'proof_sha256':h(B/'PROOF.md'),'checker_sha256':h(Path(__file__)),'rounding_checks':rounding,'threshold_163_88_still_passes_with_rounded_upper':True,'all_33_table_ratios_strictly_conservative':True,'candidate_rows':rows,'elapsed_seconds':time.monotonic()-started}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['candidate_rows','rounding_checks']},indent=2))
