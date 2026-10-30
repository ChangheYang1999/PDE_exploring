"""Check a nominated report diff against immutable accepted audit records."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,gzip,hashlib,re,time,difflib
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def text(p):
 p=B/p;raw=p.read_bytes();return (gzip.decompress(raw) if p.suffix=='.gz' else raw).decode()
def read(p):return json.loads(text(p))
def need(k,v):
 assert v,k
 checks.append(k)
flat=lambda s:' '.join(s.split())
m=read('data/manifest.json')
for p,h in m['inputs'].items():need('binding '+p,sha(B/p)==h)
f=read('data/PROOF_FIRST.json');need('argument before checker',not f['checker_exists'] and f['proof_sha256']==sha(B/'PROOF.md'))
for row in read('data/initial_sources.json')['rows']:
 need('decoded source '+row['local'],hashlib.sha256(text(row['local']).encode()).hexdigest()==row['source_sha256'])
old=text('../frozen_report_1837_audit/source/FINAL_REPORT.md');new=text('source/FINAL_REPORT.md');matrix=text('source/matrix_v180.md.gz');a=old.splitlines();b=new.splitlines();nf=flat(new)
need('nominated report identity',sha(B/'source/FINAL_REPORT.md')=='ff680b749d855f1c28dfdea1eff56455ca3ded98643838a8c26e3e8dfd57af21' and len(b)==2952)
need('old report identity',hashlib.sha256(old.encode()).hexdigest()=='7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743' and len(a)==2867)
need('official diff identity',sha(B/'source/official.diff')=='32240684cb3f069b2a8bcbc9b3bdfb8162a932f5206f402e32f67a8498f592f7')
need('nominated matrix180',hashlib.sha256(matrix.encode()).hexdigest().startswith('51bad26b') and 'v180' in matrix[:4000])
need('nominated target request',sha(B/'source/FINAL_REPORT.md') in text('source/COORD_REQUEST.md.gz'))
# Reconstruct from unified hunks, independently of the saved sequence-comparison blocks.
d=text('source/official.diff').splitlines(keepends=True);original=old.splitlines(keepends=True);out=[];cursor=0;i=2;hunks=0
while i<len(d):
 h=re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',d[i]);need('diff header '+str(i),h is not None)
 os_,oc,ns,nc=[int(x) if x is not None else 1 for x in h.groups()];pos=os_-1 if oc else os_;need('ordered hunk '+str(hunks),pos>=cursor)
 out.extend(original[cursor:pos]);cursor=pos;need('new hunk start '+str(hunks),len(out)==(ns-1 if nc else ns));i+=1;used=added=0
 while i<len(d) and not d[i].startswith('@@ '):
  tag=d[i][0];payload=d[i][1:];need('diff line type '+str(i),tag in ' +-')
  if tag in ' -':need('old diff content '+str(i),original[cursor]==payload);cursor+=1;used+=1
  if tag in ' +':out.append(payload);added+=1
  i+=1
 need('hunk lengths '+str(hunks),used==oc and added==nc);hunks+=1
out.extend(original[cursor:]);need('full exact reconstruction',''.join(out)==new and hunks==18)
changes=[]
for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=i+1,old_end=j,new_start=k+1,new_end=l,old=a[i:j],new=b[k:l]))
need('every changed block retained',changes==read('data/changes.json') and len(changes)==29)
def table(lines,width,label):
 rows={};nphysical=0
 for lineno,line in enumerate(lines,1):
  if not re.match(r'^\|\s*\d',line):continue
  cells=[x.strip() for x in re.split(r'(?<!\\)\|',line.strip())[1:-1]]
  if len(cells)!=width:continue
  nphysical+=1
  for token in re.split(r'\s*,\s*',cells[0]):
   p=token.split('-')
   for n in range(int(p[0]),int(p[-1])+1):need('unique '+label+'/'+str(n),n not in rows);rows[n]=dict(line=lineno,cells=cells)
 return rows,nphysical
ro,po=table(a,8,'old');rn,pn=table(b,8,'new');rm,pm=table(matrix.splitlines(),11,'matrix')
need('complete three row sets',set(ro)==set(rn)==set(rm)==set(range(1,109)))
need('physical row counts',(po,pn,pm)==(106,106,108))
status=lambda row:re.search(r'\b(RULED OUT|OPEN|PROVED|CONDITIONAL)\b',row['cells'][-1]).group(0)
rowchecks=[]
for n in range(1,109):
 oldr,r,v=ro[n],rn[n],rm[n];need('unchanged classification '+str(n),status(oldr)==status(r)==status(v) and status(r) in ['OPEN','RULED OUT'])
 need('unchanged candidate '+str(n),oldr['cells'][2]==r['cells'][2])
 c=re.search(r'C1-N1-\d{3}',r['cells'][2]);e=re.search(r'C1-N1-\d{3}',v['cells'][2])
 if c or e:need('matrix candidate '+str(n),bool(c and e) and c.group()==e.group())
 else:
  for token in ['C1-BASE-S131','d2','Mpen2','b6']:
   if token in v['cells'][2]:need('matrix reference '+str(n)+'/'+token,token in r['cells'][2])
 rowchecks.append(dict(row=n,line=r['line'],status=status(r),candidate=r['cells'][2]))
opens=[n for n in rn if status(rn[n])=='OPEN'];need('exact open set',opens==[4,19,27,33,34,50,69,70,103,104,107,108])
accepted={}
for audit,topic,count in [(485,'sharpw_maximum_review_acceptance',57),(488,'candidate016_complete_bounds_reciprocal',121),(502,'candidate016_prefix63_replay_audit',7564),(504,'prefix63_opus_review_acceptance',473),(506,'theory_final_frozen_audit',828),(507,'t2_final_frozen_audit',73),(508,'frozen_report_1837_audit',1083),(509,'energy_share_attribution_acceptance',95),(510,'rounded_table_display_audit',59),(511,'theory_final_replay_comparison',532)]:
 r=read('../'+topic+'/verification/result.json');need('accepted dependency '+str(audit),r['check_count']==count);accepted[audit]=r
need('old audit matches target',accepted[508]['target_sha256']==hashlib.sha256(old.encode()).hexdigest())
mu=Q(97,250)-Q(397,5184);A=Q(8,5)*72;radius=mu/(2*A);eta=mu*mu/(4*A)
need('same fixed optimum',radius==Q(201799,149299200)==Q(accepted[485]['radius_star_exact']) and eta==Q(40722836401,193491763200000)==Q(accepted[485]['eta_star_exact']))
need('complete square',2*A*radius==mu and A*radius**2==eta)
for lo,hi in [(42,51),(110,121)]:
 block=flat('\n'.join(b[lo-1:hi]))
 for literal in ['maximum of this one audited sufficient estimate at s = 1/5184 and w = (2^15, 2^20)','background hypotheses retained','40722836401/193491763200000','201799/149299200']:
  need('F1 repair '+str(lo)+'/'+literal,literal in block)
for lo,hi,literals in [(1308,1309,['AUDITED','T4-337']), (1712,1715,['AUDITED','T4-443','T4-452','T4-454','T4-464','no proved obstruction']), (1705,1708,['selected sharpw sufficient residual test','constants fixed','not a necessary condition for every route']), (1690,1692,['slack','T4-504','T4-505','does not determine it'])]:
 block=flat('\n'.join(b[lo-1:hi]))
 for literal in literals:need('scope repair '+str(lo)+'/'+literal,literal in block)
for lo,hi in [(65,66),(146,147),(1139,1139),(2370,2371)]:need('precision repair '+str(lo),'T4-488' in '\n'.join(b[lo-1:hi]))
need('accepted fine E2 bound',Q(accepted[488]['E2_strict_lower_exact'])==Q(accepted[502]['E2_strict_lower_exact'])==Q('628.580088526341'))
need('accepted fine E2 gap',Q(accepted[488]['strict_E2_gap_lower'])==Q(accepted[502]['strict_E2_gap_lower'])==Q('21.759869526341'))
for lo,hi in [(233,234),(999,1001)]:
 block=flat('\n'.join(b[lo-1:hi]));need('energy attribution '+str(lo),'E_star^2=P2^2+2^14 G1^2+2^18 G0^2' in block and 'T4-509' in block and '72 percent' in block and '14 percent' in block)
need('actual fractional G0 share',Q(accepted[509]['actual_fractional_sharpw_G0_share_lower_exact'])>Q(1,4) and 'more than one quarter' in flat('\n'.join(b[2502:2515])))
legend=flat('\n'.join(b[1055:1060]));need('rounded summary convention','rounded summaries' in legend and 'not directed bounds' in legend and 'residual value or bound' in legend and 'exact underlying bounds' in legend)
for row in accepted[510]['rows']:
 display,lo,hi,unit=map(Q,[row['display_exact'],row['lower_exact'],row['upper_exact'],row['unit_exact']]);need('retained nearest example '+str(row['table_row']),display-unit/2<lo<=hi<display<display+unit/2)
need('017 no new upper promotion','source premises OPEN' in rn[82]['cells'][4] and 'conditional arithmetic' in rn[82]['cells'][4])
# Static evidence identities and finite counts; no claim that this checks all mathematics.
receipt=read('source/static_validation_v06.json.gz');need('4608 actual listed checks',receipt['check_count']==len(receipt['checks'])==4608)
need('static no failures',receipt['failures']==[])
need('fixed static coverage',receipt['through_audit']==505 and receipt['postfreeze_through_audit']==510 and receipt['unique_evidence_files']==148 and receipt['postfreeze_evidence_files']==20)
need('validator identity',hashlib.sha256(text('source/static_validate_evidence_v02.py.gz').encode()).hexdigest()==receipt['checker_sha256']=='e5da1bcde66ca8f19e7b17cdf96548bfe0a0b057c45c8ff348f52ad439d93e28')
for name,prefix in [('FINAL_AUDIT.md','006d2852'),('FINAL_EVIDENCE.json','6ec562cc'),('FREEZE.json','acd96877'),('FINAL_ADDENDA_through510.md','387c487f'),('FINAL_ADDENDA_EVIDENCE_v01.json','dbf36e38')]:
 need('quoted immutable hash '+name,hashlib.sha256(text('source/static_'+name+'.gz').encode()).hexdigest().startswith(prefix) and prefix in flat('\n'.join(b[1180:1198])))
sec8=flat('\n'.join(b[2922:]));need('separate integrity from mathematics','check hashes and links only; the mathematics is checked by the per-result scripts' in sec8 and '49 selected evidence roots' in sec8)
need('three named scripts',all(p in sec8 for p in ['finalization/validate_evidence.py','finalization/validate_evidence_v02.py','research/final_evidence_integrity/code/check_v04.py']))
r=accepted[511];need('rerun finite partition',r['job_count']==69 and len(r['byte_identical_jobs'])==51 and len(r['terminal_rc_only_jobs'])==3 and len(r['runtime_only_jobs'])==15)
need('only stated side changes',[x['different_keys'] for x in r['side_records']]==[['seconds'],[],['seconds']])
need('F1 literal present','none differs' in b[2520] and 'in a number, a check count or a verdict' in b[2521])
need('F2 incomplete exceptions','run times and' in b[2946] and 'clock stamps' in b[2947] and 'rc=0' not in '\n'.join(b[2946:2948]))
need('producing-lane scope explicit','This is a rerun by the producing lane' in flat('\n'.join(b[2520:2523])))
need('C1 selected label','Whole-ledger checks' in b[2940] and 'These two' in b[2944])
need('C2 approximate label','not an approximate solution in any registered ball' in b[2928])
findings=[{'id':'F1','lines':[2521,2522],'verdict':'REFUTED literal','repair':'Replace in a number with in a mathematical number.'},{'id':'F2','lines':[2947,2948],'verdict':'REFUTED complete exception list','repair':'Include the terminal rc=0 line among the allowed differences.'},{'id':'C1','lines':[2941,2946],'verdict':'CLARIFICATION','repair':'Static checks of the selected final evidence; These validators.'},{'id':'C2','lines':[2928,2929],'verdict':'CLARIFICATION','repair':'State exclusion of exact solutions in the registered correction balls and conditional dyadic scheme.'}]
result=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,check_count=len(checks),checks=checks,proof_sha256=sha(B/'PROOF.md'),checker_sha256=sha(Path(__file__)),target_sha256=sha(B/'source/FINAL_REPORT.md'),old_target_sha256=hashlib.sha256(old.encode()).hexdigest(),matrix_sha256=hashlib.sha256(matrix.encode()).hexdigest(),diff_sha256=sha(B/'source/official.diff'),unified_hunks=hunks,changed_blocks=len(changes),physical_rows=pn,logical_rows=len(rn),open_rows=opens,row_comparisons=rowchecks,eta_star_exact=str(eta),radius_star_exact=str(radius),substantive_repairs_confirmed=8,findings=findings,static_receipt_check_count=4608,verdict='CONFIRMED eight substantive repairs and108status/candidate rows; REFUTED two literal rerun descriptions; two label clarifications.',scope='Changed text only, plus finite row and exact-constant comparisons. No mathematical re-audit of unchanged history, no existence closure, no peer execution or new integrals.')
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks;',len(changes),'changed blocks;',hunks,'hunks;',len(rn),'rows;',result['elapsed_seconds'],'seconds')
