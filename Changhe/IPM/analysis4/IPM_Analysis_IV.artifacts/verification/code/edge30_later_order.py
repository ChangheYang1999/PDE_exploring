"""Extend the independently checked edge30 prefix to a selected later order."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import gzip
import json
import pickle
import shutil
import sys
import time
sys.dont_write_bytecode = True
from flint import arb, arb_poly, fmpq, ctx
from stream_precision_audit import unpack


def pack(x):
    m, e = x.mid().man_exp()
    r, re = x.rad().man_exp()
    return [str(m), int(e), str(r), int(re)]


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--order', type=int, default=300)
    args = parser.parse_args()
    target_order = args.order
    assert 287 <= target_order <= 330
    start = time.monotonic()
    ctx.prec = 768
    root = Path('research/166_edge30_later_order')
    out = root/'verification'
    path = Path('../a4-num/ckpt/log23_edge30_p512.pkl')
    raw = path.read_bytes()
    digest, size = sha256(raw).hexdigest(), len(raw)
    state = pickle.loads(raw)
    del raw
    assert state['ring'] == 'arb' and state['prec'] == 512
    assert state['A'] == '2' and state['B'] == '3'
    assert max(state['f']) >= target_order
    previous_path = Path('research/161_edge30_certified_departure/verification/checks.json')
    previous = json.loads(previous_path.read_text())
    for key, expected in previous['dependency_coefficient_hashes'].items():
        field, index = key.split(':')
        assert sha256(pickle.dumps(state[field][int(index)], protocol=4)).hexdigest() == expected, ('prefix changed', key)
    prefix_checks = len(previous['dependency_coefficient_hashes'])
    log_path = Path('../a4-num/logs/log23_edge30_p512.jsonl')
    log = log_path.read_text()
    headers = [json.loads(line) for line in log.splitlines() if '"tag"' in line]
    assert headers and all(row['edge_only_min_ij_le'] == 30 and row['f1'] == ['1']
                           and row.get('radii_reset_at') is None for row in headers)
    (root/'sources/run_headers.json').write_text(json.dumps(headers,indent=2)+'\n')
    selected = [target_order]
    snapshot = {k:state[k] for k in ['ring','prec','A','B']}
    for field in ['f','g']:
        snapshot[field] = {n:state[field][n] for n in selected}
    selected_raw = pickle.dumps(snapshot, protocol=4)
    compressed = gzip.compress(selected_raw,compresslevel=3,mtime=0)
    used = sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file())
    assert shutil.disk_usage('.').free > 20_000_000_000
    assert used+len(compressed) < 2_997_000_000, ('disk reserve',used,len(compressed))
    frozen = out/'selected_coefficients.pkl.gz'
    frozen.write_bytes(compressed)
    freeze = dict(bytes=len(selected_raw),sha256=sha256(selected_raw).hexdigest(),
                  compressed_bytes=len(compressed),compressed_sha256=sha256(compressed).hexdigest())
    del selected_raw, compressed
    cache = {}
    fingerprints = {}
    zero, log10 = arb(0), arb(10).log()
    text = lambda x:x.str(50,radius=True)

    def load(field,n):
        key = (field,n)
        if key not in cache:
            blob = pickle.dumps(state[field][n],protocol=4)
            fingerprints[f'{field}:{n}'] = sha256(blob).hexdigest()
            cache[key] = [[arb(*unpack(v)) for v in col] for col in state[field][n]]
        return cache[key]

    def get(columns,q,j):
        return columns[q][j] if 0<=q<len(columns) and 0<=j<len(columns[q]) else zero

    first = load('f',1)
    assert len(first)==1 and len(first[0])==1 and first[0][0].contains(1)
    canonical_path = Path('research/82_weighted_loss_criterion/verification/plain_update_20261031T101108Z/checks.json')
    canonical = {row['n']:row for row in json.loads(canonical_path.read_text())['rows']}
    float_path = Path('research/127_amplitude_probe_scope/verification/checks.json')
    floating = {row['n']:row for row in json.loads(float_path.read_text())['rows']}
    rows = []
    poisson_count = 0
    for n in range(target_order-26, target_order+1):
        row = dict(n=n)
        for field,label in [('f','M'),('g','N')]:
            columns = load(field,n)
            norm = sum((abs(x) for col in columns for x in col),zero)
            total_mid, total_rad = zero, zero
            max_individual, unresolved = zero, 0
            for col in state[field][n]:
                for packed in col:
                    mid,rad = unpack(packed)
                    total_mid += abs(mid)
                    total_rad += rad
                    if mid:
                        max_individual = max(max_individual,rad/abs(mid))
                    elif rad:
                        unresolved += 1
            logarithm = norm.log()/log10
            row['log10_'+label] = text(logarithm)
            row[label+'_norm_exact_dyadic'] = pack(norm)
            row[label+'_norm_relative_radius'] = text(total_rad/total_mid)
            row[label+'_max_individual_relative_radius'] = text(max_individual)
            row[label+'_unresolved_zero_midpoints'] = unresolved
            row['edge_minus_full_'+label] = text(logarithm-arb(canonical[n]['log10_'+label]))
            if n in floating:
                float_value = F.from_float(floating[n]['base_log_'+label])
                difference = abs(logarithm-arb(fmpq(str(float_value))))
                row['float_log_error_'+label] = text(difference)
        if n in selected:
            columns_f, columns_g = load('f',n), load('g',n)
            P = arb(2)-arb(2*n)/3
            errnorm, scale = zero,zero
            for q in range(max(len(columns_f),len(columns_g))):
                for j in range(1,n+2):
                    m = 2*j
                    lhs = (m*m-P*P)*get(columns_g,q,j)-2*P*(q+1)*get(columns_g,q+1,j)-(q+1)*(q+2)*get(columns_g,q+2,j)
                    rhs = ((P-m)*get(columns_f,q,j-1)+(q+1)*get(columns_f,q+1,j-1)+(P+m)*get(columns_f,q,j)+(q+1)*get(columns_f,q+1,j))/2
                    residual = lhs-rhs
                    assert residual.contains(0),('Poisson',n,q,m,text(residual))
                    errnorm += abs(residual)
                    scale += abs(lhs)+abs(rhs)
                    poisson_count += 1
            row['poisson_relative_residual'] = text(errnorm/scale)
        rows.append(row)
        if n%10==0:
            print(json.dumps(dict(stage='norms',n=n,elapsed_s=time.monotonic()-start)),flush=True)
    # All comparisons use interval logarithms, including the regression.
    def slope(end,key,source_rows):
        indexed = {r['n']:r for r in source_rows}
        center = end-13
        denominator = sum((i-center)**2 for i in range(end-26,end+1))
        return sum((arb(indexed[i][key])*(i-center) for i in range(end-26,end+1)),zero)/denominator
    slopes = {}
    for label in ['M','N']:
        slopes[label] = dict(edge=text(slope(target_order,'log10_'+label,rows)),
                            full=text(slope(target_order,'log10_'+label,list(canonical.values()))))
    interim = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                   source_checkpoint=str(path),source_sha256=digest,source_bytes=size,
                   source_maximum_order=max(state['f']),selected_orders=selected,
                   selected_archive=freeze,arithmetic_bits=768,rows=rows,
                   poisson_coefficients=poisson_count,slopes_27=slopes, slope_ending_order=target_order,
                   prior_prefix_hash_checks=prefix_checks,
                   prior_check_sha256=sha256(previous_path.read_bytes()).hexdigest(),
                   all_norm_and_poisson_checks_pass=True)
    (out/'norm_checks.json').write_text(json.dumps(interim,indent=2)+'\n')
    print(json.dumps(dict(stage='norms_done',poisson_coefficients=poisson_count,elapsed_s=time.monotonic()-start)),flush=True)

    n = target_order
    stride = 4*n+3
    max_mode = 2*n+1
    derivative_cache = {}

    def derivatives(field,index):
        key = (field,index)
        if key in derivative_cache:
            return derivative_cache[key]
        columns = load(field,index)
        M = 2*index-(field=='f')
        degree = arb(2 if field=='g' else 1)-arb(2*index)/3
        signed = []
        for col in columns:
            a = [zero]*(2*M+1)
            for j,value in enumerate(col):
                m = 2*j+(field=='f')
                if not m:
                    assert value.is_zero()
                else:
                    assert m<=M
                    a[M+m] = value/2
                    a[M-m] = -value/2
            signed.append(a)
        count = len(signed)
        x,y = [zero]*(stride*(count-1)+2*M+3), [zero]*(stride*(count-1)+2*M+3)
        for q,col in enumerate(signed):
            for j,value in enumerate(col):
                m = j-M
                next_value = (q+1)*signed[q+1][j] if q+1<count else zero
                lower = ((degree+m)*value+next_value)/2
                upper = ((degree-m)*value+next_value)/2
                offset = stride*q+j
                x[offset] += lower
                y[offset] += lower
                x[offset+2] += upper
                y[offset+2] -= upper
        answer = arb_poly(x),arb_poly(y),count-1,M+1
        derivative_cache[key] = answer
        return answer

    total = arb_poly([])
    pairs = 0
    largest_degree = 0
    for i in range(1,n):
        j = n-i
        if min(i,j)>30:
            continue
        XG,YG,dg,mg = derivatives('g',i)
        XF,YF,df,mf = derivatives('f',j)
        assert mg+mf==max_mode and 2*(mg+mf)<stride
        total += XG*YF-YG*XF
        largest_degree = max(largest_degree,dg+df)
        pairs += 1
        if pairs%10==0:
            print(json.dumps(dict(stage='Cartesian',ordered_pairs=pairs,elapsed_s=time.monotonic()-start)),flush=True)
    assert pairs==60
    columns = load('f',n)
    degree = max(largest_degree,len(columns)-1)
    checks,errnorm,scale = 0,zero,zero
    for q in range(degree+1):
        for offset in range(stride):
            m = offset-max_mode
            if m and abs(m)%2:
                index = (abs(m)-1)//2
                target = (2*(n-1)*get(columns,q,index)-3*(q+1)*get(columns,q+1,index))/2
                if m<0:
                    target = -target
            else:
                target = zero
            actual = total[stride*q+offset]
            residual = actual-target
            assert residual.contains(0),('Cartesian forcing',q,m,text(residual))
            errnorm += abs(residual)
            scale += abs(actual)+abs(target)
            checks += 1
    interim.update(cartesian_order=n,cartesian_ordered_pairs=pairs,
                   cartesian_coefficient_checks=checks,
                   cartesian_relative_residual=text(errnorm/scale),
                   dependency_coefficient_hashes=fingerprints,
                   dependency_hash_format='SHA256 of pickle.dumps(coefficient_columns,protocol=4)',
                   all_cartesian_checks_pass=True,
                   canonical_norm_source=str(canonical_path),canonical_norm_sha256=sha256(canonical_path.read_bytes()).hexdigest(),
                   float_source=str(float_path),float_source_sha256=sha256(float_path.read_bytes()).hexdigest(),
                   actual_elapsed_s=time.monotonic()-start,
                   scope='Finite interval norm bounds and differential consistency; no infinite growth law.')
    (out/'checks.json').write_text(json.dumps(interim,indent=2)+'\n')
    for name in ['edge30_later_order.py','stream_precision_audit.py']:
        (root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    for name in ['logff.py','ffcore.py']:
        (root/'sources'/('peer_'+name)).write_bytes(Path('../a4-num/code',name).read_bytes())
    print(json.dumps(dict(all_checks_pass=True,cartesian_coefficients=checks,actual_elapsed_s=interim['actual_elapsed_s'])),flush=True)


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        import traceback
        failure = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                       error_type=type(exc).__name__,error=str(exc),
                       frames=[dict(file=Path(f.filename).name,line=f.lineno)
                               for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/166_edge30_later_order/verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(json.dumps(failure),flush=True)
        raise SystemExit(1)
