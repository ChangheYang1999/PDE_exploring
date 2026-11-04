"""Read-only external receipt admission and independent source/table identity."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,importlib.util,json,math,os,sys,time
from flint import ctx
import identity_v01,plans_v01
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/source013_admission'
MANIFEST='9c7c123275176f3a48596aaaf69c6d0c2ea61ecdf128cc10dcfed8e07809cb57'
REVIEW='39fe6b29a2c6689e352efa3a45658eab045f6ba61837a756145d7cd54711cdcc'
DEADLINE=datetime(2026,11,4,17,5,30,tzinfo=timezone.utc).timestamp();CUTOFF=DEADLINE-30
RUN_BINDING={}
sys.set_int_max_str_digits(0)
def digest(path):
 h=sha256()
 with path.open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
def put(p,d):
 with p.open('x')as f:json.dump(d,f,indent=2);f.write('\n')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='microseconds').replace('+00:00','Z')
def moment(text):
 assert isinstance(text,str) and text.endswith('Z')
 d=datetime.fromisoformat(text.replace('Z','+00:00'));assert d.tzinfo is not None
 return d.timestamp()
def local(name):
 p=Path(name);assert not p.is_absolute() and '..'not in p.parts
 return ROOT/p
def own(name,path):
 s=importlib.util.spec_from_file_location(name,local(path));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def validate_receipts(m,j,installation,execution,result,result_hash):
 for r in [installation,execution,result]:
  assert r['job']==j['id'] and r['owner']==j['owner'] and r['cpu']==j['cpu']
  assert r['manifest_sha256']==MANIFEST
 assert installation['review_sha256']==execution['review_sha256']==REVIEW
 assert installation['worker_root']=='research/source013_startup/worker_'+j['id']
 assert execution['schema']=='source013-startup-execution-v1' and execution['status']=='COMPLETED'
 assert execution['exit_code']==0 and execution['stop_reason']is None and execution['result_sha256']==result_hash
 assert execution['guard_sha256']==m['files']['research/source013_startup/code/guard_v01.py']
 assert result['schema']=='source013-startup-result-v1' and result['status']=='COMPLETED' and result['role']==j['role']
 assert result['source']==m['source'] and result['precision_bits']==1024
 identity=result['center'];assert identity['fields_sha256']==m['source']['fields_sha256'] and identity['fixed_c_exact']==m['source']['fixed_c_exact']
 assert identity['input_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
 assert identity['phi']['input_sha256']==m['source']['canonical_sha256']
 times=[moment(installation['installed_utc']),moment(execution['started_utc']),moment(result['started_utc']),moment(result['finished_utc']),moment(execution['finished_utc'])]
 assert times==sorted(times) and times[1]<CUTOFF and times[2]<CUTOFF and times[-1]<=DEADLINE
 for r in [execution,result]:assert math.isfinite(r['elapsed_seconds']) and r['elapsed_seconds']>=0
 for n,h in result['source_bindings'].items():assert m['files'].get(n)==h
 assert execution['initial_resources']['owner_lane_bytes']<2_950_000_000 and execution['initial_resources']['filesystem_free_bytes']>=20_000_000_000
 if j['role']=='planner':
  assert [r['parent_index']for r in result['rows']]==j['indices']
  old=ctx.prec;ctx.prec=1536
  try:
   for r in result['rows']:plans_v01.check_row(r,r['parent_index'],result['safe_structural_bandwidth'])
  finally:ctx.prec=old
 else:
  assert result['table']=='output/source013_table_v01.json.zst' and len(result['table_sha256'])==64
  assert result['statistics']['exact_reverse_accumulation_passed']is True
 return times

def admit(job):
 start,tick=stamp(),time.monotonic();mf=local('research/source013_startup/verification/manifest_v01.json');rf=local('research/source013_startup/verification/external_review_v01.json')
 assert digest(mf)==MANIFEST and digest(rf)==REVIEW;m=read(mf);review=read(rf)
 assert review['status']=='BOUND' and review['manifest_sha256']==MANIFEST
 jobs=[j for j in m['jobs']if j['id']==job];assert len(jobs)==1;j=jobs[0]
 assert j['owner']in ['numerics_agent_1','numerics_agent_2'];remote=ROOT.parent/j['owner']/'research/source013_startup'/('worker_'+job)
 assert remote.resolve()==remote
 for n,h in m['files'].items():
  assert digest(local(n))==h and digest(remote/n)==h,n
  if n in m['copied_code']:assert not(remote/n).is_symlink() and (remote/n).resolve().is_relative_to(remote)
 assert digest(remote/'manifest.json')==MANIFEST and digest(remote/'review.json')==REVIEW
 installation=read(remote/'installation.json');execution=read(remote/'execution_v01.json');result=read(remote/'output/result.json');result_hash=digest(remote/'output/result.json')
 validate_receipts(m,j,installation,execution,result,result_hash)
 folder=BASE/'verification'/(job+'_v01');folder.mkdir(exist_ok=False)
 bindings={};copied={}
 for n in ['installation.json','execution_v01.json','output/result.json']:
  p=remote/n;name=n.replace('/','_');data=p.read_bytes();assert sha256(data).hexdigest()==digest(p)
  (folder/name).write_bytes(data);bindings['../'+str(p.relative_to(ROOT.parent))]=digest(p);copied[name]=digest(folder/name)
 evidence=None
 if j['role']=='table':
  archive=remote/result['table'];assert digest(archive)==result['table_sha256']
  loader=own('admission_storage','storage/code/load.py');document=loader.read_json_zst(archive,result['table_sha256'])
  assert document['source']==m['source'] and document['center']==result['center'] and document['manifest_sha256']==MANIFEST and document['files']==m['files']
  for k,v in result['statistics'].items():assert document[k]==v,k
  ctx.prec=1024;source=own('admission_fresh_source','research/matched_circle_audit/code/check_v01.py');fields,_,_,identity,source_bindings=source.source()
  assert identity==result['center'] and source_bindings==result['source_bindings']
  groups=source.region.radial.legacy_groups(fields)
  evidence=identity_v01.verify(groups,document)
  assert digest(archive)==result['table_sha256']
  link=folder/'source013_table_v01.json.zst';link.symlink_to(os.path.relpath(archive,folder))
  bindings['../'+str(archive.relative_to(ROOT.parent))]=result['table_sha256']
 receipt={'status':'ADMITTED_PREPARATION','job':job,'started_utc':start,'finished_utc':stamp(),'elapsed_seconds':time.monotonic()-tick,'source':m['source'],'manifest_sha256':MANIFEST,'review_sha256':REVIEW,'external_bindings':bindings,'copied_records':copied,'identity_evidence':evidence,'code_sha256':digest(Path(__file__)),'identity_code_sha256':digest(BASE/'code/identity_v01.py'),'plans_code_sha256':digest(BASE/'code/plans_v01.py'),'proof_sha256':digest(BASE/'PROOF.md'),'admission_binding':RUN_BINDING,'scope':'One complete preparation record admitted. No primary or norm certificate.'}
 assert time.time()<=DEADLINE;put(folder/'receipt.json',receipt);print(receipt['status'],job,receipt['elapsed_seconds'],flush=True)

def combine():
 rows=[];receipts=[]
 for job in ['planner_a','planner_b','table']:
  folder=BASE/'verification'/(job+'_v01');receipt=read(folder/'receipt.json')
  assert receipt['status']=='ADMITTED_PREPARATION' and receipt['job']==job and receipt['manifest_sha256']==MANIFEST and receipt['review_sha256']==REVIEW
  assert receipt['code_sha256']==digest(Path(__file__)) and receipt['identity_code_sha256']==digest(BASE/'code/identity_v01.py') and receipt['plans_code_sha256']==digest(BASE/'code/plans_v01.py') and receipt['proof_sha256']==digest(BASE/'PROOF.md')
  for n,h in receipt['copied_records'].items():assert digest(folder/n)==h
  rows.append(read(folder/'output_result.json'));receipts.append({'path':str((folder/'receipt.json').relative_to(ROOT)),'sha256':digest(folder/'receipt.json')})
 assert rows[0]['source']==rows[1]['source']==rows[2]['source'] and rows[0]['center']==rows[1]['center']==rows[2]['center']
 assert read(BASE/'verification/table_v01/receipt.json')['identity_evidence']['exact_equality']is True
 assembled=plans_v01.verify(rows[0],rows[1]);config=read(local('research/source013_startup/data/policy_v01.json'))
 request={k:config[k]for k in ['structure_tag','input','input_sha256','phi','sigma_exact','r0_exact','source']}
 request.update(kind='annulus',order=48,panels=assembled['panels'],created_utc=stamp(),startup_admissions=receipts,compact_table='research/source013_admission/verification/table_v01/source013_table_v01.json.zst',compact_table_sha256=rows[2]['table_sha256'],majorant_method='containing polynomial shift',status='PREPARED; separately bound primary deployment required')
 assert digest(local(request['compact_table']))==request['compact_table_sha256']
 folder=BASE/'verification/combined_v01';folder.mkdir(exist_ok=False);put(folder/'request.json',request)
 put(folder/'result.json',{'status':'ADMITTED_PREPARATION','source':request['source'],'request_sha256':digest(folder/'request.json'),'startup_admissions':receipts,**assembled,'admission_binding':RUN_BINDING,'scope':'Exact source013 preparation admitted. No energies, global norms, background or closure.'})
 assert time.time()<=DEADLINE

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--job',choices=['planner_a','planner_b','table','combine'],required=True);ap.add_argument('--manifest-sha256',required=True);ap.add_argument('--review-sha256',required=True);a=ap.parse_args()
 assert sorted(os.sched_getaffinity(0))==[50] and os.getpriority(os.PRIO_PROCESS,0)>=19 and time.time()<CUTOFF
 assert sys.version_info[:3]==(3,12,13) and all(os.environ.get(k)=='1'for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
 mf=BASE/'verification/manifest_v01.json';rf=BASE/'verification/external_review_v01.json'
 assert digest(mf)==a.manifest_sha256 and digest(rf)==a.review_sha256
 manifest,review=read(mf),read(rf);assert review['status']=='BOUND' and review['manifest_sha256']==a.manifest_sha256
 for n,h in manifest['files'].items():assert digest(local(n))==h,n
 RUN_BINDING.update(manifest_sha256=a.manifest_sha256,review_sha256=a.review_sha256)
 if a.job=='combine':combine()
 else:admit(a.job)
if __name__=='__main__':main()
