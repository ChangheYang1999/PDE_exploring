"""Reconstruct all degree23 equations and exact symbolic inner resultants.

Heavy work runs sequentially. Each case is checkpointed independently; final
univariate resultant identities are a separate bound-plus-one determinant gate.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,gzip,resource,traceback,sys
from degree23_inputs import certificate
from degree23_algebra import *
from modular_gcd_certificate_285 import certify
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)
R=Path('research/degree23_grouped_moment_obstruction');V=R/'verification';OUT=V/'cases';OUT.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
BIND_FILES=[R/'PROOF.md',R/'DESIGN_REVIEW_RESOLUTION_PROOF.md',R/'ELIMINATION_STAGE_PROOF.md',V/'INPUTS.json',V/'PARTITION_CHECKS.json',V/'PARTITIONS.json',Path(__file__),Path('independent_code/degree23_algebra.py'),Path('independent_code/exact_degree21.py'),Path('independent_code/modular_gcd_certificate_285.py'),Path('independent_code/degree23_inputs.py'),Path('research/degree21_grouped_moment_obstruction/verification/UNIVERSAL_NEWTON.json')]
bindings={str(p):sha(p)for p in BIND_FILES};checks=[];jobs=[];certs=[]
def ck(name,ok,e=None):
 checks.append(dict(name=name,passed=bool(ok),evidence=e))
 if not ok:raise AssertionError((name,e))
def save(status):
 p=OUT/(name+'.json.gz');obj=dict(status=status,name=name,started_utc=started,updated_utc=utc(),count=len(checks),checks=checks,jobs=jobs,gcd_certificates=certs,bindings=bindings)
 tmp=p.with_suffix('.tmp');tmp.write_bytes(gzip.compress((json.dumps(obj,indent=1)+'\n').encode(),compresslevel=6,mtime=0));tmp.replace(p)

def gauss(a):
 a=[[Fraction(int(v))for v in row]for row in a];out=Fraction(1)
 for k in range(len(a)):
  i=next((i for i in range(k,len(a))if a[i][k]),None)
  if i is None:return Fraction(0)
  if i!=k:a[k],a[i]=a[i],a[k];out=-out
  pivot=a[k][k];out*=pivot
  for i in range(k+1,len(a)):
   fac=a[i][k]/pivot
   for j in range(k+1,len(a)):a[i][j]-=fac*a[k][j]
   a[i][k]=Fraction(0)
 return out

def remove(raw,rows,allowed,eliminated,label):
 ck(label+' raw nonzero',bool(raw));p=raw
 for j,z in enumerate(rows):
  f=dp(z['factor']);power=z['power']
  ck(label+' exact allowed factor '+str(j),bool(f)and type(power)is int and power>=0 and any(prim(f)==prim(a)for a in allowed))
  ck(label+' factor absent eliminated variable '+str(j),all(degree(f,k)<=0 for k in eliminated))
  p=divexact(p,f**power)
  ck(label+' maximal stated factor '+str(j),bool(divmod(p,f)[1]))
 p=prim(p);ck(label+' divided nonzero',bool(p));return p

def restore(core,rows,allowed,label):
 out=core
 for j,z in enumerate(rows):
  f=dp(z['factor']);power=z['power'];ck(label+' restored factor '+str(j),type(power)is int and power>=0 and any(prim(f)==prim(a)for a in allowed)and degree(f,0)<=0 and degree(f,1)<=0)
  out*=f**power
 return prim(out)

def positive(data,label,required=True):
 p=coeffpoly(data);ck(label+' primitive positive normalization',p==prim(p));co=univ(p);shift=data['shift'];sh=shifted(co,shift)
 ck(label+' shift25',shift==25);ck(label+' shifted full list',sh==list(map(int,data['shifted_coefficients_low_to_high'])))
 ck(label+' minimum',min(sh)==int(data['least_shifted_coefficient']));ck(label+' positivity flag',all(z>0 for z in sh)==data['all_shifted_coefficients_positive'])
 if required:
  if 'alternative_positive_shift'in data:
   ck(label+' only declared integer exceptions',name in ['1_3_3_1_1_1_1_1','1_2_2_1_1_1_1_1_1_1'])
   alt=data['alternative_positive_shift'];aa=shifted(co,alt)
   ck(label+' alternative shift26',alt==26);ck(label+' alternative all positive',all(z>0 for z in aa));ck(label+' alternative minimum',min(aa)==int(data['least_coefficient_at_alternative_shift']))
   ck(label+' eta25 nonzero negative',sh[0]<0)
   ck(label+' eta25 mod101',sh[0]%101==(98 if len(co)==49 else 56))
   ck(label+' every other admissible integer eta>=27',23+2*2>26)
   vals=data['integer_values_before_alternative_shift'];ck(label+' exact recorded eta25',len(vals)==1 and vals[0]['eta']==25 and int(vals[0]['value'])==sh[0])
   certs.append(dict(name=label+' exceptional integer evaluation',eta=25,value=str(sh[0]),producer_integer_values=vals))
  else:ck(label+' all coefficients positive',all(z>0 for z in sh))
 return p

def queue(f,g,target,i,label):
 f,g=prim(f),prim(g);target=prim(target);m,n=degree(f,i),degree(g,i);a,b=degree(f,2),degree(g,2);bound=n*a+m*b
 ck(label+' positive formal degrees',m>0 and n>0);ck(label+' eliminated other variable absent',degree(f,1-i)<=0 and degree(g,1-i)<=0)
 ck(label+' univariate nonzero target',bool(target)and degree(target,0)<=0 and degree(target,1)<=0)
 ck(label+' target degree bound',degree(target,2)<=bound)
 jobs.append(dict(name=label,f=encode(f),g=encode(g),resultant=encode(target),var=i,degrees=[m,n,a,b],bound=bound))
 return target

def inner(f,g,i,label):
 ck(label+' positive inner degrees',degree(f,i)>0 and degree(g,i)>0)
 mat=sylv(f,g,i);raw,divs,swaps=bareiss(mat)
 ck(label+' exact polynomial determinant nonzero',bool(raw),dict(divisions=divs,swaps=swaps))
 ck(label+' eliminated variable absent',degree(raw,i)<=0)
 for point in [(2,3,25),(-2,4,26),(5,-3,27)]:
  evaluated=[[q(*point)for q in row]for row in mat]
  ck(label+' Fraction Gaussian '+str(point),gauss(evaluated)==Fraction(int(raw(*point))))
 return raw

def gcdf(f,g,target,label):
 z=certify(f,g,target);ck(label+' exact divisions',z['exact_divisions_verified']);ck(label+' explicit Bezout',z['identity_verified']);ck(label+' quotient leading degrees retained',z['leading_degrees_preserved']);certs.append(dict(name=label,**z))

parts=json.loads((V/'PARTITIONS.json').read_text());selected=[p for p in parts if not p['excluded_by_lemma']]
if len(sys.argv)>1:selected=[p for p in selected if p['id']in sys.argv[1:]]
for p in selected:
 name=p['id'];casefile=OUT/(name+'.json.gz')
 if casefile.exists():
  old=json.loads(gzip.decompress(casefile.read_bytes()))
  if old.get('status')=='PASS'and old.get('bindings')==bindings and all(z['passed']for z in old['checks']):print('REUSE',name,old['count'],utc(),flush=True);continue
  archive=casefile.with_name(casefile.name+'.before_'+utc().replace(':','-'));casefile.rename(archive)
 checks=[];jobs=[];certs=[];started=utc();print('START',name,started,flush=True);save('RUNNING')
 try:
  gate=json.loads((V/'PARTITION_CHECKS.json').read_text());ck('partition455PASS',gate['status']=='PASS'and gate['count']==455 and all(z['passed']for z in gate['checks']))
  universal=json.loads(Path('research/degree21_grouped_moment_obstruction/verification/UNIVERSAL_NEWTON.json').read_text())
  ck('universal320PASS',universal['status']=='PASS'and universal['count']==320 and all(z['passed']for z in universal['checks']))
  ck('universal code binding',universal['library_sha256']==sha('independent_code/exact_degree21.py'))
  d=certificate(name);A=p['A0'];T=A*h-23;kind=d['type'];ck('pattern tuple',d['pattern']['A0']==A and Counter(d['pattern']['mu'])==Counter(p['mu'])and d['pattern']['e']==p['e'])
  if kind=='exceptional':
   ck('exceptional unique tuple',name=='1_5_5_1')
   node=Q(h)*(Q(1)-Q(8,T));q=fill(A,[(2,[Q(1),node,node**2])],2,10,2,ck,name+' pair')
   pi_deriv=val(q,h)+(Q(h)-node)*der(q,h)
   pp=positive(d['derivative_numerator'],name+' numerator');ck('exact rational exceptional formula',pi_deriv==Q(pp,dp(d['derivative_denominator'])))
   ck('exceptional denominator 200T2',dp(d['derivative_denominator'])==200*T*T)
   for row in d['integer_evaluations']:
    n=row['n'];eta=row['eta'];text=row['scaled_pi_prime'];a,b=text.replace('(','').replace(')','').split('/')
    ck('integer eta n'+str(n),eta==23+2*n and n in [1,2,3]);ck('exact exceptional n'+str(n),Fraction(int(pi_deriv.n(0,0,eta)),int(pi_deriv.d(0,0,eta)))==Fraction(int(a),int(b)))
  else:
   built=regular(d,ck,name);eq=built['equations'];allowed=built['allowed'];core=positive(d['Lambda'],name+' Lambda')
   if len(eq)==2:
    target=restore(core,d['resultant_removed'],[h,T],name+' resultant');queue(eq[0],eq[1],target,0,name+' final')
    if kind=='III':
     f,g,br=built['pivot'];positive(d['extra']['branch'],name+' zero pivot');queue(f,g,br,0,name+' zero pivot')
   else:
    ri=[];i=built['inner'];outer=built['outer'];pairs=[(0,1),(0,2),(1,2)]
    ck(name+' three inner targets',len(d['inner_resultants'])==len(d['inner_removed'])==3)
    for j,(a,b)in enumerate(pairs):
     raw=inner(eq[a],eq[b],i,name+' inner'+str(j));z=remove(raw,d['inner_removed'][j],allowed,[i],name+' inner'+str(j))
     ck(name+' normalized full inner'+str(j),z==prim(dp(d['inner_resultants'][j])));ri.append(z);save('RUNNING')
    ck(name+' two final targets',len(d['final_resultants'])==2)
    H=queue(ri[0],ri[1],dp(d['final_resultants'][0]),outer,name+' finalH');J=queue(ri[0],ri[2],dp(d['final_resultants'][1]),outer,name+' finalJ')
    target=restore(core,d['gcd_removed'],[h,T],name+' full gcd');gcdf(H,J,target,name+' full gcd')
   if kind in ['IV','VI','VI4']:
    branches=d['extra']['branches'];ck(name+' both zero branches',len(branches)==2 and {z['zero']for z in branches}=={1,2})
    for br in branches:
     label=name+' L'+str(br['zero'])+'zero';bld=singular(d,br,ck,label);q=positive(br['gcd'],label+' normalized gcd');ck(label+' normalized gcd1',q==1)
     target=restore(q,br['removed'],[h,T],label+' restored gcd')
     if bld['substituted']is not None:f,g=bld['substituted']
     else:
      bq=bld['equations'];ck(label+' two resultant records',len(br['resultants'])==2)
      rr=[positive(row,label+' resultant'+str(j),False)for j,row in enumerate(br['resultants'])]
      f=queue(bq[0],bq[1],rr[0],0,label+' finalH');g=queue(bq[0],bq[2],rr[1],0,label+' finalJ')
     gcdf(f,g,target,label+' exact gcd');save('RUNNING')
  for path,digest in bindings.items():ck('binding '+path,sha(path)==digest)
  save('PASS');print('PASS',name,len(checks),'jobs',len(jobs),utc(),flush=True)
 except BaseException:
  save('FAIL');(OUT/(name+'.traceback.txt')).write_text(traceback.format_exc());raise
# This summary is an index; only complete49-case coverage can support the theorem.
rows=[]
for p in [p for p in parts if not p['excluded_by_lemma']]:
 f=OUT/(p['id']+'.json.gz')
 if f.exists():
  z=json.loads(gzip.decompress(f.read_bytes()));rows.append(dict(name=p['id'],path=str(f),sha256=sha(f),status=z['status'],count=z['count'],bindings_current=z['bindings']==bindings))
allpass=len(rows)==49 and all(z['status']=='PASS'and z['bindings_current']for z in rows)
(V/'RECONSTRUCTION_INDEX.json').write_text(json.dumps(dict(utc=utc(),status='PASS'if allpass else'PARTIAL',cases=rows,count=sum(z['count']for z in rows if z['status']=='PASS'),bindings=bindings),indent=2)+'\n')
print('INDEX','PASS'if allpass else'PARTIAL',len(rows),utc(),flush=True)
