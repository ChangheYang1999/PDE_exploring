"""Audit completed Q9/Q10 extensions, retaining all exact printed differences."""
from pathlib import Path
from fractions import Fraction as F
import json, time, traceback, sys
sys.dont_write_bytecode=True
from flint import arb, ctx
from certificate_admission import stamp, ref, checkref
from floating_order_doubling_audit import parse, fits, ab, disp
ctx.prec=768
ROOT=Path('research/303_period_nine_ten_floating_extensions')

def main():
    started=time.monotonic(); completed=[]; pending=[]
    for Q,N,count,oldN,topic in [(10,600,14,300,'298_period_ten_floating_audit'),(9,612,10,306,'279_period_nine_floating_audit')]:
        for index in range(1,count+1):
            out=ROOT/'verification'/f'Q{Q}_root{index}.json'
            if out.exists():
                d=json.loads(out.read_text()); assert d['all_checks_pass']
                checkref(d['source']); checkref(d['baseline'])
                completed.append(d); continue
            src=Path('../a4-lead/code/tuned')/f'hhf_Q{Q}h1_root{index}_N{N}_f64.out'
            if not src.exists() or '# done,' not in src.read_text():
                pending.append(dict(Q=Q,root=index)); continue
            raw=src.read_bytes(); assert raw==src.read_bytes()
            dst=ROOT/'sources'/src.name; dst.write_bytes(raw)
            baseline=Path('research')/topic/'sources'/f'hhf_Q{Q}h1_root{index}_N{oldN}_f64.out'
            a=parse(baseline,Q); b=parse(dst,Q)
            assert a['normalized']==b['normalized'],(Q,index,a['normalized'],b['normalized'])
            assert set(a['rows'])<=set(b['rows']) and set(a['tuning'])<=set(b['tuning'])
            norm_differences=[]
            for n,old in a['rows'].items():
                for j,channel in enumerate(['density','stream']):
                    difference=b['rows'][n][j]-old[j]
                    if difference:
                        norm_differences.append(dict(n=n,channel=channel,old=str(old[j]),new=str(b['rows'][n][j]),difference=str(difference)))
            tuning_differences=[]; identical_tuning_rows=0
            for k,old in a['tuning'].items():
                new=b['tuning'][k]
                assert old[0]==new[0] and old[3]==new[3]
                if old==new: identical_tuning_rows+=1
                for j,name in [(1,'R_log'),(2,'sigma'),(4,'H_log')]:
                    if old[j]!=new[j]:
                        tuning_differences.append(dict(k=k,component=name,old=str(old[j]),new=str(new[j]),difference=str(new[j]-old[j])))
            fa=fits(a['rows'],Q); fb=fits(b['rows'],Q)
            oldfits={(r['channel'],r['window_lower']):r for r in fa}; changes=[]
            for r in fb:
                key=(r['channel'],r['window_lower'])
                if key in oldfits:
                    ds=F(r['slope'])-F(oldfits[key]['slope'])
                    change=(ab(ds)*arb(10).log()).exp()-1
                    radius_change=(ab(ds*F(Q,2))*arb(10).log()).exp()-1
                    changes.append(dict(channel=key[0],window_lower=key[1],relative_A_change=disp(change),absolute_relative_A_change=disp(abs(change)),relative_apparent_radius_change=disp(radius_change),absolute_relative_apparent_radius_change=disp(abs(radius_change))))
            d=dict(at=stamp(),all_checks_pass=True,Q=Q,root_index=index,source=ref(dst),baseline=ref(baseline),header=b['header'],announced_order=b['announced_order'],last_printed_order=max(b['rows']),last_complete_block=Q*(max(b['rows'])//Q),baseline_epsilon=a['epsilon'],extended_epsilon=b['epsilon'],printed_norm_overlap_count=2*len(a['rows']),exact_norm_overlap_count=2*len(a['rows'])-len(norm_differences),norm_differences=norm_differences,printed_tuning_overlap_count=len(a['tuning']),exact_tuning_overlap_count=identical_tuning_rows,tuning_differences=tuning_differences,baseline_fits=fa,extended_fits=fb,same_window_changes=changes,scope='Finite statistics of printed rounded-root floating data only; no high-order coefficient enclosure or infinite-tail bound.')
            out.write_text(json.dumps(d,indent=2)+'\n'); completed.append(d)
            print(json.dumps(dict(at=d['at'],Q=Q,root=index,norm_discrepancies=len(norm_differences),tuning_discrepancies=len(tuning_differences))),flush=True)
    largest=[]
    for Q in [9,10]:
        group=[r for r in completed if r['Q']==Q]
        candidates=[(r['root_index'],x) for r in group for x in r['same_window_changes'] if x['channel']=='density']
        if candidates:
            root,x=max(candidates,key=lambda p:float(arb(p[1]['absolute_relative_A_change']).mid()))
            largest.append(dict(Q=Q,completed=len(group),root=root,window_lower=x['window_lower'],absolute_relative_A_change=x['absolute_relative_A_change']))
    result=dict(at=stamp(),all_completed_checks_pass=True,completed=len(completed),pending=pending,checked_sources=[r['source'] for r in completed],max_density_changes=largest,actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification/latest.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'sources/period_nine_ten_extension_audit.py').write_bytes(Path(__file__).read_bytes())
    (ROOT/'sources/reused_floating_fit.py').write_bytes(Path('code/floating_order_doubling_audit.py').read_bytes())
    print(json.dumps(result),flush=True)

if __name__=='__main__':
    try: main()
    except Exception as e:
        failure=dict(at=stamp(),error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(v.filename).name,line=v.lineno) for v in traceback.extract_tb(e.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(json.dumps(failure),flush=True); raise SystemExit(1)
