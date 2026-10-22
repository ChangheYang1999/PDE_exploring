"""Freeze current reviewed sources and accepted canonical parent maps."""
from protocol import *
import argparse,subprocess,ast

def main():
    ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['freeze','extract','accept']);args=ap.parse_args()
    if args.stage=='freeze':
        for name in OWN:
            if name.endswith('.py'):ast.parse((DIR/name).read_text())
        pins,deps=parents()
        assert when(load(OUT/'proof_first.json')['utc'])<when(load(OUT/'proof_adjudication.json')['utc'])
        # All current kernel changes must be part of the actual resolved review.
        r=auth(pins,'full_derivative_norm_kernel_resolution','CONFIRM_DERIVATIVE_KERNEL_AND_DIAGNOSTICS_ONLY')
        post(pins,'full_derivative_norm_kernel_resolution',r,'KERNEL_ADJUDICATION')
        write(OUT/'parent_manifest.json',{'utc':now(),'parents':deps,'files':dict(sorted(parents()[0].items()))})
        write(OUT/'source_freeze.json',{'utc':now(),'status':'IMMUTABLE_DERIVATIVE_NORM_SOURCE_BEFORE_SMOKE_AND_FULL','files':dict(sorted({str((DIR/n).relative_to(ROOT)):sha(DIR/n) for n in OWN}.items()))})
        print('SOURCE_AND_CANONICAL_PARENTS_FROZEN',flush=True);return
    p,deps,f=source();s=load(OUT/'smoke_summary.json');a=load(OUT/'smoke_audit.json');r=load(OUT/'smoke_replay.json');tests=load(OUT/'selfcheck.json')
    assert s['status']=='PASS_SIX_CELL_DERIVATIVE_PREPARATION_DIAGNOSTIC_ONLY' and s['cells']==6 and s['full_middle'] is False
    assert a['status']=='PASS_COMPLETE_SAVED_DERIVATIVE_STREAM_AND_EXACT_REDUCTION' and r['status']=='PASS_COMPLETE_SELECTED_DERIVATIVE_CELLS_AND_ALL_TAILS_REPLAY'
    assert a['summary_sha256']==r['summary_sha256']==sha(OUT/'smoke_summary.json') and r['audit_sha256']==sha(OUT/'smoke_audit.json') and r['required_cells']==SMOKE
    assert tests['status']=='PASS_MANUFACTURED_EXACT_FOURIER_JETS_AND_CRT'
    assert tests['counts']=={'manufactured_CRT_products':4,'all_manufactured_real_Fourier_binomial_coefficients':54810,'actual_linear_identity_checks':24044,'injective_support_coordinates':167040}
    ed=load(OUT/'error_diagnostics.json');assert ed['status']=='PASS_NONZERO_RADII_MODEWISE_EXACT_ERRORS_AND_DUAL_ENGINES' and ed['modewise_aggregate_equalities']==34 and ed['actual_linear_identity_checks']==24044 and ed['exact_dV_dW_and_interval_overlap_checks']==28
    for name in ['smoke_summary.json','smoke_audit.json','smoke_replay.json','smoke_tails.json','smoke_rows.jsonl','smoke_restarts.jsonl','selfcheck.json','error_diagnostics.json']:pin(p,OUT/name)
    extract={'status':'EXACT_SIX_CELL_PREPARATION_PROJECTION_ONLY','parents':deps,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'smoke':{k:v for k,v in s.items() if k!='files'},'audit':{k:v for k,v in a.items() if k!='files'},'replay':r,'manufactured':tests,'nonzero_error_diagnostics':load(OUT/'error_diagnostics.json'),'scope':'No complete numerical result. All7809 cells and final actual review remain mandatory.'}
    if args.stage=='extract':write(OUT/'preparation_extract.json',{'utc':now(),**extract});return
    x=load(OUT/'preparation_extract.json');assert {k:v for k,v in x.items() if k!='utc'}==extract;pin(p,OUT/'preparation_extract.json')
    files=load(DIR/'review_files.json')['preparation'];rev=auth(p,'full_derivative_norm_preparation','CONFIRM_FULL_DERIVATIVE_NORM_PREPARATION_ONLY',files,(DIR/'preparation_question.txt').read_text());po=post(p,'full_derivative_norm_preparation',rev,'PREFLIGHT_ADJUDICATION')
    assert when(x['utc'])<when(rev['start_utc']);rehash(p)
    out={'utc':now(),'status':'CONFIRMED_FULL_DERIVATIVE_NORM_PREPARATION_ONLY','parents':deps,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'actual_review':rev,'own_postreview':po,'files':dict(sorted(p.items())),'scope':extract['scope']};write(OUT/'preparation_acceptance.json',out);print(canonical({'utc':out['utc'],'status':out['status'],'pins':len(p),'sha256':sha(OUT/'preparation_acceptance.json')}),flush=True)
if __name__=='__main__':main()
