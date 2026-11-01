"""Independent finite Cartesian enclosures for the four delta=3/5 roots."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, gzip, json, os, pickle, shutil, sys, time, traceback
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from flint import arb, ctx
from pure_cartesian_ball import Tuning, refine_root
from pure_chi_three_fifths import reconstruct
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT = Path('research/202_three_fifths_numerical_audit')


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def put(path, data):
    temporary = path.with_name(path.name + '.new')
    temporary.write_text(json.dumps(data, indent=2) + '\n')
    temporary.replace(path)


def allocated():
    seen = set()
    total = 0
    for base, dirs, names in os.walk('.'):
        for name in names:
            p = Path(base, name)
            s = p.stat()
            identity = (s.st_dev, s.st_ino)
            if identity not in seen:
                total += s.st_blocks * 512
                seen.add(identity)
    return total


def one(index, N, bits):
    start = time.monotonic()
    ctx.prec = bits
    input_path = Path('research/200_three_fifths_tuning/verification/obstruction_checks.json')
    data = json.loads(input_path.read_text())
    assert data['all_checks_pass'] and data['obstruction_exactly_matches']
    b, interval = refine_root(data['primitive_coefficients'], data['real_roots'][index-1]['interval'], bits+64)
    path = Path('../a4-num/ckpt') / f'tuned35_r{index}_p1024.pkl'
    raw = path.read_bytes()
    source = dict(path=str(path), sha256=sha256(raw).hexdigest(), bytes=len(raw))
    state = pickle.loads(raw)
    del raw
    assert state['ring'] == 'arb' and state['prec'] == 1024
    assert str(state['delta_exact']) == '3/5'
    maxN = max(state['f'])
    assert maxN >= N+10
    hp = path.with_name(path.stem+'_H.json')
    hraw = hp.read_bytes()
    hd = json.loads(hraw)
    assert hd['period'] == 10 and hd['delta'] == '3/5'
    assert arb(*unpack(state['f'][1][0])) == 1
    assert arb(*unpack(state['f'][1][1])).contains(b)
    source.update(maximum_order=maxN, harmonics_path=str(hp), harmonics_sha256=sha256(hraw).hexdigest())
    solver = Tuning(3, 10, 4)
    def progress(n, H, S):
        print(json.dumps(dict(checked_at_utc=stamp(), root=index, tuned_order=n, actual_elapsed_s=time.monotonic()-start)), flush=True)
    f, g, hs = solver.prefix(b, N, progress)
    counts = dict(f=0, g=0)
    for field, series, odd in [('f', f, True), ('g', g, False)]:
        for n in range(1, N+1):
            for j, packed in enumerate(state[field][n]):
                mode = 2*j+int(odd)
                own = series[n].sine(mode) if mode else arb(0)
                original = arb(*unpack(packed))
                assert own.overlaps(original), ('coefficient', field, n, mode)
                counts[field] += 1
            for mode in range(2*len(state[field][n])+int(odd), 4*n+1, 2):
                assert series[n].sine(mode).contains(0)
    harmonics = []
    for row in hs:
        n = row['n']
        assert row['H'].overlaps(arb(hd['H'][str(n)]['str']))
        assert row['sigma'].overlaps(arb(hd['sigma'][str(n)]))
        harmonics.append(dict(n=n, H=pack(row['H']), sigma=pack(row['sigma']), obstruction=pack(row['obstruction'])))
    norms = []
    potential_counts = dict(density=0, stream=0, resonant_coordinate=0)
    for n in range(1, N+1):
        potential, potential_norm, checked = reconstruct(n, f[n], g[n])
        for key, value in checked.items():
            potential_counts[key] += value
        norms.append(dict(n=n, F=pack(f[n].norm()), G=pack(g[n].norm()), C=pack(potential_norm)))
    samples = sorted({N, maxN} | {n for n in [100, 200, 300] if n <= maxN})
    source_norms = []
    for n in samples:
        row = dict(n=n)
        for field, label in [('f', 'F'), ('g', 'G')]:
            if field == 'g' and n % 10 == 0 and str(n) not in hd['H']:
                row['G_status'] = 'untuned final harmonic; excluded'
                continue
            values = [arb(*unpack(v)) for v in state[field][n]]
            norm = sum(map(abs, values), arb(0))
            mid = sum((abs(v.mid()) for v in values), arb(0))
            rad = sum((v.rad() for v in values), arb(0))
            assert norm > 0
            row[label+'_norm'] = pack(norm)
            row[label+'_root'] = (norm.log()/n).exp().str(50, radius=True)
            row[label+'_relative_radius'] = (rad/mid).str(40, radius=True)
        source_norms.append(row)
    selected = sorted(set(range(1, N+1)) | set(samples))
    payload = pickle.dumps({key: {n: state[key][n] for n in selected} for key in ['f', 'g']}, protocol=4)
    compressed = gzip.compress(payload, compresslevel=6, mtime=0)
    assert allocated()+len(compressed) < 2_994_000_000 and shutil.disk_usage('.').free > 20_000_000_000
    archive = ROOT/'verification'/f'root{index}_selected.pkl.gz'
    assert not archive.exists(), 'Preserve earlier successful archive; use a new version for a rerun.'
    archive.write_bytes(compressed)
    source.update(archive=str(archive), archive_sha256=sha256(compressed).hexdigest(), archive_bytes=len(compressed), selected_sha256=sha256(payload).hexdigest(), selected_orders=selected)
    result = dict(checked_at_utc=stamp(), all_checks_pass=True, root_index=index, root_interval=interval, bits=bits,
        independent_maximum_order=N, source=source, inputs={str(input_path):sha256(input_path.read_bytes()).hexdigest()},
        counts=solver.counts, coefficient_comparisons=counts, potential_identity_counts=potential_counts, harmonics=harmonics, independent_norms=norms,
        source_norms=source_norms, actual_elapsed_s=time.monotonic()-start)
    put(ROOT/'verification'/f'root{index}_checks.json', result)
    print(json.dumps({key:result[key] for key in ['checked_at_utc','root_index','counts','coefficient_comparisons','actual_elapsed_s']}), flush=True)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--roots', default='4')
    ap.add_argument('--N', type=int, default=40)
    ap.add_argument('--bits', type=int, default=2048)
    args = ap.parse_args()
    for index in map(int, args.roots.split(',')):
        try:
            one(index, args.N, args.bits)
        except Exception as exc:
            record = dict(checked_at_utc=stamp(), root=index, error_type=type(exc).__name__, error=str(exc),
                frames=[dict(file=Path(f.filename).name, line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            put(ROOT/'verification'/f'root{index}_FAILURE.json', record)
            print(json.dumps(record), flush=True)
            raise SystemExit(1)
    for name in ['three_fifths_numerical_audit.py','pure_cartesian_ball.py','pure_chi_three_fifths.py','stream_precision_audit.py','certified_initial_majorants.py']:
        (ROOT/'sources'/name).write_bytes(Path('code', name).read_bytes())
    for name in ['tuned_general.py','tuned_c3.py','tuned_cQ.py','ffcore.py']:
        (ROOT/'sources'/('numerical_'+name)).write_bytes(Path('../a4-num/code', name).read_bytes())


if __name__ == '__main__':
    main()
