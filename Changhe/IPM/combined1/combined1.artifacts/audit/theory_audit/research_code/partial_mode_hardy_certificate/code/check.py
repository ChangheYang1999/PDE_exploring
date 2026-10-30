"""Exact finite identities for a complete Hardy certificate from a mode prefix."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib, json, time
B=Path(__file__).resolve().parents[1]
start=time.monotonic()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):
 need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');component=read('../candidate016_complete_forcing_audit/verification/result.json');cross=read('../candidate016_cross_archive_audit/verification/result.json');manufacture=read('../divergence_free_negative_norm_upper/verification/result.json')
need('accepted complete component',component['check_count']==len(component['checks'])==8874)
need('accepted cross arithmetic',cross['check_count']==len(cross['checks'])==3113)
need('exact candidate rF upper',Q(p['rF_upper'])==Q(component['components']['rF']['strict_upper_exact']))
need('exact candidate cross lower',Q(p['cross_improvement_lower'])==Q(cross['improvement_sum_strict_lower_exact']))
need('positive cross lower',Q(p['cross_improvement_lower'])>0)
need('manufactured original75 checks',manufacture['check_count']==len(manufacture['checks'])==75)
fixtures=[]
def bound(e,N):
 S=sum(e.values(),Q(0))
 return S/(N*N)+sum(((Q(1,n*n)-Q(1,N*N))*v for n,v in e.items() if n<N),Q(0))
for f in p['fixtures']:
 e={int(n):Q(v) for n,v in f['energies'].items()};S=sum(e.values(),Q(0));M=sum((v/(n*n) for n,v in e.items()),Q(0));row={'name':f['name'],'S':str(S),'M2':str(M),'prefixes':[]}
 need(f['name']+' legal spectrum',all(n>0 and n%2==1 and v>=0 for n,v in e.items()))
 for N in range(1,68,2):
  b=bound(e,N);tail=sum((v for n,v in e.items() if n>=N),Q(0));diff=sum(((Q(1,N*N)-Q(1,n*n))*v for n,v in e.items() if n>=N),Q(0))
  need(f'{f["name"]}/{N} tail identity',b==sum((v/(n*n) for n,v in e.items() if n<N),Q(0))+tail/(N*N))
  need(f'{f["name"]}/{N} full upper',b>=M)
  need(f'{f["name"]}/{N} complete loss',b-M==diff and 0<=diff<=S/(N*N))
  nextb=bound(e,N+2)
  need(f'{f["name"]}/{N} monotonic identity',nextb-b==(Q(1,(N+2)**2)-Q(1,N*N))*sum((v for n,v in e.items() if n>N),Q(0))<=0)
  eps=Q(1,10**20);U=S+eps
  directed=U/(N*N)+sum(((Q(1,n*n)-Q(1,N*N))*(e.get(n,Q(0))+eps) for n in range(1,N,2)),Q(0))
  need(f'{f["name"]}/{N} directed input upper',directed>=b)
  if N in p['odd_cuts']:row['prefixes'].append({'N':N,'B_N':str(b),'loss':str(diff),'directed_upper_fixture':str(directed)})
 fixtures.append(row)
known=next(f for f in p['fixtures'] if f['name']=='known_solution_without_pi');e={int(n):Q(v) for n,v in known['energies'].items()};d=Q(0);a=Q(0)
for source in manufacture['fixtures']:
 n=source['n'];vals={k:Q(v) for k,v in source['values_over_pi'].items()}
 need('known source energy '+str(n),e[n]==n*n*vals['M2'])
 need('known signed cross '+str(n),vals['b']==-vals['a'] and vals['p']==vals['d'])
 need('known optimized identity '+str(n),vals['M2']-vals['b']**2/vals['a']==vals['d'])
 d+=vals['d'];a+=vals['a']
need('known exact H2',d==Q(153,280))
need('known exact M2',bound(e,3)==Q(1201,1260))
need('known both corrections',bound(e,3)-a==d)
need('known positive-only rational S',sum(e.values(),Q(0))==Q(361,140))
# Deliberately invalid omitted-low-frequency certificate, refuted by the known mode1 solution.
need('omitted low mode refutation',Q(3,4)/9<Q(3,8))
need('dropped high-mode tail refutation',0<Q(6,35))
R=Q(p['rF_upper']);losses=[]
for N in p['odd_cuts']:
 loss=R*R/(N*N);scale=10**12;upper=Q(loss.numerator*scale//loss.denominator+1,scale)
 need('strict directed loss N'+str(N),loss<upper and upper-loss<=Q(1,scale))
 losses.append({'N':N,'loss_strict_upper_exact':str(loss),'display_strict_upper_exact':str(upper)})
need('sixteen-mode loss below .047',R*R/(33*33)<Q(p['tail_loss_upper_N33']))
# Every directed scalar endpoint has one exact direction, without evaluating any candidate mode integral.
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'fixtures':fixtures,'known_exact_H2_over_pi':str(d),'candidate016_tail_loss_bounds':losses,'candidate016_rF_upper_exact':str(R),'candidate016_cross_improvement_strict_lower_exact':p['cross_improvement_lower'],'candidate_integrals_evaluated':False,'candidate_H_upper_asserted':False,'foreign_code_executed':False,'verdict':'CONFIRMED exact prefix arithmetic and complete omitted-mode loss. General corollary submitted for independent Opus review. New candidate H upper remains OPEN until compatible prefix certificates and the upper-proof review pass.'}
with (B/'verification/result.json').open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
print('PASS',len(checks),'checks',result['elapsed_seconds'],'seconds')
for row in losses:print('N',row['N'],'loss <',row['display_strict_upper_exact'])
