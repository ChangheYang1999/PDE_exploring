"""Admit checked finite single-sine coefficients and continuum residuals."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,sys
from fractions import Fraction
sys.dont_write_bytecode=True
from flint import arb,ctx
ctx.prec=512

def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def reference(p):
    r=p.read_bytes();return dict(path=str(p),sha256=sha256(r).hexdigest(),bytes=len(r))
def verify(r):
    assert sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256'],r['path']
def admit(M,entry):
    ledger=Path('VERIFY_REPORT.md');old=ledger.read_text();assert f'## V{entry} |' not in old and f'## V{entry+1} |' not in old
    a=Path('research/271_single_harmonic_finite_audit');b=Path('research/272_single_harmonic_residuals')
    cp=a/'verification'/f'sin{M}/checks.json.gz';rp=b/'verification'/f'sin{M}/checks.json.gz'
    c=json.loads(gzip.decompress(cp.read_bytes()));r=json.loads(gzip.decompress(rp.read_bytes()))
    assert c['all_checks_pass'] and r['complete'] and r['all_reported_within_one_percent'] and c['M']==r['M']==M
    for v in [c['source'],c['harmonics'],c['log'],c['selected_source'],r['peer_evaluation'],r['prior_audit']]:verify(v)
    assert sha256(gzip.decompress(Path(c['selected_source']['path']).read_bytes())).hexdigest()==c['selected_raw_sha256']
    assert c['source']==r['source'] and c['bits']==2048 and r['bits']==1024 and r['grid_steps']==2048
    comparisons=[v for row in r['rows'] for group in row['comparison'].values() for v in group.values()]
    orders=sorted({v['N'] for v in r['rows']});radii=sorted({v['R'] for v in r['rows']},key=Fraction)
    assert orders==[10,20,40,80]
    assert {(v['N'],v['R']) for v in r['rows']}=={(n,R) for n in orders for R in radii}
    assert len(r['rows'])==len(orders)*len(radii) and len(comparisons)==6*len(r['rows']) and all(v['within_one_percent'] for v in comparisons)
    for row in r['rows']:
        for group in ['residual_bounds','next_term_bounds']:
            for v in row[group].values():assert arb(v['lower'])>0 and arb(v['upper'])>arb(v['lower']) and arb(v['interpolation_error'])>0
    t=now();refs=[]
    for base,i in [(a,entry),(b,entry+1)]:
        p=base/'sources'/f'PROOF_at_V{i}.md';p.write_bytes((base/'PROOF.md').read_bytes());refs.append(reference(p))
    cc=c['counts'];N=c['maximum_order'];final=next(row for row in c['norms'] if row['n']==N)
    result=(f"At unit amplitude, sin({M} theta), delta={2*c['h']}/{c['Q']}, the independent prefix through{c['independent_prefix_order']} agrees on{cc['prefix_f']} density and{cc['prefix_g']} stream coefficients and{cc['prefix_tuning']} tuned harmonics. All{cc['poisson']} signed-Laurent Poisson coefficient identities, {cc['denominators']} nonresonant-divisor tests and{cc['statistics']} printed log norms through{N} pass. Complete nonlinear sums at{[x['n'] for x in c['nonlinear']]} check{cc['nonlinear_pairs']} ordered pairs and{cc['nonlinear_coefficients']} residual coefficients. The density root at{N} is {final['f_root']}. The actual maximum norm-relative radius is {c['maximum_norm_relative_radius']}. Final stream orders{c['untuned_final_stream_orders']} have an unset free harmonic and are excluded from full stream norms. Runtime{c['actual_elapsed_s']} seconds.")
    verdict='CONFIRMED for the finite checks under the stated outward-interval execution hypotheses. Exact compatibility is supplied by the separately proved profile theorem, not by a zero-containing interval. No sharp radius or limiting growth constant is inferred.'
    residual=(f"All{len(r["rows"])} combinations of N=10,20,40,80 and R={",".join(radii)} have continuum residual and first-omitted-term enclosures through two angular derivatives. All{len(comparisons)} reported sampled values meet the one-percent comparison tolerance. Three partial-sum angles are enclosed in each case. Runtime{r['actual_elapsed_s']} seconds.")
    extra=''
    if M==7:
        group={row['N']:row for row in r['rows'] if row['R']=='1/2'}
        for x,y in [(20,40),(40,80)]:assert arb(group[y]['residual_bounds']['0']['lower'])>arb(group[x]['residual_bounds']['0']['upper'])
        v=group[80]['residual_bounds']['0'];extra=f" At R=1/2, the weighted residual increases strictly from N20 to40 and40 to80; its N80 supremum is between0.2858469906 and0.2864138296. This finite increase does not decide eventual convergence."
        assert arb(v['lower'])>arb('0.2858469906') and arb(v['upper'])<arb('0.2864138296')
    if M==9:
        group={row['N']:row for row in r['rows'] if row['R']=='2'}
        assert arb(group[40]['residual_bounds']['0']['upper'])<arb(group[20]['residual_bounds']['0']['lower'])
        assert arb(group[80]['residual_bounds']['0']['lower'])>arb(group[40]['residual_bounds']['0']['upper'])
        v=group[80]['residual_bounds']['0'];extra=f" At R=2, the weighted residual decreases from N20 to40 and then increases strictly from40 to80; its N80 supremum lies between {v['lower']} and {v['upper']}. This finite reversal does not decide eventual convergence."
        group={row['N']:row for row in r['rows'] if row['R']=='4'}
        for x,y in [(10,20),(20,40),(40,80)]:assert arb(group[y]['residual_bounds']['0']['upper'])<arb(group[x]['residual_bounds']['0']['lower'])
        extra+=' At R=4, each of the three successive finite residual decreases is strict.'
    if M==11:
        for radius,increases in [('4',True),('8',False)]:
            group={row['N']:row for row in r['rows'] if row['R']==radius}
            for x,y in [(10,20),(20,40),(40,80)]:
                earlier=group[x]['residual_bounds']['0'];later=group[y]['residual_bounds']['0']
                assert arb(later['lower'])>arb(earlier['upper']) if increases else arb(later['upper'])<arb(earlier['lower'])
        extra=' At R=4 the weighted residual strictly increases at each of the three successive truncations. At R=8 it strictly decreases at each step. These finite comparisons do not bracket the infinite convergence threshold.'
    entries=[(entry,'Finite single-harmonic coefficient audit, sin'+str(M),'The new tuned single-harmonic checkpoint agrees with independent Cartesian arithmetic.', 'Decode and hash the exact dyadic inputs, inspect the producer enclosure induction, recompute complete tuning blocks at2048 bits, and evaluate every stored differential Poisson identity and selected complete nonlinear sums.',result,verdict,cp,refs[0]),(entry+1,'Single-harmonic continuum residual audit, sin'+str(M),'The reported finite residuals and first omitted terms agree with independent continuum enclosures.','Form the full finite Cartesian residual without dropping low-order terms; evaluate at2049 angular points at1024 bits and bound interpolation error by the second derivative.',residual+extra,'CONFIRMED as finite continuum interval bounds under topic271 coefficient-enclosure hypotheses. Sampled maxima are not identified with continuum suprema. No infinite-series conclusion follows from the finite sequence.',rp,refs[1])]
    for i,title,claim,method,res,v,p,proof in entries:
        record=dict(checked_at_utc=t,entry=i,all_checks_pass=True,evidence=reference(p),proof=proof,source=c['source'],scope=v)
        (p.parent/'admission.json').write_text(json.dumps(record,indent=2)+'\n')
        old+=f'\n## V{i} | {t} | {title}\n\n**Claim.** {claim}\n\n**Method.** {method}\n\n**Result.** {res}\n\n**Verdict: {v}** Evidence: {p.parent}/admission.json.\n'
    ledger.write_text(old)
    note=Path('NOTES_FOR_TEAM.md');note.write_text(f'## {t} | V{entry}/V{entry+1}: sin{M} finite and continuum checks admitted\n\n{result}\n\n{residual}{extra}\n\n{verdict} Producer-source and proof snapshots are retained in271/272. The lead independently reviewed the protocol at20:04:50Z; arithmetic admission is restricted to the written execution hypotheses.\n\n'+note.read_text())
    with Path('WORKLOG.md').open('a') as f:f.write(f'\n{t}: admitted V{entry}/V{entry+1}, sin{M} finite coefficient and continuum checks.\n')
    print(json.dumps(dict(at=t,entries=[entry,entry+1],M=M,source=c['source'],root=final['f_root'])))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--M',type=int,required=True);ap.add_argument('--entry',type=int,required=True);v=ap.parse_args();admit(v.M,v.entry)
