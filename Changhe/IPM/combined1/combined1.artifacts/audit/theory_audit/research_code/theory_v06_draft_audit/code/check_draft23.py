from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json, time
B=Path(__file__).resolve().parents[1]
start=time.monotonic()
c=Q(4076476460239181,2251799813685248)
gamma=1/c
delta=1-gamma
# Exhaustive finite limits: l delta <= 1-threshold and 2q <= 1-threshold.
def sectors(threshold):
    return [(l,q,str(1-l*delta-2*q))
            for l in range(1,(1-threshold)//delta+1)
            for q in range((1-threshold)//2+1)
            if 1-l*delta-2*q>=threshold]
l2=sectors(Q(-1)); moment=sectors(Q(-2))
assert [(l,q) for l,q,e in l2]==[(1,0),(2,0),(3,0),(4,0)]
assert {(l,q) for l,q,e in moment}=={(l,0) for l in range(1,7)}|{(1,1),(2,1)}
assert len(l2)-1==3 and len(moment)-1==7
assert c*gamma-1==0
allowed={'d2','Mpen2','005','006','007','008','009','010','012','013','014','015','016','017','018'}
rows=[]
for line in (B/'source/THEORY_FINAL_observed.md').read_text().splitlines():
    if not line.startswith('| '): continue
    cols=[v.strip() for v in line.split('|')[1:-1]]
    if len(cols)!=6 or cols[0] not in allowed: continue
    floor=Q(cols[1].split()[0]); ratios=[]
    for label,col,den in zip(['TB-sharp','sharpw','graded'],cols[2:5],[Q('3.7930e-6'),Q('2.8496e-6'),Q(25,54684)]):
        claim=Q(col); actual=floor/den
        assert claim<actual,(cols[0],label,claim,actual)
        ratios.append({'budget':label,'claim':str(claim),'exact_lower_ratio':str(actual),'conservative':True})
    rows.append({'candidate':cols[0],'ratios':ratios})
assert len(rows)==15
q1=-1-4*delta;q2=1-9*delta
assert -3<q1<-1 and gamma-4<q2<-3
q3=-1-5*delta
assert q1-delta==q3 and q2-delta<q3 and 2*q2-1<q3
extra=[]
for probe,floor,claims in [('n19',Q('0.001655825792'),['436.5','581.0','3.621']),('n23',Q('0.001328016044'),['350.1','466.0','2.904'])]:
    for claim,budget in zip(claims,[Q('3.7930e-6'),Q('2.8496e-6'),Q(25,54684)]):
        assert Q(claim)<floor/budget
        extra.append({'probe':probe,'claim':claim,'exact_ratio':str(floor/budget),'conservative':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,
     'source_sha256':hashlib.sha256((B/'source/THEORY_FINAL_observed.md').read_bytes()).hexdigest(),
     'proof_sha256':hashlib.sha256((B/'PROOF.md').read_bytes()).hexdigest(),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'l2_sectors':l2,'first_moment_sectors':moment,'ratio_rows':rows,
     'all_45_displayed_ratios_conservative':True,'all_six_new_prose_ratios_conservative':True,'extra_prose_ratios':extra,
     'q1_exact':str(q1),'q2_exact':str(q2),
     'all_confirmed_arithmetic_not_acceptance_of_open_certificate':True}
with (B/'verification/draft23_result.json').open('x') as f: json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='ratio_rows'},indent=2))
