"""Finite source-bound repair audit. No publisher code or numerical field replay."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as Q
from decimal import Decimal
import json, re, os, time
R=Path(__file__).resolve().parents[3]
B=R/'research/numerics_final_repairs'
def sha(p): return sha256(p.read_bytes()).hexdigest()
def main():
    start=time.monotonic()
    assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
    prep=json.loads((B/'source/PREPARE.json').read_text())
    roots=json.loads((B/'source/OWN_ROOTS.json').read_text())
    assert not prep['checker_exists'] and not roots['checker_exists']
    assert sha(B/'PROOF.md')==prep['proof_sha256']
    inputs={p:e['sha256'] for p,e in prep['files'].items()}
    inputs.update(roots['inputs'])
    records={}
    for p,h in roots['inputs'].items():
        assert sha(R/p)==h
        j=json.loads((R/p).read_text());records[p]=j
        for kind in ['inputs','bindings']:
            for k,v in j.get(kind,{}).items():
                if k in inputs:assert inputs[k]==v
                inputs[k]=v
    fix=json.loads((B/'verification/PROOF_FIRST_v02.json').read_text())
    assert not fix['checker_v02_exists']
    assert sha(B/'SELECTED_SUBSET_PROOF_v02.md')==fix['supplement_sha256']
    assert sha(B/'verification/FAILED_v01.json')==fix['failure_sha256']
    for p in [B/'PROOF.md',B/'source/PREPARE.json',B/'source/OWN_ROOTS.json',B/'SELECTED_SUBSET_PROOF_v02.md',B/'verification/PROOF_FIRST_v02.json',B/'verification/FAILED_v01.json',B/'code/check.py',Path(__file__)]:
        inputs[str(p.relative_to(R))]=sha(p)
    for p,h in inputs.items():
        assert (R/p).resolve().is_relative_to(R) and sha(R/p)==h,p
    old=records['research/numerics_final_literal_audit/verification/result_v02.json']
    origin=records['research/candidate007_origin_tolerance/verification/result.json']
    norms=records['research/candidate016_multimode_complete_bounds/verification/result_v01.json']
    recon=records['research/candidate024_hash_reconstruction/verification/result.json']
    report=(B/'source/report.md').read_text()
    notes=(B/'source/N1_NOTES.md').read_text()
    log=(B/'source/N1_WORKLOG.md').read_text()
    checks={}; issues=[]; excerpts={}
    def nearest(q,s):
        d=Decimal(s);u=Q(Decimal(1).scaleb(d.as_tuple().exponent))
        return abs(Q(q)-Q(d))<=u/2
    pat=r'\((\d+), (\d+)\) ([0-9.e+\-]+) -> ([0-9.e+\-]+) \(x([0-9.]+)\)'
    groups=re.findall(pat,report)
    assert len(groups)==len(old['probe_rows'])==200
    for i,(g,row) in enumerate(zip(groups,old['probe_rows'])):
        expected=(str(row['probe'][0]),str(row['probe'][1]),row['display']['old'],row['display']['new'],row['display']['factor'])
        checks[f'unchanged_probe_display_{i}']=tuple(g)==expected and all(row['nearest_display_checks'].values())
    extrema=old['first_mode_extrema']
    checks['first_mode_min26point8']=nearest(extrema['minimum']['improvement_exact'],'26.8') and extrema['minimum']['k']==128
    checks['first_mode_max9359']=nearest(extrema['maximum']['improvement_exact'],'9359') and extrema['maximum']['k']==12
    checks['first_mode_corrected_two_occurrences']=report.count('factors 26.8 (k = 128) to 9359 (k = 12)')==2
    phase=old['phase_final_over12_rows']
    qs={tuple(row['probe']):Q(row['ratio_exact']) for row in phase}
    checks['phase_min_nearest058']=nearest(min(qs.values()),'.58')
    checks['phase_max_nearest1026']=nearest(max(qs.values()),'10.26')
    checks['phase12_vs016_nearest444']=nearest(old['phase023']['023_s12']['probe_19_600']['ratio_exact'],'44.4')
    checks['phase40_vs016_nearest262']=nearest(old['phase023']['023']['probe_19_600']['ratio_exact'],'26.2')
    lines=report.splitlines()
    reading=next(s for s in lines if '023 at its final endpoint' in s)
    excerpts['phase023']=reading
    checks['phase_endpoint_corrected']='40 attempted GPU iterations' in reading and '12-iteration stage had x44.4' in reading
    checks['phase_complete_range_corrected']='final/12-iteration ratios 0.58 to 10.26 over the 25 probes' in reading
    values={tuple(row['probe']):Q(row['new_exact']) for row in old['probe_rows'] if row['comparison']=='023/016'}
    selected=[(19,1800),(23,2400),(25,2400),(31,2400)]
    ranked=sorted(values,key=values.get,reverse=True)
    checks['four_largest_literal']='the four largest values change by 0.94 to 1.04' in reading
    checks['listed_four_not_global_largest']=set(selected)!=set(ranked[:4])
    selected_ratios=[qs[p] for p in selected]
    checks['selected_four_nearest_min094']=nearest(min(selected_ratios),'.94')
    checks['selected_four_max_below104']=max(selected_ratios)<Q('1.04')
    checks['selected_four_nearest_max101']=nearest(max(selected_ratios),'1.01')
    issues.append({'id':'four_largest_scope','verdict':'REFUTED','scope':'Literal largest-four claim on the full25-probe register, not a PDE statement.','listed_probes':[list(p) for p in selected],'actual_largest_four':[list(p) for p in ranked[:4]],'repair':'Say the four listed selected probes, with rounded ratios about0.94 to1.04; do not call them the largest four registered values.'})
    checks['origin_counterexample_preserved']='2.0899e-11 < [y^4] R_f(0, y) < 2.0900e-11' in report
    checks['origin_linear_nonlinear_distinction']='2.3e-13 (linear rows)' in report and 'five quadratic Taylor equations hold only to about 1.6e-11' in report
    checks['origin_bounds_match']=Q(origin['Rf_y4_lower_exact'])==Q('2.0899e-11') and Q(origin['Rf_y4_upper_exact'])==Q('2.0900e-11')
    normline=next(s for s in lines if s.startswith('Assembled FLOAT E_2 proxy'))
    excerpts['norms']=normline
    for label,q,square,lower in [
        ('new_Hlower','.6167335007','H_lower_square_exact',True),
        ('new_E2lower','628.580088526341','E2_lower_square_exact',True),
        ('old_Hlower','.529469576110','H_lower_square_exact',True),
        ('old_Hupper','.619652','H_upper_square_exact',False),
        ('old_E2lower','608.392385921614','E2_lower_square_exact',True),
        ('old_E2upper','629.296113','E2_upper_square_exact',False),
    ]:
        checks[label]=Q(q)**2 < Q(norms[square]) if lower else Q(q)**2>Q(norms[square])
    checks['new_Hgap_direction']=Q('.017571422145091')<=Q(norms['H007_minus_H016_strict_lower_exact'])
    checks['Hgap_in_report']='H(007) - H(016) > 0.017571422145091' in normline
    checks['full017_stays_claimed']='is CLAIMED (N4-413 and T4-484 accept only its conditional arithmetic)' in normline
    checks['no_distance_ordering']='No ordering of correction distances follows from E_2 or H' in normline
    checks['finite_far_qualification']='finite asymptotic far correction computed from the exact sector coefficients' in report and 'with no certified tail remainder' in report
    oldhash=recon['reconstructed_sha256'];current=recon['current_sha256']
    note0913=notes.split('## 2026-10-29T09:13Z:',1)[1].split('\n## ',1)[0]
    log0913=next(s for s in log.splitlines() if s.startswith('- 2026-10-29T09:13Z'))
    attribution=next(s for s in lines if s.startswith('- Held-out registration:'))
    excerpts.update(note0913=note0913,log0913=log0913,current_report_attribution=attribution)
    checks['note0913_current_hash']=current in note0913 and oldhash not in note0913
    checks['log0913_current_hash']=current[:12] in log0913 and oldhash[:8] not in log0913
    checks['reconstruction_identity']=recon['hash_matches_claim'] and recon['one_replacement_only'] and recon['all_other_bytes_equal'] and recon['all60_pairs_preserved']
    checks['remaining_bad_attribution']='sha256 in NOTES 09:13Z; the hash cited there, 58586004...' in attribution
    checks['publisher_prior_limit']='my record, not a verifiable fact' in notes and 'no copy' in notes
    issues.append({'id':'heldout024_attribution_persists','verdict':'REFUTED','scope':'Current literal hash attribution to the09:13 note. Historical saves remain independently OPEN.','current_hash':current,'reconstructed_hash':oldhash,'repair':'The09:13 note and WORKLOG print e171c051. The snapshot INDEX and11:00 note print58586004. Reversing the unique wording edit reproduces58586004 and preserves every probe; the alleged save times are publisher testimony.'})
    for p,h in inputs.items(): assert sha(R/p)==h,p
    assert all(checks.values()),{k:v for k,v in checks.items() if not v}
    out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'checks':checks,'check_count':len(checks),'transferred_display_count':600,'new_report_sha256':prep['files']['research/numerics_final_repairs/source/report.md']['sha256'],'phase023_sorted_probes':[{'probe':list(p),'final_exact':str(values[p]),'final_over12_exact':str(qs[p])} for p in ranked],'selected_four_ratio_range_exact':[str(min(selected_ratios)),str(max(selected_ratios))],'excerpts':excerpts,'issues':issues,'verdict':'CONFIRMED specified repairs and unchanged finite displays; two remaining literal scope defects REFUTED','scope':'Finite serialized data and frozen text only, no new PDE norm or chronology certificate.'}
    target=B/'verification/result_v02.json'
    with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(out['utc'],out['verdict'],'checks',len(checks),'inputs',len(inputs),'seconds',out['elapsed_seconds'],'sha256',sha(target),flush=True)
    for issue in issues:print(json.dumps(issue),flush=True)
if __name__=='__main__':main()
