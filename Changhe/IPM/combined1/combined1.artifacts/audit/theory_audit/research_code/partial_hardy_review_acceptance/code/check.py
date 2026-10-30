"""Independent partial-Hardy review acceptance. Peer programs are parsed only."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import factorial
import ast,hashlib,json,sys,time
from flint import fmpq,fmpq_poly as Poly,arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');ctx.prec=p['precision_bits'];t2=read('source/T2_result.json')
need('T1 finished log','checks passed 4783 ; elapsed 7.1 s' in (B/'source/T1_log.txt').read_text() and (B/'source/T1_log.txt').read_text().endswith('RESULT PASS\n'))
need('T2 finished log','35 checks, 0 FAIL, 26.99 s' in (B/'source/T2_log.txt').read_text() and t2['fails']==[])
need('proof before checker',read('data/PROOF_FIRST.json')['checker_exists'] is False)
tree=ast.parse((B/'source/T1_check.py').read_text());ast.parse((B/'source/T2_check.py').read_text())
hm=[ast.literal_eval(n.value) for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HASH' for t in n.targets)]
need('one T1 source map',len(hm)==1)
for name,h in hm[0].items():need('T1 accepted source '+name,sha(B/read('data/peer_data_mapping.json')[name])==h)
for section in ['A','G']:
 for name,h in t2[section]['inputs'].items():need('T2 accepted source '+name,sha(B/('..'+name.split('/research',1)[1]))==h)
for row in read('../partial_mode_hardy_certificate/data/manifest.json'):need('474 manifest '+row['local'],sha(B/'../partial_mode_hardy_certificate'/row['local'])==row['sha256'])
for topic,count in [('partial_mode_hardy_certificate',720),('candidate016_prefix_hardy_audit',2297),('reciprocal_hardy_review_acceptance',209),('candidate016_prefix31_hardy_audit',4463)]:
 d=read('../'+topic+'/verification/result.json');need('accepted count '+topic,d['check_count']==len(d['checks'])==count)
# Derive every manufactured radial identity by exact polynomial moments.
x=Poly([0,1]);w=1-x;ff=lambda q:fmpq(str(q))
def D(b,P):return (1-2*ff(b)*x)*P+2*x*w*P.derivative()
def integral(P,q):
 q=Q(q);need('integrable moment '+str(q),q>-1);out=Q(0)
 for j,c in enumerate(P.coeffs()):
  v=Q(factorial(j))
  for k in range(1,j+2):v/=q+k
  out+=Q(str(c))*v
 return out
fixtures={}
for n,b,P in [(1,Q(3,2),Poly([1])),(3,Q(2),x)]:
 D1=D(b,P);D2=D(b,D1);L=n*n*P-D2
 S=integral(L*L,2*b-2)/2;d=integral(D1*D1+n*n*P*P,2*b-2)/2
 a=integral(D1*D1+D2*D2/(n*n),2*b-2)/2;bb=integral(L*D2/(n*n),2*b-2)/2
 vals={'S':S,'d':d,'a':a,'b':bb}
 for k,v in vals.items():need('manufactured '+str(n)+' '+k,v==Q(t2['E'][str(n)][k]))
 need('exact known mode energy '+str(n),S/(n*n)-a==d and bb==-a and a>0)
 fixtures[n]=vals
need('total known S',sum(v['S'] for v in fixtures.values())==Q(361,140))
need('total known H2',sum(v['d'] for v in fixtures.values())==Q(153,280))
need('total known M2',sum(v['S']/(n*n) for n,v in fixtures.items())==Q(1201,1260))
# Positive beta arguments with integer second argument, and half-half beta/pi.
def beta_int(a,b):
 a=Q(a);b=int(b);assert a>0 and b>0
 out=Q(factorial(b-1))
 for k in range(b):out/=a+k
 return out
def beta_half_pi(a,b):
 a=Q(a);b=Q(b);m=a-Q(1,2);n=b-Q(1,2);assert m.denominator==n.denominator==1 and m>=0 and n>=0
 m=int(m);n=int(n);return Q(factorial(2*m)*factorial(2*n),4**(m+n)*factorial(m)*factorial(n)*factorial(m+n))
need('infinite source radial integral',beta_int(2,4)/2==Q(1,40))
for j,terms in enumerate(p['polynomials']):
 val=Q(0)
 for ax,by,c in terms:
  if ax%2 or by%2==0:continue
  angular=2*beta_int(Q(ax+1,2),(by+1)//2)
  s=Q(ax+by+2,2);radial=beta_half_pi(s,7-s)/2
  val-=Q(c)*angular*radial
 need('whole-plane test pairing '+str(j),val==Q(p['pairings_over_pi'][j]))
D2=D(Q(3,2),D(Q(3,2),Poly([1])))
need('mode1 Euler square',D2==Poly([1,-12,15]))
cross=2*sum((Q(str(c))*beta_int(Q(3,2)+j,3) for j,c in enumerate(D2.coeffs())),Q(0))
need('infinite-source exact cross',cross==Q(-256,1155))
pi=arb.pi();S=pi/20;M=pi**3/240;last=None;infinite=[]
for N in p['odd_cuts']:
 total2=sum((Q(1,n*n) for n in range(1,N,2)),Q(0));total4=sum((Q(1,n**4) for n in range(1,N,2)),Q(0))
 BN=S/(N*N)+2/(5*pi)*arb(ff(total4-total2/(N*N)))
 need('infinite strict loss '+str(N),BN-M>0 and BN-M<S/(N*N))
 if last is not None:need('infinite strict prefix decrease '+str(N),BN<last)
 need('T2 approximate B '+str(N),abs(BN-arb(t2['D']['B_N'][str(N)]['B_N']))<arb('6e-16'))
 infinite.append({'N':N,'B_N_arb':str(BN),'loss_arb':str(BN-M)});last=BN
# Complete coefficient identities and all finite fixtures, with exact outward widths.
oldp=read('../partial_mode_hardy_certificate/data/parameters.json');old=read('../partial_mode_hardy_certificate/verification/result.json')
for row,saved in zip(oldp['fixtures'],old['fixtures']):
 es={int(n):Q(v) for n,v in row['energies'].items()};SS=sum(es.values(),Q(0));MM=sum((v/n**2 for n,v in es.items()),Q(0));last=None
 need(row['name']+' S M',SS==Q(saved['S'])==Q(t2['C']['fixtures'][row['name']]['S']) and MM==Q(saved['M2'])==Q(t2['C']['fixtures'][row['name']]['M2']))
 for N,obs in zip(p['odd_cuts'],saved['prefixes']):
  BN=sum((max(Q(1,n*n),Q(1,N*N))*v for n,v in es.items()),Q(0));loss=sum(((Q(1,N*N)-Q(1,n*n))*v for n,v in es.items() if n>N),Q(0))
  need(row['name']+' prefix '+str(N),BN==Q(obs['B_N']) and loss==Q(obs['loss'])==BN-MM and 0<=loss<=SS/(N*N)<=Q(obs['directed_upper_fixture'])+SS/(N*N))
  need(row['name']+' directed '+str(N),BN<=Q(obs['directed_upper_fixture']))
  if last is not None:need(row['name']+' decrease '+str(N),BN<=last)
  last=BN
  change=(Q(1,(N+2)**2)-Q(1,N*N))*sum((v for n,v in es.items() if n>N),Q(0))
  Bnext=sum((max(Q(1,n*n),Q(1,(N+2)**2))*v for n,v in es.items()),Q(0))
  need(row['name']+' adjacent identity '+str(N),Bnext-BN==change<=0)
es={int(n):Q(v) for n,v in oldp['fixtures'][2]['energies'].items()};bad=sum(es.values())/25+sum(((Q(1,n*n)-Q(1,25))*v for n,v in es.items() if n<5 and n!=3),Q(0))
need('omission of mode3 fails',bad==Q(t2['C']['omission_mixed_N5'])<Q(t2['C']['mixed_M2']))
# Prefix candidate arithmetic is independently recomposed from saved rational endpoints.
comp=read('../candidate016_dual_replay_audit/source/components.json')['norms'];U={k:Q(v['accepted_upper_exact']) for k,v in comp.items()};L={k:Q(v['accepted_lower_exact']) for k,v in comp.items()}
Shi=U['rF']**2;Slo=L['rF']**2;oldcross=read('../candidate016_cross_archive_audit/verification/result.json');J=Q(oldcross['improvement_sum_strict_lower_exact']);Hlo2=Q(oldcross['H_lower_square_exact'])
need('same accepted U and cross',U['rF']==Q(oldp['rF_upper'])==Q(t2['F']['U']) and J==Q(oldp['cross_improvement_lower'])==Q(t2['F']['cross_lower']))
for row in old['candidate016_tail_loss_bounds']:
 N=row['N'];loss=Shi/(N*N);display=Q(t2['F']['loss_displays'][str(N)])
 need('loss upper '+str(N),loss==Q(row['loss_strict_upper_exact'])<display==Q(row['display_strict_upper_exact']))
need('prefix33 gain exceeds loss',Shi/1089-J<Q('-0.19'))
computed={}
for name,path in [('T4','../candidate016_prefix_hardy_audit/verification/result.json'),('N4','../candidate016_prefix_hardy_audit/source/N4_prefix_v01.json')]:
 d=read(path);modes=d['modes'];need(name+' complete prefix',[v['n'] for v in modes]==[1,3,5,7])
 ql=sum((Q(v['q_lower_exact']) for v in modes),Q(0));qu=sum((Q(v['q_upper_exact']) for v in modes),Q(0));P=Shi/81+sum(((Q(1,v['n']**2)-Q(1,81))*Q(v['q_upper_exact']) for v in modes),Q(0))
 split=sum((Q(v['q_upper_exact'])/v['n']**2 for v in modes),Q(0))+(Shi-ql)/81
 need(name+' complete upper and interval difference',P==Q(d['M2_upper_exact']) and split-P==(qu-ql)/81>0)
 need(name+' tail',Shi-ql==Q(d['tail_rF_square_upper_exact'])>0)
 improved=P-J;need(name+' exact improvement',improved==Q(d['improved_H_square_upper_exact'])>Hlo2==Q(d['H_lower_square_exact']))
 need(name+' coarse upper',P<Q('1.063013')**2 and improved<Q('.944107')**2)
 Ehi=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*improved
 need(name+' exact energy upper',Ehi==Q(d['E2_upper_square_exact' if name=='T4' else 'conditional_E2_upper_square_exact'])<Q('722.968760')**2)
 need(name+' energy fraction below1/20',0<ql<=qu<Slo/20)
 computed[name]={'P':P,'improved':improved,'Ehi':Ehi}
Elo=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*Hlo2
need('retained lower H',Hlo2>Q('.529469576110512066428681')**2)
need('strict E2 separation',Elo>Q('608.392385921614')**2>Q('606.820219')**2)
# Locate the inward decimal attribution, keeping the actual coarse inequalities.
N4=read('../candidate016_prefix_hardy_audit/source/N4_prefix_v01.json');repairs=p['directed_repairs'];rounding=[]
for row in p['display_attributions']:
 true=Q(N4[row['source_key']]);shown=Q(row['display']);mapped=shown if row['kind']=='direct' else shown*shown
 need('inward displayed '+row['name'],mapped<true)
 key={'M2':'M2_upper','plain_H':'plain_H_upper','improved_H':'improved_H_upper'}[row['name']];upper=Q(repairs[key]);safe=upper if row['kind']=='direct' else upper*upper
 need('repaired upper '+row['name'],safe>true)
 rounding.append({'name':row['name'],'display':row['display'],'exact_deficit':str(true-mapped),'safe_display':repairs[key]})
need('total S repaired interval',Q(repairs['S_lower'])<Slo<Shi<Q(repairs['S_upper']))
need('repeated rounded total not enclosure',Q('51.061045287604983')<Slo)
review=(B/'source/T1_review.md').read_text()
need('exact squaring attribution located','plain H(016) <= 1.063012676 < 1.063013, by exact squaring' in review)
need('conditional observations remain conditional','CONDITIONAL on c1-n3' in review and 'FLOAT quadrature' in (B/'source/T2_review.md').read_text())
# Same-mode and source-wide qualifications are analytic statements in PROOF.md.
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'peer_counts':[4783,35],'fixtures_over_pi':{str(n):{k:str(v) for k,v in row.items()} for n,row in fixtures.items()},'infinite_source_exact_cross':str(cross),'infinite_source_prefix_checks':infinite,'inward_decimal_attributions':rounding,'directed_repairs':repairs,'accepted_prefix7_H_upper':'0.944107','accepted_prefix7_E2_upper':'722.968760','separate_prefix31_H_upper':'0.619652','separate_prefix31_E2_upper':'629.296113','foreign_code_executed':False,'candidate_integrals_repeated':False,'general474_both_reviews':'CONFIRMED with local integrability, complete odd prefix and distinct-frequency correction tests','verdict':'CONFIRMED both independent Opus474 analytic reviews and exact fixture/candidate composition. REFUTED inward intermediate decimal attribution as directed squaring in R1-050 V7; coarse endpoints remain valid. Equality of split and positive forms requires included zero interval widths, not exact total U. FLOAT quadrature retained. No inverse or existence.'}
with (B/'verification/result.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
print('PASS',len(checks),'checks',result['elapsed_seconds'],'seconds')
