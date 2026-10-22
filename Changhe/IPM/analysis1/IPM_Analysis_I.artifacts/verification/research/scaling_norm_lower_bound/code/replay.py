"""Regenerate both exact spline paths at fixed and actual maximizing spans."""
from common import *
import argparse,resource,time
import cox_monomial as a,deboor_legendre as b,weights as w

def selected_replay(tag,rr):
    spans=selected(tag)
    if tag=='smoke':return spans
    ans=set(load(E/'input_manifest.json')['smoke_spans'])
    for eng in ['arb512','iv220']:
        for side in ['left','right']:
            ans.add(max(rr,key=lambda z:F(z['weights'][eng][side]['upper_exact']))['span'])
    ans.add(max(rr,key=lambda z:F(z['methods']['cox_monomial']['Q']))['span'])
    return sorted(ans)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));assert os.getpriority(os.PRIO_PROCESS,0)==19
    source();rr=rows(args.tag);assert len(rr)==len(selected(args.tag));lookup={z['span']:z for z in rr};indices=selected_replay(args.tag,rr)
    aa,bb,c,ma=input_data();start=now();results=[]
    for span in indices:
        t=time.monotonic();ar=a.compute(*aa,span);br=b.compute(*bb,span);old=lookup[span]
        assert ar==old['methods']['cox_monomial'] and br==old['methods']['deboor_legendre'] and ar==br
        assert w.cell_arb(ar,c['k'],c['L'])==old['weights']['arb512'] and w.cell_iv(br,c['k'],c['L'])==old['weights']['iv220']
        results.append({'span':span,'seconds':time.monotonic()-t,'Q':ar['Q'],'density_coefficients_sha256':ar['density_coefficients_sha256']})
    write(E/(args.tag+'_replay.json'),{'start_utc':start,'utc':now(),'status':'PASS_EXACT_DUAL_SPLINE_AND_WEIGHT_REPLAY_FIXED_AND_ACTUAL_MAXIMA','tag':args.tag,'source_sha256':sha(Path(__file__)),'rows_sha256':sha(E/(args.tag+'_rows.jsonl')),'indices':indices,'results':results,'density_coefficient_equalities':2088*len(indices)});print(json.dumps({'replay_spans':indices}))
if __name__=='__main__':main()
