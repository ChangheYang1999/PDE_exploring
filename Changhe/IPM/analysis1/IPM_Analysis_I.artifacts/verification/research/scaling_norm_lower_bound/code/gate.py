"""Source, three-span preparation, and complete1558-span result acceptance."""
from common import *
import argparse,ast,subprocess
import audit as au,replay as rp,selfcheck as sc
STAGES={'workflow':('scaling_lower_workflow','CONFIRM_SCALING_NORM_SOURCE_PENDING_NUMERICAL_COMPUTATION','WORKFLOW_ADJUDICATION','workflow'),'preparation':('scaling_lower_preparation','CONFIRM_THREE_SCALING_NORM_PREPARATION_SPANS_ONLY','PREFLIGHT_ADJUDICATION','smoke'),'actual':('scaling_lower_actual','CONFIRM_COMPLETE_CANONICAL_SCALING_NORM_LOWER_BOUND','POSTREVIEW_ADJUDICATION','full')}

def review(stage):
    tag,expected,stem,kind=STAGES[stage];fs=load(D/'review_files.json')[stage]
    assert len(fs)==len(set(fs)) and not (REV/(tag+'_request.txt')).exists()
    cmd=[sys.executable,'-B',str(REV/'focused_review.py'),'--tag',tag,'--max-tokens','16000','--question',(D/(stage+'_question.txt')).read_text()]
    for n in fs:cmd+=['--file',n]
    raise SystemExit(subprocess.run(cmd,cwd=ROOT,timeout=555).returncode)

def projection(tag):
    p=source();rr=rows(tag);s=load(E/(tag+'_summary.json'));a=load(E/(tag+'_audit.json'));r=load(E/(tag+'_replay.json'))
    assert len(rr)==len(selected(tag))
    assert a['status']=='PASS_COMPLETE_SCALING_NORM_ROWS_WEIGHTS_SUMS_AND_INTEGER_LOWER_ROUNDING' and a['tag']==tag and a['source_sha256']==sha(D/'code/audit.py') and a['counts']==au.audit(tag)
    assert a['rows_sha256']==s['rows_sha256']==r['rows_sha256']==sha(E/(tag+'_rows.jsonl')) and a['summary_sha256']==sha(E/(tag+'_summary.json'))
    assert r['status']=='PASS_EXACT_DUAL_SPLINE_AND_WEIGHT_REPLAY_FIXED_AND_ACTUAL_MAXIMA' and r['tag']==tag and r['source_sha256']==sha(D/'code/replay.py') and r['indices']==rp.selected_replay(tag,rr)
    lookup={z['span']:z for z in rr};assert len(r['results'])==len(r['indices'])
    for z,i in zip(r['results'],r['indices']):
        assert z['span']==i and z['Q']==lookup[i]['methods']['cox_monomial']['Q'] and z['density_coefficients_sha256']==lookup[i]['methods']['cox_monomial']['density_coefficients_sha256']
    assert r['density_coefficient_equalities']==2088*len(r['indices'])
    assert when(load(E/'source_freeze.json')['utc'])<when(s['start_utc'])<=when(s['utc'])<when(a['start_utc'])<=when(a['utc'])<when(r['start_utc'])<=when(r['utc'])
    freeze_time=when(load(E/'source_freeze.json')['utc'])
    assert all(freeze_time<when(z['utc'])<=when(s['utc']) for z in rr)
    if tag=='full':
        prep=load(E/'preparation.json');assert when(prep['utc'])<when(s['start_utc']);accepted_preparation()
        assert all(when(prep['utc'])<when(z['utc']) for z in rr)
    return {'status':'EXACT_ACTUAL_SCALING_NORM_REVIEW_PROJECTION','tag':tag,'source_freeze_sha256':sha(E/'source_freeze.json'),'constants':load(E/'constants.json'),'full_span_count':len(selected('full')),'inherited_pin_count':len(p),'summary':s,'audit':a,'replay':r,'selected_actual_rows':[lookup[i] for i in r['indices']]}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['workflow','freeze','extract_preparation','preparation','accept','extract_actual','actual','finalize']);args=ap.parse_args()
    stage=args.stage
    if stage in ['workflow','preparation','actual']:
        if stage!='workflow':assert (E/('smoke_extract.json' if stage=='preparation' else 'full_extract.json')).exists()
        review(stage)
    if stage=='freeze':
        for n in FIXED:
            if n.endswith('.py'):ast.parse((D/n).read_text())
        p=parents();fs=load(D/'review_files.json')['workflow'];assert len(fs)==len(set(fs)) and {str((D/n).relative_to(ROOT)) for n in FIXED}<=set(fs)
        old=load(E/'selfcheck.json');assert old['source_sha256']==sha(D/'code/selfcheck.py') and old['counts']==sc.run() and old['actual_modal_spans_executed']==0
        tag,expected,stem,kind=STAGES['workflow'];rv=auth(p,tag,expected,fs,(D/'workflow_question.txt').read_text());ad=post(p,tag,rv,stem)
        write(E/'source_freeze.json',{'utc':now(),'status':'IMMUTABLE_SCALING_NORM_SOURCE_BEFORE_ACTUAL_SPANS','manufactured_selfcheck_repeated_counts':old['counts'],'files':dict(sorted({str((D/n).relative_to(ROOT)):sha(D/n) for n in FIXED}.items()))});print('SOURCE_FROZEN_ZERO_ACTUAL_SPANS');return
    tag='smoke' if stage in ['extract_preparation','accept'] else 'full';xp=projection(tag);ep=E/(tag+'_extract.json')
    if stage.startswith('extract_'):write(ep,{'utc':now(),**xp});return
    old=load(ep);assert {k:v for k,v in old.items() if k!='utc'}==xp
    p=source()
    if tag=='full':
        for n,h in accepted_preparation().items():pin(p,n,h)
    for n in ['rows.jsonl','summary.json','audit.json','replay.json','extract.json']:pin(p,E/(tag+'_'+n))
    key='preparation' if tag=='smoke' else 'actual';rt,expected,stem,kind=STAGES[key]
    rv=auth(p,rt,expected,load(D/'review_files.json')[key],(D/(key+'_question.txt')).read_text());ad=post(p,rt,rv,stem);assert when(old['utc'])<when(rv['start_utc'])
    rehash(p);s=xp['summary'];status='ACCEPTED_THREE_SCALING_NORM_PREPARATION_SPANS_ONLY' if tag=='smoke' else 'CONFIRMED_COMPLETE_CANONICAL_SCALING_NORM_LOWER_BOUND'
    v={'utc':now(),'status':status,'cells':s['cells'],'complete_middle':tag=='full','spans':s['spans'],'strict_norm_lower_decimal':s['strict_norm_lower_decimal'],'norm':load(E/'constants.json')['norm'],'canonical_identity_files':load(E/'constants.json')['canonical_identity_files'],'engines':s['engines'],'density_coefficient_equalities':s['density_coefficient_equalities'],'exact_square_integral_equalities':s['exact_square_integral_equalities'],'source_freeze_sha256':sha(E/'source_freeze.json'),'actual_review':rv,'own_postreview':ad,'files':dict(sorted(p.items())),'scope':'Strict whole-plane norm lower bound for K=rho-D rho of the distinguished exact normalized modal trial, obtained from exactly the listed finite annuli. Right-endpoint sum only bounds their union. No whole-plane upper bound, numerical inverse quotient, X3 distance, closure or decisive endpoint.'}
    write(E/('preparation.json' if tag=='smoke' else 'verdict.json'),v);print(json.dumps({k:v[k] for k in ['utc','status','cells','strict_norm_lower_decimal']}))
if __name__=='__main__':main()
