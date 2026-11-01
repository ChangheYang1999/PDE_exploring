"""Admit a completed finite precision-monitor audit, retaining reset provenance."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,re
p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);p.add_argument('--entry',type=int,required=True);a=p.parse_args()
root=Path('research/266_later_conditional_continuations');v=root/f'N{a.N}'/'verification'
now=datetime.now(timezone.utc).isoformat(timespec='seconds');tag=f'V{a.entry}'
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
x=json.loads((v/'radius_metadata_checks.json').read_text());prior=json.loads((v/'admission.json').read_text())
assert x['all_checks_pass'] and x['full_monitor_reconstructed'] and x['target_order']==a.N
assert x['source_sha256']==prior['source_sha256']
assert x['printed_radius_comparisons']==x['residue_class_comparisons']==10
assert all(r['full_monitor_reconstructed'] and not r['uncertain_pivots'] and not r['zero_midpoint_uncertain_columns'] for r in x['rows'])
ledger=Path('VERIFY_REPORT.md');assert int(re.findall(r'^## V(\d+) ',ledger.read_text(),re.M)[-1])==a.entry-1
assert not (v/'radius_metadata_admission.json').exists()
last=x['rows'][-1];n=a.N
text=f'''\n\n## {tag} | {now} | Order{n} finite precision monitor and reset provenance\n\n**Claim.** The last ten displayed precision-monitor values and residue classes agree with the stored conditional continuation.\n\n**Method.** Reconstruct the producer's column normalization and radius statistic with512-bit directed arithmetic, checking every pivot and retaining the checkpoint hash.\n\n**Result.** All ten monitor rounding bins and all ten residue classes agree. The order{n} monitor is{last['finite_pivot_monitor']}. Every required pivot is resolved; no uncertain column is skipped. The checkpoint has no top-level reset flag or retained reset ancestry, so external provenance from topics160 and189 remains necessary. The actual audit took{x['actual_elapsed_s']:.6f}seconds.\n\n**Verdict: CONFIRMED for the finite conditional monitor; OPEN for canonical-sequence error.** This statistic is not a bound on uncertainty discarded at order329. Evidence: {v}/radius_metadata_checks.json.\n'''
with ledger.open('a') as f:f.write(text)
proof=root/'PROOF.md';s=proof.read_text()+f'''\n### Order{n} monitor admitted {now}\n\n{tag} verifies all ten printed precision-monitor bins and residue classes through{n}. All normalization pivots are resolved. This is a finite statistic of the reset continuation. The checkpoint does not itself retain reset ancestry; the external provenance in topics160 and189 is required. No canonical error or convergence statement follows.\n''';proof.write_text(s)
snapshot=root/f'N{n}'/'sources'/f'PROOF_at_{tag}.md';snapshot.write_text(s)
(v/'radius_metadata_admission.json').write_text(json.dumps(dict(admitted_at_utc=now,verdict='CONFIRMED_FINITE_MONITOR_ONLY',ledger=tag,checks=ref(v/'radius_metadata_checks.json'),proof=ref(snapshot),missing_reset_metadata=not x['metadata_retains_reset'],canonical_uncertainty_certified=False),indent=2)+'\n')
notes=f'''## {now} VERIFIER -> TEAM: {tag} order{n} precision monitor checked\n\nAll ten monitor values and residue classes pass. At{n}, the normalized column-radius monitor is{last['finite_pivot_monitor']}. It is conditional on the order329 reset; the checkpoint still lacks reset metadata, so external provenance remains essential. The monitor is not the relative error of the canonical sequence.\n\n'''
p=Path('NOTES_FOR_TEAM.md');p.write_text(notes+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: {tag} admits the finite conditional precision monitor through{n}; all20 printed bookkeeping comparisons pass.\n')
print(json.dumps(dict(at=now,ledger=tag,N=n,monitor=last['finite_pivot_monitor'])))
