"""Exact serialized-decimal audit only; no spatial or PDE certification."""
from pathlib import Path
from decimal import Decimal
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json, re, time
R = Path(__file__).resolve().parents[3]
B = R / 'research/numerics_final_literal_audit'
def sha(p): return sha256(p.read_bytes()).hexdigest()
def main():
    start = time.monotonic()
    mf = json.loads((B/'source/MANIFEST.json').read_text())
    bindings = {str((B/'source'/n).relative_to(R)): e['sha256'] for n,e in mf['files'].items()}
    for name, digest in bindings.items(): assert sha(R/name) == digest, name
    assert sha(B/'PROOF.md') == mf['proof_sha256']
    extra=json.loads((B/'source/PROOF_FIRST_v02.json').read_text())
    assert not extra['checker_v02_exists'] and sha(B/'ERRATA_v02.md')==extra['supplement_sha256']
    assert sha(B/'source/023_s12_exact.json')==extra['raw12_sha256']
    for p in [B/'PROOF.md', B/'source/MANIFEST.json', B/'ERRATA_v02.md', B/'source/PROOF_FIRST_v02.json', B/'source/023_s12_exact.json', Path(__file__)]: bindings[str(p.relative_to(R))] = sha(p)
    def load(n): return json.loads((B/'source'/n).read_text(), parse_float=Decimal)
    checks = {}; rows = []; failures = []; issues = []
    text = (B/'source/report.md').read_text(); lines = text.splitlines()
    reg = [(n,k) for n in [19,23,25,29,31] for k in [600,900,1200,1800,2400]]
    data = {n:load(n+'_weaktests3.json') for n in ['016','022','023','024','025','026','027','028','023_s12']}
    def val(c,p): return Q(data[c]['probes'][f'{p[0]}:{p[1]}']['m_lower_bound'])
    def exact_nearest(q, literal):
        d=Decimal(literal); unit=Q(Decimal(1).scaleb(d.as_tuple().exponent))
        return abs(q-Q(d)) <= unit/2
    pat = r'\((\d+), (\d+)\) ([0-9.e+\-]+) -> ([0-9.e+\-]+) \(x([0-9.]+)\)'
    blocks=[]
    for ln, new, old in [(205,'023','016'),(207,'024','016'),(208,'025','016'),(209,'026','022')]:
        blocks.append((ln,new,old,re.findall(pat,lines[ln-1])))
    for ln, new, old1, old2 in [(210,'027','022','026'),(212,'028','022','027')]:
        gs=re.findall(pat,lines[ln-1]); assert len(gs)==50
        blocks.extend([(ln,new,old1,gs[:25]),(ln,new,old2,gs[25:])])
    comparisons={}
    for ln, new, old, groups in blocks:
        name=new+'/'+old
        checks['register_'+name] = [(int(x[0]),int(x[1])) for x in groups] == reg
        vals=[]
        for ns,ks,od,nd,fac in groups:
            p=(int(ns),int(ks)); a,b=val(old,p),val(new,p); assert a>0 and b>0
            ratio=b/a; passes={k:exact_nearest(v,t) for k,v,t in [('old',a,od),('new',b,nd),('factor',ratio,fac)]}
            row={'comparison':name,'line':ln,'probe':list(p),'old_exact':str(a),'new_exact':str(b),'ratio_exact':str(ratio),'ratio_FLOAT':float(ratio),'display':{'old':od,'new':nd,'factor':fac},'nearest_display_checks':passes}
            rows.append(row);vals.append(row)
            for k,ok in passes.items():
                checks[f'display_{name}_{ns}_{ks}_{k}']=ok
                if not ok:failures.append({'comparison':name,'probe':list(p),'field':k,'literal':row['display'][k],'exact':str({'old':a,'new':b,'factor':ratio}[k])})
        ratios=[Q(v['ratio_exact']) for v in vals]
        comparisons[name]={'count':len(vals),'decreased':sum(q<1 for q in ratios),'equal':sum(q==1 for q in ratios),'increased':sum(q>1 for q in ratios),'min_ratio_exact':str(min(ratios)),'max_ratio_exact':str(max(ratios))}
    checks['all200probes']=len(rows)==200
    first={c:load(c+'_weaktests2.json') for c in ['007','013']}
    checks['same_first_mode_rule']=first['007']['rule']==first['013']['rule']
    checks['same_first_mode_register']=list(first['007']['NORM-T-WEAK-v1_a0'])==list(first['013']['NORM-T-WEAK-v1_a0'])
    firstrows=[]
    for k,e in first['007']['NORM-T-WEAK-v1_a0'].items():
        if int(k)>128:continue
        a,b=abs(Q(e['I_k'])),abs(Q(first['013']['NORM-T-WEAK-v1_a0'][k]['I_k']))
        assert b>0
        firstrows.append({'k':int(k),'I007_exact':str(a),'I013_exact':str(b),'improvement_exact':str(a/b),'improvement_FLOAT':float(a/b)})
    witness=next(r for r in firstrows if r['k']==128)
    checks['k128_strictly_between26and28']=26<Q(witness['improvement_exact'])<28
    checks['report_has_thousandfold_headline']='are three orders of magnitude below' in lines[15]
    checks['report_detailed_line_has27']='factors 27 (k = 128)' in lines[179]
    issues.append({'id':'headline_first_mode','verdict':'REFUTED','line':16,'scope':'Literal comparison of the saved FLOAT pairings, not a certified PDE pairing comparison.','claim':'The sampled k<=128 first-mode pairings of013 are three orders of magnitude below007.','witness':witness,'repair':'State the full saved-register range, or name the three selected probes k64,96,128 explicitly.'})
    firstlo=min(firstrows,key=lambda r:Q(r['improvement_exact'])); firsthi=max(firstrows,key=lambda r:Q(r['improvement_exact']))
    checks['firstmode_min_is128']=firstlo['k']==128
    checks['firstmode_max_is12']=firsthi['k']==12 and 9358<Q(firsthi['improvement_exact'])<9360
    checks['source12_raw_identity']=data['023_s12']['sha256']==extra['raw12_sha256']
    issues.append({'id':'detailed_first_mode_range','verdict':'REFUTED','line':180,'scope':'Full saved k<=128 register; the displayed27 to314 range describes only the listed high-k subregister k64,96,128.','minimum':firstlo,'maximum':firsthi,'repair':'For the full register use approximate factors27 to9359, or restrict the assertion to k64,96,128.'})
    phase={}
    for new in ['023_s12','023']:
        qs=[val(new,p)/val('016',p) for p in reg]
        phase[new]={'source_candidate_sha256':data[new]['sha256'],'increased':sum(q>1 for q in qs),'decreased':sum(q<1 for q in qs),'min_ratio_exact':str(min(qs)),'max_ratio_exact':str(max(qs)),'probe_19_600':{'m_exact':str(val(new,(19,600))),'ratio_exact':str(val(new,(19,600))/val('016',(19,600))),'ratio_FLOAT':float(val(new,(19,600))/val('016',(19,600)))}}
    checks['twelve_step_label_literal']='023 (016 + scale 100, 12 steps)' in lines[205]
    checks['26point2_is_final40step_nearest']=exact_nearest(Q(phase['023']['probe_19_600']['ratio_exact']),'26.2')
    checks['26point2_is_not12step_nearest']=not exact_nearest(Q(phase['023_s12']['probe_19_600']['ratio_exact']),'26.2')
    issues.append({'id':'phase_label_023','verdict':'REFUTED','line':206,'scope':'The displayed witness is the final40-step FLOAT record, not the saved12-step record.','claim':'The paragraph attributes (19,600)x26.2 to023 after12steps.','witness':{n:phase[n]['probe_19_600'] for n in phase},'repair':'Attribute these probe factors to the final40-step state; retain the distinct12-step objective/norm diagnostics where intended.'})
    phaserows=[{'probe':list(p),'ratio_exact':str(val('023',p)/val('023_s12',p)),'ratio_FLOAT':float(val('023',p)/val('023_s12',p))} for p in reg]
    phaselo=min(phaserows,key=lambda r:Q(r['ratio_exact'])); phasehi=max(phaserows,key=lambda r:Q(r['ratio_exact']))
    checks['phase_min_witness']=phaselo['probe']==[23,900] and Q(phaselo['ratio_exact'])<Q('.582')
    checks['phase_max_witness']=phasehi['probe']==[29,1200] and Q(phasehi['ratio_exact'])>Q('10.262')
    checks['phase_range_literal']='registered probes at phase-2/phase-1 ratios 0.94 to 1.04' in lines[205]
    issues.append({'id':'phase_ratio_range_023','verdict':'REFUTED','line':206,'scope':'Finite ratios of saved final40-step to12-step weak-test records, all25 registered probes.','claim':'All registered phase2/phase1 ratios are between0.94 and1.04.','minimum':phaselo,'maximum':phasehi,'repair':'Use the approximate range0.5816 to10.2623 for the complete register, or name a properly checked smaller subset.'})
    checks['source_explicit_finite_asymptotic']=all('finite asymptotic far correction' in d['label'] for d in first.values())
    checks['report_exact_far_part_literal']='add an exact far part from the surviving sectors' in lines[243]
    issues.append({'id':'finite_tail_qualification','verdict':'OPEN','line':244,'scope':'Documentary qualification, no new quadrature computation.','claim':'The report calls the added first-mode correction an exact far part.','evidence':first['013']['label'],'repair':'Say a finite asymptotic far correction from exact sector coefficients; no tail remainder is enclosed.'})
    checks['hash_provenance_literal_mismatch']='current file\'s hash is e171c051..., recorded in my 09:13Z WORKLOG' in lines[206] and 'hash cited there is the pre-typo-fix text' in lines[213]
    issues.append({'id':'heldout024_provenance','verdict':'REFUTED','lines':[207,214],'scope':'Internal attribution conflict in the frozen report only; no new claim about unwitnessed save times.','repair':'Make line214 agree with line207: the09:13ZWORKLOG records the current e171c051 hash, not the reconstructed58586004 pre-edit hash.'})
    for name, digest in bindings.items(): assert sha(R/name)==digest, name
    assert all(checks.values()), {k:v for k,v in checks.items() if not v}
    out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED finite arithmetic; literal issues individually classified','scope':'Exact checks of serialized FLOAT decimals and frozen text only. No PDE bound or quadrature certificate.','bindings':bindings,'checks':checks,'check_count':len(checks),'probe_rows':rows,'comparison_counts':comparisons,'first_mode_rows_k_le128':firstrows,'phase023':phase,'phase_final_over12_rows':phaserows,'first_mode_extrema':{'minimum':firstlo,'maximum':firsthi},'display_failures':failures,'issues':issues}
    dest=B/'verification/result_v02.json'
    with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'utc':out['utc'],'elapsed_seconds':out['elapsed_seconds'],'check_count':len(checks),'result_sha256':sha(dest),'issues':issues,'comparison_counts':comparisons},indent=2))
if __name__=='__main__':main()
