from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx,fmpq as Q
import json,time
R=Path(__file__).resolve().parents[3];B=R/'research/numerics_v08_audit';sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator

def main():
 start=time.monotonic();ctx.prec=1024;outpath=B/'verification/result.json';assert not outpath.exists();inputs={}
 def read(p):inputs[str(p.relative_to(R))]=sha(p);return json.loads(p.read_text())
 manifest=read(B/'source/MANIFEST.json')
 for local,row in manifest['files'].items():p=B/'source'/local;assert sha(p)==row['sha256'];inputs[str(p.relative_to(R))]=sha(p)
 J=lambda x,y:(1-x-y)**2+y*y;assert J(Q(0),Q(0))==1 and J(Q(0),Q(1,2))==Q(1,2) and J(Q(1),Q(0))==0
 own=read(R/'research/far_pairing_audit/verification/result.json');accept=read(R/'research/far_pairing_audit/reviews/T4/ACCEPTANCE.json');peer=read(B/'source/N1_007_far_weak.json')
 # Bind the previously accepted record exactly, without presuming its key names.
 assert sha(R/'research/far_pairing_audit/verification/result.json')=='358174ebecc4668bb5000077378090fd2c5460a47170ab4618e09d7bc0aa9e1b'
 assert sha(R/'research/far_pairing_audit/reviews/T4/ACCEPTANCE.json')=='78f844c1534f2e1bfc7f418a74934bbf2fa4396f172868b899556901010d2c28'
 tab={r['k']:r for r in peer['rows']};comparisons=[]
 for row in own['rows']:
  K=row['K']
  if K not in [100000,1000000,3162278]:continue
  I=arb(row['I_v_endpoint']);S=arb(row['I_truncated_exact_sectors']);sgn=-1 if K in [100000,1000000] else 1;assert I*sgn>0 and S*sgn>0
  published=arb(tab[K]['I_far']);assert published>0;relative=abs(published-abs(S))/abs(S);assert relative<arb('1e-9')
  comparisons.append({'K':K,'full_signed_pairing':row['I_v_endpoint'],'truncated_signed_pairing':row['I_truncated_exact_sectors'],'published_magnitude_FLOAT':tab[K]['I_far'],'magnitude_relative_error_ball':relative.str(50),'true_relative_model_error':row['relative_pairing_error'],'signed_model_and_full_sign':sgn,'published_field_is_absolute_value':True})
 code=(B/'source/N1_far_weak.py').read_text();assert 'Ifar = abs(sum(v for e, v in terms_k))' in code;assert len(peer['sectors_sin1'])==30
 rank=read(R/'research/scaled_quotient_rank/verification/result.json');assert rank['mode17_Cartesian_coefficient_equal'] and Q(rank['mode17_leading_harmonic_coefficient'])!=0
 objective=read(R/'research/candidate016_holdout/verification/result.json')
 publication=(B/'source/numerics_v08.md').read_text();status=(B/'source/N1_RUN_STATUS.md').read_text();final=(B/'source/N1_NUMERICS_FINAL.md').read_text()
 assert 'over all k' in publication and 'a span limit' in publication and 'SPAN limit' in status and 'SPAN limit' in final
 for p in [Path(__file__),B/'PROOF.md',R/'research/uniform_first_mode_tail/reviews/T4/ACCEPTANCE.json',R/'research/numerics_v07_audit/verification/result.json']:inputs[str(p.relative_to(R))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'publication_sha256':sha(B/'source/numerics_v08.md'),'nested_space_counterexample':{'old_trial_squared_residual':'1','new_trial_squared_residual':'1/2','old_exact_minimum':'0','residual_column_determinant':'1'},'signed_model_comparisons':comparisons,'nonzero_first_sine_sectors':30,'mode17_exact_coefficient':rank['mode17_leading_harmonic_coefficient'],'inputs':inputs,'elapsed_seconds':time.monotonic()-start,'verdicts':{'trial_improvement_implies_positive_old_span_floor':'REFUTED general inference; actual IPM optimum OPEN','first_mode_global_maximum_at12288':'OPEN; finite FLOAT sweep and available tail bounds do not establish this','signed_sector_sum_label':'REFUTED as labelled; stored I_far is an absolute magnitude','new_density_support_only19to31':'REFUTED; explicit nonzero mode17 fixture','exact_physical_density_rank_from_FLOAT_Gram':'OPEN; no such certificate supplied','finite_whole_plane_model_errors221':'CONFIRMED previously; includes1e6 and3162278'}}
 with outpath.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'v08scopeaudit',sha(outpath),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
