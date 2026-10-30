"""Static own-lane evidence validation. No research checker or peer code is executed."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,time,gzip
L=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[];failures=[];hash_cache={};parsed=set();bindings=set();decoded=set();roots=[]
def ck(c,msg):
 checks.append(msg)
 if not c:failures.append(msg)
 return c
def local(p):
 p=p.resolve();ck(p.is_relative_to(L),'own-lane path '+str(p))
 if not p.is_relative_to(L):raise ValueError('external path')
 return p
def digest(p):
 p=local(p)
 if p not in hash_cache:
  h=hashlib.sha256()
  with p.open('rb') as f:
   for data in iter(lambda:f.read(1048576),b''):h.update(data)
  hash_cache[p]=h.hexdigest()
 return hash_cache[p]
def parse(p):
 p=local(p);parsed.add(str(p.relative_to(L)));return json.loads(p.read_text())
E=parse(L/'FINAL_EVIDENCE.json');report=E['final_report'];q=L/report['path']
ck(digest(q)==report['sha256'] and q.stat().st_size==report['bytes'],'exact report hash and size')
ck(E['schema']=='T4-final-evidence-v1','evidence schema')
ck(E['state'] in ['WORKING_UNTIL_FREEZE','FROZEN'],'declared state')
expected={'scalar_theorem','forcing_comparison','candidate016_complete','candidate017_partial','normalization','distance_obstruction','candidate001_affine','hardy_alternative','dyadic_alternative','tail_alternative','endpoint_alternative','final_peer_texts'}
ck({g['claim_group'] for g in E['claim_groups']}==expected and len(E['claim_groups'])==12,'twelve unique claim groups')
seen={};manifests={}
for group in E['claim_groups']:
 ck(bool(group['status']) and bool(group['scope']),'status and scope '+group['claim_group'])
 for ev in group['evidence']:
  topic=ev['topic'];ck(any(r['path']==f'research/{topic}/PROOF.md' for r in ev['records']),'standalone argument '+topic)
  for r in ev['records']:
   p=local(L/r['path']);ck(p.is_file(),'evidence exists '+r['path'])
   ck(digest(p)==r['sha256'] and p.stat().st_size==r['bytes'],'evidence hash and size '+r['path'])
   if r['path'] in seen:ck(seen[r['path']]==r,'duplicate record consistent '+r['path'])
   seen[r['path']]=r
   if p.suffix=='.json':a=parse(p)
   if p.name in ['manifest.json','E15_manifest.json']:manifests[p]=a
ck(len(seen)==E['unique_evidence_files'],'unique evidence count')
for p,a in manifests.items():
 base=p.parents[1]
 if isinstance(a,list):rows=a
 else:
  rows=[{'local':k,'sha256':v['sha256'] if isinstance(v,dict) else v} for k,v in a['inputs'].items()]
  if 'proof_sha256' in a:rows.append({'local':'PROOF.md','sha256':a['proof_sha256']})
 for r in rows:
  src=local(base/r['local']);label=str(p.relative_to(L))+':'+r['local'];ck(digest(src)==r['sha256'],'manifest binding '+label);bindings.add(label)
  if r.get('decoded_sha256'):
   ck(src.suffix=='.gz','decoded gzip source '+label);h=hashlib.sha256()
   with gzip.open(src,'rb') as f:
    for data in iter(lambda:f.read(1048576),b''):h.update(data)
   ck(h.hexdigest()==r['decoded_sha256'],'decoded source binding '+label);decoded.add(str(src.relative_to(L)))
postfreeze = parse(L/'FINAL_ADDENDA_EVIDENCE_v04.json');post_seen={};post_bindings=set();post_manifests={}
ck(postfreeze['schema']=='T4-final-addenda-evidence-v1','addenda evidence schema')
ck(postfreeze['baseline_through_audit']==E['through_audit']==505,'same frozen baseline')
ck([row['audit'] for row in postfreeze['audits']]==list(range(506,postfreeze['through_audit']+1)),'consecutive postfreeze audit selection')
for key in ['baseline_report','baseline_evidence','baseline_freeze','addenda_snapshot','count_erratum']:
 r=postfreeze[key];p=local(L/r['path']);ck(digest(p)==r['sha256'] and p.stat().st_size==r['bytes'],'addenda fixed '+key)
for row in postfreeze['audits']:
 ck(any(r['path']==f"research/{row['topic']}/PROOF.md" for r in row['records']),'addenda standalone argument '+str(row['audit']))
 for r in row['records']:
  p=local(L/r['path']);ck(digest(p)==r['sha256'] and p.stat().st_size==r['bytes'],'addenda evidence '+r['path']);post_seen[r['path']]=r
  if p.suffix=='.json':a=parse(p)
  if p.name=='manifest.json':post_manifests[p]=a
ck(len(post_seen)==postfreeze['unique_evidence_files'],'addenda unique evidence count')
for p,a in post_manifests.items():
 base=p.parents[1]
 if isinstance(a,list):rows=a
 else:
  rows=[{'local':k,'sha256':v['sha256'] if isinstance(v,dict) else v} for k,v in a['inputs'].items()]
  if 'proof_sha256' in a:rows.append({'local':'PROOF.md','sha256':a['proof_sha256']})
 for row in rows:
  src=local(base/row['local']);label=str(p.relative_to(L))+':'+row['local']
  ck(digest(src)==row['sha256'],'addenda source binding '+label);post_bindings.add(label)
  if row.get('decoded_sha256'):
   ck(src.suffix=='.gz','addenda gzip source '+label);h=hashlib.sha256()
   with gzip.open(src,'rb') as f:
    for data in iter(lambda:f.read(1048576),b''):h.update(data)
   ck(h.hexdigest()==row['decoded_sha256'],'addenda decoded source binding '+label);decoded.add(str(src.relative_to(L)))
post_map_hash=digest(L/'FINAL_ADDENDA_EVIDENCE_v04.json')
report_text=q.read_text();links=re.findall(r'\]\(([^\s)]+\.md)(?:#[^)]*)?\)',report_text)
ck(sorted(set(links))==E['direct_markdown_links'],'report direct links equal map')
for name in ['FINAL_AUDIT.md','README.md','research/INDEX.md','REPRODUCE.md','finalization/VALIDATION.md','FINAL_ADDENDA.md','FINAL_ADDENDA_through514.md','finalization/COUNT_ERRATUM_v01.md']:
 p=L/name;count=0
 for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',p.read_text()):
  if '://' in target or target.startswith('#'):continue
  target=target.split('#',1)[0]
  if not target:continue
  # Mathematical expressions such as c[h](0) are not Markdown file links.
  if not re.search(r'\.[A-Za-z0-9]+$',target):continue
  t=local(p.parent/target);ck(t.is_file(),'Markdown target '+name+':'+target);count+=1
 roots.append({'path':name,'sha256':digest(p),'local_file_links':count})
ledger=(L/'VERIFY_REPORT.md').read_text();ids=list(map(int,re.findall(r'^## T4-(\d+)',ledger,re.M)))
ck(ids==list(range(1,max(ids)+1)),'ledger IDs complete unique and ordered')
ck(E['through_audit']<=max(ids),'map through audit present')
if E['state']=='WORKING_UNTIL_FREEZE':ck(E['through_audit']==max(ids),'working map through latest audit')
ck('No candidate-framework pair has an a posteriori existence proof.' in report_text,'no existence claim in final')
ck('Complete H upper, E2, and E2 ordering remain OPEN' in report_text,'partial017 scope explicit')
ck('\u2014' not in report_text,'no em dash in final')
# Detect concurrent changes to the map and report without mutating research files.
map_hash=digest(L/'FINAL_EVIDENCE.json');ck(hashlib.sha256((L/'FINAL_EVIDENCE.json').read_bytes()).hexdigest()==map_hash,'map stable during validation');ck(hashlib.sha256(q.read_bytes()).hexdigest()==report['sha256'],'report stable during validation')
checker_hash=digest(Path(__file__))
now=datetime.now(timezone.utc).isoformat();result={'schema':'T4-final-static-validation-v1','utc':now,'elapsed_seconds':time.monotonic()-start,'evidence_map_sha256':map_hash,'report_sha256':report['sha256'],'map_state':E['state'],'through_audit':E['through_audit'],'latest_ledger_audit':max(ids),'postfreeze_map_sha256':post_map_hash,'postfreeze_through_audit':postfreeze['through_audit'],'postfreeze_evidence_files':len(post_seen),'postfreeze_source_bindings':len(post_bindings),'postfreeze_manifest_count':len(post_manifests),'check_count':len(checks),'failures':failures,'unique_evidence_files':len(seen),'unique_files_hashed':len(hash_cache),'json_records_parsed':len(parsed),'source_manifest_count':len(manifests),'source_bindings':len(bindings),'decoded_sources_checked':len(decoded),'root_documents':roots,'checker_sha256':checker_hash,'scope':'Static hashes, source bindings, syntax, links and ledger continuity. This is not a new mathematical proof or research computation replay. No peer code executes; all reads and writes are within the own lane.','checks':checks}
existing=[int(p.stem.rsplit('v',1)[1]) for p in (L/'finalization').glob('validation_v[0-9][0-9].json')];v=max(existing,default=0)+1;out=L/f'finalization/validation_v{v:02d}.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n')
print('PASS' if not failures else 'FAIL',out.name,now,len(checks),'checks',len(seen),'evidence',len(bindings),'source bindings',len(hash_cache),'files hashed',result['elapsed_seconds'],'seconds')
if failures:
 print('\n'.join(failures));raise SystemExit(1)
