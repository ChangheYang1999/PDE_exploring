"""Assemble seven admitted regions and exact NR-25 inputs for source013."""
import argparse, time
from flint import arb, ctx
import common_v03 as c
import arithmetic_v01 as a
import provenance_v03 as p

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--request', required=True); ap.add_argument('--request-sha256', required=True); args = ap.parse_args()
    c.environment(); start, tick = c.stamp(), time.monotonic(); registry = c.Registry()
    request = registry.json(args.request, args.request_sha256)
    assert request['schema'] == 'source013-near-norms-request-v1' and request['source'] == c.SOURCE
    mf = 'research/source013_near_norms/verification/manifest_v02.json'; rf = 'research/source013_near_norms/verification/external_review_v02.json'
    method = registry.json(mf, request['method_sha256']); review = registry.json(rf, request['review_sha256'])
    assert method['schema'] == 'source013-near-norms-method-v1' and method['source'] == c.SOURCE
    assert review['status'] == 'BOUND' and review['manifest_sha256'] == request['method_sha256']
    assert request['files'] == {**method['files'], mf: request['method_sha256'], rf: request['review_sha256']}
    registry.mapping(request['files'])
    chunk_mf = c.CHUNK + '/verification/chunk_manifest_v02.json'; chunk_rf = c.CHUNK + '/verification/chunk_external_review_v02.json'
    chunk = registry.json(chunk_mf, method['chunk_method_sha256']); chunk_review = registry.json(chunk_rf, method['chunk_review_sha256'])
    assert chunk['schema'] == 'source013-near-chunk-method-v1' and chunk['source'] == c.SOURCE and chunk['chunk_size'] == 8 and chunk['precision_bits'] == 2048
    assert chunk['chunk_counts'] == [15,14,14,14,14]
    assert chunk_review['status'] == 'BOUND' and chunk_review['manifest_sha256'] == method['chunk_method_sha256']
    registry.mapping(chunk['files'])
    manifest, plan = p.deployment(registry)
    assert [row['job'] for row in request['blocks']] == ['n0','n1','n2','n3','n4']
    assert set(request['endpoints']) == {'origin', 'exterior'}
    blocks = []
    for descriptor in request['blocks']:
        blocks.append(p.block(registry, descriptor, manifest, plan, chunk, method['chunk_method_sha256'], method['chunk_review_sha256']))
        print(c.stamp(), 'ADMITTED_BLOCK_CONSUMED', descriptor['job'], flush=True)
    origin = p.endpoint(registry, 'origin', request['endpoints']['origin'])
    exterior = p.endpoint(registry, 'exterior', request['endpoints']['exterior'])
    norms = a.assemble(blocks, manifest['jobs'], c.SOURCE, origin, exterior)
    ctx.prec = 256; pi = arb.pi(); pi_interval = [str(pi.lower().fmpq()), str(pi.upper().fmpq())]
    assert a.exact(pi_interval[0]) > 3 and a.exact(pi_interval[1]) < 4
    moment_inputs = a.moments(norms, pi_interval[0])
    registry.final(); tag = request['output_tag']
    assert tag == 'wholeplane_v02'
    folder = c.BASE / 'verification' / tag; folder.mkdir(exist_ok=False)
    output = {'schema': 'source013-wholeplane-near-norms-v1', 'status': 'ADMITTED_WHOLEPLANE_NEAR_NORMS',
              'started_utc': start, 'finished_utc': c.stamp(), 'elapsed_seconds': time.monotonic()-tick,
              'source': c.SOURCE, 'request': args.request, 'request_sha256': args.request_sha256,
              'blocks': request['blocks'], 'endpoints': request['endpoints'], 'panel_count': 561,
              'norms': norms, 'pi_interval_exact': pi_interval, 'pi_precision_bits': 256, 'moment_inputs': moment_inputs,
              'method_sha256': request['method_sha256'], 'review_sha256': request['review_sha256'],
              'input_files': request['files'], 'files': registry.files, 'external_dependencies': registry.external,
              'code_sha256': c.digest(c.local('research/source013_near_norms/code/assemble_v03.py')),
              'scope': 'Whole-plane ordered Cartesian D4-D6 and NR-25 Fourier L1 moment/tail inputs, conditional on the accepted source and containing regional theorems. Actual result review is still required. No complete near price, inverse, invariant ball or existence.'}
    c.put(folder / 'result.json', output)
    print(c.stamp(), 'WHOLEPLANE_NEAR_NORMS', norms, output['elapsed_seconds'], flush=True)
if __name__ == '__main__': main()
