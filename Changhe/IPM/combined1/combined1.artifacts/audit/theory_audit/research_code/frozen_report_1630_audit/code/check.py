"""Read-only composition of a frozen report, exact thresholds and accepted records."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,gzip,hashlib,re,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(path):
 p=B/path;raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def text(path):
 p=B/path;raw=p.read_bytes();return (gzip.decompress(raw) if p.suffix=='.gz' else raw).decode()
def need(k,v):
 assert v,k
 checks.append(k)
m=read('data/manifest.json');need('proof precedes checker',read('data/PROOF_FIRST.json')['checker_exists'] is False)
for p,h in m['inputs'].items():need('binding '+p,sha(B/p)==h)
for row in read('data/initial_sources.json')['rows']:
 need('decoded original '+row['local'],hashlib.sha256(text(row['local']).encode()).hexdigest()==row['source_sha256'])
report=text('source/FINAL_REPORT.md');matrix=text('source/matrix_v149.md');rl=report.splitlines();ml=matrix.splitlines()
need('report official digest',sha(B/'source/FINAL_REPORT.md')=='244c9c223dad0925c570d594cb4afdfcbbcb8196d5981a6c8cf024827813f838')
need('matrix official digest',sha(B/'source/matrix_v149.md')=='6a6c2bc0fac0460b0add7b2e6d139bd49eb30d6973e96180a8d8543c668c0982')
for a,b,head in [(20,107,'## Answers in brief'),(108,328,'## Short answers'),(1031,1149,'## Comparison table')]:need('section '+str(a),rl[a-1].startswith(head) and rl[b].startswith('## '))
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
  for n in ids:
   need('unique table row '+str(width)+'/'+str(n),n not in out);out[n]={'line':lineno,'cells':cells}
 return out,physical
rrows,physical=table(rl,8);mrows,mp=table(ml,11)
need('complete108matrix rows',set(mrows)==set(range(1,109)) and len(mp)==108)
need('complete108report represented rows',set(rrows)==set(mrows))
need('106physical report rows with one combinedrange',len(physical)==106 and sum(len(z['numbers'])>1 for z in physical)==1)
status=lambda c:re.search(r'\b(RULED OUT|OPEN|PROVED|CONDITIONAL)\b',c).group(0)
comparisons=[]
for n in range(1,109):
 r=rrows[n]['cells'];v=mrows[n]['cells'];need('status row'+str(n),status(r[-1])==status(v[-1]) and status(r[-1]) in ['OPEN','RULED OUT'])
 a=re.search(r'C1-N1-\d{3}',r[2]);b=re.search(r'C1-N1-\d{3}',v[2])
 if a or b:
  need('snapshot candidate row'+str(n),bool(a and b) and a.group()==b.group())
 elif r[2].startswith('C1-BASE-S131') or v[2].startswith('C1-BASE-S131'):need('state131 row'+str(n),r[2].startswith('C1-BASE-S131') and v[2].startswith('C1-BASE-S131'))
 else:
  for token in ['d2','Mpen2','b6']:
   if token in v[2]:need('named reference '+str(n)+'/'+token,token in r[2])
 comparisons.append({'row':n,'report_line':rrows[n]['line'],'matrix_line':mrows[n]['line'],'status':status(r[-1]),'report_candidate':r[2],'matrix_candidate':v[2]})
need('unaccepted snapshots remainOPEN',all(status(rrows[n]['cells'][-1])=='OPEN' for n in [69,70,103,104,107,108]))
target='\n'.join(rl[19:328]+rl[1030:1149]);t4=text('source/T4_ledger.md.gz');n4=text('source/N4_ledger.md.gz');ids=sorted(set(re.findall(r'\b(?:T4|N4)-\d{3}\b',target)))
for ident in ids:need('cited audit exists '+ident,ident in (t4 if ident.startswith('T4') else n4))
old=read('../theory_v08_published_audit/verification/result.json');need('accepted471',old['check_count']==695)
coverage=read('../h18_coverage_audit/verification/result.json');need('accepted459 count',coverage['checks_passed']==806)
need('24distinctcoverage',{z['number'] for z in coverage['weak_candidates']}==set(range(2,27))-{11})
for row in coverage['weak_candidates']:
 I,D,H=map(Q,[row['I_lower_exact'],row['D_upper_exact'],row['H_upper_exact']]);need('weak gap'+str(row['number']),I-D/1000-H/1000000==Q(row['positive_gap_exact'])>0)
for row in read('../family_ceiling_brackets/data/parameters.json')['rows']:
 mu,C,u,w=map(Q,[row['mu'],row['C'],row['cU'],row['sqrtW2']]);need('scalar common bound '+row['name'],4*mu**3/(27*C*u*u*w*w)<Q('3.7930e-6')**2<Q('3.8e-6')**2)
gsq=Q(625,2992882662);need('both graded displays safe',gsq<Q('4.57e-4')**2<Q('4.572e-4')**2 and gsq<Q(25,54684)**2)
need('unweighted allweight ceilingfactor',Q(1,1000)/Q('4.1069e-6')>243)
ratios=[]
for name,floor,cap,display in [('007scalar','.004769166867','3.7930e-6','1257'),('007graded','.004769166867','25/54684','10.43'),('016sharpw','.001470360924','2.8496e-6','515.9'),('017sharpw','.00167183069831928','2.8496e-6','586.6'),('016graded','.001470360924','25/54684','3.21'),('017graded','.00167183069831928','25/54684','3.65'),('026graded','.001355907204057457','25/54684','2.965'),('007forcing','756.5312630768','2.1035e-4','3596535.57'),('TBfamily','1.0578e-4','6.3578288e-7','166')]:
 ratio=Q(floor)/Q(cap);need('directed factor '+name,ratio>Q(display));ratios.append({'name':name,'exact_ratio':str(ratio),'printed_lower':display})
need('row25 exact registered factor',Q('4321.48')/Q('1.0578e-4')>Q('4.08e7'))
need('rounded row25 threshold not exactdivision',Q('4321.48')/Q('1.06e-4')<Q('4.08e7'))
need('legend presently omits rounding qualifier','Ratio = residual lower bound /\nthreshold.' in report)
# The maximum claim is tested using the earlier accepted complete conditional theorem.
d=read('../defect_review_audit/verification/results.json');need('accepted065 proof',d['all_checks_pass'] and d['proof_sha256']==sha(B/'../defect_review_audit/PROOF.md'))
s=Q(1,5184);mu=Q(97,250)-397*s;A=Q(8,5)*72;r=mu/(2*A);beta=mu-A*r;eps=r*beta
need('exact defect witness radius',r==Q(201799,149299200)>0)
need('exact defect witness margin',beta==Q(201799,1296000)>0)
need('exact optimum and archived value',eps==Q(40722836401,193491763200000)==Q(d['boxes'][0]['epsilon_at_r']))
need('larger already certified sufficient tolerance',eps>Q('2.1046e-4')>Q('2.1035e-4'))
need('low contraction usingpi>3',r*r/(48*s*(1+s))<1)
need('fixed original radius also permitslarger tolerance',Q(1351,1000000)*(mu-A*Q(1351,1000000))>Q('2.1046e-4'))
need('maximality phrase brief','The largest admissible\n   residual is that of FW-T-T4L2-sharpw-v1.' in report)
need('maximality phrase short','The largest admissible residual in a scalar norm is FW-T-T4L2-sharpw-v1' in report)
need('frozen matrix registers witness','2.1046e-4 at g = 0' in matrix and 'FW-T-T4L2-defect-v1' in matrix)
need('T1 draft registers witness','2.1046e-4 (g = 0)' in text('source/T1_draft.md.gz'))
p=read('../candidate016_prefix_hardy_audit/verification/result.json');cross=read('../candidate016_cross_archive_audit/verification/result.json');need('accepted476and472',p['check_count']==2297 and cross['check_count']==3113)
need('frozen016H enclosure',Q(p['H_strict_lower'])>Q('.529469576110512066') and Q(p['improved_H_strict_upper'])==Q('.944107'))
need('frozen016E2 enclosure',Q(p['E2_strict_lower'])==Q('608.392385921614') and Q(p['E2_strict_upper'])==Q('722.969'))
need('strict gap same registeredE2',Q(p['E2_strict_lower'])-Q(cross['007_E2_strict_upper_exact'])==Q('1.572166921614'))
need('source double Opusacceptance',read('../reciprocal_hardy_review_acceptance/verification/result.json')['check_count']==209)
for literal in ['not under the weighted margin (B-L2-w)','affine class rho_001 + L^2 only','not shown to\n   minimize E_2','Lower distance bounds for different candidates do not order their actual distances','Whether an improved valid universal constant\n   reaches 2^-25 or 6.8626e-8 is therefore OPEN','planning judgment from these numbers, not a theorem']:
 need('explicit retained scope '+literal,' '.join(literal.split()) in ' '.join(target.split()))
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'target_sha256':sha(B/'source/FINAL_REPORT.md'),'matrix_sha256':sha(B/'source/matrix_v149.md'),'physical_report_rows':len(physical),'matrix_rows':len(mp),'row_comparisons':comparisons,'cited_ids':ids,'factors':ratios,'stronger_registered_residual_witness':{'g':'0','m':'0','B':'0','s':str(s),'weights':[32768,1048576],'r':str(r),'beta':str(beta),'epsilon_exact':str(eps),'safe_sufficient_epsilon':'2.1046e-4','same_old_radius_also_sufficient':True},'refuted':[{'lines':[22,23,110,111],'claim':'absolute maximality of the selected2.1035e-4 registered residual threshold','repair':'restrict to selected matrix tests or include the existing065 g=0 specialization'}],'clarifications':[{'lines':[1035,1036,1062],'claim':'rounded table thresholds do not reproduce every strict factor literally','repair':'state that exact registered thresholds are used before rounding table displays'}],'confirmed':'All108 matrix statuses and candidate associations, existing conditional theorem, scope boundaries, accepted frozen016pairwise bounds,24weak exclusions and directed budgets. No snapshot verdict changes.','open':'No existence closure; narrow N3 and later N4-409prefix remain separate numerical audits.','candidate_integrals_repeated':False,'foreign_code_executed':False}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',len(physical),'report rows',len(mp),'matrix rows',len(ids),'citedIDs',result['elapsed_seconds'],'seconds')
