"""Independent exact-endpoint replay of a complete candidate016 Hardy prefix."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,gzip,sys,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
 path=B/p;raw=path.read_bytes()
 return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
def endpoint(a,upper=False):
 n,e=(a.upper() if upper else a.lower()).man_exp();n,e=int(n),int(e)
 return Q(n*2**e) if e>=0 else Q(n,2**(-e))
def endpoints(a):return endpoint(a),endpoint(a,True)
def contains_exact(text,lo,hi):
 a,b=endpoints(arb(text));return a<=lo<=hi<=b
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');ctx.prec=p['precision_bits'];peer=read('source/N4_prefix_v04.json');prod=read('../candidate016_prefix31_hardy_audit/source/N4_partial.json.gz');component=read('../candidate016_complete_forcing_audit/verification/result.json');acceptance=read('../candidate016_complete_forcing_audit/source/component_acceptance.json');cross=read('../candidate016_cross_archive_audit/verification/result.json');review=read('../divergence_free_upper_review_acceptance/verification/result.json')
external={row['source']:row['sha256'] for row in read('data/external_bindings.json')['rows']}
for rel,h in peer['inputs'].items():need('external source '+rel,external[str(Path(p['peer_root'])/rel)]==h)
for row in read('data/initial_sources.json')['rows']:
 raw=(B/row['local']).read_bytes();original=gzip.decompress(raw) if row['compressed'] else raw
 need('original frozen '+row['local'],hashlib.sha256(original).hexdigest()==row['source_sha256'])
need('N4 finite3017checks',peer['check_count']==len(peer['checks'])==3017 and all(peer['checks'].values()))
need('T4 complete8874checks',component['check_count']==len(component['checks'])==8874)
need('T4 cross3113checks',cross['check_count']==len(cross['checks'])==3113)
need('T4 Opus review acceptance',review['check_count']==len(review['checks'])==193 and 'CONFIRMED' in review['verdict'])
reciprocal=read('../reciprocal_hardy_review_acceptance/verification/result.json');need('both Opus reviews accepted477',reciprocal['check_count']==len(reciprocal['checks'])==209)
need('all353source graph bindings',len(external)==p['expected_external_sources']==353)
need('proof before checker',read('data/PROOF_FIRST.json')['proof_sha256']==sha(B/'PROOF.md') and not read('data/PROOF_FIRST.json')['checker_exists'])
for key in ['candidate','raw_sha256']:
 need('identity '+key,peer[key]==prod[key]==acceptance[key]==p[key])
need('exact c and delta',prod['cl_exact']==p['c'] and prod['delta_exact']==p['delta'] and 1-1/Q(p['c'])==Q(p['delta']))
field=prod['fields']['D0_0'];branches=field['components'];digest=hashlib.sha256()
for j,row in enumerate(branches):
 digest.update(json.dumps(row,sort_keys=True,separators=(',',':')).encode()+b'\n')
 ell,kind,n=row['key'];need('component legal '+str(j),isinstance(ell,int) and ell>0 and kind=='s' and n in range(1,320,2) and row['degree']>=0 and all(isinstance(k,int) and k>=0 for k in row['powers']) and row['powers'][0]==row['powers'][2]==row['powers'][3]==0 and len(row['numerator_sha256'])==64)
need('ordered complete unique field',len(branches)==field['component_count']==peer['complete_field_component_count']==1360 and [tuple(row['key']) for row in branches]==sorted({tuple(row['key']) for row in branches}))
need('canonical complete field hash',digest.hexdigest()==field['representation_sha256']==peer['F_representation_sha256'])
need('complete160mode support',sorted({row['key'][2] for row in branches})==list(range(1,320,2)) and peer['complete_field_mode_count']==160)
need('complete checked Cartesian premise',prod['point_checks']['value_count']==33 and prod['point_checks']['minimum_accuracy_bits']>150)
need('exact included prefix',peer['prefix']==p['prefix']==47 and [row['n'] for row in peer['modes']]==list(range(1,48,2)) and peer['mode_count_replayed']==24 and peer['smallest_omitted_mode']==49)
pi_lo,pi_hi=endpoints(arb.pi());need('positive pi interval',3<pi_lo<pi_hi<4)
mode_results=[];n3peer={row['n']:row for row in read('../candidate016_prefix31_hardy_audit/source/N3_hardy.json')['modes']};qlo_sum=Q(0);qhi_sum=Q(0);Mlo=Q(0);Mhi=Q(0);savedlo=Q(0);savedhi=Q(0);saved_Mlo=Q(0);records=peer['modes'];allgroupcount=0
for n,rec in zip(range(1,48,2),records):
 mode_path=(f'../candidate016_prefix31_hardy_audit/source/mode_{n:03d}.json' if n<33 else f'source/mode_{n:03d}.json');row=read(mode_path);prefix=f'mode{n}';need(prefix+' frozen original hash',sha(B/mode_path)==rec['sha256'])
 for key in ['candidate','raw_sha256']:need(prefix+' '+key,row[key]==p[key])
 need(prefix+' source field and status',row['n']==n and row['F_representation_sha256']==field['representation_sha256'] and row['status']=='CONFIRMED complete own mode integral')
 for rel,h in row['inputs'].items():need(prefix+' input '+rel,external[str(Path(p['peer_root'])/rel)]==h)
 branch=[b for b in branches if b['key'][2]==n];ells=[b['key'][0] for b in branch]
 need(prefix+' complete ordered pairs',row['component_count']==len(branch) and row['ordered_pair_count']==len(branch)**2)
 need(prefix+' complete groups',row['group_count']==len(row['groups'])==rec['group_count'] and [g['ell_sum'] for g in row['groups']]==sorted({e+f for e in ells for f in ells}))
 lo_sum=Q(0);hi_sum=Q(0);minbits=10000000
 for j,g in enumerate(row['groups']):
  label=prefix+'/group'+str(j);allgroupcount+=1;power=g['powers'];e=Q(g['b']);dec=g['decomposition'];ball=arb(g['integral_ball']);lo,hi=endpoints(ball)
  need(label+' endpoint',isinstance(g['endpoint_v_order'],int) and g['endpoint_v_order']>=0 and e==Q(g['ell_sum'])*Q(p['delta'])/2-4+g['endpoint_v_order'] and e>-1)
  need(label+' positive factor structure',power[0]==power[2]==power[3]==0 and all(isinstance(k,int) and k>=0 for k in power) and dec['factors']==([[str(624),power[1]]] if power[1] else []) and dec['denominator_degree']==sum(power))
  need(label+' exact decomposition premise',dec['exact_reconstruction'] and Q(dec['b'])==e and dec['relative_accuracy_bits']==g['integral_accuracy_bits'] and len(g['numerator_v_sha256'])==64 and g['degree_v']>=0)
  need(label+' valid precision',ball.is_finite() and lo<=hi and ball.rel_accuracy_bits()>150 and g['integral_accuracy_bits']>150)
  lo_sum+=lo;hi_sum+=hi;minbits=min(minbits,ball.rel_accuracy_bits())
 need(prefix+' cancellation resolved',0<lo_sum<=hi_sum and hi_sum-lo_sum<Q(1,10**100))
 qlo=lo_sum*pi_lo/2;qhi=hi_sum*pi_hi/2
 source_lo,source_hi=endpoints(arb(row['rF_n_sq']))
 need(prefix+' source mode interval consistency',source_lo<=qhi and qlo<=source_hi)
 need(prefix+' N3 display containment',contains_exact(n3peer[n]['rF_n_sq'],qlo,qhi))
 sL=Q(rec['q_lower_exact']);sU=Q(rec['q_upper_exact'])
 need(prefix+' published prefix endpoints contain exact replay',sL<=qlo<=qhi<=sU)
 rlo,rhi=endpoints(arb(row['rF_n']));hlo,hhi=endpoints(arb(row['H_n_UB']))
 need(prefix+' source square root consistency',0<rlo and rlo*rlo<=qhi and qlo<=rhi*rhi and 0<hlo and (n*hlo)**2<=qhi and qlo<=(n*hhi)**2)
 qlo_sum+=qlo;qhi_sum+=qhi;Mlo+=qlo/(n*n);Mhi+=qhi/(n*n);savedlo+=sL;savedhi+=sU;saved_Mlo+=sL/(n*n)
 mode_results.append({'n':n,'group_count':len(row['groups']),'minimum_parsed_group_bits':minbits,'q_lower_exact':str(qlo),'q_upper_exact':str(qhi),'source_prefix_encloses_exact_replay':True})
need('complete708group assembly',allgroupcount==p['expected_groups']==708)
L={k:Q(v['strict_lower_exact']) for k,v in component['components'].items()};U={k:Q(v['strict_upper_exact']) for k,v in component['components'].items()}
for k in ['G0','rF','G1','P2']:
 need('accepted component endpoints '+k,L[k]==Q(acceptance['norms'][k]['accepted_lower_exact']) and U[k]==Q(acceptance['norms'][k]['accepted_upper_exact']) and 0<L[k]<U[k])
Slo=L['rF']**2;Shi=U['rF']**2;m=49
need('exact complete total square',Slo==Q(peer['full_rF_square_lower_exact']) and Shi==Q(peer['full_rF_square_upper_exact']))
new_upper=Shi/(m*m)+sum(((Q(1,rec['n']**2)-Q(1,m*m))*Q(rec['q_upper_exact']) for rec in mode_results),Q(0))
new_split=Mhi+(Shi-qlo_sum)/(m*m)
need('complete tail nonnegative',Shi-qlo_sum>0)
need('positive coefficient versus split exact identity',new_split-new_upper==(qhi_sum-qlo_sum)/(m*m)>=0)
peer_upper=Shi/(m*m)+sum(((Q(1,rec['n']**2)-Q(1,m*m))*Q(rec['q_upper_exact']) for rec in records),Q(0))
peer_split=sum((Q(rec['q_upper_exact'])/rec['n']**2 for rec in records),Q(0))+(Shi-savedlo)/(m*m)
need('N4 positive formula',peer_upper==Q(peer['positive_coefficient_formula_upper_exact'])==Q(peer['M2_upper_exact']))
need('N4 split formula',peer_split==Q(peer['split_formula_upper_exact']) and peer_split-peer_upper==(savedhi-savedlo)/(m*m)>=0)
need('new exact-endpoint upper at least as sharp',0<Mlo<new_upper<=peer_upper and saved_Mlo==Q(peer['M2_lower_exact']))
need('N4 exact tail upper',Shi-savedlo==Q(peer['tail_rF_square_upper_exact']))
need('N4 exact tail lower',max(Q(0),Slo-savedhi)==Q(peer['tail_rF_square_lower_exact']))

complete=read('source/N4_complete_v02.json');own=read('../candidate016_multimode_replay_audit/verification/result.json');prior=read('../candidate016_complete_bounds_reciprocal/verification/result.json');general=read('../partial_hardy_review_acceptance/verification/result.json')
need('accepted486 exact trials',own['check_count']==len(own['checks'])==13380)
need('accepted488 complete prior',prior['check_count']==len(prior['checks'])==121)
need('both Opus general-prefix reviews accepted481',general['check_count']==len(general['checks'])==263)
need('N4 finite4438checks',complete['check_count']==len(complete['checks'])==4438 and all(complete['checks'].values()))
for rel,h in complete['inputs'].items():need('complete producer source '+rel,external[str(Path(p['peer_root'])/rel)]==h)
for key in ['candidate','raw_sha256']:need('complete identity '+key,complete[key]==own[key]==p[key])
need('sixteen distinct selected trials',[r['n'] for r in complete['selected_modes']]==[r['n'] for r in own['rows']]==peer['selected_improvement_modes']==list(range(1,32,2)))
h2=J=Q(0)
for a,b in zip(own['rows'],complete['selected_modes']):
 n=a['n'];l=Q(a['selected_lower_floor']);j=Q(a['selected_cross_floor'])
 need(f'n{n} accepted selected floor equality',0<l==Q(b['selected_lower']) and 0<j==Q(b['selected_improvement']));h2+=l*l;J+=j
need('accepted exact improvement',J==Q(own['improvement_sum_strict_lower_exact'])==Q(peer['selected_improvement_sum_lower_exact'])==Q(complete['selected_improvement_sum_lower_exact']))
need('accepted exact dual square',h2==Q(own['H_lower_square_exact'])==Q(peer['H_lower_square_exact'])==Q(complete['H_lower_square_exact']))
need('complete prefix and source',complete['prefix']==47 and complete['all160_source_modes_covered'] and complete['individually_integrated_Hardy_modes']==24 and peer['complete_uncomputed_tail_retained'] is True and peer['all160_individual_mode_integrals_replayed'] is False)
need('N4 same complete M2',peer_upper==Q(complete['complete_M2_upper_exact']))
delta=peer_upper-new_upper
need('exact positive source interval difference',delta==sum(((Q(1,a['n']**2)-Q(1,49**2))*(Q(a['q_upper_exact'])-Q(b['q_upper_exact'])) for a,b in zip(records,mode_results)),Q(0)) and 0<=delta<Q(1,10**500))
improved=new_upper-J;peer_improved=peer_upper-J
need('improved complete H interval',0<h2<improved<=peer_improved==Q(complete['H_upper_square_exact'])==Q(peer['improved_H_square_upper_exact']))
need('strictly improves previous upper',peer_improved<Q(prior['H_upper_square_exact']))
loE=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*h2
hiE=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*improved
peerE=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*peer_improved
need('E2 lower equality',loE==Q(complete['E2_lower_square_exact'])==Q(peer['E2_lower_square_exact'])==Q(own['E2_lower_square_exact']))
need('E2 upper equality',peerE==Q(complete['E2_upper_square_exact'])==Q(peer['conditional_E2_upper_square_exact']) and peerE-hiE==Q(20,21)*2**18*delta)
hl,hu,el,eu=[Q(complete[k]) for k in ['H_strict_lower_exact','H_strict_upper_exact','E2_strict_lower_exact','E2_strict_upper_exact']]
need('directed full H endpoints',0<hl*hl<h2<peer_improved<hu*hu)
need('directed full E2 endpoints',0<el*el<loE<peerE<eu*eu)
for key,tailkey in [('H_strict_lower_exact','H_strict_lower_exact'),('H_strict_upper_exact','conditional_improved_H_strict_upper_exact'),('E2_strict_lower_exact','E2_strict_lower_exact'),('E2_strict_upper_exact','conditional_E2_strict_upper_exact')]:need('N4 endpoint equality '+key,Q(complete[key])==Q(peer[tailkey]))
need('lower endpoints unchanged',hl==Q(prior['H_strict_lower_exact']) and el==Q(prior['E2_strict_lower_exact']))
need('upper endpoints improved',hu<Q(prior['H_strict_upper_exact']) and eu<Q(prior['E2_strict_upper_exact']))
need('outward coarse H display',Q(p['H_lower'])<hl<hu<Q(p['improved_H_upper']))
need('outward coarse E2 display',Q(p['E2_lower'])==el<eu<Q(p['E2_upper']))
base=read('../candidate016_dual_replay_audit/source/baseline007.json')
import re
m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',base['H_input_lower_ball']);need('exact007 containing lower',m is not None and Q(m[2])>0)
h07=Q(m[1])-Q(m[2]);e07=Q(base['E_upper']['strict_upper_exact']);hgap=h07-hu;egap=el-e07
need('identical007energy premise',e07==Q('606.820219')==Q(p['baseline007_E2_upper']))
need('strict E2 opposite gap',egap==Q(complete['E2016_minus_E2007_strict_lower_exact'])==Q('21.759869526341'))
need('strict H opposite gap',hgap==Q(complete['H007_minus_H016_strict_lower_exact'])>Q(p['H_gap_lower']))
need('complete reviews explicit',complete['general_and_tail_reviews_completed'] is True)
need('no peer execution or repeated integral',complete['peer_code_executed'] is False and complete['new_source_integrals'] is False and peer['peer_code_executed'] is False and peer['new_mode_integrals_performed'] is False)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'precision_bits':ctx.prec,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'manifest_sha256':sha(B/'data/manifest.json'),'candidate':p['candidate'],'raw_sha256':p['raw_sha256'],'prefix':47,'complete_field_mode_count':160,'complete_field_component_count':1360,'individually_integrated_modes':24,'omitted_modes_retained':136,'group_count':allgroupcount,'source_binding_count':len(external),'modes':mode_results,'M2_independent_upper_exact':str(new_upper),'M2_producer_upper_exact':str(peer_upper),'producer_minus_independent_upper_exact':str(delta),'H_lower_square_exact':str(h2),'H_independent_upper_square_exact':str(improved),'H_upper_square_exact':str(peer_improved),'E2_lower_square_exact':str(loE),'E2_independent_upper_square_exact':str(hiE),'E2_upper_square_exact':str(peerE),'H_strict_lower_exact':str(hl),'H_strict_upper_exact':str(hu),'E2_strict_lower_exact':str(el),'E2_strict_upper_exact':str(eu),'strict_H_gap_lower':str(hgap),'strict_E2_gap_lower':str(egap),'foreign_code_executed':False,'new_candidate_integrals':False,'verdict':'CONFIRMED complete prefix47 and N4-427/428 two-sided H/E2 bounds; every708 saved group is independently resummed and136 omitted modes remain covered. Source-specific integration soundness retained; no new candidate distance or existence conclusion.'}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(r['utc'],len(checks),'checks',allgroupcount,'groups',r['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
