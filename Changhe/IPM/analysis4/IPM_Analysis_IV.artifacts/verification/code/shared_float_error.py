"""Compare normalized floating twins with retained exact-input norm enclosures."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
ROOT=Path('research/165_shared_float_error')
START=time.monotonic()
def run():
    ctx.prec=512
    def text(v):return v.str(50,radius=True)
    source=Path('research/82_weighted_loss_criterion/verification/plain_update_20261031T101108Z/checks.json')
    checked=json.loads(source.read_text());canonical={r['n']:r for r in checked['rows']}
    datasets=[];dependencies={str(source):dict(sha256=sha256(source.read_bytes()).hexdigest())}
    for tag in ['log23_full_float','log23_full_float_pert']:
        path=Path('../a4-num/logs')/(tag+'.jsonl');raw=path.read_bytes()
        data=[json.loads(line) for line in raw.decode().splitlines()]
        (ROOT/'sources'/(tag+'.jsonl.gz')).write_bytes(gzip.compress(raw,mtime=0))
        dependencies[str(path)]=dict(sha256=sha256(raw).hexdigest(),bytes=len(raw))
        assert data[0]['delta']=='2/3' and data[0]['edge_only_min_ij_le'] is None
        datasets.append((arb(data[0]['f1'][0]),{r['n']:r for r in data if 'n' in r}))
    (a,first),(b,second)=datasets;assert a==1
    rows=[];first_errors={};last=min(max(first),max(second),max(canonical))
    for n in range(1,last+1):
        if n not in first or n not in second or n not in canonical:continue
        output=dict(n=n)
        for label,key in [('M','log10_sum_cols'),('N','log10_sum_gcols')]:
            if key not in first[n] or key not in second[n]:continue
            if first[n][key] is None or second[n][key] is None:continue
            x=arb(str(first[n][key]));y=arb(str(second[n][key]))-n*b.log()/arb(10).log()
            exact=arb(canonical[n]['log10_'+label]);error=x-exact;twin=y-x
            output[label]=dict(exact_log10=text(exact),float_log10=text(x),normalized_twin_log10=text(y),
                               float_error_log10=text(error),normalized_twin_difference_log10=text(twin))
            for bound in ['0.000001','0.01','1','5']:
                tag=label+'_'+bound
                if tag not in first_errors and abs(error)>arb(bound):first_errors[tag]=n
        rows.append(output)
    selected={r['n']:r for r in rows}
    final=selected[300]
    for label in ['M','N']:
        assert abs(arb(final[label]['float_error_log10']))>5
        assert abs(arb(final[label]['normalized_twin_difference_log10']))<arb('0.000001')
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
        all_checks_pass=True,maximum_common_order=last,first_certified_error_exceedances=first_errors,
        counterexample_order=300,source_dependencies=dependencies,rows=rows,
        actual_elapsed_s=time.monotonic()-START,
        scope='Displayed floating values compared with exact-input interval norms; no causal or infinite-order conclusion.')
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'sources/shared_float_error.py').write_bytes(Path('code/shared_float_error.py').read_bytes())
    files={str(p.relative_to(ROOT)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log'}
    (ROOT/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
    print(json.dumps(dict(all_checks_pass=True,last=last,first_errors=first_errors,order300=final,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
    try:run()
    except Exception as exc:
        import traceback
        failure=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(v.filename).name,line=v.lineno) for v in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
