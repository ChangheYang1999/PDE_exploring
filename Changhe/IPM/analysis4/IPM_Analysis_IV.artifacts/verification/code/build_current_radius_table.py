"""Summarize already admitted prefix radius certificates for the report owner."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,re,sys
sys.set_int_max_str_digits(0)
rows={}
def add(path,family,index,N=None):
    d=json.loads(gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_bytes());a=d.get('adaptive',d);q=a.get('q',a.get('w_dyadic_exponent'));h,Q=d['h'],d['Q'];assert q is not None
    box=list(map(F,a['box']));image=list(map(F,a['image']));assert len(box)==len(image) and all(0<=x<=b for x,b in zip(image,box))
    key=(family,h,Q,index);row=dict(family=family,root_index=index,delta=str(F(2*h,Q)),Q=Q,h=h,N=N or d.get('N'),q=q,radius_exponent=str(F(q,2*h)),amplitude_exponent=str(F(Q,2*h)),response_lower_bound=d['s'],path=str(path),sha256=sha256(path.read_bytes()).hexdigest())
    if family=='Candidate-shaped':
        e=F(q,4)+F(949,100);row['restored_original_amplitude_exponent']=-(-e.numerator//e.denominator)
    if key not in rows or (q,row['N'])<(rows[key]['q'],rows[key]['N']):rows[key]=row
for p in Path('research/175_integer_period_prefix/verification').glob('Q*_root*.json'):
    m=re.fullmatch(r'Q([3456])_root([1-6])',p.stem)
    if m:add(p,'two-mode',int(m[2]))
for number in [176,178,179,181,182,186,205]:
    folder=next(Path('research').glob(str(number)+'_*'))/'verification'
    for p in folder.glob('*_N*.json'):
        if number in [176,179]:
            m=re.match(r'(candidate|two_mode)(\d+)_N',p.stem)
            if not m:continue
            family='Candidate-shaped' if m[1]=='candidate' else 'two-mode';i=int(m[2])
        elif number==181:
            m=re.match(r'candidate(\d+)_N',p.stem)
            if not m:continue
            family='Candidate-shaped';i=int(m[1])
            if not (folder/f'root{i}_review.json').exists():continue
        else:
            m=re.match(r'root(\d+)_N',p.stem)
            if not m:continue
            family='two-mode';i=int(m[1])
            if number in [182,186,205] and not (folder/f'root{i}_review.json').exists() and not (number==182 and i==6):continue
        add(p,family,i)
# Topic220 admitted inV462, all four separate exact replays required.
folder=Path('research/220_high_prefix_three_fifths_radii/verification')
for index in range(1,5):
    review=json.loads((folder/f'root{index}_review.json').read_text());assert review['all_checks_pass']
    for p in folder.glob(f'root{index}_N*.json.gz'):add(p,'two-mode',index)
# Tail-only improvements explicitly admitted in V469, V470, V483 and V486.
for index in [1,2,3,4]:
    folder=Path('research/223_tail_response_radii/verification')
    review=json.loads((folder/f'root{index}_K30_review.json').read_text());assert review['all_checks_pass']
    add(folder/f'root{index}_K30_box.json.gz','two-mode',index)
folder=Path('research/226_integer_period_tail_radii/verification')
for Q,index in [(4,2),(5,6)]:
    review=json.loads((folder/f'Q{Q}_root{index}_review.json').read_text());assert review['all_checks_pass']
    add(folder/f'Q{Q}_root{index}_box.json.gz','two-mode',index)
# The single-harmonic branch is admitted in V484.
review=json.loads(Path('research/227_single_eleven_convergence/verification/review.json').read_text());assert review['all_checks_pass']
add(Path('research/227_single_eleven_convergence/verification/box.json.gz'),'single sin11',1)
# Delta4/7 certificates admitted in V497-V498.
review=json.loads(Path('research/233_single_nine_four_sevenths/verification/review.json').read_text());assert review['all_checks_pass']
add(Path('research/233_single_nine_four_sevenths/verification/box.json.gz'),'single sin9',1)
for index in range(1,4):
    folder=Path('research/239_four_sevenths_two_mode/verification')
    review=json.loads((folder/f'root{index}_review.json').read_text());assert review['all_checks_pass']
    add(folder/f'root{index}_box.json.gz','two-mode',index)
# Sharper delta4/7 bounds admitted in V514 after exact-minimum checks.
for index in range(1,4):
    folder=Path('research/247_four_sevenths_exact_minima/verification')
    review=json.loads((folder/f'root{index}_radius_replay.json').read_text());assert review['all_checks_pass']
    add(folder/f'root{index}_radius.json.gz','two-mode',index)
# Single sin7 specialization admitted in V504.
review=json.loads(Path('research/241_single_seven_four_fifths/verification/review.json').read_text());assert review['all_checks_pass']
add(Path('research/241_single_seven_four_fifths/verification/box.json.gz'),'single sin7',1)
# Ten period-seven roots admitted in V527.
folder=Path('research/253_period_seven_tuning/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
for index in range(1,11):
    review=json.loads((folder/f'root{index}_review.json').read_text());assert review['all_checks_pass']
    add(folder/f'root{index}_box.json.gz','two-mode',index)
# Sin17 at delta6/13 admitted in V528.
folder=Path('research/242_single_seventeen_six_thirteenths/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
assert json.loads((folder/'review.json').read_text())['all_checks_pass']
add(folder/'box.json.gz','single sin17',1)
# Ten period-eight roots admitted in V531.
folder=Path('research/256_period_eight_tuning/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
for index in range(1,11):
    review=json.loads((folder/f'root{index}_review.json').read_text());assert review['all_checks_pass']
    add(folder/f'root{index}_box.json.gz','two-mode',index)
# Sharper sin17 minimum and box admitted in V537.
folder=Path('research/255_seventeen_exact_minimum/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
assert json.loads((folder/'review.json').read_text())['all_checks_pass']
add(folder/'box.json.gz','single sin17',1)
# Twenty longer Q7/Q8 prefixes admitted in V539.
folder=Path('research/261_period_seven_eight_prefixes/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
for Q in [7,8]:
    for index in range(1,11):
        assert json.loads((folder/f'Q{Q}_root{index}_review.json').read_text())['all_checks_pass']
        for p in folder.glob(f'Q{Q}_root{index}_N*_box.json.gz'):
            add(p,'two-mode',index)
# New Q7/Q8 tail-only applications are included only after separate admission.
folder=Path('research/262_tail_response_prefix/verification')
for Q in [7,8]:
    if (folder/f'Q{Q}_admission.json').exists():
        assert json.loads((folder/f'Q{Q}_admission.json').read_text())['verdict']=='PROVED'
        assert json.loads((folder/f'Q{Q}_tail_review.json').read_text())['all_checks_pass']
        add(folder/f'Q{Q}_tail_box.json.gz','two-mode',3)
# Ten period-nine roots admitted in V551.
folder=Path('research/267_period_nine_tuning/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
for index in range(1,11):
    review=json.loads((folder/f'root{index}_review.json').read_text());assert review['all_checks_pass']
    add(folder/f'root{index}_box.json.gz','two-mode',index)
# Longer period-nine prefixes admitted in V574.
folder=Path('research/280_period_nine_prefixes/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
for index in range(1,11):
    assert json.loads((folder/f'Q9_root{index}_review.json').read_text())['all_checks_pass']
    for p in folder.glob(f'Q9_root{index}_N*_box.json.gz'):add(p,'two-mode',index)
# Longer period-ten prefixes admitted in V596.
folder=Path('research/286_period_ten_prefixes/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
for index in range(1,15):
    assert json.loads((folder/f'Q10_root{index}_review.json').read_text())['all_checks_pass']
    for p in folder.glob(f'Q10_root{index}_N*_box.json.gz'):add(p,'two-mode',index)
# Period-ten root-five tail-only boxes admitted in V597.
folder=Path('research/294_q10_tail_prefix/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
assert json.loads((folder/'tail_replay.json').read_text())['all_checks_pass']
for p in folder.glob('Q10_root5_N*_tail_box.json.gz'):add(p,'two-mode',5)
add(Path('research/174_adaptive_majorant_boxes/verification/prefix_N90_sharp.json'),'two-mode',5,90)
now=datetime.now(timezone.utc).isoformat(timespec='seconds');data=sorted(rows.values(),key=lambda r:(r['family'],F(r['delta']),r['root_index']))
Path('artifacts/current_certified_radii.json').write_text(json.dumps(dict(checked_at_utc=now,scope='Summary of already admitted prefix certificates; no new theorem or optimality claim.',rows=data),indent=2)+'\n')
lines=['# Current certified prefix radii','',f'Updated {now}. This table summarizes admitted results in the verification ledger. It is not a claim of optimal radii.','', 'For a two-mode row, the leading profile is epsilon times (sin(theta)+b_i sin(3 theta)); roots are numbered increasingly within the stated exact compatibility polynomial. Candidate-shaped rows use the normalized exact profile of topic 156 with only its third-harmonic coefficient replaced by the indexed root. They are compatible modifications at delta=4/9. The single sinM rows have leading profile epsilon sin(M theta).','', 'Every listed bound is R>2^e |epsilon|^a. On each such closed exterior, the tuned density, stream and common potential series converge with all appropriately weighted derivatives, under the exact hypotheses in the linked proof. The reported N is the smallest retained prefix attaining this table exponent.','', '| Family | delta | Root | Prefix N | e | a | Restored Candidate exponent | Certificate |','|---|---|---:|---:|---:|---:|---:|---|']
for r in data:
    proof=Path(r['path']).parents[1]/'PROOF.md';lines.append(f"| {r['family']} | {r['delta']} | {r['root_index']} | {r['N']} | {r['radius_exponent']} | {r['amplitude_exponent']} | {r.get('restored_original_amplitude_exponent','')} | [{proof.parent.name}]({proof}) |")
lines+=['','The restored Candidate column uses the exact amplitude inequality a1^225<2^949. The stored Candidate007 exponent and unmodified profile are outside this modification theorem. Roots still awaiting their individual prefix admission are omitted. Exact certificate paths and hashes are retained in artifacts/current_certified_radii.json.','', 'Finite fitted growth constants are intentionally absent: they do not establish an infinite convergence boundary.']
Path('CERTIFIED_RADII.md').write_text('\n'.join(lines)+'\n');print(now,'summarized',len(data),'admitted branches')
