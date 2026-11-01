"""Inventory admission references without confusing changed inputs with new proof."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,os,re,sys,time
from reconstruct_text_delta import reconstruct
sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('--max-raw-mib',type=int,default=64);a=ap.parse_args()
limit=a.max_raw_mib*1024**2;begin=time.monotonic();now=datetime.now(timezone.utc)
folder=Path('artifacts/final_audit')/now.strftime('%Y%m%dT%H%M%SZ');folder.mkdir(parents=True)
archives={}
for p in Path('artifacts/storage').glob('json_compression_*.json'):
 for row in json.loads(p.read_text()).get('rows',[]):archives[row['original']]=row
cache={};references=[];admissions=[]
bindings=[]
for bp in [Path('research/301_final_claim_audit/verification/historical_reading_bindings.json'),Path('research/301_final_claim_audit/verification/historical_reference_bindings.json')]:
 if bp.exists():
  for binding in json.loads(bp.read_text())['bindings']:
   bindings.append(dict(binding,binding_manifest=str(bp),binding_manifest_sha256=sha256(bp.read_bytes()).hexdigest()))
def filehash(path):
 st=path.stat();key=(str(path),st.st_size,st.st_mtime_ns)
 if key not in cache:
  h=sha256()
  with path.open('rb') as f:
   for chunk in iter(lambda:f.read(1024**2),b''):h.update(chunk)
  cache[key]=h.hexdigest()
 return cache[key]
def verify(ref):
 path=Path(ref['path']);expected=ref['sha256'];out=dict(path=str(path),expected_sha256=expected)
 if path.is_absolute():return dict(out,status='absolute_path')
 if path.exists():
  if not path.is_file():return dict(out,status='not_a_file')
  actual=filehash(path);return dict(out,status='match' if actual==expected else 'changed',actual_sha256=actual,bytes=path.stat().st_size)
 row=archives.get(str(path))
 if row:
  packed=Path(row['archive']);actual=filehash(packed)
  if actual!=row['archive_sha256']:return dict(out,status='changed_archive',archive=str(packed))
  if expected!=row['original_sha256']:return dict(out,status='different_historical_version',archive=str(packed),archived_raw_sha256=row['original_sha256'])
  if row['original_bytes']>limit:return dict(out,status='raw_replay_deferred',archive=str(packed),archive_hash_matches=True)
  h=sha256()
  with gzip.open(packed,'rb') as f:
   for chunk in iter(lambda:f.read(1024**2),b''):h.update(chunk)
  actual=h.hexdigest();return dict(out,status='match_lossless_archive' if actual==expected else 'changed_raw',actual_sha256=actual,archive=str(packed))
 return dict(out,status='missing')
def walk(obj,trail=''):
 if isinstance(obj,dict):
  if isinstance(obj.get('path'),str) and isinstance(obj.get('sha256'),str) and re.fullmatch('[0-9a-f]{64}',obj['sha256']):yield trail,obj
  for key,value in obj.items():yield from walk(value,trail+'/'+key)
 elif isinstance(obj,list):
  for i,value in enumerate(obj):yield from walk(value,trail+'/'+str(i))
for path in sorted(Path('research').rglob('*admission*.json')):
 obj=json.loads(path.read_text());admissions.append(dict(path=str(path),sha256=filehash(path),verdict=obj.get('verdict'),ledger=obj.get('ledger',obj.get('entry'))))
 for trail,ref in walk(obj):
  checked=verify(ref)
  if trail=='/proof' and checked['status']=='changed' and isinstance(obj.get('proof_snapshot'),dict):
   snapshot=obj['proof_snapshot'];saved=verify(snapshot)
   if snapshot['sha256']==ref['sha256'] and saved['status'].startswith('match'):
    checked.update(status='historical_proof_snapshot_match',current_path_changed=True,snapshot=snapshot)
  if checked['status'] in ['changed','missing']:
   for binding in bindings:
    if binding['admission']!=str(path) or binding['original_path']!=ref['path'] or binding['sha256']!=ref['sha256']:continue
    if 'field' in binding and binding['field']!=trail:continue
    if 'snapshot' in binding:
     saved=verify(dict(path=binding['snapshot'],sha256=ref['sha256']))
     if saved['status'].startswith('match'):
      checked.update(status='historical_snapshot_match',current_path_changed=True,snapshot=binding['snapshot'],binding_manifest=binding['binding_manifest'],binding_manifest_sha256=binding['binding_manifest_sha256'])
    elif 'delta' in binding:
     saved=verify(binding['delta'])
     if saved['status'].startswith('match'):
      raw=reconstruct(binding['delta']['path'])
      if sha256(raw).hexdigest()==ref['sha256']:
       checked.update(status='historical_delta_match',current_path_changed=True,delta=binding['delta'],binding_manifest=binding['binding_manifest'],binding_manifest_sha256=binding['binding_manifest_sha256'])
  references.append(dict(admission=str(path),field=trail,**checked))
counts={}
for row in references:counts[row['status']]=counts.get(row['status'],0)+1
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),method='Hash references embedded in admission receipts. A changed live input is reported, not silently treated as an invalid historical proof. Large raw archive replays may be deferred explicitly.',admission_count=len(admissions),reference_count=len(references),status_counts=counts,admissions=admissions,references=references,actual_elapsed_s=time.monotonic()-begin)
(folder/'admission_reference_checks.json').write_text(json.dumps(result,indent=2)+'\n')
(folder/'final_evidence_audit.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ['admissions','references']}))
for row in references:
 if not row['status'].startswith('match') and row['status'] not in ['historical_proof_snapshot_match','historical_snapshot_match','historical_delta_match']:print(json.dumps(row))
