"""Finite report successor acceptance from independently accepted own roots."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,re,time
B=Path(__file__).resolve().parents[1];tick=time.monotonic();checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert bool(v),k
 checks.append(k)
def near(v,d):
 parts=d.lower().split('e');mant=parts[0];exp=int(parts[1]) if len(parts)==2 else 0;digits=len(mant.split('.')[1]) if '.' in mant else 0;return 2*abs(Q(v)-Q(d))<=Q(10)**(exp-digits)
for z in read('data/manifest.json'):need('binding '+z['local'],sha(B/z['local'])==z['sha256'])
p=read('data/parameters.json');peer=read('source/N4_result.json');need('233 peer checks',peer['check_count']==len(peer['checks'])==233 and all(peer['checks'].values()));need('proof first',not read('data/PROOF_FIRST.json')['checker_exists']);ast.parse((B/'source/N4_check.py').read_text());doc=(B/'source/report.md').read_text();old=(B/'../numerical_literal_review_acceptance/source/report.md').read_text();own=read('../numerical_literal_review_acceptance/verification/result.json');need('1340 accepted',own['check_count']==1340);pat=r'\((\d+), (\d+)\) ([0-9.e+\-]+) -> ([0-9.e+\-]+) \(x([0-9.]+)\)';before=re.findall(pat,old);after=re.findall(pat,doc);need('200complete',len(before)==len(after)==200)
for i,(a,b) in enumerate(zip(before,after)):need('unchanged display '+str(i),a==b)
fr={int(k):Q(v) for k,v in own['first_mode_ratios_exact'].items()};phase={tuple(map(int,k.split(':'))):Q(v) for k,v in own['phase_final_over12_exact'].items()};need('first minima',min(fr,key=fr.get)==128 and near(fr[128],'26.8'));need('first maxima',max(fr,key=fr.get)==12 and near(fr[12],'9359'));need('phase minima',min(phase,key=phase.get)==(23,900) and near(min(phase.values()),'.58'));need('phase maxima',max(phase,key=phase.get)==(29,1200) and near(max(phase.values()),'10.26'))
raw=json.loads((B/'../numerical_literal_review_acceptance/source/023_weaktests3.json').read_text(),parse_float=Q);values={probe:Q(raw['probes'][f'{probe[0]}:{probe[1]}']['m_lower_bound']) for probe in phase};rank=sorted(values,key=values.get,reverse=True);need('largestfour',[list(x) for x in rank[:4]]==p['expected_largest'])
for a,b in zip(rank,rank[1:]):need('sorted '+str(a),values[a]>=values[b])
need('differentselected',set(map(tuple,p['selected']))!=set(rank[:4]));sv=[phase[tuple(x)] for x in p['selected']];need('selected exact',min(sv)==Q(p['selected_min']) and max(sv)==Q(p['selected_max']));need('selected nearest',near(min(sv),'.94') and near(max(sv),'1.01') and max(sv)<Q('1.04'));need('peer ranking',peer['phase023_sorted_probes']==[{'probe':list(x),'final_exact':str(values[x]),'final_over12_exact':str(phase[x])} for x in rank]);need('peer selected',peer['selected_four_ratio_range_exact']==[p['selected_min'],p['selected_max']])
notes=(B/'source/N1_NOTES.md').read_text();log=(B/'source/N1_WORKLOG.md').read_text();note=notes.split('## 2026-10-29T09:13Z:',1)[1].split('\n## ',1)[0];lr=next(s for s in log.splitlines() if s.startswith('- 2026-10-29T09:13Z'));need('09:13note current',p['current024'] in note and p['reconstructed024'] not in note);need('09:13log current',p['current024'][:12] in lr and p['reconstructed024'][:8] not in lr)
need('11:00old',p['reconstructed024'][:8] in notes.split('## 2026-10-29T11:00Z:',1)[1].split('\n## ',1)[0]);need('publisherlimits','my record, not a verifiable fact' in notes and 'no copy' in notes)
need('bad report attribution','sha256 in NOTES 09:13Z; the hash cited there, 58586004...' in doc);need('bad largestfour','the four largest values change by 0.94 to 1.04' in doc)
for phrase in ['factors 26.8 (k = 128) to 9359 (k = 12)','40 attempted GPU iterations','12-iteration stage had x44.4','final/12-iteration ratios 0.58 to 10.26 over the 25 probes','2.0899e-11 < [y^4] R_f(0, y) < 2.0900e-11','finite asymptotic far correction computed from the exact sector coefficients','with no certified tail remainder','No ordering of correction distances follows from E_2 or H','is CLAIMED (N4-413 and T4-484 accept only its conditional arithmetic)']:need('repair '+phrase,phrase in doc)
norms=read('../candidate016_complete_bounds_reciprocal/source/N4_complete_result.json')
for name,v,direction in [('H_lower_square_exact','.6167335007',-1),('H_upper_square_exact','.619652',1),('E2_lower_square_exact','628.580088526341',-1),('E2_upper_square_exact','629.296113',1)]:need('016display '+name,(Q(v)**2-Q(norms[name]))*direction>0)
need('Hgapdirection',Q(norms['H007_minus_H016_strict_lower_exact'])>Q('.017571422145091'));need('Egapdirection',Q(norms['E2016_minus_E2007_strict_lower_exact'])==Q('21.759869526341'));need('twoissues',len(peer['issues'])==2 and all(x['verdict']=='REFUTED' for x in peer['issues']))
for z in read('data/manifest.json'):need('unchanged '+z['local'],sha(B/z['local'])==z['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'target_sha256':sha(B/'source/report.md'),'display_count':600,'largest_four':[list(x) for x in rank[:4]],'selected_ratio_range_exact':[str(min(sv)),str(max(sv))],'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED N4-422 specified repairs and600unchanged displays. REFUTED two literal scope/provenance claims; chronology and017whole-fieldnorms OPEN. No PDE verdict change.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks;',out['elapsed_seconds'],'seconds')
