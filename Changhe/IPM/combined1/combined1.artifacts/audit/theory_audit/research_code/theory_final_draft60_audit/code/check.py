"""Independent incremental draft60 audit. Peer programs are frozen data."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,difflib,hashlib,json,re,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert bool(v),k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
need('proof first',not read('data/PROOF_FIRST.json')['checker_exists'])
doc=(B/'source/THEORY_FINAL.md').read_text();flat=' '.join(doc.split());old=(B/'../theory_final_draft58_audit/source/THEORY_FINAL.md').read_text();rv=' '.join((B/'source/REVIEWS_v52.md').read_text().split())
need('frozen60',sha(B/'source/THEORY_FINAL.md')=='8bac7dfc4a62c315297c0d54bc1f42812afbeb85dc2868af93c41e06c45ce137')
changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,old.splitlines(),doc.splitlines()).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=a+1,old_stop=b,new_start=c+1,new_stop=d))
need('18changes',len(changes)==18 and changes==read('data/changes.json'))
accepted={}
for topic,count in [('theory_final_draft58_audit',535),('t2_final_summary_audit',278),('numerical_literal_review_acceptance',1340),('candidate017_partial_replay_audit',10450),('numerical_literal_completion',310)]:
 r=read('../'+topic+'/verification/result.json');need('accepted '+topic,r['check_count']==len(r['checks'])==count);accepted[topic]=r
HL=Q(308366750368225240013184170643,5*10**29);dH=HL-Q('.6167335007')
need('exact difference',dH==Q(18225240013184170643,5*10**29));need('directed difference',Q('3.64e-11')<dH<Q('3.65e-11'))
for text in ['Unless expressly compared with eta*','below 3.7930e-6','below 4.5717e-4','beta(r) > 0','slope margin 7/10 - c_s r > 0','89 checks since REVIEWS_v52','Drafts 56 to 59 read','9359 (k = 12; nearest roundings','T4-493 (535 checks)','3.65e-11']:
 need('phrase '+text,text in flat)
need('review E13', 'is below HL by less than 3.65e-11' in rv)
need('review E14','Unless expressly compared with eta*' in rv)
need('eta distinct',Q(40722836401,193491763200000)>Q(4207,2*10**7))
r=Q(3791,1953125);b=r/512;need('budget example',b==Q('3.791e-6') and Q('3.79e-6')<b<Q('3.7930e-6'))
ex=accepted['t2_final_summary_audit']['scalar_example'];need('inherited exact example',Q(ex['r_exact'])==r and Q(ex['L2_budget_exact'])==b and Q(ex['s_exact'])==Q(1,4096));need('example self map',Q(ex['beta_exact'])>0 and Q(ex['self_map_budget_exact'])>Q(ex['forcing_exact']))
for n,z in accepted['t2_final_summary_audit']['scalar_family_squares'].items():need('common cap '+n,Q(z)<Q('3.7930e-6')**2)
gradedsq=Q(2500,651**2*28248);need('graded true upper',gradedsq<Q('4.5717e-4')**2);need('graded coarse differs',Q(25,54684)>Q('4.5717e-4'))
d=Q(4769166867,10**12);need('1257scalar',d/Q('3.7930e-6')>1257);need('10.43graded',d*d>Q('10.43')**2*gradedsq)
first={n:json.loads((B/'../numerical_literal_review_acceptance/source'/f'{n}_weaktests2.json').read_text(),parse_float=Q)['NORM-T-WEAK-v1_a0'] for n in ['007','013']}
rat={int(k):abs(Q(v['I_k'])/Q(first['013'][k]['I_k'])) for k,v in first['007'].items()}
need('nearest9359',Q('9358.8588')<rat[12]<Q('9358.8589') and abs(rat[12]-9359)<Q(1,2));need('nearest26.8',Q('26.8')<rat[128]<Q('26.85'))
for k,v in rat.items():
 if 192<=k<=1024:need('later '+str(k),v<Q('2.1'))
readme=(B/'source/README.md').read_text();pairs=re.findall(r'^\s+([a-f0-9]{64})\s+(\S+)\s*$',readme,re.M);prior={r['local']:r['sha256'] for r in read('../theory_final_draft58_audit/data/README_bindings.json')['bindings']};changed=[]
need('186README',len(pairs)==len(prior)==186)
for h,p in pairs:
 if prior[p]==h:need('inherited README '+p,True)
 else:
  local=B/'source'/Path(p).name;need('replaced README '+p,sha(local)==h);changed.append(p)
need('two replacements',changed==['checks/check_N4418.py','checks/check_N4418.out'])
code=(B/'source/check_N4418.py').read_text();ast.parse(code)
need('review code hash',sha(B/'source/check_N4418.py')=='04dad65377c0fa6db08bcc48f27f439b28ed323664b01f5eb041b2f0bbc9a440');need('review output hash',sha(B/'source/check_N4418.out')=='24c61edaf70f5b7d81724bdc29ace821dcec2f36a9388f3cd8e0945308bdf412')
oldtree=ast.parse((B/'../theory_final_draft58_audit/source/T1_check_N4418.py').read_text());newtree=ast.parse(code)
def calls(tree):return [ast.dump(n,include_attributes=False) for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='ok']
a,c=calls(oldtree),calls(newtree);diff=[v for v in c if v not in a];need('one added ok',len(c)==len(a)+1 and len(diff)==1 and all(v in c for v in a));need('directed comparison added',"Constant(value=18225240013184170643)" in diff[0] and "Constant(value=364)" in diff[0] and "Constant(value=365)" in diff[0]);need('recorded89','checks passed 89' in (B/'source/check_N4418.out').read_text())
rows={}
for line in (B/'source/closure_matrix.md').read_text().splitlines():
 cells=[x.strip() for x in re.split(r'(?<!\\)\|',line.strip())[1:-1]]
 if len(cells)==11 and cells[0].isdigit():rows[int(cells[0])]=cells
need('108matrix',set(rows)==set(range(1,109)));refs=[]
for m in re.finditer(r'(C1-N1-0\d\d|\b0[0-2]\d\b)[^.;]{0,160}?\brows? (\d+)(?: and (\d+))?',flat):
 name=m.group(1);name=name if name.startswith('C1') else 'C1-N1-'+name
 for token in [m.group(2),m.group(3)]:
  if token is None:continue
  n=int(token);need('reference '+str(len(refs)),n in rows and name in rows[n][1]+' '+rows[n][2]);refs.append([name,n])
need('83references',len(refs)==83 and refs==accepted['theory_final_draft58_audit']['references']);factors=[]
for line in doc.splitlines():
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)!=6 or not re.match(r'\d',cells[1]) or cells[2]=='-':continue
 d=Q(cells[1].split()[0])
 for j,cap in enumerate(['.0000037930','.0000028496','25/54684']):
  shown=cells[2+j];q=d/Q(cap);m=re.fullmatch(r'(\d+)(?:\.(\d+))?(?:e(\d+))?',shown);digits=len(m.group(2) or '')-int(m.group(3) or 0);scale=Q(10)**digits;v=q*scale;floor=Q(v.numerator//v.denominator)/scale;need('factor '+str(len(factors)),Q(shown)==floor<=q);factors.append([cells[0],j,shown])
need('78factors',len(factors)==78 and factors==accepted['theory_final_draft58_audit']['distance_factors'])
for n in [69,70,103,104,107,108]:need('OPEN '+str(n),rows[n][-1].startswith('OPEN'))
for row in read('data/manifest.json'):need('unchanged '+row['local'],sha(B/row['local'])==row['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'target_sha256':sha(B/'source/THEORY_FINAL.md'),'changed_blocks':18,'README_bindings':186,'README_replacements':changed,'references':refs,'distance_factors':factors,'proximity_exact':str(dH),'candidate_integrals_repeated':False,'foreign_code_executed':False,'verdict':'CONFIRMED all18 changed blocks and REVIEWS_v52 literal repairs under accepted premises. No closure or correction-distance ordering. 017 partial lower is separately accepted495; full upper/E2 OPEN.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',out['elapsed_seconds'],'seconds')
