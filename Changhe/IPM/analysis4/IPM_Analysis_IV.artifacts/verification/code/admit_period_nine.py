"""Admit period-nine convergence only after all ten exact/interval replays."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json
root=Path('research/267_period_nine_tuning'); vf=root/'verification'
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
assert '## V551 ' not in Path('VERIFY_REPORT.md').read_text()
def ref(p):
 p=Path(p);return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def check_ref(r):
 assert ref(r['path'])['sha256']==r['sha256'],r['path']
finite=json.loads((vf/'obstruction_admission.json').read_text())
assert finite['verdict']=='PROVED_FINITE_ALGEBRA' and finite['root_count']==10 and finite['degree']==18
for key in ['proof','obstruction','independent_comparison']:check_ref(finite[key])
lead=json.loads((vf/'lead_review.json').read_text())
assert lead['review_status']=='ACCEPTED_PROTOCOL_PENDING_RECEIPTS';check_ref(lead['review'])
rows=[]
for i in range(1,11):
 p=vf/f'root{i}_review.json';d=json.loads(p.read_text())
 assert d['all_checks_pass'] and d['root_index']==i and d['Q']==9 and d['h']==1
 assert d['exact_prefix_coefficients']==1978 and d['exact_scalar_identities']==54
 assert d['finite_responses_recomputed']==25 and d['full_compact_comparisons']==8
 assert d['complete_partition_replayed'] and d['exact_box_replayed'] and d['independent_polynomial_norms_checked']
 assert d['taylor_replay']=='separate term summation with shared audited jet algebra'
 assert d['arithmetic_bits']==1024 and d['amplitude_exponent']=='9/2'
 assert F(d['radius_exponent'])==F(d['q'],2) and F(d['s'])>0
 check_ref(d['receipt']);c=json.loads(Path(d['receipt']['path']).read_text())
 assert c['all_checks_pass'] and c['N']==18 and c['K']==19 and c['B']==4 and c['arithmetic_bits']==768
 for value in c.values():
  if isinstance(value,dict) and set(['path','sha256'])<=set(value):check_ref(value)
 rows.append(dict(root=i,s=d['s'],q=d['q'],radius_exponent=d['radius_exponent'],leaf_counts=d['leaf_counts'],review=ref(p)))
common=str(F(max(r['q'] for r in rows),2)); qs=','.join(str(r['q']) for r in rows)
p=root/'PROOF.md';s=p.read_text()
s=s.replace('# Period-nine compatibility and a conditional convergence certificate','# Ten convergent tuned profiles at delta=2/9')
s=s.replace('Status: independent protocol written before computation. No period-nine branch is admitted yet.','Status: PROVED in V549 and V551 after exact obstruction algebra, ten complete response and box replays, and the lead\'s independent protocol review.')
s=s.replace('Exact real-root counts, irreducibility and numerical constants remain unasserted until the receipts pass.','The exact algebra gives ten simple real roots of an irreducible degree18 polynomial. All ten satisfy the response and majorant hypotheses, with the constants recorded below.')
s+='\n## Completed convergence certificates\n\nThe ten roots are ordered increasingly in the exact obstruction receipt. For each root the 768-bit construction and 1024-bit replay check 25 finite responses,8 full/compact comparisons, all 1,978 signed exact-prefix coefficients, a complete closed Taylor cover, and 54 exact rational scalar identities. The replay sums Taylor terms separately while sharing the audited jet algebra. Each row gives a unit-amplitude response lower bound and a sufficient exterior R>2^(q/2)|epsilon|^(9/2).\n\n| Root | Response lower bound | q | Radius exponent |\n|---|---:|---:|---:|\n'
for r in rows:s+=f"| {r['root']} | {r['s']} | {r['q']} | {r['radius_exponent']} |\n"
s+=f'\nThe common sufficient radius is 2^({common})|epsilon|^(9/2). All weighted derivatives converge on every strict closed exterior, and the common-potential expansion solves the stationary equation exactly there. Topic270 separately proves that its order9 potential logarithm is nonzero at every root. These conclusions do not assert a sharp radius, a pure potential, or a whole-plane stationary extension. All certificate hashes are recorded in verification/admission.json.\n';p.write_text(s)
snapshot=root/'sources/PROOF_at_V551.md';snapshot.write_text(s)
(vf/'admission.json').write_text(json.dumps(dict(admitted_at_utc=now,verdict='PROVED',ledger='V551',rows=rows,amplitude_exponent='9/2',common_radius_exponent=common,proof=ref(snapshot),finite_algebra=ref(vf/'obstruction_admission.json'),independent_protocol_review=ref(vf/'lead_review.json'),taylor_replay='separate term summation with shared audited jet algebra'),indent=2)+'\n')
with Path('VERIFY_REPORT.md').open('a') as f:f.write(f'''\n\n## V551 | {now} | Ten convergent profiles at delta2/9\n\n**Claim.** Every real root of the irreducible period-nine compatibility polynomial gives a uniquely tuned convergent density and stream series with a convergent common-potential expansion.\n\n**Method.** Check V549's exact obstruction and independent polar agreement; audit all ten 768-bit interval constructions and 1024-bit replays; verify 1,978 signed exact-prefix coefficients,25 finite responses,8 full/compact comparisons, complete closed interval covers and 54 exact rational majorant identities per root. Combine these receipts with the lead's accepted independent protocol review. The replay sums Taylor terms separately and shares the audited jet algebra.\n\n**Result.** Every check passes. In increasing-root order the q values are{qs}. The sufficient exteriors are R>2^(q/2)|epsilon|^(9/2), with common exponent{common}. All weighted derivatives converge on every strict closed exterior and justify the exact stationary equation. V550 proves a nonzero first-period potential logarithm for all ten branches.\n\n**Verdict: CONFIRMED and PROVED.** The explicit-profile count rises from 63 to 73:62 two-mode, seven Candidate-shaped, and four single-harmonic profiles. No sharp convergence boundary or whole-plane extension is claimed. Evidence: research/267_period_nine_tuning/PROOF.md and verification/admission.json.\n''')
p=Path('code/build_current_radius_table.py');s=p.read_text();marker="add(Path('research/174_adaptive_majorant_boxes/verification/prefix_N90_sharp.json'),'two-mode',5,90)";assert marker in s
new="""# Ten period-nine roots admitted in V551.
folder=Path('research/267_period_nine_tuning/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
for index in range(1,11):
    review=json.loads((folder/f'root{index}_review.json').read_text());assert review['all_checks_pass']
    add(folder/f'root{index}_box.json.gz','two-mode',index)
""";assert new not in s;p.write_text(s.replace(marker,new+marker))
p=Path('VERIFY_SUMMARY.md');s=p.read_text().replace('63 profiles have','73 profiles have').replace('contains63 profiles:52 two-mode','contains73 profiles:62 two-mode')
s=s.replace('All63 certificate hashes, radius powers and amplitude powers match the lead\'s frozen summary in V546.','The prior63 certificate hashes, radius powers and amplitude powers match the lead\'s frozen summary in V546. V551 adds ten period-nine certificates.')
old='The period-nine proposal at delta2/9 remains OPEN pending its exact algebra, complete response covers, rational boxes and replay receipts. It is not included in the count63.'
new=f'At delta2/9, V549 proves the irreducible degree18 compatibility polynomial has ten simple real roots. V551 admits all ten complete convergence certificates, with q values {qs}, physical exponent q/2, amplitude exponent9/2 and common sufficient exponent{common}. V550 proves a nonzero order9 common-potential logarithm at every root.'
assert old in s;s=s.replace(old,new).replace('All40 two-mode h=1 profiles at Q3 throughQ8','All50 two-mode h=1 profiles at Q3 throughQ9').replace('(V476,V533,V536).','(V476,V533,V536,V550).');p.write_text(s)
p=Path('research/INDEX.md');s=p.read_text().replace('conditional proof and independent exact obstruction protocol. No branch admitted yet.','PROVED in V549/V551: exact obstruction and ten complete convergence certificates.').replace('[Period-nine first potential logarithm](270_period_nine_potential_log/PROOF.md): conditional protocol, not yet admitted.','[Period-nine first potential logarithm](270_period_nine_potential_log/PROOF.md): PROVED in V550 by exact polar/Cartesian agreement and a unit polynomial gcd.');p.write_text(s)
notes=f'''## {now} VERIFIER -> TEAM: V551 admits all ten Q9 roots ;73 profiles\n\nEvery period-nine response and rational majorant replay passes. The ten q values, in increasing-root order, are{qs}; exteriors R>2^(q/2)|epsilon|^(9/2), common exponent{common}. The total is now73 profiles:62 two-mode,7 Candidate-shaped,4 single-harmonic. Each replay checks1,978 signed prefix coefficients,25 finite responses,8 overlaps, a complete closed cover and 54 scalar identities. It sums Taylor terms separately while sharing the audited jet algebra.\n\nV549 already establishes the exact irreducible P18 and all ten roots; V550 proves a nonzero first-period potential logarithm at each root. Please integrate with your accepted19:28Z protocol review and the final report. Full all-root receipts and proof: research/267_period_nine_tuning/verification/admission.json.\n\n'''
p=Path('NOTES_FOR_TEAM.md');p.write_text(notes+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V551 admits all ten period-nine roots after all interval, exact-prefix and rational-box replays. Total73 profiles; q={qs}; common exponent{common}. Updated proof, summary, reading index and radius generator.\n')
print(now,'V551 admitted',qs,'common',common)
