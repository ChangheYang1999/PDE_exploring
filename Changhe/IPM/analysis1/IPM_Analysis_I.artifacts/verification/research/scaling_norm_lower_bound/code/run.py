"""Serial resumable dual-method calculation for exactly the frozen selection."""
from common import *
import argparse,time,resource
import cox_monomial as a,deboor_legendre as b,weights as w

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);ap.add_argument('--resume',action='store_true');ap.add_argument('--max-new-cells',type=int);args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));assert os.getpriority(os.PRIO_PROCESS,0)==19
    if args.tag=='full':accepted_preparation()
    else:source()
    if args.max_new_cells is not None:assert args.max_new_cells>0
    path=E/(args.tag+'_rows.jsonl');rr=rows(args.tag) if args.resume else [];assert args.resume or not path.exists()
    aa,bb,c,ma=input_data();start=now();new=0
    with path.open('a') as out:
        for span in selected(args.tag)[len(rr):]:
            t=time.monotonic();ar=a.compute(*aa,span);br=b.compute(*bb,span);assert ar==br,span
            row={'type':'cell','span':span,'utc':now(),'source_freeze_sha256':sha(E/'source_freeze.json'),'methods':{'cox_monomial':ar,'deboor_legendre':br},'weights':{'arb512':w.cell_arb(ar,c['k'],c['L']),'iv220':w.cell_iv(br,c['k'],c['L'])}}
            verify_row(row,span);out.write(u.canonical(row)+'\n');out.flush();os.fsync(out.fileno());rr.append(row);new+=1
            print(json.dumps({'utc':now(),'span':span,'completed':len(rr),'seconds':time.monotonic()-t,'rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
            if args.max_new_cells is not None and new>=args.max_new_cells:break
    if len(rr)==len(selected(args.tag)):
        result=summarize(args.tag,rr);write(E/(args.tag+'_summary.json'),{'start_utc':start,'utc':now(),**result});print('COMPLETE_COMPUTATION_REQUIRES_AUDIT_AND_ACTUAL_REVIEW',flush=True)
if __name__=='__main__':main()
