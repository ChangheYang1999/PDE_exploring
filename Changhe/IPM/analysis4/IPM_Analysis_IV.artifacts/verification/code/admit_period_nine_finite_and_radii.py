"""Freeze the Q9 finite audit, precision correction, and necessary radii."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
ctx.prec=1024

def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):
    r=p.read_bytes();return dict(path=str(p),sha256=sha256(r).hexdigest(),bytes=len(r))
def verify(r):assert sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256'],r['path']
def snapshot(base,i):
    p=base/'sources'/f'PROOF_at_V{i}.md';p.write_bytes((base/'PROOF.md').read_bytes());return ref(p)
def main():
    ledger=Path('VERIFY_REPORT.md');old=ledger.read_text();assert '## V554 |' in old
    for i in range(555,559):assert f'## V{i} |' not in old
    base=Path('research/273_period_nine_finite_audit');p=base/'verification/checks.json.gz';d=json.loads(gzip.decompress(p.read_bytes()));assert d['all_checks_pass']
    for v in [d['source'],d['polynomial'],d['harmonics'],d['log']]:verify(v)
    n99=d['norms'][-1];endpoint=(arb(n99['f_log'])-arb(d['norms'][44]['f_log']))/54
    assert abs(endpoint-arb('1.0033658597292008'))<arb('5e-16')
    root=arb(n99['f_root']);assert abs(root-arb('9.237573288144763'))<arb('5e-16')
    actual=arb(n99['f_norm_relative_radius']);actual_log=actual.log()/arb(10).log();monitor=arb(d['division_monitor_log10']);assert abs(monitor-arb('-133.9232112'))<arb('5e-8');assert abs(actual_log-monitor)>arb('0.3')
    peer=Path('../a4-num/notes/q9_r10_check_p512.txt');(base/'sources/peer_note.txt').write_bytes(peer.read_bytes())
    sup=dict(checked_at_utc=now(),all_checks_pass=True,source_audit=ref(p),peer_note=ref(peer),endpoint_orders=[45,99],endpoint_slope=endpoint.str(50,radius=True),least_squares_slope=d['fit_slope'],actual_norm_relative_radius=n99['f_norm_relative_radius'],actual_norm_relative_radius_log10=actual_log.str(50,radius=True),division_monitor_log10=d['division_monitor_log10'],diagnosis='The printed slope is the endpoint slope. The printed precision is the normalized-division monitor, not the actual norm-relative radius.')
    sp=base/'verification/statistics_distinctions.json';sp.write_text(json.dumps(sup,indent=2)+'\n')
    result555=f"For the largest root b=0.421494658565943218..., the 512-bit source contains the exact algebraic input. Independent1024-bit Cartesian arithmetic agrees on all2700 prefix coefficients through36 and three tuned harmonics. All nine responses through90,40095 Poisson coefficient identities,9900 nonresonant divisors,99 printed log norms and the complete nonlinear sums at50 and99 pass. The latter check147 ordered pairs and1198 residual coefficients. The density root at99 is9.2375732881447629132. The endpoint log-norm slope on45..99 is{endpoint.str(20,radius=True)}, while the least-squares slope is0.99765674493717292368. The final99 stream harmonic is unset and its full norm is excluded. Runtime15.6962670288 seconds."
    result556=f"The source note calls log10=-133.9232112 a norm-relative radius. It equals the division-based monitor at512 bits. The actual sum-of-radii over sum-of-absolute-midpoints is{n99['f_norm_relative_radius']}, with log10={actual_log.str(25,radius=True)}. The monitor remains a valid diagnostic under its own definition; the nomenclature must be corrected."
    rb=Path('research/274_period_nine_necessary_radii');rp=rb/'verification/checks.json';r=json.loads(rp.read_text());assert r['all_checks_pass'] and len(r['rows'])==10 and len(r['exact_top_checks'])==18;verify(r['source'])
    radii=', '.join(row['quoted_lower'] for row in r['rows'])
    result557=f"All18 exact highest-sector coefficients match the independent Cartesian polynomial prefix. Independent512-bit and1024-bit evaluations agree. R_H={r['R_H']}. The ten rounded-down necessary constants are{radii}, each multiplied by|epsilon|^(9/2). All four finite scalar diagnostics at100,400,800,1500 round as reported. Runtime{r['actual_elapsed_s']} seconds."
    sb=Path('research/269_summary_radius_audit');ss=sb/'verification/20261031T200029Z/checks.json';s=json.loads(ss.read_text());assert s['all_checks_pass'] and s['profile_count']==73
    verify(s['source_summary']);verify(s['source_aggregate'])
    result558='The frozen20:00:29Z summary has15 groups and73 profiles. All73 certificate hashes,73 exact radius exponents,73 amplitude exponents,15 rational c/delta pairs and the Candidate-shaped amplitude restoration entries agree with the admitted aggregate. No certificate or parameter discrepancy was found.'
    entries=[
      (555,base,'Largest period-nine root, finite checkpoint audit','The independent512-bit period-nine run agrees with the exact branch and the reported finite statistics.','Refine the exact root, recompute full Cartesian tuning blocks, directly evaluate all responses, differential identities and selected complete ordered convolutions.',result555,'CONFIRMED for the finite checks under the stated producer execution hypotheses. Infinite convergence is separately PROVED in267; these finite growth statistics do not establish an asymptotic constant.',[p,sp]),
      (556,base,'Period-nine precision monitor is mislabeled','The reported -133.9232112 is the logarithm of the actual norm-relative radius.','Independently compute both the sum-of-radii norm ratio and the512-bit normalized-division monitor from the exact stored balls.',result556,'REFUTED as a norm-relative-radius label; CONFIRMED as the normalized-division monitor. The source coefficient enclosures are unaffected.',[p,sp]),
      (557,rb,'Necessary exterior radii at period nine','The ten period-nine branches obey the strict second-angular-derivative necessary bounds in Corollary T_9(d).','Specialize the proved positive highest-sector recurrence and asymptotic; compare exact top coefficients and evaluate all constants twice in directed arithmetic.',result557,'CONFIRMED and PROVED under the precise uniform termwise second-angular-derivative hypothesis. These are necessary bounds only; they do not identify the true convergence threshold.',[rp]),
      (558,sb,'All73 published sufficient radius entries match','The updated summary faithfully reports every admitted sufficient radius and amplitude power.','Freeze the lead summary and aggregate, verify source certificate hashes, and compare every rational parameter and exponent exactly.',result558,'CONFIRMED for the frozen summary. Later edits require a fresh comparison.',[ss])]
    t=now();notes=[]
    for i,b,title,claim,method,result,verdict,evidence in entries:
        proof=snapshot(b,i);record=dict(checked_at_utc=t,entry=i,all_checks_pass=True,verdict=verdict,proof=proof,evidence=[ref(x) for x in evidence])
        name='admission.json' if i in [555,557] else f'admission_V{i}.json';(b/'verification'/name).write_text(json.dumps(record,indent=2)+'\n')
        old+=f'\n## V{i} | {t} | {title}\n\n**Claim.** {claim}\n\n**Method.** {method}\n\n**Result.** {result}\n\n**Verdict: {verdict}** Evidence: {b}/verification/{name}.\n'
        notes.append(f'V{i}: {result}\n\n{verdict}')
    ledger.write_text(old)
    note=Path('NOTES_FOR_TEAM.md');note.write_text(f'## {t} | V555-V558: period-nine finite audit, precision correction, T_9(d) accepted,73-profile table checked\n\n'+'\n\n'.join(notes)+'\n\nThe T_9(d) label may now be PROVED with its precise hypothesis. The lead scalar script has a stale opening docstring mentioning delta2/7 and1/4; its actual loop correctly uses Q9.\n\n'+note.read_text())
    with Path('WORKLOG.md').open('a') as f:f.write(f'\n{t}: V555-V558 admitted; Q9 finite checks, precision-label correction, all ten necessary radii and73 sufficient-table entries.\n')
    for b in [base,rb]:(b/'sources/admit_period_nine_finite_and_radii.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(dict(at=t,entries=list(range(555,559)),statistics=sup)))
if __name__=='__main__':main()
