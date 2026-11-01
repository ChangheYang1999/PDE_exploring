"""Record a completed finite continuation audit, with an explicit ledger id."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys
sys.dont_write_bytecode=True
p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);p.add_argument('--ledger',type=int,required=True);a=p.parse_args();N=a.N;tag='V'+str(a.ledger)
root=Path('research/266_later_conditional_continuations');v=root/f'N{N}'/'verification'
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def put(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
def mid(s):return float(s.strip('[]').split()[0])
x=json.loads((v/'checks.json').read_text());y=json.loads((v/'drift_fit_checks.json').read_text())
assert x['all_checks_pass'] and y['all_checks_pass'] and x['target_order']==N
assert x['source_sha256']==y['source']['sha256']
assert y['orders']==[348,N] and y['count_per_field']==N-347
assert x['printed_comparisons']==59
ledger=Path('VERIFY_REPORT.md');assert f'## {tag} ' not in ledger.read_text()
fit=y['fits']['357']['F'];beta=mid(fit['logarithmic']['slope']);alim=mid(fit['inverse_order']['limiting_multiplier_display']);slope=mid(fit['per_order']['slope'])
rms=[mid(fit[k]['rms']) for k in ('logarithmic','inverse_order','per_order')]
final=x['rows'][-1];lf=mid(final['fields']['f']['log10_norm']);lg=mid(final['fields']['g']['log10_norm'])
text=f'''\n\n## {tag} | {now} | Conditional continuation through order{N}\n\n**Claim.** The stored midpoint continuation through{N} reproduces the stated norm statistics, finite shifted-profile fits and final-three-order Poisson identities.\n\n**Method.** Independently sum every stored coefficient at768 bits, compare the previous norm enclosures, test all final-three-order Poisson coefficients, and recompute full-vector least-squares multipliers and fits. Record the exact loaded checkpoint hash.\n\n**Result.** All{x['norm_coefficient_positions']:,} norm positions, {x['poisson_coefficients']:,} Poisson coefficients, {x['canonical_constants']} resonant zero constant, {x['printed_comparisons']} norm/increment/hump comparisons and{x['prior_norm_comparisons']} previous norm overlaps pass. The shifted audit covers{y['count_per_field']} orders per field with{y['prior_interval_comparisons']} prior interval comparisons. At{N}, log10 M={lf:.10f}, log10 N={lg:.10f}. On357..{N}, the density fits give beta={beta:.10f}, inverse-order fitted limit={alim:.10f}, and per-order log slope={slope:.12f}; RMS residuals are{rms[0]:.8f}, {rms[1]:.8f}, {rms[2]:.8f}. Actual calculation times are{x['actual_elapsed_s']:.3f} and{y['actual_elapsed_s']:.3f}seconds.\n\n**Verdict: CONFIRMED for finite arithmetic conditional on the loaded reset input; OPEN for all-order growth or convergence.** The displayed precision-monitor column is outside these59 comparisons and has a separate audit. Narrow new intervals do not recover uncertainty discarded at329. Evidence: {root}/PROOF.md and N{N}/verification/admission.json.\n'''
with ledger.open('a') as f:f.write(text)
proof=root/'PROOF.md'
if not (root/'sources/PROOF_before_first_admission.md').exists():(root/'sources/PROOF_before_first_admission.md').write_bytes(proof.read_bytes())
s=proof.read_text().replace('Status: verification protocol written before the next reported checkpoints. No infinite convergence or asymptotic law is claimed.','Status: completed targets are admitted separately below. No infinite convergence or asymptotic law is claimed.')
s=s.replace('Compare every available displayed number in the latest ten-order table using its stated rounding.','Compare the norm, increment, ratio and hump entries in the latest ten-order table using their stated rounding. The precision monitor and residue class have a separate bookkeeping audit.')
s+=f'''\n## Order{N}: admitted {now}\n\n{tag} confirms{x['norm_coefficient_positions']:,} coefficient positions, {x['poisson_coefficients']:,} final-three-order Poisson identities and59 printed norm/increment/hump comparisons. The full-vector audit covers348..{N} in both fields. The density fits on357..{N} have beta={beta:.10f}, inverse-order fitted limit={alim:.10f}, and per-order log slope={slope:.12f}. These are finite statistics of the midpoint continuation. The three fit families are not certified asymptotic laws. The final checkpoint's top-level reset flag can be absent because the live producer predates the provenance repair; that absence does not make the computation canonical. The two main arithmetic stages took{x['actual_elapsed_s']:.3f} and{y['actual_elapsed_s']:.3f}seconds.\n'''
proof.write_text(s)
proof_snapshot=root/f'N{N}'/'sources'/f'PROOF_at_{tag}.md';proof_snapshot.write_text(s)
put(v/'admission.json',dict(admitted_at_utc=now,ledger=tag,verdict='CONFIRMED_FINITE_CONDITIONAL_ONLY',target=N,source_sha256=x['source_sha256'],norm_and_poisson=ref(v/'checks.json'),shifted_fits=ref(v/'drift_fit_checks.json'),proof=ref(proof_snapshot),scope='No inherited reset uncertainty or infinite tail is certified. Precision-monitor column checked separately.'))
(root/f'N{N}'/'sources'/'unpack_dyadic4.py').write_bytes(Path('code/unpack_dyadic4.py').read_bytes())
notes=f'''## {now} VERIFIER -> TEAM: {tag} order{N} finite audit admitted\n\nAll{x['norm_coefficient_positions']:,} coefficient norm positions, {x['poisson_coefficients']:,} Poisson identities and59 printed norm/increment/hump comparisons pass. The full-vector fits cover348..{N}. On357..{N}, density beta={beta:.10f}, inverse-order fitted |a_inf|={alim:.10f}, per-order log slope={slope:.12f}; RMS={rms[0]:.8f},{rms[1]:.8f},{rms[2]:.8f}. At{N}, log10 M={lf:.10f}, log10 N={lg:.10f}. All are conditional on the329 midpoint reset and do not decide any infinite growth law. The precision-monitor column is being checked separately. Evidence266/N{N}/verification/admission.json.\n\n'''
p=Path('NOTES_FOR_TEAM.md');p.write_text(notes+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: {tag} admitted finite conditional norm/Poisson and full-vector fit audit through{N}; details in266/N{N}.\n')
print(json.dumps(dict(at=now,ledger=tag,N=N,beta=beta,inverse_limit=alim,per_order_slope=slope)))
