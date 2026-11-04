"""Exact receipt and endpoint requirements without numerical source generation."""
from fractions import Fraction as F
import common_v03 as c

def finite(execution, gate_request, request_hash, result, application, application_hash, script, gate_kind, index=0, completed=True):
    assert gate_kind in ['short', 'long']
    method, review = (c.LONG_MH, c.LONG_RH) if gate_kind == 'long' else (c.SHORT_MH, c.SHORT_RH)
    assert execution['schema'] == ('finite-long-preparation-execution-v1' if gate_kind == 'long' else 'post-handoff-preparation-execution-v1')
    assert execution['method_manifest_sha256'] == method and execution['method_review_sha256'] == review
    assert execution['request_sha256'] == request_hash and execution['old_process_signals'] == 0
    if completed:
        assert execution['status'] == 'COMPLETED' and execution['reason'] is None
        assert len(execution['stages']) == len(gate_request['stages'])
        assert all(type(s['exit_code']) is int and s['exit_code'] == 0 for s in execution['stages'])
    else:
        assert execution['status'] == 'REJECTED' and execution['reason'] and index == 0
    assert type(index) is int and 0 <= index < len(execution['stages'])
    stage, requested = execution['stages'][index], gate_request['stages'][index]
    assert type(stage['exit_code']) is int and stage['exit_code'] == 0
    assert stage['argv'] == requested['argv']
    assert requested['argv'][:2] == ['-B', script]
    assert requested['argv'].count('--request') == requested['argv'].count('--request-sha256') == 1
    assert requested['argv'][requested['argv'].index('--request') + 1] == application
    assert requested['argv'][requested['argv'].index('--request-sha256') + 1] == application_hash
    limit = requested['limit_seconds']
    assert type(limit) in [int, float] and 0 < limit <= (480 if gate_kind == 'long' else 120)
    assert stage['elapsed_seconds'] <= limit + 2
    assert gate_request['files'][application] == application_hash
    assert result['request'] == application and result['request_sha256'] == application_hash
    eb, ee = c.contract.measured(execution); sb, se = c.contract.measured(stage); rb, re = c.contract.measured(result)
    assert eb <= sb <= rb <= re <= se <= ee
    return True

def endpoint(primary, reduction, region, primary_hash):
    assert region in ['origin', 'exterior'] and reduction['primary_sha256'] == primary_hash
    for row, kind, bits in [(primary, 'primary', 1024), (reduction, 'reduction', 1536)]:
        assert row['status'] == 'LOCAL_NEAR_ENDPOINT_COMPUTED' and row['kind'] == kind and row['region'] == region
        assert row['source'] == c.ENDPOINT_SOURCE and row['geometry'] == c.ENDPOINT_GEOMETRY
        assert row['precision_bits'] == bits and row['bandwidth'] == 160
        assert row['regional']['request'] == c.ENDPOINT_GEOMETRY[region]
        assert [e['order'] for e in row['regional']['laplacian_energies']] == [4, 5, 6]
        assert F(row['regional']['source_bound_upper_exact']) > 0
    assert primary['source_admission_sha256'] == reduction['source_admission_sha256'] == '1d7b5172a35b36db641f533a74e13fe6115d4c1f48af99369fba7e595a881766'
    assert primary['source_archive_sha256'] == reduction['source_archive_sha256'] == 'cca33fbf02241a3bbdaf4d63895593b32538fc6a1a6c24d7a020f59de148b48e'
    if region == 'origin':
        assert primary['regional']['polynomial'] == reduction['regional']['polynomial']
        for p, r in zip(primary['regional']['laplacian_energies'], reduction['regional']['laplacian_energies'], strict=True):
            assert p['polynomial_squared_norm_divided_by_pi_exact'] == r['polynomial_squared_norm_divided_by_pi_exact']
    else:
        assert primary['endpoint_terms'] == reduction['endpoint_terms'] == 3008
        assert primary['regional']['power_exact'] == reduction['regional']['power_exact'] == '-1824676646553933/4076476460239181'
    rows = []
    for p, r in zip(primary['regional']['laplacian_energies'], reduction['regional']['laplacian_energies'], strict=True):
        pl, pu, rl, ru = map(F, [p['lower_exact'], p['upper_exact'], r['lower_exact'], r['upper_exact']])
        assert 0 <= pl <= pu and 0 <= rl <= ru
        lo, hi = max(pl, rl), min(pu, ru); assert lo <= hi
        rows.append({'order': p['order'], 'lower_exact': str(lo), 'upper_exact': str(hi)})
    assert reduction['containing_intersections'] == rows
    assert c.contract.measured(primary)[1] <= c.contract.measured(reduction)[0]
    return {'radius_exact': c.ENDPOINT_GEOMETRY[region]['radius_exact'], 'source': c.SOURCE, 'laplacian_energies': rows}
