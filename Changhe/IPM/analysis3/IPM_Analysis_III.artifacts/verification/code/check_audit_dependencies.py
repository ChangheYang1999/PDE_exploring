"""Read-only checks of explicit paths in final audit records. No proof execution."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,time
ROOT=Path(__file__).resolve().parents[1]
START=datetime.now(timezone.utc).isoformat();tick=time.monotonic()
HASH=re.compile(r'^[a-f0-9]{64}$')
cache={}
def sha(p):
 p=p.resolve()
 if p not in cache: cache[p]=hashlib.sha256(p.read_bytes()).hexdigest()
 return cache[p]
def relative(p):
 try:return str(p.relative_to(ROOT))
 except ValueError:return str(p)
def resolve(k):
 p=Path(k)
 if p.is_absolute(): return p
 for p in [ROOT/k,ROOT/'proofs'/k]:
  if p.is_file(): return p
  if p.is_dir() and (p/'PROOF.md').is_file():return p/'PROOF.md'
 return ROOT/k
checks=[];manifest_records=[]
def check(record,key,p,expected):
 actual=sha(p) if p.is_file() else None
 checks.append({'record':relative(record),'key':key,'path':relative(p),'expected':expected,'actual':actual,'matches':actual==expected})
proof_dirs=[]
for d in sorted((ROOT/'proofs').iterdir()):
 if not d.is_dir() or not re.match(r'^\d+_',d.name):continue
 proof=d/'PROOF.md'
 proof_dirs.append({'topic':d.name,'proof_exists':proof.is_file(),'proof_sha256':sha(proof) if proof.is_file() else None,
  'binding_sidecars':[p.name for p in sorted(d.glob('*.md')) if 'CLARIFICATION' in p.name or p.name in ['AUDIT_SCOPE.md','AUDIT_ADOPTION.md']]})
 for name in ['audit_record.json','final_audit.json','derivation.json']:
  rp=d/'evidence'/name
  if not rp.is_file():continue
  j=json.loads(rp.read_text());manifest_records.append({'path':relative(rp),'sha256':sha(rp)})
  if HASH.fullmatch(str(j.get('proof_sha256',''))):check(rp,'proof_sha256',proof,j['proof_sha256'])
  if HASH.fullmatch(str(j.get('clarifications_sha256',''))):check(rp,'clarifications_sha256',d/'AUDIT_CLARIFICATIONS.md',j['clarifications_sha256'])
  if j.get('audit_file') and HASH.fullmatch(str(j.get('audit_sha256',''))):check(rp,'audit_sha256',resolve(j['audit_file']),j['audit_sha256'])
  for key in ['files','dependencies','extra_dependencies','additional_dependencies']:
   ds=j.get(key,{})
   if not isinstance(ds,dict):continue
   for k,h in ds.items():
    if isinstance(k,str) and isinstance(h,str) and HASH.fullmatch(h):check(rp,key+':'+k,resolve(k),h)
links=[]
for rp in [ROOT/'FINAL_VERIFICATION.md',ROOT/'THEOREM_MAP.md',ROOT/'proofs/INDEX.md']:
 for target in re.findall(r'\]\(([^)]+)\)',rp.read_text()):
  if ':' in target or target.startswith('#'):continue
  p=(rp.parent/target.split('#')[0]).resolve()
  links.append({'record':relative(rp),'target':target,'exists':p.exists()})
failures=[x for x in checks if not x['matches']]
ans={'started_utc':START,'finished_utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tick,
 'method':'Check present final_audit.json, audit_record.json and derivation.json records only. Explicit typed path hashes and current proof/clarification hashes. This does not rerun computations, parse every historical hash in prose, or establish mathematical truth.',
 'script_sha256':sha(Path(__file__)),'counts':{'proof_topics':len(proof_dirs),'audit_manifests':len(manifest_records),'hash_relations':len(checks),'mismatches':len(failures),'handoff_links':len(links),'missing_links':sum(not x['exists'] for x in links)},
 'proofs':proof_dirs,'audit_manifests':manifest_records,'checks':checks,'failures':failures,'links':links}
out=ROOT/'certificates/audit_dependency_identity.json';out.write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({'date':ans['finished_utc'],'counts':ans['counts'],'failures':failures,'missing_links':[x for x in links if not x['exists']],'output_sha256':sha(out),'seconds':ans['seconds']},indent=2))
