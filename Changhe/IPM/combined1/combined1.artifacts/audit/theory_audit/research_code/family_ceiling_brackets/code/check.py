"""Independent rational-square certificates for the family supremum brackets."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from decimal import Decimal
import hashlib,json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=512
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads((B/p).read_text());checks=[]
def req(name,test,value=None):
 assert bool(test),(name,str(value));checks.append({'claim':name,'value':None if value is None else str(value)})
def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator
m=read('data/manifest.json');req('proof first',m['proof_written_before_checker'])
for rel,h in m['inputs'].items():req('binding '+rel,sha(B/rel)==h)
for z in read('data/input_sources.json')['inputs']:req('copied '+z['local'],sha(B/z['local'])==z['sha256'])
p=read('data/parameters.json');peer=read('source/T2_result.json');reach=read('source/reach_result.json');fix=read('source/repairs_result.json')
req('peer37passes',peer['checks']==37 and peer['fails']==[])
source_map={'c1-shared/theory_requirements/theory_v01.md':'theory_v01.md','c1-shared/theory_requirements/theory_v03.md':'theory_v03.md','c1-t2/artifacts/arith/distance_budget_update.py':'T2_distance_budget.py','c1-t2/artifacts/data/falsify_section0_results.json':'T2_falsify_result.json'}
req('complete peer source graph',set(source_map)==set(peer['inputs']))
for path,name in source_map.items():req('peer source '+path,peer['inputs'][path]==sha(B/'source'/name))
for label,j,name,n in [('reach',reach,'reach_PROOF.md',948),('repair',fix,'repairs_PROOF.md',107)]:
 req(label+' accepted result',j['check_count']==n and j['proof_sha256']==sha(B/'source'/name))
v1=' '.join((B/'source/theory_v01.md').read_text().split());v3=' '.join((B/'source/theory_v03.md').read_text().split())
for text in ['297/1000 - 4800 s - 5 N_s(k)/sqrt(s)','297/1000 - 402 s - (8/5) N_s(k)/sqrt(s)','1/10 - 4800 s - 5 N_s(k)/sqrt(s)']:req('v01 rate '+text,text in v1)
for text in ['97/250 - 397 s - (8/5) X(k)/sqrt(s)','259/1000 - 401 s - (8/5) X(k)/sqrt(s)','359/1000 - 397 s','151/500 - 397 s','NORM-T-XSW-v1[1/5476, 2^15, 2^20]','NORM-T-XSW-v1[1/6561, 2^15, 2^20]','NORM-T-XSW-v1[1/5184, 2^15, 2^20]']:req('v03 rate or weights '+text,text in v3)
req('historical upward claim exists','Budgets b_fam (rounded up): baseline FW-A2-Db 6.8626e-8, FW-T-TB-rebal-v1 3.5125e-7' in v3)
rows=[]
for z in p['rows']:
 name=z['name'];mu,C,cU,w=Q(z['mu']),Q(z['C']),Q(z['cU']),Q(z['sqrtW2']);printed=Q(z['printed']);unit=Q(10)**Decimal(z['printed']).as_tuple().exponent
 lo=printed if name=='TB-rebal' else printed-unit;hi=printed+unit if name=='TB-rebal' else printed;s=mu/(3*C);square=4*mu**3/(27*C*cU**2*w**2);b=ar(square).sqrt();n=peer['ceilings'][name]
 req(name+' positivity',min(mu,C,cU,w,lo)>0)
 req(name+' cubic critical point',mu-3*C*s==0)
 req(name+' exact maximum square',(mu-C*s)**2*s/(cU**2*w**2)==square)
 req(name+' exact lower square',lo**2<square)
 req(name+' exact upper square',square<hi**2)
 req(name+' common scalar ceiling',square<Q(p['common_scalar_upper'])**2)
 req(name+' peer parameters',(mu,C,cU,w)==(Q(n['mu0']),Q(n['C']),Q(n['c_U']),Q(n['sqrt_W2'])))
 oldlo,oldhi=map(Q,n['bracket']);req(name+' peer one-unit bracket',(oldlo,oldhi)==(printed-unit,printed))
 req(name+' old bracket flag',n['in_bracket']==(name!='TB-rebal') and n['printed_is_upper_bound']==(name!='TB-rebal'))
 ball=arb(n['b_fam']);req(name+' peer ball positive',ball.lower()>0)
 req(name+' peer ball contains exact square',ball.lower()**2<ar(square) and ar(square)<ball.upper()**2)
 req(name+' independent root overlap',b.overlaps(ball))
 rows.append({'name':name,'sstar_exact':str(s),'supremum_square_exact':str(square),'lower_exact':str(lo),'upper_exact':str(hi),'supremum':b.str(90),'integer_lower_gap':str(square-lo**2),'integer_upper_gap':str(hi**2-square)})
 if name=='TB-rebal':
  req('rebal printed below supremum',printed**2<square)
  req('rebal corrected upper',square<Q(p['rebal_corrected_upper'])**2)
  req('rebal relative lower',square/printed**2>1)
  req('rebal relative upper',square/printed**2<Q(p['relative_upper'])**2)
  rebal={'relative_square_exact':str(square/printed**2),'relative':(b/ar(printed)).str(90)}
gsquare=Q(p['graded_numerator']**2,p['graded_denominator_factor']**2*p['graded_radicand']);glo=Q(45697,10**8);ghi=Q(25,54684);gb=arb(peer['ceilings']['graded']['b_fam']);g=ar(gsquare).sqrt()
req('graded critical point',Q(1,2)-3*4708*Q(1,28248)==0)
req('graded maximum square',(Q(50,217)*(Q(1,2)-4708*Q(1,28248)))**2*Q(1,28248)==gsquare)
req('graded strict lower square',glo**2<gsquare)
req('graded strict upper square',gsquare<ghi**2)
req('graded peer ball positive',gb.lower()>0)
req('graded peer ball contains exact square',gb.lower()**2<ar(gsquare)<gb.upper()**2)
req('graded root overlap',g.overlaps(gb))
eps=Q(p['relative_upper'])-1;req('four-digit repair margin',eps>0 and eps*9999<1)
c=Q(4076476460239181,2251799813685248);q=1/c-4;delta=1-1/c;req('endpoint exponent positive',delta/(-q-1)>0)
req('current-list cap below rebal printed',Q('2.66323e-8')<Q('3.5125e-7'))
for z in reach['rows']:req(z['candidate']+' accepted current CI cap',arb(z['reach']['current_H0']['bound'])<ar('2.66323e-8'))
for rel,h in m['inputs'].items():req('unchanged '+rel,sha(B/rel)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'rows':rows,'graded':{'square_exact':str(gsquare),'lower_exact':str(glo),'upper_exact':str(ghi),'supremum':g.str(90)},'rebal':rebal,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'peer_result_sha256':sha(B/'source/T2_result.json'),'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED seven scalar and graded exact brackets, corrected TB-rebal upper and scoped persistence; REFUTED historical TB-rebal upward-rounding assertion'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),out['utc'],out['elapsed_seconds'])
for z in rows:print(z['name'],z['supremum'])
print('graded',g.str(40),'rebal relative',rebal['relative'])
