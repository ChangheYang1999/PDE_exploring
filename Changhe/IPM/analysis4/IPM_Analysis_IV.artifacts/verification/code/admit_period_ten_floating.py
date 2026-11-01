"""Replay and admit finite Q10 norms, responses and printed-data line fits."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import argparse, gzip, json, re, sys
sys.dont_write_bytecode = True
from flint import arb, fmpq, ctx
from certificate_admission import read, ref, checkref, reviewed, next_entry
ctx.prec = 1536
ap = argparse.ArgumentParser()
ap.add_argument('--entry', type=int, required=True)
ap.add_argument('--review', required=True)
a = ap.parse_args()
base = Path('research/298_period_ten_floating_audit')
evidence = base/'verification/checks.json.gz'
d = read(evidence)
assert d['all_checks_pass'] and d['bits'] == 768 and len(d['results']) == 14
for source in d['inputs'] + [row['source'] for row in d['results']]:
    checkref(source)
review = reviewed(base, a.review)
ledger, old = next_entry(a.entry)
assert not (base/'verification/admission.json').exists()
def ball(q):
    q = Fraction(q)
    return arb(fmpq(q.numerator, q.denominator))
fittext = (base/'sources/fit_hhf_Q10_N300.out').read_text()
counts = {'norms': 0, 'responses': 0, 'fits': 0, 'rounding_bins': 0}
limits = {key: Fraction(0) for key in ['norm_log', 'relative_exact', 'relative_binary', 'relative_root_effect']}
replays = []
for row in d['results']:
    assert row['announced_density_order'] == 300 and row['last_printed_order'] == 299 and row['maximum_fit_endpoint'] == 290
    assert row['norm_comparisons'] == 39 and row['response_comparisons'] == 28
    assert [x['blocks'] for x in row['fits']] == [20, 15, 10]
    assert row['printed_fit_rounding_matches']
    for key, saved in row['maxima'].items():
        bound = Fraction(saved['strict_bound'])
        assert bound > 0 and arb(saved['value']) < ball(bound)
        limits[key] = max(limits[key], bound)
    for item in row['norms']:
        assert arb(item['absolute_log_discrepancy']) < ball(row['maxima']['norm_log']['strict_bound'])
        counts['norms'] += 1
    for item in row['responses']:
        for key in ['relative_exact', 'relative_binary', 'relative_root_effect']:
            assert arb(item[key]) < ball(row['maxima'][key]['strict_bound'])
        counts['responses'] += 1
    data = {}
    for line in Path(row['source']['path']).read_text().splitlines():
        if line.startswith('n '):
            _, n, f, g = line.split()
            data[int(n)] = (Fraction(f), Fraction(g))
    assert set(data) == set(range(1, 300))
    blocks = [(Fraction(end), max(data[n][0] for n in range(end-9, end+1)), max(data[n][1] for n in range(end-9, end+1))) for end in range(10, 300, 10)]
    fitline = next(line for line in fittext.splitlines() if line.startswith(Path(row['source']['path']).name + ' '))
    printed = re.findall(r'n>=(\d+) A_f=([^ ]+) A_g=([^ ]+) rms=([^ ]+)', fitline)
    assert len(printed) == 3
    for fit, bins in zip(row['fits'], printed):
        lo, pf, pg, prms = bins
        assert fit['lo'] == int(lo)
        sample = [b for b in blocks if b[0] >= int(lo)]
        assert len(sample) == fit['blocks'] and sample[-1][0] == fit['last_endpoint'] == 290
        mx = sum(b[0] for b in sample)/len(sample)
        for j, channel in enumerate(fit['channels'], 1):
            my = sum(b[j] for b in sample)/len(sample)
            slope = sum((b[0]-mx)*(b[j]-my) for b in sample)/sum((b[0]-mx)**2 for b in sample)
            intercept = my-slope*mx
            mse = sum(((b[j]-my)-slope*(b[0]-mx))**2 for b in sample)/len(sample)
            assert slope == Fraction(channel['slope']) and intercept == Fraction(channel['intercept'])
            A = (ball(slope)*arb(10).log()).exp()
            R = (ball(5*slope)*arb(10).log()).exp()
            rms = ball(mse).sqrt()
            assert A.overlaps(arb(channel['A'])) and R.overlaps(arb(channel['R'])) and rms.overlaps(arb(channel['rms']))
            assert abs(A-ball(pf if j == 1 else pg)) < ball('0.00005')
            counts['rounding_bins'] += 1
            if j == 1:
                assert abs(rms-ball(prms)) < ball('0.005')
                counts['rounding_bins'] += 1
            counts['fits'] += 1
            replays.append({'root_index': row['root_index'], 'lo': int(lo), 'channel': channel['channel'], 'slope': str(slope), 'intercept': str(intercept), 'A': A.str(55), 'R': R.str(55), 'rms': rms.str(55)})
assert counts == {'norms': 546, 'responses': 392, 'fits': 84, 'rounding_bins': 126}
now = datetime.now(timezone.utc).isoformat(timespec='seconds')
replay = base/'verification/centered_fit_replay.json.gz'
replay.write_bytes(gzip.compress(json.dumps({'at': now, 'all_checks_pass': True, 'bits': ctx.prec, 'evidence': ref(evidence), 'counts': counts, 'fits': replays}, separators=(',', ':')).encode(), mtime=0))
result = f"All fourteen runs pass546 exact-root low-order norm comparisons,392 affine response comparisons at indices2..29,84 complete-block line fits and126 printed rounding bins. Every producer announces density order300 and prints norms through299; the complete-block fits end at290 with20,15,10 blocks. Uniform strict discrepancy bounds are norm-log<{limits['norm_log']}, response-relative-to-exact<{limits['relative_exact']}, response-relative-to-binary<{limits['relative_binary']}, and root-rounding-effect<{limits['relative_root_effect']}. A separate1536-bit centered covariance replay gives identical rational slopes and intercepts and overlapping directed A, A^5 and RMS enclosures. The original finite audit took{d['actual_elapsed_s']:.6f}seconds."
scope = 'CONFIRMED for finite comparisons and printed-data statistics. The high-order binary64 arrays are not enclosed. These fits provide no asymptotic growth law, sharp radius or new convergence theorem.'
proof = base/'PROOF.md'
(base/'sources'/f'PROOF_before_V{a.entry}.md').write_bytes(proof.read_bytes())
s = proof.read_text(); start = s.index('Status:'); end = s.index('\n', start)
proof.write_text(s[:start]+f'Status: finite checks CONFIRMED in V{a.entry} on {now}.'+s[end:]+f'\n## Completed checks\n\n{result}\n\n{scope}\n')
snapshot = base/'sources'/f'PROOF_at_V{a.entry}.md'; snapshot.write_bytes(proof.read_bytes())
receipt = {'at': now, 'entry': a.entry, 'all_checks_pass': True, 'verdict': 'CONFIRMED_FINITE', 'evidence': ref(evidence), 'fit_replay': ref(replay), 'proof': ref(snapshot), 'independent_review': ref(review), 'uniform_strict_error_bounds': {k:str(v) for k,v in limits.items()}, 'scope': scope}
(base/'verification/admission.json').write_text(json.dumps(receipt, indent=2)+'\n')
ledger.write_text(old+f'\n## V{a.entry} | {now} | Period-ten floating-data audit\n\n**Claim.** The fourteen printed Q10 runs agree with the exact early norms and affine responses, and the stated fits reproduce their complete-block data.\n\n**Method.** Directed exact-root and binary-root evaluations, rational printed-data least squares and a separate centered covariance replay.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {base}/verification/admission.json.\n')
table = ['# Period-ten printed-data density fits', '', f'Checked {now}; V{a.entry}. Unit amplitude; radius diagnostic A^5. All fits end at complete-block endpoint290. These are finite diagnostics, not infinite-series bounds.', '', '| Root | Cutoff100 | Cutoff150 | Cutoff200 |', '|---|---:|---:|---:|']
for row in d['results']:
    table.append('| '+str(row['root_index'])+' | '+' | '.join(arb(f['channels'][0]['R']).str(13) for f in row['fits'])+' |')
(base/'verification/FIT_TABLE.md').write_text('\n'.join(table)+'\n')
notes = Path('NOTES_FOR_TEAM.md'); notes.write_text(f'## {now} VERIFIER -> LEAD: V{a.entry} admits Q10 finite floating-data checks\n\n{result}\n\n{scope} Density radius diagnostics: {base}/verification/FIT_TABLE.md.\n\n'+notes.read_text())
for name, line in [('WORKLOG.md', f'{now}: V{a.entry} admitted Q10 finite floating-data audit.'), ('VERIFY_SUMMARY.md', f'V{a.entry}: {result} {scope}'), ('research/INDEX.md', f'Update {now}: topic298 finite checks CONFIRMED in V{a.entry}.')]:
    with Path(name).open('a') as f: f.write('\n'+line+'\n')
(base/'sources/admit_period_ten_floating.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps({'at': now, 'entry': a.entry, 'counts': counts, 'limits': {k:str(v) for k,v in limits.items()}}))
