"""Check N3's independent d2 enclosure against every direct Green mode."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import arb,ctx,fmpq as Q
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/exact_negative_norm'
def digest(p):return sha256(p.read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/arb(q.denominator)

def run():
 start=time.monotonic();ctx.prec=2048
 peer_path=BASE/'peer_review/N3_d2_hminus1_20261028T2355.json'
 peer_code=BASE/'peer_review/N3_hminus1_20261028T2355.py'
 own_path=ROOT/'research/whole_plane_norms/verification/d2_Hminus1_ball_2048.json'
 canonical=ROOT/'research/refit_audit/data/d2_canonical.json'
 peer=json.loads(peer_path.read_text());own=json.loads(own_path.read_text());can=json.loads(canonical.read_text())
 assert peer['code_sha256']==digest(peer_code)
 assert peer['canonical_sha256']==can['canonical_serialization_sha256']
 assert peer['source_sha256']==peer['input_sha256']==can['source_sha256']
 assert own['source_sha256']==digest(canonical)
 modes={r['n']:r for r in own['mode_contributions']}
 exact_modes=set(peer['modes']);tail_modes=set(peer['tail']['modes'])
 assert not exact_modes & tail_modes and exact_modes|tail_modes==set(modes)
 assert len(exact_modes)==len(peer['rows'])==31
 comparisons=[]
 for row in peer['rows']:
  n=row['n'];value=arb(modes[n]['norm'])
  lo,hi=arb(row['mode_norm_LB']),arb(row['mode_norm_UB'])
  assert value>lo and value<hi
  N,D,P,R=(Q(row[k]) for k in ['F_phi_over_pi','grad_phi_sq_over_pi','phi_g_over_pi','rg_sq_over_pi'])
  assert D>0 and R>=0 and P==N-D
  expected=max(N*N/D,2*N-D,Q(0))
  assert expected==Q(row['lb_sq_over_pi'])
  assert D+2*P+R==Q(row['ub_sq_identity_over_pi'])
  error=arb(row['err_Hardy_norm'])
  lower=(arb.pi()*ar(expected)).sqrt()-error
  upper1=(arb.pi()*ar(D+2*P+R)).sqrt()+error
  upper2=(arb.pi()*ar(D)).sqrt()+(arb.pi()*ar(R)).sqrt()+error
  assert lo.lower() <= lower.lower()
  assert hi.upper() >= upper1.upper() or hi.upper() >= upper2.upper()
  comparisons.append({'n':n,'direct_norm':value.str(45),'contained_in_peer_bounds':True,
                      'rational_energy_identities':True,'derived_endpoints_outward_enclose':True})
 tail=(arb.pi()*sum((arb(modes[n]['squared_norm_div_pi']) for n in tail_modes),arb(0))).sqrt()
 assert tail<arb(peer['tail']['rF_norm_UB'])
 full=arb(own['norm_ball']);assert full>arb(peer['H_lower']) and full<arb(peer['H_upper'])
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
      'peer_result_sha256':digest(peer_path),'peer_code_sha256':digest(peer_code),
      'own_result_sha256':digest(own_path),'canonical_file_sha256':digest(canonical),
      'code_sha256':digest(Path(__file__)),'review_sha256':digest(BASE/'REVIEW_N3.md'),
      'source_identities_confirmed':True,'all_120_modes_covered_once':True,
      'explicit_mode_comparisons':comparisons,'tail_modes':len(tail_modes),
      'direct_tail_norm':tail.str(65),'peer_tail_upper':peer['tail']['rF_norm_UB'],
      'direct_full_norm':own['norm_ball'],'peer_lower':peer['H_lower'],'peer_upper':peer['H_upper'],
      'full_norm_contained':True,'peer_elapsed_seconds':peer['elapsed_seconds'],
      'elapsed_seconds':time.monotonic()-start,
      'scope':'Independent confirmation at the width of the peer interval; no independent certification of every digit in the narrower direct Green enclosure.'}
 dest=BASE/'verification/N3_d2_confirmation.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
 print('N3 d2: all31 explicit modes and89 tail modes confirmed',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run()
