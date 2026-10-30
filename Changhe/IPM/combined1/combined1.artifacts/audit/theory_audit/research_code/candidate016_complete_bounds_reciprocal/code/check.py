"""Independent exact assembly equivalence. No producer program or integral runs."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib,json,re,sys,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0);checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
need('proof first',read('data/PROOF_FIRST.json')['checker_exists'] is False)
need('corrected proof precedes corrected checker',read('data/PROOF_REVISION.json')['proof_sha256']==sha(B/'PROOF.md'))
p=read('data/parameters.json');accepted={}
for topic,count in p['accepted_counts'].items():
 r=read('../'+topic+'/verification/result.json');need('accepted '+topic,r['check_count']==len(r['checks'])==count);accepted[topic]=r
own=accepted['candidate016_multimode_replay_audit'];prior=accepted['candidate016_prefix31_hardy_audit'];peer=read('source/N4_complete_result.json');tail=read('source/N4_prefix_v03.json');oldtail=read('../candidate016_prefix31_hardy_audit/source/N4_prefix_v02.json')
for name,r,count in [('N4-417',tail,2065),('N4-418',peer,4430)]:
 need(name+' finite checks',len(r['checks'])==r['check_count']==count and all(r['checks'].values()))
 need(name+' field identity',r['candidate']==p['candidate'] and r['raw_sha256']==p['raw_sha256'])
need('own field identity',own['candidate']==p['candidate'] and own['raw_sha256']==p['raw_sha256'])
need('sixteen selected modes',[r['n'] for r in own['rows']]==[r['n'] for r in peer['selected_modes']]==list(range(1,32,2)))
L=J=Q(0)
for a,b in zip(own['rows'],peer['selected_modes']):
 n=a['n'];lo=Q(a['selected_lower_floor']);j=Q(a['selected_cross_floor'])
 need(f'n{n} independently accepted floors',lo==Q(b['selected_lower'])>0 and j==Q(b['selected_improvement'])>0)
 L+=lo*lo;J+=j
need('lower square agreement',L==Q(own['H_lower_square_exact'])==Q(peer['H_lower_square_exact'])==Q(tail['H_lower_square_exact']))
need('cross sum agreement',J==Q(own['improvement_sum_strict_lower_exact'])==Q(peer['selected_improvement_sum_lower_exact'])==Q(tail['selected_improvement_sum_lower_exact']))
need('source complete coverage',tail['complete_field_mode_count']==160 and tail['complete_field_component_count']==1360 and tail['complete_uncomputed_tail_retained'] is True and peer['all160_source_modes_covered'] is True)
need('own complete coverage',prior['complete_mode_count']==160 and prior['complete_field_branch_count']==1360)
need('same field representation',tail['F_representation_sha256']==oldtail['F_representation_sha256']==prior['complete_field_hash'])
need('same prefix',[r['n'] for r in tail['modes']]==[r['n'] for r in oldtail['modes']]==list(range(1,32,2)) and tail['prefix']==31 and tail['smallest_omitted_mode']==33)
S=Q(tail['full_rF_square_upper_exact']);V=S/33**2
for a,b,c in zip(tail['modes'],oldtail['modes'],prior['modes']):
 n=a['n'];ql,qu=Q(a['q_lower_exact']),Q(a['q_upper_exact'])
 need(f'n{n} source integral unchanged',a['record']==b['record'] and a['sha256']==b['sha256'] and ql==Q(b['q_lower_exact']) and qu==Q(b['q_upper_exact']))
 need(f'n{n} independently resummed enclosure',ql<=Q(c['q_lower_exact'])<=Q(c['q_upper_exact'])<=qu and c['source_prefix_encloses_exact_replay'] is True)
 coefficient=Q(1,n*n)-Q(1,33*33);need(f'n{n} positive coefficient',coefficient>0)
 V+=coefficient*qu
need('same total upper',S==Q(oldtail['full_rF_square_upper_exact']))
need('producer M2 upper equality',V==Q(peer['complete_M2_upper_exact'])==Q(tail['M2_upper_exact'])==Q(tail['positive_coefficient_formula_upper_exact']))
V0=Q(own['M2_upper_exact']);delta=sum((Q(1,a['n']**2)-Q(1,1089))*(Q(a['q_upper_exact'])-Q(c['q_upper_exact'])) for a,c in zip(tail['modes'],prior['modes']))
need('independent M2 enclosure relation',V0==Q(prior['M2_upper_exact']) and 0<V-V0==delta<Q(1,10**500))
U=V-J;need('complete H interval equality',0<L<Q(own['H_upper_square_exact'])<U==Q(peer['H_upper_square_exact'])==Q(tail['improved_H_square_upper_exact']) and U-Q(own['H_upper_square_exact'])==delta)
comp=read('../candidate016_dual_replay_audit/source/components.json')['norms'];bounds={}
for side,target in [('lower',L),('upper',U)]:
 v={k:Q(comp[k]['accepted_'+side+'_exact']) for k in ['G0','G1','P2']}
 E=v['P2']**2+2**14*v['G1']**2+2**18*v['G0']**2+Q(20,21)*2**18*target
 key='E2_'+side+'_square_exact';tailkey=key if side=='lower' else 'conditional_E2_upper_square_exact'
 need(side+' producer full energy equality',E==Q(peer[key])==Q(tail[tailkey]));need(side+' independent energy relation',E-Q(own[key])==(Q(0) if side=='lower' else Q(20,21)*2**18*delta));bounds[side]=E
hl,hu,el,eu=[Q(peer[k]) for k in ['H_strict_lower_exact','H_strict_upper_exact','E2_strict_lower_exact','E2_strict_upper_exact']]
need('narrow H endpoints',0<hl*hl<L<U<hu*hu)
need('narrow E2 endpoints',0<el*el<bounds['lower']<bounds['upper']<eu*eu)
for key,tailkey in [('H_strict_lower_exact','H_strict_lower_exact'),('H_strict_upper_exact','conditional_improved_H_strict_upper_exact'),('E2_strict_lower_exact','E2_strict_lower_exact'),('E2_strict_upper_exact','conditional_E2_strict_upper_exact')]:need('N4 endpoint agreement '+key,Q(peer[key])==Q(tail[tailkey]))
base=read('../candidate016_dual_replay_audit/source/baseline007.json');m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',base['H_input_lower_ball']);need('exact007ball',m is not None and Q(m[2])>0)
h07=Q(m[1])-Q(m[2]);e07=Q(base['E_upper']['strict_upper_exact'])
need('same007norm',base['candidate']=='C1-N1-007-d2w-j7-e2bal' and e07==Q(p['007_E2_upper'])==Q(own['007_E2_upper_exact']) and h07>Q(own['007_H_lower_exact']))
hgap=h07-hu;egap=el-e07
need('new E2 gap exact',egap==Q(p['E2_gap_lower'])==Q(peer['E2016_minus_E2007_strict_lower_exact'])>Q(own['strict_E2_gap_lower']))
need('new H gap exact',hgap==Q(peer['H007_minus_H016_strict_lower_exact'])>Q(p['H_gap_lower'])>0)
need('both analytic reviews explicit',peer['general_and_tail_reviews_completed'] is True and peer['peer_code_executed'] is False and peer['new_source_integrals'] is False)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'manifest_sha256':sha(B/'data/manifest.json'),'candidate':p['candidate'],'raw_sha256':p['raw_sha256'],'selected_mode_count':16,'complete_field_mode_count':160,'omitted_modes_retained':144,'producer_M2_minus_independent_M2_exact':str(delta),'H_lower_square_exact':str(L),'H_upper_square_exact':str(U),'E2_lower_square_exact':str(bounds['lower']),'E2_upper_square_exact':str(bounds['upper']),'H_strict_lower_exact':str(hl),'H_strict_upper_exact':str(hu),'E2_strict_lower_exact':str(el),'E2_strict_upper_exact':str(eu),'strict_H_gap_lower':str(hgap),'strict_E2_gap_lower':str(egap),'foreign_code_executed':False,'new_candidate_integrals':False,'verdict':'CONFIRMED reciprocal agreement with N4-417/418; all complete-field upper premises are discharged by T4-477/480/481/486. Candidate017 receives no acceptance.'}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(r['utc'],len(checks),'checks',r['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
