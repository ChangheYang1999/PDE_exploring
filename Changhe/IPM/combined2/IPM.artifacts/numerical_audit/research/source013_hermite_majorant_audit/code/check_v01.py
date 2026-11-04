from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from datetime import datetime,timezone
from time import perf_counter
import json,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/source013_hermite_majorant_audit';A=R.parent/'theory_audit'
def h(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def stamp():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
start=stamp();timer=perf_counter();checks=0;files={}
def ok(v,msg):
 global checks
 assert v,msg
 checks+=1
def bind(p,name=None):files[name or str(p.relative_to(R))]=h(p)
def add(*terms):return [sum((p[i]if i<len(p)else Q(0))for p in terms)for i in range(max(map(len,terms)))]
def scale(p,c):return [c*v for v in p]
def mul(p,r):
 z=[Q(0)]*(len(p)+len(r)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(r):z[i+j]+=x*y
 return z
def evalp(p,x):return sum(c*x**i for i,c in enumerate(p))
for kind,filename in [('result','result_v01.json'),('check','check_v01.json'),('review','certificate_review_v01.json')]:
 p=B/f'verification/at_{kind}_v01.json';foreign=A/'research/source013_hermite_majorant/verification'/filename
 ok(h(p)==h(foreign),'immutable AT '+kind);bind(p);bind(foreign,'../theory_audit/'+str(foreign.relative_to(A)))
r=read(B/'verification/at_result_v01.json');check=read(B/'verification/at_check_v01.json');review=read(B/'verification/at_review_v01.json')
ok(check['status']=='PASS'and check['output_sha256']==h(B/'verification/at_result_v01.json'),'AT result check')
ok(review['status']=='BOUND','AT review')
for n,z in review['bindings'].items():
 ok(not Path(n).is_absolute()and'..'not in Path(n).parts,'relative AT path');ok(h(A/n)==z,'AT binding '+n);bind(A/n,'../theory_audit/'+n)
p=R/'research/source013_norms/verification/weighted_publication_v01/result.json';v=p.parent/'actual_review_v01.json';own=read(p);rv=read(v)
ok(own['status']=='CERTIFIED_NORMS'and own['kind']=='weighted','own moment certificate')
ok(rv['status']=='BOUND'and rv['result_sha256']==h(p),'own actual review');bind(p);bind(v)
refp=R/'research/source013_moment_refinement_audit/verification/check_v01.json';ref=read(refp);bind(refp)
ok(ref['status']=='PASS'and ref['source']==r['source']==own['source'],'same exact source')
ok(r['fractional_order_exact']==own['output']['fractional_order_exact']=='21/10','same norm order')
ok(r['nodes_exact']==['1','13000'],'fixed interpolation nodes')
a,b=map(Q,r['nodes_exact']);t=b-a;u=[-a/t,1/t];u2=mul(u,u);u3=mul(u2,u)
h00=add(scale(u3,2),scale(u2,-3),[Q(1)]);h10=add(u3,scale(u2,-2),u)
h01=add(scale(u3,-2),scale(u2,3));h11=add(u3,scale(u2,-1));q=Q(21,10)
left=add(scale(h00,(1+a)**2),scale(h10,t*q*(1+a)))
right=add(scale(h01,(1+b)**2),scale(h11,t*q*(1+b)))
forms=list(zip(left,right))
for j,pair in enumerate(forms):ok(pair==tuple(map(Q,r['coefficient_linear_forms'][j])),'independent Hermite coefficient '+str(j))
for coeff,node,value,derivative in [(left,a,(1+a)**2,q*(1+a)),(left,b,Q(0),Q(0)),(right,a,Q(0),Q(0)),(right,b,(1+b)**2,q*(1+b))]:
 ok(evalp(coeff,node)==value,'node value');ok(sum(i*c*node**(i-1)for i,c in enumerate(coeff)if i)==derivative,'node derivative')
ok(q*(q-1)*(q-2)*(q-3)<0,'global remainder sign')
roots=[list(map(Q,x))for x in r['roots_intervals_exact']]
for (lo,hi),node in zip(roots,[a,b]):ok(0<lo<=hi and lo**10<=1+node<=hi**10,'exact tenth-root enclosure')
coeffs=[]
for j,(ca,cb)in enumerate(forms):
 ends=[ca*x+cb*y for x in roots[0]for y in roots[1]];box=[min(ends),max(ends)];coeffs.append(box)
 ok(box==list(map(Q,r['coefficient_intervals_exact'][j])),'coefficient enclosure '+str(j))
 ok((box[1]<0)if j==1 else(box[0]>0),'coefficient sign '+str(j))
mom=own['output']['tensor_energies'];ok([m['order']for m in mom]==[0,1,2,3],'moment ordering')
terms=[];choices=[]
for j,m in enumerate(mom):
 lo,hi=Q(m['lower_exact']),Q(m['upper_exact']);ok(0<=lo<=hi,'moment interval')
 terms.append(max(c*x for c in coeffs[j]for x in [lo,hi]));choices.append('lower'if coeffs[j][1]<0 else'upper')
upper=sum(terms);ok(upper==Q(r['energy_upper_exact']),'signed moment sum');ok(choices==r['moment_choices'],'sign-aware choices')
lo,hi=map(Q,r['fractional_norm_interval_exact']);dl,dh=map(Q,r['fractional_display'])
ok(str(lo)==str(Q(ref['fractional_norm_interval_exact'][0])),'prior exact lower')
ok(0<=dl<=lo<=hi<=dh and hi*hi>=upper,'outward fractional norm')
ok(hi<Q(ref['fractional_norm_interval_exact'][1]),'strictly sharper upper')
for p in [Path(__file__),B/'PROOF.md',B/'formal/README.md']:bind(p)
for n,z in files.items():ok(h(R/n)==z,'final binding '+n)
out={'status':'PASS','started_utc':start,'finished_utc':stamp(),'elapsed_seconds':perf_counter()-timer,'checks':checks,'source':r['source'],'fractional_display':r['fractional_display'],'coefficient_signs':['positive','negative','positive','positive'],'moment_choices':choices,'energy_upper_exact':str(upper),'files':dict(sorted(files.items())),'scope':'Independent exact Hermite-basis consequence of admitted whole-plane moments. No new quadrature, optimality or closure claim.'}
with(B/'verification/check_v01.json').open('x')as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k]for k in ['status','started_utc','finished_utc','elapsed_seconds','checks','fractional_display']},indent=2));print('SHA256',h(B/'verification/check_v01.json'))
