"""Independent repaired Euler moments and source-bound calibration comparisons."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
import importlib.util,json,sys,time
from flint import arb,ctx,fmpq as Q
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/n3_repaired_calibration_runs'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();ctx.prec=1536;inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);s=sha(p);assert h is None or h==s,(str(p),h,s);inputs[str(p.relative_to(R))]=s;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE_v02.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 man=read(B/'source/MANIFEST.json',prep['prior_manifest_sha256'])
 for name,e in man['sources'].items():bind(B/'source'/name,e['sha256'])
 repaired=read(R/'research/n3_scaled_calibration_repairs/verification/result.json','000a7199b37137ebb36e2ac3526635908d6439492449dd4b8ab13a0b8144b3de')
 for p,h in repaired['inputs'].items():bind(R/p,h)
 for name in ['legqs_tests.py','legqs_quadcheck.py']:assert sha(B/'source'/name)==sha(R/'research/n3_scaled_calibration_repairs/source'/name)
 assert repaired['small_cases']==810 and repaired['large_cases']==3 and repaired['panel_count']==58 and all(repaired['checks'].values());checks['actual_repaired_source_and_partition_bound']=True
 synthetic=read(R/'research/n3_synthetic_field_audit/verification/result.json','73a0fa76fa2c772c2bd76c3d2d58aafbd481f07ba0699389fb690841e3cd08d4')
 for p,h in synthetic['inputs'].items():bind(R/p,h)
 fixture=read(R/'research/n3_synthetic_field_audit/data/synthetic.json',synthetic['raw_sha256'])
 quad=read(B/'source/legqs_quadcheck_synthetic.json');assert fixture['generators']==quad['candidate'] and len(fixture['generators'])==6 and (quad['panels'],quad['gauss_points'],quad['angular_points'])==(58,20,36);checks['identical_six_generator_fixture_and_rule_counts']=True
 mmax=max(g['m'] for g in fixture['generators']);density_nmax=2*mmax+1;stream_nmax=2*mmax+2;Fbound=density_nmax+stream_nmax
 assert mmax==3 and Fbound==15 and 2*Fbound<36;checks['unaliased_mathematical_angular_rule']=True
 quadrature=[]
 ar=lambda q:arb(Q(q).numerator)/arb(Q(q).denominator)
 def decimal_q(s):
  f=Fraction(s);return Q(f.numerator,f.denominator)
 def enclosing(a,b):
  den=10**30;lo=Q(int((min(a.lower(),b.lower())*den).floor().unique_fmpz())-1,den);hi=Q(int((max(a.upper(),b.upper())*den).ceil().unique_fmpz())+1,den)
  assert ar(lo)<a and ar(lo)<b and a<ar(hi) and b<ar(hi);return [str(lo),str(hi)]
 for label in ['G0','rF']:
  own=next(x for x in synthetic['norms'] if x['label']==label);qrow=quad['results'][label]
  a=arb(own['own_lower_norm']);b=arb(own['own_upper_norm']);c=arb(qrow['norm_t_lower']);d=arb(qrow['norm_t_upper']);assert a.overlaps(b) and a.overlaps(c) and b.overlaps(d)
  Qprinted=ar(decimal_q(qrow['quadrature']));discrepancy=abs(Qprinted-a)/a;assert discrepancy>0 and discrepancy<ar(Q(12,10**17))
  enclosure=enclosing(a,b);assert ar(Q(enclosure[0]))<c and ar(Q(enclosure[0]))<d and c<ar(Q(enclosure[1])) and d<ar(Q(enclosure[1]))
  quadrature.append({'label':label,'recorded_approximation_exact_decimal':qrow['quadrature'],'accepted_norm_containing_ball':a.str(100),'common_norm_enclosure_exact':enclosure,'relative_discrepancy':discrepancy.str(70),'observed_relative_discrepancy_less_than':'3/25000000000000000','printed_norm_balls_overlap':True,'quadrature_error_certificate':False})
 checks['two_quadrature_discrepancies_below1point2e_minus16']=True
 quadsrc=bind(B/'source/legqs_quadcheck.py').read_text();assert 'mpmath.mp.dps = 30' in quadsrc and 'np.polynomial.legendre.leggauss(20)' in quadsrc and 'mpmath.cos(n * th)' in quadsrc and 'mpq(v) ** (ell * dm / 2)' in quadsrc;checks['complete_point_values_are_not_exact_rationals']=True
 base=R/'research/weighted_laplacian_audit';weighted=read(base/'verification/d2.json','85758c4e35b4f3d1e32c11b3bc63bded1b34eb4f7710afdbe7a4eb94d913744f')
 bind(base/'PROOF.md',weighted['proof_sha256']);bind(base/'code/check.py',weighted['code_sha256']);bind(base/'source/T4_d2.json',weighted['source_sha256']);bind(base/'source/T4_d2_2048.json',weighted['peer_result_sha256']);bind(base/'verification/d2_exact_power_groups.json.gz',weighted['exact_power_groups_sha256'])
 cells=read(B/'source/legqs_cells_test_d2.json');cellrows=[]
 for astr in ['0','1']:
  w=next(x for x in weighted['weights'] if x['a']==astr);own=arb(w['weighted_laplacian_norm']);peer=arb(cells[astr]['N_a']);assert own.overlaps(peer)
  ref=ar(decimal_q(cells[astr]['ref_T4_107']));err=abs(own-ref);comparison=bool(err<ar(Q(1,10**12)));assert comparison==cells[astr]['agree']==(astr=='1')
  cellrows.append({'a':astr,'accepted_norm':own.str(100),'saved_N3_norm':peer.str(100),'common_enclosure_exact':enclosing(own,peer),'full_norms_overlap':True,'abbreviated_reference':cells[astr]['ref_T4_107'],'abbreviated_reference_absolute_error':err.str(70),'saved_boolean':cells[astr]['agree'],'reproduced_boolean':comparison})
 checks['both_actual_d2_norms_overlap']=True;checks['N0_false_boolean_explained_by_abbreviation']=True
 log=bind(B/'source/legqs_testA_rerun.out').read_text();assert 'MISMATCH' not in log and '3 scales x 3 classes x 15 i x 6 m: True' in log and 'large-m entries (m = 600, 1800, 2400; i = 23) overlap 2F1: True' in log;checks['actual_repaired_testA_log_reports_pass']=True
 path=bind(R/'research/rational_pole_moments/code/moments.py');bind(R/'research/rational_pole_moments/PROOF.md');spec=importlib.util.spec_from_file_location('n4_repaired_run_moments',path);M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
 cases=repaired['exponent_cases'];assert len(cases)==813;cache={};rows=[];minimum=10**9
 for case in cases:
  a=Q(case['scale']);b=Q(case['exponent']);i=int(case['power']);assert a>0 and b>-1 and i>=0
  key=(a,b);largest=23 if i==23 else 14
  if key not in cache:cache[key]=M.pole_moments(b,a,largest)
  rec=cache[key][i];z=ar(a/(1+a));transformed=ar((1+a)**(-i)/(b+1))*z.hypgeom_2f1(arb(i),arb(1),ar(b+2))
  bits=min(rec.rel_accuracy_bits(),transformed.rel_accuracy_bits());minimum=min(minimum,bits)
  assert rec.is_finite() and transformed.is_finite() and rec.overlaps(transformed) and bits>700,(case,rec,transformed,bits)
  rows.append({'scale':str(a),'b':str(b),'i':i,'recurrence_ball':rec.str(90),'transformed_Euler_ball':transformed.str(90),'overlap':True,'minimum_relative_accuracy_bits':bits})
 assert len(rows)==813;checks['all813_independent_repaired_Euler_instances']=True
 assert all(checks.values()) and all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'checks':checks,'inputs':inputs,'quadrature_comparisons':quadrature,'d2_comparisons':cellrows,'moment_count':len(rows),'moments':rows,'minimum_moment_relative_accuracy_bits':minimum,'elapsed_seconds':time.monotonic()-start,'publisher_code_executed':False,'spatial_quadrature_executed':False,'verdict':'CONFIRMED repaired finite moment cases, source-bound reported runs and numerical comparisons; quadrature rounding/truncation bounds OPEN; actual016 norms outside scope'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'REPAIRED_CALIBRATION',len(checks),'checks',len(inputs),'inputs','813 moments minbits',minimum,'seconds',out['elapsed_seconds'],'sha',sha(p),flush=True)
if __name__=='__main__':main()
