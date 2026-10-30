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
p=read('data/parameters.json');ctx.prec=p['precision_bits'];peer=read('source/N4_prefix_v01.json');prod=read('source/N4_partial.json.gz');component=read('../candidate016_complete_forcing_audit/verification/result.json');acceptance=read('../candidate016_complete_forcing_audit/source/component_acceptance.json');cross=read('../candidate016_cross_archive_audit/verification/result.json');review=read('../divergence_free_upper_review_acceptance/verification/result.json')
external={row['source']:row['sha256'] for row in read('data/external_bindings.json')['rows']}
for rel,h in peer['inputs'].items():need('external source '+rel,external[str(Path(p['peer_root'])/rel)]==h)
for row in read('data/initial_sources.json')['rows']:
 raw=(B/row['local']).read_bytes();original=gzip.decompress(raw) if row['compressed'] else raw
 need('original frozen '+row['local'],hashlib.sha256(original).hexdigest()==row['source_sha256'])
need('N4 finite539checks',peer['check_count']==len(peer['checks'])==539 and all(peer['checks'].values()))
need('T4 complete8874checks',component['check_count']==len(component['checks'])==8874)
need('T4 cross3113checks',cross['check_count']==len(cross['checks'])==3113)
need('T4 Opus review acceptance',review['check_count']==len(review['checks'])==193 and 'CONFIRMED' in review['verdict'])
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
need('exact included prefix',peer['prefix']==p['prefix']==7 and [row['n'] for row in peer['modes']]==[1,3,5,7] and peer['mode_count_replayed']==4 and peer['smallest_omitted_mode']==9)
pi_lo,pi_hi=endpoints(arb.pi());need('positive pi interval',3<pi_lo<pi_hi<4)
mode_results=[];n3peer={row['n']:row for row in read('source/N3_hardy.json')['modes']};qlo_sum=Q(0);qhi_sum=Q(0);Mlo=Q(0);Mhi=Q(0);savedlo=Q(0);savedhi=Q(0);saved_Mlo=Q(0);records=peer['modes'];allgroupcount=0
for n,rec in zip([1,3,5,7],records):
 row=read(f'source/mode_{n:03d}.json');prefix=f'mode{n}';need(prefix+' frozen original hash',sha(B/f'source/mode_{n:03d}.json')==rec['sha256'])
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
L={k:Q(v['strict_lower_exact']) for k,v in component['components'].items()};U={k:Q(v['strict_upper_exact']) for k,v in component['components'].items()}
for k in ['G0','rF','G1','P2']:
 need('accepted component endpoints '+k,L[k]==Q(acceptance['norms'][k]['accepted_lower_exact']) and U[k]==Q(acceptance['norms'][k]['accepted_upper_exact']) and 0<L[k]<U[k])
Slo=L['rF']**2;Shi=U['rF']**2;m=9
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
J=sum((Q(row['cross']) for row in p['floors'].values()),Q(0));h2=sum((Q(row['dual'])**2 for row in p['floors'].values()),Q(0))
need('accepted exact improvement',J==Q(p['improvement'])==Q(cross['improvement_sum_strict_lower_exact'])==Q(peer['selected_improvement_sum_lower_exact']))
need('accepted dual square',h2==Q(cross['H_lower_square_exact'])==Q(peer['H_lower_square_exact']))
need('selected distinct modes',peer['selected_improvement_modes']==[1,3])
improved=new_upper-J;need('complete improved upper consistent',0<h2<improved<new_upper and peer_upper-J==Q(peer['improved_H_square_upper_exact']))
for label,upper,square in [('new plain coarse',p['plain_H_upper'],new_upper),('new improved coarse',p['improved_H_upper'],improved),('N4 plain',peer['plain_H_strict_upper_exact'],new_upper),('N4 improved',peer['conditional_improved_H_strict_upper_exact'],improved)]:need(label+' strict upper',Q(upper)>0 and Q(upper)**2>square)
need('retained H lower',0<Q(p['H_lower'])**2<h2 and 0<Q(peer['H_strict_lower_exact'])**2<h2)
El=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*h2
Eu=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*improved
Epeer=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*(peer_upper-J)
need('N4 energy squares',El==Q(peer['E2_lower_square_exact']) and Epeer==Q(peer['conditional_E2_upper_square_exact']) and Eu<=Epeer)
need('coarse two sided energy',0<Q(p['E2_lower'])**2<El<Eu<Q(p['E2_upper'])**2)
need('N4 directed energy endpoints',0<Q(peer['E2_strict_lower_exact'])**2<El<Eu<Q(peer['conditional_E2_strict_upper_exact'])**2)
need('actual007energy strict ordering',Q(p['baseline007_E2_upper'])==Q(cross['007_E2_strict_upper_exact']) and Q(p['E2_lower'])>Q(p['baseline007_E2_upper']))
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'candidate':p['candidate'],'raw_sha256':p['raw_sha256'],'prefix':p['prefix'],'modes':mode_results,'group_count':allgroupcount,'complete_field_hash':field['representation_sha256'],'complete_mode_count':160,'complete_field_branch_count':1360,'plain_H_strict_upper':p['plain_H_upper'],'improved_H_strict_upper':p['improved_H_upper'],'H_strict_lower':p['H_lower'],'E2_strict_lower':p['E2_lower'],'E2_strict_upper':p['E2_upper'],'M2_upper_exact':str(new_upper),'improved_H_square_upper_exact':str(improved),'H_lower_square_exact':str(h2),'selected_cross_improvement_strict_lower_exact':str(J),'tail_rF_square_upper_exact':str(Shi-qlo_sum),'E2_upper_square_exact':str(Eu),'foreign_code_executed':False,'candidate_moment_integrals_repeated':False,'exact_full_residual_reconstructed_in_this_checker':False,'source_soundness_and_execution_premises':'Retains accepted complete raw-to-residual construction, all source-specific positive-pole moment enclosures and their outward serialization.140original source files rehashed read-only at preparation. This independently composes all124group endpoints as exact rationals and proves complete omitted-mode coverage.','verdict':'CONFIRMED finite whole-field Hardy prefix assembly and its improved upper through the reviewed469 theorem. No discarded tail, exact H, correction distance, inverse, contraction or existence conclusion.'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',allgroupcount,'groups',result['elapsed_seconds'],'seconds')
print('H',p['H_lower'],p['improved_H_upper'],'E2',p['E2_lower'],p['E2_upper'])
