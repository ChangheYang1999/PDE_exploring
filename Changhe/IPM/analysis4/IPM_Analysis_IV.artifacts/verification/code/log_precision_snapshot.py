"""Append-only independent norm/precision audits of rational-log checkpoints."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
from stream_precision_audit import unpack,text
import argparse,gzip,pickle,json,time,math


def main():
    ap=argparse.ArgumentParser();ap.add_argument('tag');ap.add_argument('--select',default='');ap.add_argument('--checkpoint');ap.add_argument('--selected-gzip',action='store_true');a=ap.parse_args()
    start=time.monotonic();ctx.prec=640
    path=Path(a.checkpoint) if a.checkpoint else Path('../a4-num/ckpt')/(a.tag+'.pkl')
    from read_checkpoint_archive import read_bytes
    raw=read_bytes(path)
    digest=sha256(raw).hexdigest();size=len(raw)
    state=pickle.loads(raw);del raw
    assert state['ring']=='arb' and state['prec']==512
    N=max(state['f']);stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    root=Path('research/64_log_precision_updates')
    out=root/'verification'/f'{a.tag}_N{N}_{stamp}';out.mkdir();(out/'sources').mkdir()
    selected={N,N-1}|{int(n) for n in a.select.split(',') if n and int(n)<=N}
    packed={key:{str(n):state[key][n] for n in selected if n in state[key]} for key in ['f','g']}
    selected_raw=(json.dumps(dict(checkpoint_sha256=digest,precision_bits=512,delta=f"{state['A']}/{state['B']}",**packed))+'\n').encode()
    if a.selected_gzip:
        (out/'selected_packed_coefficients.json.gz').write_bytes(gzip.compress(selected_raw,compresslevel=1,mtime=0))
    else:
        (out/'selected_packed_coefficients.json').write_bytes(selected_raw)
    del selected_raw
    records={};l10=arb(10).log()
    for field in ['f','g']:
        maxscale=arb(0);maxnorm=arb(0);maxindividual=arb(0);locscale=None;locnorm=None;locindividual=None
        uncertain=[];uncertain_individual=0;count=0;profiles=[];sums=[];order_precision=[]
        for n,cols in sorted(state[field].items()):
            logs=[];norms=[];details=[]
            order_individual=arb(0);order_location=None;order_uncertain=0;order_count=0
            for q,col in enumerate(cols):
                S,T,M,R=arb(0),arb(0),arb(0),arb(0);ballnorm=arb(0)
                for j,packed_value in enumerate(col):
                    m,r=unpack(packed_value);am=abs(m);S+=am;T+=r;M=max(M,am);R=max(R,r);ballnorm+=abs(arb(m,r));count+=1;order_count+=1
                    if m!=0:
                        relative=r/am
                        if relative>maxindividual:maxindividual,locindividual=relative,[n,q,j]
                        if relative>order_individual:order_individual,order_location=relative,[q,j]
                    elif r!=0:uncertain_individual+=1;order_uncertain+=1
                if M==0:
                    if R!=0:uncertain.append([n,q])
                    scale=normrel=arb(0) if R==0 else None
                else:scale,normrel=R/M,T/S
                if scale is not None and scale>maxscale:maxscale,locscale=scale,[n,q]
                if normrel is not None and normrel>maxnorm:maxnorm,locnorm=normrel,[n,q]
                log=ballnorm.log()/l10 if ballnorm>0 else None
                logs.append(log);norms.append(ballnorm)
                if n in selected:details.append(dict(q=q,norm=text(ballnorm),log10_norm=text(log) if log is not None else None,
                    maximum_scale_relative_radius=text(scale) if scale is not None else None,
                    wiener_scale_relative_radius=text(normrel) if normrel is not None else None))
            order_precision.append(dict(n=n,coefficient_count=order_count,
                maximum_individual_relative_radius=text(order_individual),maximum_location=order_location,
                uncertain_zero_individuals=order_uncertain,
                all_coefficients_resolved=(not order_uncertain and bool(order_individual<1)),
                all_individual_relative_radii_below_1e_minus_6=(not order_uncertain and bool(order_individual<arb('1e-6')))))
            if logs[0] is not None:
                values=[(arb(math.factorial(q)).log()/l10+log-logs[0],q) for q,log in enumerate(logs) if q and log is not None]
                if values:
                    win,q=max(values,key=lambda t:float(t[0].mid()))
                    plain=sum(norms,arb(0));plain_log=plain.log()/l10
                    row=dict(n=n,degree=len(cols)-1,log10_c0=text(logs[0]),log10_plain_norm=text(plain_log),
                        plain_norm_root=text((plain.log()/n).exp()),column_log10_norms=[text(v) if v is not None else None for v in logs],
                        max_factorial_ratio_log10=text(win),winner=q,
                        winner_certified=all(bool(win>v) for v,j in values if j!=q),positive_hump_certified=bool(win>0),
                        all_nonconstant_factorial_columns_smaller=all(bool(v<0) for v,j in values))
                    sums.append(row)
                    if n in selected:profiles.append(dict(**row,columns=details))
            if n%40==0:print(json.dumps(dict(tag=a.tag,field=field,n=n,elapsed_s=time.monotonic()-start)),flush=True)
        records[field]=dict(coefficient_count=count,maximum_column_scale_relative_radius=text(maxscale),maximum_column_scale_location=locscale,
            maximum_wiener_relative_radius=text(maxnorm),maximum_wiener_location=locnorm,
            maximum_individual_relative_radius=text(maxindividual),maximum_individual_location=locindividual,
            uncertain_zero_columns=uncertain,uncertain_zero_individuals=uncertain_individual,
            all_column_scale_radii_below_10_to_minus_20=not uncertain and bool(maxscale<arb('1e-20')) and bool(maxnorm<arb('1e-20')),
            all_order_factorial_comparisons=sums,selected_profiles=profiles,per_order_precision=order_precision)
    last_resolved=0;last_six_digits=0
    per_field={field:{row['n']:row for row in records[field]['per_order_precision']} for field in ['f','g']}
    for n in range(1,N+1):
        if all(per_field[field][n]['all_coefficients_resolved'] for field in ['f','g']) and last_resolved==n-1:last_resolved=n
        if all(per_field[field][n]['all_individual_relative_radii_below_1e_minus_6'] for field in ['f','g']) and last_six_digits==n-1:last_six_digits=n
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
        checkpoint_path=str(path),checkpoint_sha256=digest,checkpoint_bytes=size,maximum_order=N,delta=f"{state['A']}/{state['B']}",
        arithmetic='640-bit Arb with exact dyadic centers and radii',source_precision_bits=512,last_both_field_resolved_prefix=last_resolved,last_both_field_1e_minus_6_prefix=last_six_digits,
        scope='finite precision and norm audit, conditional on correctness of coefficient enclosure recursion',
        actual_elapsed_s=time.monotonic()-start,code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),fields=records)
    (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['log_precision_snapshot.py','stream_precision_audit.py','read_checkpoint_archive.py']:
        (root/'sources'/f'{name}.txt').write_bytes(Path('code',name).read_bytes())
        (out/'sources'/f'{name}.txt').write_bytes(Path('code',name).read_bytes())
    print(json.dumps(dict(result_directory=str(out),maximum_order=N,elapsed_s=result['actual_elapsed_s'],
        brief={k:{kk:vv for kk,vv in v.items() if kk not in ['all_order_factorial_comparisons','selected_profiles','per_order_precision']} for k,v in records.items()}),indent=2))

if __name__=='__main__':main()
