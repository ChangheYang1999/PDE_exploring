"""Exact source, scalar-budget and constant checks for the T2 final summary."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,time
from flint import arb,ctx
ctx.prec=512;B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert bool(v),k
 checks.append(k)
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
for x in read('data/manifest.json'):need('binding '+x['local'],sha(B/x['local'])==x['sha256'])
p=read('data/parameters.json');need('proof before checker',not read('data/PROOF_FIRST.json')['checker_exists'])
for name,n in p['accepted_counts'].items():j=read('../'+name+'/verification/result.json');need('accepted '+name,j['check_count']==len(j['checks'])==n)
summary=(B/'source/T2_FINAL_SUMMARY.md').read_text();need('audited version 17:25','17:25Z (section 7: FLOAT labels' in summary)
for needle in ['The closest candidate, 007','exact factor 0.99998313','fixed-c L2 distance below 3.79e-6']:need('summary wording '+needle,needle in summary)
mu,C,cU,sw,s,b,eta=[Q(p[k]) for k in ['mu','C','cU','sqrtW2','s','b','eta']];r=sw*b;beta=mu-C*s-cU*r*64
need('exact s sqrt',s==Q(1,64**2) and 0<s<=Q(1,1024))
need('larger admitted scalar budget',Q('3.79e-6')<b<Q('3.7930e-6'))
need('positive high rate',beta>0)
need('self map with positive forcing',0<eta<beta*r)
cs_upper_square=1024*r*r/(3*(1+s));need('normalization trace bound',cs_upper_square<Q('.036')**2)
need('slope condition',Q(7,10)-Q('.036')>0)
need('positive low margin',Q(19,5)-Q('.036')>0)
need('strict low contraction',Q('.036')/(Q(19,5)-Q('.036'))<1)
family=read('../family_ceiling_brackets/data/parameters.json');squares={}
for row in family['rows']:
 a,c,u,w=[Q(row[k]) for k in ['mu','C','cU','sqrtW2']];z=4*a**3/(27*c*u*u*w*w);squares[row['name']]=str(z);need(row['name']+' outward common cap',0<z<Q('3.7930e-6')**2)
need('TB strict endpoints',Q('3.7929e-6')**2<Q(squares['TB-sharp'])<Q('3.7930e-6')**2)
gradedsq=Q(2500,651**2*28248);need('true graded upper valid',gradedsq<Q('4.5717e-4')**2)
need('old coarse graded equality approximate',Q(25,54684)>Q('4.5717e-4'))
sigma=arb(1)/1024;pi=arb.pi();M=pi.sqrt()*((1-sigma)/2).gamma()/2;W=8*arb(5).sqrt()*arb(6)**(-arb(3)/5)/5
k1=M+arb(8)/5;cr=3*M/2+arb(32)/15;c8=1+3*pi*W/4;dtop=1+pi*W/2;K=2*dtop+6*c8+24*(cr+2*k1)+32*k1
q0=1/(2*pi.sqrt());ps=arb(2)**sigma*(1+sigma).sqrt()/(2*pi.sqrt());P0=ps*(1+W*M*sigma)+W*M*sigma/(2*pi.sqrt());v=arb(4)/5*q0+q0*(1+4*W*M*sigma)+arb(19)/5*P0
factor=(ar(Q(39068,100))/K).sqrt()*ar(Q(15871,10000))/v;old=read('../constant_display_successors_audit/verification/result.json')
need('same exact factor source',arb(old['factor']).contains(factor))
need('strict factor rational enclosure',ar(p['factor_lower'])<factor<ar(p['factor_upper']))
need('exact decimal equality false',factor<ar(p['factor_display']))
need('nearest decimal rounding valid',ar(Q(p['factor_display'])-Q(5,10**9))<factor<ar(Q(p['factor_display'])+Q(5,10**9)))
ast.parse((B/'source/T2_BS_check.py').read_text());j=read('source/T2_BS_result.json');need('peer finite result',j['checks']==29 and j['fails']==[])
filemap={'artifacts/data/inputs/theory_final_d55_aa2d3063_excerpt.txt':'T2_draft55_excerpt.txt','artifacts/data/inputs/c1t4_verify_report_excerpt_1708.txt':'T2_ledger_excerpt.txt','artifacts/data/inputs/theory_v01_47ba2ee7_excerpt.txt':'T2_v01_excerpt.txt','notes/T2_T4L2_sharp.md':'T2_sharp.md'}
need('all peer source bindings covered',set(filemap)==set(j['input']))
for k,n in filemap.items():need('producer input '+k,sha(B/'source'/n)==j['input'][k])
def numbered(path):
 d={}
 for line in path.read_text().splitlines():a,x=line.split('\t',1);i=int(a);need('unique numbered '+path.name+' '+a,i not in d);d[i]=x
 return d
frozen=(B/'../theory_final_draft55_audit/source/THEORY_FINAL.md').read_text().splitlines();ex=numbered(B/'source/T2_draft55_excerpt.txt');need('47 draft lines',len(ex)==47)
for n,x in ex.items():need('complete draft55 source line '+str(n),frozen[n-1]==x)
led=numbered(B/'source/T2_ledger_excerpt.txt');own=numbered(B/'source/own_ledger_excerpt.txt');need('32 ledger lines',len(led)==32 and led==own)
orig=(B/'source/theory_v01.md').read_text().splitlines();tv=numbered(B/'source/T2_v01_excerpt.txt');need('6 original sector lines',len(tv)==6)
for n,x in tv.items():need('complete original theory line '+str(n),orig[n-1]==x)
need('conditional AJ2 already accepted','CONFIRMED under the explicitly unchanged high-row margin and norm-domination hypotheses' in led[2779])
need('no localized PDE promotion','does not establish those hypotheses for a new localized PDE framework' in led[2779])
need('separate WU3 norm families','T2-R3 balls (beta 2)' in ex[685] and 'T2-R1 TB-sharp matrix with E0 as one component' in ex[686] and '(beta 11/4)' in ex[687])
need('registered floors corrected in summary','registered floors 1/2 and 9/10' in summary and 'not the T4-119 floor ceilings 0.61151 and 0.99116' in summary)
need('draft short closure statement scope','K_H eta <= r' in ex[425] and 'beta > 0' not in ex[425] and '7/10' not in ex[425])
need('box omitted in draft row','epsilon_max 1.8938e-7' in ex[495] and '2^-17' not in ex[495])
hand=(B/'source/T2_handoff.md').read_text();boxes=[]
for i,x in enumerate(p['boxes'],1):
 ss,mm,bb=[Q(x[k]) for k in ['s','m','B']];a=Q(2560);mub=Q(1,10)-4800*ss;eps=((mub-a*mm-bb)**2-4*a*bb*mm)/(4*a);rs=(mub+a*mm-bb)/(2*a);d=Q(x['eps_display']);e=int(x['eps_display'].split('e')[1]);half=Q(10)**(e-4)/2
 need('box '+str(i)+' exact sqrt',ss==Q(1,512**2) and a==5*512)
 need('box '+str(i)+' positive feasibility',mub-a*mm-bb>0 and eps>0 and rs>mm)
 need('box '+str(i)+' five digit rounding',d-half<eps<d+half)
 need('box '+str(i)+' source display',x['eps_display'] in hand)
 boxes.append({'s':str(ss),'m':str(mm),'B':str(bb),'eps_max_exact':str(eps),'r_star_exact':str(rs),'display':x['eps_display'],'rounding_half_unit_exact':str(half)})
need('different defect maxima',Q(boxes[0]['eps_max_exact'])>Q(boxes[1]['eps_max_exact']))
rates={}
for name,mub,A,rr,display,quotient in [('sharp',Q(200587,968000),Q(8,5)*88,Q(147,200000),Q('9.6432'),Q(10000,1037)),('sharpw',Q(201799,648000),Q(8,5)*72,Q(1351,10**6),Q('6.4226'),Q(10000,1557))]:
 beta0=mub-A*rr;need(name+' exact rate equality',beta0==Q(j['K_H'][name]['beta']))
 need(name+' intermediate equality false',quotient>display)
 need(name+' actual inverse bound valid',0<1/beta0<display)
 need(name+' peer exact reciprocal',1/beta0==Q(j['K_H'][name]['K_H_exact']))
 rates[name]={'beta_exact':str(beta0),'inverse_bound_exact':str(1/beta0),'display_upper_exact':str(display),'coarser_quotient_exact':str(quotient)}
floor=Q(6091157959,250000000000);need('005 floor scope',Q('.02436463')<floor<Q('.024364634'))
need('ratio nearest 1.50',Q('1.495')<floor/Q('.01625064')<Q('1.505'))
for h in [1,2,3]:
 for dd in [Q(0),Q(1)]:need('index affine coefficient '+str(h)+' '+str(dd),(1-dd)-h*dd==1-(h+1)*dd)
need('correct new list accepted','correct nonautomatic L2 list is(2,0),(3,0),(4,0)' in led[3092])
for x in read('data/manifest.json'):need('unchanged '+x['local'],sha(B/x['local'])==x['sha256'])
rout={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'manifest_sha256':sha(B/'data/manifest.json'),'scalar_example':{'r_exact':str(r),'L2_budget_exact':str(b),'s_exact':str(s),'beta_exact':str(beta),'self_map_budget_exact':str(beta*r),'forcing_exact':str(eta),'trace_square_upper_exact':str(cs_upper_square),'PDE_hypotheses_asserted':False},'scalar_family_squares':squares,'factor_ball':factor.str(100),'graded_square_exact':str(gradedsq),'boxes':boxes,'rates':rates,'draft_lines_checked':len(ex),'ledger_lines_checked':len(led),'theory_v01_lines_checked':len(tv),'closest_candidate_ordering':'OPEN; lower bounds alone cannot rank actual distances','foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED source-bound draft55 corrections and outward scalar cap3.7930e-6. REFUTED3.79e-6 as a uniform scalar-budget deduction and0.99998313 as the exact factor. Actual candidate distance ordering OPEN. No exclusion changes.'}
with (B/'verification/result.json').open('x') as f:json.dump(rout,f,indent=2);f.write('\n')
print(rout['utc'],len(checks),'checks',rout['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
print('SCALAR',rout['scalar_example']);print('FACTOR',factor.str(32));print('BOXES',boxes)
