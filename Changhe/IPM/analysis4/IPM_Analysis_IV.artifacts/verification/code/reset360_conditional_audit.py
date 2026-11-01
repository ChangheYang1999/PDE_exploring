"""Independent finite diagnostics of the reset continuation through order 360."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import gzip
import json
import math
import os
import pickle
import shutil
import sys
import time
import traceback
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from flint import arb, ctx
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT = Path('research/199_reset360_conditional_audit')


def allocated_bytes():
    seen = set()
    total = 0
    for base, dirs, files in os.walk('.'):
        for name in files:
            p = Path(base, name)
            st = p.stat()
            identity = (st.st_dev, st.st_ino)
            if identity not in seen:
                seen.add(identity)
                total += st.st_blocks * 512
    return total


def main():
    start = time.monotonic()
    ctx.prec = 768
    zero = arb(0)
    lg = arb(10).log()
    text = lambda x: x.str(42, radius=True)
    source = Path('../a4-num/ckpt/log_sin1_c3_from329.pkl')
    raw = source.read_bytes()
    digest = sha256(raw).hexdigest()
    source_size = len(raw)
    state = pickle.loads(raw)
    del raw
    assert (state['A'], state['B'], state['ring'], state['prec']) == ('2', '3', 'arb', 512)
    assert max(state['f']) >= 360
    selected = {key: {n: state[key][n] for n in [358, 359, 360]} for key in ['f', 'g']}
    selected.update(A='2', B='3', ring='arb', prec=512, source_sha256=digest,
                    scope='Conditional on loaded midpoints through 329; inherited uncertainty excluded.')
    raw = pickle.dumps(selected, protocol=4)
    compressed = gzip.compress(raw, compresslevel=6, mtime=0)
    assert allocated_bytes() + len(compressed) < 2990000000
    assert shutil.disk_usage('.').free > 20000000000
    (ROOT / 'verification/selected.pkl.gz').write_bytes(compressed)
    manifest = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                    source=str(source), source_sha256=digest, source_bytes=source_size,
                    source_maximum_order=max(state['f']), selected_orders=[358, 359, 360],
                    selected_raw_sha256=sha256(raw).hexdigest(), selected_raw_bytes=len(raw),
                    archive_sha256=sha256(compressed).hexdigest(), archive_bytes=len(compressed),
                    checkpoint_flags={k: state.get(k) for k in ['radii_reset_at', 'perturbed_seed']})
    (ROOT / 'verification/input_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    del selected, raw, compressed
    table_path = Path('../a4-num/notes/table_511b_351_360.md')
    table = table_path.read_text()
    (ROOT / 'sources/peer_table.md').write_text(table)
    printed = {}
    for line in table.splitlines():
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if cells and cells[0].isdigit():
            printed[int(cells[0])] = cells
    norms, rows = {}, []
    positions = poisson = canonical = comparisons = 0
    for n in range(324, 361):
        decoded, row = {}, dict(n=n, fields={})
        for field in ['f', 'g']:
            cols = [[arb(*unpack(v)) for v in col] for col in state[field][n]]
            decoded[field] = cols
            column = [sum(map(abs, col), zero) for col in cols]
            total = sum(column, zero)
            assert total > 0
            norms[field, n] = total
            positions += sum(map(len, cols))
            facts = [arb(math.factorial(q)) * v for q, v in enumerate(column)]
            win = max(range(len(facts)), key=lambda q: float((facts[q] / column[0]).mid()))
            assert all(facts[win] > v for q, v in enumerate(facts) if q != win)
            row['fields'][field] = dict(norm=pack(total), log10_norm=text(total.log() / lg),
                relative_radius=text(total.rad() / abs(total.mid())), degree=len(cols)-1,
                root=text(total.root(n)), factorial_maximizer=win,
                factorial_log10_ratio=text((facts[win] / column[0]).log() / lg))
        ratio = norms['g', n] / norms['f', n]
        row['log10_N_over_M'] = text(ratio.log() / lg)
        if n >= 358:
            FF, GG = decoded['f'], decoded['g']
            P = arb(2) - arb(2*n) / 3
            def get(A, q, j):
                return A[q][j] if 0 <= q < len(A) and 0 <= j < len(A[q]) else zero
            local, res, scale = 0, zero, zero
            for q in range(max(len(FF), len(GG))):
                assert get(GG, q, 0).is_zero()
                for j in range(1, max(max(map(len, FF)), max(map(len, GG))) + 1):
                    lhs = (4*j*j-P*P)*get(GG,q,j)-2*P*(q+1)*get(GG,q+1,j)-(q+1)*(q+2)*get(GG,q+2,j)
                    rhs = ((P-2*j)*get(FF,q,j-1)+(q+1)*get(FF,q+1,j-1)
                           +(P+2*j)*get(FF,q,j)+(q+1)*get(FF,q+1,j))/2
                    assert (lhs-rhs).contains(0), (n,q,j)
                    res += abs(lhs-rhs)
                    scale += abs(lhs)+abs(rhs)
                    local += 1
                    if q == 0 and 3*(2+2*j) == 2*n:
                        assert get(GG,0,j).is_zero()
                        canonical += 1
            poisson += local
            row['poisson'] = dict(coefficients=local, relative_residual=text(res/scale))
        if n >= 351:
            P3, shifts = 6-2*n, {}
            for col in decoded['g']:
                for j,v in enumerate(col):
                    if j:
                        distance = min(abs(P3+6*j),abs(P3-6*j))
                        key = str(Fraction(distance,3)) if distance <= 12 else 'far'
                        shifts[key] = shifts.get(key,zero)+abs(v)
            row['stream_shares_by_shift'] = {k:text(v/norms['g',n]) for k,v in shifts.items()}
            cells = printed[n]
            for value, cell, tol in [(norms['f',n].log()/lg,cells[2],'0.00051'),
                                     (norms['g',n].log()/lg,cells[4],'0.00051'),
                                     (ratio.log()/lg,cells[5],'0.00051'),
                                     (arb(row['fields']['f']['factorial_log10_ratio']),cells[6].split()[0],'0.0051')]:
                assert value.overlaps(arb(cell,tol)), (n,text(value),cell)
                comparisons += 1
            assert row['fields']['f']['factorial_maximizer'] == int(cells[6].split('(')[1].split(')')[0])
            comparisons += 1
            if cells[3]:
                value = (norms['f',n]/norms['f',n-1]).log()/lg
                assert value.overlaps(arb(cells[3],'0.00051')), (n,text(value),cells[3])
                comparisons += 1
        rows.append(row)
        if n >= 358:
            print(json.dumps(dict(n=n, fields=row['fields'], poisson=row['poisson'])), flush=True)
    slopes = {}
    for b in [350,355,360]:
        center = b-13
        denominator = sum((n-center)**2 for n in range(b-26,b+1))
        slopes[str(b)] = {f:text(sum(((n-center)*norms[f,n].log()/lg for n in range(b-26,b+1)),zero)/denominator)
                          for f in ['f','g']}
    decrements = [dict(n=n, f=text((norms['f',n+3]/norms['f',n]).log()/lg),
                           g=text((norms['g',n+3]/norms['g',n]).log()/lg)) for n in range(324,358)]
    exact_cycle_refuted = not arb(decrements[-1]['f']).overlaps(arb(decrements[-4]['f']))
    assert exact_cycle_refuted
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                  all_checks_pass=True, scope='Conditional finite arithmetic for loaded midpoint continuation; inherited uncertainty excluded.',
                  source_sha256=digest, bits=768, norm_coefficient_positions=positions, poisson_coefficients=poisson,
                  canonical_constants=canonical, printed_comparisons=comparisons, rows=rows,
                  slopes=slopes, three_order_decrements=decrements, exact_finite_cycle_refuted=exact_cycle_refuted,
                  actual_elapsed_s=time.monotonic()-start)
    (ROOT / 'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['reset360_conditional_audit.py','stream_precision_audit.py','certified_initial_majorants.py']:
        (ROOT / 'sources' / name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','three_order_decrements']}),flush=True)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        d = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),type=type(e).__name__,error=str(e),
                 frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(d,indent=2)+'\n')
        print(json.dumps(d),flush=True)
        raise SystemExit(1)
