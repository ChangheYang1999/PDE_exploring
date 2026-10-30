"""Independent exact power/Bernstein replay of proposed uniform budgets."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
from fractions import Fraction
import json,time,os
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/weight_uniform_budget_peer';now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:sha256(p.read_bytes()).hexdigest()
def aq(q):
 q=Q(q);return arb(q.numerator)/arb(q.denominator)
def exact_decimal(value):
 q=Fraction(str(value));return Q(q.numerator,q.denominator)
def main():
 tick=time.monotonic();ctx.prec=1024;inputs={};checks={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def bind(p,expected=None):
  h=sha(p);rel=str(p.relative_to(R));assert expected is None or h==expected,(rel,h,expected)
  assert rel not in inputs or inputs[rel]==h;inputs[rel]=h;return p
 def read(p,expected=None):return json.loads(bind(p,expected).read_text())
 def check(label,ok):assert label not in checks;checks[label]=bool(ok);assert ok,label
 bind(B/'DECIMAL_PROOF_v02.md');pf=read(B/'verification/PROOF_FIRST.json');check('proof_before_checker',not pf['checker_exists']);bind(B/'PROOF.md',pf['proof_sha256']);bind(Path(__file__))
 manifest=read(B/'source/MANIFEST.json')
 for name,rec in manifest['files'].items():bind(B/'source'/name,rec['sha256'])
 peer=read(B/'source/T4_result.json','61803920bea366913555ebb213ac40b466d370b1c92dd5cfe9cc9b67b9895450')
 check('T4_proof_bound',peer['proof_sha256']==sha(B/'source/T4_PROOF.md'))
 check('T4_checker_as_text_bound',peer['checker_sha256']==sha(B/'source/T4_check.py'))
 check('T4_all_reported_checks',all(peer['checks'].values()) and len(peer['checks'])==peer['check_count']==320)
 opus=read(B/'source/T2_result.json');check('Opus_reciprocal_finite_verdict',opus['checks']==52 and not opus['fails'])
 for original,name in [('c1-t4/research/weight_uniform_gram_audit/PROOF.md','T4_PROOF.md'),('c1-t4/research/weight_uniform_gram_audit/verification/result_v02.json','T4_result.json'),('c1-t4/research/weight_uniform_gram_audit/data/parameters.json','T4_parameters.json'),('c1-t4/research/weight_uniform_gram_audit/code/check.py','T4_check.py')]:check('Opus_binding:'+name,opus['inputs'][original]==sha(B/'source'/name))
 params=read(B/'source/T4_parameters.json','554a581e6eea77947e4eb7f9235fc848cc693c7f73a2ed9297b9be800263e1a8')
 accepted=read(R/'research/h18_coverage_peer/verification/result_v02.json','f73dceb02100e4b51ac311f17ab1c47e03329db988a4468daa185d92b03ca438')
 check('own390_accepted',all(accepted['checks'].values()) and accepted['verdict'].startswith('CONFIRMED'))
 for rel,h in accepted['inputs'].items():bind(R/rel,h)
 numbers=[row['number'] for row in accepted['weak_candidates']]
 check('all24fixed_c_candidates',numbers==[n for n in range(2,27) if n!=11])
 for row in accepted['weak_candidates']:
  I,D,H=[Q(row[k]) for k in ['I_lower_exact','D_upper_exact','H_upper_exact']]
  gap=I-D/1000-H/10**6
  check(f'weak_gap_{row["number"]}',gap>0 and gap==Q(row['gap_at_1e_minus3_exact']))
  floor=Q(row['own_root_floor_exact'])
  check(f'weak_floor_{row["number"]}',floor>Q(1,1000) and I-D*floor-H*floor**2>0)
 c0=Q(params['c0']);check('same_c0',c0==Q(4076476460239181,2251799813685248) and Q(9,5)<c0<Q(37,20))
 O=Q(params['O']);k=Q(params['K_lower']);u=Q(params['cU_lower']);sig=Q(params['sigma'])
 check('exact_uniform_parameters',O==Q(347,10) and k==Q(39068,100) and u==Q(15871,10000) and sig==Q(1,1024))
 sigma=aq(sig);pi=arb.pi();M=pi.sqrt()*((1-sigma)/2).gamma()/2;W=8*arb(5).sqrt()*arb(6)**aq(Q(-3,5))/5
 k1=M+aq(Q(8,5));cr=3*M/2+aq(Q(32,15));c8=1+3*pi*W/4;dtop=1+pi*W/2
 K=2*dtop+6*c8+24*(cr+2*k1)+32*k1
 q0=1/(2*pi.sqrt());ps=arb(2)**sigma*(1+sigma).sqrt()/(2*pi.sqrt())
 P0=ps*(1+W*M*sigma)+W*M*sigma/(2*pi.sqrt())
 v=aq(Q(4,5))*q0+q0*(1+4*W*M*sigma)+aq(Q(19,5))*P0
 check('K_lower_directed',K>aq(k));check('v_lower_directed',v>aq(u))
 for label,value in [('K',K),('v',v)]:
  source=arb(peer[label]);check(label+'_peer_contains_own',source.lower()<value.lower() and value.upper()<source.upper())
 mu=Poly([0,1]);records=[];totalleaves=0
 fam={row['name']:Q(row['ceiling_squared_exact']) for row in accepted['scalar_families']}
 d007=Q(params['d007']);own007=next(row for row in accepted['weak_candidates'] if row['number']==7)
 check('007_floor_accepted',d007<Q(own007['own_root_floor_exact']))
 check('seven_matching_rows',len(params['rows'])==len(peer['rows'])==len(opus['rows'])==7)
 for row,pr,op in zip(params['rows'],peer['rows'],opus['rows']):
  label=row['label'];m2,m1,beta,b=[Q(row[k]) for k in ['m2','m1','beta','bound']]
  check(label+':labels',label==pr['label']==op['label'])
  check(label+':parameters',m2>0 and m1>m2 and beta>m2 and b>0 and all(Q(pr[key])==val for key,val in [('m2',m2),('m1',m1),('beta',beta),('strict_L2_upper',b)]) and Q(op['bound'])==b)
  if label=='bL_c0':check('bL_same_c0',beta==1+c0)
  if label=='bL_all_A':check('bL_all_A_cap',beta==Q(57,20))
  p,a,c=m2-mu,m1-mu,beta-mu
  poly=27*k*u*u*b*b*(1440*p+(6*O+5*a)**2)-4*mu**3*c*p*a**2
  check(label+':degree7',poly.degree()==7)
  check(label+':power_coefficients',list(poly)==[Q(q) for q in pr['polynomial_power_mu']])
  leaves=pr['leaves'];previous=Q(0);minimum=None;recordleaves=[]
  for i,leaf in enumerate(leaves):
   A,Bb=map(Q,leaf['t_interval']);check(f'{label}:leaf{i}:partition',A==previous and A<Bb<=1)
   local=poly(Poly([m2*A,m2*(Bb-A)]))
   bern=[sum((local[j]*Q(comb(kx,j),comb(7,j)) for j in range(kx+1)),Q(0)) for kx in range(8)]
   check(f'{label}:leaf{i}:exact_coefficients',bern==[Q(q) for q in leaf['Bernstein_coefficients']])
   for j,q in enumerate(bern):check(f'{label}:leaf{i}:positive{j}',q>0)
   previous=Bb;minimum=min(bern) if minimum is None else min(minimum,min(bern));recordleaves.append({'interval':[str(A),str(Bb)],'minimum_exact':str(min(bern))})
  check(label+':full_coverage',previous==1 and len(leaves)==pr['leaf_count'])
  check(label+':saved_minimum',minimum==Q(pr['minimum_Bernstein_coefficient']))
  check(label+':gain_upper',b*b<=exact_decimal(row['gain'])**2*fam[row['family']])
  check(label+':007_factor',d007>=exact_decimal(row['factor'])*b)
  if 'old_bound' in row:check(label+':implies_old_bound',b<exact_decimal(row['old_bound']))
  if 'old_H18_factor' in row:check(label+':old_H18_factor',Q(params['old_H18_minimum'])>=exact_decimal(row['old_H18_factor'])*b)
  check(label+':below_common_floor',b<Q(1,1000))
  totalleaves+=len(leaves);records.append({'label':label,'strict_L2_upper_exact':str(b),'polynomial_power_mu':[str(q) for q in poly],'leaves':recordleaves,'gain_upper_exact':str(exact_decimal(row['gain'])),'007_factor_lower_exact':str(exact_decimal(row['factor']))})
 check('all_unweighted_bL_factor243',243*Q(params['rows'][-1]['bound'])<Q(1,1000))
 for rel,h in inputs.items():assert sha(R/rel)==h,rel
 result={'utc':now(),'inputs':inputs,'checks':checks,'check_count':len(checks),'precision_bits':ctx.prec,'K_ball':K.str(200),'v_ball':v.str(200),'rows':records,'total_bernstein_leaves':totalleaves,'fixed_c_snapshot_numbers':numbers,'all_unweighted_bL_factor_strict_lower':243,'foreign_code_executed':False,'new_candidate_integrals':False,'Opus_supremum_displays_reproduced':False,'scope':'Seven necessary algebraic budgets; original-floor unweighted bL and all-weight composition with accepted fixed-c24 L2 witnesses. Explicit uniform constants, fixed floors and norm embedding required.','elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED seven exact budget ceilings and stated fixed-c composition; no inverse, new background margin or existence result'}
 with (B/'verification/result_v02.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'utc':result['utc'],'checks':len(checks),'inputs':len(inputs),'leaves':totalleaves,'result_sha256':sha(B/'verification/result_v02.json'),'elapsed_seconds':result['elapsed_seconds']}))
if __name__=='__main__':main()
