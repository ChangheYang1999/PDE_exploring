"""Independent exact acceptance of corrected review text and report arithmetic."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,difflib,hashlib,json,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
need('proof first',not read('data/PROOF_FIRST.json')['checker_exists']);p=read('data/parameters.json')
for topic,count in p['accepted_counts'].items():
 r=read('../'+topic+'/verification/result.json');need('accepted '+topic,r['check_count']==len(r['checks'])==count)
old=(B/'../divergence_free_upper_review_acceptance/source/T2_review.md').read_text().splitlines();new=(B/'source/T2_review469.md').read_text().splitlines();changes=[{'tag':tag,'old_start':a+1,'old_stop':b,'new_start':c+1,'new_stop':d} for tag,a,b,c,d in difflib.SequenceMatcher(None,old,new).get_opcodes() if tag!='equal']
need('only three changed blocks',changes==read('data/changes.json') and len(changes)==3)
need('correct old frozen source',sha(B/'../divergence_free_upper_review_acceptance/source/T2_review.md')=='49583d59798726dc3b3e56e0949f7ed35af77bb50096ab3f97f8683e6b096441')
flat=' '.join(' '.join(new).split());need('revised sufficiency','r Delta psi is in L^2 when beta_min > 3/2' in flat and 'this condition is sufficient, not necessary' in flat)
need('failure count disclosure','Three test runs' in flat and 'stopped on a Python type error' in flat and 'third (15:55:41Z) passed 59 of 59' in flat)
for name in ['469','479']:ast.parse((B/f'source/T2_check{name}.py').read_text());j=read(f'source/T2_result{name}.json');need(name+' saved check count',j['checks']==(7 if name=='469' else 12) and j['fails']==[])
j=read('source/T2_result469.json');need('counterexample source pin',j['input']['c1-t4/research/divergence_free_upper_review_acceptance/PROOF.md']==sha(B/'../divergence_free_upper_review_acceptance/PROOF.md'))
def add(a,b):
 c=[Q(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def scale(a,c):return [x*c for x in a]
def mul(a,b):
 c=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for k,y in enumerate(b):c[i+k]+=x*y
 return c
def derivative(a):return [i*x for i,x in enumerate(a)][1:] or [Q(0)]
def D(a):return add(mul([Q(1),-2*Q(p['b'])],a),mul([Q(0),Q(2),Q(-2)],derivative(a)))
def integral(a):return sum((x/Q((i+1)*(i+2)) for i,x in enumerate(a)),Q(0))
P=list(map(Q,p['P']));DP=D(P);DDP=D(DP);n=p['n']
need('exact first differentiated polynomial',DP==list(map(Q,p['DP'])))
need('exact second differentiated polynomial',DDP==list(map(Q,p['DDP'])))
d=integral(add(mul(DP,DP),scale(mul(P,P),Q(n*n))))/2
a=integral(add(mul(DP,DP),scale(mul(DDP,DDP),Q(1,n*n))))/2
lap=add(DDP,scale(P,Q(-n*n)));M=integral(mul(lap,lap))/Q(2*n*n)
oldresult=read('../divergence_free_upper_review_acceptance/verification/result.json')['counterexample_energies_over_pi']
for name,value,key in [('d',d,'d_over_pi'),('a',a,'a_over_pi'),('M2',M,'M2_over_pi')]:need('counterexample energy '+name,value==Q(p[name])==Q(j[key])==Q(oldresult['M' if name=='M2' else name]))
need('exact sum identity',M==d+a>0)
need('ungrouped asymptotic coefficients',j['single_term_limits']==[['1','81','9'],['-1','81','9']])
# Each reported divergent coefficient follows from constant angular limits +/-1.
for s in [Q(1),Q(-1)]:need('nonzero logarithmic coefficients '+str(s),(n*n*s)**2==81 and n*n*s*s==9)
j=read('source/T2_result479.json');ex=B/'source/report_excerpt.txt';need('exact excerpt hash',sha(ex)==j['input']['data/inputs/final_report_live_edde27fc_excerpt.txt']=='68168051a89e41ac8502534f468b5fc3fc9b5657cfb5bce1b01788dd51eb7f83')
lines={}
for line in ex.read_text().splitlines():a0,b=line.split('\t',1);i=int(a0);need('unique excerpt line '+a0,i not in lines);lines[i]=b
need('exact excerpt line coverage',set(lines)==set(range(22,32))|set(range(118,129))|set(range(380,386))|set(range(468,473)))
for name,rng in [('answer1',range(22,32)),('short1',range(118,129)),('defect',range(380,386))]:
 text=' '.join(lines[k] for k in rng);need(name+' optimum and radius',p['eta'] in text and p['rstar'] in text and 'above 2.1046e-4' in text and 'T4-479' in text)
for name,rng in [('answer1',range(22,32)),('short1',range(118,129))]:
 text=' '.join(lines[k] for k in rng);need(name+' registered-radius scope','1351/1000000' in text and 'admits 2.1046e-4' in text and 'CHECK_T4_479_SHARPW_MAX_T2' in text)
mu,A=Q(p['mu']),Q(p['A']);eta=mu*mu/(4*A);rs=mu/(2*A);r=Q(p['selected_r']);budget=(mu-A*r)*r;X=Q(p['X007_lower']);sel=Q(p['selected_threshold'])
need('optimum value',eta==Q(p['eta'])==Q(j['eta_star'])>Q('.00021046'))
need('optimum radius',rs==Q(p['rstar'])==Q(j['r_star']) and Q('.00135155')<=rs<Q('.00135165'))
need('registered-radius budget',budget==Q(j['beta_r_at_1351e-6'])==Q(85237452769,405000000000000)>Q('.00021046'))
need('complete square loss',eta-budget==A*(r-rs)**2>0)
need('new factor floor',X/eta>3594606)
need('registered factor floor',X/sel>Q('3596535.57'))
need('bound explicitly in source','756.5312630768' in lines[472] and '3596535.57' in lines[472])
# Numeric output is rounded display only; exact inequalities above are decisive.
for key,value in [('factor_vs_eta_star',X/eta),('factor_vs_published',X/sel)]:need('rounded diagnostic '+key,abs(Q(j[key])-value)<Q(1,10**9))
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'manifest_sha256':sha(B/'data/manifest.json'),'counterexample_energies_over_pi':{'d':str(d),'a':str(a),'M2':str(M)},'review_changed_block_count':len(changes),'eta_star_exact':str(eta),'r_star_exact':str(rs),'selected_radius_budget_exact':str(budget),'factor_optimum_exact':str(X/eta),'factor_registered_exact':str(X/sel),'complete_historical_report_recovered':False,'historical_excerpt_source_provenance':'Producer reports historical complete-file hash edde27fc362222bab4b99e972ae3277d713b61174db0eb5f685707150cb3e0c3. Only the frozen numbered excerpt and its own exact hash are independently checked here.','foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED REVIEW_T4_469 revision2 and CHECK_T4_479_REPORT_REPAIR_T2 within their stated scopes; no candidate or existence verdict change.'}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(r['utc'],len(checks),'checks',r['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
