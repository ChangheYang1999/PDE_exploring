#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,re,time
v=Path('research/347_final_evidence_and_time/verification');started=datetime.now(timezone.utc);tick=time.monotonic();checks=[]
def ck(n,t,d=None):checks.append(dict(name=n,passed=bool(t),detail=d))
def dt(s):return datetime.fromisoformat(s.replace('Z','+00:00'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((v/'freeze.json').read_text());ck('proof_before_check',dt(f['revised_utc'])<started);ck('proof_hash',sha(v.parent/'PROOF.md')==f['proof_sha256'])
for name,key in [('loop_source.sh','loop_sha256'),('shifts_snapshot.log','shifts_sha256')]:ck('source_'+name,sha(v/name)==f[key])
for z in f['additional_inputs']:ck('input_'+z['snapshot'],sha(v/z['snapshot'])==z['sha256'])
def parse_lane(label,name,expected):
 text=(v/name).read_text();starts={};ends={};floors={}
 for line in text.splitlines():
  z=re.match(r'^(\S+) shift (\d+) (start|end)\b(.*)$',line)
  if not z:continue
  stamp,n,kind,rest=z.groups();n=int(n)
  (starts if kind=='start' else ends)[n]=dt(stamp)
  if kind=='end': floors[n]=int(re.search(r'after (\d+) min',rest).group(1))
 ck(label+'_T0',starts[1]==dt(expected));horizon=starts[1]+timedelta(hours=48)
 completed=[];gaps=[]
 for n,e in sorted(ends.items()):
  secs=(e-starts[n]).total_seconds();ck(label+'_duration_'+str(n),secs>=0 and int(secs//60)==floors[n]);completed.append(dict(shift=n,seconds=secs,logged_floor_minutes=floors[n]))
  if n+1 in starts:
   g=(starts[n+1]-e).total_seconds();gaps.append(dict(after_shift=n,seconds=g));ck(label+'_restart_gap_'+str(n),g==30)
 ck(label+'_seven_known_gaps',len(gaps)==7)
 first_missing=[n for n in starts if n not in ends and n<max(starts)]
 ck(label+'_missing_initial_end',first_missing==([1] if label=='verifier' else []))
 complete_seconds=sum(z['seconds'] for z in completed);counter=sum(z['logged_floor_minutes'] for z in completed)
 current=max(starts);current_secs=(started-starts[current]).total_seconds()
 ck(label+'_ongoing_not_future',current_secs>=0 and started<horizon)
 return dict(T0=starts[1].isoformat(),horizon=horizon.isoformat(),snapshot_utc=started.isoformat(),wall_elapsed_seconds=(started-starts[1]).total_seconds(),completed_shifts=completed,completed_session_seconds=complete_seconds,completed_logged_floor_minutes=counter,rounding_loss_seconds=complete_seconds-60*counter,known_gaps=gaps,known_gap_seconds=sum(z['seconds'] for z in gaps),current_shift=current,current_shift_start=starts[current].isoformat(),current_session_seconds=current_secs,missing_completed_ends=first_missing,session_occupancy_not_active_time=True)
lanes={label:parse_lane(label,name,T0) for label,name,T0 in [('verifier','shifts_snapshot.log','2026-10-20T12:44:15Z'),('lead','lead_shifts.log','2026-10-20T12:44:11Z'),('numerics','num_shifts.log','2026-10-20T12:44:13Z')]}
for a,b,gap in [('verifier','lead',4),('numerics','lead',2)]:ck('distinct_horizons_'+a,(dt(lanes[a]['horizon'])-dt(lanes[b]['horizon'])).total_seconds()==gap)
num=lanes['numerics'];provisional=dt('2026-10-22T10:58:00Z');num_sec=num['completed_session_seconds']+(provisional-dt(num['current_shift_start'])).total_seconds();floor_min=num['completed_logged_floor_minutes']+int((provisional-dt(num['current_shift_start'])).total_seconds()//60)
ck('NUM_completed_counter2427',num['completed_logged_floor_minutes']==2427);ck('NUM_provisional_floor338',int((provisional-dt(num['current_shift_start'])).total_seconds()//60)==338);ck('NUM_provisional_counter46h05',floor_min==46*60+5)
wall=(provisional-dt(num['T0'])).total_seconds();ck('NUM_provisional_wall46h13m47',wall==46*3600+13*60+47);ck('NUM_provisional_exact_session46h10m17',num_sec==46*3600+10*60+17);ck('NUM_provisional_gap_partition',wall==num_sec+num['known_gap_seconds']);ck('NUM_counter_loss317seconds',num_sec-60*floor_min==317)
s=(v/'loop_source.sh').read_text();ck('outer_condition_before_timeout',s.index('while [ "$(date +%s)" -lt "$DEADLINE" ]')<s.index('timeout 6h'));ck('one_outer_deadline_assignment',len(re.findall(r'^DEADLINE=',s,re.M))==1);ck('single_loop_deadline_read',s.count('"$DEADLINE"')==1);ck('separate_6h_timeout',s.count('timeout 6h')==1);ck('timeout_foreground',not s[s.index('cd $DIR && timeout'):s.index('rc=$?')].rstrip().endswith('&'))
nominal=dt('2026-10-20T13:06:32Z')+timedelta(hours=47);shift9limit=dt(lanes['verifier']['current_shift_start'])+timedelta(hours=6)
ck('nominal_outer_deadline',nominal==dt('2026-10-22T12:06:32Z'));ck('shift9_nominal_end',shift9limit==dt('2026-10-22T13:09:05Z'));ck('shift9_covers_horizon',shift9limit>dt(lanes['verifier']['horizon']))
# Negative controls keep each rounding or mistaken substitution visible.
ck('negative_same_lane_clock',dt(lanes['lead']['horizon'])!=dt(lanes['verifier']['horizon']));ck('negative_counter_is_not_exact_duration',num_sec!=floor_min*60);ck('negative_wall_is_not_session_duration',wall!=num_sec);ck('negative_planned_time_not48h',dt('2026-10-22T12:43:30Z')<dt(lanes['lead']['horizon']));ck('negative_one_missing_end_prevents_unique_first_duration',lanes['verifier']['missing_completed_ends']==[1])
out=dict(started_utc=started.isoformat(),ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,code_sha256=sha(Path(__file__)),proof_sha256=f['proof_sha256'],passed=sum(z['passed'] for z in checks),total=len(checks),checks=checks,lanes=lanes,numerics_provisional=dict(stated_utc=provisional.isoformat(),wall_seconds=wall,exact_session_occupancy_seconds=num_sec,logged_floor_minutes=floor_min,rounding_loss_seconds=num_sec-60*floor_min,active_time_not_proved=True),scope='Finite source and timestamp accounting only. No actual finalization or future end time is certified.')
(v/'time_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:z for k,z in out.items() if k not in ['checks','lanes']},indent=2));print('FAILED',[z for z in checks if not z['passed']]);raise SystemExit(0 if all(z['passed'] for z in checks) else 1)
