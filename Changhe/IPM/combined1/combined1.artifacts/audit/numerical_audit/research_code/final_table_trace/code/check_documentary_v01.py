"""Audit frozen table references and two exact documentary defects."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/final_table_trace'
def sha(p):return sha256(p.read_bytes()).hexdigest()
def ball(s):
    match=re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]',s)
    assert match,s
    m,e=map(Q,match.groups());assert e>=0
    return m-e,m+e

def rows(text,columns,anchor=None):
    result={};active=anchor is None
    for lineno,line in enumerate(text.splitlines(),1):
        if anchor and anchor in line:active=True;continue
        if not active:continue
        if anchor and result and not line.startswith('|'):break
        cells=[c.strip() for c in re.split(r'(?<!\\)\|',line)[1:-1]]
        if len(cells)!=columns or not re.fullmatch(r'\d+(?:-\d+)?',cells[0]):continue
        numbers=list(map(int,cells[0].split('-')))
        for number in range(numbers[0],numbers[-1]+1):
            assert number not in result
            result[number]={'line':lineno,'cells':cells,'text':line,'combined_row':cells[0]}
    return result

def lab(text):
    labels=['RULED OUT','OPEN','PROVED','CONDITIONAL','FLOAT','REFUTED','CONFIRMED','AUDITED','CLAIMED']
    found=sorted((text.upper().find(x),x) for x in labels if x in text.upper())
    return found[0][1] if found else None

def main():
    start=time.monotonic();inputs={}
    def bind(path,expected=None):
        p=R/path if isinstance(path,str) else path
        assert p.resolve().is_relative_to(R)
        h=sha(p)
        if expected is not None:assert h==expected,(str(p),h,expected)
        inputs[str(p.relative_to(R))]=h
        return p
    manifest=json.loads(bind(B/'source/MANIFEST_v01.json').read_text())
    for p,entry in manifest['files'].items():bind(p,entry['sha256'])
    bind(B/'PROOF.md');bind(Path(__file__).resolve());bind(B/'verification/PROOF_FIRST_v01.json')
    report=(B/'source/FINAL_REPORT_v01.md').read_text();matrix=(B/'source/closure_matrix_v01.md').read_text()
    ledger=(B/'source/N4_VERIFY_REPORT_v01.md').read_text();summary=(B/'source/N4_AUDIT_SUMMARY_v01.md').read_text()
    RR=rows(report,8,'| # | framework | candidate |');MM=rows(matrix,11)
    assert RR and set(RR)==set(range(1,max(RR)+1))
    blocks=re.split(r'(?m)(?=^## )',ledger);cites={}
    for block in blocks:
        header=block.splitlines()[0] if block.splitlines() else ''
        ids=re.findall(r'N4-(\d{3})',header)
        if 'V001' in header:ids.append('001')
        if 'V002' in header:ids.append('002')
        for id in ids:cites.setdefault(int(id),[]).append(block)
    trace=[];issues=[]
    for number,row in RR.items():
        peer=MM.get(number);assert peer is not None,number
        own_ids=sorted({int(x) for x in re.findall(r'N4-(\d{3})',row['text']+' '+peer['text'])})
        found={f'N4-{i:03d}':[b.splitlines()[0] for b in cites.get(i,[])] for i in own_ids}
        missing=[k for k,v in found.items() if not v]
        candidate=lambda x:re.findall(r'C1-N1-\d{3}|C1-BASE-S131|C1-A2-(?:d2|Mpen2|b6)',x)
        tr={'row':number,'report':row,'matrix':peer,'status_agrees':lab(row['cells'][-1])==lab(peer['cells'][-1]),'candidate_ids_agree':candidate(row['cells'][2])==candidate(peer['cells'][2]),'N4_ledger_headers':found,'missing_citations':missing,'scope':'Documentary linkage only. Each mathematical and numerical subclaim needs the stated accepted proof and result.'}
        if missing or not tr['status_agrees'] or not tr['candidate_ids_agree']:issues.append(number)
        trace.append(tr)
    old=json.loads(bind('research/numerics_v11_audit/verification/result.json','e14b7398eeed5f8498ebde12371cb98ff9ef47c20d6a757fc39afa6d7359c4a0').read_text())
    accepted=json.loads(bind('research/candidate016_weak_peer/verification/result.json','a9a568fd52a50a5a385f9ea698d06255f091e8e3873d9764b03134808a615941').read_text())
    row=next(x for x in accepted['rows'] if x['n']==19 and x['K']==1800)
    l=Q(row['strict_floor']);lo,hi=ball(row['radius_recomputed']);printed=Q('0.0014704');safe=Q('0.0014703')
    own014=json.loads(bind('research/successor_factored_weak/reviews/T4_014/ACCEPTANCE.json','a0577a9d7cf2d08326d32878c126dccf721c233454d0ade060a00d265e6c013e').read_text())
    block224='\n'.join(cites[224]);ownproof=bind('research/successor_factored_weak/PROOF.md')
    blanket='These probes are from the registered family and outside the documented\nanalytic objective span.'
    correction=('The deterministic weak bounds do not require objective separation. '
                'Candidate014\'s displayed (21,522) probe was included in its objective; '
                'the public25-probe extension for later successors has its own registration '
                'and objective-span checks. The exact scope of each earlier or design probe '
                'is given in its accepted proof.')
    checks={
        'report_all105_rows_present':set(RR)==set(range(1,106)),
        'matrix_has_all_report_rows':set(RR)<=set(MM),
        'all_explicit_N4_citations_present_in_frozen_ledger':all(not x['missing_citations'] for x in trace),
        'all_status_labels_agree':all(x['status_agrees'] for x in trace),
        'all_literal_candidate_ids_agree':all(x['candidate_ids_agree'] for x in trace),
        'row80_prints_upward_floor':'> 0.0014704' in RR[80]['text'],
        'printed_floor_above_cited_root_upper':printed>hi,
        'safe_floor_below_accepted_floor_below_root':safe<=l<lo,
        'existing328_independently_recorded_same_issue':old['checks']['016_printed_floor_is_above_certified_root'],
        'own_summary_blanket_scope_present':summary.count(blanket)==1,
        'own014_included_probe_explicitly_accepted':'belongs to014\'s objective' in block224 and 'CONFIRMED N4-214' in own014['verdict'],
        'own_summary_also_acknowledges014_exception':'included in014\'s objective' in summary,
    }
    # A missing citation or documentary mismatch is a finding, not a reason
    # to discard the complete row trace. The two defect checks must pass.
    for k in ['row80_prints_upward_floor','printed_floor_above_cited_root_upper','safe_floor_below_accepted_floor_below_root','existing328_independently_recorded_same_issue','own_summary_blanket_scope_present','own014_included_probe_explicitly_accepted','own_summary_also_acknowledges014_exception']:assert checks[k],k
    for rel,h in list(inputs.items()):assert sha(R/rel)==h
    result={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'checks':checks,'documentary_trace_count':len(trace),'documentary_mismatch_rows':issues,'trace':trace,'findings':[{'claim':'row80 >0.0014704 is certified by N4-246/253','verdict':'REFUTED as support from the cited certificate; actual distance upper bound OPEN','printed':str(printed),'accepted_floor':str(l),'root_interval':[str(lo),str(hi)],'safe_short_floor':str(safe),'row_status_changes':False},{'claim':'all displayed own distance probes are outside the recorded analytic objective','verdict':'REFUTED by candidate014 objective inclusion; deterministic distance certificate remains CONFIRMED','source_literal':blanket,'proposed_own_replacement':correction,'independent_acceptance':'N4-224'}],'mathematical_scope':'No fresh full-plane integration, complete numerical audit of all105 rows, existence proof, dyadic inference from L2, or candidate ranking. This is exact source-to-ledger linkage and the two stated source defects.','elapsed_seconds':time.monotonic()-start}
    out=B/'verification/documentary_v01.json'
    with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'utc':result['utc'],'trace_count':len(trace),'checks':checks,'mismatch_rows':issues,'result_sha256':sha(out),'elapsed_seconds':result['elapsed_seconds']},indent=2))
if __name__=='__main__':main()
