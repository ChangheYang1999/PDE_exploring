"""Guarded literal-versus-center-defined candidate diagnostics; no correction."""
import argparse
from decimal import Decimal, localcontext
import json
import time

from absolute_common import ROOT,OUT,A_REF,read,atomic,digest,provenance
from absolute_chart import hp_report
from absolute_fields import prepare_candidate
from highprecision_origin import residual_series


def run(args):
    output=OUT/(args.label+'.json')
    if output.exists():raise ValueError('Refusing to overwrite candidate semantics diagnostics')
    start=time.time();rows={}
    index=read(ROOT/'inputs/candidates.json')
    keys=[('constant',0,0),('Ex',2,0),('Ey',0,2),('D1',4,0),('D2',2,2),('D3',0,4)]
    for name,record in index['candidates'].items():
        path=ROOT/'inputs'/(name+'.json');case=read(path)
        literal=prepare_candidate(case,'literal')
        center=prepare_candidate(case,'center_chart')
        p=center['parameters'];report=hp_report(p)
        interpretations={}
        for convention,prepared in [('literal',literal),('center_chart',center)]:
            series=residual_series(prepared,order=8,precision=90)
            coefficients={label:str(series['residual'].get((i,j),Decimal(0))) for label,i,j in keys}
            with localcontext() as ctx:
                ctx.prec=90
                zero=Decimal(coefficients['constant'])
                exact_center=prepared['center_metadata']['literal_center_defect'] if convention=='literal' else '0'
                if convention=='literal':
                    from highprecision_origin import field_series
                    field=field_series(prepared,order=8,precision=90)['fields']
                    a0=field['f'].get((0,0),Decimal(0))
                else:a0=Decimal(report['jets']['a'])
                interpretations[convention]={
                    'physical_residual_Taylor_coefficients_decimal':coefficients,
                    'physical_Rf_at_origin_decimal':str(zero),
                    'physical_center_identity_defect_decimal':exact_center,
                    'a0_decimal':str(a0),
                    'physical_Rf_C5_max_abs':float(max(abs(Decimal(coefficients[k])) for k in ('Ex','Ey','D1','D2','D3'))),
                    'literal_whole_log_radius_integral_diverges_at_origin':bool(zero!=0),
                    'literal_divergence_reason':('A nonzero constant Rf gives a nonintegrable constant in ds as s approaches minus infinity.' if zero else None),
                    'center_metadata':prepared['center_metadata']}
        rows[name]={'candidate_path':str(path),'candidate_sha256':digest(path),
            'source_snapshot_sha256':record['source_sha256'],
            'cl':float(p[0]),'independent_core_parameters':p.tolist(),
            'new_mode_count':len(center['modes']),
            'all_saved_core_free_and_extra_coefficients_preserved':True,
            'candidate_repaired_refitted_or_overwritten':False,
            'center_chart_independent_C5_report':report,
            'center_chart_C5_passes_historical_1e_minus10_tolerance':bool(report['max_abs']<1e-10),
            'center_chart_all_C5_physical_residual_coefficients_pass_1e_minus10':bool(interpretations['center_chart']['physical_Rf_C5_max_abs']<1e-10),
            'original_physical_parameter_bounds_pass':report['physical_bounds'],
            'original_saved_HP_if_present':case.get('core_HP'),
            'interpretations':interpretations}
        atomic(output,{'schema':'absolute_loss_candidate_semantics_v1','completed':False,'candidates':rows})
    result={'schema':'absolute_loss_candidate_semantics_v1','completed':True,
        'a_ref':A_REF,'reference_amplitude_fixed':True,'candidates':rows,
        'source_sha256':{name:digest(ROOT/name) for name in ['candidate_semantics.py','absolute_chart.py','absolute_fields.py','highprecision_origin.py']},
        'base_manifest_sha256':digest(ROOT/'provenance/base_manifest.json'),
        'candidate_index_sha256':digest(ROOT/'inputs/candidates.json'),
        'environment':provenance(),'elapsed_seconds':time.time()-start,
        'optimization_performed':False,'saved_candidates_modified':False,
        'diagnostic_completed_not_feasibility_acceptance':True}
    atomic(output,result)
    print(json.dumps({'path':str(output),'completed':True,
        'center_C5_max':{k:v['center_chart_independent_C5_report']['max_abs'] for k,v in rows.items()},
        'all_literal_origin_diverge':all(v['interpretations']['literal']['literal_whole_log_radius_integral_diverges_at_origin'] for v in rows.values())}),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--label',default='candidate_semantics')
    args=parser.parse_args()
    if '/' in args.label or '\\' in args.label:parser.error('Simple output label required')
    run(args)


if __name__=='__main__':main()
