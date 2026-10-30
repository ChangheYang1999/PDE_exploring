from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib,json,os,signal,sys,time
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3]
LANE=BASE.parent
sys.set_int_max_str_digits(0)
ctx.prec=2048
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def freeze(src,dst):
 src,dst=Path(src),Path(dst);data=src.read_bytes();dst.parent.mkdir(parents=True,exist_ok=True)
 if dst.exists():assert dst.read_bytes()==data,str(dst)
 else:dst.write_bytes(data)
 return sha(dst)
def alive(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]
 except FileNotFoundError:return None
begin=datetime.now(timezone.utc).isoformat();start=time.monotonic();stopped=[]
try:
 root=286853;state=alive(root)
 if state and state not in ['T','Z','X']:os.kill(root,signal.SIGSTOP);stopped.append(root)
 if state:
  f=Path(f'/proc/{root}/task/{root}/children')
  for text in f.read_text().split() if f.exists() else []:
   pid=int(text);state=alive(pid)
   if state and state not in ['T','Z','X']:os.kill(pid,signal.SIGSTOP);stopped.append(pid)
 configs=[('numerics_v06_audit','omitted_far_sector','1c1d57752d6422ffb7fc93fcf586bdf0a919f4a0514379a0c335dcc426319706'),('far_pairing_audit','full_far_pairing','2a2bf86bfe9a2b5589c9ba808c9dfca0c04b1577021767ed94f324f1072ccf0b')]
 for topic,peer_topic,expected in configs:
  dest=BASE/topic/'reviews/T4';ownpath=BASE/topic/'verification/result.json';peerroot=LANE.parent/'c1-t4/research'/peer_topic;peerpath=peerroot/'verification/result.json'
  own=json.loads(ownpath.read_text());peer=json.loads(peerpath.read_text());assert sha(peerpath)==expected
  bindings={str(p):sha(p)==h for p,h in peer['inputs'].items()};assert all(bindings.values())
  assert sha(ownpath) in peer['inputs'].values()
  frozen={}
  for text,h in peer['inputs'].items():
   p=Path(text);rel=p.relative_to(LANE.parent/'c1-t4/research');target=dest/'source'/rel
   frozen[str(target.relative_to(LANE))]=freeze(p,target);assert frozen[str(target.relative_to(LANE))]==h
  target=dest/'T4_result.json';frozen[str(target.relative_to(LANE))]=freeze(peerpath,target)
  checks={};rows=[]
  if topic=='numerics_v06_audit':
   checks['seven_rows']=len(peer['rows'])==len(own['rows'])==7
   for row,old in zip(peer['rows'],own['rows'],strict=True):
    q=row['q'];checks[f'q{q}_index']=q==old['q']
    checks[f'q{q}_density']=Fraction(row['density_exact'])==Fraction(old['rho_sine1_exact'])
    checks[f'q{q}_residual']=Fraction(row['residual_exact'])==Fraction(old['linear_residual_sine1_exact'])
    checks[f'q{q}_peer_flag']=row['peer_exact_agreement']
   checks['q4_nonzero']=Fraction(peer['rows'][4]['residual_exact'])!=0 and peer['q4_nonzero']
   c=Fraction(4076476460239181,2251799813685248);delta=1-1/c
   checks['nonresonance']=all(((ell-1)*delta/2).denominator!=1 for ell in range(2,17)) and peer['nonresonance_ell_2_to_16']
  else:
   checks['same_30_sectors']=peer['exact_model_sectors']==own['exact_model_sectors'] and len(peer['exact_model_sectors'])==30
   checks['same_q4']=Fraction(peer['q4_exact'])==Fraction(own['q4_exact'])!=0
   checks['all_19_K']=len(peer['rows'])==len(own['rows'])==19 and [r['K'] for r in peer['rows']]==[r['K'] for r in own['rows']]
   checks['all_16_branches']=peer['residual_branches']==16
   checks['all_4044_pairs']=peer['stream_density_pairs']==4044
   for row,old in zip(peer['rows'],own['rows'],strict=True):
    ck={'parts_direct':arb(row['I_parts']).overlaps(arb(row['I_direct'])),'peer_v':arb(row['I_parts']).overlaps(arb(old['I_v_endpoint'])),'peer_t':arb(row['I_parts']).overlaps(arb(old['I_t_endpoint'])),'precision':min(row['accuracy_bits'])>150,'peer_flags':all(row['checks'].values())}
    if 'model_checks' in row:
     for key in ['I_truncated_exact_sectors','global_pairing_error','absolute_pairing_error','relative_pairing_error','model_cancellation_fraction','leading_model_pairing','last_model_pairing']:
      ck[key]=arb(row[key]).overlaps(arb(old[key]))
     ck['last_term_strictly_smaller']=abs(arb(row['last_model_pairing']))<arb(row['absolute_pairing_error']) and abs(arb(old['last_model_pairing']))<arb(old['absolute_pairing_error'])
     ck['stored_flags']=not row['last_term_bounds_actual_error'] and not old['last_term_bounds_actual_error'] and all(row['model_checks'].values())
    assert all(ck.values()),(row['K'],ck);rows.append({'K':row['K'],'checks':ck})
   checks['15_model_errors']=sum('model_checks' in r for r in peer['rows'])==15
  assert all(checks.values()),checks
  out={'utc':datetime.now(timezone.utc).isoformat(),'peer_result_sha256':sha(peerpath),'own_result_sha256':sha(ownpath),'acceptance_code_sha256':sha(__file__),'review_sha256':sha(dest/'REVIEW.md'),'peer_input_bindings':bindings,'frozen_sources':frozen,'checks':checks,'rows':rows,'comparison_count':len(bindings)+len(checks)+sum(len(r['checks']) for r in rows),'peer_completion_utc':peer['utc'],'peer_elapsed_seconds':peer['elapsed_seconds'],'verdict':'CONFIRMED exact finite-list claims under the standalone proof hypotheses'}
  with (dest/'ACCEPTANCE.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
  print(topic,out['utc'],'checks',out['comparison_count'],'sha256',sha(dest/'ACCEPTANCE.json'),flush=True)
finally:
 for pid in reversed(stopped):
  try:os.kill(pid,signal.SIGCONT)
  except ProcessLookupError:pass
 out={'began_utc':begin,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'stopped_and_resumed_pids':stopped}
 with (BASE/'far_pairing_audit/reviews/T4/pause.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
