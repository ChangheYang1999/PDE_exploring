from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,re
sys.dont_write_bytecode=True
from flint import arb,ctx
from unpack_dyadic4 import unpack
BASE=Path('research/189_reset350_conditional_audit')
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
d=json.loads((BASE/'verification/checks.json').read_text());r=json.loads((BASE/'verification/replay.json').read_text())
assert d['all_checks_pass'] and r['all_checks_pass'] and r['poisson_replays']==d['poisson_coefficients']==121800
notes=Path('../a4-num/NOTES_FOR_TEAM.md').read_text();start=notes.index('## 2026-10-31T14:01Z');end=notes.index('\n## ',start+3)
correction=notes[start:end]+'\n'
(BASE/'sources/num_correction_1401.md').write_text(correction)
start=notes.index('## 2026-10-31T13:58Z');end=notes.index('\n## ',start+3)
(BASE/'sources/num_claims_1358.md').write_text(notes[start:end]+'\n')
ctx.prec=1024;rows={x['n']:x for x in d['rows']}
ratio=arb(*unpack(rows[332]['fields']['g']['norm']))/arb(*unpack(rows[331]['fields']['g']['norm']))
assert ratio>arb('4.79')
band=next(x for x in d['bands350'] if x['q']==40)['fields']['f'];nonfar=arb(band[0])+arb(band[1]);assert nonfar>arb('.004')
claims=[
 (372,'Order350 conditional arithmetic and table replay',
  'The finite diagnostics for the continuation from reset order329 midpoints agree with the stored arrays.',
  'Fresh 768-bit extraction from the hashed source, followed by a separate 1024-bit selected-archive replay, differential-operator Poisson reconstruction, Horner versus power polynomial evaluation, and exact rational band membership.',
  f'Orders324..350 include 1351611 coefficient positions. At348..350 all121800 Poisson coefficients and the canonical resonant constant pass. The first audit checks97 rounded mode-share entries; the replay checks6 norms,689 factorial-column comparisons,16 printed t-profile values and42 band values. Density/stream slopes over324..350 are -0.57938783705527378336 and -0.54996014549122461555. Original audit took {d["actual_elapsed_s"]} seconds; separate replay took {r["actual_elapsed_s"]} seconds. Source SHA256 {d["source_sha256"]}. Selected archive hash {r["archive_sha256"]}.',
  'CONFIRMED for these finite arithmetic statements conditional on the loaded midpoint arrays. Original canonical coefficients, inherited uncertainty, high-order nonlinear recurrence and infinite convergence are not established by this check.'),
 (373,'Numerical lane withdraws the inherited-uncertainty claim',
  'The unsupported13:58 uncertainty assertion challenged inV364 has been withdrawn.',
  'Read the14:01 numerical-lane correction and the corresponding current report caveats; retain the correction verbatim as source evidence.',
  'The numerical lane explicitly accepts that resetting radii loses the order329 input enclosure and that no propagated input-uncertainty bound is available for330..350. The proposed random boundary-point experiment is labelled a sensitivity diagnostic, not a bound.',
  'CONFIRMED as a correction of the report scope. The original canonical350 accuracy remains OPEN; the earlier unresetV271 certificates remain valid.'),
 (374,'Two finite-description counterexamples in the350 numerical note',
  'Both plain sums decrease at every order330..350, and every density column of degree at least40 is entirely in the far band.',
  'Evaluate the stream-norm ratio at332/331 and the exact band partition at350,q=40 from the independently audited interval summaries.',
  f'The conditional stream norm increases by a factor {ratio.str(35,radius=True)} at332. At350,q=40 the density near plus middle share is {nonfar.str(35,radius=True)}, while the far share is {band[2]}. Thus a range-wide monotonicity assertion and an exact all-far assertion fail. Safe descriptions are: both norms decline over this window overall; the stream norm has an upward step at332; atq40 about99.596% of the density column lies in the far band.',
  'REFUTED as exact descriptions of the displayed finite data. These counterexamples do not settle any asymptotic growth claim.')]
ledger=Path('VERIFY_REPORT.md');old=ledger.read_text();assert all(f'## V{k} |' not in old for k,*_ in claims)
for k,title,claim,method,result,verdict in claims:
 old+=f'\n## V{k} | {now} | {title}\n\nClaim: {claim}\n\nMethod: {method}\n\nResult: {result}\n\nVerdict: {verdict}\n'
ledger.write_text(old)
p=BASE/'PROOF.md';s=p.read_text().replace('Status: finite audit in progress. No claim about the discarded input uncertainty is made.','Status: CONFIRMED finite conditional arithmetic, V372. No claim about the discarded input uncertainty is made.')
s+=f'\n## Audit outcome, {now}\n\n'+claims[0][4]+'\n\nThe14:01 source correction explicitly agrees with this scope (V373). The two literal descriptions inV374 fail by the norm and band counterexamples retained in verification/narrative_counterexamples.json. Overall decay within a finite window does not imply pointwise monotonicity or infinite convergence.\n';p.write_text(s)
(BASE/'verification/narrative_counterexamples.json').write_text(json.dumps(dict(checked_at_utc=now,stream_ratio_332_331=ratio.str(40,radius=True),density_nonfar_share_n350_q40=nonfar.str(40,radius=True),verdict='REFUTED finite wording, not asymptotic behavior'),indent=2)+'\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} | V372-V374:350 conditional audit passed; two prose corrections\n\n'+claims[0][4]+'\n\n'+claims[2][4]+'\n\nPlease correct those two13:58 descriptions wherever they appear. The14:01 uncertainty correction is accepted and retained; random perturbation remains a diagnostic. Topic189/PROOF.md gives the scope and source hashes. No original canonical350 accuracy is being asserted.\n\n'+p.read_text())
p=Path('research/INDEX.md');s=p.read_text();s=s.replace('185. [Period-six finite audit](185_period_six_numerical_audit/PROOF.md): CONFIRMED root 6 through 60; later source-bound norms through 300.','185. [Period-six finite audit](185_period_six_numerical_audit/PROOF.md): CONFIRMED roots1,2,6 through60; later source-bound norms through300.')
s=s.replace('186. [Period-six prefix radii](186_period_six_prefix_radii/PROOF.md): PROVED root 6, exponent 79/2.','186. [Period-six prefix radii](186_period_six_prefix_radii/PROOF.md): PROVED roots1,2,6 with exponents38,42,79/2 respectively.')
s+='\n189. [Order350 conditional audit](189_reset350_conditional_audit/PROOF.md): CONFIRMED selected arithmetic and printed diagnostics; original canonical accuracy OPEN; two finite prose claims REFUTED.\n';p.write_text(s)
with Path('WORKLOG.md').open('a') as o:o.write(f'\n{now}: V372-V374 admitted. Conditional350 audit and replay passed; inherited-uncertainty correction accepted; finite monotonicity and exact all-far wording refuted.\n')
(BASE/'sources/admit_reset350.py').write_bytes(Path(__file__).read_bytes())
files={str(p.relative_to(BASE)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in BASE.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log'}
(BASE/'verification/MANIFEST.json').write_text(json.dumps(dict(checked_at_utc=now,files=files),indent=2)+'\n')
print(now,'admitted372-374')
