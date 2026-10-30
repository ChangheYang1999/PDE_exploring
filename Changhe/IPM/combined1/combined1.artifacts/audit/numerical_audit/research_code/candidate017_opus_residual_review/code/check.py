"""Own exact radial fixture arithmetic and source regularity; no peer execution."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
from collections import Counter
from math import factorial
import json,os,time,sys
R=Path(__file__).resolve().parents[3];B=R/'research/candidate017_opus_residual_review'
sys.set_int_max_str_digits(0)
assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
start=time.monotonic();inputs={};checks={};terms=0

def bind(p,h=None):
 p=Path(p);p=p if p.is_absolute() else R/p
 assert p.resolve().is_relative_to(R)
 value=sha256(p.read_bytes()).hexdigest();assert h is None or value==h,(p,h,value)
 rel=str(p.relative_to(R));assert rel not in inputs or inputs[rel]==value;inputs[rel]=value;return p

def read(p,h=None):return json.loads(bind(p,h).read_text())
def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k

def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,Q(0))+v
 return {k:v for k,v in d.items() if v}
def scale(p,a):return {k:Q(a)*v for k,v in p.items() if a*v}
def mul(p,q):
 out={}
 for (m,e),c in p.items():
  for (n,f),d in q.items():out[m+n,e+f]=out.get((m+n,e+f),Q(0))+c*d
 return {k:v for k,v in out.items() if v}
def sq(p):return mul(p,p)
def shift(p,m):return {(i+m,e):v for (i,e),v in p.items()}
def deriv(p):
 out=[]
 for (m,e),c in p.items():out.extend([{(m-1,e):m*c},{(m+1,e-1):2*e*c}])
 return add(*out)
def lap(p,n):return add(deriv(deriv(p)),shift(deriv(p),-1),scale(shift(p,-2),-n*n))
def poly(rows):return add(*[{(int(m),Q(e)):Q(c)} for m,e,c in rows])
def integral(p):
 global terms
 z=Q(0)
 for (m,e),c in p.items():
  A=Q(m+1,2);s=-e
  assert A.denominator==1 and A>0 and s>A,(m,e,c)
  A=int(A);den=Q(2)
  for j in range(1,A+1):den*=s-j
  z+=c*factorial(A-1)/den;terms+=1
 return z

def parts(u,f,n):
 up=deriv(u);uyy=add(shift(deriv(up),1),up)
 return {'d':integral(add(shift(sq(up),1),scale(shift(sq(u),-1),n*n))),
         'p':integral(shift(mul(f,u),1)),
         'a':integral(shift(add(sq(up),scale(sq(uyy),Q(1,n*n))),1)),
         'b':integral(scale(shift(mul(f,uyy),2),Q(1,n*n))),
         'Q':integral(shift(sq(f),3)),
         'R2':integral(shift(sq(add(f,lap(u,n))),3))}

def le_sum(X,Y,Z):return X<=Y+Z or (X-Y-Z)**2<=4*Y*Z
assert not (B/'verification/result.json').exists()
first=read(B/'verification/PROOF_FIRST.json');ck('proof_first',not first['checker_exists'] and not first['result_exists'])
bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
man=read(B/'source/MANIFEST.json',first['manifest_sha256'])
for rel,h in man['files'].items():bind(rel,h)
fixtures=read(B/'source/fixtures.json');t2=read(B/'source/T2_results.json');t1=read(B/'source/T1_extract.json')
ck('T2_documented_checks',t2['checks']==18 and t2['fails']==[])
ck('T1_documented_checks','checks 79 failures 0' in (B/'source/T1_log.txt').read_text() and 'RESULT PASS' in (B/'source/T1_log.txt').read_text())
ck('old_T2_missing_factor_literal','= sqrt(Qn (a + d))' in (B/'source/T2_review_v01.md').read_text())
ck('integrator_fixture',integral({(1,Q(-2)):Q(1)})==Q(1,2) and integral({(3,Q(-3)):Q(1)})==Q(1,4))
results={}
for row in fixtures['external']:
 name=row['name'];n=row['n'];u=poly(row['u']);f=poly(row['f']);out=parts(u,f,n)
 for k,v in out.items():ck(name+':'+k,v==Q(t2['examples'][name][k]))
 ck(name+':identity',out['R2']==out['Q']+2*n*n*(out['b']-out['p'])+n*n*(out['a']+out['d']))
 ck(name+':lap_square',integral(shift(sq(lap(u,n)),3))==n*n*(out['a']+out['d']))
 results[name]={k:str(v) for k,v in out.items()}
for i,row in enumerate(t2['trial_family_orders']):
 n,k,beta=row['n'],row['k'],Q(row['beta']);alpha=3-2*beta;power=3+2*k
 ck(f'asymptotic{i}:admissible',beta>Q(3,2) and k>=-1 and power>=n and (power-n)%2==0)
 ck(f'asymptotic{i}:leading',[Q(v) for v in row['lead_inf']]==[alpha**2+n*n,alpha**2+alpha**4/(n*n),(alpha**2-n*n)**2])
 ck(f'asymptotic{i}:boundary',row['bdry_0']==row['bdry_inf']=='0' and 2*power>0 and 6-4*beta<0)
x=fixtures['riesz'];n=x['n'];u=poly(x['u']);w=poly(x['w']);f=scale(lap(w,n),-1);out=parts(u,f,n)
for k,v in out.items():ck('riesz:'+k,v==Q(t2['riesz_example'][k]))
H=parts(w,{},n)['d'];g=add(w,scale(u,-1));Hg=parts(g,{},n)['d']
ck('riesz:H2',H==Q(t2['riesz_example']['H2_over_pi'])==Q(4,15))
ck('riesz:residual_H2',Hg==Q(t2['riesz_example']['residual_H2_over_pi'])==Q(9,280))
ck('riesz:triangle',le_sum(H,out['d'],out['R2']) and le_sum(out['d'],H,out['R2']))
ck('riesz:duality',out['p']**2<=H*out['d'])
ck('riesz:Hardy',Hg<=out['R2']/(n*n))
results['riesz']={**{k:str(v) for k,v in out.items()},'H2':str(H),'residual_H2':str(Hg)}
x=fixtures['counterexample'];n=x['n'];u=poly(x['u']);f=lap(u,n);out=parts(u,f,n);C=integral(shift(mul(f,f),3))
ck('counterexample:nonzero',out['a']+out['d']>0 and n==3)
ck('counterexample:cross_equality',C==out['Q']==n*n*(out['a']+out['d']))
ck('counterexample:old_false',C*C>out['Q']*(out['a']+out['d']))
ck('counterexample:corrected_equality',C*C==n*n*out['Q']*(out['a']+out['d']))
results['counterexample']={**{k:str(v) for k,v in out.items()},'cross_over_pi':str(C),'old_RHS_over_pi':str(n*(out['a']+out['d'])),'corrected_RHS_over_pi':str(n*n*(out['a']+out['d']))}
rawrel='research/candidate_audits/data/C1-N1-017-legqs50-quot013/quot013_legqs50_m9to15_cpu_m16_exact.json'
raw=read(rawrel,'7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114')
ck('raw_c',Q(raw['cl_exact'])==Q(4076476460239181,2251799813685248)>1)
counts=Counter();radii=set()
for i,g in enumerate(raw['generators']):
 spec=g['spec'];kind=spec[0];m,j=g['m'],g['j'];w=spec[1]
 n=0 if kind=='mono' else spec[2];q=spec[3] if kind in ('legq','legqs') else 0
 rad=Q(spec[4]) if kind=='legqs' else Q(1)
 ck(f'generator{i}:smooth_exact',kind in ('mono','leg','legq','legqs') and len(spec)=={'mono':2,'leg':3,'legq':4,'legqs':5}[kind] and all(type(v) is int and v>=0 for v in (m,j,w,n,q)) and rad in (1,10,25,50,100) and not isinstance(g['coef'],float) and Q(g['coef']).denominator>0)
 counts[kind]+=1;radii.add(rad)
ck('2174generators',len(raw['generators'])==2174)
for p in ['research/joint_scaled_factored_weak/PROOF.md','research/joint_scaled_factored_weak/code/fields_joint.py','research/joint_scaled_factored_weak/code/weak.py']:bind(p)
root=read('research/candidate017_dual_residual_replay/verification/result.json',t1['result_sha256'])
recip=read('research/candidate017_final_reciprocal/verification/result.json','ead4de91e21981335ef4d4ce12a8085929fd5f1d6c64ea3b4bb3421c782c2b74')
for tag,j in [('425',root),('426',recip)]:
 ck(tag+':accepted',all(j['checks'].values()))
 for rel,h in j['inputs'].items():bind(rel,h)
for k in ['raw_sha256','H_lower_square_exact','H_strict_lower_exact','complete_H_upper','complete_E2_and_017_less_than007']:ck('T1:'+k,t1[k]==root[k])
ck('T1:all16modes',len(t1['modes'])==16 and [r['n'] for r in t1['modes']]==list(range(1,32,2)))
S=Q(0)
for a,b in zip(t1['modes'],root['modes'],strict=True):
 n=a['n'];j=read(b['record'],b['sha256'])
 ck(f'T1:n{n}:extract',all(a[k]==b[k] for k in a))
 q=Q(a['quotient_strict_lower_exact']);ck(f'T1:n{n}:positive',q>0 and q==Q(j['dual_quotient_strict_lower_exact']));S+=q*q
 if a['independent_hres']:
  e=t1['residual'][str(n)];rr=j['residual_trial']
  for k in ['H_mode_strict_lower_exact','H_mode_strict_upper_exact']:ck(f'T1:n{n}:{k}',e[k]==rr[k])
  ck(f'T1:n{n}:balltexts',rr['residual_ball']==e['residual_ball_text'] and rr['gradient_ball'].startswith(e['gradient_ball_head']))
  ck(f'T1:n{n}:dual_and_hash',e['record_sha256']==a['sha256'] and Q(e['dual_quotient_strict_lower_exact'])==q)
  lo,hi=Q(rr['H_mode_strict_lower_exact']),Q(rr['H_mode_strict_upper_exact']);ck(f'T1:n{n}:ordered',0<lo<q<hi)
HL=Q(root['H_strict_lower_exact']);ck('T1:lower_square',0<HL*HL<S==Q(root['H_lower_square_exact']))
ck('T1:display',Q('.614419598760')<HL<Q('.614419598761'))
for rel,h in list(inputs.items()):bind(rel,h)
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'checks':checks,'check_count':len(checks),'exact_integrated_terms':terms,'fixtures':results,'source_generator_count':len(raw['generators']),'source_kinds':dict(counts),'positive_source_radii':[str(x) for x in sorted(radii)],'source_local_integrability':'CONFIRMED from smooth finite potential and F odd in y, hence F and each angular projection O(r) at zero','T1_main_analytic_review':'CONFIRMED under stated hypotheses; exact extract independently compared','T2_main_analytic_review':'CONFIRMED under stated hypotheses, with source-origin condition discharged','T2_old_auxiliary_cross_bound':'REFUTED: missing factor n; correct bound n sqrt(Q(a+d)); manufactured n=3 counterexample exact','full_017_upper_E2':'OPEN','peer_code_executed':False,'peer_quadratures_repeated':False,'new_candidate_integrals':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED main analytic reviews, source local regularity and listed finite checks; auxiliary old typo explicitly refuted'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'checks':len(checks),'inputs':len(inputs),'terms':terms,'seconds':out['elapsed_seconds'],'result_sha256':sha256((B/'verification/result.json').read_bytes()).hexdigest(),'counterexample':results['counterexample']},indent=2))
