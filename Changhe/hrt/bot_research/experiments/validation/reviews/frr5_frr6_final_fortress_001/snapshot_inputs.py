"""Read and archive exact bytes. No imports from the project under review."""
import ast, gzip, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
OUT=Path('bot_research/experiments/validation/reviews/frr5_frr6_final_fortress_001')
label=sys.argv[1]
UTC=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda b:hashlib.sha256(b).hexdigest()
m={'schema':1,'snapshot_label':label,'started_utc':UTC(),'reviewer_model':'GPT-6 Astra',
   'execution':'stdlib byte reads, compression, JSON and AST parsing only; no project imports or execution',
   'files':{},'absent':[],'snapshot_runs':{}}
def retain(name):
    if name in m['files']:return gzip.decompress((OUT/m['files'][name]['archive']).read_bytes())
    p=Path(name)
    if not p.is_file():
        m['absent'].append({'path':name,'observed_utc':UTC()});return None
    before=p.stat();b=p.read_bytes();after=p.stat();digest=sha(b);archive='inputs/'+digest+'.gz';q=OUT/archive
    q.parent.mkdir(exist_ok=True)
    if not q.exists():
        with q.open('xb') as f:f.write(gzip.compress(b,compresslevel=6,mtime=0))
    z=q.read_bytes()
    if gzip.decompress(z)!=b:raise ValueError('archive verification failed '+name)
    m['files'][name]={'sha256':digest,'bytes':len(b),'archive':archive,'archive_sha256':sha(z),'archive_bytes':len(z),
      'read_utc':UTC(),'source_mtime_utc':datetime.fromtimestamp(after.st_mtime,timezone.utc).isoformat(),
      'stat_stable_during_read':(before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns)}
    return b
allrows=[]
for run in ['frr3','frr4','frr5','frr6']:
    base='bot_research/runs/lead/'+run;b=retain(base+'/results.jsonl');summary=retain(base+'/summary.md')
    if b is None:rr=[]
    else:
        if b and not b.endswith(b'\n'):raise ValueError('unfinished JSON line '+run)
        rr=[json.loads(x) for x in b.splitlines() if x.strip()]
    logs=sorted(p.as_posix() for p in (Path(base)/'logs').glob('*.jsonl'))
    m['snapshot_runs'][run]={'rows':len(rr),'results_present':b is not None,'summary_present':summary is not None,'log_directory_files':logs}
    allrows.extend(rr)
    for row in rr:
        if row.get('log'):retain(row['log'])
for name in ['bot_research/runs/lead/frr1/results.jsonl','bot_research/runs/lead/frr2/results.jsonl',
             'bot_research/runs/lead/frr1/summary.md','bot_research/runs/lead/frr2/summary.md',
             'bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md',
             'bot_research/experiments/validation/analysis/frr1_equilibrium/verification/independent_audit_001.json',
             'bot_research/experiments/validation/analysis/frr1_equilibrium/verification/check_frr1_matrix.py',
             'bot_research/bots/counters/data/early_wall_guard_001.json',
             'bot_research/reports/REPORT.md','bot_research/notes/defense.md','../hrt-lead/NOTES_FOR_TEAM.md','../hrt-lead/RUN_STATUS.md',
             'bot_research/experiments/lead/rr_specs.sh','bot_research/bots/best.py','td_game/balanced.json',
             'bot_research/experiments/validation/reviews/frr4_final_fortress_001/REVIEW.md',
             'bot_research/experiments/validation/reviews/frr4_final_fortress_001/seal_001.json',
             'bot_research/experiments/validation/reviews/frr4_final_fortress_001/record_audit_001.json']:
    retain(name)
for n in ['17','19','20']:
    retain('bot_research/experiments/lead/queue_h'+n+'.sh');retain('bot_research/runs/lead/queue_h'+n+'.log')
for n in ['3','4','5','6']:retain('bot_research/runs/lead/frr'+n+'.out')
for directory,pattern in [('bot_research/harness','*.py'),('data','*.json'),('td_game','*.py'),
                          ('bot_research/bots/defense/frozen/v46','*'),('bot_research/bots/defense/frozen/v48','*')]:
    for p in sorted(Path(directory).glob(pattern)):
        if p.is_file():retain(p.as_posix())
for row in allrows:
    for name in row.get('sources',{}):retain(name)
def module_file(name):
    base=Path(*name.split('.'))
    for p in [base.with_suffix('.py'),base/'__init__.py']:
        if p.is_file():return p.as_posix()
    return None
def closure(spec):
    seen={};todo=[spec.partition(':')[0]]
    while todo:
        name=todo.pop()
        if name in seen or not name.startswith('bot_research'):continue
        p=module_file(name)
        if p is None:continue
        seen[name]=p;parts=name.split('.');todo.extend('.'.join(parts[:i]) for i in range(1,len(parts)))
        package=name if p.endswith('/__init__.py') else '.'.join(parts[:-1])
        for node in ast.walk(ast.parse(retain(p).decode())):
            if isinstance(node,ast.Import):todo.extend(a.name for a in node.names)
            elif isinstance(node,ast.ImportFrom):
                if node.level:
                    pkg=package.split('.');pkg=pkg[:len(pkg)-(node.level-1)]
                    target='.'.join(pkg+([node.module] if node.module else []))
                else:target=node.module or ''
                todo.append(target);todo.extend(target+'.'+a.name for a in node.names)
    return sorted(set(seen.values())|{p.as_posix() for p in Path('bot_research/harness').glob('*.py')})
m['current_static_versions']={}
for spec in sorted({r[k] for r in allrows for k in ['spec_a','spec_b']}):
    paths=closure(spec);h=hashlib.sha256()
    for p in paths:h.update((p+'\0'+sha(retain(p))+'\n').encode())
    m['current_static_versions'][spec]={'version':h.hexdigest(),'closure_paths':paths}
m['finished_utc']=UTC();m['archive_unique_bytes']=sum(p.stat().st_size for p in (OUT/'inputs').glob('*.gz'))
m['stat_unstable_inputs']=[p for p,v in m['files'].items() if not v['stat_stable_during_read']]
p=OUT/('input_manifest_'+label+'.json')
with p.open('x') as f:json.dump(m,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'manifest':p.as_posix(),'sha256':sha(p.read_bytes()),'files':len(m['files']),
                 **{k:m[k] for k in ['started_utc','finished_utc','snapshot_runs','archive_unique_bytes','stat_unstable_inputs']}},indent=2))
