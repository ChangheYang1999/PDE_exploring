"""Independent potential-product projections and Cartesian Laplacian moments."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import gzip
import json
import sys
import time
from flint import arb, ctx, fmpq as Q, fmpq_poly as P

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/projected_laplacian_audit'
SRC = BASE / 'source'
sys.path.insert(0, str(ROOT / 'research/radial_fourier/code'))
sys.path.insert(0, str(ROOT / 'research/whole_plane_norms/code'))
sys.path.insert(0, str(ROOT / 'research/projected_residual/code'))
from radial import Radial, pshift, put
from norms import derivative, ar, T, U, ZERO
from build import read_projection


def digest(path):
    h = sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def project(model, mode):
    out = {}
    for (j, n), V in model.rho.items():
        if n == mode:
            TP = T * V.derivative()
            put(out, j + 1, pshift(model.c * (2*TP - 3*V + 2*T*(model.p[j]*V-TP)) - V, 2))
    quad = {}
    counts = []
    for C, S in [(model.u1, model.rx), (model.ry, model.u2)]:
        count = 0
        for (i, n), V in C.items():
            for (j, m), W in S.items():
                twice = int(m+n == mode) + int(m-n == mode) - int(m-n == -mode)
                if twice:
                    put(quad, i+j+2, V*W*Q(twice, 2))
                    count += 1
        counts.append(count)
    for ell, V in quad.items():
        put(out, ell, pshift(V, 4))
    return {k: V for k, V in out.items() if V}, counts


def main():
    start = time.monotonic()
    ctx.prec = 2048
    name = 'C1-N1-007-d2w-j7-e2bal'
    canonical = ROOT / f'research/candidate_audits/data/{name}/canonical.json'
    assert digest(canonical) == '153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
    peer = {n: json.loads((SRC/f'verification/candidate007_mode{n}.json').read_text()) for n in [1, 3]}
    combined = json.loads((SRC/'verification/combined_cover.json').read_text())
    checked = {}
    for n, rec in peer.items():
        assert rec['candidate'] == name and rec['angular_modes'] == [n]
        for rel, expected in rec['inputs'].items():
            p = canonical if rel == 'data/candidate007_canonical.json' else SRC/rel
            assert digest(p) == expected, (rel, digest(p), expected)
            checked[f'mode{n}:{rel}'] = expected
    assert digest(SRC/'T4_reproduce.py') == peer[3]['helper_sha256']
    for n in [1, 3]:
        rel = f'verification/candidate007_mode{n}.json'
        assert digest(SRC/rel) == combined['inputs'][rel]
    assert digest(SRC/'COVER.md') == combined['proof_sha256']
    assert digest(SRC/'code/combine.py') == combined['code_sha256']
    model = Radial(canonical)
    saved_first, saved_meta = read_projection(name)
    print('loaded model', time.monotonic()-start, flush=True)
    rows = []; values = {}; identities = []; count_rows = []
    for n in [1, 3]:
        projected, counts = project(model, n)
        if n == 1:
            assert projected == saved_first
        F = {(ell, 's', n): V for ell, V in projected.items()}
        dx = derivative(F, 0, 'x', model.delta)
        dy = derivative(F, 0, 'y', model.delta)
        assert derivative(dx, 1, 'y', model.delta) == derivative(dy, 1, 'x', model.delta)
        xx = derivative(dx, 1, 'x', model.delta)
        yy = derivative(dy, 1, 'y', model.delta)
        lap = {k: xx.get(k, ZERO) + yy.get(k, ZERO) for k in set(xx)|set(yy)}
        lap = {k: V for k, V in lap.items() if V}
        td = lambda V,d: (1-2*d*T)*V + 2*T*U*V.derivative()
        polar = {k: td(td(V, k[0]*model.delta/2), k[0]*model.delta/2)-n*n*V for k,V in F.items()}
        polar = {k: V for k,V in polar.items() if V}
        assert set(polar) == set(lap)
        assert all(T*V == polar[k] for k,V in lap.items())
        assert all(kind == 's' and frequency == n for ell,kind,frequency in lap)
        identities.append({'mode': n, 'branches': len(lap), 'cartesian_polar_exact': True, 'mixed_exact': True})
        terms = []; diagonals = []
        for (ell,kind,frequency), V in lap.items():
            W = V(U)
            q = next(i for i,x in enumerate(W) if x)
            terms.append((ell, W)); diagonals.append((ell, q))
        groups = {}
        for i,(ell,V) in enumerate(terms):
            for j in range(i,len(terms)):
                ell2,W = terms[j]
                b = (ell+ell2)*model.delta/2 - 3
                groups[b] = groups.get(b,ZERO) + (1 if i==j else 2)*U*V*W
        moments = [(b+j+1,ar(x)) for b,V in groups.items() for j,x in enumerate(V) if x]
        count_rows.append({'mode':n, 'nonlinear_pair_counts':counts, 'groups':len(groups), 'moments':len(moments)})
        peerrows = {Q(r['a']):r for r in peer[n]['rows']}
        print('prepared mode',n,'seconds',time.monotonic()-start,flush=True)
        for a in [Q(k,4) for k in range(8)]:
            assert all(a+ell*model.delta+2*q-2>0 for ell,q in diagonals)
            assert all(a+b>0 for b,x in moments)
            E = sum((x/ar(a+b) for b,x in moments), arb(0))
            assert E>0
            norm = (arb.pi()*E/2).sqrt()
            lower = arb(5)**ar((a-2)/2)*norm
            beta = 1+model.c-model.c*a
            ceiling = (8*arb.pi()).sqrt()*ar(beta**2/(1+a)) if beta>0 else None
            checks = {'norm':norm.overlaps(arb(peerrows[a]['projected_norm'])),
                      'Y_lower':lower.overlaps(arb(peerrows[a]['Y_lower']))}
            if ceiling is not None: checks['ceiling'] = ceiling.overlaps(arb(peerrows[a]['B']))
            assert all(checks.values())
            rows.append({'mode':n,'a':str(a),'norm':norm.str(100),'Y_lower':lower.str(100),'peer_overlaps':checks})
            values[n,a] = norm
    A = 1+1/model.c
    assert A<Q(7,4)
    cells = []
    for i,(l,h,evaluation) in enumerate([(Q(4,5),Q(1),Q(1)),(Q(1),Q(5,4),Q(5,4)),(Q(5,4),Q(3,2),Q(3,2)),(Q(3,2),A,Q(7,4))]):
        J = (values[1,evaluation]**2+values[3,evaluation]**2).sqrt()
        lower = arb(5)**ar((l-2)/2)*J
        upper = (8*arb.pi()).sqrt()*ar((1+model.c-model.c*l)**2/(1+l))
        ratio = lower/upper
        assert lower>upper and ratio>1
        old = combined['cells'][i]
        assert Q(old['left'])==l and Q(old['right'])==h and Q(old['norm_evaluation_at'])==evaluation
        overlaps = {k:x.overlaps(arb(old[k])) for k,x in [('lower',lower),('upper',upper),('ratio',ratio)]}
        assert all(overlaps.values())
        cells.append({'left':str(l),'right':str(h),'norm_evaluation_at':str(evaluation),'lower':lower.str(100),'upper':upper.str(100),'ratio':ratio.str(100),'peer_overlaps':overlaps})
    output = {
        'utc':datetime.now(timezone.utc).isoformat(), 'candidate':name,
        'precision_bits':ctx.prec, 'source_sha256':digest(canonical),
        'code_sha256':digest(Path(__file__)), 'proof_sha256':digest(BASE/'PROOF.md'),
        'dependencies':{p:digest(ROOT/p) for p in ['research/radial_fourier/code/radial.py','research/whole_plane_norms/code/norms.py','research/projected_residual/code/build.py']},
        'peer_files':{str(p.relative_to(SRC)):digest(p) for p in SRC.rglob('*') if p.is_file()},
        'peer_input_hashes_checked':checked, 'rows':rows,'counts':count_rows,
        'cartesian_identities':identities,'cells':cells,
        'elapsed_seconds':time.monotonic()-start,
        'verdict':'CONFIRMED for modes1,3 and the four-cell scheme-specific exclusion on [4/5,A).',
    }
    dest = BASE/'verification/candidate007_modes13.json'
    assert not dest.exists()
    dest.write_text(json.dumps(output,indent=2)+'\n')
    print('DONE',output['elapsed_seconds'],flush=True)
    for row in cells: print(row['left'],row['right'],row['ratio'],flush=True)

if __name__ == '__main__':
    main()
