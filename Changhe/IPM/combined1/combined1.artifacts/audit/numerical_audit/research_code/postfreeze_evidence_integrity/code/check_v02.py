"""Check the selected postfreeze roots and all recorded direct local inputs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,os,re,time
R=Path(__file__).resolve().parents[3]
B=R/'research/postfreeze_evidence_integrity'
def now():return datetime.now(timezone.utc).isoformat()
def main():
 assert os.sched_getaffinity(0)=={57}
 assert os.getpriority(os.PRIO_PROCESS,0)==19
 start=now();tick=time.monotonic()
 target=B/'verification/result_v02.json';index_target=R/'POSTFREEZE_EVIDENCE_INDEX_v02.json'
 assert not target.exists()and not index_target.exists()
 cache={};observed={};checks=[];edges=[];roots=[];errors=[];inputs={}
 def ck(value,label):
  checks.append({'check':label,'pass':bool(value)})
  if not value:errors.append(label)
  assert value,label
 def signature(p):
  s=p.stat();return s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns
 def digest(path):
  p=Path(path);p=p if p.is_absolute()else R/p;q=p.resolve(strict=True)
  assert q.is_relative_to(R),('outside lane',q)
  sig=signature(q);key=(str(q),sig)
  if key not in cache:
   h=hashlib.sha256()
   with q.open('rb')as f:
    for chunk in iter(lambda:f.read(1<<20),b''):h.update(chunk)
   assert signature(q)==sig,('changed while reading',q)
   cache[key]=h.hexdigest()
  observed[str(q)]=sig
  return cache[key]
 def bind(path,expected,label):
  ck(isinstance(path,str)and isinstance(expected,str)and re.fullmatch('[0-9a-f]{64}',expected) is not None,'schema '+label)
  actual=digest(path);ck(actual==expected,'digest '+label);return actual
 marker=json.loads((B/'verification/PROOF_FIRST_v02.json').read_text())
 ck(not marker['checker_exists']and not marker['result_exists'],'proof before code')
 for p,h in marker['inputs'].items():bind(p,h,'predeclared '+p);inputs[p]=h
 for p in [Path(__file__),B/'verification/PROOF_FIRST_v02.json']:
  inputs[str(p.relative_to(R))]=digest(p)
 selection=json.loads((B/'source/selection_v02.json').read_text())
 ledger=(B/'source/ledger436_446.md').read_text();blocks=re.split(r'(?m)(?=^## )',ledger)
 ck(selection['root_count']==len(selection['roots'])==11,'eleven selected roots')
 ck({r['audit']for r in selection['roots']}==set(range(436,447)),'exact consecutive selected audit IDs')
 for row in selection['roots']:
  n=row['audit'];p=R/row['path'];bind(row['path'],row['sha256'],'root '+str(n));inputs[row['path']]=row['sha256']
  match=[b for b in blocks if re.match(r'## (?:N4-)?'+str(n)+r'\b',b)]
  ck(len(match)==1 and row['sha256']in match[0],'ledger binding '+str(n))
  root=json.loads(p.read_text());mapping=root['inputs'];ck(isinstance(mapping,dict)and len(mapping)==row['direct_input_count'],'complete direct input map '+str(n))
  for rel,h in mapping.items():
   actual=bind(rel,h,str(n)+' '+rel);edges.append({'owner':n,'path':rel,'expected_sha256':h,'actual_sha256':actual,'pass':True})
  proof=R/row['proof'];proof_hash=digest(proof);previously_bound=row['proof']in mapping
  if previously_bound:ck(mapping[row['proof']]==proof_hash,'previously bound retained proof '+str(n))
  roots.append(dict(row,retained_proof_sha256=proof_hash,proof_already_bound_in_root=previously_bound))
 ck(len(edges)==selection['direct_input_count']==1994,'all1994directedgesenumerated')
 for rel,h in selection['frozen_documents'].items():bind(rel,h,'frozen document '+rel)
 ck(selection['frozen_documents']['AUDIT_SUMMARY.md']=='d9e0c36554b1aff4f5ebe0809133e8397f6cd8f114b16af63091f92fd3863931','summary original freeze')
 ck(selection['frozen_documents']['FINAL_REPORT_NUMERICAL_AUDIT.md']=='15dec90541c3708d88dc92c582da16edcdc2c111f04fc6f560c52a34bbf193bc','numerical audit original freeze')
 ck(selection['frozen_documents']['NEXT_AUDIT_PLAN.md']=='b4e5e460f4844e4853a8d99bfdf37de80dace0e2a7c3bcc4921c99ed29d7f934','next plan original freeze')
 ck(selection['frozen_documents']['FINAL_EVIDENCE_INDEX_v03.json']=='a66ac924b3d283b883b9a1846eca00eaaba1799f1bd26f424a011527388d15d5','H22index original freeze')
 foreign=json.loads((R/'research/final_report_diff/verification/result.json').read_text())['external_current_readonly_hashes']
 ck(len(foreign)==739,'N443retainedexternalprovenancecount')
 for path,sig in observed.items():ck(signature(Path(path))==sig,'final unchanged signature '+path)
 scope='Selected eleven postfreeze roots and every explicit direct local input only. External739digests retained, not rehashed. No unlisted transitive or historical integrity, mathematical replay, optimization restart or status promotion.'
 index={'schema':'N4-postfreeze-selected-integrity-v2','utc':now(),'through_audit':446,'roots':roots,'root_count':11,'direct_edge_count':len(edges),'unique_resolved_files':len(observed),'frozen_documents':selection['frozen_documents'],'external_provenance_not_rehashed':foreign,'result_path':str(target.relative_to(R)),'checker_sha256':digest(Path(__file__)),'scope':scope}
 with index_target.open('x')as f:json.dump(index,f,indent=2);f.write('\n')
 index_hash=digest(index_target)
 result={'utc':now(),'started_utc':start,'inputs':inputs,'roots':roots,'edges':edges,'checks':checks,'check_count':len(checks),'root_count':11,'direct_edge_count':len(edges),'unique_resolved_files_before_index':index['unique_resolved_files'],'errors':errors,'all_direct_edges_match':True,'frozen_documents':selection['frozen_documents'],'external_provenance_not_rehashed_count':len(foreign),'index_sha256':index_hash,'scope':scope,'peer_files_read_or_executed':False,'expensive_computation_repeated':False,'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED current selected local-byte integrity'}
 with target.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',len(inputs),'bindings',len(edges),'edges',index['unique_resolved_files'],'files','index',index_hash,'result',digest(target),'seconds',result['elapsed_seconds'])
if __name__=='__main__':main()
