"""Independent all-mode interval acceptance, no foreign code executed."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys,time
from flint import arb,ctx,fmpq as Q
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/negative_norm007_peer';sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator

def main():
 start=time.monotonic();ctx.prec=2048;dest=B/'verification/result.json';assert not dest.exists();inputs={}
 def read(p):inputs[str(p.relative_to(R))]=sha(p);return json.loads(p.read_text())
 manifest=read(B/'source/MANIFEST.json')
 for local,rec in manifest['files'].items():
  p=B/'source'/local;assert sha(p)==rec['stored_sha256'];raw=gzip.decompress(p.read_bytes()) if local.endswith('.gz') else p.read_bytes();assert sha256(raw).hexdigest()==rec['original_sha256'];inputs[str(p.relative_to(R))]=sha(p)
 peer=json.loads(gzip.decompress((B/'source/N3_007_hminus1.json.gz').read_bytes()))
 ownpath=R/'research/whole_plane_norms/verification/C1-N1-007-d2w-j7-e2bal_Hminus1_ball_2048.json';own=read(ownpath)
 canonical=R/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json';can=read(canonical)
 assert peer['source_sha256']==peer['input_sha256']==can['source_sha256']
 assert peer['canonical_sha256']==can['canonical_serialization_sha256'] and own['source_sha256']==sha(canonical)
 fixes={r['code_sha256'] for r in peer['fixes']}
 assert sha(B/'source/N3_hminus1_hardy_fix.py') in fixes and sha(B/'source/N3_hminus1_mode_hardy.py') in fixes
 modes={r['n']:r for r in own['mode_contributions']};explicit=set(peer['modes']);tails=set(peer['tail']['modes'])
 assert len(modes)==160 and set(modes)==set(range(1,320,2));assert explicit==set(range(1,62,2)) and tails==set(range(63,320,2)) and not explicit&tails and explicit|tails==set(modes)
 assert len(peer['rows'])==31 and {r['n'] for r in peer['rows']}==explicit
 comparisons=[]
 for row in peer['rows']:
  ctx.prec=2048;n=row['n'];value=arb(modes[n]['norm']);lo,hi=arb(row['mode_norm_LB']),arb(row['mode_norm_UB']);assert lo<value and value<hi,(n,'independent norm containment')
  N,D,P,V=(Q(row[k]) for k in ['F_phi_over_pi','grad_phi_sq_over_pi','phi_g_over_pi','rg_sq_over_pi']);assert D>0 and V>=0 and P==N-D
  expected=max(N*N/D,2*N-D,Q(0));assert expected==Q(row['lb_sq_over_pi']);assert D+2*P+V==Q(row['ub_sq_identity_over_pi'])
  err=arb(row['err_Hardy_norm']);assert err>=0
  # At the peer precision the lower and old Galerkin endpoints must enclose
  # the derived scalar expressions. Stored strings themselves are balls.
  ctx.prec=512;lower=(arb.pi()*ar(expected)).sqrt()-arb(row['err_Hardy_norm']);u1=(arb.pi()*ar(D+2*P+V)).sqrt()+arb(row['err_Hardy_norm']);u2=(arb.pi()*ar(D)).sqrt()+(arb.pi()*ar(V)).sqrt()+arb(row['err_Hardy_norm'])
  plo=arb(row['mode_norm_LB']);assert plo.lower()<=lower.upper()
  uk='mode_norm_UB_galerkin' if 'mode_norm_UB_galerkin' in row else 'mode_norm_UB_before_mode_hardy' if 'mode_norm_UB_before_mode_hardy' in row else 'mode_norm_UB'
  original=arb(row[uk]);assert original.upper()>=u1.lower() or original.upper()>=u2.lower(),(n,'original Galerkin scalar arithmetic')
  divided=(arb(row['hardy_direct_UB'])/n).upper();assert arb(row['mode_n_hardy_UB']).overlaps(divided)
  changed='mode_norm_UB_before_mode_hardy' in row
  if changed:assert arb(row['mode_norm_UB']).overlaps(arb(row['mode_n_hardy_UB']))
  comparisons.append({'n':n,'direct_norm':value.str(70),'strictly_inside_peer_bounds':True,'rational_identities':True,'Galerkin_scalar_endpoint_consistency':True,'mode_Hardy_division_overlap':True,'mode_Hardy_selected':changed})
 ctx.prec=2048;tail=(arb.pi()*sum((arb(modes[n]['squared_norm_div_pi']) for n in tails),arb(0))).sqrt();assert tail<arb(peer['tail']['rF_norm_UB'])
 full=arb(own['norm_ball']);assert arb(peer['H_lower'])<full and full<arb(peer['H_upper'])
 sq=sum((arb(r['squared_norm_div_pi']) for r in modes.values()),arb(0));assert sq.overlaps(arb(own['squared_norm_div_pi'])) and (arb.pi()*sq).sqrt().overlaps(full)
 ctx.prec=512;taildiv=(arb(peer['tail']['rF_norm_UB_before_mode_hardy'])/63).upper();assert arb(peer['tail']['rF_norm_UB']).overlaps(taildiv)
 lo=(sum((arb(r['mode_norm_LB'])**2 for r in peer['rows']),arb(0))).sqrt().lower();hi=(sum((arb(r['mode_norm_UB'])**2 for r in peer['rows']),arb(0))+arb(peer['tail']['rF_norm_UB'])**2).sqrt().upper()
 assert arb(peer['H_lower']).overlaps(lo) and arb(peer['H_upper']).overlaps(hi)
 ctx.prec=2048;low=Q(6355243760000922,10**16);high=Q(6355322685705510,10**16);assert ar(low)<arb(peer['H_lower']) and arb(peer['H_upper'])<ar(high)
 for p in [Path(__file__),B/'PROOF.md',R/'research/exact_negative_norm/code/negative_ball.py',R/'research/exact_negative_norm/PROOF.md']:inputs[str(p.relative_to(R))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':own['candidate'],'source_sha256':peer['source_sha256'],'canonical_serialization_sha256':peer['canonical_sha256'],'canonical_file_sha256':sha(canonical),'peer_original_result_sha256':manifest['files']['N3_007_hminus1.json.gz']['original_sha256'],'peer_historical_root_code_sha256':peer['code_sha256'],'peer_current_inspected_code_sha256':sha(B/'source/N3_hminus1.py'),'historical_root_code_not_available_as_that_version':peer['code_sha256']!=sha(B/'source/N3_hminus1.py'),'source_and_fix_bindings_confirmed':True,'all160modes_covered_once':True,'explicit_mode_comparisons':comparisons,'tail_modes':len(tails),'direct_tail_norm':tail.str(80),'peer_tail_upper':peer['tail']['rF_norm_UB'],'tail_division_by63_verified':True,'direct_norm':own['norm_ball'],'peer_lower':peer['H_lower'],'peer_upper':peer['H_upper'],'strict_coarse_lower_exact':str(low),'strict_coarse_upper_exact':str(high),'peer_totals_reproduced_at512bits':True,'own_full_norm_strictly_inside_peer':True,'inputs':inputs,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED coarse whole-plane enclosure by independent complete Green formula. No certification of every finer own digit or every internal peer Galerkin coefficient.'}
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',out['utc'],'31explicit+129tail',out['direct_norm'][:100],'seconds',out['elapsed_seconds'],'SHA',sha(dest),flush=True)
if __name__=='__main__':main()
