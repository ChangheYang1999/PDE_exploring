"""Independent Python-integer hardening and current bindings for result292."""
from pathlib import Path
from fractions import Fraction
from math import comb
from datetime import datetime,timezone
import json,gzip,hashlib,traceback,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)
R=Path('research/degree23_grouped_moment_obstruction');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
checks=[];bindings={};evidence={};started=utc()
def ck(name,b):
 checks.append(dict(name=name,passed=bool(b)))
 if not b:raise AssertionError(name)
def bind(p,expected=None):
 p=str(p);digest=sha(p);ck('binding '+p,expected is None or digest==expected);bindings[p]=digest
 raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw)if p.endswith('.gz')else raw)
def source(cid):
 p=V/'external/d23/certificates'/(cid+'.json.gz');return bind(p)
def canonical(raw):return sorted((tuple(e),int(c))for e,c in raw if int(c))
def bareiss_py(matrix):
 a=[r[:]for r in matrix];sign=1;previous=1;divisions=0
 for k in range(len(a)-1):
  pivot=next((i for i in range(k,len(a))if a[i][k]),None)
  if pivot is None:return 0,divisions
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
  pivot_value=a[k][k]
  for i in range(k+1,len(a)):
   for j in range(k+1,len(a)):
    value=a[i][j]*pivot_value-a[i][k]*a[k][j];q,r=divmod(value,previous)
    ck('Python exact Bareiss division '+str(divisions),r==0);divisions+=1;a[i][j]=q
   a[i][k]=0
  previous=pivot_value
 return sign*a[-1][-1],divisions
def gaussian_py(matrix):
 a=[[Fraction(v)for v in row]for row in matrix];value=Fraction(1)
 for k in range(len(a)):
  pivot=next((i for i in range(k,len(a))if a[i][k]),None)
  if pivot is None:return Fraction(0)
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k];value=-value
  pivot_value=a[k][k];value*=pivot_value
  for i in range(k+1,len(a)):
   multiplier=a[i][k]/pivot_value
   for j in range(k+1,len(a)):a[i][j]-=multiplier*a[k][j]
   a[i][k]=Fraction(0)
 return value
try:
 for p in [Path(__file__),R/'FINAL_REVIEW_RESOLUTION_PROOF.md',R/'FINAL_PUBLICATION_PROOF.md']:
  bindings[str(p)]=sha(p)
 closure=bind(V/'CLOSURE_NATIVE_CHECKS.json');ck('native closure86928 PASS',closure['status']=='PASS_PENDING_FINAL_MODEL_REVIEW'and closure['count']==len(closure['checks'])==86928 and all(z['passed']for z in closure['checks']))
 for p,d in closure['bindings'].items():ck('closure dependency '+p,sha(p)==d);bindings[p]=d
 patterns=bind(V/'PARTITIONS.json');patterns=[z for z in patterns if not z['excluded_by_lemma']];factor_count=0
 for pattern in patterns:
  d=source(pattern['id']);A0=d['pattern']['A0'];ck(pattern['id']+' positive odd A0',type(A0)is int and A0>=1 and A0%2==1)
  ledgers=[(key,d[key])for key in ['resultant_removed','gcd_removed']if key in d]
  ledgers += [('L'+str(br['zero'])+'zero removed',br['removed'])for br in d.get('extra',{}).get('branches',[])]
  allowed=[canonical([[[0,0,1],'1']]),canonical([[[0,0,0],'-23'],[[0,0,1],str(A0)]])]
  for key,rows in ledgers:
   for j,row in enumerate(rows):
    ck(pattern['id']+' '+key+' factor'+str(j),canonical(row['factor'])in allowed)
    ck(pattern['id']+' '+key+' nonnegative power'+str(j),type(row['power'])is int and row['power']>=0);factor_count+=1
 d=source('5_2_2_2_1_1_1')['extra']['branch'];co=list(map(int,d['coefficients_low_to_high']))
 shift=[sum(co[j]*comb(j,k)*25**(j-k)for j in range(k,len(co)))for k in range(len(co))]
 ck('typeIII degree7',len(co)==8 and co[-1]!=0)
 ck('typeIII exact shift25',shift==list(map(int,d['shifted_coefficients_low_to_high'])))
 ck('typeIII strict positivity',all(z>0 for z in shift)and min(shift)==int(d['least_shifted_coefficient']))
 case=bind(V/'cases/1_6_2_2_1.json.gz');job=case['jobs'][0]
 outer=bind(V/'outer_native/1_6_2_2_1__0.json.gz');ck('constant exact minus2power63',Fraction(outer['constant'])==-2**63)
 ck('formal12by12schema',job['var']==0 and job['degrees']==[6,6,9,9])
 rows=[]
 for eta in [25,26,27]:
  coeff=[]
  for key in ['f','g']:
   aa=[0]*7
   for ex,c in job[key]['terms']:
    ck(key+' no other variable at'+str(eta),ex[1]==0 and 0<=ex[0]<=6)
    aa[6-ex[0]]+=int(c)*eta**ex[2]
   coeff.append(aa)
  matrix=[[0]*k+coeff[0]+[0]*(5-k)for k in range(6)]+[[0]*k+coeff[1]+[0]*(5-k)for k in range(6)]
  target=0
  for ex,c in job['resultant']['terms']:
   ck('target univariate eta'+str(eta),ex[0]==ex[1]==0);target+=int(c)*eta**ex[2]
  det,ndiv=bareiss_py(matrix);gauss=gaussian_py(matrix)
  ck('Python determinants agree eta'+str(eta),det==gauss)
  ck('Python constant confirmed eta'+str(eta),target!=0 and det==-(2**63)*target)
  rows.append(dict(eta=eta,determinant=str(det),target=str(target),ratio=str(Fraction(det,target)),bareiss_divisions=ndiv))
 evidence=dict(factor_records=factor_count,zero_pivot_shift=shift,pure_python_constant_checks=rows,trust_base='Native full outer arithmetic shares FLINT. These three 12x12 checks use Python int and Fraction only.')
 for name in ['request.txt','response.json','answer.md','metadata.json']:
  p=V/'opus_final'/name;bindings[str(p)]=sha(p)
 meta=json.loads((V/'opus_final/metadata.json').read_text());ck('actual final Opus5.5 endturn',meta['returned_model']=='claude-opus-5-5'and meta['stop_reason']=='end_turn'and meta['answer_nonempty'])
 for p,d in bindings.items():ck('unchanged '+p,sha(p)==d)
 status='PASS_PENDING_FOCUSED_FINAL_REVIEW'
except BaseException:
 status='FAIL';(V/'FINAL_SUPPLEMENT_TRACEBACK.txt').write_text(traceback.format_exc());raise
finally:
 out=dict(status=status,started_utc=started,finished_utc=utc(),count=len(checks),checks=checks,bindings=bindings,evidence=evidence)
 (V/'FINAL_SUPPLEMENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
 print(status,len(checks),evidence.get('factor_records'),out['finished_utc'],flush=True)
