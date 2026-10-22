"""Record the real end-of-run observation only after the wall horizon."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json
assert Path.cwd()==Path('verification')
t0=datetime(2026,10,20,12,44,15,tzinfo=timezone.utc);cap=t0+timedelta(seconds=172800);now=datetime.now(timezone.utc)
if now<cap:raise RuntimeError('Wall horizon not yet reached; no future end timestamp written')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads(Path('FINALIZATION_RECORD.json').read_text());c=json.loads(Path('FINALIZATION_CHECK.json').read_text());assert c['passed']==c['total']
peers=[]
for q in r['peer_reports']:
 p=Path('..')/('bq3-'+q['lane'])/q['file'];h=sha(p);peers.append(dict(lane=q['lane'],sha256=h,still_matches_verified=h==q['sha256']))
d=dict(T0=t0.isoformat(),T_end=now.isoformat(),elapsed_wall_seconds=(now-t0).total_seconds(),wall_cap=cap.isoformat(),seconds_after_wall_cap=(now-cap).total_seconds(),report_cutoff=r['T_end_report_cutoff'],endpoint='UNRESOLVED',accepted_yes=False,accepted_no=False,closing_record_sha256=sha('FINALIZATION_RECORD.json'),closing_check_sha256=sha('FINALIZATION_CHECK.json'),closing_checks_passed=c['passed'],closing_checks_total=c['total'],peer_report_observations=peers,active_research_time='not separately measured',scope='Real final wall-clock observation of this verifier run. Report cutoff and the outer-loop session end are distinct events. No further research computation follows this sample.')
Path('RUN_END_OBSERVATION.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
