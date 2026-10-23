"""Cheap guarded v1/v2 C5 coordinate diagnostics; no candidate correction."""
import argparse
import time

from absolute_common import ROOT,BASE,OUT,np,read,load_case,atomic,npz,digest,provenance
from absolute_chart import constraint_jacobian,hp_report
from absolute_chart_v2 import AbsoluteC5ChartV2
from stage12_chart import chart as historical_chart


def main(args):
    output=OUT/'chart_diagnostics_v2'/(args.label+'.json');artifact=output.with_suffix('.npz')
    if output.exists() or artifact.exists():raise ValueError('Refusing to overwrite chart diagnostics')
    began=time.time();candidate_path=ROOT/'inputs'/(args.case+'.json');case=load_case(args.case)
    p=np.asarray(case.get('core_parameters',[case['cl']]+case['coefficients'][1:]),dtype=float)
    g=constraint_jacobian(p)
    original=historical_chart(p,read(BASE/'results/chart_coefficient_normal.json'))
    normals=np.column_stack((np.eye(24)[:,original.zpair],original.base_geometry['R']@original.e))
    old_normal=np.zeros((24,5));old_normal[1:]=np.linalg.qr(normals[1:],mode='reduced')[0]
    old_system=g@old_normal
    new=AbsoluteC5ChartV2(p)
    projected_original=original.base_tangent-new.normal@np.linalg.solve(g@new.normal,g@original.base_tangent)
    # This map is invertible iff every original feasible direction is retained.
    equivalence=np.linalg.lstsq(new.base_tangent,projected_original,rcond=None)[0]
    eqs=np.linalg.svd(equivalence,compute_uv=False)
    span_error=np.linalg.norm(new.base_tangent@equivalence-projected_original)/max(np.linalg.norm(projected_original),1e-300)
    rank=int(np.linalg.matrix_rank(equivalence))
    diagnostics=new.geometry_diagnostics
    passed=bool(rank==19 and diagnostics['tangent_rank']==19 and diagnostics['complete_24_rank']==24
        and diagnostics['raw_G_normal_condition']<=1e10 and diagnostics['base_HP']['max_abs']<1e-10
        and diagnostics['base_HP']['physical_bounds'] and span_error<1e-10
        and diagnostics['cl_tangent_row_norm']>0)
    arrays={'p':p,'constraint_jacobian':g,'old_normal':old_normal,'old_G_normal':old_system,
        'new_normal':new.normal,'new_tangent':new.base_tangent,
        'original_tangent_seeds':original.base_tangent,'projected_original_tangent':projected_original,
        'original_to_new_coordinates':equivalence,'equivalence_singular_values':eqs,
        'complete_24':new.complete,'row_scales':new.constraint_row_scales}
    npz(artifact,**arrays)
    result={'schema':'absolute_loss_c5_chart_v2_diagnostics_v1','case':args.case,'label':args.label,
        'candidate_path':str(candidate_path),'candidate_sha256':digest(candidate_path),
        'candidate_HP_without_correction':hp_report(p),
        'old_version':'absolute_loss_analytic_center_full19_c5_v1',
        'old_G_normal_singular_values':np.linalg.svd(old_system,compute_uv=False).tolist(),
        'old_G_normal_condition':float(np.linalg.cond(old_system)),
        'old_G_normal_exceeds_unchanged_1e10_condition_limit':bool(np.linalg.cond(old_system)>1e10),
        'new_geometry':diagnostics,'original_to_new_coordinate_singular_values':eqs.tolist(),
        'original_to_new_coordinate_rank':rank,'relative_tangent_span_equivalence_error':float(span_error),
        'all_19_original_feasible_directions_represented':bool(rank==19 and span_error<1e-10),
        'all_5_physical_constraints_unchanged':True,'normal_cl_row_is_exact_zero':bool(np.array_equal(new.normal[0],np.zeros(5))),
        'coefficient_bounds_unchanged':True,'HP_tolerance_unchanged_1e_minus10':True,
        'numerical_singular_pairs_removed':False,'base_candidate_corrected':False,
        'candidate_saved_or_overwritten':False,'optimization_performed':False,
        'source_sha256':{n:digest(ROOT/n) for n in ['absolute_chart_v2.py','chart_diagnostics_v2.py','absolute_chart.py','absolute_fields.py','highprecision_origin.py']},
        'base_manifest_sha256':digest(ROOT/'provenance/base_manifest.json'),
        'arrays_path':str(artifact),'arrays_sha256':digest(artifact),
        'environment':provenance(),'elapsed_seconds':time.time()-began,
        'completed':True,'passed':passed}
    atomic(output,result)
    print(__import__('json').dumps({'path':str(output),'passed':passed,
        'old_condition':result['old_G_normal_condition'],'new_condition':diagnostics['raw_G_normal_condition'],
        'complete_condition':diagnostics['complete_24_condition'],'span_error':float(span_error),
        'equivalence_rank':rank}),flush=True)
    if not passed:raise SystemExit(2)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',required=True,choices=['stage11','combined','local','global']);p.add_argument('--label',required=True)
    a=p.parse_args()
    if '/' in a.label or '\\' in a.label:p.error('Simple label required')
    main(a)
