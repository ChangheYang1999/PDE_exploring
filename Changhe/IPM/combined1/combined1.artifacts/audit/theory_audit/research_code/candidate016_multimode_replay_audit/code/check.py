"""Independent exact beta energies, all saved signed intervals and full-tail composition."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,gzip,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=4096
B=Path(__file__).resolve().parents[1];start=time.monotonic()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def payload(p):
 p=B/p;v=p.read_bytes();return gzip.decompress(v) if p.suffix=='.gz' else v
def read(p):return json.loads(payload(p))
def rat(x):
 if isinstance(x,Q):return x
 z=Fraction(str(x));return Q(z.numerator,z.denominator)
def ar(x):
 x=rat(x);return arb(x.numerator)/x.denominator
checks=[]
def need(k,v):
 assert bool(v),k
 checks.append(k)
def inside(v,w):return w.lower()<v.lower() and v.upper()<w.upper()
def integral(P,e):
 mm=[1/(e+1)]
 for j in range(1,len(P)):mm.append(mm[-1]*j/(e+j+1))
 return sum((x*mm[j] for j,x in enumerate(P)),Q(0))/2
def directed(x,places,upper=False):
 m,e=(x.upper() if upper else x.lower()).man_exp();m,e=int(m),int(e)
 v=Fraction(m*2**e) if e>=0 else Fraction(m,2**(-e));den=10**places
 z=v.numerator*den//v.denominator
 return Q(z+(2 if upper else -1),den)
manifest=read('data/manifest.json');initial=read('data/initial_sources.json');pars=read('data/parameters.json')
for row in manifest:need('frozen '+row['local'],sha(B/row['local'])==row['sha256'])
for row in initial['sources']:need('uncompressed '+row['local'],hashlib.sha256(payload(row['local'])).hexdigest()==row['raw_sha256'])
external={r['source']:r['sha256'] for r in initial['checked_peer_graph']}
for path,h in external.items():need('external '+path,sha(path)==h)
need('proof precedes checker',read('data/PROOF_FIRST.json')['proof_sha256']==sha(B/'PROOF.md') and not read('data/PROOF_FIRST.json')['checker_exists'])
prod=read('source/N4_result.json.gz');peer=read('source/N3_full_vectors.json.gz');old=read('../candidate016_cross_archive_audit/verification/result.json');archive=read('../candidate016_cross_archive_audit/source/archive_result.json');prefix=read('../candidate016_prefix31_hardy_audit/verification/result.json');partial=read('../candidate016_prefix31_hardy_audit/source/N4_partial.json.gz');components=read('../candidate016_dual_replay_audit/source/components.json');accepted=read('../candidate016_complete_forcing_audit/verification/result.json');review=read('../partial_hardy_review_acceptance/verification/result.json');review469=read('../reciprocal_hardy_review_acceptance/verification/result.json');baseline=read('../candidate016_dual_replay_audit/source/baseline007.json')
need('complete producer checks',prod['check_count']==len(prod['checks']) and all(prod['checks'].values()))
need('complete producer immutable start',prod['inputs']==read('source/N4_start.json')['inputs'])
need('137 producer bindings',len(external)==len(prod['inputs'])==137)
for p,h in prod['inputs'].items():need('producer input '+p,external[pars['peer_root']+'/'+p]==h)
need('producer actual checker',prod['inputs']['research/candidate016_multimode_dual_cross/code/check.py']==sha(B/'source/N4_check.py'))
need('candidate exact source',prod['candidate']==peer['id']==partial['candidate']==pars['candidate'] and prod['raw_sha256']==peer['source_sha256']==partial['raw_sha256']==pars['raw_sha256'])
need('exact c delta',rat(pars['delta'])==1-1/rat(pars['c']) and partial['cl_exact']==pars['c'] and partial['delta_exact']==pars['delta'])
need('peer vector producer identity',peer['code_sha256']==sha(B/'source/N3_legqs_hdual.py'))
for label,obj,count in [('472 deep',old,3113),('480 fulltail',prefix,4463),('467 components',accepted,8874),('481 both474',review,263),('477 both469',review469,209)]:need(label+' accepted',obj['check_count']==len(obj['checks'])==count)
need('complete components accepted',all(components['checks'].values()))
need('accepted complete source',hashlib.sha256(payload('../candidate016_prefix31_hardy_audit/source/N4_partial.json.gz')).hexdigest()=='7e7b51a4473936d0ee9803fb12df45851ab42a10c0974787feed7c6728e0a58c')
field=partial['fields']['D0_0'];reference={tuple(r['key']):r for r in field['components']}
need('complete field cardinality',len(reference)==field['component_count']==prefix['complete_field_branch_count']==1360 and prefix['complete_mode_count']==160 and field['representation_sha256']==prefix['complete_field_hash'])
need('complete field frequency support',sorted({k[2] for k in reference})==list(range(1,320,2)))
need('sixteen distinct tests',[r['n'] for r in peer['modes']]==[r['n'] for r in prod['modes']]==list(range(1,32,2)))
deepdual={r['n']:rat(r['strict_floor_exact']) for r in archive['rows'] if r['kind']=='dual'};deepcross={r['n']:rat(r['strict_floor_exact']) for r in archive['rows'] if r['kind']=='cross'}
need('accepted deep floors independently bound',all(next(r['strict_floor'] for r in old['rows'] if r['n']==n and r['kind']==kind)==str(f) for kind,vals in [('dual',deepdual),('cross',deepcross)] for n,f in vals.items()))
T=Poly([0,1]);V=Poly([1,-1]);rows=[];lower2=Q(0);selected2=Q(0);J=Q(0);selectedJ=Q(0);qball2=arb(0);total_coeff=total_groups=0
for vector,rec in zip(peer['modes'],prod['modes'],strict=True):
 n=vector['n'];tag='n'+str(n);modefile=f'source/mode_{n:03d}.json.gz';mode=read(modefile)
 need(tag+' frozen mode',hashlib.sha256(payload(modefile)).hexdigest()==rec['sha256'] and mode['n']==n and mode['inputs']==prod['inputs'])
 betas=list(map(rat,vector['betas']));kmin=(n-3)//2;expected={f'{b},{k}' for b in betas for k in range(kmin,vector['kmax']+1)}
 need(tag+' complete basis',len(betas)==len(set(betas))==mode['beta_count']==9 and vector['kmax']==14 and set(vector['x_rational'])==expected and len(expected)==vector['basis_size']==mode['exact_coefficient_count'])
 pby={}
 for label,value in vector['x_rational'].items():
  beta,k=label.rsplit(',',1);beta=rat(beta);k=int(k);x=rat(value);total_coeff+=1
  need(tag+' admissible '+label,beta>Q(3,2) and k>=-1 and 3+2*k-n>=0 and (3+2*k-n)%2==0)
  b=beta-1;pby[b]=pby.get(b,Poly())+x*T**(k+1)
 first={b:(1-2*b*T)*P+2*T*V*P.derivative() for b,P in pby.items()};second={b:(1-2*b*T)*P+2*T*V*P.derivative() for b,P in first.items()};ag={};dg={};pairs=0
 for b,P in pby.items():
  for c,S in pby.items():
   e=b+c-2;need(tag+' integrable energy pair'+str(pairs),e>-1);pairs+=1
   ag[e]=ag.get(e,Poly())+first[b]*first[c]+second[b]*second[c]/(n*n)
   dg[e]=dg.get(e,Poly())+first[b]*first[c]+n*n*P*S
 need(tag+'81 ordered pairs',pairs==81)
 saved_a={rat(r['exponent']):rat(r['integral_exact']) for r in mode['a_groups']};saved_d={rat(r['exponent']):rat(r['integral_exact']) for r in mode['d_groups']}
 need(tag+' complete energy groups',set(ag)==set(dg)==set(saved_a)==set(saved_d) and len(saved_a)==len(mode['a_groups']) and len(saved_d)==len(mode['d_groups']))
 aa=Q(0);dd=Q(0)
 for e,P in sorted(ag.items()):
  av=integral(P,e);dv=integral(dg[e],e);aa+=av;dd+=dv
  need(tag+' beta a '+str(e),av==saved_a[e]);need(tag+' beta d '+str(e),dv==saved_d[e])
 need(tag+' exact positive energies',aa>0 and dd>0 and aa==rat(mode['a_over_pi_exact']) and dd==rat(mode['d_over_pi_exact'])==rat(vector['grad_psi_sq_over_pi_exact']))
 identities=mode['component_identity_checks'];wanted={ell:r for (ell,kind,m),r in reference.items() if kind=='s' and m==n}
 need(tag+' complete projection branches',[r['ell'] for r in identities]==sorted(wanted))
 for identity in identities:
  ref=wanted[identity['ell']];need(tag+' exact component identity '+str(identity['ell']),identity['reference_powers']==ref['powers'] and identity['reference_numerator_sha256']==ref['numerator_sha256'] and len(identity['own_powers'])==4 and all(isinstance(k,int) and k>=0 for k in identity['own_powers']))
 need(tag+' projection digest and pairs',len(mode['complete_projection_sha256'])==64 and isinstance(mode['complete_projection_pairs'],list) and len(mode['complete_projection_pairs'])==2 and all(isinstance(k,int) and k>0 for k in mode['complete_projection_pairs']))
 need(tag+' two complete pairing records',[g['kind'] for g in mode['group_records']]==['dual','cross'])
 values={};groupdetails=[]
 for gr in mode['group_records']:
  kind=gr['kind'];label=tag+' '+kind;file=f'source/n{n:03d}_{kind}_groups.json.gz';gs=read(file)
  need(label+' frozen groups',hashlib.sha256(payload(file)).hexdigest()==gr['sha256'])
  need(label+' format and full bindings',gs['n']==n and gs['kind']==kind and gs['precision_bits']==4096 and gs['saved_ball_digits']==650 and gs['inputs']==prod['inputs'])
  need(label+' nonempty complete group count',len(gs['groups'])==gr['group_count'] and len(gs['groups'])>0)
  exponents=[rat(g['exponent']) for g in gs['groups']];need(label+' distinct sorted exponent groups',exponents==sorted(set(exponents)))
  total=arb(0);radii=arb(0)
  for j,g in enumerate(gs['groups']):
   k=label+' group'+str(j);e=rat(g['exponent']);q=g['endpoint_order'];info=g['decomposition'];v=arb(g['integral_ball']);total_groups+=1
   need(k+' endpoint',isinstance(q,int) and q>=0 and e+q>-1 and rat(info['b'])==e+q)
   need(k+' exact reconstruction',info['exact_reconstruction'] is True and len(g['numerator_sha256'])==64 and info['polynomial_degree']>=-1 and info['denominator_degree']==sum(k for a,k in info['factors']))
   need(k+' positive denominator factors',all(rat(a) in [99,624,2499,9999] and isinstance(k,int) and k>0 for a,k in info['factors']))
   need(k+' finite containing precision',v.is_finite() and v.rel_accuracy_bits()>150 and g['relative_accuracy_bits']>150 and info['relative_accuracy_bits']>150)
   total+=v;radii+=v.rad()
  pairing=total*arb.pi()/2
  need(label+' replay radius and bits',radii.upper()<ar(Q(1,10**200)) and pairing.rel_accuracy_bits()>600 and pairing.is_finite())
  need(label+' fullprecision and saved agreement',pairing.overlaps(arb(gr['pairing_ball'])) and pairing.overlaps(arb(gr['full_precision_pairing_ball'])) and radii.overlaps(arb(gr['sum_absolute_radii_ball'])))
  # Directed floors below are proved from these group intervals themselves.
  den=dd if kind=='dual' else aa;value=abs(pairing)/(arb.pi()*ar(den)).sqrt() if kind=='dual' else pairing**2/(arb.pi()*ar(den));values[kind]=value
  key='quotient_strict_lower_exact' if kind=='dual' else 'improvement_strict_lower_exact';floor=rat(mode[key]);need(label+' independently certified strict floor',floor>0 and ar(floor)<value.lower() and mode[key]==rec[key])
  need(label+' producer containing final',value.overlaps(arb(mode['quotient_ball' if kind=='dual' else 'improvement_ball'])))
  if kind=='dual':need(label+' original containing displays',inside(pairing,arb(vector['F_psi'])) and inside(value,arb(vector['LB'])))
  groupdetails.append({'kind':kind,'groups':len(gs['groups']),'pairing_replay':pairing.str(100),'sum_absolute_radii':radii.str(30),'relative_accuracy_bits':pairing.rel_accuracy_bits(),'strict_floor':str(floor),'value':value.str(100)})
 lf=rat(mode['quotient_strict_lower_exact']);jf=rat(mode['improvement_strict_lower_exact']);chosen_l=max(lf,deepdual.get(n,Q(0)));chosen_j=max(jf,deepcross.get(n,Q(0)))
 need(tag+' maximum lower selection',chosen_l==rat(mode['selected_quotient_strict_lower_exact'])==rat(rec['selected_quotient_strict_lower_exact']))
 need(tag+' maximum upper selection',chosen_j==rat(mode['selected_improvement_strict_lower_exact'])==rat(rec['selected_improvement_strict_lower_exact']))
 lower2+=lf**2;selected2+=chosen_l**2;J+=jf;selectedJ+=chosen_j;qball2+=values['dual']**2
 rows.append({'n':n,'coefficient_count':len(expected),'exact_energy_groups':len(ag),'a_over_pi_sha256':hashlib.sha256(str(aa).encode()).hexdigest(),'d_over_pi_sha256':hashlib.sha256(str(dd).encode()).hexdigest(),'group_replay':groupdetails,'lower_floor':str(lf),'cross_floor':str(jf),'selected_lower_floor':str(chosen_l),'selected_cross_floor':str(chosen_j)})
need('all1224 trial coefficients',total_coeff==1224)
need('peer total containing display',inside(qball2.sqrt(),arb(peer['H_lower_ball'])) and qball2.sqrt().overlaps(arb(prod['H_trial_sum_ball'])))
for key,value in [('H_lower_square_exact',lower2),('selected_H_lower_square_exact',selected2),('improvement_sum_strict_lower_exact',J),('selected_improvement_sum_strict_lower_exact',selectedJ)]:need('exact total '+key,value==rat(prod[key]))
need('deep selection improves or preserves',selected2>=lower2 and selectedJ>=J)
L={k:rat(components['norms'][k]['accepted_lower_exact']) for k in ['G0','G1','P2']};U={k:rat(components['norms'][k]['accepted_upper_exact']) for k in L}
for k in L:need('accepted component '+k,0<L[k]<U[k] and L[k]==rat(accepted['components'][k]['strict_lower_exact']) and U[k]==rat(accepted['components'][k]['strict_upper_exact']))
coreL=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2;coreU=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2;scale=Q(20,21)*2**18;El=coreL+scale*selected2
for label,sq,hkey,ekey,esqkey in [('peer',lower2,'H_strict_lower_exact','E2_strict_lower_exact','E2_lower_square_exact'),('selected',selected2,'selected_H_strict_lower_exact','selected_E2_strict_lower_exact','selected_E2_lower_square_exact')]:
 need(label+' H strict floor',0<rat(prod[hkey])**2<sq and rat(prod[hkey])>0)
 need(label+' energy square',coreL+scale*sq==rat(prod[esqkey]))
 need(label+' E2 strict floor',0<rat(prod[ekey])**2<coreL+scale*sq and rat(prod[ekey])>0)
Bupper=rat(prefix['M2_upper_exact']);Hu2=Bupper-selectedJ;Eu=coreU+scale*Hu2
need('complete fulltail positive upper',0<selected2<Hu2<Bupper and prefix['prefix']==31 and prefix['complete_mode_count']==160)
Hlo=directed(ar(selected2).sqrt(),12);Hup=directed(ar(Hu2).sqrt(),12,True);Elo=directed(ar(El).sqrt(),9);Eup=directed(ar(Eu).sqrt(),9,True)
need('directed H displays by exact squares',0<Hlo and Hlo**2<selected2<Hu2<Hup**2)
need('directed energy displays by exact squares',0<Elo and Elo**2<El<Eu<Eup**2)
baseE=rat(pars['007_E2_upper']);baseH=rat(pars['007_H_lower'])
need('007 accepted energy upper',baseE==rat(baseline['E_upper']['strict_upper_exact'])==rat(prod['baseline007_E2_strict_upper_exact'])==rat(old['007_E2_strict_upper_exact']))
need('007 accepted H lower',ar(baseH)<arb(baseline['H_input_lower_ball']).lower())
need('actual opposite pairwise order',Elo>baseE and Hup<baseH)
for row in manifest:need('unchanged '+row['local'],sha(B/row['local'])==row['sha256'])
for path,h in external.items():need('unchanged external '+path,sha(path)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'candidate':pars['candidate'],'raw_sha256':pars['raw_sha256'],'rows':rows,'coefficient_count':total_coeff,'saved_group_count':total_groups,'H_peer_trial_lower_square_exact':str(lower2),'H_lower_square_exact':str(selected2),'improvement_peer_sum_strict_lower_exact':str(J),'improvement_sum_strict_lower_exact':str(selectedJ),'M2_upper_exact':str(Bupper),'H_upper_square_exact':str(Hu2),'E2_lower_square_exact':str(El),'E2_upper_square_exact':str(Eu),'H_strict_lower_exact':str(Hlo),'H_strict_upper_exact':str(Hup),'E2_strict_lower_exact':str(Elo),'E2_strict_upper_exact':str(Eup),'007_E2_upper_exact':str(baseE),'007_H_lower_exact':str(baseH),'strict_E2_gap_lower':str(Elo-baseE),'strict_H_gap_lower':str(baseH-Hup),'foreign_code_executed':False,'candidate_moment_integrals_repeated':False,'source_premises':'Retains accepted complete exact raw-to-residual construction and each source-specific positive-pole moment enclosure. Independently reconstructs all rational trial energies, resums every 650digit signed group and uses accepted complete prefix31 bound with all144 omitted modes. No integral is repeated.','verdict':'CONFIRMED complete finite sixteen-mode replay and actual two-sided full-field H/E2 enclosures under stated soundness premises. No correction distance, inverse, nonlinear closure or existence implication.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',total_groups,'groups',out['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
for k in ['H_strict_lower_exact','H_strict_upper_exact','E2_strict_lower_exact','E2_strict_upper_exact','strict_E2_gap_lower','strict_H_gap_lower']:print(k,out[k],float(rat(out[k])))
