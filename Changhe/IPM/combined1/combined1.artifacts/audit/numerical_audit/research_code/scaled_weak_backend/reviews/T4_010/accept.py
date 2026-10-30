from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,os,signal,sys,time
from flint import arb,ctx
BASE=Path(__file__).resolve().parent;LANE=BASE.parents[3]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def freeze(src,dst):
 src=Path(src);dst=Path(dst);data=src.read_bytes()
 if dst.exists():assert dst.read_bytes()==data,str(dst)
 else:dst.write_bytes(data)
 return sha(dst)
def alive(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]
 except FileNotFoundError:return None
mode=int(sys.argv[1]);assert mode in [1,7];ctx.prec=2048
start=time.monotonic();begin=datetime.now(timezone.utc).isoformat();stopped=[]
try:
 for root in [504137,286853]:
  state=alive(root)
  if state and state not in ['T','Z','X']:
   os.kill(root,signal.SIGSTOP);stopped.append(root)
  if state:
   f=Path(f'/proc/{root}/task/{root}/children')
   for s in f.read_text().split() if f.exists() else []:
    pid=int(s);state=alive(pid)
    if state and state not in ['T','Z','X']:
     os.kill(pid,signal.SIGSTOP);stopped.append(pid)
 peerroot=LANE.parent/'c1-t4/research/scaled_polar_weak'
 peerpath=peerroot/f'verification/010_n{mode}.json'
 ownpath=LANE/f'research/scaled_weak_backend/verification/C1-N1-010-d2w-j7-x3bal-legqs_n{mode}.json'
 peer=json.loads(peerpath.read_text());own=json.loads(ownpath.read_text())
 expected={7:'2548752c2002d17536fb9485a75e6494f266cbc745c34e8efd8562ff10273d68'}
 if mode in expected:assert sha(peerpath)==expected[mode]
 assert peer['angular_mode']==own['angular_mode']==mode
 assert peer['precision_bits']==own['bits']==2048
 bindings={str(p):sha(p)==v for p,v in peer['inputs'].items()};assert all(bindings.values())
 assert peer['source_sha256'] in own['inputs'].values()
 assert sha(ownpath) in peer['inputs'].values()
 frozen={}
 for ptext,digest in peer['inputs'].items():
  p=Path(ptext)
  if p.suffix in ['.md','.py'] or ('probe_n' in p.name):
   relative=p.relative_to(LANE.parent/'c1-t4/research')
   dst=BASE/'source'/relative;dst.parent.mkdir(parents=True,exist_ok=True)
   frozen[str(dst.relative_to(LANE))]=freeze(p,dst);assert frozen[str(dst.relative_to(LANE))]==digest
 dst=BASE/f'T4_n{mode}.json';frozen[str(dst.relative_to(LANE))]=freeze(peerpath,dst)
 checks={k:arb(peer[k]).overlaps(arb(own[k])) for k in ['pairing','pairing_parts','M','C','radius']}
 checks['pairings_overlap']=arb(peer['pairing']).overlaps(arb(peer['pairing_parts']))
 checks['candidate007_calibration']=peer['calibration']['R1_exact_polar_fields']
 checks['independent_point_calibration']=all(peer['independent_point_overlaps'].values())
 checks['peer_flags']=all(peer['peer_comparisons'].values())
 checks['same_H']=Fraction(peer['sup_certificate']['H_upper_exact'])==Fraction(own['H_upper_exact'])
 checks['same_floor']=Fraction(peer['strict_lower_exact'])==Fraction(own['strict_lower_exact'])
 floor=Fraction(own['strict_lower_exact']);bound=arb(floor.numerator)/floor.denominator
 checks['strict_floor_peer']=bound<arb(peer['radius']);checks['strict_floor_own']=bound<arb(own['radius'])
 checks['own_gradient_cover']=own['H_cover_tiles_unit_interval']
 moments=[m for key in ['M_moments','C_moments','direct_moments','parts_moments'] for m in peer[key]]
 checks['64_moments']=len(moments)==64
 checks['all_CRT_replay']=all(m.get('exact_zero') or m['exact_CRT_replay'] for m in moments)
 checks['all_150bits']=all(m.get('exact_zero') or m['accuracy_bits']>150 for m in moments)
 assert all(checks.values()),checks
 out={'utc':datetime.now(timezone.utc).isoformat(),'angular_mode':mode,'peer_result_sha256':sha(peerpath),'own_result_sha256':sha(ownpath),'executed_acceptance_sha256':sha(__file__),'review_sha256':sha(BASE/'REVIEW.md'),'peer_source_bindings':bindings,'frozen_sources':frozen,'checks':checks,'comparison_count':len(checks)+len(bindings),'minimum_moment_accuracy_bits':min(m['accuracy_bits'] for m in moments if not m.get('exact_zero')),'strict_lower_exact':str(floor),'peer_runtime_seconds':peer['elapsed_seconds'],'status':'CONFIRMED'}
 with (BASE/f'ACCEPTANCE_n{mode}.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({'utc':out['utc'],'mode':mode,'comparisons':out['comparison_count'],'minimum_bits':out['minimum_moment_accuracy_bits'],'floor':str(floor),'status':out['status']}))
finally:
 for pid in reversed(stopped):
  try:os.kill(pid,signal.SIGCONT)
  except ProcessLookupError:pass
 record={'began_utc':begin,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'stopped_and_resumed_pids':stopped}
 with (BASE/f'pause_n{mode}.json').open('x') as f:json.dump(record,f,indent=2);f.write('\n')
