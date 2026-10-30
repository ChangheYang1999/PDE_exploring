"""Exact dual denominators and scalar audit, without redoing pole integrals."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=2048
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def rat(x):
 if isinstance(x,Q):return x
 z=Fraction(str(x));return Q(z.numerator,z.denominator)
def ar(x):
 x=rat(x);return arb(x.numerator)/x.denominator
checks=[]
def need(label,cond):
 assert bool(cond),label
 checks.append(label)
def moments(q,n):
 a=[1/(q+1)]
 for j in range(1,n):a.append(a[-1]*j/(q+j+1))
 return a
manifest=read('data/manifest.json')
for row in manifest:need('frozen '+row['local'],sha(B/row['local'])==row['sha256'])
for row in read('data/external_bindings.json'):need('external '+row['source'],sha(row['source'])==row['sha256'])
pars=read('data/parameters.json');peer=read('source/exact_vectors.json');prod=read('source/N4_result.json');components=read('source/components.json');baseline=read('source/baseline007.json');old=read('source/T4_467_result.json')
need('exact candidate raw',prod['candidate']==peer['id']==pars['candidate'] and prod['raw_sha256']==peer['source_sha256']==pars['raw_sha256'])
need('complete production38 passed',prod['check_count']==len(prod['checks'])==38 and all(prod['checks'].values()))
need('source checker hash',prod['inputs']['research/candidate016_dual_lower/code/check.py']==sha(B/'source/N4_check.py'))
need('source vector hash',prod['inputs']['research/candidate016_dual_lower/source/N3_exact_vectors.json']==sha(B/'source/exact_vectors.json'))
need('complete components binding',prod['inputs']['research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json']==sha(B/'source/components.json'))
need('007 same energy binding',prod['inputs']['research/negative_norm_forcing_assembly/verification/result.json']==sha(B/'source/baseline007.json'))
need('original components accepted',all(components['checks'].values()) and old['check_count']==8874)
need('exact c and delta',rat(pars['delta'])==1-1/rat(pars['c']))
need('two distinct odd modes',[r['n'] for r in peer['modes']]==pars['modes']==[1,3])
T=Poly([0,1]);V=Poly([1,-1]);rows=[];lower_square=Q(0)
for peerrow,target in zip(peer['modes'],pars['two_mode_sufficient_targets'],strict=True):
 n=peerrow['n'];tag='mode'+str(n);mode=read(f'source/N4_mode{n}.json');need(tag+' complete bindings',mode['inputs']==prod['inputs'])
 need(tag+' source mode identity',mode['n']==n and mode['precision_bits']==4096)
 betas=list(map(rat,peerrow['betas']));need(tag+' distinct betas',len(betas)==len(set(betas))==13)
 expected_labels={f'{beta},{k}' for beta in betas for k in range(-1 if n==1 else 0,peerrow['kmax']+1)}
 need(tag+' complete basis label set',set(peerrow['x_rational'])==expected_labels and len(expected_labels)==peerrow['basis_size'])
 pby={}
 for label,value in peerrow['x_rational'].items():
  beta,k=label.rsplit(',',1);beta=rat(beta);k=int(k);x=rat(value)
  need(tag+' label'+label,label in expected_labels and beta>Q(3,2) and k>=-1 and 3+2*k>=n and (3+2*k-n)%2==0)
  b=beta-1;pby[b]=pby.get(b,Poly())+x*T**(k+1)
 need(tag+' coefficient and beta counts',len(peerrow['x_rational'])==mode['coefficient_count'] and len(pby)==mode['beta_group_count']==13)
 dby={b:(1-2*b*T)*P+2*T*V*P.derivative() for b,P in pby.items()};groups={};pairs=0
 for b,P in pby.items():
  for c,S in pby.items():
   e=b+c-2;need(tag+' integrable ordered beta pair '+str(pairs),e>-1);pairs+=1
   groups[e]=groups.get(e,Poly())+dby[b]*dby[c]+n*n*P*S
 need(tag+' all169 ordered energy pairs',pairs==169)
 source_groups={rat(r['exponent']):r for r in mode['gradient_energy_groups']}
 need(tag+' all exact gradient groups',set(groups)==set(source_groups) and len(source_groups)==len(mode['gradient_energy_groups']))
 den=Q(0);den_rows=[]
 for e,P in sorted(groups.items()):
  mm=moments(e,len(P));value=sum((x*mm[j] for j,x in enumerate(P)),Q(0))/2;den+=value
  record=source_groups[e]
  need(tag+' independent beta moment group '+str(e),value==rat(record['integral_over_pi_exact']))
  need(tag+' complete polynomial degree '+str(e),P.degree()==record['degree'])
  den_rows.append({'exponent':str(e),'degree':P.degree(),'integral_over_pi_sha256':hashlib.sha256(str(value).encode()).hexdigest()})
 need(tag+' exact positive denominator',den>0 and den==rat(mode['gradient_energy_over_pi_exact'])==rat(peerrow['grad_psi_sq_over_pi_exact']))
 # Calibration source is an independently accepted full projected mode, never a truncated F source.
 calpath=next(Path(row['source']) for row in read('data/external_bindings.json') if row['source'].endswith(f'joint_scaled_dyadic016/verification/{pars["candidate"]}/mode_{n:03d}.json'))
 cal=json.loads(calpath.read_text());need(tag+' complete projected source',mode['complete_projection_sha256']==cal['projection_sha256'] and mode['complete_projection_pairs']==cal['projection_pairs'])
 coarse=arb(0);evidence_rows=[]
 need(tag+' nonempty pairing groups',len(mode['pairing_groups'])>0)
 for j,g in enumerate(mode['pairing_groups']):
  e=rat(g['exponent_before_order']);order=g['endpoint_order'];info=g['decomposition'];v=arb(g['integral_ball'])
  need(tag+' endpoint integrability'+str(j),isinstance(order,int) and order>=0 and e+order>-1)
  need(tag+' exact adjusted exponent'+str(j),rat(info['b'])==e+order)
  need(tag+' decomposition identity'+str(j),info['exact_reconstruction'] is True and info['relative_accuracy_bits']>=mode['minimum_integral_accuracy_bits']>150)
  need(tag+' positive allowed factors'+str(j),all(rat(a) in [99,624,2499,9999] and k>0 for a,k in info['factors']))
  need(tag+' saved containing finite ball'+str(j),v.is_finite())
  coarse+=v;evidence_rows.append({'exponent':str(e),'order':order,'saved_absolute_radius':v.rad().str(20),'runtime_accuracy_bits':info['relative_accuracy_bits']})
 coarse*=arb.pi()/2
 pairing=arb(mode['pairing_ball']);source_quot=arb(mode['quotient_ball']);own_quot=abs(pairing)/(arb.pi()*ar(den)).sqrt();floor=rat(mode['quotient_strict_lower_exact'])
 need(tag+' positive final pairing certificate',pairing.is_finite() and pairing.lower()>0 and pairing.rel_accuracy_bits()>500)
 need(tag+' final pairing inside N3 containing ball',arb(peerrow['F_psi']).contains(pairing))
 need(tag+' quotient recomposition overlap',own_quot.overlaps(source_quot))
 need(tag+' quotient inside N3 containing ball',arb(peerrow['LB']).contains(own_quot))
 need(tag+' strict quotient floor',floor>0 and ar(floor)<own_quot.lower() and str(floor)==prod['mode_strict_floors'][str(n)])
 need(tag+' T4 sufficient target exceeded',floor>rat(target))
 need(tag+' coarse grouping loses final accuracy',coarse.contains(0) and coarse.rad()>1)
 need(tag+' coarse sum consistent with final pairing',coarse.contains(pairing))
 lower_square+=floor**2
 rows.append({'n':n,'coefficient_count':len(peerrow['x_rational']),'beta_groups':len(pby),'ordered_energy_pairs':pairs,'exact_gradient_groups':len(groups),'gradient_energy_over_pi_sha256':hashlib.sha256(str(den).encode()).hexdigest(),'exact_gradient_denominator_matches_both':True,'gradient_group_checks':den_rows,'complete_projection_sha256':mode['complete_projection_sha256'],'pairing_groups_checked':len(evidence_rows),'pairing_group_evidence':evidence_rows,'pairing_final_certificate':pairing.str(100),'quotient_from_final_certificate':own_quot.str(100),'strict_quotient_floor':str(floor),'coarse_group_sum':coarse.str(40),'coarse_group_sum_cannot_certify_pairing':True,'new_pairing_integral':False})
need('exact H square lower',lower_square==rat(prod['H_lower_square_exact']))
Hfloor=rat(pars['H_lower']);need('exact H floor square',0<Hfloor and Hfloor**2<lower_square and Hfloor==rat(prod['H_strict_lower_exact']))
L={k:rat(components['norms'][k]['accepted_lower_exact']) for k in ['G0','G1','P2']}
need('positive component floors',all(x>0 for x in L.values()))
E2=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*lower_square
need('exact E2 square composition',E2==rat(prod['E2_lower_square_exact']))
Elow=rat(pars['E2_lower']);Eup=rat(pars['007_upper']);gap=Elow-Eup
need('exact E2 floor directed',0<Elow and Elow**2<E2 and Elow==rat(prod['E2_strict_lower_exact']))
need('exact007 accepted upper',Eup==rat(baseline['E_upper']['strict_upper_exact'])==rat(prod['baseline007_E2_strict_upper_exact']))
need('actual same E2 ordering',Elow>Eup and prod['actual_E2_007_less_than016'] is True)
need('exact actual E2 separation',gap==rat(pars['gap_lower'])==rat(prod['strict_E2_separation_exact']))
need('H display overlap',ar(lower_square).sqrt().overlaps(arb(prod['H_lower_ball'])))
need('E2 display overlap',ar(E2).sqrt().overlaps(arb(prod['E2_lower_ball'])))
for row in manifest:need('unchanged '+row['local'],sha(B/row['local'])==row['sha256'])
for row in read('data/external_bindings.json'):need('unchanged external '+row['source'],sha(row['source'])==row['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'external_bindings_sha256':sha(B/'data/external_bindings.json'),'rows':rows,'H_lower_square_exact':str(lower_square),'H_strict_lower_exact':str(Hfloor),'E2_lower_square_exact':str(E2),'E2_strict_lower_exact':str(Elow),'007_E2_strict_upper_exact':str(Eup),'strict_E2_gap':str(gap),'foreign_code_executed':False,'candidate_pairing_integrals_repeated':False,'coarse_group_sum_is_a_pairing_reproduction':False,'verdict':'CONFIRMED exact vector admissibility, independent beta-moment denominator reproduction, directed final quotient/energy composition and actual E2(007)<E2(016), retaining N4 full4096bit moment execution as source-bound numerical premise. Saved200digit group logs alone are insufficient for a finite pairing replay.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),out['utc'],out['elapsed_seconds'],sha(B/'verification/result.json'))
for r in rows:print('mode',r['n'],'groups',r['exact_gradient_groups'],r['pairing_groups_checked'],'quotient_floor',r['strict_quotient_floor'],'coarse_sum',r['coarse_group_sum'])
print('E2_GAP>',str(gap))
