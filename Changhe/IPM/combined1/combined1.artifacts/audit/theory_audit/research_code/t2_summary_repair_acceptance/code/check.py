"""Independent exact acceptance of T2's repaired summary. No peer execution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,difflib,hashlib,json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];ctx.prec=512;start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads((B/p).read_text())
def need(n,x):
 assert bool(x),n
 checks.append(n)
def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator
for x in load('data/manifest.json'):need('input '+x['local'],sha(B/x['local'])==x['sha256'])
need('proof first',not load('data/PROOF_FIRST.json')['checker_exists'])
old=load('../t2_final_summary_audit/verification/result.json');need('accepted491',old['check_count']==len(old['checks'])==278)
s=(B/'source/T2_FINAL_SUMMARY.md').read_text();o=(B/'../t2_final_summary_audit/source/T2_FINAL_SUMMARY.md').read_text();d=load('data/changes.json')
need('frozen before and after',sha(B/'source/T2_FINAL_SUMMARY.md')==d['new_sha256'] and sha(B/'../t2_final_summary_audit/source/T2_FINAL_SUMMARY.md')==d['old_sha256'])
need('complete17changedblocks',d['diff']==list(difflib.unified_diff(o.splitlines(),s.splitlines(),lineterm='')) and sum(x.startswith('@@') for x in d['diff'])==17)
for phrase in ['fixed-c L2 distance below 3.7930e-6','no candidate is called closest here','factor sqrt(k/K00) u/(A\' + B\'), about','< 4.5698e-4 < 4.5717e-4','mu about 5.04423 at q*','C_T = sqrt((4 log 2 - 1)/(8 pi)), an exact closed form','3/327680 (about 9.1553e-6','0.024364631836']:
 need('repair '+phrase,phrase in s)
ast.parse((B/'source/T2_check.py').read_text());peer=load('source/T2_result.json');need('producer11checks',peer['checks']==11 and peer['fails']==[])
p=load('data/parameters.json');mu,C,u,w,ss,b,eta=[Q(p[k]) for k in ['mu','C','u','w','s','b','eta']];r=w*b;beta=mu-C*ss-u*r*64;sup2=4*mu**3/(27*C*u*u*w*w)
need('counterexample exact values',r==Q(peer['item1']['r']) and beta==Q(peer['item1']['beta']) and sup2==Q(peer['item1']['sup_sq']))
need('counterexample feasible',ss==Q(1,4096) and beta>0 and beta*r>eta and Q('3.79e-6')<b<Q('3.7930e-6'))
need('trace and contraction',r*r/(12*ss*(1+ss))<Q('.036')**2 and Q('.036')/(Q(19,5)-Q('.036'))<1 and Q('.036')<Q('.7'))
need('scalar bracket',Q('3.7929e-6')**2<sup2<Q('3.7930e-6')**2)
need('scalar extremum',mu/(3*C)==Q(33,134000) and (mu-C*mu/(3*C))**2*mu/(3*C)/(u*w)**2==sup2)
gs=Q(2500,651**2*28248);need('graded peak',Q(1,2)-Q(4708,28248)==Q(1,3) and gs==Q(peer['item4_middle_sq']))
need('graded strict ordering',Q('4.5697e-4')**2<gs<Q('4.5698e-4')**2<Q('4.5717e-4')**2<Q(25,54684)**2)
factor=arb(old['factor_ball']);need('factor strict brackets',ar(p['factor_interval'][0])<factor<ar(p['factor_interval'][1]))
need('factor rounded',ar(Q('.99998313')-Q(5,10**9))<factor<ar('.99998313'))
need('producer factor encloses',arb(peer['item2_factor']).contains(factor))
need('no distance ordering claimed','not known' in s and 'T4-491: OPEN' in s)
c=Q(p['c']);g=1/c;moment=8/((3-g)*(2-g)*(1-g));ml,mh=map(Q,p['moment_interval'])
need('moment coefficient',ml<moment<mh and Q('5.0442')<moment<Q('5.04423'))
need('positive moment factors',g<1 and all(4-j-g>0 for j in [1,2,3]))
need('threshold rounding exact gap',Q('9.1553e-6')-Q(3,327680)==Q(17,640000000000))
pi=arb.pi();md=Q(1,10)-Q(4800,2**18);aa=Q(2560)
def eps(m,v):return ((md-aa*m-v)**2-4*aa*v*m)/(4*aa)
# Match immutable line-number keys, independently rebuild every expression.
values={29:[g,1-g],89:[Q(p['universal_lower_exact'])],111:[Q(3,327680)],122:[Q(5289,50000000)],141:[Q(76219,10**9),Q(4207,20000000)],150:[1+Q(32,25)+2**14,1+Q(32,25)+2**15],174:[eps(Q(1,2**17),Q(1,100)),eps(Q(1,2**16),Q(1,200))],197:[Q(25,54684)],201:[25/(868*pi.sqrt())],301:[(2*pi).sqrt(),(8*pi).sqrt()*ar(1-c/5)/ar(Q(11,5))],326:[Q(6091157959,250000000000)],353:[2-g],437:[moment],439:[(1-g)/(3-g)],448:[Q(25,54684*512)],483:[((4*arb(2).log()-1)/(8*pi)).sqrt()]}
seen={};out=[]
for name,row in peer['sweep'].items():
 line=int(name.split(':',1)[0].split()[1]);i=seen.get(line,0);seen[line]=i+1;val=values[line][i];disp=Q(row['display'])
 if isinstance(val,Q):kind='exact' if val==disp else 'rounded up' if val<disp else 'rounded down';exact=str(val)
 else:kind='rounded up' if val<ar(disp) else 'rounded down' if val>ar(disp) else 'OPEN';exact=val.str(100)
 need('sweep '+name,kind==row['kind'] and kind!='OPEN')
 out.append({'name':name,'value_exact_or_ball':exact,'display':row['display'],'classification':kind})
need('all21expressions',len(out)==sum(map(len,values.values()))==21 and all(seen[k]==len(v) for k,v in values.items()))
need('5exact16rounded',sum(r['classification']=='exact' for r in out)==5)
need('sameacceptedfactorinput',peer['input']=={'c1-t4/research/weight_uniform_gram_audit/verification/result.json':sha(B/'../weight_uniform_gram_audit/verification/result.json')})
need('BT source result bound',sha(B/'source/T2_result.json')[:8] in (B/'source/T2_handoff_BT.md').read_text())
for x in load('data/manifest.json'):need('unchanged '+x['local'],sha(B/x['local'])==x['sha256'])
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'source_summary_sha256':sha(B/'source/T2_FINAL_SUMMARY.md'),'changed_blocks':17,'moment_exact':str(moment),'moment_interval':p['moment_interval'],'scalar_supremum_squared':str(sup2),'graded_supremum_squared':str(gs),'sweep':out,'factor_ball':factor.str(100),'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED all four491repairs, moment interval and21decimal classifications. No candidate verdict changes.'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(result['utc'],len(checks),'checks',result['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
