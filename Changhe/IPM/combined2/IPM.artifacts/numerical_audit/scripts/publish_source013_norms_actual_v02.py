"""Write complete source013 norm results after the six successful finite stages."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import comb
import argparse, json, sys
sys.set_int_max_str_digits(0)
R = Path(__file__).resolve().parents[1]
B = R / 'research/source013_norms'
def h(path):
    value = sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            value.update(block)
    return value.hexdigest()
def read(path):
    return json.loads(path.read_text())
def display(pair, digits=22):
    lo, hi = map(Q, pair)
    assert 0 <= lo <= hi
    scale = 10**digits
    lower = lo.numerator * scale // lo.denominator
    upper = -((-hi.numerator * scale) // hi.denominator)
    def text(integer):
        assert integer >= 0
        return str(integer // scale) + '.' + str(integer % scale).zfill(digits)
    strings = [text(lower), text(upper)]
    assert Q(strings[0]) <= lo <= hi <= Q(strings[1])
    return strings
p = argparse.ArgumentParser()
p.add_argument('--request-number', type=int, required=True)
p.add_argument('--publication', type=int, required=True)
a = p.parse_args()
paths = [B / f'verification/{kind}_publication_v01/result.json' for kind in ['weighted', 'unweighted']]
w, u = map(read, paths)
receipt = R / 'research/post_handoff_preparation/verification/compute_source013_complete_norms_v01/execution.json'
request = R / f'research/wait_stage_preparation/verification/preparation_request_v{a.request_number:02d}.json'
e, request_data = read(receipt), read(request)
assert e['status'] == 'COMPLETED' and e['reason'] is None and e['old_process_signals'] == 0
assert len(e['stages']) == 6 and all(row['exit_code'] == 0 for row in e['stages'])
assert e['request'] == str(request.relative_to(R)) and e['request_sha256'] == h(request)
assert w['kind'] == 'weighted' and u['kind'] == 'unweighted' and w['source'] == u['source']
assert w['source']['raw_sha256'] == 'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'
for d in [w, u]:
    assert d['status'] == 'CERTIFIED_NORMS' and d['checks'] > 0 and d['independent_checks'] > 0
    assert d['manifest_sha256'] == '55bbbee074de66aab59fd80aed97aec4a531ce8955f68f118f91534bc7ed7979'
    assert d['review_sha256'] == 'f477b08200c72b21e0cbebeaa5b523bcafd973805ef83b9190cb57f2f07edbbd'
    for group in [d['input_files'], d['files']]:
        for name, value in group.items():
            assert h(R / name) == value, name
for name, value in request_data['files'].items():
    assert h(R / name) == value, name
weighted = w['output']
assert weighted['fractional_order_exact'] == '21/10'
assert [row['order'] for row in weighted['integer_norms']] == list(range(4))
energies = []
for k, row in enumerate(weighted['integer_norms']):
    lo = sum((comb(k, j) * Q(weighted['tensor_energies'][j]['lower_exact']) for j in range(k+1)), Q(0))
    hi = sum((comb(k, j) * Q(weighted['tensor_energies'][j]['upper_exact']) for j in range(k+1)), Q(0))
    assert lo == Q(row['energy_lower_exact']) and hi == Q(row['energy_upper_exact'])
    l, v = map(Q, row['norm_interval_exact'])
    assert 0 <= l <= v and l*l <= lo <= hi <= v*v
    energies.append((lo, hi))
fl, fu = map(Q, weighted['fractional_norm_interval_exact'])
assert 0 <= fl <= fu and energies[1][1] > 0
assert fl**20 <= max(energies[2][0]**10, energies[2][0]**11/energies[1][1])
assert fu**20 >= energies[2][1]**9 * energies[3][1]
assert len(u['output']['panels']) == 114
unweighted = u['output']['values']
ll, lu = map(Q, unweighted['norm_interval_exact'])
el, eu = map(Q, unweighted['energy_interval_exact'])
assert 0 <= ll <= lu and ll*ll <= el <= eu <= lu*lu
integer_rows = []
for row in weighted['integer_norms']:
    interval = display(row['norm_interval_exact'])
    integer_rows.append(f'| {row["order"]} | {interval[0]} | {interval[1]} |')
frac, plain = display(weighted['fractional_norm_interval_exact']), display(unweighted['norm_interval_exact'])
now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
folder = B / 'results/whole_plane'
assert not folder.exists()
proof = f'''# Whole-plane residual norms for source013

Written {now} after all six finite stages completed. The independent actual-output review is pending.

## Exact statement and hypotheses

Fix c = 4076476460239181/2251799813685248, authoritative Candidate007 with exact input hash ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21, and correction013 with canonical input hash 2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33. Let psi = partial_y chi_007 + phi_013, rho = -Delta psi, u = (-psi_xy,psi_xx), F = (cX+u).grad rho-rho, W(X) = sqrt(1+4|X|^2), and g = WF. Use the unitary Fourier transform and the inhomogeneous Sobolev norm

    N_s(g)^2 = integral (1+|xi|^2)^s |g_hat(xi)|^2 dxi.

Assume the accepted source identities, containing primary arithmetic, complete analytic remainders and actual independently reviewed regional certificates listed in ../../PROOF.md and the exact finite request retained in verification/bindings_v01.json. Then g belongs to H^3 and has these containing integer-norm intervals:

| m | Lower N_m(g) | Upper N_m(g) |
|---|---:|---:|
{chr(10).join(integer_rows)}

The complete P-S1 fractional norm satisfies

    {frac[0]} <= N_(21/10)(g) <= {frac[1]}.

The unweighted residual satisfies

    {plain[0]} <= ||F||_2 <= {plain[1]}.

Every decimal here is rounded outward by an exact rational comparison. These are full-plane norms of this fixed source, not sampled diagnostics.

## Complete argument

For j = 0,1,2,3 let [L_j,U_j] be the sum of the containing integrals of the full ordered Cartesian tensor |D^j g|^2 over the origin disk r <= 1/50, all 114 annular panels 1/50 <= r <= 10000, and the infinite exterior r >= 10000. The six annulus blocks and both endpoint regions have actual independently reviewed source identities and complete analytic remainders. Their overlaps are null circles, so addition of their exact endpoints contains the whole-plane energies. Smoothness identifies the classical derivatives with the weak derivatives. Their square integrability proves g in H^3.

Parseval and the binomial theorem give N_m(g)^2 = sum_(j=0)^m binom(m,j) integral |D^j g|^2. Thus E_m^- = sum binom(m,j)L_j and E_m^+ = sum binom(m,j)U_j contain its square. Both containing computations verify the square-root endpoints by exact squaring. The publication script independently checks all four binomial sums and squares.

Holder interpolation gives N_(21/10)(g) <= ((E_2^+)^9 E_3^+)^(1/20). Monotonicity gives the lower sqrt(E_2^-). Interpolating order 2 between orders 1 and 21/10 gives the additional lower ((E_2^-)^11/E_1^+)^(1/20). Taking the larger lower proves the fractional interval. Its endpoints satisfy the exact twentieth-power inequalities, checked in both numerical routes and again here. No interpolation equality or unresolved inverse constant is assumed.

For the unweighted norm, divide the analytic weighted zeroth radial integrand by 1+4r^2 on each annular panel. Its strictly positive complex-disk denominator lower bound gives an analytic quotient with a complete Cauchy remainder. One route integrates the exact rational reciprocal coefficients, selecting each original coefficient endpoint according to the exact sign of its integration weight. The independent route encloses the formal reciprocal by truncated Newton iteration at higher precision. Both include every Taylor-tail allowance, so their nonempty interval intersection contains the same panel integral. The exact source and all 114 panel identities are rechecked; no local interval is reused for a different panel.

On the origin disk, 1 <= W^2 <= 1+4/2500 gives the lower weighted energy divided by 1+4/2500 and the original weighted upper. On the infinite exterior W^2 >= 1+4*10000^2 gives upper weighted energy divided by that constant and lower zero. Summing these bounds and all quotient-panel intervals contains integral |F|^2. Exact squaring and outward decimal comparisons prove its displayed norm interval.

## Evidence, execution and scope

Weighted result ../../verification/weighted_publication_v01/result.json: SHA256 {h(paths[0])}; unweighted result ../../verification/unweighted_publication_v01/result.json: SHA256 {h(paths[1])}. Each retains its separate primary and independent reduction records and every regional dependency. The six-stage execution ran {e['started_utc']} to {e['finished_utc']}, elapsed {e['elapsed_seconds']} seconds, six zero exits, no stop reason and no old-process signals. Receipt SHA256 {h(receipt)}. Local verification/bindings_v01.json contains exact source, result, request, receipt, proof and display bindings. No Lean formalization or build is claimed.

This conditional result awaits independent actual-output review. It covers P-S1 and unweighted L2 only; P-S2 and the strong Holder norm S_F are different quantities. It supplies no background gap, near or far coefficient bound, full inverse, invariant-ball closure or stationary existence theorem. No closure ratio can be computed without the missing same-source hypotheses.
'''
folder.mkdir(parents=True)
(folder / 'verification').mkdir()
(folder / 'formal').mkdir()
(folder / 'PROOF.md').write_text(proof)
(folder / 'formal/README.md').write_text('No Lean formalization or build is claimed. Exact certificates and the standalone informal argument are adjacent.\n')
record = {'status': 'COMPLETED_PENDING_ACTUAL_REVIEW', 'created_utc': now, 'source': w['source'], 'outward_decimal_intervals': {'P-S1_H21_10': frac, 'unweighted_L2': plain}, 'files': {str(path.relative_to(R)): h(path) for path in [*paths, receipt, request, B / 'PROOF.md', Path(__file__), folder / 'PROOF.md']}}
with (folder / 'verification/bindings_v01.json').open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
text = f'''# Numerical audit exchange v{a.publication}

Published {now}.

The complete same-source calculation for correction013 gives these outward whole-plane residual norm intervals:

    {plain[0]} <= ||F||_2 <= {plain[1]},
    {frac[0]} <= ||sqrt(1+4r^2) F||_(H^(21/10)) <= {frac[1]}.

The full integer H0 through H3 intervals, exact source, hypotheses and complete argument are in {folder.relative_to(R)}/PROOF.md. The result uses every source013 origin, annulus and infinite-exterior contribution. All 114 annular panels enter the unweighted analytic quotient with full remainders. Exact rational binomial sums, square-root endpoints, twentieth-power inequalities and decimal rounding have been independently checked. No value from source009 is transferred.

To AT: review both actual results and the successful common six-stage request {a.request_number} receipt. Weighted: {paths[0].relative_to(R)}, SHA256 {h(paths[0])}. Unweighted: {paths[1].relative_to(R)}, SHA256 {h(paths[1])}. Receipt: {receipt.relative_to(R)}, SHA256 {h(receipt)}. The execution ran {e['started_utc']} to {e['finished_utc']}, elapsed {e['elapsed_seconds']} seconds, all six exits zero, no old-process signals. Actual independent output reviews remain OPEN.

Verdict: OPEN pending independent actual-output review. The displayed intervals are completed conditional calculations under the named exact-source and containing regional hypotheses. These are P-S1 and plain L2 quantities only. P-S2, S_F, global background, near/far closure, full inverse, invariant ball and existence remain OPEN. The chain center, Candidate007 and c are unchanged; no closure ratio is asserted.
'''
with (R / f'exchange/audit_v{a.publication}.md').open('x') as stream:
    stream.write(text)
notes = R / 'NOTES_FOR_TEAM.md'
notes.write_text(text + '\n## Earlier notes\n\n' + notes.read_text())
with (R / 'VERIFY_REPORT.md').open('a') as stream:
    stream.write(f'\n## AN{a.publication} | {now}\n\nClaim: the fixed source013 has the displayed whole-plane P-S1 and plain L2 intervals. Method: complete same-source regional assembly, two containing analytic quotient reductions on all 114 panels, independent exact binomial, root-power and outward-rounding checks. Result: plain L2 {plain}, P-S1 H^(21/10) {frac}; successful receipt {h(receipt)}. Verdict: OPEN pending actual independent output review; the conditional arithmetic completed, and other norms and existence remain OPEN. Full proof: {folder.relative_to(R)}/PROOF.md.\n')
with (R / 'WORKLOG.md').open('a') as stream:
    stream.write(f'\n{now}: Published {a.publication}, completed source013 whole-plane norm calculation from six-stage request {a.request_number}; submitted both actual outputs and common receipt for independent review.\n')
with (R / 'research/README.md').open('a') as stream:
    stream.write('\n- [Source013 whole-plane residual norms](source013_norms/results/whole_plane/PROOF.md): complete P-S1 Sobolev and plain L2 intervals with exact source and verification evidence.\n')
print('PUBLISHED', a.publication, now, h(paths[0]), h(paths[1]), h(receipt), flush=True)
