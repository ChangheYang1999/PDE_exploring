"""Exact trial energies and complete saved interval composition, no field evaluation."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,gzip,time,sys,os
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=4096
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def payload(p):
 p=B/p;raw=p.read_bytes();return gzip.decompress(raw) if p.suffix=='.gz' else raw
def read(p):return json.loads(payload(p))
def rat(x):
 f=Fraction(str(x));return Q(f.numerator,f.denominator)
def ar(x):
 q=rat(x);return arb(q.numerator)/q.denominator
def need(k,v):
 assert bool(v),k
 checks.append(k)
def inside(v,w):return w.lower()<v.lower() and v.upper()<w.upper()
def beta_integral(P,e):
 m=[1/(e+1)]
 for j in range(1,len(P)):m.append(j*m[-1]/(e+j+1))
 return sum((q*m[j] for j,q in enumerate(P)),Q(0))/2
manifest=read('data/manifest.json');initial=read('data/initial_sources.json')
for row in manifest:need('frozen '+row['local'],sha(B/row['local'])==row['sha256'])
for row in initial['sources']:need('original '+row['local'],hashlib.sha256(payload(row['local'])).hexdigest()==row['raw_sha256'])
external={row['source']:row['sha256'] for row in initial['checked_peer_graph']}
for p,h in external.items():need('producer input '+p,sha(p)==h)
first=read('data/PROOF_FIRST.json');need('proof precedes checker',first['proof_sha256']==sha(B/'PROOF.md') and not first['checker_exists'])
r=read('source/N4_result.json.gz');dual=read('source/N3_dual.json.gz');hres=read('source/N3_hres.json.gz');hardy=read('source/N3_hardy.json.gz');startrec=read('source/N4_start.json')
need('producer5704checks',r['check_count']==len(r['checks'])==5704 and all(r['checks'].values()))
need('194producerbindings',len(r['inputs'])==len(external)==194 and r['inputs']==startrec['inputs'])
peerroot=str(Path(initial['sources'][0]['source']).parents[2])
for p,h in r['inputs'].items():need('binding map '+p,external[peerroot+'/'+p]==h)
need('actual checker pinned',r['inputs']['research/candidate017_dual_residual_replay/code/check_v03.py']==sha(B/'source/N4_check.py'))
raw='7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114';cid='C1-N1-017-legqs50-quot013'
for label,obj in [('dual',dual),('hres',hres),('hardy',hardy)]:need(label+' exact source',obj['id']==cid and obj['source_sha256']==raw)
need('result exact source',r['candidate']==cid and r['raw_sha256']==raw)
need('dual current code identity',dual['code_sha256']==sha(B/'source/N3_legqs_hdual.py'))
need('historical residual code mismatch explicit',hres['code_sha256']!=sha(B/'source/N3_legqs_hres.py') and not r['peer_hres_historical_code_matches_frozen_current'] and r['peer_hres_historical_code_sha256_claimed']==hres['code_sha256'])
need('source programs not executed',not r['peer_code_executed'] and not r['peer_F_cache_read'])
old=read('../candidate017_conditional_acceptance/verification/result.json');review=read('../partial_hardy_review_acceptance/verification/result.json')
need('484identity and conditional composition accepted',old['check_count']==2982 and len(old['checks'])==2982)
need('481bothOpusHardyreviews accepted',review['check_count']==263 and len(review['checks'])==263)
modes=list(range(1,32,2))
for label,obj in [('producer',r),('dual',dual),('hres',hres)]:need(label+'16distinct',[v['n'] for v in obj['modes']]==modes)
T=Poly([0,1]);V=Poly([1,-1]);total_coeff=0;total_groups=0;energy_pairs=0;rows=[];lower2=Q(0);sumquo=arb(0);hr={v['n']:v for v in hres['modes']};hy={v['n']:v for v in hardy['modes']}
def energies(vector,mode,n,kind):
 global total_coeff,energy_pairs
 tag=f'n{n} {kind}';pby={};nb=9 if kind=='dual' else 8;bs=list(map(rat,vector['betas']));expected={f'{b},{k}' for b in bs for k in range((n-3)//2,vector['kmax']+1)}
 need(tag+' complete basis',len(bs)==len(set(bs))==nb and vector['kmax']==14 and set(vector['x_rational'])==expected and len(expected)==vector['basis_size'])
 for key,val in vector['x_rational'].items():
  b,k=key.rsplit(',',1);beta,k,x=rat(b),int(k),rat(val);total_coeff+=1
  need(tag+' admissible '+key,beta>Q(3,2) and k>=-1 and 3+2*k-n>=0 and (3+2*k-n)%2==0)
  b=beta-1;pby[b]=pby.get(b,Poly())+x*T**(k+1)
 first={b:(1-2*b*T)*P+2*T*V*P.derivative() for b,P in pby.items()};second={b:(1-2*b*T)*P+2*T*V*P.derivative() for b,P in first.items()};dg={};ag={}
 for b,P in pby.items():
  for c,S in pby.items():
   e=b+c-2;need(tag+' integrable ordered pair '+str(energy_pairs),e>-1);energy_pairs+=1
   dg[e]=dg.get(e,Poly())+first[b]*first[c]+n*n*P*S
   ag[e]=ag.get(e,Poly())+first[b]*first[c]+second[b]*second[c]/(n*n)
 prefix='dual_' if kind=='dual' else '';ds={rat(v['exponent']):rat(v['integral_exact']) for v in mode[prefix+'d_groups']};aa={rat(v['exponent']):rat(v['integral_exact']) for v in mode[prefix+'a_groups']}
 need(tag+' complete energy groups',set(ds)==set(aa)==set(dg)==set(ag) and len(ds)==len(mode[prefix+'d_groups']) and len(aa)==len(mode[prefix+'a_groups']))
 d=Q(0);a=Q(0)
 for e,P in dg.items():
  q=beta_integral(P,e);z=beta_integral(ag[e],e);d+=q;a+=z
  need(tag+' exact d '+str(e),q==ds[e]);need(tag+' exact a '+str(e),z==aa[e])
 need(tag+' complete positive exact energies',d>0 and a>0 and d==rat(mode[prefix+'d_over_pi_exact'])==rat(vector['grad_psi_sq_over_pi_exact']) and a==rat(mode[prefix+'a_over_pi_exact']))
 need(tag+' counts',nb==mode['dual_beta_count' if kind=='dual' else 'beta_count'] and len(expected)==mode['dual_exact_coefficient_count' if kind=='dual' else 'coefficient_count'])
 return d,a
def groups(rec,n):
 global total_groups
 kind=rec['kind'];tag=f'n{n} {kind}';file='source/'+Path(rec['record']).name+'.gz';gs=read(file)
 need(tag+' raw saved hash',hashlib.sha256(payload(file)).hexdigest()==rec['sha256'])
 need(tag+' group format',gs['n']==n and gs['kind']==kind and gs['precision_bits']==4096 and gs['saved_ball_digits']==650 and gs['inputs']==r['inputs'])
 need(tag+' complete group count',len(gs['groups'])==rec['group_count'] and len(gs['groups'])>0)
 ee=[rat(g['exponent']) for g in gs['groups']];need(tag+' distinct sorted exponents',ee==sorted(set(ee)))
 value=arb(0);radius=arb(0)
 for i,g in enumerate(gs['groups']):
  k=tag+' g'+str(i);e=rat(g['exponent']);q=g['endpoint_order'];info=g['decomposition'];v=arb(g['integral_ball']);total_groups+=1
  need(k+' endpoint',isinstance(q,int) and q>=0 and e+q>-1 and rat(info['b'])==e+q)
  need(k+' exact reconstruction',info['exact_reconstruction'] is True and len(g['numerator_sha256'])==64 and info['polynomial_degree']>=-1 and info['denominator_degree']==sum(k for s,k in info['factors']))
  need(k+' positive denominator',all(rat(s) in [99,624,2499,9999] and isinstance(k,int) and k>0 for s,k in info['factors']))
  need(k+' finite precision',v.is_finite() and v.rel_accuracy_bits()>150 and g['relative_accuracy_bits']>150 and info['relative_accuracy_bits']>150)
  value+=v;radius+=v.rad()
 value*=arb.pi()/2
 need(tag+' aggregate radius and precision',radius.upper()<ar(Q(1,10**200)) and value.is_finite() and value.rel_accuracy_bits()>600)
 need(tag+' containing consistency',value.overlaps(arb(rec['value_ball'])) and radius.overlaps(arb(rec['sum_absolute_radii_ball'])))
 return value,{'kind':kind,'groups':len(gs['groups']),'replayed_value':value.str(100),'sum_absolute_radii':radius.str(30),'relative_accuracy_bits':value.rel_accuracy_bits()}
for vec,rec in zip(dual['modes'],r['modes'],strict=True):
 n=vec['n'];tag=f'n{n}';file='source/'+Path(rec['record']).name+'.gz';mode=read(file)
 need(tag+' mode hash',hashlib.sha256(payload(file)).hexdigest()==rec['sha256'])
 need(tag+' same complete bindings',mode['n']==n and mode['inputs']==r['inputs'])
 need(tag+' projection record',len(mode['complete_projection_sha256'])==64 and mode['complete_projection_components']>0 and len(mode['complete_projection_pairs'])==2 and all(isinstance(v,int) and v>0 for v in mode['complete_projection_pairs']))
 d,a=energies(vec,mode,n,'dual');p,g=groups(mode['dual_group_record'],n);quot=abs(p)/(arb.pi()*ar(d)).sqrt();lf=rat(mode['dual_quotient_strict_lower_exact'])
 need(tag+' directed positive dual floor',lf>0 and ar(lf)<quot.lower() and mode['dual_quotient_strict_lower_exact']==rec['quotient_strict_lower_exact'])
 need(tag+' source dual containment',inside(p,arb(vec['F_psi'])) and inside(quot,arb(vec['LB'])) and quot.overlaps(arb(mode['dual_quotient_ball'])))
 lower2+=lf*lf;sumquo+=quot**2;row={'n':n,'dual_floor_exact':str(lf),'energy_coefficient_count':vec['basis_size'],'dual_replay':g}
 need(tag+' residual scope',rec['independent_hres']==(n in [1,3]) and ('residual_trial' in mode)==(n in [1,3]))
 if n in [1,3]:
  rr=mode['residual_trial'];rd,ra=energies(hr[n],rr,n,'hres');rp,gp=groups(rr['pairing'],n);b,gb=groups(rr['cross'],n);qn,gq=groups(rr['rF_square'],n)
  need(tag+' complete positive Q',qn>0 and inside(qn,arb(hy[n]['rF_n_sq'])) and inside(qn.sqrt(),arb(hr[n]['rFn'])))
  dd=arb.pi()*ar(rd);aa=arb.pi()*ar(ra);rg2=qn+2*n*n*(b-rp)+n*n*(aa+dd)
  need(tag+' positive accurate residual square',rg2>0 and rg2.rel_accuracy_bits()>600 and rg2.overlaps(arb(rr['residual_square_ball'])))
  rg=rg2.sqrt();grad=dd.sqrt();lb=grad-rg/n;dq=abs(rp)/grad;upper=grad+rg/n;lo=rat(rr['H_mode_strict_lower_exact']);up=rat(rr['H_mode_strict_upper_exact'])
  need(tag+' directed mode lower',lo>0 and (ar(lo)<lb.lower() or ar(lo)<dq.lower()))
  need(tag+' directed mode upper',ar(up)>upper.upper() and lo<up and upper<qn.sqrt()/n)
  need(tag+' residual source containment',inside(grad,arb(hr[n]['grad_psi'])) and inside(rg,arb(hr[n]['residual_r_g'])))
  for label,v,key in [('Q',qn,'rF_square_ball'),('R',rg,'residual_ball'),('gradient',grad,'gradient_ball'),('dual',dq,'duality_quotient_ball'),('triangle',lb,'triangle_lower_ball'),('upper',upper,'upper_ball')]:need(tag+' mode consistency '+label,v.overlaps(arb(rr[key])))
  row['residual_trial']={'H_mode_strict_lower_exact':str(lo),'H_mode_strict_upper_exact':str(up),'residual_square':rg2.str(100),'residual_precision_bits':rg2.rel_accuracy_bits(),'residual_norm':rg.str(100),'replays':[gp,gb,gq]}
 rows.append(row)
need('all1472coefficients',total_coeff==1472)
need('all1424orderedenergypairs',energy_pairs==16*81+2*64==1424)
need('exact lower square',lower2==rat(r['H_lower_square_exact']))
hfloor=rat(r['H_strict_lower_exact']);need('directed full H floor',0<hfloor and hfloor*hfloor<lower2 and hfloor>rat('.614419598760'))
need('source aggregate containment',inside(sumquo.sqrt(),arb(dual['H_lower_ball'])) and sumquo.sqrt().overlaps(arb(r['H_dual_sum_ball'])))
need('full upper and energy remain OPEN',r['complete_H_upper'].startswith('OPEN:') and r['complete_E2_and_017_less_than007'].startswith('OPEN:'))
for row in manifest:need('unchanged '+row['local'],sha(B/row['local'])==row['sha256'])
for p,h in external.items():need('unchanged producer '+p,sha(p)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'candidate':cid,'raw_sha256':raw,'coefficient_count':total_coeff,'ordered_energy_pair_count':energy_pairs,'saved_group_count':total_groups,'producer_bindings':len(external),'rows':rows,'H_lower_square_exact':str(lower2),'H_strict_lower_exact':str(hfloor),'complete_H_upper':'OPEN','complete_E2_and_017_less_than007':'OPEN','foreign_code_executed':False,'candidate_integrals_repeated':False,'source_soundness_premise':'Complete raw-to-mode projection and each source-specific rational-pole moment enclosure; exact energies and every signed650digit group independently recomposed here. Historical hres program execution is unobserved.','verdict':'CONFIRMED sixteen distinct dual lower trials and individual H1/H3 enclosures; complete H upper, E2 and ordering with007 remain OPEN.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',total_groups,'groups',out['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
print('H>',hfloor)
