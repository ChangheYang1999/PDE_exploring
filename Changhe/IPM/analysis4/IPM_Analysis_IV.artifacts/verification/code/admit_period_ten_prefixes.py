"""Admit completed Q10 prefix certificates after both independent replays."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from fractions import Fraction
import argparse, gzip, json, re, sys
sys.dont_write_bytecode = True
from flint import arb, fmpq, ctx
ctx.prec = 1536
ROOT = Path('research/286_period_ten_prefixes')

def read(p):
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)

def ref(p):
    return dict(path=str(p), sha256=sha256(p.read_bytes()).hexdigest())

def checkref(r):
    assert ref(Path(r['path'])) == {k:r[k] for k in ('path','sha256')}

ap = argparse.ArgumentParser()
ap.add_argument('--entry', type=int, required=True)
ap.add_argument('--review', required=True)
a = ap.parse_args()
ledger = Path('VERIFY_REPORT.md')
old = ledger.read_text()
assert max(map(int, re.findall(r'^## V(\d+) \|', old, re.M))) == a.entry-1
assert not (ROOT/'verification/admission.json').exists()
bounds_admission = Path('research/285_period_ten_response_bounds/verification/admission.json')
ia = read(bounds_admission)
assert ia['all_checks_pass'] and ia['verdict']=='PROVED'
checkref(ia['evidence']);checkref(ia['replay'])
bounds = read(Path(ia['evidence']['path']))
for required in ['research/281_period_ten_finite_algebra/verification/obstruction_admission.json','research/282_period_ten_symbolic_response/verification/admission.json','research/283_period_ten_potential_log/verification/admission.json']:
    admission=read(Path(required));assert admission['all_checks_pass']
    for key in ['evidence','proof']:checkref(admission[key])
review=ROOT/'sources'/Path(a.review).name
if Path(a.review)!=review:review.write_bytes(Path(a.review).read_bytes())
assert len(review.read_text())>100
rows = []
for i in range(1,15):
    cart = ROOT/f'verification/Q10_root{i}_checks.json.gz'
    polar = ROOT/f'verification/Q10_root{i}_polar_replay.json.gz'
    scalar = ROOT/f'verification/Q10_root{i}_review.json'
    d,p,r = map(read, (cart,polar,scalar))
    assert all(x['all_checks_pass'] and x['Q']==10 and x['root_index']==i and x['maximum_order']==80 for x in (d,p,r))
    assert (d['bits'],p['bits'])==(1536,2048)
    assert p['source']==ref(cart) and r['source']==ref(cart)
    for source in d['inputs']+[d['exact_prefix']]:
        checkref(source)
    assert ia['evidence'] in d['inputs']
    assert arb(fmpq(d['s'])) > 0
    assert d['s']==bounds['rows'][i-1]['s']
    assert len(d['cases'])==len(r['cases'])==4
    assert [x['N'] for x in d['cases']]==[20,40,60,80]
    for x,y in zip(d['cases'],r['cases']):
        assert (x['N'],x['q'],x['box'])==(y['N'],y['q'],y['box'])
        assert y['exact_scalar_identities']==60
        checkref(x['box'])
    assert len(d['norms'])==len(p['norms'])==80
    assert len(d['harmonics'])==len(p['harmonics'])==7
    assert d['exact_prefix_comparisons']==800
    assert d['direct_response_checks']==1
    assert p['independent_norm_comparisons']==160 and p['independent_tuning_comparisons']==7
    best = min(d['cases'], key=lambda x:(x['q'],x['N']))
    rows.append(dict(Q=10,root_index=i,best_N=best['N'],best_q=best['q'],radius_exponent=str(Fraction(best['q'],2)),amplitude_exponent='5',s=d['s'],exact_prefix_comparisons=d['exact_prefix_comparisons'],cartesian_counts=d['counts'],polar_counts=p['counts'],independent_norm_comparisons=p['independent_norm_comparisons'],independent_tuning_comparisons=p['independent_tuning_comparisons'],scalar_identities=sum(x['exact_scalar_identities'] for x in r['cases']),cartesian_elapsed_s=d['actual_elapsed_s'],polar_elapsed_s=p['actual_elapsed_s'],scalar_elapsed_s=r['actual_elapsed_s'],cartesian=ref(cart),polar=ref(polar),scalar=ref(scalar),best_box=best['box']))
now = datetime.now(timezone.utc).isoformat(timespec='seconds')
totals = {k:sum(x[k] for x in rows) for k in ('exact_prefix_comparisons','independent_norm_comparisons','independent_tuning_comparisons','scalar_identities','cartesian_elapsed_s','polar_elapsed_s','scalar_elapsed_s')}
qs = ', '.join(str(x['best_q']) for x in rows)
ns = ', '.join(str(x['best_N']) for x in rows)
common = str(Fraction(max(x['best_q'] for x in rows),2))
proof = ROOT/'PROOF.md'
(ROOT/'sources'/f'PROOF_before_V{a.entry}.md').write_bytes(proof.read_bytes())
s = proof.read_text()
start = s.index('Status:')
end = s.index('\n',start)
s = s[:start]+f'Status: PROVED in V{a.entry} after all fourteen Cartesian prefixes, independent polar replays and exact rational box replays passed. The proof preceded computation.'+s[end:]
s += f'\n## Completed period-ten applications\n\nAdmitted {now}. For roots in increasing order, the best q values are {qs}, attained at the smallest retained prefix orders {ns}. The sufficient exteriors are R>2^(q/2)|epsilon|^5, with common exponent {common}. These are sufficient bounds, without an optimality claim.\n\n| Root | Response lower bound | Prefix N | q | Radius exponent |\n|---|---:|---:|---:|---:|\n'
for r in rows:
    s += f"| {r['root_index']} | {r['s']} | {r['best_N']} | {r['best_q']} | {r['radius_exponent']} |\n"
s += f"\nThe checks comprise {totals['exact_prefix_comparisons']} exact low-prefix comparisons, {totals['independent_norm_comparisons']} independently recomputed norm comparisons, {totals['independent_tuning_comparisons']} harmonic and response comparisons, and {totals['scalar_identities']} exact scalar identities across fifty-six boxes. Actual summed runtimes are {totals['cartesian_elapsed_s']:.6f} seconds for Cartesian prefixes, {totals['polar_elapsed_s']:.6f} seconds for polar replays and {totals['scalar_elapsed_s']:.6f} seconds for rational replays. These sums are job times, not campaign wall time.\n"
proof.write_text(s)
snapshot = ROOT/'sources'/f'PROOF_at_V{a.entry}.md'
snapshot.write_bytes(proof.read_bytes())
receipt = dict(checked_at_utc=now,verdict='PROVED',ledger=f'V{a.entry}',all_receipt_checks_pass=True,scope='Receipt integrity and counts after archived arithmetic replays, not a fresh arithmetic replay.',rows=rows,totals=totals,common_radius_exponent=common,amplitude_exponent='5',uniform_bounds=ref(bounds_admission),proof=ref(snapshot),independent_review=ref(review))
(ROOT/'verification/admission.json').write_text(json.dumps(receipt,indent=2)+'\n')
(ROOT/'sources/admit_period_ten_prefixes.py').write_bytes(Path(__file__).read_bytes())
result = f'The fourteen q values are {qs}, with prefixes {ns}. The sufficient radii are R>2^(q/2)|epsilon|^5, with common exponent {common}. Every check passes: {totals["exact_prefix_comparisons"]} exact low-prefix comparisons, {totals["independent_norm_comparisons"]} independent norm comparisons, {totals["independent_tuning_comparisons"]} harmonic and response comparisons, and {totals["scalar_identities"]} exact scalar identities.'
old += f'\n## V{a.entry} | {now} | Period-ten prefixes and sufficient radii\n\n**Claim.** The fourteen Q10 profiles satisfy the stated sufficient exterior bounds.\n\n**Method.** Use the admitted uniform response lower bounds of topic285, exact rational upper bounds, Cartesian 1536-bit prefixes to80, independent polar 2048-bit two-continuation replays, and exact reconstruction of four residue majorant boxes per root. Verify source hashes and the lead\'s independent proof review.\n\n**Result.** {result}\n\n**Verdict: CONFIRMED; the stated sufficient bounds are PROVED.** The profile count becomes87. No sharp boundary, pure common potential or whole-plane extension is asserted. Evidence: research/286_period_ten_prefixes/verification/admission.json.\n'
ledger.write_text(old)
generator = Path('code/build_current_radius_table.py')
g = generator.read_text()
marker = "add(Path('research/174_adaptive_majorant_boxes/verification/prefix_N90_sharp.json'),'two-mode',5,90)"
assert marker in g and 'research/286_period_ten_prefixes/verification' not in g
addition = f"""# Longer period-ten prefixes admitted in V{a.entry}.
folder=Path('research/286_period_ten_prefixes/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
for index in range(1,15):
    assert json.loads((folder/f'Q10_root{{index}}_review.json').read_text())['all_checks_pass']
    for p in folder.glob(f'Q10_root{{index}}_N*_box.json.gz'):add(p,'two-mode',index)
"""
generator.write_text(g.replace(marker,addition+marker))
notes = Path('NOTES_FOR_TEAM.md')
notes.write_text(f'## {now} VERIFIER -> LEAD: V{a.entry} admits Q10 sufficient radii\n\n{result}\n\nThese supply the first admitted Q10 prefix bounds; they raise the explicit-radius profile count from73 to87 with amplitude exponent5. Full proof and table: research/286_period_ten_prefixes/PROOF.md. The radius table generator now includes these admitted boxes.\n\n'+notes.read_text())
with Path('WORKLOG.md').open('a') as f:
    f.write(f'\n{now}: V{a.entry} admits all fourteen Q10 longer prefixes and fifty-six exact majorant boxes. q={qs}; common radius exponent {common}.\n')
with Path('VERIFY_SUMMARY.md').open('a') as f:
    f.write(f'\nV{a.entry} certifies the fourteen Q10 sufficient exponents using longer prefixes and the uniform response lower bounds of topic285. {result}\n')
with Path('research/INDEX.md').open('a') as f:
    f.write(f'\nUpdate {now}: topic286 is PROVED in V{a.entry}; all fourteen longer-prefix applications and their independent replays passed.\n')
print(json.dumps(dict(at=now,entry=a.entry,q=qs,N=ns,common=common,totals=totals)))
