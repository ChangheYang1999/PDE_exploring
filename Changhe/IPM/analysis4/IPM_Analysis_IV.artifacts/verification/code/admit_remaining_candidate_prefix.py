"""Check and record a completed prefix certificate for a Candidate-shaped root."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,json,re,sys
sys.set_int_max_str_digits(0)
ROOT=Path('research/181_remaining_candidate_prefixes')
def unpack(a):return F(a[0])*F(2)**int(a[1]),F(a[2])*F(2)**int(a[3])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=int,required=True);ap.add_argument('--entry',type=int,required=True);args=ap.parse_args();i,v=args.root,args.entry
    now=datetime.now(timezone.utc).isoformat(timespec='seconds');ledger=Path('VERIFY_REPORT.md');assert f'## V{v} |' not in ledger.read_text()
    folder=ROOT/'verification';p=folder/f'candidate{i}_checks.json';raw=p.read_bytes();d=json.loads(raw);assert d['all_checks_pass'] and d['N']==36 and d['bits']==2048 and d['B']==20
    response=json.loads(Path(f'research/163_other_candidate_shaped_roots/verification/root{i}_checks.json').read_text());assert response['all_index_lower_bound_proved'] and F(response['lower_bound'])==F(d['s'])
    for name,h in d['inputs'].items():assert sha256(Path(name).read_bytes()).hexdigest()==h
    counts=d['counts'];assert counts['poisson_coefficient_checks']==73165 and counts['ordered_products']==1818 and counts['provisional_continuations']==6 and counts['compatibility_projections']==4
    for row in d['norms']:
        m,r=unpack(row['norm_times_n']);assert m+r<=F(row['bound'])
    for row in d['harmonics']:
        m,r=unpack(row['H']);assert row['n']*(abs(m)+r)<=F(row['bound'])
        m,r=unpack(row['sigma']);assert abs(m)>r
    for row in d['obstructions']:
        m,r=unpack(row['exact_dyadic']);assert abs(m)<=r
    assert [x['N'] for x in d['boxes']]==[9,18,27,36];components=0;scalar=0
    for row in d['boxes']:
        boxdata=json.loads(Path(row['path']).read_text());assert boxdata['h']==2 and boxdata['Q']==9 and boxdata['B']==20 and F(boxdata['L'])==F(243,104) and F(boxdata['kappa'])==F(475,9)*F(row['N']+1,row['N'])
        assert F(boxdata['s'])==F(d['s']);scalar+=boxdata['scalar_coefficient_checks']
        for data in [boxdata,boxdata['adaptive']]:
            box=list(map(F,data['box']));image=list(map(F,data['image']));y=list(map(F,data['Y0']));assert len(box)==18
            assert all(0<=yy<=b and 0<=x<=b for yy,x,b in zip(y,image,box));components+=len(box)
        assert row['adaptive_q']==boxdata['adaptive']['q']
    assert scalar==216 and components==144
    best=min(x['adaptive_q'] for x in d['boxes']);first=min(x['N'] for x in d['boxes'] if x['adaptive_q']==best)
    a=F(json.loads(Path('research/156_candidate_shaped_compatibility/verification/polynomial.json').read_text())['original_amplitude']);assert a**225<2**949
    e=F(best,4)+F(949,100);E=-(-e.numerator//e.denominator);assert E==d['restored_radius_exponent']
    ordinary=[x['box_q'] for x in d['boxes']];adaptive=[x['adaptive_q'] for x in d['boxes']]
    result=f"At 2048 bits, the independent prefix through order 36 passes 73,165 Poisson coefficient checks, 1,818 ordered products, six provisional continuations and four compatibility projections. No midpoint reset is used. For N=9,18,27,36, ordinary box exponents are {ordinary}, and adaptive exponents are {adaptive}. All 216 scalar identities and 144 retained box components pass. The uniform response lower bound is {d['s']}. Thus R>2^({best}/4)|epsilon|^(9/4) suffices, with the best exponent first attained at N={first}. Restoring the exact Candidate amplitude gives R>2^{E}. Actual computation took {d['actual_elapsed_s']} seconds."
    review=dict(checked_at_utc=now,entry=v,all_checks_pass=True,retained_components_checked=components,box_count=4,best_q=best,restored_radius_exponent=E,source_check_sha256=sha256(raw).hexdigest());(folder/f'root{i}_review.json').write_text(json.dumps(review,indent=2)+'\n')
    with ledger.open('a') as f:f.write(f'\n## V{v} | {now} | Candidate-shaped root {i} prefix radius\n\nClaim: the certified prefix gives the stated sufficient exterior radius.\n\nMethod: independent directed-ball recurrence from the exact algebraic root, followed by exact rational norm, input-hash and supersolution inequalities under reviewed theorems 172 and 174.\n\nResult: {result}\n\nVerdict: CONFIRMED. The sufficient radius and convergence of all weighted derivatives and the common potential are PROVED. The radius is not asserted optimal. Evidence 181/root{i}.\n')
    admitted=sorted(int(x.stem.split('_')[0][4:]) for x in folder.glob('root*_review.json'));pending=sorted({5,6,7}-set(admitted))
    p=ROOT/'PROOF.md';t=p.read_text();t=re.sub(r'^Status:.*$','Status: PROVED for roots '+', '.join(map(str,admitted))+'. '+('Pending roots '+', '.join(map(str,pending))+'.' if pending else 'All requested branches completed.'),t,count=1,flags=re.M);t+=f'\n## Completed root {i} certificate\n\nAt {now}, V{v} confirms the following. {result}\n';p.write_text(t)
    p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} | V{v}: Candidate-shaped root {i} sharper prefix radius\n\n{result}\n\n'+p.read_text())
    with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V{v} confirms 181 root {i}, adaptive q={best}, restored exponent {E}.\n')
    p=Path('research/INDEX.md');t=p.read_text();t=re.sub(r'^181\..*$',f'181. [Remaining Candidate-shaped prefix radii](181_remaining_candidate_prefixes/PROOF.md): PROVED roots {", ".join(map(str,admitted))}; pending {", ".join(map(str,pending)) or "none"}.',t,flags=re.M);p.write_text(t)
    (ROOT/'sources'/'admit_remaining_candidate_prefix.py').write_bytes(Path(__file__).read_bytes());files={}
    for p in ROOT.rglob('*'):
        if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log':
            b=p.read_bytes();files[str(p.relative_to(ROOT))]=dict(bytes=len(b),sha256=sha256(b).hexdigest())
    (folder/'MANIFEST.json').write_text(json.dumps(dict(checked_at_utc=now,files=files),indent=2)+'\n');print(now,f'V{v}',f'root{i}','admitted')
if __name__=='__main__':main()
