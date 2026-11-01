"""Check the exact dependencies of the Q9 genericity specialization."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime, timezone
import gzip,json,time
start=time.monotonic();now=datetime.now(timezone.utc).isoformat(timespec='seconds')
out=Path('research/275_period_nine_genericity');base=Path('research/267_period_nine_tuning/verification')
checked=[]
def ref(p):
 p=Path(p);return {'path':str(p),'sha256':sha256(p.read_bytes()).hexdigest()}
def check_ref(r):
 assert ref(r['path'])['sha256']==r['sha256'],r['path'];checked.append(r)
def read(p):
 p=Path(p);raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def ball(p):
 m,e,r,re=p;mid=F(int(m))*F(2)**int(e);rad=F(int(r))*F(2)**int(re);return mid-rad,mid+rad
old=read('research/257_period_seven_eight_genericity/verification/admission.json')
assert old['verdict']=='PROVED' and old['ledger']=='V532'
for k in ['proof','independent_review']:check_ref(old[k])
finite=read(base/'obstruction_admission.json');conv=read(base/'admission.json')
assert finite['verdict']=='PROVED_FINITE_ALGEBRA' and finite['degree']==18 and finite['root_count']==10
assert conv['verdict']=='PROVED' and conv['ledger']=='V551'
for k in ['proof','obstruction','independent_comparison']:check_ref(finite[k])
for k in ['proof','finite_algebra','independent_protocol_review']:check_ref(conv[k])
row=conv['rows'][0];assert row['root']==1 and F(row['s'])==2**20;check_ref(row['review'])
review=read(row['review']['path']);assert review['all_checks_pass'] and review['complete_partition_replayed']
check_ref(review['receipt']);receipt=read(review['receipt']['path'])
assert receipt['all_checks_pass'] and receipt['Q']==9 and receipt['h']==1 and receipt['K']==19
check_ref(receipt['coverage']);cover=read(receipt['coverage']['path'])
assert cover['edge']=='1/36' and cover['K']==19 and len(cover['nodes'])==1
leaf=cover['nodes'][0];assert leaf['a']=='0' and leaf['b']=='1/36' and leaf['lower']==19 and leaf['upper'] is None
assert leaf['status']=='interval';lo,hi=ball(leaf['enclosure']);assert hi < -2**20
llo,lhi=ball(receipt['limit']);assert lhi < -2**20 and lo<=llo<=lhi<=hi
assert [v['k'] for v in receipt['finite']]==list(range(2,27))
for v in receipt['finite']:
 a,b=ball(v['enclosure']);assert a>2**20 or b < -2**20
obs=read(base/'obstruction_checks.json');assert obs['all_checks_pass'] and len(obs['primitive_coefficients'])==19
coeff=list(map(int,obs['primitive_coefficients']));assert coeff[-1]>0
h=sha256(','.join(map(str,reversed(coeff))).encode()).hexdigest();assert h==finite['primitive_descending_coefficients_sha256']
a,b=map(F,receipt['root_interval']);a0,b0=map(F,obs['real_roots'][0]['interval']);assert a0<=a<b<=b0
assert obs['real_roots'][0]['sturm_variations'][0]-obs['real_roots'][0]['sturm_variations'][1]==1
proper=set(range(1,18))
for row in obs['modular_irreducibility']:
 degs=row['factor_degrees'];assert sum(degs)==18
 choices={0}
 for d in degs:choices|={x+d for x in list(choices)}
 proper &= choices
assert not proper
result={'checked_at_utc':now,'all_checks_pass':True,'Q':9,'center_root':1,'finite_response_indices':[2,26],'uniform_center_bound':'1048576','limiting_response_bound':'1048576','cover_includes_zero':True,'irreducible_degree':18,'primitive_descending_coefficients_sha256':h,'proper_factor_degree_intersection':sorted(proper),'amplitude_response_exponent':9,'amplitude_radius_exponent':'9/2','checked_references':checked,'general_theorem_admission':ref('research/257_period_seven_eight_genericity/verification/admission.json'),'source':ref('code/period_nine_genericity_audit.py'),'scope':'Dependency and specialization check using previously admitted irreducibility and complete response cover; not a new giant symbolic response computation.','actual_elapsed_s':time.monotonic()-start}
(out/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'sources/period_nine_genericity_audit.py').write_bytes(Path('code/period_nine_genericity_audit.py').read_bytes())
print(now,'all checks pass',len(checked),'dependency references',result['actual_elapsed_s'])
