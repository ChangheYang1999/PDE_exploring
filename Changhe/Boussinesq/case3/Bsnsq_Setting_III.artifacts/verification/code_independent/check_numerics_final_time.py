"""Own source/data audit; never imports or executes another lane's code."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import ast, difflib, hashlib, json, re, time
root=Path('research/349_numerics_final_time_source'); v=root/'verification'
tick=time.monotonic(); started=datetime.now(timezone.utc); checks=[]
def ck(name, truth, detail=None):
    checks.append(dict(name=name,passed=bool(truth),detail=detail))
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dt(s): return datetime.fromisoformat(s.replace('Z','+00:00'))
f=json.loads((v/'freeze.json').read_text()); ck('proof_hash',digest(root/'PROOF.md')==f['proof_sha256'])
ck('proof_before_checks',dt(f['prepared_utc'])<started)
for i in f['inputs']:
    ck('frozen_hash_'+i['source'],digest(i['copy'])==i['sha256'])
    ck('frozen_size_'+i['source'],Path(i['copy']).stat().st_size==i['bytes'])
lookup={x['source']:Path(x['copy']) for x in f['inputs']}
log=lookup['../numerics/shifts/shifts.log'].read_text().splitlines()
starts={};ends={};mins={}
for line in log:
    m=re.fullmatch(r'(\S+) shift (\d+) start',line)
    if m: starts[int(m[2])]=dt(m[1])
    m=re.fullmatch(r'(\S+) shift (\d+) end exit (-?\d+) after (\d+) min',line)
    if m: ends[int(m[2])]=dt(m[1]);mins[int(m[2])]=int(m[4])
ck('nine_starts',set(starts)==set(range(1,10)))
ck('eight_ends',set(ends)==set(range(1,9)))
ck('eight_floor_counters',[mins[j] for j in range(1,9)]==[356,342,353,352,348,353,323,360])
ck('floor_sum_2787',sum(mins.values())==2787)
durations=[];gaps=[]
for j in range(1,9):
    d=int((ends[j]-starts[j]).total_seconds());g=int((starts[j+1]-ends[j]).total_seconds())
    durations.append(d);gaps.append(g)
    ck(f'floor_{j}',d//60==mins[j],dict(seconds=d,floor=mins[j],residue=d%60))
    ck(f'gap_{j}',g==30)
ck('gap_total',sum(gaps)==240)
t0=starts[1];cap=t0+timedelta(hours=48)
ck('cap_seconds',cap==dt('2026-10-22T12:44:13Z'))
examples=[]
for timestamp in ['2026-10-22T11:25:00Z','2026-10-22T12:42:00Z','2026-10-22T12:44:00Z','2026-10-22T12:44:12Z','2026-10-22T12:44:13Z','2026-10-22T12:44:14Z','2026-10-22T12:45:00Z']:
    event=dt(timestamp);q=event.replace(second=0,microsecond=0)
    occupancy=sum(durations)+int((q-starts[9]).total_seconds())
    floored=sum(mins.values())+int((q-starts[9]).total_seconds())//60
    wall=int((q-t0).total_seconds())
    ck('telescoping_'+timestamp,wall==occupancy+240)
    loss=occupancy-60*floored
    ck('floor_loss_'+timestamp,loss==sum(d%60 for d in durations)+int((q-starts[9]).total_seconds())%60)
    cls='before' if event<cap else 'at' if event==cap else 'after'
    source_cls='at' if q>=dt('2026-10-22T12:44:00Z') else 'shortly before'
    examples.append(dict(event=timestamp,minute_cutoff=q.isoformat(),wall_seconds=wall,occupancy_seconds=occupancy,floored_occupancy_minutes=floored,floor_loss_seconds=loss,actual_relation=cls,source_word=source_cls))
ck('thirteen_seconds_early',examples[2]['actual_relation']=='before' and examples[2]['source_word']=='at')
ck('one_minute_late_also_at',examples[-1]['actual_relation']=='after' and examples[-1]['source_word']=='at')
ck('at_cap_floor_earlier',dt(examples[4]['minute_cutoff'])<cap)
source=lookup['../numerics/runs/final_tend.py'].read_text(); tree=ast.parse(source)
ck('clock_discards_seconds','utcnow().replace(second=0, microsecond=0)' in source)
ck('branch_minute_not_exact_cap',"horizon = 'at' if now >= datetime.datetime(2026, 10, 22, 12, 44) else 'shortly before'" in source)
ck('write_after_clock',source.index("open(out, 'w').write(s)")>source.index('datetime.datetime.utcnow()'))
ck('last_activity_claim','the last recorded activity of this lane: this entry' in source)
ck('overbroad_no_computation_claim','ran no computation' in source)
ck('no_foreign_execution',not any(isinstance(n,(ast.Import,ast.ImportFrom)) and any(a.name.startswith(('bq3','final_tend')) for a in n.names) for n in ast.walk(ast.parse(Path(__file__).read_text()))))
old=lookup['research/333_actual_numerics_wording/verification/NUM_REPORT.md'].read_text()
new=lookup['../numerics/NUM_REPORT.md'].read_text()
# The two literal passage pairs are extracted with independent boundaries from both documents.
def strip_passages(s):
    a=s.index('Time accounting: T0 = 2026-10-20T12:44:13Z (shifts/shifts.log).')
    b=s.index('\n\n## 8.',a); s=s[:a]+'[TIME6]'+s[b:]
    a=s.index('shifts/shifts.log. T_end');b=s.index('The timestamp exactly 48 h',a)
    return s[:a]+'[TIME9]'+s[b:]
ck('only_two_time_passages_changed',strip_passages(old)==strip_passages(new))
ck('actual_time_passages_changed',old!=new)
(v/'time_only.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='P333',tofile='current')))
f333=json.loads(Path('research/333_actual_numerics_wording/verification/freeze.json').read_text())
for i in f['inputs']:
    if '/artifacts/' not in i['source']:continue
    approved=[x for x in f333['inputs'] if x['source'].endswith('/artifacts/'+Path(i['source']).name)]
    ck('approved_artifact_'+Path(i['source']).name,len(approved)==1 and i['sha256']==approved[0]['sha256'])
preview=lookup['../numerics/runs/NUM_REPORT_final_preview.md'].read_text()
ck('preview_retains_unresolved_endpoint','No candidate data: none has been obtained.' in preview)
ck('preview_new_time_claim','the last recorded activity of this lane: this entry' in preview)
ck('preview_not_actual_report',preview!=new)
ended=datetime.now(timezone.utc)
out=dict(started_utc=started.isoformat(),ended_utc=ended.isoformat(),elapsed_seconds=time.monotonic()-tick,code_sha256=digest(__file__),proof_sha256=digest(root/'PROOF.md'),passed=sum(c['passed'] for c in checks),total=len(checks),recorded_shift_seconds=durations,gaps_seconds=gaps,exact_completed_occupancy_seconds=sum(durations),floor_loss_completed_seconds=sum(durations)-60*sum(mins.values()),examples=examples,checks=checks)
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:val for k,val in out.items() if k!='checks'},indent=2))
for c in checks:
    if not c['passed']: print('FAILED',c)
