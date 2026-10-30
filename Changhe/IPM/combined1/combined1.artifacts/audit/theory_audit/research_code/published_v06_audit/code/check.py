from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib,json,time
from flint import arb,ctx
ctx.prec=768
B=Path(__file__).resolve().parents[1]; start=time.monotonic()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(x):
    x=Q(x);return arb(x.numerator)/x.denominator
p=json.loads((B/'data/parameters.json').read_text());raw=Path(p['source_raw'])
assert sha(raw)==p['raw_sha256']
assert sha(B/'source/theory_v06.md')=='493549a9b49ac3eb0fd2c115c90c4ac8e5e9513305c38eb3f41598c31801b6bb'
assert sha(B/'source/R1_037.md')=='d25fa09bf5783e9a55b10a2a6057e70747cf61750be3f576d3eed0d7ba70eea4'
text=(B/'source/theory_v06.md').read_text()
rows=[];budgets=[Q('3.7930e-6'),Q('2.8496e-6'),Q(25,54684)]
allowed={'d2','Mpen2','005','006','007','008','009','010','012','013','014','015','016','017','018','019','020'}
for line in text.splitlines():
    if not line.startswith('| '):continue
    cols=[x.strip() for x in line.split('|')[1:-1]]
    if len(cols)!=6 or cols[0] not in allowed:continue
    floor=Q(cols[1].split()[0]);ratios=[]
    for claim,budget in zip(cols[2:5],budgets):
        assert Q(claim)<floor/budget
        ratios.append({'claim':claim,'exact_ratio':str(floor/budget)})
    rows.append({'candidate':cols[0],'ratios':ratios})
assert len(rows)==17
c=Q(p['c']);gamma=1/c;delta=1-gamma
assert 0<gamma<1
j=p['witness_shape']['j'];m=p['witness_shape']['m'];spec=p['witness_shape']['spec']
assert spec[0]=='legqs' and spec[2]==0 and spec[3]==4
pj=(3+gamma-j*delta)/2;d=2*pj-2*spec[3]
coeff=-Q(spec[4])**8*(d*d-(2*m)**2)*(d-2-2*m)/2
assert coeff!=0 and j+1<4 and d-3==1-(j+1)*delta-2*spec[3]
mu=Q(p['mu']);C=Q(p['C']);s=Q(p['s']);r=Q(p['r']);eta=Q(p['eta']);cu=Q(p['cU'])
rate=mu-C*s-cu*r*72
assert rate==Q(63092119,405000000)
KH=Q(10000,1557);slack=r-KH*eta
assert slack==Q(7,1557000000)>0 and 1/rate<Q('6.4226') and KH<Q('6.4227')
cs=1/(2*(arb.pi()*aa(s)*aa(1+s)).sqrt())
assert cs*aa(r)/2<aa('0.0137200')
baseline=(2*aa(mu)/3)*(aa(mu)/(3*aa(C))).sqrt()/(aa(cu)*1024)
assert aa('2.849577738e-6')<baseline<aa('2.8496e-6')
cap=C*Q(125,97)**3/Q(1673)**2
assert cap==Q(775390625,2554506927217) and cap<Q('3.04e-4')
# Annular support/frequency restriction, distinct from the general bound.
q=Q(361,1024);A=(arb(1601)**aa(Q(4,5))*aa(q*q)+32768*aa(q)+1048576).sqrt()
annular=baseline*1024/((1-aa(Q(48,25*1024)))*A)
assert annular<aa('2.839272409e-6')<baseline
assert gamma-3<-2 and -6<-2
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,
'inputs':{str(x):sha(x) for x in [B/'PROOF.md',Path(__file__),B/'data/parameters.json',B/'source/theory_v06.md',B/'source/R1_037.md',raw,B.parent/'annulus_radius_audit/PROOF.md',B.parent/'annular_moment_adjustment/PROOF.md',B.parent/'candidate020_sectors/PROOF.md']},
'all_51_table_ratios_conservative':True,'table':rows,'counterexample_sector':[j+1,spec[3]],'counterexample_density_coefficient':str(coeff),'residual_drift_exponent':'-2','remainder_exponents':[str(gamma-3),'-6'],
'closure_rate':str(rate),'selfmap_slack':str(slack),'contraction':str(cs*aa(r)/2),'unrestricted_ceiling':str(baseline),'specialized_annular_ceiling':str(annular),'necessary_C_upper':str(cap),'all_exact_checks_pass':True}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['inputs','table']},indent=2))
