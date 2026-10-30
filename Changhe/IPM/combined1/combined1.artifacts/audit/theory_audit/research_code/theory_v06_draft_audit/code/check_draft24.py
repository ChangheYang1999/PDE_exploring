from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib,json,time
from flint import arb,ctx
ctx.prec=768
B=Path(__file__).resolve().parents[1]; start=time.monotonic()
def aa(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
budgets=[Q('3.7930e-6'),Q('2.8496e-6'),Q(25,54684)]
allowed={'d2','Mpen2','005','006','007','008','009','010','012','013','014','015','016','017','018'}
results={}
for name in ['THEORY_FINAL_draft24.md','theory_v06_preview2.md']:
    rows=[]
    for line in (B/'source'/name).read_text().splitlines():
        if not line.startswith('| '):continue
        cols=[v.strip() for v in line.split('|')[1:-1]]
        if len(cols)!=6 or cols[0] not in allowed:continue
        floor=Q(cols[1].split()[0]);rr=[]
        for claim,budget in zip(cols[2:5],budgets):
            assert Q(claim)<floor/budget
            rr.append({'claimed':claim,'exact_lower_ratio':str(floor/budget)})
        rows.append({'candidate':cols[0],'ratios':rr})
    assert len(rows)==15
    extra=[]
    for candidate,floor,claims in [('018n19',Q('0.001655825792'),['436.5','581.0','3.621']),('018n23',Q('0.001328016044'),['350.1','466.0','2.904']),('019n19',Q('0.001661806967'),['438.1','583.1','3.634'])]:
        for claim,budget in zip(claims,budgets):
            assert Q(claim)<floor/budget
            extra.append({'candidate':candidate,'claimed':claim,'exact_lower_ratio':str(floor/budget)})
    results[name]={'source_sha256':sha(B/'source'/name),'table':rows,'prose':extra,'all_54_ratios_conservative':True}
mu=Q(97,250);C=Q(397);s=Q(1,5184);r=Q(1351,10**6);eta=Q(4207,2*10**7);cu=Q(8,5)
rate=mu-C*s-cu*r*72;KH=Q(10000,1557)
assert rate>Q(1557,10000) and KH<Q('6.4227') and KH>Q('6.4226')
assert 1/rate<Q('6.4226')
assert KH*eta==Q(4207,3114000) and KH*eta<r
cs=1/(2*(arb.pi()*aa(s)*aa(1+s)).sqrt());ratio=cs*aa(r)/2
assert ratio<aa('0.0137200')
b=(2*aa(mu)/3)*(aa(mu)/(3*aa(C))).sqrt()/(aa(cu)*1024)
assert b<aa('2.8496e-6') and aa('0.004769166867')/b>1673
cap=C*Q(125,97)**3/Q(1673)**2
assert cap<Q('3.04e-4') and C/cap>10**6
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'sources':results,
'proof_sha256':sha(B/'DRAFT24_ADDENDUM.md'),'code_sha256':sha(Path(__file__)),
'rate_exact':str(rate),'rate':str(aa(rate)),'full_rate_inverse_exact':str(1/rate),'inherited_6_4226_valid':True,'KH_exact':str(KH),'KH_eta_exact':str(KH*eta),'strict_selfmap_slack_exact':str(r-KH*eta),
'contraction':str(ratio),'baseline_family_ceiling':str(b),'baseline_distance_ratio':str(aa('0.004769166867')/b),
'necessary_C_upper_exact':str(cap),'necessary_C_upper':str(aa(cap)),
'only_for_same_family_formula_and_fixed_cU_w2':True,'all_arithmetic_confirmed':True}
with (B/'verification/draft24_result_v2.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='sources'},indent=2))
