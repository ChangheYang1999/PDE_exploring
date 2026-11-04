"""Finite, hash-bound protocol for the proposed numerics_agent_2 ordinary-slab host.
No installation or execution occurs at import. All paths are explicit.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, os, shutil

ROOTS=list(range(97,55,-1))
SOURCE='numerics_agent_1/research/source013_background_source/worker_background_v02/research/source013_background_source/verification/source_v01/polynomials.json.gz'
SOURCE_SHA='2e3c649402c72ad50836f41f35c5657f50232a877557a5641038262355fa689d'
COVER='numerical_audit/research/source013_background_cover/verification/manifest_v01.json'
METHOD='source_host_049/method_v01'
OUTPUT='source_host_049/ordinary_v01'
REQUIRED_EVIDENCE={'allocation','producer_manifest','producer_review','method_review','n4_execution','n4_result','n4_installation'}

def stamp():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
def moment(s):
 t=datetime.fromisoformat(s.replace('Z','+00:00'))
 assert t.tzinfo is not None and t.utcoffset().total_seconds()==0
 return t

def digest(p):
 h=sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()

def read(p):return json.loads(p.read_text())
def save(p,obj):
 with p.open('x') as f:
  json.dump(obj,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())

def named(base,name):
 p=Path(name)
 assert type(name)is str and not p.is_absolute() and '..' not in p.parts and str(p)==name
 q=base/p;assert q.resolve().is_relative_to(base.resolve())
 return q

def environment(cpu):
 assert os.sched_getaffinity(0)=={cpu} and os.getpriority(os.PRIO_PROCESS,0)>=19
 assert all(os.environ.get(n)=='1' for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'))

def usage(root):
 logical=allocated=0
 for folder,dirs,files in os.walk(root,followlinks=False):
  dirs[:]=[d for d in dirs if not (Path(folder)/d).is_symlink()]
  for name in files:
   p=Path(folder)/name
   if p.is_symlink():continue
   try:s=p.stat()
   except FileNotFoundError:continue
   logical+=s.st_size;allocated+=s.st_blocks*512
 return {'logical_bytes':logical,'allocated_bytes':allocated,'lane_bytes':max(logical,allocated),'filesystem_free_bytes':shutil.disk_usage(root).free}

def processes(root,excluded=()):
 """Observe, never signal. Other host cores are not conflicts."""
 conflicts=[];rss=0;own=[]
 for d in Path('/proc').iterdir():
  if not d.name.isdigit():continue
  pid=int(d.name)
  try:
   state=(d/'stat').read_text().rsplit(')',1)[1].split()[0]
   if state=='Z':continue
   affinity=os.sched_getaffinity(pid)
   argv=(d/'cmdline').read_bytes().split(b'\0')
   cwd=(d/'cwd').resolve()
   host_process=cwd==root or cwd.is_relative_to(root)
   if host_process:
    rss+=int((d/'statm').read_text().split()[1])*os.sysconf('SC_PAGE_SIZE');own.append(pid)
   if pid not in excluded and affinity=={49} and argv and b'python' in argv[0]:
    conflicts.append({'pid':pid,'own_lane':host_process,'affinity':[49]})
  except (FileNotFoundError,ProcessLookupError,PermissionError,IndexError):pass
 return {'conflicts':conflicts,'host_rss_bytes':rss,'host_pids':own}

def add_arguments(parser):
 for n in ('request','request-sha256','review','review-sha256','adoption','adoption-sha256'):
  parser.add_argument('--'+n,required=True)

def authenticate(campaign,args):
 """Hash all named inputs and check concrete request and review contracts."""
 qpath=named(campaign,args.request);vpath=named(campaign,args.review);apath=named(campaign,args.adoption)
 assert qpath.parts[len(campaign.parts)]=='numerical_audit'
 assert vpath.parts[len(campaign.parts)]=='theory_audit'
 assert apath.parts[len(campaign.parts)]=='numerical_audit'
 assert digest(qpath)==args.request_sha256 and digest(vpath)==args.review_sha256 and digest(apath)==args.adoption_sha256
 q,v,ad=map(read,(qpath,vpath,apath))
 assert q['schema']=='an-independent-ordinary-slab-host-request-v1'
 assert v['status']==ad['status']=='BOUND'
 assert v['request_sha256']==ad['request_sha256']==args.request_sha256
 assert ad['review_sha256']==args.review_sha256
 assert q['owner']=='numerics_agent_2' and q['cpu']==49 and q['nice']==19 and q['threads']==1
 assert q['roots']==ROOTS and q['method_directory']==METHOD and q['output']==OUTPUT
 assert q['limit_seconds']==7200 and q['min_start_reserve_bytes']==650000000
 assert q['lane_cap_bytes']==3000000000 and q['stop_lane_bytes']==2900000000
 assert q['min_filesystem_free_bytes']==20000000000 and q['max_host_rss_bytes']==30000000000
 assert q['no_new_after']=='2026-11-04T12:00:00Z' and q['stop_at']=='2026-11-04T14:50:00Z'
 assert moment(q['created_utc'])<=moment(v['received_utc'])<=moment(ad['received_utc'])
 mp=named(campaign,q['method_manifest']);assert digest(mp)==q['method_manifest_sha256']
 m=read(mp)
 assert m['schema']=='an-independent-ordinary-slab-host-method-v1'
 assert v['manifest_sha256']==ad['manifest_sha256']==q['method_manifest_sha256']
 assert m['owner']=='numerics_agent_2' and m['cpu']==49 and m['roots']==ROOTS
 assert m['source']==SOURCE and m['source_sha256']==SOURCE_SHA and m['cover']==COVER
 assert m['host_method_directory']==METHOD and m['script']=='code/check_v01.py'
 method_source=named(campaign,m['source_directory'])
 assert m['source_directory']=='numerical_audit/research/ordinary_slabs_host_method'
 bindings={args.request:args.request_sha256,args.review:args.review_sha256,args.adoption:args.adoption_sha256,q['method_manifest']:q['method_manifest_sha256']}
 for name,h in m['files'].items():
  path=named(method_source,name);assert digest(path)==h
  bindings[str(path.relative_to(campaign))]=h
 for name,h in m['external_files'].items():
  assert digest(named(campaign,name))==h;bindings[name]=h
 assert m['external_files'][SOURCE]==SOURCE_SHA
 assert m['external_files'][COVER]==m['cover_sha256']
 assert set(q['evidence'])==REQUIRED_EVIDENCE
 for role,item in q['evidence'].items():
  path=named(campaign,item['path']);assert digest(path)==item['sha256']
  bindings[item['path']]=item['sha256']
 assert q['evidence']['allocation']['path'].startswith('coordinator/')
 assert q['evidence']['producer_manifest']['path'].startswith('theory_agent_1/')
 assert q['evidence']['producer_review']['path'].startswith('theory_audit/')
 assert q['evidence']['method_review']['path'].startswith('theory_audit/')
 method_review=read(named(campaign,q['evidence']['method_review']['path']))
 assert method_review['status']=='BOUND' and method_review['manifest_sha256']==q['method_manifest_sha256']
 assert moment(m['created_utc'])<=moment(method_review['received_utc'])<=moment(q['created_utc'])
 # Producer admission is a separate BOUND record, not a claim inferred from stdout.
 producer_review=read(named(campaign,q['evidence']['producer_review']['path']))
 assert producer_review['status']=='BOUND'
 assert producer_review['producer_manifest_sha256']==q['evidence']['producer_manifest']['sha256']
 assert producer_review['required_roots']==ROOTS
 assert moment(producer_review['received_utc'])<=moment(q['created_utc'])
 ne=read(named(campaign,q['evidence']['n4_execution']['path']))
 ni=read(named(campaign,q['evidence']['n4_installation']['path']))
 assert ni['job']=='n4' and ni['owner']=='numerics_agent_2' and ni['cpu']==49
 assert ni['manifest_sha256']==ne['manifest_sha256'] and ni['review_sha256']==ne['review_sha256']
 assert moment(ni['installed_utc'])<=moment(ne['started_utc'])
 nr=read(named(campaign,q['evidence']['n4_result']['path']))
 assert ne['schema']=='source013-near-cover-deployment-execution-v1'
 assert ne['status']=='COMPLETED' and ne['exit_code']==0 and ne['stop_reason']is None
 assert ne['job']=='n4' and ne['owner']=='numerics_agent_2' and ne['cpu']==49
 assert ne['result_sha256']==q['evidence']['n4_result']['sha256']
 assert nr['status']=='COMPLETED' and nr['job']=='n4' and nr['cpu']==49
 assert nr['complete_requested_assignment']is True and len(nr['panels'])==112
 assert [p['index'] for p in nr['panels']]==list(range(4,561,5))
 assert moment(ne['finished_utc'])<=moment(q['created_utc'])
 assert q['evidence']['n4_execution']['path']=='numerics_agent_2/research/source013_near_cover/worker_n4/execution_v01.json'
 assert q['evidence']['n4_installation']['path']=='numerics_agent_2/research/source013_near_cover/worker_n4/installation.json'
 assert q['evidence']['n4_result']['path']=='numerics_agent_2/research/source013_near_cover/worker_n4/output/result.json'
 for name,h in q['producer_files'].items():
  assert name.startswith('theory_agent_1/') and digest(named(campaign,name))==h
  bindings[name]=h
 assert q['producer_files'] and q['evidence']['producer_manifest']['path'] in q['producer_files']
 return q,m,bindings

def recheck(campaign,bindings):return all(digest(named(campaign,n))==h for n,h in bindings.items())
