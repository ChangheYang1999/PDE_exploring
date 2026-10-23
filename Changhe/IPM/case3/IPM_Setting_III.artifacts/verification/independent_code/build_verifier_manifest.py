"""Freeze verifier reproduction inputs and code; stdlib only, no solver execution."""
from pathlib import Path
import datetime, hashlib, importlib.metadata, json, platform, shlex
ROOT=Path.cwd().resolve()
assert ROOT==Path('verification')
now=datetime.datetime.now(datetime.timezone.utc)
stamp=now.strftime('%Y%m%dT%H%M%SZ')
out=Path('evidence')/('repro_manifest_'+stamp);out.mkdir()
(out/'independent_code').mkdir();(out/'inputs').mkdir()
def dump(p,d):p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def file_record(p):
 p=Path(p);p=p.relative_to(ROOT) if p.is_absolute() else p
 return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size)
def command(args):
 assert args[0].startswith('independent_code/')
 return 'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 '+shlex.join([str(out/args[0]),*args[1:]])
code=[]
for p in sorted(Path('independent_code').glob('*.py')):
 dest=out/p;dest.write_bytes(p.read_bytes());code.append(file_record(dest))
# Recover the actual shell-runner commands. They are historical observations, not reconstructions.
history=[]
for p in sorted(Path('runs').glob('*campaign*.log')):
 for lineno,line in enumerate(p.read_text().splitlines(),1):
  try:d=json.loads(line)
  except (ValueError,TypeError):continue
  if isinstance(d,dict) and 'start' in d and 'args' in d:
   history.append(dict(log=str(p),line=lineno,**d))
provenance={}
for p in [*Path('evidence').glob('q_snapshots*/manifest.json'),*Path('evidence/published_snapshots').glob('*.json')]:
 try:d=json.loads(p.read_text())
 except (ValueError,UnicodeDecodeError):continue
 for row in d if isinstance(d,list) else [d]:
  if isinstance(row,dict) and row.get('sha256'):
   provenance[row['sha256']]=dict(manifest=file_record(p),record=row)
allstates=json.loads(Path('evidence/q_exact_jets/ALL_STATES.json').read_text())
qstates=[];selected=[];rawmaps=[]
for i,row in enumerate(allstates['rows'],1):
 meta=row['metadata'];p=Path(meta['source']);p=p.relative_to(ROOT)
 f=file_record(p);assert f['sha256']==meta['sha256']
 identity=('Q%02d_'%i)+(p.parent.name if p.name=='snapshot.npz' else p.stem)
 inp=out/'inputs'/(identity+'.json');dump(inp,[str(p)])
 args=['independent_code/audit_q_exact_jets.py','--paths-file',str(inp),'--out',str(out/'reruns'/identity/'exact')]
 state=dict(id=identity,kind='Q finite coefficient formula',file=f,parameters=meta,exact_command=command(args),exact_reference='evidence/q_exact_jets/ALL_STATES.json',diagnostics=[],historical_commands=[])
 state['provenance']=provenance.get(f['sha256'])
 if p.name=='snapshot.npz':
  q2=json.loads((p.parent/'q2.json').read_text());raw=file_record(q2['metadata']['source']);assert raw['sha256']==q2['metadata']['sha256']
  state['original_archive']=raw;state['original_archive_provenance']=provenance.get(raw['sha256'])
  rawmaps.append(dict(raw=raw,converted=f));selected.append(raw['sha256'])
 qstates.append(state);selected.append(f['sha256'])
# Own solver states are explicit frozen coefficient files. Their independent diagnostic is primary.
smooth=[]
for prefix in ['fixed','common1000']:
 for n,m in [(20,16),(24,20),(28,24)]:
  tag=f'{prefix}_cl2.5_N{n}M{m}';base=Path('evidence/smooth_solver')/tag
  f=file_record(base/'final.npz');meta=json.loads((base/'metadata.json').read_text())
  args=['independent_code/audit_complementary_charts.py',f['path'],'--kind','smooth','--tag','repro_'+stamp+'_'+tag,'--points-file','evidence/smooth_dense_points.json']
  state=dict(id=tag,kind='verifier SmoothBasis formula',file=f,metadata=file_record(base/'metadata.json'),result=file_record(base/'result.json'),parameters=meta['arguments'],independent_grid=file_record('evidence/smooth_dense_points.json'),independent_command=command(args),diagnostics=[],historical_commands=[])
  smooth.append(state);selected.append(f['sha256'])
states=qstates+smooth
lookup={}
for state in states:
 lookup[state['file']['sha256']]=state
 if state.get('original_archive'):lookup[state['original_archive']['sha256']]=state
# Snapshot diagnostics and all coordinates that determine pointwise reruns.
patterns=['q_evaluations/*/q*.json','q_evaluations/*/axis_q*.json','complementary_charts/*/diagnostic.json','complementary_mp/*/diagnostic.json','q_residual_grid/*/diagnostic.json','q_weighted/*/diagnostic.json','q_local_refinement/*/diagnostic.json','smooth_far_field/*/*.json','q_far_precision/*/*.json']
seen=set()
for pattern in patterns:
 for p in sorted(Path('evidence').glob(pattern)):
  if p in seen:continue
  seen.add(p)
  try:d=json.loads(p.read_text())
  except (ValueError,UnicodeDecodeError):continue
  if not isinstance(d,dict):continue
  h=d.get('sha256',d.get('metadata',{}).get('sha256'))
  if h not in lookup:continue
  state=lookup[h];record=file_record(p);record['started_utc']=d.get('started_utc');record['finished_utc']=d.get('finished_utc')
  # FD reproduction uses the recorded physical points, so changes to default grids cannot change it.
  if p.parent.parent.name=='q_evaluations' and d.get('points'):
   inp=out/'inputs'/(p.parent.name+'_'+p.stem+'_points.json');dump(inp,[[z['x'],z['y']] for z in d['points']])
   level=int(p.stem[-1]);src=state.get('original_archive',state['file'])['path']
   args=['independent_code/evaluate_q_state.py',src,'--level',str(level),'--tag','repro_'+stamp+'_'+p.parent.name,'--points-file',str(inp)]
   if d.get('log_radius_exterior',False):args+=['--log-tail']
   record['reproduction_command']=command(args);record['points_input']=file_record(inp)
  state['diagnostics'].append(record)
for state in states:
 paths={state['file']['path']}
 if state.get('original_archive'):paths.add(state['original_archive']['path'])
 for h in history:
  args=h['args'];matched=any(a in args or str(ROOT/a) in args for a in paths)
  # Diagnostic tags identify runs whose input was passed through a lineage file.
  if not matched and '--tag' in args:
   tag=args[args.index('--tag')+1];matched=any(Path(d['path']).parent.name==tag for d in state['diagnostics']) or tag==state['id']
  if matched:
   copied=dict(h);copied['current_frozen_code_command']=command(args);state['historical_commands'].append(copied)
versions={'python':platform.python_version(),'platform':platform.platform()}
for pkg in ['numpy','scipy','sympy','mpmath','torch']:
 try:versions[pkg]=importlib.metadata.version(pkg)
 except importlib.metadata.PackageNotFoundError:versions[pkg]='not installed'
manifest=dict(utc=now.isoformat(),root=str(ROOT),directory=str(out),scope='Frozen verifier inputs and independent evaluations. No exact or nearby profile is asserted.',software_versions=versions,thread_environment={'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'},code_snapshot=code,states=states,raw_to_converted=rawmaps,exact_source=file_record('evidence/q_exact_jets/ALL_STATES.json'),limitations=['Historical solver/evaluator source hashes were not recorded at every execution. The code directory here is the actual current snapshot, not a claimed historical version.','Some saved drift iterates were copied from producer runs before publication to artifacts; their copy provenance is retained. Producer code is neither copied nor used by these independent checks.','The four first exact-audit inputs are compressed numeric conversions. Their original archives and separate hashes are listed. Byte hashes differ by format; coefficient equivalence is checked separately.','Optimizer replay is not promised bitwise. Explicit coefficients, physical diagnostic grids, commands and current source are retained.','The current active campaign log may grow. Historical log paths and line numbers locate commands; a full command record is also embedded here.','Sample maxima, precision comparisons and exact finite-state jets do not prove a uniform continuum residual or existence.'])
dump(out/'MANIFEST.json',manifest)
md=['# Verifier reproducibility manifest','',f'Frozen {now.isoformat()}. All paths are relative to `{ROOT}` unless absolute. JSON: `{out}/MANIFEST.json`. Current verifier source is frozen under `{out}/independent_code/`. Run commands from the lane root, serially; do not run them alongside another heavy CPU process.','', 'This manifest covers all 14 exact Q audits, their four original drift archives, the original N20/N24/N28 verifier states, and the three common-ceiling controls. The coefficient hashes were recomputed when writing this file. Canonical velocities and residuals use verifier code only.','', 'Software: '+', '.join(k+'='+v for k,v in versions.items())+'.','', '| id | coefficient file | full SHA-256 |','|---|---|---|']
for s in states:
 md.append(f"| {s['id']} | `{s['file']['path']}` | `{s['file']['sha256']}` |")
 if s.get('original_archive'):md.append(f"| {s['id']} original archive | `{s['original_archive']['path']}` | `{s['original_archive']['sha256']}` |")
for s in states:
 md+=['',f"## {s['id']}",'',s.get('exact_command',s.get('independent_command')),'',f"Diagnostics: {len(s['diagnostics'])}. Actual historical command records: {len(s['historical_commands'])}. Full hashes and dates are in JSON."]
 for d in s['diagnostics']:
  md.append('- `'+d['path']+'`')
  if d.get('reproduction_command'):md.append('  Command: `'+d['reproduction_command']+'`')
 # All non-FD reproduction commands are also explicit here, deduplicated.
 cmds=[]
 for h in s['historical_commands']:
  c=h['current_frozen_code_command']
  if c not in cmds:cmds.append(c)
 if cmds:
  md+=['','Recorded commands using this frozen source snapshot (historical originals and log line numbers are in JSON):','']
  md+=['- `'+c+'`' for c in cmds]
md+=['','## Limits','']+['- '+x for x in manifest['limitations']]
md+=['','Exact replay prerequisites: the existing proof-gate files under `research/*/verification/` are needed by some checkers. Source code contains their explicit paths. No Lean build is required. The current code snapshot, JSON inputs, retained coefficient files, and listed diagnostics are sufficient for the numerical verifier; all paths lie in this lane.']
(out/'MANIFEST.md').write_text('\n'.join(md)+'\n')
Path('evidence/MANIFEST.md').write_text('\n'.join(md)+'\n')
Path('evidence/MANIFEST.json').write_text(json.dumps({'latest':str(out/'MANIFEST.json'),'utc':now.isoformat()},indent=2)+'\n')
print(json.dumps({'directory':str(out),'states':len(states),'source_files':len(code),'raw_pairs':len(rawmaps),'diagnostics':sum(len(s['diagnostics']) for s in states),'historical_commands':sum(len(s['historical_commands']) for s in states)},indent=2))
