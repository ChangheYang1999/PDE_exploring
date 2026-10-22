"""Independent byte/time readback of this lane's actual closing files."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json
root=Path.cwd();assert root==Path('verification')
started=datetime.now(timezone.utc);checks=[]
def ck(name,ok):checks.append(dict(name=name,passed=bool(ok)))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dt(s):return datetime.fromisoformat(s.replace('Z','+00:00'))
p=Path('FINALIZATION_RECORD.json');raw=p.read_bytes();r=json.loads(raw);t0=dt(r['T0']);end=dt(r['T_end_report_cutoff']);cap=t0+timedelta(seconds=172800);pre=dt(r['write_pre_utc']);post=dt(r['write_post_utc'])
ck('known_T0',t0==dt('2026-10-20T12:44:15Z'));ck('known_cap',dt(r['cap'])==cap);ck('ordered_real_clock_bracket',end<=pre<=post<=started);ck('real_elapsed',(end-t0).total_seconds()==r['elapsed_wall_seconds']);ck('headline_before_or_after',r['headline_bracket_confirmed']and((r['headline_classification']=='under'and post<cap)or(r['headline_classification']=='after'and pre>cap)));ck('scope_unresolved',r['endpoint']=='UNRESOLVED'and r['active_research_time']=='not separately measured')
lines=Path('shifts/shifts.log').read_text().splitlines();starts={};ends={}
for line in lines:
 a=line.split()
 if len(a)>=4 and a[1]=='shift' and a[2].isdigit():
  if a[3]=='start':starts[int(a[2])]=dt(a[0])
  elif a[3]=='end':ends[int(a[2])]=dt(a[0])
closed=sum((ends[i]-starts[i]).total_seconds()for i in range(2,10));current=(end-starts[10]).total_seconds();gaps=sum((starts[i+1]-ends[i]).total_seconds()for i in range(2,10));unknown=(starts[2]-starts[1]).total_seconds()
ck('raw_closed_shift_seconds',closed==r['completed_shift2_to9_seconds']);ck('raw_current_shift_seconds',current==r['current_shift10_seconds']);ck('raw_restart_gaps',gaps==r['restart_gaps_seconds']==240);ck('raw_unclassified_interval',unknown==r['unclassified_initial_interval_seconds']==1337);ck('raw_occupancy',closed+current==r['session_occupancy_seconds']);ck('raw_time_partition',abs(closed+current+gaps+unknown-r['elapsed_wall_seconds'])<1e-5)
for rel,v in r['files'].items():
 p=Path(rel);b=p.read_bytes();ck('file_size_'+rel,len(b)==v['bytes']);ck('file_sha256_'+rel,hashlib.sha256(b).hexdigest()==v['sha256'])
for no,c in r['actual_audits'].items():
 folder={'358':'358_final_archive_readback','359':'359_final_numerics_readback','360':'360_final_lead_readback'}[no];p=Path('research')/folder/'verification/checks.json';d=json.loads(p.read_text());ck('actual_audit_'+no,c['verdict']=='CONFIRMED'and d['passed']==d['total']and not d.get('fixture_only',False));ck('audit_unchanged_'+no,sha(p)==c['evidence_sha256'])
for q in r['peer_reports']:
 p=Path('..')/('bq3-'+q['lane'])/q['file'];ck('peer_report_current_'+q['lane'],q['verdict']=='CONFIRMED'and sha(p)==q['sha256'])
ck('finalizer_source',sha('code_independent/finalize_verifier_files.py')==r['finalizer_sha256']);ck('record_stable',Path('FINALIZATION_RECORD.json').read_bytes()==raw)
summary=Path('FINAL_VERIFIER_SUMMARY.md').read_text();ck('summary_headline',summary.splitlines()[0]==f'# UNRESOLVED: independent verification completed {r["headline_classification"]} the 48-hour wall-clock cap');ck('no_endpoint_claim','No accepted YES or NO endpoint has been established.'in summary);ck('active_time_scope','not a claim of 48 active research hours'in summary)
result=dict(started_utc=started.isoformat(),ended_utc=datetime.now(timezone.utc).isoformat(),passed=sum(c['passed']for c in checks),total=len(checks),checks=checks,record_sha256=hashlib.sha256(raw).hexdigest(),code_sha256=sha(__file__),scope='Actual finite closing-file observation. The outer session end and later wall-horizon observation are separate events; active research time not measured.')
Path('FINALIZATION_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='checks'},indent=2));print('FAILED',[c for c in checks if not c['passed']]);assert result['passed']==result['total']
