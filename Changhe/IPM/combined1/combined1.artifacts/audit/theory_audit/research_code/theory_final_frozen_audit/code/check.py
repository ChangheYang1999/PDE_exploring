"""Finite final-text verification, never execute peer code or field integrals."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,difflib,gzip,hashlib,json,re,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert v,k
 checks.append(k)
for r in read('data/manifest.json'):need('binding '+r['local'],sha(B/r['local'])==r['sha256'])
need('proof first',not read('data/PROOF_FIRST.json')['checker_exists'] and read('data/PROOF_FIRST.json')['proof_sha256']==sha(B/'PROOF.md'))
doc=(B/'source/THEORY_FINAL.md').read_text();flat=' '.join(doc.split());old=(B/'../theory_final_draft60_audit/source/THEORY_FINAL.md').read_text()
need('final65',sha(B/'source/THEORY_FINAL.md')=='55406b637f5e6c23c0abe0335ec6eab183af73967842a5591c2644663ab61a62')
changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,old.splitlines(),doc.splitlines()).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=a+1,old_stop=b,new_start=c+1,new_stop=d))
need('19changedblocks',len(changes)==19 and changes==read('data/changes.json'))
accepted={}
for topic,count in [('theory_final_draft60_audit',452),('candidate017_partial_replay_audit',10450),('candidate016_prefix47_replay_audit',6234),('candidate016_prefix63_replay_audit',7564),('candidate017_review_repair_acceptance',4710),('prefix63_opus_review_acceptance',473)]:
 r=read('../'+topic+'/verification/result.json');need('accepted '+topic,r['check_count']==len(r['checks'])==count);accepted[topic]=r
p=accepted['candidate016_prefix63_replay_audit'];p47=accepted['candidate016_prefix47_replay_audit']
for k,v in [('H_strict_lower_exact',Q(308366750368225240013184170643,5*10**29)),('H_strict_upper_exact',Q(308948684181969723952067879861,5*10**29)),('E2_strict_lower_exact',Q(628580088526341,10**12)),('E2_strict_upper_exact',Q(39304086799647,62500000000))]:need('exact016 '+k,Q(p[k])==v)
need('H upperdisplay',Q(p['H_strict_upper_exact'])<Q('.617897369'));need('E2 upperdisplay',Q(p['E2_strict_upper_exact'])<Q('628.865389'))
need('Hgapdisplay',Q(p['strict_H_gap_lower'])>Q('.017627007636152'));need('E2gapdisplay',Q(p['strict_E2_gap_lower'])>Q('21.759869525'))
for k in ['H_strict_upper_exact','E2_strict_upper_exact']:need('nesting '+k,Q(p[k])<Q(p47[k]))
h17=accepted['candidate017_partial_replay_audit'];need('017lower',Q(h17['H_strict_lower_exact'])==Q(307209799380023711068567013529,5*10**29)>Q('.614419598760'))
need('017remainsOPEN',h17['complete_H_upper']=='OPEN' and h17['complete_E2_and_017_less_than007']=='OPEN')
fix=accepted['candidate017_review_repair_acceptance'];need('2174generators',fix['source_generator_count']==2174 and fix['source_kinds']==dict(mono=262,leg=1660,legqs=252));f=fix['fixtures']['t4_n3'];need('factor3fixture',Q(f['cross'])==Q(64,35) and Q(f['Q'])*(Q(f['a'])+Q(f['d']))==Q(64,105)**2)
need('explicit factor n','corrects its auxiliary cross bound to n sqrt(Qn (a + d))' in flat)
for phrase in ['14 residual trials, 158 Hardy squares and G0, G1, P2 are not reproduced','each mode gap is the sum of the lower and the upper slack','Neither orders correction distances','Unless expressly compared with eta*','No reference profile of the campaign is shown to satisfy the hypotheses','by the stronger affine L^2 exclusion at every real c']:
 need('scope '+phrase,phrase in flat)
need('exact X3 threshold',Q(1,163840)==Q('.000006103515625')>Q('.0000061035'));need('exact rebal threshold',Q(3,327680)<Q('.0000091553'))
need('X3 quotientfloor',(Q(5169658564469929616848857,10**22)*163840).__floor__()==84699685)
need('rebal quotientfloor',(Q(30325166845552152737989,5*10**19)*Q(327680,3)).__floor__()==66246337)
need('literal contradiction documented','This document quotes neither ratio.' in flat and '84699685 (X3)' in flat and '66246337 (rebal)' in flat)
rv=' '.join((B/'source/REVIEWS_v56.md').read_text().split());need('E16correctrepair','consistent with the rounded FLOAT shares' in rv)
need('first bracket excludes rounded endpoint',not Q('.681')<Q('.681')<Q('.682'));need('second contains rounded display',Q('.682')<Q('.683')<Q('.6835'))
oldpairs={p:h for h,p in re.findall(r'^\s+([a-f0-9]{64})\s+(\S+)\s*$',(B/'../theory_final_draft60_audit/source/README.md').read_text(),re.M)}
pairs=re.findall(r'^\s+([a-f0-9]{64})\s+(\S+)\s*$',(B/'source/README.md').read_text(),re.M);bind=read('data/README_bindings.json')['bindings'];need('195README',len(pairs)==len(bind)==195)
for (h,p),r in zip(pairs,bind):
 need('README '+p,r['path']==p and r['sha256']==h)
 if r['inherited']:need('inherited '+p,oldpairs[p]==h)
 else:
  need('newlocal '+p,sha(B/r['local'])==h)
  if p.endswith('.gz'):need('historical decompressed '+p,hashlib.sha256(gzip.decompress((B/r['local']).read_bytes())).hexdigest()==oldpairs[p[:-3]])
need('175inherited20new',sum(r['inherited'] for r in bind)==175)
for name in ['row_refs','h18_verdicts']:
 a=(B/f'../theory_final_draft58_audit/source/T1_{name}.py').read_text();b=(B/f'source/artifacts/checks/{name}.py').read_text();need('only matrixdefault AST '+name,ast.dump(ast.parse(a))==ast.dump(ast.parse(b.replace('closure_matrix_v170.md','closure_matrix_v157.md'))))
for filename,prior in [('check_N4427.py','../prefix63_opus_review_acceptance/source/T1_checker.py.txt'),('data/N4427_extract.json','../prefix63_opus_review_acceptance/source/T1_extract.json')]:need('accepted R1054 '+filename,sha(B/'source/artifacts/checks'/filename)==sha(B/prior))
for filename,prior in [('check_N4425.py','../candidate017_residual_review_acceptance/source/T1_check.py'),('data/N4425_extract.json','../candidate017_residual_review_acceptance/source/T1_extract.json')]:need('accepted R1053 '+filename,sha(B/'source/artifacts/checks'/filename)==sha(B/prior))
rows={}
for line in (B/'source/closure_matrix_v170.md').read_text().splitlines():
 cells=[x.strip() for x in re.split(r'(?<!\\)\|',line.strip())[1:-1]]
 if len(cells)==11 and cells[0].isdigit():need('unique '+cells[0],int(cells[0]) not in rows);rows[int(cells[0])]=cells
need('108matrix',set(rows)==set(range(1,109)));refs=[]
for m in re.finditer(r'(C1-N1-0\d\d|\b0[0-2]\d\b)[^.;]{0,160}?\brows? (\d+)(?: and (\d+))?',flat):
 name=m.group(1);name=name if name.startswith('C1') else 'C1-N1-'+name
 for token in [m.group(2),m.group(3)]:
  if token is None:continue
  n=int(token);need('reference '+str(len(refs)),n in rows and name in rows[n][1]+' '+rows[n][2]);refs.append([name,n])
need('83references',len(refs)==83 and refs==accepted['theory_final_draft60_audit']['references']);factors=[]
for line in doc.splitlines():
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)!=6 or not re.match(r'\d',cells[1]) or cells[2]=='-':continue
 d=Q(cells[1].split()[0])
 for j,cap in enumerate(['.0000037930','.0000028496','25/54684']):
  shown=cells[2+j];q=d/Q(cap);m=re.fullmatch(r'(\d+)(?:\.(\d+))?(?:e(\d+))?',shown);digits=len(m.group(2) or '')-int(m.group(3) or 0);scale=Q(10)**digits;v=q*scale;floor=Q(v.numerator//v.denominator)/scale;need('factor '+str(len(factors)),Q(shown)==floor<=q);factors.append([cells[0],j,shown])
need('78factors',len(factors)==78 and factors==accepted['theory_final_draft60_audit']['distance_factors'])
for n in [69,70,103,104,107,108]:need('OPEN '+str(n),rows[n][-1].startswith('OPEN'))
for r in read('data/manifest.json'):need('unchanged '+r['local'],sha(B/r['local'])==r['sha256'])
out=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,check_count=len(checks),checks=checks,proof_sha256=sha(B/'PROOF.md'),checker_sha256=sha(Path(__file__)),target_sha256=sha(B/'source/THEORY_FINAL.md'),changed_blocks=19,README_bindings=195,inherited_bindings=175,new_local_bindings=20,references=refs,distance_factors=factors,verdict='CONFIRMED mathematical additions, exact factors, source bindings and REVIEWS_v56 E16. REFUTED only literal sentence This document quotes neither ratio. No candidate or theorem verdict changes; full017 upper,E2 and correction-distance ranking OPEN.',foreign_code_executed=False,new_candidate_integrals=False)
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',out['elapsed_seconds'],'seconds')
