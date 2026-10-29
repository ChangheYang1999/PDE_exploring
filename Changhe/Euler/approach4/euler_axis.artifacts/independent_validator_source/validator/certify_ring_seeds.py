#!/usr/bin/env python3
"""Propose and independently recheck finite rational positivity certificates."""
import argparse,datetime,json,time
from pathlib import Path
from fractions import Fraction as F
from ring_seed_certificate import load_exact,parameters,power_bound_valid,cell_lower_bound,check_case
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parent

def power_pair(y,p):
    guess=float(y)**(-float(p))
    for eps in [1e-13,1e-12,1e-10,1e-8]:
        lo=F(str(guess*(1-eps)));hi=F(str(guess*(1+eps)))
        if power_bound_valid(lo,y,p,True) and power_bound_valid(hi,y,p,False):return lo,hi
    raise RuntimeError('could not propose a certified power enclosure')

def build(row):
    c,A,B,b,a,n,p=parameters(row);cutoff=F(1)
    while (cutoff/a)**n<4*B*(n-1)/c:cutoff*=2
    todo=[(F(0),cutoff,0)];cells=[]
    while todo:
        l,h,depth=todo.pop();lo,hi=power_pair(1+(h/b)**3,p)
        lower=cell_lower_bound(row,l,h,lo)
        if lower>0:cells.append(dict(left=str(l),right=str(h),power_lower=str(lo)))
        else:
            if depth>=28:raise RuntimeError('positive cell bound not resolved')
            m=(l+h)/2;todo.extend([(m,h,depth+1),(l,m,depth+1)])
    # Existing float fits need only a narrow, rigorously checked root bracket.
    delta=F(1,10**8);l,h=1-delta,1+delta
    ll,lh=power_pair(1+(l/b)**3,p);hl,hh=power_pair(1+(h/b)**3,p)
    cert=dict(cutoff=str(cutoff),cells=cells,root_bracket=dict(left=str(l),right=str(h),left_power_lower=str(ll),left_power_upper=str(lh),right_power_lower=str(hl),right_power_upper=str(hh)))
    return cert

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('outside lane')
    if out.exists():raise FileExistsError('retain certificates')
    out.mkdir(parents=True);start=time.perf_counter();cpu=time.process_time();rows=load_exact(a.input);results=[]
    for i,row in enumerate(rows):
        cert=build(row);path=out/f'case_{i:03d}.json';atomic_json(path,cert)
        # Reopen the artifact. The checker has no floating-point positivity decision.
        checked=check_case(row,json.loads(path.read_text()))
        checked.update(index=i,c_l=str(row['c']),K=str(row['K']),certificate_sha256=sha256(path));results.append(checked)
        print(i,float(row['c']),float(row['K']),checked['cells'],checked['minimum_certified_H_lower_float'],flush=True)
    report=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),input_sha256=sha256(a.input),
                checker_sha256=sha256(ROOT/'src/ring_seed_certificate.py'),generator_sha256=sha256(Path(__file__)),
                elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,all_passed=True,rows=results)
    atomic_json(out/'summary.json',report)
if __name__=='__main__':main()
