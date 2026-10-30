from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,tarfile,io,gzip,difflib
L=Path.cwd();B=L/'research/theory_final_draft56_audit';T=L.parent/'c1-t1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for d in ['source','data','code','verification']:(B/d).mkdir(parents=True,exist_ok=True)
files={'THEORY_FINAL.md':T/'THEORY_FINAL.md','T1_note59.md':T/'notes/T1_TEAM_NOTE_v59.md','T1_REVIEWS_v51.md':T/'nonlinear_closure/REVIEWS_v51.md','T1_README.md':T/'artifacts/README.md','T1_check_N4418.py':T/'artifacts/checks/check_N4418.py','T1_check_N4418.out':T/'artifacts/checks/check_N4418.out','closure_matrix_v155.md':T/'artifacts/checks/data/closure_matrix_v155.md','T1_row_refs.py':T/'artifacts/checks/row_refs.py','T1_h18_verdicts.py':T/'artifacts/checks/h18_verdicts.py'}
rows=[]
for name,p in files.items():
 raw=p.read_bytes();(B/'source'/name).write_bytes(raw);rows.append({'source':str(p),'local':'source/'+name,'sha256':hashlib.sha256(raw).hexdigest()})
assert sha(B/'source/THEORY_FINAL.md')=='4ff4b6625d190e1f74b04ca2a857c7b6fe4c8a0008aa03ee42c5ecc0dc9bd1d6'
old=(L/'research/theory_final_draft55_audit/source/THEORY_FINAL.md').read_text().splitlines();new=(B/'source/THEORY_FINAL.md').read_text().splitlines();changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,old,new).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=a+1,old_stop=b,new_start=c+1,new_stop=d))
(B/'source/changes.diff').write_text('\n'.join(difflib.unified_diff(old,new,fromfile='accepted55',tofile='frozen56',n=2))+'\n');(B/'data/changes.json').write_text(json.dumps(changes,indent=2)+'\n')
prior=json.loads((L/'research/theory_final_draft55_audit/data/README_bindings.json').read_text()); priorrows={r['local']:r for r in prior['bindings']}
records=re.findall(r'^\s+([a-f0-9]{64})\s+(\S+)\s*$',(B/'source/T1_README.md').read_text(),re.M);buf=io.BytesIO();bindings=[];nnew=0
with tarfile.open(fileobj=buf,mode='w') as tar:
 for h,p in records:
  raw=(T/'artifacts'/p).read_bytes();assert hashlib.sha256(raw).hexdigest()==h,p
  useold=p in priorrows and priorrows[p]['sha256']==h
  bindings.append({'local':p,'sha256':h,'bytes':len(raw),'archive':'prior' if useold else 'delta'})
  if not useold:
   ti=tarfile.TarInfo(p);ti.size=len(raw);ti.mtime=0;tar.addfile(ti,io.BytesIO(raw));nnew+=1
raw=gzip.compress(buf.getvalue(),compresslevel=6,mtime=0);(B/'source/README_delta.tar.gz').write_bytes(raw)
(B/'data/README_bindings.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'prior_archive_sha256':prior['archive_sha256'],'delta_archive_sha256':hashlib.sha256(raw).hexdigest(),'bindings':bindings},indent=2)+'\n')
(B/'data/initial_sources.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'sources':rows},indent=2)+'\n')
print('sources',len(rows),'changedblocks',len(changes),'README',len(bindings),'new',nnew,'compressed bytes',len(raw))
