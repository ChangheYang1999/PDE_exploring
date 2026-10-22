#!/usr/bin/env python3
"""Read portable JSON/NPZ data by full hashes; never import numerics code."""
from pathlib import Path
from collections import Counter,defaultdict
from datetime import datetime,timezone
import csv,hashlib,json,math,time,os,re
import numpy as np
V=Path('research/316_portable_residual_package/verification')
NUM=Path('numerics');PKG=NUM/'artifacts/verifier'
start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();counts=Counter();failures=[];observed={}
def ck(cat,ok,detail=None):
 counts[cat+':total']+=1
 if ok:counts[cat+':passed']+=1
 else:failures.append(dict(category=cat,detail=detail))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def localhash(p):
 z=sha(p);observed[str(p)]=z;return z
freeze=json.loads((V/'freeze.json').read_text())
for x in freeze['inputs']:ck('frozen_input',sha(V/x['snapshot'])==x['sha256'],x['snapshot'])
ck('proof_precedes_checks',freeze['utc']<start)
ck('proof_hash',sha(V.parent/'PROOF.md')==freeze['proof_sha256'])
# First reconstruct required entries solely from packaged regional JSON.
regional=sorted(list((PKG/'verification').glob('*/REGIONAL_RESIDUALS.json'))+list((PKG/'research').glob('*/verification/REGIONAL_RESIDUALS.json')))
entries={};records={};regional_hashes={}
for p in regional:
 rel=p.relative_to(PKG).as_posix();h=localhash(p);regional_hashes[rel]=h
 d=json.loads(p.read_text());folder=p.parent.parent.name if p.parent.name=='verification' else p.parent.name
 for st in d['states']:
  key=(folder,st['label']);ck('entry_key_unique',key not in entries,key)
  entries[key]=dict(source_hash=st['source_sha256'],runs=st['runs'],regional_path=rel)
ck('123_portable_entries',len(entries)==123,len(entries));ck('62_regional_files',len(regional)==62,len(regional))
required={d['source_hash']for d in entries.values()};ck('119_required_hashes',len(required)==119,len(required))
# Paths in inventory must themselves be valid. This does not consult the live verifier root.
inv=json.loads((V/'packaged_inventory.json').read_text());inventory_paths=set();inventory_hashes=set()
for st in inv['states']:
 rel=Path(st['archive']);p=PKG/rel
 ck('inventory_path_stays_in_package',not rel.is_absolute() and '..'not in rel.parts,str(rel))
 ck('inventory_archive_present',p.is_file(),str(rel))
 if not p.is_file():continue
 h=localhash(p);ck('inventory_archive_hash',h==st['archive_sha256'],str(rel));inventory_paths.add(str(rel));inventory_hashes.add(h)
 rp=PKG/st['regional_table'];ck('inventory_regional_hash',rp.is_file() and localhash(rp)==st['regional_table_sha256'],st['regional_table'])
ck('61_inventory_archive_paths',len(inventory_paths)==61,len(inventory_paths))
# Discover coefficient archive bytes by full SHA-256 under only the declared portable roots.
# No filename-prefix or rounded-parameter match is used.
paths_by_hash=defaultdict(list);scan_count=0;scan_bytes=0
for root,recursive in [(PKG,True),(NUM/'runs',False)]:
 paths=sorted(root.rglob('*.npz')if recursive else root.glob('*.npz'))
 for p in paths:
  size=p.stat().st_size;h=observed.get(str(p))or localhash(p);scan_count+=1;scan_bytes+=size
  if h in required:paths_by_hash[h].append(p)
ck('all_required_archives_portable',required<=set(paths_by_hash),sorted(required-set(paths_by_hash)))
metadata={};archive_choices={}
META=('K','Nt','a0','beta','beta_basis','continuation_accepted','eps','lam','obj')
for h in sorted(required):
 if h not in paths_by_hash:continue
 choices=sorted(paths_by_hash[h],key=lambda p:(not p.is_relative_to(PKG),str(p)))
 p=choices[0];archive_choices[h]=[x.relative_to(NUM).as_posix()for x in choices]
 with np.load(p,allow_pickle=False)as z:
  ck('portable_archive_has_beta','beta'in z.files,str(p));metadata[h]={}
  for k in META:
   if k in z.files and z[k].size==1:
    value=float(z[k].reshape(-1)[0]);ck('metadata_finite',math.isfinite(value),[str(p),k]);metadata[h]['meta_'+k]=value
bands=[(0.,.03,'0-0.03'),(.03,.3,'0.03-0.3'),(.3,3.,'0.3-3'),(3.,30.,'3-30'),(30.,300.,'30-300'),(300.,math.inf,'300-1e8')]
rows=[]
for (folder,label),st in entries.items():
 if st['source_hash']not in metadata:continue
 before=len(rows)
 for run in st['runs']:
  for rg in run['regions']:
   match=[name for lo,hi,name in bands if float(rg['r_min'])==lo and (math.inf if rg['r_max'] is None else float(rg['r_max']))==hi]
   ck('exact_radial_band',len(match)==1,[folder,label,rg['r_min'],rg['r_max']])
   if len(match)!=1:continue
   row=dict(field=rg['field'],folder=folder,infinite_ratios=rg.get('infinite_ratios',0),kind=run['kind'],label=label,max_abs=rg['max_abs'],max_ratio=rg['max_ratio'],points=rg['points'],region=match[0],zero_normalizers=rg.get('zero_normalizers',0),**metadata[st['source_hash']]);rows.append(row)
 ck('48_rows_per_entry',len(rows)-before==48,[folder,label,len(rows)-before])
fields=sorted({k for row in rows for k in row});out=V/'independently_reconstructed.csv'
with out.open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
# Only after portable reconstruction read the target/original oracle.
keynames=('folder','label','kind','field','region')
def getrows(p):
 with p.open(newline='')as f:r=csv.DictReader(f);header=r.fieldnames;data=list(r)
 return header,{tuple(x[k]for k in keynames):x for x in data},len(data)
head,a,n=getrows(out);target,b,m=getrows(V/'target.csv')
ck('CSV_header_equal',head==target);ck('5904_reconstructed_rows',n==5904,n);ck('reconstructed_key_unique',len(a)==n);ck('target_key_unique',len(b)==m);ck('complete_key_set',set(a)==set(b))
for key,row in a.items():
 if key not in b:continue
 for field in target:
  av=row[field];bv=b[key][field]
  if field in keynames:ok=av==bv
  elif av==''or bv=='':ok=av==bv
  else:ok=float(av)==float(bv)
  ck('every_CSV_value',ok,[key,field,av,bv]if not ok else None)
p313=json.loads((V/'P313_checks.json').read_text());oldfreeze=json.loads((V/'P313_freeze.json').read_text())
for st in p313['states']:
 key=(st['folder'],st['label']);ck('original_state_key',key in entries,key)
 if key in entries:ck('original_state_hash',entries[key]['source_hash']==st['sha256'],key)
for folder,rel in oldfreeze['source_directories'].items():
 path=rel+'/REGIONAL_RESIDUALS.json';ck('packaged_original_regional_hash',regional_hashes.get(path)==p313['input_sha256'][path],path)
original_inv=Path('verification/regional_inventory_20261021T035630Z.json')
ck('packaged_inventory_exact_original',sha(original_inv)==sha(V/'packaged_inventory.json'))
# Independent source-copy and checksum comparison. Read only, never execute/import.
manifest=[]
for line in (V/'code_sha256.txt').read_text().splitlines():
 if not line.strip():continue
 parts=line.split(maxsplit=1);ck('checksum_line_format',len(parts)==2 and bool(re.fullmatch('[a-f0-9]{64}',parts[0])),line)
 if len(parts)!=2:continue
 expected,fn=parts;fn=fn.removeprefix('*');ap=NUM/'artifacts'/fn;cp=NUM/'code'/fn
 ck('manifest_artifact_present',ap.is_file(),fn);ck('manifest_code_present',cp.is_file(),fn)
 ah=localhash(ap)if ap.is_file()else None;ch=localhash(cp)if cp.is_file()else None
 ck('artifact_checksum_current',ah==expected,fn);ck('code_checksum_current',ch==expected,fn);ck('code_artifact_same',ah==ch,fn)
 manifest.append(dict(file=fn,declared=expected,artifact=ah,code=ch))
for p,h in list(observed.items()):
 # Check only files actually relied upon, avoiding a redundant rescan of unrelated run archives.
 if p in {str(x)for h0 in required for x in paths_by_hash.get(h0,[])} or 'REGIONAL_RESIDUALS.json'in p or p.endswith('.py'):
  ck('source_stable_during_read',sha(Path(p))==h,p)
for fn in ['generator_readonly.py','generator_artifact_readonly.py']:ck('generator_copy_freeze_consistency',sha(V/fn)==freeze['inputs'][1 if fn=='generator_readonly.py'else 2]['sha256'])
report=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(v for k,v in counts.items()if k.endswith(':passed')),total=sum(v for k,v in counts.items()if k.endswith(':total')),counts=dict(counts),failures=failures,entries=len(entries),rows=n,regional_files=len(regional),inventory_archive_paths=len(inventory_paths),inventory_unique_hashes=len(inventory_hashes),required_hashes=len(required),matched_hashes=len(required&set(paths_by_hash)),scanned_npz_files=scan_count,scanned_bytes=scan_bytes,archive_choices=archive_choices,source_hashes=observed,regional_hashes=regional_hashes,manifest=manifest,script_sha256=sha(Path(__file__)),reconstructed_csv_sha256=sha(out),scope='Finite portable input sufficiency and independent keyed-data reconstruction; no numerics code executed, no PDE evaluation rerun, no guarantee about an unexecuted filename-based resolver.')
(V/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k]for k in ['started_utc','ended_utc','elapsed_seconds','passed','total','entries','rows','regional_files','inventory_archive_paths','inventory_unique_hashes','required_hashes','matched_hashes','scanned_npz_files','scanned_bytes','script_sha256','reconstructed_csv_sha256']},indent=2));print('FAILURES',json.dumps(failures[:30],indent=2))
