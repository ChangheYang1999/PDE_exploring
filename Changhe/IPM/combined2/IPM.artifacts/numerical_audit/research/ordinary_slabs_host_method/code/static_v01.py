"""Finite preparation checks. This never executes the numerical worker or guard."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import ast,difflib,json,os,time
R=Path.cwd().resolve();B=R/'research/ordinary_slabs_host_method';V=B/'verification'
assert R.name=='numerical_audit' and os.sched_getaffinity(0)=={50} and os.getpriority(os.PRIO_PROCESS,0)>=19
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=0

def ck(v,why):
 global checks
 checks+=1;assert v,why

def h(p):
 z=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):z.update(b)
 return z.hexdigest()
old=R/'research/background_slabs_independent/code/check_v01.py';new=B/'code/check_v01.py'
ck(h(old)=='f854bde5cd06f942d632c98941ab96637d1adfd1eac4c08b388eb1e14ed27c23','admitted old numerical worker')
text=old.read_text();replacements=[
 ('interval-Horner capped-slab audit','interval-Horner ordinary-slab host audit'),
 ('B=Path(__file__).resolve().parents[1];R=B.parents[1]','B=Path(__file__).resolve().parents[1];R=Path.cwd().resolve();CAM=R.parent'),
 ('assert JS == list(range(126,106,-1))+[105,103,101,99]','assert JS == list(range(97,55,-1)) and R.name=="numerics_agent_2"'),
 ('os.sched_getaffinity(0)=={50}','os.sched_getaffinity(0)=={49}'),
 ("SOURCE=R/'research/source013_background_source/verification/observed_owner_v02/polynomials.json.gz'","SOURCE=CAM/'numerics_agent_1/research/source013_background_source/worker_background_v02/research/source013_background_source/verification/source_v01/polynomials.json.gz'"),
 ("COVER=R/'research/source013_background_cover/verification/manifest_v01.json'","COVER=CAM/'numerical_audit/research/source013_background_cover/verification/manifest_v01.json'"),
 ('str(p.relative_to(R)):digest(p)','str(p.relative_to(CAM)):digest(p)'),
 ('base>0 and abs(g)*rho<1 and abs(g)<1','base>0 and abs(g)*rho<1'),
 ('SOURCE.relative_to(R)','SOURCE.relative_to(CAM)'),
 ('digest(R/n)==q','digest(CAM/n)==q'),
 ('specified capped slabs','specified ordinary slabs')]
for a,b in replacements:ck(text.count(a)==1,'unique declared replacement '+a);text=text.replace(a,b)
ck(text==new.read_text(),'no undeclared numerical worker changes')
old_recount=(R/'research/background_slabs_independent/code/recount_v01.py').read_text().split('source=loadz(source_path)',1)[1]
new_recount=(B/'code/recount_v01.py').read_text().split('source=loadz(source_path)',1)[1]
old_recount=old_recount.replace('str(p.relative_to(R))','str(p.relative_to(CAM))').replace('h(R/n)==z','h(CAM/n)==z').replace("with(D/'recount_v01.json').open('x')as f:","with OUT.open('x')as f:")
ck(old_recount==new_recount,'exact rational recount arithmetic unchanged')
files={}
for path in sorted((B/'code').glob('*.py')):
 tree=ast.parse(path.read_text());ck(isinstance(tree,ast.Module),'Python syntax '+path.name)
 files[str(path.relative_to(R))]=h(path)
 for node in ast.walk(tree):
  if isinstance(node,ast.Import):ck(not any(n.name.split('.')[0] in ['socket','http','flask','uvicorn'] for n in node.names),'no server import')
  if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and node.func.attr=='killpg':ck(ast.unparse(node.args[0])=='child.pid','only freshly created child group may be signalled')
 ck(not any(s in path.read_text() for s in ['/'+n+'/' for n in ('mnt','home','efs','tmp')]),'published paths relative')
worker_tree=ast.parse(new.read_text())
assignments=[node for node in ast.walk(worker_tree) if isinstance(node,ast.Assign) and any(isinstance(n,ast.Name) and n.id=='CAM' for n in node.targets)]
ck(len(assignments)==1,'campaign path variable not overwritten by matrix compilation')
geometry=R/'research/ordinary_slabs_host_plan/verification/geometry_v01.json'
ck(h(geometry)=='4f90c5e4e9c018b3c5765b0de61f8e1085ad281d08fd2eae51d57bdff45429da','prior complete branch and ordinary-slab geometry')
files[str(geometry.relative_to(R))]=h(geometry)
for path in [old,R/'research/background_slabs_independent/code/recount_v01.py',B/'PROOF.md',B/'METHOD.md',B/'README.md',B/'formal/README.md']:files[str(path.relative_to(R))]=h(path)
diff=''.join(difflib.unified_diff(old.read_text().splitlines(True),new.read_text().splitlines(True),fromfile='admitted_capped_worker',tofile='proposed_ordinary_host_worker'))
with (V/'source_transform_v01.diff').open('x')as f:f.write(diff)
report=dict(status='PASS_PREPARATION_ONLY',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,checks=checks,files=files,source_changes=[a for a,b in replacements],scope='Syntax, exact code transformation and protocol source checks. No guard, installer, numerical source worker or recount was executed; independent review and concrete allocation remain required.')
with (V/'static_v01.json').open('x')as f:json.dump(report,f,indent=2);f.write('\n')
print(report['status'],checks,report['elapsed_seconds'],h(V/'static_v01.json'),flush=True)
