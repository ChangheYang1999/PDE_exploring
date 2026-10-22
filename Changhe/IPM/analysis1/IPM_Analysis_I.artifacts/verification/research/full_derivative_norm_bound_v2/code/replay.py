"""Fresh complete selected cells and complete two-engine end-tail replay."""
from protocol import *
import argparse,time
from run import cell_result,tail_result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);args=ap.parse_args();tag=args.tag;start=now();tick=time.monotonic();audit=load(OUT/(tag+'_audit.json'));summary=load(OUT/(tag+'_summary.json'));pins,deps,freeze=source()
    assert audit['status']=='PASS_COMPLETE_SAVED_DERIVATIVE_STREAM_AND_EXACT_REDUCTION' and audit['summary_sha256']==sha(OUT/(tag+'_summary.json')) and audit['rows_sha256']==sha(OUT/(tag+'_rows.jsonl'))
    needed=audit['required_replay_cells'];saved={}
    with (OUT/(tag+'_rows.jsonl')).open() as f:
        for line in f:
            z=parse(line)
            if z['type']=='cell' and z['cell'] in needed:saved[z['cell']]=z
    assert sorted(saved)==needed
    refs=radial_rows();d=data();results=[]
    for i in needed:
        fresh=cell_result(d,i,refs[i]);old=saved[i]
        assert {k:v for k,v in fresh.items() if k not in ['utc','seconds']}=={k:v for k,v in old.items() if k not in ['utc','seconds']},('fresh entire cell',i)
        results.append({'cell':i,'all_product_coefficient_equalities':fresh['all_product_coefficient_equalities'],'actual_linear_identity_checks':fresh['actual_linear_identity_checks'],'comparison':'ALL_EXACT_PRODUCTS_AND_ALL_SAVED_BOUND_ENDPOINTS_IDENTICAL'})
        print(canonical({'utc':now(),'replayed_cell':i}),flush=True)
    fresh_tail=tail_result();assert fresh_tail==load(OUT/(tag+'_tails.json')),'complete tail replay'
    rehash(summary['files']);out={'start_utc':start,'utc':now(),'status':'PASS_COMPLETE_SELECTED_DERIVATIVE_CELLS_AND_ALL_TAILS_REPLAY','full_middle':tag=='full','required_cells':needed,'results':results,'tail_weight_pairs':3508,'tail_derivative_equalities':14672+10524,'audit_sha256':sha(OUT/(tag+'_audit.json')),'summary_sha256':sha(OUT/(tag+'_summary.json')),'rows_sha256':sha(OUT/(tag+'_rows.jsonl')),'tails_sha256':sha(OUT/(tag+'_tails.json')),'source_freeze_sha256':sha(OUT/'source_freeze.json'),'seconds':time.monotonic()-tick}
    write(OUT/(tag+'_replay.json'),out);print(canonical(out),flush=True)
if __name__=='__main__':main()
