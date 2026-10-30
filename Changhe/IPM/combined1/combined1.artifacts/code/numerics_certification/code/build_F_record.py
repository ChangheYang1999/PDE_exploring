"""Assemble the exact compactified residual F of a candidate and store it as <outdir>/<stem>_Fpoly_cache.json (the hminus1 cache
layout: canonical_sha256, delta, polynomials['0,0']). The expensive step (about 33 min for 1922 generators) is then shared by
general_probe.py, weak_from_cache.py, wlap_modes.py, hminus1.py and candidate_pipeline.py. Usage: build_F_record.py <source> <outdir>"""
from pathlib import Path
import json, sys, time
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E

def run(source, outdir):
    t0 = time.monotonic(); outdir = Path(outdir)
    c, A, src_sha, can_sha, meta = E.load_reference(source)
    print(f'{source}: {meta} source {src_sha} canonical {can_sha}', flush=True)
    D, fields = E.residual_polynomials(A, c, 0, print)
    poly = {'0,0': [{'ell': ell, 'kind': kind, 'mode': n, 'coeff': [str(v) for v in p.coeffs()]} for (ell, kind, n), p in sorted(D[0, 0].items())]}
    dest = outdir / (Path(source).stem + '_Fpoly_cache.json')
    dest.write_text(json.dumps({'canonical_sha256': can_sha, 'source_sha256': src_sha, 'delta': str(1 - 1 / c), 'cl': str(c), 'polynomials': poly}, separators=(',', ':')) + '\n')
    print(f'F record {dest} ({dest.stat().st_size/1e6:.1f} MB, {len(poly["0,0"])} components) in {time.monotonic()-t0:.0f}s', flush=True)

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
