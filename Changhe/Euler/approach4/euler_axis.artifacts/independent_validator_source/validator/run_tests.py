#!/usr/bin/env python3
"""Run the retained independent tests sequentially in clean processes."""
import datetime,hashlib,json,os,shutil,subprocess,sys,time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CASES=[('test_operators.py','operator_tests.json'),('test_farfield.py','farfield_tests.json'),
       ('test_identities.py','identity_tests.json'),('test_parameter_jvp.py','parameter_jvp_tests.json'),
       ('test_corrected_tail.py','corrected_tail_tests.json'),('test_precision.py','precision_tests.json'),
       ('test_axis_stagnation.py','axis_stagnation_tests.json'),('test_second_order.py','second_order_tests.json'),
       ('test_registered_metrics.py','registered_metric_tests.json'),('test_projection.py','projection_tests.json'),
       ('test_global_moments.py','global_moment_tests.json'),('test_hyperbolic_sources.py','hyperbolic_source_tests.json'),
       ('test_source_curvature.py','source_curvature_tests.json'),('test_weighted_identities.py','weighted_identity_tests.json'),
       ('test_validation_resume.py','validation_resume_tests.json'),
       ('test_global_diagnostics.py','global_diagnostic_tests.json'),
       ('test_s1_formal_jets.py','s1_formal_jet_tests.json'),('test_axis_moments.py','axis_moment_tests.json'),
       ('test_upper_endpoint.py','upper_endpoint_tests.json'),
       ('test_s1_pilot.py','s1_pilot_tests.json'),('test_source_endpoints.py','source_endpoint_tests.json'),
       ('test_s1_constrained.py','s1_constrained_tests.json'),
       ('test_piecewise_adapter.py','piecewise_adapter_tests.json'),
       ('test_interface_pressure.py','interface_pressure_tests.json'),
       ('test_axis_source_chains.py','axis_source_chain_tests.json'),
       ('test_piecewise_projection.py','piecewise_projection_tests.json'),
       ('test_t2_pilot.py','t2_pilot_tests.json'),
       ('test_interface_stream.py','interface_stream_tests.json'),
       ('test_piecewise_balances.py','piecewise_balances_tests.json'),
       ('test_ring_seed_certificate.py','ring_seed_certificate_tests.json'),
       ('test_zero_inventory.py','zero_inventory_tests.json'),
       ('test_ring_seed_field.py','ring_seed_field_tests.json'),
       ('test_ring_axis_identity.py','ring_axis_identity_tests.json'),
       ('test_eta_green_basis.py','eta_green_basis_tests.json'),
       ('test_piecewise_jacobi.py','piecewise_jacobi_tests.json'),
       ('test_t3_equatorial_zero.py','t3_equatorial_zero_tests.json'),
       ('test_t1_source_maximum.py','t1_source_maximum_tests.json'),
       ('test_t3_budgets.py','t3_budgets_tests.json'),
       ('test_t2_green_pilot.py','t2_green_pilot_tests.json'),
       ('test_s1_green_pilot.py','s1_green_pilot_tests.json'),
       ('test_t3_axis_model.py','t3_axis_model_tests.json'),
       ('test_s1_free_c.py','s1_free_c_tests.json'),
       ('test_coefficient_tail.py','coefficient_tail_tests.json'),
       ('test_angular_tail_projection.py','angular_tail_projection_tests.json'),
       ('test_tail_replacement.py','tail_replacement_tests.json'),
       ('test_correction_enrichment.py','correction_enrichment_tests.json'),
       ('test_finite_regularity.py','finite_regularity_tests.json'),
       ('test_slaved_green.py','slaved_green_tests.json'),
       ('test_polynomial_cusp.py','polynomial_cusp_tests.json'),
       ('test_reduced_screen.py','reduced_screen_tests.json'),
       ('test_t1_characteristics.py','t1_characteristic_tests.json'),
       ('test_green_precision.py','green_precision_tests.json'),
       ('test_t1_positive_strain.py','t1_positive_strain_tests.json'),
       ('test_t1_seed_obstruction.py','t1_seed_obstruction_tests.json'),
       ('test_t1_axis_green.py','t1_axis_green_tests.json'),
       ('test_fractional_radial_germs.py','fractional_radial_germ_tests.json'),
       ('test_t3_characteristics.py','t3_characteristic_tests.json'),
       ('test_missing_axis_correction.py','missing_axis_correction_tests.json'),
       ('test_jacobi_projection.py','jacobi_projection_tests.json')]

def main():
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=ROOT/'results'/'test_runs'/stamp;out.mkdir(parents=True)
    env=os.environ.copy()
    for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:env[name]='1'
    env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(ROOT/'src'),MPLBACKEND='Agg',
               MPLCONFIGDIR=str(ROOT/'environment/matplotlib'),XDG_CACHE_HOME=str(ROOT/'environment/cache'),TMPDIR=str(ROOT/'environment/tmp'))
    source_paths=list((ROOT/'src').glob('*.py'))+list((ROOT/'tests').glob('*.py'))+[Path(__file__)]
    source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
    results=[];started=time.time()
    for script,record in CASES:
        old=ROOT/'results'/record
        if old.exists():shutil.copyfile(old,out/('previous_'+record))
        case_start=time.time()
        with (out/(script+'.log')).open('w') as log:
            try:
                run=subprocess.run([sys.executable,str(ROOT/'tests'/script)],cwd=ROOT.parent,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=120,check=False)
                code=run.returncode
            except subprocess.TimeoutExpired:code=124
        if old.exists():shutil.copyfile(old,out/record)
        row={'script':script,'returncode':code,'elapsed_seconds':time.time()-case_start}
        results.append(row);print(json.dumps(row),flush=True)
        if code:break
    result={'started_utc':stamp,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'elapsed_seconds':time.time()-started,'python':sys.version,'executable':sys.executable,
            'source_sha256':source_hashes,'cases':results,'all_passed':len(results)==len(CASES) and all(r['returncode']==0 for r in results)}
    (out/'suite.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'results/latest_test_run.txt').write_text(str(out.relative_to(ROOT))+'\n')
    print(json.dumps({'output':str(out),'all_passed':result['all_passed'],'elapsed_seconds':result['elapsed_seconds']}))
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
