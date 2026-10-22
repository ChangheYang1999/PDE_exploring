"""Read-only foreign source audit, no execution/import of that source."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import ast,hashlib,json,re,time
r=Path('research/352_revised_numerics_time_source');v=r/'verification';start=datetime.now(timezone.utc);tick=time.monotonic();checks=[]
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dt(s):return datetime.fromisoformat(s.replace('Z','+00:00'))
def ck(n,t,d=None):checks.append(dict(name=n,passed=bool(t),detail=d))
f=json.loads((v/'freeze.json').read_text());ck('proof_hash',h(r/'PROOF.md')==f['proof_sha256']);ck('proof_before',f['revised_utc']<start.isoformat());srcs={i['source']:Path(i['copy']) for i in f['inputs']}
for i in f['inputs']:ck('hash_'+i['source'],h(i['copy'])==i['sha256']);ck('size_'+i['source'],Path(i['copy']).stat().st_size==i['bytes'])
s=srcs['../numerics/runs/final_tend.py'].read_text();tree=ast.parse(s)
ck('full_clock_no_minute_replace','utcnow().replace' not in s);ck('cutoff_named','T_end (report cutoff)' in s);ck('strict_bracket',"post < CAP else ('after cap (pre > cap)' if pre > CAP else 'UNRESOLVED" in s);ck('cutoff_missing_equality',"pos = 'before' if pre < CAP else 'after'" in s);ck('pre_write_post_order',s.index('pre = datetime.datetime.utcnow()')<s.index("open(out, 'w').write(s)")<s.index('post = datetime.datetime.utcnow()'));ck('hash_after_post',s.index('sha = hashlib.sha256')>s.index('post = datetime.datetime.utcnow()'));ck('record_after_hash',s.index("open('runs/final_tend_record.txt', 'a').write(rec)")>s.index('sha = hashlib.sha256'));ck('source_custom_fraction_layout','pre={fmt(pre)}.{pre.microsecond:06d}' in s);ck('report_displays_seconds','fmt = lambda t: t.strftime(\'%Y-%m-%dT%H:%M:%SZ\')' in s);ck('no_past_idle_end','after which the session idled past' not in s)
t0=dt('2026-10-20T12:44:13Z');cap=t0+timedelta(hours=48);micro=timedelta(microseconds=1);examples=[]
for j in [-1000001,-1,0,1,1000001]:
 p=cap+j*micro;actual='before' if p<cap else 'at' if p==cap else 'after';current='before' if p<cap else 'after';ck('cutoff_agreement_except_equality_'+str(j),(actual==current)==(j!=0));examples.append(dict(p=p.isoformat(),actual=actual,current=current))
for a,b in [(-3,-1),(-1,0),(0,0),(0,1),(-1,1),(1,3)]:
 p=cap+a*micro;q=cap+b*micro;cl='before' if q<cap else 'after' if p>cap else 'unresolved';ck('bracket_sound_'+str((a,b)),(cl!='before' or q<cap) and (cl!='after' or p>cap));ck('bracket_order_'+str((a,b)),p<=q)
for micros in [0,1,123456,999999]:
 p=cap+timedelta(microseconds=micros);current=p.strftime('%Y-%m-%dT%H:%M:%SZ')+f'.{p.microsecond:06d}';standard=p.strftime('%Y-%m-%dT%H:%M:%S.%fZ');ck('format_nonstandard_'+str(micros),current!=standard);rec=datetime.strptime(current,'%Y-%m-%dT%H:%M:%SZ.%f').replace(tzinfo=timezone.utc);ck('custom_recovery_'+str(micros),rec==p);ck('standard_recovery_'+str(micros),dt(standard)==p)
starts={};ends={};floors={}
for line in srcs['../numerics/shifts/shifts.log'].read_text().splitlines():
 m=re.fullmatch(r'(\S+) shift (\d+) start',line)
 if m:starts[int(m[2])]=dt(m[1])
 m=re.fullmatch(r'(\S+) shift (\d+) end exit (-?\d+) after (\d+) min',line)
 if m:ends[int(m[2])]=dt(m[1]);floors[int(m[2])]=int(m[4])
ck('first_start_equals_hardcoded_t0',starts[1]==t0);ck('nine_starts_eight_ends',set(starts)==set(range(1,10)) and set(ends)==set(range(1,9)))
D=sum((ends[k]-starts[k]).total_seconds() for k in range(1,9));g=sum((starts[k+1]-ends[k]).total_seconds() for k in range(1,9));ck('completed_seconds',D==167486);ck('completed_floors',sum(floors.values())==2787);ck('gap_seconds',g==240)
for ts in ['2026-10-22T11:40:00.123456Z','2026-10-22T12:42:00.999999Z','2026-10-22T12:44:13Z']:
 p=dt(ts);ck('cutoff_after_shift9_'+ts,p>=starts[9]);occ=D+(p-starts[9]).total_seconds();wall=(p-t0).total_seconds();ck('telescoping_'+ts,abs(wall-occ-g)<1e-9)
old=json.loads(Path('research/333_actual_numerics_wording/verification/freeze.json').read_text())
for i in f['inputs']:
 if '/artifacts/' in i['source']:
  matches=[x for x in old['inputs'] if x['source'].endswith('/artifacts/'+Path(i['source']).name)];ck('approved_artifact_'+Path(i['source']).name,len(matches)==1 and matches[0]['sha256']==i['sha256'])
for name in ['README.md','consolidated_residuals.md','consolidate_audits.py','code_sha256.txt']:
 approved=Path('research/330_numerics_wording_rebase/verification/approved/artifacts')/name
 actual=Path('research/333_actual_numerics_wording/verification/artifacts')/name
 ck('P330_P333_byte_identity_'+name,approved.read_bytes()==actual.read_bytes())
p=cap+timedelta(microseconds=400000);ck('displayed_cap_but_true_after',p.strftime('%Y-%m-%dT%H:%M:%SZ')==cap.strftime('%Y-%m-%dT%H:%M:%SZ') and p>cap)
old_report=Path('research/349_numerics_final_time_source/verification/freeze.json');f349=json.loads(old_report.read_text());i349=next(i for i in f349['inputs'] if i['source']=='../numerics/NUM_REPORT.md');ck('actual_report_still_provisional_unchanged',h(srcs['../numerics/NUM_REPORT.md'])==i349['sha256'])
ck('start9_offset',int((starts[9]-t0).total_seconds())==167726)
ck('cap_remaining_seconds',int((cap-starts[9]).total_seconds())==5074)
ck('cap_occupancy',D+(cap-starts[9]).total_seconds()==172560)
ck('cap_floor_counters',2787+int((cap-starts[9]).total_seconds())//60==2871)
ck('floor_of_total_differs',int(D)//60==2791 and int(D)//60!=sum(floors.values()))
ck('source_cap_naive','CAP = datetime.datetime(2026, 10, 22, 12, 44, 13)' in s)
ck('source_hash_rereads_output',"hashlib.sha256(open(out, 'rb').read())" in s)
for item in f['manifest_sources']:
 ck('manifest_exists_'+item['source'],Path(item['copy']).is_file())
 ck('manifest_sha_'+item['source'],h(item['copy'])==item['sha256']==item['advertised_sha256'])
ck('manifest_66',len(f['manifest_sources'])==66)
ck('manifest_unique',len({x['source'] for x in f['manifest_sources']})==66)
end=datetime.now(timezone.utc);out=dict(started_utc=start.isoformat(),ended_utc=end.isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(c['passed'] for c in checks),total=len(checks),proof_sha256=h(r/'PROOF.md'),code_sha256=h(__file__),source_sha256=h(srcs['../numerics/runs/final_tend.py']),examples=examples,checks=checks);(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:x for k,x in out.items() if k not in ('checks','examples')},indent=2))
for c in checks:
 if not c['passed']:print('FAILED',c)
