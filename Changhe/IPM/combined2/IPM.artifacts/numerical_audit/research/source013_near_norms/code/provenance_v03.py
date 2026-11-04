"""Consume independently admitted complete blocks and both exact endpoints."""
from pathlib import Path
import common_v03 as c
import contracts_v03 as k

ENDPOINTS = {
    'origin': {
        'primary': ('research/source013_near_endpoints/verification/origin/primary.json', '044f3c5358937f857ab9885942c3e0f5a7e5a15d48f99ef54ad04a84846d24d4'),
        'reduction': ('research/source013_near_endpoints/verification/origin/reduction_v02.json', '3b0607e1695c607c97abcdd060b0b7ef6e350d644a9c43768ed2f7d0ac8c6813'),
        'primary_receipt': ('research/post_handoff_preparation/verification/compute_source013_near_endpoints_v01/execution.json', 'a01ef8aa41e870c61f6fa476f3b84335e6b50254844fe5386bdfbe5da6d03b97'),
        'reduction_receipt': ('research/finite_long_preparation/verification/reduce_source013_near_origin_fast_v01/execution.json', 'c97a8fd86ecb2ddf51012405b0f9066b7fdf5d88bbfcca3a651e5a11fd46a6aa'),
        'primary_script': 'research/source013_near_endpoints/code/calculate_v01.py',
        'reduction_script': 'research/source013_near_endpoints/code/calculate_fast_origin_v01.py',
    },
    'exterior': {
        'primary': ('research/source013_near_endpoints/verification/exterior_correlated_v01/primary.json', '2462bbdce6efbd0856acdaf1378d4048a492aba9641f52a05a6a0fe8c5768772'),
        'reduction': ('research/source013_near_endpoints/verification/exterior_correlated_v01/reduction.json', '175fc6f55f07b3708ea7ca0d0fd6336bffd3b9ad4a39fabc23a04f39d31cf31e'),
        'primary_receipt': ('research/post_handoff_preparation/verification/compute_source013_near_correlated_exterior_v01/execution.json', 'f3984a784f5aeb3d35cd3febd9dc6426da7493272ce05b1891a749acb92d05a2'),
        'reduction_receipt': ('research/post_handoff_preparation/verification/compute_source013_near_correlated_exterior_v01/execution.json', 'f3984a784f5aeb3d35cd3febd9dc6426da7493272ce05b1891a749acb92d05a2'),
        'primary_script': 'research/source013_near_endpoints/code/calculate_correlated_exterior_v01.py',
        'reduction_script': 'research/source013_near_endpoints/code/calculate_correlated_exterior_v01.py',
    },
}

def finite(registry, path, expected, result, script, gate_kind='long', index=0, completed=True):
    execution = registry.json(path, expected)
    outer_path = execution['request']; outer_hash = execution['request_sha256']
    outer = registry.json(outer_path, outer_hash); registry.mapping(outer['files'])
    application = registry.json(result['request'], result['request_sha256']); registry.mapping(application['files'])
    base = 'research/finite_long_preparation' if gate_kind == 'long' else 'research/post_handoff_preparation'
    method_hash, review_hash = (c.LONG_MH, c.LONG_RH) if gate_kind == 'long' else (c.SHORT_MH, c.SHORT_RH)
    method = registry.json(base + '/verification/manifest_v01.json', method_hash)
    review = registry.json(base + '/verification/external_review_v01.json', review_hash)
    assert review['status'] == 'BOUND' and review['manifest_sha256'] == method_hash
    registry.mapping(method['files'])
    assert execution['code_sha256'] == method['files'][base + '/code/run_v01.py']
    assert outer['files'][script] == result['code_sha256']
    assert all(outer['files'].get(n) == q for n, q in application['files'].items())
    k.finite(execution, outer, outer_hash, result, result['request'], result['request_sha256'], script, gate_kind, index, completed)
    return execution, application

def deployment(registry):
    manifest = registry.json(c.COVER + '/verification/manifest_v01.json', c.contract.MH)
    review = registry.json(c.COVER + '/verification/external_review_v01.json', c.contract.RH)
    assert review['status'] == 'BOUND' and review['manifest_sha256'] == c.contract.MH
    registry.mapping(manifest['files'])
    d = c.load('near_norm_deployment', c.COVER + '/code/deployment_common_v01.py'); d.ROOT = c.ROOT
    d.validate(manifest); plan = d.plan_check(manifest); d.source_check(manifest)
    assert manifest['source'] == c.SOURCE and len(plan) == 561
    return manifest, plan

def owner(registry, manifest, job, pinned):
    assert set(pinned) == {'installation.json', 'execution_v01.json', 'output/result.json'}
    prefix = '../' + job['owner'] + '/' + c.COVER + '/worker_' + job['id'] + '/'
    root = c.ROOT.parent / job['owner'] / c.COVER / ('worker_' + job['id'])
    assert registry.path(prefix.rstrip('/'), True).resolve() == root == root.resolve()
    for name, expected in pinned.items(): registry.bind(prefix + name, expected, True)
    registry.bind(prefix + 'manifest.json', c.contract.MH, True)
    registry.bind(prefix + 'review.json', c.contract.RH, True)
    for name, expected in manifest['files'].items():
        path = registry.bind(prefix + name, expected, True)
        if name in manifest['copied_code']: assert not path.is_symlink() and path.resolve().is_relative_to(root)
    install, receipt, result = [c.read(root / name) for name in ['installation.json', 'execution_v01.json', 'output/result.json']]
    c.contract.receipt(manifest, job, install, receipt, result, pinned['output/result.json'])
    return prefix, root, result, receipt

def block(registry, descriptor, manifest, plan, method, method_hash, method_review_hash):
    result = registry.json(descriptor['result'], descriptor['sha256'])
    assert result['schema'] == 'source013-near-block-admission-v1' and result['status'] == 'ADMITTED_NEAR_BLOCK'
    assert result['job'] == descriptor['job']
    job = manifest['jobs'][int(result['job'][1:])]; assert job['id'] == result['job'] and result['block'] == job
    assert result['source'] == c.SOURCE and result['complete_requested_assignment'] is True and result['precision_bits'] == 2048
    assert result['code_sha256'] == method['files'][c.CHUNK + '/code/assemble_chunk_v02.py']
    review = registry.actual_review(descriptor['actual_review'], descriptor['actual_review_sha256'],
        {'result_sha256': descriptor['sha256'], 'execution_sha256': descriptor['execution_sha256']},
        {descriptor['result']: descriptor['sha256'], descriptor['execution']: descriptor['execution_sha256']})
    execution, application = finite(registry, descriptor['execution'], descriptor['execution_sha256'], result, c.CHUNK + '/code/assemble_chunk_v02.py')
    assert application['schema'] == 'source013-near-block-assembly-request-v1' and application['job'] == job['id']
    expected_files = {**method['files'], c.CHUNK + '/verification/chunk_manifest_v02.json': method_hash,
                      c.CHUNK + '/verification/chunk_external_review_v02.json': method_review_hash}
    assert application['files'] == result['input_files'] == expected_files
    assert application['method_sha256'] == method_hash and application['review_sha256'] == method_review_hash
    identity = {'source': c.SOURCE, 'deployment_manifest_sha256': c.contract.MH, 'deployment_review_sha256': c.contract.RH,
                'method_sha256': method_hash, 'review_sha256': method_review_hash, 'owner_files': application['owner_files']}
    assert result['identity'] == identity
    prefix, remote, parent, owner_receipt = owner(registry, manifest, job, application['owner_files'])
    assert result['original_result_sha256'] == application['owner_files']['output/result.json']
    registry.mapping(result['files']); registry.mapping(result['external_bindings'], True)
    metadata = {row['index']: row for row in parent['panels']}
    chunks = result['chunks']; assert chunks == application['chunks']
    expected_groups = c.chunks.partition(job['indices'])
    assert len(chunks) == result['chunk_count'] == len(expected_groups)
    assert result['panel_count'] == len(job['indices'])
    assert [row['chunk'] for row in chunks] == list(range(len(chunks)))
    rows = []
    for description in chunks:
        part = registry.json(description['result'], description['sha256'], compressed=True)
        assert part['schema'] == 'source013-near-chunk-result-v1' and part['identity'] == identity
        assert part['job'] == job['id'] and part['chunk'] == description['chunk']
        assert part['indices'] == expected_groups[part['chunk']] and part['input_files'] == expected_files
        assert part['code_sha256'] == method['files'][c.CHUNK + '/code/chunk_v02.py']
        assert part['source_counts'] == {'branches': 52, 'mode_polynomials': 5136, 'polynomial_coefficients': 211664}
        partial_execution, partial_application = finite(registry, description['execution'], description['execution_sha256'], part, c.CHUNK + '/code/chunk_v02.py')
        assert partial_application['schema'] == 'source013-near-chunk-request-v1' and partial_application['job'] == job['id']
        assert partial_application['chunk'] == part['chunk'] and partial_application['indices'] == part['indices']
        assert partial_application['method_sha256'] == method_hash and partial_application['review_sha256'] == method_review_hash
        assert partial_application['owner_files'] == identity['owner_files'] and partial_application['files'] == expected_files
        assert partial_application['archives'] == [metadata[i] for i in part['indices']]
        assert c.contract.measured(owner_receipt)[1] <= c.contract.measured(partial_execution)[0]
        assert c.contract.measured(partial_execution)[1] <= c.contract.measured(result)[0]
        registry.mapping(part['files']); registry.mapping(part['external_bindings'], True)
        folder = Path(description['result']).parent
        assert [panel['index'] for panel in part['panels']] == part['indices']
        for panel in part['panels']:
            index = panel['index']; meta = metadata[index]
            assert panel['panel'] == plan[index] and panel['archive_sha256'] == meta['sha256']
            assert panel['majorant']['passed'] is True and panel['majorant']['source_counts'] == part['source_counts']
            named = str(folder / f'panel_{index:05d}.json.gz')
            assert part['files'][named] == meta['sha256']
            archive = registry.bind(prefix + meta['path'], meta['sha256'], True)
            assert archive.stat().st_size == meta['bytes'] and archive.resolve().is_relative_to(remote)
            pair = registry.json(named, meta['sha256'], compressed=True)
            exact, times = c.contract.panel(pair, plan, index, manifest, job, parent, meta)
            assert exact == panel['containing_intersections'] and times == panel['original_record_times']
            rb, re = c.contract.measured(panel); pb, pe = c.contract.measured(part)
            assert pb <= rb <= re <= pe
        rows.append(part)
    total = c.chunks.assemble(job, rows, identity, parent['laplacian_energies'])
    assert total == result['laplacian_energies']
    assert c.contract.measured(owner_receipt)[1] <= c.contract.measured(result)[0]
    return result

def endpoint(registry, region, descriptor):
    fixed = ENDPOINTS[region]
    for kind in ['primary', 'reduction']:
        assert descriptor[kind] == fixed[kind][0] and descriptor[kind + '_sha256'] == fixed[kind][1]
    primary = registry.json(descriptor['primary'], descriptor['primary_sha256'])
    reduction = registry.json(descriptor['reduction'], descriptor['reduction_sha256'])
    records = [primary, reduction]
    bound = {descriptor[kind]: descriptor[kind + '_sha256'] for kind in ['primary', 'reduction']}
    for n, kind in enumerate(['primary', 'reduction']):
        path, expected = fixed[kind + '_receipt']
        assert expected is not None, 'Exact original execution binding must be frozen before preparation'
        assert descriptor[kind + '_execution'] == path and descriptor[kind + '_execution_sha256'] == expected
        bound[path] = expected
        gate_kind = 'long' if region == 'origin' and kind == 'reduction' else 'short'
        index = n if region == 'exterior' else 0
        finite(registry, path, expected, records[n], fixed[kind + '_script'], gate_kind, index,
               completed=not (region == 'origin' and kind == 'primary'))
    registry.actual_review(descriptor['actual_review'], descriptor['actual_review_sha256'],
        {'primary_sha256': descriptor['primary_sha256'], 'reduction_sha256': descriptor['reduction_sha256']}, bound)
    return k.endpoint(primary, reduction, region, descriptor['primary_sha256'])
