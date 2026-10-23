"""Close degree23 gates using the separate native exact determinant records."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
from math import isqrt
import json,gzip,hashlib,resource,sys,traceback
from flint import fmpq
from degree23_inputs import certificate
from degree23_algebra import dp,coeffpoly
from exact_degree21 import prim,decode,degree,univ,shifted,divexact,h
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)
R=Path('research/degree23_grouped_moment_obstruction');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
checks=[];bound={};stats=Counter();outer_rows=[];gcd_rows=[];started=utc()
def ck(name,b,e=None):
 checks.append(dict(name=name,passed=bool(b),evidence=e))
 if not b:raise AssertionError((name,e))
def bind(p,digest=None):
 p=str(p);current=sha(p);ck('binding '+p,digest is None or current==digest);bound[p]=current
 return json.loads(gzip.decompress(Path(p).read_bytes())if p.endswith('.gz')else Path(p).read_bytes())
def gate(p,n=None):
 d=bind(p);ck(str(p)+' PASS',d['status']=='PASS');ck(str(p)+' count',d['count']==len(d['checks'])and(n is None or d['count']==n));ck(str(p)+' all true',all(v['passed']for v in d['checks']));return d

def restore(core,rows):
 out=core
 for d in rows:out*=dp(d['factor'])**d['power']
 return prim(out)
def modproduct(a,b,p):
 out=[0]*(len(a)+len(b)-1)
 for i,c in enumerate(a):
  for j,d in enumerate(b):out[i+j]=(out[i+j]+c*d)%p
 return out

def bezout(F,G,D,record,label):
 A=prim(divexact(F,D));B=prim(divexact(G,D));a=univ(A);b=univ(B);p=record['prime'];s=record['s'];t=record['t']
 ck(label+' prime',p>1 and all(p%j for j in range(2,isqrt(p)+1)))
 ck(label+' exact cofactor degrees',record['cofactor_degrees']==[len(a)-1,len(b)-1])
 ck(label+' leading coefficients retained',a[-1]%p!=0 and b[-1]%p!=0)
 ck(label+' canonical witness residues',all(type(x)is int and 0<=x<p for x in s+t))
 aa=modproduct(s,[x%p for x in a],p)if s else[];bb=modproduct(t,[x%p for x in b],p)if t else[]
 total=[((aa[i]if i<len(aa)else 0)+(bb[i]if i<len(bb)else 0))%p for i in range(max(len(aa),len(bb)))]
 while total and total[-1]==0:total.pop()
 ck(label+' recomputed Bezout equals1',total==[1]);gcd_rows.append(dict(name=label,prime=p,cofactor_degrees=[len(a)-1,len(b)-1],full_gcd_degree=degree(D,2)))

def save(status):
 for p,digest in bound.items():
  if sha(p)!=digest:raise AssertionError('file changed during closure '+p)
 obj=dict(status=status,started_utc=started,finished_utc=utc(),count=len(checks),checks=checks,bindings=bound,statistics=dict(stats),outer_identities=outer_rows,gcd_certificates=gcd_rows,scope='Degree23 finite node system excluded for integer n>=1; finite auxiliary d>=25,P>=27/2 only with prior reductions. Principal full-plane problem unresolved. Final model review still required.')
 (V/'CLOSURE_NATIVE_CHECKS.json').write_text(json.dumps(obj,indent=2)+'\n')
try:
 for p in [R/'PROOF.md',R/'DESIGN_REVIEW_RESOLUTION_PROOF.md',R/'ELIMINATION_STAGE_PROOF.md',R/'OUTER_CHECKPOINT_PROOF.md',R/'CLOSURE_PROOF.md',R/'NATIVE_DETERMINANT_PROOF.md',R/'NATIVE_CLOSURE_PROOF.md',R/'NATIVE_REVIEW_RESOLUTION_PROOF.md',Path('independent_code/check_degree23_outer_native.py'),Path('independent_code/degree23_native_determinant.py'),Path(__file__),Path('independent_code/degree23_algebra.py'),Path('independent_code/exact_degree21.py'),Path('independent_code/degree23_inputs.py')]:bound[str(p)]=sha(p)
 inputs=bind(V/'INPUTS.json');ck('62 frozen source files',len(inputs['files'])==62)
 for row in inputs['files']:
  p=Path(row['frozen']);raw=p.read_bytes();ck('compressed source hash '+row['source'],len(raw)==row['compressed_bytes']and hashlib.sha256(raw).hexdigest()==row['compressed_sha256']);plain=gzip.decompress(raw);ck('uncompressed source hash '+row['source'],len(plain)==row['bytes']and hashlib.sha256(plain).hexdigest()==row['sha256']);bound[str(p)]=sha(p)
 parent=gate('research/degree21_grouped_moment_obstruction/verification/FINAL_CHECKS.json',158)
 for row in parent['bindings']:ck('degree21 parent '+row['path'],sha(row['path'])==row['sha256']);bound[row['path']]=row['sha256']
 review=gate('research/degree21_grouped_moment_obstruction/verification/REVIEW_BINDINGS.json',159)
 for row in review['files']:ck('degree21 reviewed '+row['path'],sha(row['path'])==row['sha256']);bound[row['path']]=row['sha256']
 lemma=gate('research/report79_new_lemma_audit/verification/LEMMA_CHECKS.json',5307)
 lb=bind('research/report79_new_lemma_audit/verification/FINAL_BINDINGS.json')
 for row in lb['files']:ck('lemma final '+row['path'],sha(row['path'])==row['sha256']);bound[row['path']]=row['sha256']
 pg=gate(V/'PARTITION_CHECKS.json',455);parts=bind(V/'PARTITIONS.json');survivors=[x for x in parts if not x['excluded_by_lemma']]
 ck('153 patterns49 survivors',len(parts)==153 and len(survivors)==49)
 ck('survivor full tuple coverage',pg['survivors']==survivors)
 for key,path in [('inputs_sha256',V/'INPUTS.json'),('reader_sha256','independent_code/degree23_inputs.py'),('driver_sha256','independent_code/check_degree23_partitions.py'),('proof_sha256',R/'PROOF.md')]:ck('partition '+key,sha(path)==pg[key]);bound[str(path)]=pg[key]
 enumtypes=Counter(x['type']for x in survivors)
 ck('structural type counts',enumtypes==Counter({'I':12,'II':22,'III':1,'IV':5,'V':2,'VI':4,'V5':1,'VI4':1,'exceptional_remaining':1}))
 ng=gate('research/degree21_grouped_moment_obstruction/verification/UNIVERSAL_NEWTON.json',320);ck('Newton library',ng['library_sha256']==sha('independent_code/exact_degree21.py'))
 om=gate(V/'OUTER_MANUFACTURES.json',10)
 for key,path in [('driver_sha256','independent_code/check_degree23_outer.py'),('proof_sha256',R/'OUTER_CHECKPOINT_PROOF.md')]:ck('outer manufacture '+key,sha(path)==om[key]);bound[str(path)]=om[key]
 native_m=bind(V/'native/MANUFACTURES.json');ck('native manufactures PASS138',native_m['status']=='PASS_MANUFACTURES_AND_TIMINGS_ONLY'and native_m['count']==len(native_m['checks'])==138 and all(z['passed']for z in native_m['checks']))
 for p,d in native_m['bindings'].items():ck('native manufacture current '+p,sha(p)==d);bound[p]=d
 source_manifest=bind(V/'native/PRIMARY_SOURCES.json')
 expected_common={str(p)for p in [Path('independent_code/check_degree23_outer_native.py'),Path('independent_code/degree23_native_determinant.py'),Path('independent_code/exact_degree21.py'),R/'NATIVE_DETERMINANT_PROOF.md',R/'NATIVE_REVIEW_RESOLUTION_PROOF.md',R/'NATIVE_CLOSURE_PROOF.md',R/'OUTER_CHECKPOINT_PROOF.md',V/'native/MANUFACTURES.json',V/'native/PRIMARY_SOURCES.json']}
 for source in source_manifest:
  if 'sha256'in source:
   source_path=V/'native'/source['name'];ck('native source '+source['name'],sha(source_path)==source['sha256']);expected_common.add(str(source_path));bound[str(source_path)]=source['sha256']
 index=bind(V/'RECONSTRUCTION_INDEX.json');ck('reconstruction complete status',index['status']=='PASS');ck('reconstruction full case names',Counter(z['name']for z in index['cases'])==Counter(p['id']for p in survivors))
 expected_jobs={'I':1,'II':1,'III':2,'IV':2,'V':2,'VI':6,'V5':2,'VI4':6,'exceptional':0}
 for row in survivors:
  cid=row['id'];d=certificate(cid);kind=d['type'];cf=V/'cases'/(cid+'.json.gz');case=bind(cf)
  ck(cid+' reconstruction PASS',case['status']=='PASS'and case['count']==len(case['checks'])and all(x['passed']for x in case['checks']))
  ck(cid+' name',case['name']==cid)
  for p,digest in case['bindings'].items():ck(cid+' case binding '+p,sha(p)==digest);bound[p]=digest
  item=next(x for x in index['cases']if x['name']==cid);ck(cid+' index bytes',item['path']==str(cf)and item['sha256']==sha(cf)and item['status']=='PASS'and item['bindings_current'])
  ck(cid+' job count',len(case['jobs'])==expected_jobs[kind]);stats['cases']+=1;stats['reconstruction_assertions']+=case['count'];stats['outer_jobs']+=len(case['jobs'])
  coredata=d['derivative_numerator']if kind=='exceptional'else d['Lambda'];core=coeffpoly(coredata);co=univ(core);shift=shifted(co,25)
  ck(cid+' shift25 full coefficients',coredata['shift']==25 and shift==list(map(int,coredata['shifted_coefficients_low_to_high']))and min(shift)==int(coredata['least_shifted_coefficient']))
  if 'alternative_positive_shift'in coredata:
   stats['integer_exceptions']+=1;ck(cid+' specified integer exception',cid in ['1_3_3_1_1_1_1_1','1_2_2_1_1_1_1_1_1_1']);ss=shifted(co,26);ck(cid+' shift26 positivity',coredata['alternative_positive_shift']==26 and min(ss)>0 and min(ss)==int(coredata['least_coefficient_at_alternative_shift']));ck(cid+' eta25 nonzero',shift[0]<0);ck(cid+' all remaining integer eta',23+2*2>=26)
  else:ck(cid+' shift25 positive',min(shift)>0);stats['positive_real_patterns']+=1
  expected_targets={};case_labels={z['name']:z['passed']for z in case['checks']}
  if kind in ['I','II','III']:
   expected_targets[cid+' final']=restore(core,d['resultant_removed'])
   if kind=='III':expected_targets[cid+' zero pivot']=prim(coeffpoly(d['extra']['branch']))
  elif kind!='exceptional':
   expected_targets.update({cid+' finalH':prim(dp(d['final_resultants'][0])),cid+' finalJ':prim(dp(d['final_resultants'][1]))})
   for inner_index in range(3):ck(cid+' inner downstream linkage'+str(inner_index),case_labels.get(cid+' normalized full inner'+str(inner_index))is True)
  if kind in ['IV','VI','VI4']:
   for br in d['extra']['branches']:
    blabel=cid+' L'+str(br['zero'])+'zero'
    if 'resultants'in br:
     expected_targets[blabel+' finalH']=prim(coeffpoly(br['resultants'][0]));expected_targets[blabel+' finalJ']=prim(coeffpoly(br['resultants'][1]))
    else:
     for residual_index in range(2):ck(blabel+' direct residual linkage'+str(residual_index),case_labels.get(blabel+' substituted residual polynomial '+str(residual_index))is True)
  ck(cid+' exact expected job names',Counter(z['name']for z in case['jobs'])==Counter(expected_targets.keys()))
  for job in case['jobs']:ck(job['name']+' direct target downstream linkage',decode(job['resultant'])==expected_targets[job['name']])
  for j,job in enumerate(case['jobs']):
   label=job['name'];of=V/'outer_native'/(cid+'__'+str(j)+'.json.gz');o=bind(of);f,g=decode(job['f']),decode(job['g']);i=job['var'];m,n=degree(f,i),degree(g,i);a,b=degree(f,2),degree(g,2);B=n*a+m*b;target=decode(job['resultant'])
   ck(label+' outer PASS',o['status']=='PASS'and o['count']==len(o['checks'])and all(x['passed']for x in o['checks']))
   ck(label+' precise name',o['name']==label)
   ck(label+' complete binding set',set(o['bindings'])==expected_common|{str(cf)})
   ck(label+' case binding',o['bindings'][str(cf)]==sha(cf))
   for p,digest in o['bindings'].items():ck(label+' outer binding '+p,sha(p)==digest);bound[p]=digest
   ck(label+' variable schema',i in [0,1]and len(f.degrees())==len(g.degrees())==3)
   ck(label+' formal degrees',m>0 and n>0 and o['degrees']==job['degrees']==[m,n,a,b])
   ck(label+' degree bound',o['bound']==job['bound']==B and o['target_degree']==degree(target,2)<=B)
   ck(label+' Bplus1 consecutive samples',[z['eta']for z in o['points']]==list(range(25,25+B+1)))
   ck(label+' native runtime',o['algorithm']=='flint_fmpz_mat_det_proved'and o['python_flint']=='0.9.0'and o['flint']=='3.6.0'and o['flint_threads']==1)
   ck(label+' native driver binding',o['bindings']['independent_code/check_degree23_outer_native.py']==sha('independent_code/check_degree23_outer_native.py'))
   ck(label+' sample records',all(z['algorithm']=='flint_fmpz_mat_det_proved'and len(z['determinant_sha256'])==64 for z in o['points']))
   ck(label+' fixed nonzero normalization',fmpq(o['constant'])!=0 and o['normalization_point']in range(25,25+B+1))
   labels={z['name']:z['passed']for z in o['checks']}
   for eta in [25,26,27]:ck(label+' Gaussian'+str(eta),labels.get('independent Gaussian eta'+str(eta))is True)
   for eta in {25,26,27,25+B//2,25+B}:
    recpoint=next(z for z in o['points']if z['eta']==eta);ck(label+' Bareiss'+str(eta),labels.get('independent Bareiss eta'+str(eta))is True and recpoint['bareiss_divisions']>=0 and recpoint['bareiss_swaps']>=0)
   for point_record in o['points']:
    pred=point_record['dispatch'];dim=m+n;bits=pred['max_entry_bits'];expected_branch='cofactor'if dim<5 else 'bareiss'if dim<25 else 'modular_proved'if dim<60 or dim<bits else 'modular_accelerated_proved'
    ck(label+' dispatch schema'+str(point_record['eta']),pred['dimension']==dim and type(bits)is int and bits>=0 and pred['source_dispatch_prediction']==expected_branch)
    if point_record['native_value_is_zero']:ck(label+' zero Bareiss'+str(point_record['eta']),labels.get('independent Bareiss eta'+str(point_record['eta']))is True and point_record['bareiss_divisions']>=0 and point_record['bareiss_swaps']>=0)
   for eta in range(25,25+B+1):ck(label+' determinant record'+str(eta),labels.get(('exact determinant eta'if eta>=o['normalization_point']else'both zero before normalization eta')+str(eta))is True)
   stats['outer_assertions']+=o['count'];stats['exact_samples']+=len(o['points']);outer_rows.append(dict(name=label,path=str(of),sha256=sha(of),bound=B,target_degree=degree(target,2),constant=o['constant'],samples=len(o['points'])))
  records={z['name']:z for z in case['gcd_certificates']if'prime'in z};ck(cid+' no duplicate gcd labels',len(records)==sum('prime'in z for z in case['gcd_certificates']))
  expected_gcd=0
  if kind in ['IV','V','VI','V5','VI4']:
   F,G=[prim(dp(z))for z in d['final_resultants']];D=restore(core,d['gcd_removed']);label=cid+' full gcd';ck(label+' present',label in records);bezout(F,G,D,records[label],label);expected_gcd+=1
  if kind in ['IV','VI','VI4']:
   for br in d['extra']['branches']:
    stats['zero_branches']+=1;label=cid+' L'+str(br['zero'])+'zero exact gcd';bd=coeffpoly(br['gcd']);ck(label+' primitive core1',bd==1)
    F,G=[prim(dp(z))for z in br['residuals']]if'residuals'in br else[coeffpoly(z)for z in br['resultants']]
    D=restore(bd,br['removed']);ck(label+' present',label in records);bezout(F,G,D,records[label],label);expected_gcd+=1
  ck(cid+' exact gcd coverage',len(records)==expected_gcd);stats['gcd_certificates']+=len(records)
  print('CLOSED',cid,utc(),flush=True)
 ck('82 outer identities',stats['outer_jobs']==len(outer_rows)==82)
 ck('33 exact gcd certificates',stats['gcd_certificates']==len(gcd_rows)==33)
 ck('20 zero branches',stats['zero_branches']==20)
 ck('two integer exceptions47 positive patterns',stats['integer_exceptions']==2 and stats['positive_real_patterns']==47)
 oi=bind(V/'OUTER_NATIVE_INDEX.json');ck('native index complete',oi['status']=='COMPLETE_REQUIRES_FINAL_COVERAGE_GATE');ck('outer index exact coverage',Counter(z['path']for z in oi['jobs'])==Counter(z['path']for z in outer_rows))
 ck('native index complete binding set',set(oi['bindings'])==expected_common)
 for p,d in oi['bindings'].items():ck('native index binding '+p,sha(p)==d);bound[p]=d
 for row in oi['jobs']:ck('outer index bytes '+row['path'],sha(row['path'])==row['sha256']and row['status']=='PASS')
 ck('reconstruction count index',index['count']==stats['reconstruction_assertions'])
 ck('outer index assertion and sample counts',oi['count']==stats['outer_assertions']and oi['samples']==stats['exact_samples'])
 save('PASS_PENDING_FINAL_MODEL_REVIEW');print('CLOSURE',len(checks),dict(stats),utc(),flush=True)
except BaseException:
 save('FAIL_OR_INCOMPLETE');(V/'closure_native.traceback.txt').write_text(traceback.format_exc());raise
