"""Exact generator-map rank and zero-potential directions; no optimizer import."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from collections import defaultdict
from math import comb
import json
import time
from flint import fmpq as Q, fmpq_poly as Poly

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/basis_redundancy'
T = Poly([0, 1])


def digest(p):
    return sha256(Path(p).read_bytes()).hexdigest()


def rodrigues(n):
    return Poly([(-1)**(n-k)*comb(n, k)*comb(n+k, k) for k in range(n+1)])


def recurrence(n):
    a, b = Poly([1]), 2*T-1
    if n == 0:
        return a
    for k in range(1, n):
        a, b = b, ((2*k+1)*(2*T-1)*b-k*a)/(k+1)
    return b


def polynomial(spec):
    if spec[0] == 'mono':
        return T**int(spec[1])
    assert spec[0] == 'leg'
    return T**int(spec[1])*rodrigues(int(spec[2]))


def subtract(v, w, coefficient):
    out = dict(v)
    for i, x in w.items():
        out[i] = out.get(i, Q(0))-coefficient*x
        if not out[i]:
            del out[i]
    return out


def main():
    tick = time.monotonic()
    manifest = json.loads((BASE/'source/MANIFEST.json').read_text())
    for name, info in manifest['files'].items():
        assert digest(BASE/'source'/name) == info['sha256']
    src = BASE/'source/candidate007.json'
    raw = json.loads(src.read_text())
    assert raw['n_free'] == 2982 and raw['n_fixed'] == 0
    c = Q(raw.get('cl', raw.get('cl_exact')))
    assert c == Q(4076476460239181, 2251799813685248)
    delta = 1-1/c
    gens = raw['generators']
    js = sorted({int(g['j']) for g in gens})
    pairs = []
    for j in js:
        for k in js:
            if j >= k:
                continue
            z = (k-j)*delta/2
            assert z.denominator != 1
            pairs.append({'j': j, 'k': k, 'exponent_difference': str(z)})
    for n in range(max(int(g['spec'][2]) for g in gens if g['spec'][0]=='leg')+1):
        assert rodrigues(n) == recurrence(n)
    columns = [polynomial(g['spec']) for g in gens]
    groups = defaultdict(list)
    for i, g in enumerate(gens):
        groups[int(g['j']), int(g['m'])].append(i)
    blocks, relations, total_rank = [], [], 0
    for (j, m), indices in sorted(groups.items()):
        ordered = sorted(indices, key=lambda i: (gens[i]['spec'][0]!='mono', columns[i].degree(), i))
        basis, pivots, nulls = {}, [], []
        for index in ordered:
            p, vector = columns[index], {index: Q(1)}
            while p:
                deg = p.degree()
                if deg not in basis:
                    basis[deg] = (p, vector)
                    pivots.append(index)
                    break
                bp, bv = basis[deg]
                factor = p[deg]/bp[deg]
                p -= factor*bp
                vector = subtract(vector, bv, factor)
            if not p:
                assert vector[index] == 1
                assert all(i in pivots or i == index for i in vector)
                # Explicit independent polynomial multiplication checks each identity.
                check = sum((coefficient*columns[i] for i, coefficient in vector.items()), Poly([]))
                assert not check
                nulls.append(index)
                relations.append({'j': j, 'm': m, 'unit_nonpivot_index': index,
                                  'coefficients': {str(i): str(q) for i, q in sorted(vector.items())}})
        rank = len(basis)
        assert rank+len(nulls) == len(indices)
        degrees = {int(gens[i]['spec'][1]) for i in indices if gens[i]['spec'][0]=='mono'}
        supports = {k for i in indices for k, q in enumerate(columns[i]) if q}
        if supports <= degrees:
            second_rank, reason = len(degrees), 'monomial subset spans all columns'
        else:
            assert all(gens[i]['spec'][0]=='leg' for i in indices)
            assert len({columns[i].degree() for i in indices}) == len(indices)
            second_rank, reason = len(indices), 'distinct-degree Legendre triangular family'
        assert rank == second_rank
        total_rank += rank
        blocks.append({'j': j, 'm': m, 'columns': len(indices), 'rank': rank,
                       'kernel_dimension': len(nulls), 'pivot_indices': pivots,
                       'nonpivot_indices': nulls, 'separate_rank_proof': reason,
                       'maximum_degree': max(columns[i].degree() for i in indices)})
    assert len(relations) == len(gens)-total_rank
    # Reconstruct the published canonical polynomial map with this binomial route.
    actual = defaultdict(lambda: Q(0))
    for i, g in enumerate(gens):
        for k, q in enumerate(columns[i]):
            actual[int(g['j']), int(g['m']), int(g['m'])+k] += Q(g['coef'])*q
    actual = {k: q for k, q in actual.items() if q}
    canonical = json.loads((BASE/'source/canonical007.json').read_text())
    expected = {tuple(map(int, k)): Q(q) for k, q in zip(canonical['order'], canonical['coefficients'])}
    assert actual == expected
    relations_file = BASE/'verification/candidate007_kernel_relations.json'
    with relations_file.open('x') as f:
        json.dump({'utc': datetime.now(timezone.utc).isoformat(), 'relations': relations}, f, indent=2)
        f.write('\n')
    result = {'utc': datetime.now(timezone.utc).isoformat(), 'candidate':'C1-N1-007-d2w-j7-e2bal',
              'generators': len(gens), 'blocks': len(blocks), 'potential_space_dimension': total_rank,
              'exact_zero_potential_dimension': len(relations),
              'nonresonance_pairs': pairs, 'block_results': blocks,
              'all_kernel_relations_verified': True, 'all_blocks_have_two_rank_checks': True,
              'canonical_nonzero_coefficients':len(actual), 'canonical_identity': True,
              'relations_sha256': digest(relations_file), 'source_sha256': digest(src),
              'canonical_sha256': digest(BASE/'source/canonical007.json'),
              'source_manifest_sha256': digest(BASE/'source/MANIFEST.json'),
              'code_sha256': digest(__file__), 'proof_sha256': digest(BASE/'PROOF.md'),
              'elapsed_seconds': time.monotonic()-tick,
              'status':'OPEN peer; exact zero-potential representation directions, not a PDE near-kernel'}
    with (BASE/'verification/candidate007.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['block_results','nonresonance_pairs']},indent=2),flush=True)


if __name__ == '__main__':
    main()
