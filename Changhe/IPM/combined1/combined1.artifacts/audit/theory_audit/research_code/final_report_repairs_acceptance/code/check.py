"""Finite source-bound acceptance of four literal report repairs."""
from pathlib import Path
from datetime import datetime,timezone
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
f=read('data/PROOF_FIRST.json');need('proof before checker',not f['checker_exists'] and f['proof_sha256']==sha(B/'PROOF.md'))
for row in read('data/initial_sources.json')['rows']:need('decoded source '+row['local'],hashlib.sha256(text(row['local']).encode()).hexdigest()==row['source_sha256'])
old=text('../frozen_report_1900_diff_audit/source/FINAL_REPORT.md');new=text('source/FINAL_REPORT.md');matrix=text('source/matrix_v182.md.gz');a=old.splitlines();b=new.splitlines();nf=flat(new)
need('new exact target',sha(B/'source/FINAL_REPORT.md')=='12638987379f94b545751c9f96008696718861a3057b5ca02e1165a980b9502a' and len(b)==2967)
need('old exact target',hashlib.sha256(old.encode()).hexdigest()=='ff680b749d855f1c28dfdea1eff56455ca3ded98643838a8c26e3e8dfd57af21' and len(a)==2952)
need('matrix182',hashlib.sha256(matrix.encode()).hexdigest().startswith('ab39ad90'))
changes=[]
for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=i+1,old_end=j,new_start=k+1,new_end=l,old=a[i:j],new=b[k:l]))
need('all thirteen changed blocks',changes==read('data/changes.json') and len(changes)==13)
def table(lines,width,label):
 rows={};physical=[]
 for lineno,line in enumerate(lines,1):
  if not re.match(r'^\|\s*\d',line):continue
  cells=[x.strip() for x in re.split(r'(?<!\\)\|',line.strip())[1:-1]]
  if len(cells)!=width:continue
  physical.append(line)
  for token in re.split(r'\s*,\s*',cells[0]):
   p=token.split('-')
   for n in range(int(p[0]),int(p[-1])+1):need('unique '+label+'/'+str(n),n not in rows);rows[n]=dict(line=lineno,cells=cells)
 return rows,physical
ro,po=table(a,8,'old');rn,pn=table(b,8,'new');rm,pm=table(matrix.splitlines(),11,'matrix')
need('all three complete row sets',set(ro)==set(rn)==set(rm)==set(range(1,109)))
need('all physical report rows byte identical',po==pn and len(pn)==106 and len(pm)==108)
status=lambda row:re.search(r'\b(RULED OUT|OPEN|PROVED|CONDITIONAL)\b',row['cells'][-1]).group(0)
for n in range(1,109):
 r,v=rn[n],rm[n];need('classification '+str(n),status(ro[n])==status(r)==status(v) and status(r) in ['OPEN','RULED OUT'])
 need('unchanged candidate '+str(n),ro[n]['cells'][2]==r['cells'][2])
 c=re.search(r'C1-N1-\d{3}',r['cells'][2]);e=re.search(r'C1-N1-\d{3}',v['cells'][2])
 if c or e:need('matrix candidate '+str(n),bool(c and e) and c.group()==e.group())
 else:
  if v['cells'][2].startswith('C1-BASE-S131'):need('primary state131 '+str(n),r['cells'][2].startswith('C1-BASE-S131'))
  for token in ['d2','Mpen2','b6']:
   if token in v['cells'][2]:need('matrix reference '+str(n)+'/'+token,token in r['cells'][2])
opens=[n for n in rn if status(rn[n])=='OPEN'];need('exact open rows',opens==[4,19,27,33,34,50,69,70,103,104,107,108])
r511=read('../theory_final_replay_comparison/verification/result.json');r512=read('../frozen_report_1900_diff_audit/verification/result.json')
need('accepted511',r511['check_count']==532 and r511['job_count']==69)
need('accepted512',r512['check_count']==1433 and r512['target_sha256']==hashlib.sha256(old.encode()).hexdigest() and r512['substantive_repairs_confirmed']==8)
need('accepted output partition',tuple(len(r511[k]) for k in ['byte_identical_jobs','terminal_rc_only_jobs','runtime_only_jobs'])==(51,3,15))
for name,lo,hi,literals in [('F1',2520,2523,['none differs in a mathematical number, a check count or a verdict','reading of team note v72','producing lane']),('F2',2960,2963,['run times, clock stamps','in three outputs, the stored final rc=0 line','comparison of the saved files','T4-511 and N4-442']),('C1',2954,2960,['Static checks of the selected final evidence','These validators check hashes and links only','mathematics is checked by the per-result scripts','validation_v06.json, 4608 checks','validation_v07.json, 5302 checks']),('C2',2940,2942,['registered scalar and graded correction balls about this reference contain no exact solution','dyadic scheme is also excluded under that scheme\'s stated premises','T4-512 C2'])]:
 block=flat('\n'.join(b[lo-1:hi]))
 for lit in literals:need(name+'/'+lit,lit in block)
for n in [56,57,64]:need('007 excluded registered row '+str(n),'C1-N1-007' in rn[n]['cells'][2] and status(rn[n])=='RULED OUT')
need('process attestation withheld','comparison of saved files, not the execution, the wall time or the core affinity' in nf)
t1=flat(text('source/T1_note72.md'));need('Opus-configured T1 literal acceptance','accepts both literal findings F1 and F2' in t1 and 'mathematical number (coefficient, bound, interval, ratio or count)' in t1 and 'Notes v69 to v71 are not edited' in t1)
v=read('source/validation_v07.json.gz');e=read('source/addenda_map_v02.json')
need('5302 actual checks',v['check_count']==len(v['checks'])==5302 and not v['failures'])
need('main and addenda selections',(v['through_audit'],v['postfreeze_through_audit'],v['unique_evidence_files'],v['postfreeze_evidence_files'],v['postfreeze_source_bindings'])==(505,512,148,28,336))
need('validator hash',v['checker_sha256']=='a681c4c17e63e448e9c2d8418afd026ae8075ba945d85c25ba406f0f64535f59')
need('map hash',v['postfreeze_map_sha256']==sha(B/'source/addenda_map_v02.json')=='d46fa40f0ae784d608411d77db4de20174b96ee7cdb7682e611ca481c5800f91')
need('seven exact audit maps',[r['audit'] for r in e['audits']]==list(range(506,513)) and sum(len(r['records']) for r in e['audits'])==28 and e['baseline_through_audit']==505)
need('immutable snapshot identity',e['addenda_snapshot']['sha256']=='6c05f797cdfb2add7b495ff0903967f62890db691a01270eff4121d646d64a1c')
v6=read('../frozen_report_1900_diff_audit/source/static_validation_v06.json.gz');need('earlier selection retained',v6['check_count']==len(v6['checks'])==4608 and v6['postfreeze_through_audit']==510 and not v6['failures'])
for literal in ['FINAL_ADDENDA_through512.md (6c05f797','FINAL_ADDENDA_EVIDENCE_v02.json (d46fa40f','a file that keeps growing','a681c4c1','addenda through T4-512']:need('quoted source identity '+literal,literal in nf)
need('N4 findings hash',sha(B/'source/N4_findings.md').startswith('244d7ff1') and '244d7ff1' in nf)
need('N4 frozen numerical audit hash',sha(B/'source/N4_numerical_audit.md')=='15dec90541c3708d88dc92c582da16edcdc2c111f04fc6f560c52a34bbf193bc' and '15dec905' in nf)
need('N4 finite audit scope cited','N4-443 (4970 checks)' in nf and '739' not in flat('\n'.join(b[2520:2535])))
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'target_sha256':sha(B/'source/FINAL_REPORT.md'),'predecessor_sha256':hashlib.sha256(old.encode()).hexdigest(),'matrix_sha256':hashlib.sha256(matrix.encode()).hexdigest(),'changed_blocks':13,'physical_rows':106,'logical_rows':108,'open_rows':opens,'repairs_confirmed':['F1','F2','C1','C2'],'static_latest_check_count':5302,'manifest_binding_count':len(m['inputs']),'verdict':'CONFIRMED all four T4-512 repairs, unchanged108rows, and quoted static selection/count. No new claim refuted.','scope':'Literal changed text and saved evidence only. No independent process attestation, no new mathematics, no acceptance of future coordinator edits.'}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print('PASS',r['check_count'],'checks',r['manifest_binding_count'],'bindings',r['elapsed_seconds'],'seconds')
