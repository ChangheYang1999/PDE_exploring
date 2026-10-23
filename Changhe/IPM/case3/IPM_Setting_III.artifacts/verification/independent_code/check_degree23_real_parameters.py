"""Independent exact existence certificates for two noninteger node systems.

Candidate JSON supplies rational boxes and root centers. No producer proof code,
Jacobian inverse or asserted interval bound is used.
"""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys,resource,json,gzip,hashlib,traceback
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
from degree23_inputs import certificate
from degree23_algebra import regular,Q,prim,dp,degree
from rational_node_intervals import Interval,Rectangle,rational,polynomial,qvalue,taylor_at,fixed_point
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)
R=Path('research/degree23_real_parameter_audit');V=R/'verification';P=Path('research/degree23_grouped_moment_obstruction')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
files=[R/'PROOF.md',R/'DESIGN_REVIEW_RESOLUTION_PROOF.md',R/'GENERAL_IDENTITY_CLARIFICATION_PROOF.md',P/'PROOF.md',P/'verification/INPUTS.json',V/'INTERVAL_MANUFACTURES.json',Path(__file__),Path('independent_code/rational_node_intervals.py'),Path('independent_code/degree23_algebra.py'),Path('independent_code/degree23_inputs.py'),Path('independent_code/exact_degree21.py'),Path('research/degree21_grouped_moment_obstruction/verification/UNIVERSAL_NEWTON.json')]
bindings={str(p):sha(p)for p in files}
ids=['1_3_3_1_1_1_1_1','1_2_2_1_1_1_1_1_1_1'];selected=set(sys.argv[1:])if len(sys.argv)>1 else set(ids)
summary=[]
for cid in ids:
 out=V/('INDEPENDENT_REAL_'+cid+'.json.gz')
 if out.exists():
  old=json.loads(gzip.decompress(out.read_bytes()))
  if old.get('status')=='PASS'and old.get('bindings')==bindings and all(z['passed']for z in old['checks']):
   print('REUSE',cid,utc(),flush=True);summary.append(dict(name=cid,path=str(out),sha256=sha(out),count=old['count']));continue
 if cid not in selected:continue
 if out.exists():out.rename(out.with_name(out.name+'.before_'+utc().replace(':','-')))
 checks=[];evidence={};started=utc()
 def ck(name,b,e=None):
  checks.append(dict(name=name,passed=bool(b),evidence=e))
  if not b:raise AssertionError(name)
 def save(status):
  obj=dict(name=cid,status=status,started_utc=started,updated_utc=utc(),count=len(checks),checks=checks,evidence=evidence,bindings=bindings)
  tmp=out.with_suffix('.tmp');tmp.write_bytes(gzip.compress((json.dumps(obj,indent=1,default=str)+'\n').encode(),compresslevel=6,mtime=0));tmp.replace(out)
 print('START',cid,started,flush=True);save('RUNNING')
 try:
  gate=json.loads((V/'INTERVAL_MANUFACTURES.json').read_text());ck('96 manufactured checks PASS',gate['status']=='PASS'and gate['count']==96 and all(v['passed']for v in gate['checks']))
  for p,digest in gate['bindings'].items():ck('manufacture binding '+p,sha(p)==digest)
  ng=json.loads(Path('research/degree21_grouped_moment_obstruction/verification/UNIVERSAL_NEWTON.json').read_text());ck('Newton320 exact PASS',ng['status']=='PASS'and ng['count']==320 and all(v['passed']for v in ng['checks']))
  ck('Newton library binding',ng['library_sha256']==sha('independent_code/exact_degree21.py'))
  d=certificate(cid);real=certificate(cid+'_real');pat=d['pattern'];mu=[3,3,1,1,1,1,1]if cid==ids[0]else[2,2,1,1,1,1,1,1,1]
  ck('specified tuple',pat['A0']==1 and Counter(pat['mu'])==Counter(mu)and pat['e']==len(mu)-1)
  ck('real and algebraic tuple',real['pattern']==pat)
  ck('total degree23',pat['A0']+2*sum(mu)==23)
  built=regular(d,ck,cid);eq=built['equations'];groups=built['groups'];e=pat['e'];m=e-1
  ck('two independent unknowns',len(eq)==2 and all(degree(f,1)<=0 for f in eq))
  ck('two-class structure',built['singletons']==[]and len(groups)==2 and len(groups[0][1])==3 and len(groups[1][1])==m+1 and groups[0][0]!=groups[1][0])
  ck('real certificate equations',len(real['equations'])==2 and all(prim(dp(stored))==f for stored,f in zip(real['equations'],eq)))
  center=list(map(rational,real['krawczyk']['center']));radius=rational(real['krawczyk']['radius'])
  ck('two exact center coordinates',len(center)==2);ck('radius10minus80',radius==rational(1)/10**80)
  result=fixed_point(eq,center,radius);box=result['box']
  ck('eta box strictly between25and26',25<box[2].lo<box[2].hi<26)
  ck('T positive throughout box',(box[2]-23).lo>2)
  ck('Jacobian inverse exact',all(sum(result['Y'][i][k]*result['J0'][k][j]for k in range(2))==int(i==j)for i in range(2)for j in range(2)))
  ck('strict contraction',0<=result['q']<1)
  ck('strict self inclusion',all(v>0 for v in result['margins']))
  evidence['fixed_point']=dict(center=list(map(str,center)),radius=str(radius),parameter_box=[z.saved()for z in [box[0],box[2]]],n_interval=((box[2]-23)/2).saved(),jacobian_determinant=str(result['determinant']),jacobian_center=[[str(v)for v in row]for row in result['J0']],inverse_jacobian=[[str(v)for v in row]for row in result['Y']],jacobian_box=[[v.saved()for v in row]for row in result['J']],error_matrix=[[v.saved()for v in row]for row in result['E']],row_bounds=list(map(str,result['row_bounds'])),kappa=str(result['q']),newton_displacement=list(map(str,result['b'])),strict_margins=list(map(str,result['margins'])))
  for k in range(1,e-1):ck('identically solved moment'+str(k),built['moments'][k]==0)
  for j,k in enumerate([e-1,e]):
   qq=built['moments'][k];ratio=Q(qq.n,eq[j]);den=polynomial(qq.d,box)
   ck('primitive numerator removes only constant '+str(k),degree(ratio.n,0)<=0 and degree(ratio.n,1)<=0 and degree(ratio.n,2)<=0 and ratio.n!=0 and degree(ratio.d,0)<=0 and degree(ratio.d,1)<=0 and degree(ratio.d,2)<=0)
   ck('moment denominator away from zero '+str(k),not den.contains(0))
  group_bounds={};coefficient_records=[]
  for j,(weight,co)in enumerate(groups):
   qco=[]
   for k,q in enumerate(co):
    den=polynomial(Q(q).d,box);ck(f'class{j} coefficient{k} denominator nonzero',not den.contains(0));ival=qvalue(Q(q),box);qco.append(ival)
   ck('monic class'+str(j),qco[0]==1)
   group_bounds[weight]=(j,qco);coefficient_records.append(dict(polynomial=j,weight=weight,degree=len(co)-1,coefficients=[v.saved()for v in qco]))
  evidence['class_coefficient_boxes']=coefficient_records
  disks=real['root_disks'];ck('total number of root disks',len(disks)==e+1)
  ck('disk counts by weight',Counter(z['weight']for z in disks)==Counter({w:len(co)-1 for w,co in groups}))
  ck('all disk weight sum',1+sum(z['weight']for z in disks)==23)
  parsed=[];rootrecords=[]
  for j,disk in enumerate(disks):
   weight=disk['weight'];ck('assigned class weight'+str(j),weight in group_bounds)
   gi,co=group_bounds[weight];cre,cim=map(rational,disk['center']);rad=rational(disk['radius']);ck('disk radius'+str(j),rad==rational(1)/10**65)
   expanded=taylor_at(co,Rectangle(cre,cim));upper=[v.upper()for v in expanded];lower=expanded[1].lower();tail=sum((upper[k]*rad**k for k in range(2,len(upper))),rational(0));margin=lower*rad-upper[0]-tail
   ck('nonzero linear coefficient'+str(j),lower>0);ck('strict Rouche inequality'+str(j),margin>0)
   for label,forbidden in [('zero',Interval(0)),('eta_minus_one',box[2]-1),('eta',box[2])]:
    distance=max((Interval(cre)-forbidden).lower(),abs(cim));ck('disk avoids '+label+' '+str(j),distance>rad)
   parsed.append(dict(polynomial=gi,weight=weight,center=(cre,cim),radius=rad))
   rootrecords.append(dict(polynomial=gi,weight=weight,center=[str(cre),str(cim)],radius=str(rad),constant_bound=str(upper[0]),linear_lower_bound=str(lower),tail_bound=str(tail),strict_margin=str(margin),constant_relative_to_linear_circle=str(upper[0]/(lower*rad))))
  for i,a in enumerate(parsed):
   conjugates=[j for j,b in enumerate(parsed)if b['polynomial']==a['polynomial']and b['weight']==a['weight']and b['center']==(a['center'][0],-a['center'][1])and b['radius']==a['radius']]
   ck('unique conjugate disk '+str(i),len(conjugates)==1)
   ck('real versus paired disk '+str(i),(conjugates[0]==i)==(a['center'][1]==0))
   for j in range(i):
    b=parsed[j];distance=max(abs(a['center'][k]-b['center'][k])for k in range(2));ck(f'disks{i},{j} disjoint',distance>a['radius']+b['radius'])
  evidence['root_disks']=rootrecords
  evidence['scope']='Two-class degree23 node system at real noninteger n in(1,3/2), with all unweighted sums over distinct nodes. No polynomial profile or full-plane PDE existence claim.'
  for p,digest in bindings.items():ck('unchanged '+p,sha(p)==digest)
  save('PASS');summary.append(dict(name=cid,path=str(out),sha256=sha(out),count=len(checks)));print('PASS',cid,len(checks),utc(),flush=True)
 except BaseException:
  save('FAIL');(V/('INDEPENDENT_REAL_'+cid+'.traceback.txt')).write_text(traceback.format_exc());raise
(V/'REAL_INDEX.json').write_text(json.dumps(dict(utc=utc(),status='PASS_PENDING_FINAL_REVIEW'if len(summary)==2 else'PARTIAL',cases=summary,count=sum(z['count']for z in summary),bindings=bindings),indent=2)+'\n')
