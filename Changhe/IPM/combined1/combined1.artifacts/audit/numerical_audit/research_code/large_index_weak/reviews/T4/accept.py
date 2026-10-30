from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,os,sys
from flint import arb,ctx,fmpq as Q
ROOT=Path(__file__).resolve().parents[4]
BASE=Path(__file__).resolve().parent
PEER=ROOT.parent/'c1-t4/research'
sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
ar=lambda q:arb(Q(q).numerator)/arb(Q(q).denominator)
def new(path,record):
    with path.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
def main():
    ctx.prec=2048;count=0
    def check(condition):
        nonlocal count
        assert condition,count
        count+=1
    pp=PEER/'large_index_weak_audit/verification/result.json'
    check(sha(pp)=='e23fa3d8cd4926bb9ef6f5cc3ca142211da8676a10071748ba2d3878dbe43984')
    shutil.copy2(pp,BASE/'T4_result.json');peer=json.loads((BASE/'T4_result.json').read_text())
    frozen={}
    reuse=[ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json',
        ROOT/'research/far_pairing_audit/reviews/T4/source/taylor_projection/source/canonical007.json',
        ROOT/'research/far_pairing_audit/reviews/T4/source/weak_probe_audit/code/reproduce.py',
        ROOT/'research/far_pairing_audit/reviews/T4/source/full_far_pairing/PROOF.md',
        ROOT/'research/far_pairing_audit/reviews/T4/source/full_far_pairing/code/check.py',
        ROOT/'research/far_pairing_audit/reviews/T4/T4_result.json',
        ROOT/'research/large_index_weak/verification/result.json',ROOT/'research/large_index_weak/verification/manifest.json',
        ROOT/'research/large_index_weak/PROOF.md',ROOT/'research/large_index_weak/code/check.py',
        ROOT/'research/large_index_weak/source/N1_weak_tests2.py',ROOT/'research/far_pairing_audit/source/N1_007_far_weak.json']
    reuse.extend(sorted((ROOT/'research/large_index_weak/verification').glob('K_*.json')))
    cache={sha(p):p for p in reuse if p.exists()}
    for text,digest in peer['inputs'].items():
        src=Path(text);check(src.is_file() and sha(src)==digest)
        rel=src.relative_to(PEER);dst=BASE/'source'/rel;dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.exists():
            if digest in cache:dst.symlink_to(os.path.relpath(cache[digest],dst.parent))
            else:shutil.copy2(src,dst)
        check(sha(dst)==digest);frozen[text]={'path':str(dst.relative_to(ROOT)),'sha256':digest}
    ours_path=ROOT/'research/large_index_weak/verification/result.json';ours=json.loads(ours_path.read_text())
    ownrows={}
    for row in ours['rows']:
        p=ROOT/row['path'];check(sha(p)==row['sha256']);v=json.loads(p.read_text());ownrows[v['K']]=v
    check(set(ownrows)=={r['K'] for r in peer['rows']}=={1024,100000,1000000,3000000,10000000,10000000000})
    far_path=ROOT/'research/far_pairing_audit/reviews/T4/T4_result.json';far=json.loads(far_path.read_text());farrows={r['K']:r for r in far['rows']}
    keys=['pairing','pairing_t_endpoint','pairing_by_parts','M2','M2_t_endpoint','C2','C2_t_endpoint','M','C','D','radius','A2','A','Benv2','Benv','Cenv2','Cenv']
    rows=[]
    for row in peer['rows']:
        K=row['K'];other=ownrows[K]
        for key in keys:check(arb(row[key]).overlaps(arb(other[key])))
        check(all(row['checks'].values()) and len(row['checks'])==19)
        for key in ['I_direct','I_parts']:check(arb(row['pairing']).overlaps(arb(farrows[K][key])))
        check(row['minimum_energy_accuracy_bits']>150)
        check(arb(row['M'])<arb(row['A'])+arb(row['Benv']))
        check(arb(row['C'])<arb(row['Cenv']))
        for key in ['M2','C2','A2','Benv2','Cenv2']:check(arb(row[key])>0)
        floor=Q(row['strict_lower_exact']);check(floor==Q(other['strict_lower_exact']))
        check(ar(floor)<arb(row['radius']) and ar(floor)<arb(other['radius']))
        g=row['gradient_certificate'];og=other['gradient_certificate']
        check(Q(g['H_exact'])==Q(other['H_upper_exact'])==Q(2,K*K))
        check(g['polynomial_exact']==og['derivative_polynomial_exact'])
        for x,y in zip(g['v_roots'],og['v_roots'],strict=True):check(arb(x).overlaps(arb(y)) and 0<arb(x) and arb(x)<1)
        for x,y in zip(g['amplitudes'],og['amplitude_caps'],strict=True):check(arb(x).overlaps(arb(y)) and arb(x)<ar(Q(g['H_exact'])))
        check(g['all_strict'] and row['strict_floor_verified'])
        for label,comp in row['N1_matching_envelope_comparisons'].items():
            oc=other['N1_matching_envelope_comparisons'][label]
            for key in ['estimate_over_full','absolute_relative_error']:check(arb(comp[key]).overlaps(arb(oc[key])))
            q=Q(*float(oc['FLOAT_estimate']).as_integer_ratio());check(q==Q(comp['estimate_exact_binary64']))
            ratio=ar(q)/arb(row[label]);check(ratio.overlaps(arb(comp['estimate_over_full'])))
            if label=='Cenv':check(comp['strictly_below_full'] and ratio<1)
        rows.append({'K':K,'all17_scalar_intervals_overlap':True,'strict_lower_exact':str(floor),'minimum_energy_accuracy_bits':row['minimum_energy_accuracy_bits']})
    out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED N4-216 via T4-282: six whole-plane weak records and matched envelopes; no uniform-K or existence conclusion',
        'checks_passed':count,'peer_result_sha256':sha(BASE/'T4_result.json'),'own_result_sha256':sha(ours_path),'peer_inputs_frozen':frozen,
        'review_sha256':sha(BASE/'REVIEW.md'),'acceptance_code_sha256':sha(Path(__file__)),'peer_elapsed_seconds':peer['elapsed_seconds'],'rows':rows}
    new(BASE/'ACCEPTANCE.json',out);print('ACCEPTED',count,out['utc'])
if __name__=='__main__':main()
