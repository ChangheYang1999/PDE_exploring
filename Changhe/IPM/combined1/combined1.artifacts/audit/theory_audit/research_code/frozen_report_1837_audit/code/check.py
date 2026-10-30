"""Finite composition of a frozen report and accepted, hash-bound audit records."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,gzip,hashlib,re,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
 p=B/p;raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def text(p):
 p=B/p;raw=p.read_bytes();return (gzip.decompress(raw) if p.suffix=='.gz' else raw).decode()
def need(k,v):
 assert v,k
 checks.append(k)
flat=lambda s:' '.join(s.split())
m=read('data/manifest.json')
for p,h in m['inputs'].items():need('binding '+p,sha(B/p)==h)
first=read('data/PROOF_FIRST.json');need('proof precedes checker',first['checker_exists'] is False and first['proof_sha256']==sha(B/'PROOF.md'))
for file in ['initial_sources.json','supplemental_sources.json']:
 for row in read('data/'+file)['rows']:
  need('decoded original '+row['local'],hashlib.sha256(text(row['local']).encode()).hexdigest()==row['source_sha256'])
report=text('source/FINAL_REPORT.md');matrix=text('source/matrix_v175.md');rl=report.splitlines();ml=matrix.splitlines();rf=flat(report)
need('official target',sha(B/'source/FINAL_REPORT.md')=='7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743' and len(rl)==2867)
need('official matrix',sha(B/'source/matrix_v175.md')=='d16aedf93023679b47cc3dd144db361b36ad926e1513829e88b71e77f930da72')
sections=[(39,102,'## Answers in brief'),(103,336,'## Short answers'),(1042,1161,'## Comparison table'),(1187,1453,'## 3. Theory track'),(1659,1707,'## 6. Unresolved inequalities')]
for a,b,head in sections:need('audited section '+str(a),rl[a-1].startswith(head) and rl[b].startswith('## '))
need('coordinator nominated same target','7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743' in text('source/COORD_FINAL_REQUEST.md.gz'))
def table(lines,width):
 out={};physical=[]
 for lineno,line in enumerate(lines,1):
  if not re.match(r'^\|\s*\d',line):continue
  cells=[s.strip() for s in re.split(r'(?<!\\)\|',line.strip())[1:-1]]
  if len(cells)!=width:continue
  ids=[]
  for token in re.split(r'\s*,\s*',cells[0]):
   pair=token.split('-');ids+=list(range(int(pair[0]),int(pair[-1])+1))
  physical.append({'line':lineno,'numbers':ids,'cells':cells})
  for n in ids:need('unique table row '+str(width)+'/'+str(n),n not in out);out[n]={'line':lineno,'cells':cells}
 return out,physical
rrows,physical=table(rl,8);mrows,mp=table(ml,11)
need('complete108matrix rows',set(mrows)==set(range(1,109)) and len(mp)==108)
need('complete108report rows',set(rrows)==set(mrows))
need('106physical report rows',len(physical)==106 and sum(len(z['numbers'])>1 for z in physical)==1)
status=lambda c:re.search(r'\b(RULED OUT|OPEN|PROVED|CONDITIONAL)\b',c).group(0)
comparisons=[]
for n in range(1,109):
 r=rrows[n]['cells'];v=mrows[n]['cells'];need('status row'+str(n),status(r[-1])==status(v[-1]) and status(r[-1]) in ['OPEN','RULED OUT'])
 a=re.search(r'C1-N1-\d{3}',r[2]);b=re.search(r'C1-N1-\d{3}',v[2])
 if a or b:need('candidate row'+str(n),bool(a and b) and a.group()==b.group())
 elif r[2].startswith('C1-BASE-S131') or v[2].startswith('C1-BASE-S131'):need('state131 row'+str(n),r[2].startswith('C1-BASE-S131') and v[2].startswith('C1-BASE-S131'))
 else:
  for token in ['d2','Mpen2','b6']:
   if token in v[2]:need('reference '+str(n)+'/'+token,token in r[2])
 comparisons.append(dict(row=n,report_line=rrows[n]['line'],matrix_line=mrows[n]['line'],status=status(r[-1]),report_candidate=r[2],matrix_candidate=v[2]))
openrows=[n for n in range(1,109) if status(rrows[n]['cells'][-1])=='OPEN']
need('exact open set',openrows==[4,19,27,33,34,50,69,70,103,104,107,108])
target='\n'.join('\n'.join(rl[a-1:b]) for a,b,_ in sections);t4=text('source/T4_ledger.md.gz');n4=text('source/N4_ledger.md.gz');ids=sorted(set(re.findall(r'\b(?:T4|N4)-\d{3}\b',target)))
for ident in ids:need('cited audit exists '+ident,ident in (t4 if ident.startswith('T4') else n4))
coverage=read('../h18_coverage_audit/verification/result.json');need('accepted459',coverage['checks_passed']==806)
need('24distinctweakcandidates',{z['number'] for z in coverage['weak_candidates']}==set(range(2,27))-{11})
for row in coverage['weak_candidates']:
 I,D,H=map(Q,[row['I_lower_exact'],row['D_upper_exact'],row['H_upper_exact']]);need('weak positive gap'+str(row['number']),I-D/1000-H/1000000==Q(row['positive_gap_exact'])>0)
for row in read('../family_ceiling_brackets/data/parameters.json')['rows']:
 mu,C,u,w=map(Q,[row['mu'],row['C'],row['cU'],row['sqrtW2']]);need('scalar bound '+row['name'],4*mu**3/(27*C*u*u*w*w)<Q('3.7930e-6')**2<Q('3.8e-6')**2)
gsq=Q(625,2992882662);need('graded displays',gsq<Q('4.57e-4')**2<Q('4.572e-4')**2 and gsq<Q(25,54684)**2)
need('unweighted margin allweight ceiling',Q(1,1000)/Q('4.1069e-6')>243)
ratios=[]
for name,floor,cap,display in [('007scalar','.004769166867','3.7930e-6','1257'),('007graded','.004769166867','25/54684','10.43'),('016sharpw','.001470360924','2.8496e-6','515.9'),('017sharpw','.00167183069831928','2.8496e-6','586.6'),('016graded','.001470360924','25/54684','3.21'),('017graded','.00167183069831928','25/54684','3.65'),('026graded','.001355907204057457','25/54684','2.965'),('007forcing','756.5312630768','2.1035e-4','3596535.57'),('TBfamily','1.0578e-4','6.3578288e-7','166')]:
 ratio=Q(floor)/Q(cap);need('directed factor '+name,ratio>Q(display));ratios.append(dict(name=name,exact_ratio=str(ratio),strict_display=display))
need('loosecap alone insufficientfor1257',Q('.004769166867')/Q('3.8e-6')<1257)
need('tight cap supplied in report','3.7930e-6' in target or '3.7930e-6' in report)
need('row25 exact thresholdfactor',Q('4321.48')/Q('1.0578e-4')>Q('4.08e7'))
need('table exact threshold legend','exact' in flat('\n'.join(rl[1042:1053])).lower() and 'threshold' in flat('\n'.join(rl[1042:1053])).lower())
a=read('../sharpw_maximum_review_acceptance/verification/result.json');need('accepted485',a['check_count']==57)
s=Q(1,5184);mu=Q(97,250)-397*s;A=Q(8,5)*72;r=mu/(2*A);eta=mu*mu/(4*A)
need('maximum radius',r==Q(201799,149299200)==Q(a['radius_star_exact']))
need('maximum residual',eta==Q(40722836401,193491763200000)==Q(a['eta_star_exact']))
need('complete square coefficients',2*A*r==mu and A*r*r==eta)
need('high positive rate',mu-A*r==mu/2>0)
need('low contraction usingpi3',r*r/(48*s*(1+s))<1)
need('oldradiuslarger sufficient budget',Q('0.001351')*(mu-A*Q('.001351'))==Q(a['old_radius_tolerance_exact'])>Q('2.1046e-4')>Q('2.1035e-4'))
need('007 even maximum fails',Q('756.5312630768')/eta>3594606)
need('same estimate qualification in history','maximum of this one sufficient estimate at s = 1/5184 and w = (2^15, 2^20)' in rf)
p=read('../candidate016_prefix63_replay_audit/verification/result.json');old=read('../candidate016_multimode_replay_audit/verification/result.json');mid=read('../candidate016_complete_bounds_reciprocal/verification/result.json');q=read('../candidate017_partial_replay_audit/verification/result.json')
need('accepted502and486and488and495',[z['check_count'] for z in [p,old,mid,q]]==[7564,13380,121,10450])
need('016 full modecoverage',p['complete_field_mode_count']==160 and p['individually_integrated_modes']==32 and p['omitted_modes_retained']==128)
for key,value in [('H_strict_lower_exact','308366750368225240013184170643/500000000000000000000000000000'),('H_strict_upper_exact','308948684181969723952067879861/500000000000000000000000000000'),('E2_strict_lower_exact','628580088526341/1000000000000'),('E2_strict_upper_exact','39304086799647/62500000000')]:need('016 exact '+key,Q(p[key])==Q(value))
need('016 H displays',Q(p['H_strict_lower_exact'])>Q('.6167335007') and Q(p['H_strict_upper_exact'])<Q('.617897369'))
need('016 E2 displays',Q(p['E2_strict_upper_exact'])<Q('628.865389'))
need('016 opposite exact gaps',Q(p['strict_H_gap_lower'])>Q('.017627007636152781') and Q(p['strict_E2_gap_lower'])==Q('21.759869526341'))
need('original486 lower precision',Q(old['E2_strict_lower_exact'])==Q('628.580088525') and Q(old['strict_E2_gap_lower'])==Q('21.759869525'))
need('488 explicit precision acceptance',mid['E2_strict_lower_exact']==p['E2_strict_lower_exact'] and mid['strict_E2_gap_lower']==p['strict_E2_gap_lower'])
need('486 squaredpremise supports488 display',Q(p['E2_strict_lower_exact'])**2<Q(old['E2_lower_square_exact']))
need('017 lower',Q(q['H_strict_lower_exact'])==Q('307209799380023711068567013529/500000000000000000000000000000')>Q('.614419598760'))
need('017 remains partial',q['complete_H_upper']=='OPEN' and q['complete_E2_and_017_less_than007']=='OPEN')
w=read('../prefix63_opus_review_acceptance/verification/result.json');need('accepted504',w['check_count']==473 and 'Actual division between upper and lower slack is OPEN' in w['refuted_inference'])
t1=read('../theory_final_frozen_audit/verification/result.json');t2=read('../t2_final_frozen_audit/verification/result.json');need('accepted506and507',t1['check_count']==828 and t2['check_count']==73)
note=text('source/T1_note67.md');need('T1 frozenhash',t1['target_sha256'] in note)
for literal in ['These corrected ratios do not alter any earlier norm bound.','since v101; v170 at the final','84699685','66246337']:need('T1 dated erratum '+literal,literal in note)
need('T1506 v170 source binding','closure_matrix_v170.md' in text('../theory_final_frozen_audit/data/manifest.json'))
f=read('data/findings.json')['findings'];need('six exact findings',len(f)==6)
for row in f:
 for line in row['lines']:need('finding line '+row['id']+'/'+str(line),1<=line<=len(rl))
 for ident in row['evidence']:need('finding evidence '+row['id']+'/'+ident,ident in t4)
need('F1 exact current phrases','largest admissible residual' in rl[41] and 'largest admissible residual' in rl[105])
need('F2 pending text at1290','AUDITED once c1-t4 cites the review' in rl[1289])
need('F2 accepted337','T4-324 is AUDITED.' in t4)
need('F3 current CLAIMED at1688','falsification check (CLAIMED)' in rl[1687])
need('F4 current gain at1684','3596535.57' in rl[1683])
need('F5 absent fromsection6','slack' not in '\n'.join(rl[1658:1707]))
for line in [62,141,1129]:need('F6 precision citation '+str(line),'T4-486' in rl[line-1])
for literal in ['not under the weighted margin (B-L2-w)','affine class rho + L^2 at every real c','Lower distance bounds for different candidates do not order their actual distances','no existence theorem closes','Other high spaces are not excluded','each application must check its realization','no concrete (H) is proved','not a stationary solution']:
 need('retained scope '+literal,flat(literal) in rf)
result=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,check_count=len(checks),checks=checks,proof_sha256=sha(B/'PROOF.md'),checker_sha256=sha(Path(__file__)),target_sha256=sha(B/'source/FINAL_REPORT.md'),matrix_sha256=sha(B/'source/matrix_v175.md'),physical_report_rows=len(physical),logical_report_rows=len(rrows),open_rows=openrows,row_comparisons=comparisons,cited_ids=ids,factors=ratios,eta_star_exact=str(eta),radius_star_exact=str(r),findings=f,T1_errata_accepted=['EF1','EF2'],confirmed='Conditional criteria, fixed-norm maximum, all108 classifications, accepted016 orderings,017 partial scope and listed inverse/endpoint limitations.',open='Existence closure, unregistered routes, improved stationary-specific endpoint estimates,017 full upper/E2,actual correction-distance orderings and016 upper/lower slack allocation.',foreign_code_executed=False,new_candidate_integrals=False)
with (B/'verification/result.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
print('PASS',len(checks),'checks',len(physical),'physical rows',len(rrows),'logical rows',len(ids),'citedIDs',result['elapsed_seconds'],'seconds')
