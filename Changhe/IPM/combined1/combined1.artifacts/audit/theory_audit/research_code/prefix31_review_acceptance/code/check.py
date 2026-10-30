"""Exact prefix31 review recomposition and directed display audit."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,re,sys,time
from flint import arb,fmpq,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');ctx.prec=p['precision_bits'];A=lambda q:arb(fmpq(str(q)))
need('proof first',read('data/PROOF_FIRST.json')['checker_exists'] is False)
review=(B/'source/T1_review.md').read_text();tree=ast.parse((B/'source/T1_check.py').read_text());hashmaps=[ast.literal_eval(x.value) for x in ast.walk(tree) if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HASH' for t in x.targets)];need('one source map',len(hashmaps)==1)
for f,h in hashmaps[0].items():need('T1 source '+f,sha(B/read('data/peer_data_mapping.json')[f])==h)
need('finished T1log','checks passed 54 ; elapsed 0.0 s\nRESULT PASS\n' in (B/'source/T1_log.txt').read_text())
need('repaired prefix log','checks passed 4783 ; elapsed 7.0 s\nRESULT PASS\n' in (B/'source/T1_repaired_prefix_log.txt').read_text())
oldtree=ast.parse((B/'../partial_hardy_review_acceptance/source/T1_check.py').read_text());newtree=ast.parse((B/'source/T1_repaired_prefix_check.py').read_text())
assertions=lambda t:[ast.dump(n,include_attributes=False) for n in ast.walk(t) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='ok']
need('revised program same assertions',assertions(oldtree)==assertions(newtree))
for topic,count in p['accepted_counts'].items():
 d=read('../'+topic+'/verification/result.json');need('accepted '+topic,d['check_count']==len(d['checks'])==count)
r9=read('../candidate016_prefix31_hardy_audit/source/N4_prefix_v02.json');r3=read('../candidate016_prefix_hardy_audit/source/N4_prefix_v01.json');r10=read('source/N4_upper_result.json');r12=read('source/N4_opposite_result.json');params=read('source/N4_upper_parameters.json');own=read('../candidate016_prefix31_hardy_audit/verification/result.json');cross=read('../candidate016_cross_archive_audit/verification/result.json');base007=read('../candidate016_dual_replay_audit/source/baseline007.json')
for k,v in p['upper_dependencies'].items():need('upper dependency '+k,params['dependencies'][k]==sha(B/v))
need('one raw candidate',r9['raw_sha256']==r10['raw_sha256']==params['raw_sha256']==r3['raw_sha256']==p['raw_sha256'])
need('complete field160',r9['complete_field_mode_count']==160 and r9['complete_uncomputed_tail_retained'] and not r9['all160_individual_mode_integrals_replayed'])
need('prefix all16',[v['n'] for v in r9['modes']]==list(range(1,32,2)) and r9['smallest_omitted_mode']==33)
q={v['n']:(Q(v['q_lower_exact']),Q(v['q_upper_exact'])) for v in r9['modes']}
for n,(l,u) in q.items():need('strict mode interval '+str(n),0<l<u and u-l<Q('1e-510'))
for v in r3['modes']:need('unchanged prefix '+str(v['n']),q[v['n']]==(Q(v['q_lower_exact']),Q(v['q_upper_exact'])))
for v in own['modes']:need('own resummed interval '+str(v['n']),q[v['n']][0]<=Q(v['q_lower_exact'])<=Q(v['q_upper_exact'])<=q[v['n']][1])
comp=read('../candidate016_dual_replay_audit/source/components.json')['norms'];L={k:Q(v['accepted_lower_exact']) for k,v in comp.items()};U={k:Q(v['accepted_upper_exact']) for k,v in comp.items()};RL=L['rF']**2;RU=U['rF']**2
QL=sum((l for l,u in q.values()),Q(0));QU=sum((u for l,u in q.values()),Q(0));P=RU/1089+sum(((Q(1,n*n)-Q(1,1089))*u for n,(l,u) in q.items()),Q(0));Mlo=sum((l/n**2 for n,(l,u) in q.items()),Q(0));Mprefhi=sum((u/n**2 for n,(l,u) in q.items()),Q(0));split=Mprefhi+(RU-QL)/1089
need('R2 squares',RL==Q(r9['full_rF_square_lower_exact']) and RU==Q(r9['full_rF_square_upper_exact']))
need('complete positive tail',RL-QU==Q(r9['tail_rF_square_lower_exact'])>0 and RU-QL==Q(r9['tail_rF_square_upper_exact']))
need('positive formula selected',P==Q(r9['M2_upper_exact'])==Q(r9['positive_coefficient_formula_upper_exact'])==Q(r10['complete_M2_upper_exact']))
need('split upper excess',split==Q(r9['split_formula_upper_exact']) and split-P==(QU-QL)/1089 and 0<split-P<Q('1e-512'))
need('prefix lower',Mlo==Q(r9['M2_lower_exact']))
for name,l,u in [('Q_prefix_ball',QL,QU),('S_prefix_ball',Mlo,Mprefhi)]:
 z=arb(r9[name]);need(name+' encloses endpoints',z.contains(A(l)) and z.contains(A(u)));need(name+' narrow radius',z.rad()<arb('1e-510'))
J=Q(cross['improvement_sum_strict_lower_exact']);Hlo2=Q(cross['H_lower_square_exact']);Hhi2=P-J;energy=lambda C,h:C['P2']**2+2**14*C['G1']**2+2**18*C['G0']**2+Q(20,21)*2**18*h
need('two distinct corrections',r9['selected_improvement_modes']==[1,3] and J==Q(r9['selected_improvement_sum_lower_exact']))
need('corrected H upper',Hhi2==Q(r9['improved_H_square_upper_exact'])==Q(r10['H_upper_square_exact'])>Hlo2==Q(r10['H_lower_square_exact']))
Ehi2=energy(U,Hhi2);Elo2=energy(L,Hlo2)
need('both E2 squares',Ehi2==Q(r9['conditional_E2_upper_square_exact'])==Q(r10['E2_upper_square_exact']) and Elo2==Q(r10['E2_lower_square_exact']))
values={'M2':P,'plain_H':P,'H2':Hhi2,'H':Hhi2,'E2':Ehi2,'plain_E2':energy(U,P),'H2lo':Hlo2}
for row in p['displays']:
 shown=Q(row['value']);val=shown**2 if row['square'] else shown;true=values[row['key']]
 need('directed display '+row['key']+' '+row['value'],val>true if row['direction']=='upper' else val<true)
Hs=Q(r10['H_strict_upper_exact']);Hl=Q(r10['H_strict_lower_exact']);Es=Q(r10['E2_strict_upper_exact']);El=Q(r10['E2_strict_lower_exact'])
need('strict H display squares',Hl**2<Hlo2<Hhi2<Hs**2 and Hl>Q('.529469576110') and Hs==Q(p['H_strict_upper']))
need('strict E2 display squares',El**2<Elo2<Ehi2<Es**2 and El==Q('608.392385921614') and Es==Q('629.296112162914'))
need('prefix31 improvement over7',P<Q(r3['M2_upper_exact']))
need('actual enclosure width',0<P-Mlo<Q('.000525')<RU/1089<Q('.046889'))
# Exact decimal endpoints, avoiding binary widening in the source comparison.
def ball_exact(s):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',s);assert m,s
 mid,rad=map(Q,m.groups());assert rad>0
 return mid-rad,mid+rad
H7lo,H7hi=ball_exact(base007['H_input_lower_ball']);Hg=H7lo-Hs;Eg=El-Q(base007['E_upper']['strict_upper_exact'])
need('007 lower endpoint exact',H7lo==Q(r12['H007_lower_endpoint_exact']))
need('opposite H strict gap',Hg==Q(r12['H007_minus_H016_gap_lower_exact'])>Q(p['H_gap']))
need('opposite E2 strict gap',Eg==Q(r12['E2016_minus_E2007_gap_strict_lower_exact'])==Q(p['E2_gap']))
need('012 uses same016 endpoint',Hs==Q(r12['H016_strict_upper_exact']) and El==Q(r12['E2016_strict_lower_exact']))
sharelo,sharehi=QL/RU,QU/RL
need('exact prefix fraction',Q('.988805')<sharelo<sharehi<Q('.988806'))
need('literal reported fraction inward','at most 0.9888 of R2' in review and sharelo>Q('.9888'))
# E4-E7: repaired directed values at the old prefix7.
P7=Q(r3['M2_upper_exact']);H7hi2=P7-J;E7plain=energy(U,P7)
for key,shown,true in [('M2','1.129995950',P7),('Hplain','1.063012677',P7),('Himproved','.944106347',H7hi2),('Eplain','763.064677',E7plain)]:
 s=Q(shown);need('corrected prefix7 '+key,(s if key=='M2' else s*s)>true)
need('inward old no-improvement E2',Q('763.064676')**2<E7plain)
need('narrow total repaired',Q('51.061045287604984')<RL<RU<Q('51.061045287604985'))
for N,upper in p['tail_displays'].items():need('directed tail '+N,RU/int(N)**2<Q(upper))
need('peer FLOAT not proof','CONDITIONAL on c1-n3' in review and 'consistency checks; no bound above uses them' in review)
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'frozen_T1_review_sha256':sha(B/'source/T1_review.md'),'H_strict_upper_exact':str(Hs),'E2_strict_upper_exact':str(Es),'H007_minus_H016_lower_exact':str(Hg),'E2016_minus_E2007_lower_exact':str(Eg),'prefix_fraction_lower_exact':str(sharelo),'prefix_fraction_upper_exact':str(sharehi),'prefix_fraction_strict_display':['.988805','.988806'],'source_groups_reintegrated':False,'foreign_code_executed':False,'R1_051':'CONFIRMED main exact recomposition and E4-E7 repairs','literal_fraction':'REFUTED at most.9888; use approximately.9888 or directed upper.988806','verdict':'CONFIRMED R1-051, N4-410 and N4-412 finite consequences under accepted source premises. Complete tail and both Opus469/474 reviews retained. Opposite actual H and E2 orderings, no correction-distance or existence conclusion. REFUTED literal inward fraction display only.'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',result['elapsed_seconds'],'seconds')
