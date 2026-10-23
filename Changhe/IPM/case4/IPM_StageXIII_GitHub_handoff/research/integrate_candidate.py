"""One immutable candidate/dilation integral per guarded invocation."""
import argparse
from log_integral import *


def main(a):
    path=OUT/'integrals'/(a.label+'.json')
    if path.exists():raise ValueError('Refusing to overwrite an integration record')
    case=load_case(a.case);model=prepare_candidate(case,'center_chart')
    literal=prepare_candidate(case,'literal')
    from highprecision_origin import residual_series
    zero=residual_series(literal,order=6)['constant']
    value,vectors=integrate(model,a.dilation)
    array_path=path.with_suffix('.npz');npz(array_path,**vectors)
    value.update(schema='absolute-loss-candidate-integral-v1',case=a.case,label=a.label,
        candidate_sha256=digest(ROOT/'inputs'/(a.case+'.json')),center_metadata=model['metadata'],
        literal_origin_residual_constant=zero,
        literal_saved_profile_J_abs='infinite_due_nonzero_origin_constant' if float(zero)!=0 else 'not_diagnosed_divergent',
        interpretation='All independent old coefficients, cl and extras fixed; implicit center coefficient is defined by the exact original center equation. No fit or candidate overwrite.',
        original_fixed_domain_J=case.get('objectives',{}).get('J_joint'),
        source_identity=sources(),native_environment=provenance(),array_path=str(array_path),arrays_sha256=digest(array_path),optimization_performed=False)
    atomic(path,value);print(json.dumps({k:value[k] for k in ['case','dilation','J_abs_estimate','total_error_diagnostic','numerical_error_checks_passed','seconds']}),flush=True)
    if not value['numerical_error_checks_passed']:raise SystemExit(2)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--case',choices=['stage11','combined','local','global'],required=True);p.add_argument('--label',required=True);p.add_argument('--dilation',type=float,default=1.);a=p.parse_args()
    from threadpoolctl import threadpool_limits
    with threadpool_limits(limits=1):main(a)
