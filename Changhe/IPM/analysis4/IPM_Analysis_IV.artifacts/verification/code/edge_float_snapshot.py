"""Immutable diagnostics for peer edge recurrences; no rigorous tail inference."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
from hashlib import sha256
import argparse, gzip, json, pickle, math, time

def run(K):
    start=time.monotonic(); root=Path('research/102_edge_recurrence_reference')
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    out=root/'verification'/f'float_edge{K}_{stamp}';out.mkdir()
    source=Path(f'../a4-num/ckpt/log23_edge{K}_float.pkl')
    raw=source.read_bytes();digest=sha256(raw).hexdigest();d=pickle.loads(raw)
    (out/'input_checkpoint.pkl.gz').write_bytes(gzip.compress(raw,compresslevel=3,mtime=0))
    assert (d['ring'],d['A'],d['B'])==('float','2','3')
    refpath=root/'verification/exact_reference.json';ref=json.loads(refpath.read_text())['variants'][str(K)]['rows']
    checks=0;maxerror=Fraction(0);maxloc=None;zero_mismatches=[]
    for row in ref:
        n=row['n']
        for field,name in [('f','density'),('g','stream')]:
            exact={(int(q),int(m)):Fraction(v) for q,c in row[name].items() for m,v in c.items()}
            approx={(q,2*j+(field=='f')):Fraction.from_float(float(v)) for q,c in enumerate(d[field][n]) for j,v in enumerate(c)}
            norm=Fraction(row[name+'_plain_norm'])
            for key in set(exact)|set(approx):
                x=exact.get(key,Fraction(0));y=approx.get(key,Fraction(0));checks+=1
                e=abs(x-y)/norm
                if e>maxerror:maxerror,maxloc=e,[field,n,*key]
                if not x and y:zero_mismatches.append([field,n,*key,str(y)])
    rows=[];subnormals=0;nonfinite=0;staterror=0
    for n in sorted(d['f']):
        rec=dict(n=n)
        for field,name,stkey in [('f','density','log10_sum_cols'),('g','stream','log10_sum_gcols')]:
            cols=[]
            for c in d[field][n]:
                vals=[float(v) for v in c]
                nonfinite+=sum(not math.isfinite(v) for v in vals)
                subnormals+=sum(0<abs(v)<float.fromhex('0x1p-1022') for v in vals)
                cols.append(math.fsum(map(abs,vals)))
            norm=math.fsum(cols);log=math.log10(norm)
            # Difference of logarithms avoids underflow in the column ratio itself.
            vals=[(math.lgamma(q+1)/math.log(10)+math.log10(v)-math.log10(cols[0]),q) for q,v in enumerate(cols) if q and v]
            rec[name]=dict(log10_plain_norm=log,root=10**(log/n),retained_degree=max(q for q,v in enumerate(cols) if v),
                retained_factorial_max=max(vals)[0] if vals else None,retained_factorial_argmax=max(vals)[1] if vals else None)
            st=d['stats'][n].get(stkey)
            if st is not None:staterror=max(staterror,abs(log-st))
        rec['log10_N_over_M']=rec['stream']['log10_plain_norm']-rec['density']['log10_plain_norm'];rows.append(rec)
    lookup={r['n']:r for r in rows};N=max(lookup);slopes={}
    for n in sorted({100,150,200,250,300,N}):
        if n not in lookup or n<27:continue
        mid=n-13;xs=range(n-26,n+1)
        slopes[str(n)]={name:math.fsum((i-mid)*lookup[i][name]['log10_plain_norm'] for i in xs)/math.fsum((i-mid)**2 for i in xs) for name in ['density','stream']}
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),K=K,N=N,source_path=str(source),source_sha256=digest,
        source_bytes=len(raw),exact_reference_sha256=sha256(refpath.read_bytes()).hexdigest(),exact_orders=len(ref),exact_coefficient_checks=checks,
        maximum_error_over_order_norm=float(maxerror),maximum_error_location=maxloc,exact_zero_mismatches=zero_mismatches,
        nonfinite_values=nonfinite,subnormal_nonzero_values=subnormals,max_stored_log_stat_difference=staterror,slopes_27=slopes,
        selected_rows=[lookup[n] for n in sorted({100,150,200,250,300,N}) if n in lookup],
        scope='Finite floating diagnostics. Missing columns may affect factorial maxima; neither tails nor numerical error are certified.',actual_elapsed_s=time.monotonic()-start)
    (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');(out/'all_rows.json').write_text(json.dumps(rows,indent=2)+'\n')
    (out/'source.py.txt').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(dict(output=str(out),**result)),flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('K',type=int,nargs='+');a=ap.parse_args()
    for K in a.K:run(K)
