"""Independent two-continuation Cartesian audit of numerical four-ninths prefixes."""
from pathlib import Path
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
from flint import arb, ctx
from pure_cartesian_ball import Tuning, refine_root
from stream_precision_audit import unpack


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--roots', default='5')
    parser.add_argument('--N', type=int, default=90)
    parser.add_argument('--bits', type=int, default=1536)
    args = parser.parse_args()
    assert args.N >= 36 and args.N <= 150
    ctx.prec = args.bits
    start = time.monotonic()
    root = Path('research/167_four_ninths_finite_audit')
    certificate_path = Path('research/146_four_ninths_profiles/verification/algebraic_certificates.json')
    certificate_raw = certificate_path.read_bytes()
    certificate = json.loads(certificate_raw)
    polynomial = list(map(int, certificate['primitive_coefficients']))
    source_poly_path = Path('../a4-num/notes/tuned49_poly.json')
    source_poly_raw = source_poly_path.read_bytes()
    assert list(map(int, json.loads(source_poly_raw)['coeffs_ascending'])) == polynomial
    text = lambda x: x.str(65, radius=True)
    for index in map(int, args.roots.split(',')):
        root_start = time.monotonic()
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        out = root/'verification'/f'root{index}_{stamp}'
        out.mkdir()
        source_path = Path(f'../a4-num/ckpt/tuned49_r{index}_p1024.pkl')
        raw = source_path.read_bytes()
        source_sha, source_size = sha256(raw).hexdigest(), len(raw)
        state = pickle.loads(raw)
        del raw
        sourceN = max(state['f'])
        assert state['ring'] == 'arb' and state['prec'] == 1024
        assert str(state['delta_exact']) == '4/9'
        assert sourceN >= args.N+9, ('open final resonance', sourceN, args.N)
        hpath = source_path.with_name(source_path.stem+'_H.json')
        hraw = hpath.read_bytes()
        hdata = json.loads(hraw)
        assert hdata['delta'] == '4/9' and hdata['period'] == 9
        assert all(str(n) in hdata['H'] for n in range(9,args.N+1,9))
        b, interval = refine_root(polynomial, certificate['real_roots'][index-1]['interval'], args.bits+64)
        assert arb(*unpack(state['f'][1][0])) == 1
        assert arb(*unpack(state['f'][1][1])).contains(b)
        source_selected = {key:{n:state[key][n] for n in range(1,args.N+1)} for key in ['f','g']}
        packed = pickle.dumps(source_selected, protocol=4)
        archive = gzip.compress(packed, compresslevel=6, mtime=0)
        used = sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file())
        assert shutil.disk_usage('.').free > 20_000_000_000
        assert used+len(archive) < 2_992_000_000, ('disk reserve',used,len(archive))
        archive_hash=sha256(archive).hexdigest()
        existing=next((p for p in (root/'verification').glob('root*/*selected_source.pkl.gz') if sha256(p.read_bytes()).hexdigest()==archive_hash),None)
        archive_path=existing if existing is not None else out/'selected_source.pkl.gz'
        if existing is None:archive_path.write_bytes(archive)
        else:(out/'selected_source_reference.json').write_text(json.dumps({'archive':str(archive_path.relative_to(root)),'sha256':archive_hash},indent=2)+'\n')
        source_info = dict(path=str(source_path), sha256=source_sha, bytes=source_size,
            source_maximum_order=sourceN, selected_maximum_order=args.N,
            selected_uncompressed_sha256=sha256(packed).hexdigest(),
            selected_uncompressed_bytes=len(packed), archive_sha256=sha256(archive).hexdigest(),
            archive_bytes=len(archive), archive_path=str(archive_path.relative_to(root)), selection_rule='source maximum at least nine above selected maximum',
            harmonic_source_sha256=sha256(hraw).hexdigest())
        del packed, archive, state
        selected_h = {key:{n:v for n,v in hdata[key].items() if int(n)<=args.N}
                      for key in ['H','sigma','R_k','obstruction']}
        (out/'source_harmonics.json').write_text(json.dumps(selected_h,indent=2)+'\n')
        solver = Tuning(2,9)
        def progress(n,H,S):
            print(json.dumps(dict(root=index,n=n,H=text(H),sigma=text(S),
                                  actual_elapsed_s=time.monotonic()-root_start)),flush=True)
        f,g,harmonics = solver.prefix(b,args.N,progress)
        comparisons = []
        exact_coefficients = {}
        for key,series,odd in [('f',f,True),('g',g,False)]:
            count = 0
            exact_coefficients[key] = {}
            for n in range(1,args.N+1):
                values = []
                expected_length = len(source_selected[key][n])
                for j in range(expected_length):
                    m = 2*j+(1 if odd else 0)
                    own = series[n].sine(m) if m else arb(0)
                    old = arb(*unpack(source_selected[key][n][j]))
                    assert own.overlaps(old), ('source mismatch',index,key,n,m,text(own),text(old))
                    values.append(text(own))
                    count += 1
                for m in range(2*expected_length+(1 if odd else 0),solver.B*n+1,2):
                    assert series[n].sine(m).contains(0), ('unmatched support',index,key,n,m)
                exact_coefficients[key][str(n)] = values
            comparisons.append(dict(field=key,maximum_order=args.N,coefficients=count,all_overlap=True))
        hrows = []
        for item in harmonics:
            n = item['n']
            oldH = arb(selected_h['H'][str(n)]['str'])
            oldS = arb(selected_h['sigma'][str(n)])
            assert item['H'].overlaps(oldH), ('harmonic',index,n)
            assert item['sigma'].overlaps(oldS), ('response',index,n)
            assert item['obstruction'].contains(0), ('compatibility',index,n,text(item['obstruction']))
            hrows.append({key:text(value) if key in ['H','sigma','obstruction'] else value
                          for key,value in item.items()})
        norms = []
        for n in range(1,args.N+1):
            F,G = f[n].norm(),g[n].norm()
            norms.append(dict(n=n,density_norm=text(F),stream_norm=text(G),
                density_root=text((F.log()/n).exp()),stream_root=text((G.log()/n).exp()),
                density_relative_radius=text(F.rad()/abs(F.mid())),
                stream_relative_radius=text(G.rad()/abs(G.mid()))))
        coeffraw = (json.dumps(exact_coefficients,separators=(',',':'))+'\n').encode()
        (out/'independent_coefficients.json.gz').write_bytes(gzip.compress(coeffraw,mtime=0))
        result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            all_checks_pass=True,Q=9,h=2,root_index=index,maximum_order=args.N,
            arithmetic_bits=args.bits,root_interval=interval,root_ball=text(b),counts=solver.counts,
            source=source_info,comparisons=comparisons,norms=norms,harmonics=hrows,
            actual_elapsed_s=time.monotonic()-root_start,total_elapsed_s=time.monotonic()-start,
            root_certificate_sha256=sha256(certificate_raw).hexdigest(),
            source_polynomial_sha256=sha256(source_poly_raw).hexdigest(),
            scope='Independent finite Cartesian enclosures. No improved infinite radius inferred.')
        (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
        files = {p.name:dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest())
                 for p in out.iterdir() if p.is_file()}
        (out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
        print(json.dumps(dict(root=index,all_checks_pass=True,comparisons=comparisons,
                              actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
    for name in ['four_ninths_finite_audit.py','pure_cartesian_ball.py','stream_precision_audit.py']:
        (root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    for name in ['tuned_general.py','tuned_cQ.py','ffcore.py']:
        (root/'sources'/('numerical_'+name)).write_bytes(Path('../a4-num/code',name).read_bytes())
    (root/'sources/exact_polynomial.json').write_bytes(source_poly_raw)


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        import traceback
        fail = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            error_type=type(exc).__name__,error=str(exc),
            frames=[dict(file=Path(x.filename).name,line=x.lineno) for x in traceback.extract_tb(exc.__traceback__)])
        Path('research/167_four_ninths_finite_audit/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n')
        print(json.dumps(fail),flush=True)
        raise SystemExit(1)
