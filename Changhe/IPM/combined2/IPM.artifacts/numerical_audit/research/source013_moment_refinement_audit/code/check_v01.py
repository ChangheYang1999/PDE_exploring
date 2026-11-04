"""Independent rational replay from the original admitted AN moments."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
from time import perf_counter
import json, sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3]
B=R/'research/source013_moment_refinement_audit'
A=R.parent/'theory_audit'
def h(p):
    z=sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):z.update(b)
    return z.hexdigest()
def read(p):return json.loads(p.read_text())
def now():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
start=now();timer=perf_counter();checks=0;bindings={}
def ok(p,msg):
    global checks
    assert p,msg
    checks+=1
own_path=R/'research/source013_norms/verification/weighted_publication_v01/result.json'
actual_path=own_path.parent/'actual_review_v01.json'
own,actual=read(own_path),read(actual_path)
ok(own['status']=='CERTIFIED_NORMS' and own['kind']=='weighted','original result status')
ok(actual['status']=='BOUND' and actual['result_sha256']==h(own_path),'original actual review')
for rel in ['result','display','check','review']:
    p=B/'verification'/f'at_{rel}_v01.json'
    original=A/'research/source013_moment_refinement/verification'/({'result':'result_v01.json','display':'display_v01.json','check':'check_v01.json','review':'certificate_review_v01.json'}[rel])
    ok(h(p)==h(original),'AT immutable '+rel)
    bindings[str(p.relative_to(R))]=h(p)
    bindings['../theory_audit/'+str(original.relative_to(A))]=h(original)
r=read(B/'verification/at_result_v01.json');disp=read(B/'verification/at_display_v01.json');at=read(B/'verification/at_check_v01.json');rv=read(B/'verification/at_review_v01.json')
ok(at['status']=='PASS' and at['output_sha256']==h(B/'verification/at_result_v01.json'),'AT result audit')
for rel,s in rv['bindings'].items():
    p=A/rel
    ok(not Path(rel).is_absolute() and '..' not in Path(rel).parts,'relative review path')
    ok(h(p)==s,'review binding '+rel)
    bindings['../theory_audit/'+rel]=s
ok(rv['status']=='BOUND','AT review status')
ok(own['source']==r['source'],'exact source identity')
ok(r['source']['fixed_c_exact']=='4076476460239181/2251799813685248','fixed parameter')
a=own['output'];ok(a['fractional_order_exact']==r['fractional_order_exact']=='21/10','fractional order')
ok([x['order'] for x in a['tensor_energies']]==[0,1,2,3],'input moment order')
lo=[Q(x['lower_exact']) for x in a['tensor_energies']];up=[Q(x['upper_exact']) for x in a['tensor_energies']]
for l,u in zip(lo,up):ok(0<=l<=u,'input containment ordering')
q=Q(disp['T1_upper']);ok(q>=0 and q*q>=up[0]*up[2],'Cauchy Schwarz root')
ok(Q(r['old_T1_upper_exact'])==up[1],'old upper identity')
new=up.copy();new[1]=min(new[1],q)
ok(new[1]>=lo[1],'refined nonempty moment')
for j,x in enumerate(r['tensor_energies']):
    ok(x['order']==j and Q(x['lower_exact'])==lo[j] and Q(x['upper_exact'])==new[j],'refined moment '+str(j))
bl=[sum(comb(m,j)*lo[j] for j in range(m+1)) for m in range(4)]
bu=[sum(comb(m,j)*new[j] for j in range(m+1)) for m in range(4)]
for m,row in enumerate(r['integer_norms']):
    ok(row['order']==m and Q(row['energy_lower_exact'])==bl[m] and Q(row['energy_upper_exact'])==bu[m],'binomial '+str(m))
    l,u=map(Q,row['norm_interval_exact'])
    ok(0<=l<=u and l*l<=bl[m] and u*u>=bu[m],'exact square bounds '+str(m))
    dl,du=map(Q,disp['integer_norms'][m]['interval'])
    ok(disp['integer_norms'][m]['order']==m and 0<=dl<=l<=u<=du,'outward display '+str(m))
l,u=map(Q,r['fractional_norm_interval_exact'])
ok(bl[2]>0 and bu[1]>0,'nonzero fractional case')
ok(0<=l<=u and (l*l<=bl[2] or l**20*bu[1]<=bl[2]**11),'fractional lower')
ok(u**20>=bu[2]**9*bu[3],'fractional upper')
dl,du=map(Q,disp['fractional_interval'])
ok(0<=dl<=l<=u<=du,'fractional outward display')
for p in [own_path,actual_path,B/'PROOF.md',Path(__file__)]:bindings[str(p.relative_to(R))]=h(p)
output={'status':'PASS','started_utc':start,'finished_utc':now(),'elapsed_seconds':perf_counter()-timer,'checks':checks,'files':dict(sorted(bindings.items())),'source':r['source'],'new_T1_upper_exact':str(new[1]),'fractional_norm_interval_exact':r['fractional_norm_interval_exact'],'fractional_display':disp['fractional_interval'],'scope':'Independent rational consequence of already admitted full-plane source013 moments. No new regional quadrature or closure.'}
with(B/'verification/check_v01.json').open('x') as f:json.dump(output,f,indent=2);f.write('\n')
print(json.dumps({k:output[k] for k in ['status','started_utc','finished_utc','elapsed_seconds','checks','fractional_display']},indent=2))
print('result_sha256',h(B/'verification/check_v01.json'))
