"""Current local-byte integrity only. Never executes any evidence program."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/final_evidence_integrity'
now=lambda:datetime.now(timezone.utc).isoformat()
def main():
 started=time.monotonic();start=now();target=B/'verification/result_v02.json';assert not target.exists()
 cache={};observed={};edges=[];errors=[];roots=[]
 def signature(p):
  s=p.stat();return(s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns)
 def digest(path,decoded=False):
  p=Path(path);p=p if p.is_absolute() else R/p;q=p.resolve(strict=True)
  assert q.is_relative_to(R),('outside own lane',str(q))
  sig=signature(q);key=(str(q),decoded,sig)
  if key not in cache:
   h=sha256()
   with (gzip.open(q,'rb') if decoded else q.open('rb')) as f:
    while chunk:=f.read(1024*1024):h.update(chunk)
   assert signature(q)==sig,('changed while reading',str(q));cache[key]=h.hexdigest()
  observed[str(q)]=sig
  return cache[key]
 def check(owner,kind,path,expected,decoded=False):
  row={'owner':owner,'kind':kind,'path':path,'expected_sha256':expected,'decoded_gzip':decoded}
  try:
   assert isinstance(expected,str) and re.fullmatch('[a-f0-9]{64}',expected),('unsupported digest',expected)
   row['actual_sha256']=digest(path,decoded);row['pass']=row['actual_sha256']==expected
   if not row['pass']:row['error']='digest mismatch'
  except Exception as e:row['pass']=False;row['error']=str(e)
  edges.append(row)
  if not row['pass']:errors.append(row)
  return row['pass']
 prepared=json.loads((B/'verification/PROOF_FIRST_v02.json').read_text())
 assert not prepared['checker_exists']
 assert digest(B/'ENCODING_PROOF_v02.md')==prepared['supplement_sha256']
 assert digest(B/'verification/result_v01.json')==prepared['first_result_sha256']
 assert digest(B/'PROOF.md')==prepared['proof_sha256']
 assert digest(B/'source/selection_v02.json')==prepared['selection_sha256']
 selection=json.loads((B/'source/selection_v02.json').read_text());ledger=(B/'source/VERIFY_REPORT_v01.md').read_text()
 for row in selection:
  owner=row['claim'];assert row['sha256'] in ledger,('digest not cited in frozen ledger',owner)
  okay=check(owner,'root',row['record'],row['sha256']);root=dict(row,root_digest_pass=okay)
  try:root['current_proof_sha256']=digest(row['proof'])
  except Exception as e:root['proof_error']=str(e);errors.append({'owner':owner,'path':row['proof'],'error':str(e)})
  if okay:
   d=json.loads((R/row['record']).read_text());root['recorded_utc']=d.get('utc');root['recorded_verdict']=d.get('verdict',d.get('status'))
   decoded=set(row.get('decoded_gzip_inputs',[]))
   if decoded:
    assert set(decoded).issubset(d['inputs'])
    mp=row['encoding_manifest'];sp=row['encoding_source']
    assert check(owner,'encoding_source',sp,row['encoding_source_sha256'])
    assert d['inputs'][sp]==row['encoding_source_sha256'] and check(owner,'encoding_manifest',mp,d['inputs'][mp])
    manifest=json.loads((R/mp).read_text());entries={e['local']:e for e in manifest['files'].values()}
    for path in decoded:
     e=entries[path];assert e['encoding']=='gzip' and e['sha256']==d['inputs'][path] and Path(path).suffix=='.gz'
     check(owner,'explicit_gzip_stored',path,e['stored_sha256'])
   for key in ['inputs','own_inputs']:
    for path,expected in d.get(key,{}).items():check(owner,key,path,expected,path in decoded)
   for path,e in d.get('frozen_or_retained_sources',{}).items():
    check(owner,'stored_peer_source',path,e['stored_sha256'])
    if e.get('gzip'):check(owner,'decoded_peer_source',path,e['sha256'],True)
    elif e['sha256']!=e['stored_sha256']:errors.append({'owner':owner,'path':path,'error':'plain stored/original digest disagreement'})
  roots.append(root)
 changed=[]
 for path,sig in observed.items():
  try:
   if signature(Path(path))!=sig:changed.append(path)
  except OSError:changed.append(path)
 if changed:errors.extend({'path':p,'error':'changed during audit'} for p in changed)
 inputs={str(p.relative_to(R)):digest(p) for p in [Path(__file__),B/'PROOF.md',B/'source/selection_v02.json',B/'ENCODING_PROOF_v02.md',B/'verification/result_v01.json',B/'source/VERIFY_REPORT_v01.md',B/'verification/PROOF_FIRST_v02.json']}
 result={'start_utc':start,'utc':now(),'selection_count':len(selection),'direct_edge_count':len(edges),'unique_resolved_files':len(observed),'decoded_streams':sum(k[1] for k in cache),'inputs':inputs,'roots':roots,'edges':edges,'errors':errors,'all_direct_edges_match':not errors,'scope':'Current explicitly recorded local direct bindings only; no unlisted transitive integrity, mathematical replay or status promotion.','expensive_computation_repeated':False,'foreign_files_read_or_executed':False,'elapsed_seconds':time.monotonic()-started,'verdict':'CONFIRMED selected current local-byte integrity' if not errors else 'OPEN selected current local-byte integrity: inspect errors'}
 with target.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 result_sha=digest(target)
 index={'utc':result['utc'],'integrity_result':str(target.relative_to(R)),'integrity_result_sha256':result_sha,'integrity_scope':result['scope'],'all_direct_edges_match':not errors,'entries':roots,'pending':['016 full P2 and Hardy upper bound','Independent actual026 acceptance','Immutable027 and028 snapshot audits','All inverse and existence closures']}
 with (R/'FINAL_EVIDENCE_INDEX_v02.json').open('x') as f:json.dump(index,f,indent=2);f.write('\n')
 print(result['utc'],result['verdict'],'roots',len(roots),'edges',len(edges),'unique',len(observed),'decoded',result['decoded_streams'],'elapsed',result['elapsed_seconds'],'SHA256',result_sha,flush=True)
 for e in errors:print('ERROR',json.dumps(e),flush=True)
if __name__=='__main__':main()
