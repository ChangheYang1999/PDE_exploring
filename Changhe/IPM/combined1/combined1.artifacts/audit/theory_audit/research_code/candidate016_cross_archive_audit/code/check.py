"""Independent exact beta energies and finite650digit interval-group replay."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,gzip,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=4096
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
manifest=read('data/manifest.json');external=read('data/external_bindings.json')['rows']
for row in manifest:need('frozen '+row['local'],sha(B/row['local'])==row['sha256'])
for row in external:need('external '+row['source'],sha(row['source'])==row['sha256'])
initial=read('data/initial_sources.json')['rows']
for row in initial:
 if 'decompressed_sha256' in row:need('decompressed '+row['local'],hashlib.sha256(payload(row['local'])).hexdigest()==row['decompressed_sha256'])
prod=read('source/cross_result.json');archive=read('source/archive_result.json')
oldbase='../candidate016_dual_replay_audit/'
old=read(oldbase+'verification/result.json');dualprod=read(oldbase+'source/N4_result.json');peer=read(oldbase+'source/exact_vectors.json');components=read(oldbase+'source/components.json')
pars=read('data/parameters.json')
need('candidate bindings',prod['candidate']==archive['candidate']==peer['id']==pars['candidate'] and prod['raw_sha256']==archive['raw_sha256']==peer['source_sha256']==pars['raw_sha256'])
need('complete source cross38',prod['check_count']==len(prod['checks'])==38 and all(prod['checks'].values()))
need('complete source archive566',archive['check_count']==len(archive['checks'])==566 and all(archive['checks'].values()))
need('own2099 dual checks',old['check_count']==len(old['checks'])==2099)
need('own accepted components',all(components['checks'].values()))
need('archive four frequencies and kinds',[(r['n'],r['kind']) for r in archive['rows']]==[(1,'dual'),(1,'cross'),(3,'dual'),(3,'cross')])
need('exact candidate c delta',rat(pars['delta'])==1-1/rat(pars['c']))
# Every producer input hash is in the independently rehashed external receipt.
external_map={r['source']:r['sha256'] for r in external}
peerroot=pars['peer_root']
for tag,source in [('cross',prod),('archive',archive)]:
 for rel,h in source['inputs'].items():need(tag+' complete input '+rel,external_map[peerroot+'/'+rel]==h)
need('source cross checker binding',prod['inputs']['research/candidate016_solenoidal_upper/code/check.py']==sha(B/'source/cross_check.py'))
need('source archive checker binding',archive['inputs']['research/candidate016_pairing_archive/code/check.py']==sha(B/'source/archive_check.py'))
T=Poly([0,1]);V=Poly([1,-1]);rows=[];lower2=Q(0);improvement=Q(0);total_coeff=total_groups=0
for vector in peer['modes']:
 n=vector['n'];tag='mode'+str(n);cross=read(f'source/cross_mode_{n:03d}.json.gz');dualmode=read(oldbase+f'source/N4_mode{n}.json')
 need(tag+' complete projection binding',cross['complete_projection_sha256']==dualmode['complete_projection_sha256'] and cross['complete_projection_pairs']==dualmode['complete_projection_pairs'])
 need(tag+' frozen cross record hash',next(r['sha256'] for r in prod['modes'] if r['n']==n)==hashlib.sha256(payload(f'source/cross_mode_{n:03d}.json.gz')).hexdigest())
 betas=list(map(rat,vector['betas']));expected={f'{b},{k}' for b in betas for k in range(-1 if n==1 else 0,vector['kmax']+1)}
 need(tag+' complete basis',len(betas)==len(set(betas))==13 and set(vector['x_rational'])==expected and len(expected)==vector['basis_size'])
 pby={}
 for label,value in vector['x_rational'].items():
  beta,k=label.rsplit(',',1);beta=rat(beta);k=int(k);x=rat(value);total_coeff+=1
  need(tag+' admissible '+label,beta>Q(3,2) and k>=-1 and 3+2*k-n>=0 and (3+2*k-n)%2==0)
  b=beta-1;pby[b]=pby.get(b,Poly())+x*T**(k+1)
 first={b:(1-2*b*T)*P+2*T*V*P.derivative() for b,P in pby.items()}
 second={b:(1-2*b*T)*P+2*T*V*P.derivative() for b,P in first.items()}
 agroups={};dgroups={};pairs=0
 for b,P in pby.items():
  for c,S in pby.items():
   e=b+c-2;need(tag+' integrable pair'+str(pairs),e>-1);pairs+=1
   agroups[e]=agroups.get(e,Poly())+first[b]*first[c]+second[b]*second[c]/(n*n)
   dgroups[e]=dgroups.get(e,Poly())+first[b]*first[c]+n*n*P*S
 need(tag+'169 ordered pairs',pairs==169)
 saved_a={rat(r['exponent']):rat(r['value']) for r in cross['a_group_integrals_over_pi']}
 saved_d={rat(r['exponent']):rat(r['integral_over_pi_exact']) for r in dualmode['gradient_energy_groups']}
 need(tag+' complete exact exponent sets',set(agroups)==set(saved_a)==set(saved_d) and len(saved_a)==len(cross['a_group_integrals_over_pi']))
 anum=Q(0);dnum=Q(0);energies=[]
 for e,P in sorted(agroups.items()):
  aa=integral(P,e);dd=integral(dgroups[e],e);anum+=aa;dnum+=dd
  need(tag+' independent a beta moment '+str(e),aa==saved_a[e])
  need(tag+' independent d beta moment '+str(e),dd==saved_d[e])
  energies.append({'exponent':str(e),'a_sha256':hashlib.sha256(str(aa).encode()).hexdigest(),'d_sha256':hashlib.sha256(str(dd).encode()).hexdigest()})
 need(tag+' exact positive a',anum>0 and anum==rat(cross['a_over_pi_exact']))
 need(tag+' exact positive d',dnum>0 and dnum==rat(cross['old_d_over_pi_exact'])==rat(dualmode['gradient_energy_over_pi_exact'])==rat(vector['grad_psi_sq_over_pi_exact']))
 for kind,prior,den in [('dual',dualmode,dnum),('cross',cross,anum)]:
  label=tag+' '+kind;file=f'source/archive_mode_{n:03d}_{kind}_groups.json.gz';groupsource=read(file)
  row=next(r for r in archive['rows'] if (r['n'],r['kind'])==(n,kind))
  need(label+' frozen archive groups',hashlib.sha256(payload(file)).hexdigest()==row['group_sha256'])
  need(label+' source format',groupsource['n']==n and groupsource['kind']==kind and groupsource['precision_bits']==4096 and groupsource['saved_ball_digits']==650)
  need(label+' archive all bindings',groupsource['inputs']==archive['inputs'])
  previous=prior['pairing_groups' if kind=='dual' else 'cross_groups'];groups=groupsource['groups'];expected_count=58 if n==1 else 73
  need(label+' complete group count',len(groups)==len(previous)==row['group_count']==expected_count)
  total=arb(0);radii=arb(0);coarse=arb(0);group_rows=[]
  for j,(g,h) in enumerate(zip(groups,previous,strict=True)):
   key=label+' group'+str(j);e=rat(g['exponent']);order=g['endpoint_order'];info=g['decomposition'];priorinfo=h['decomposition'];value=arb(g['integral_ball']);oldvalue=arb(h['integral_ball'])
   need(key+' exact exponent and numerator',g['exponent']==h['exponent_before_order' if kind=='dual' else 'exponent'] and order==h['endpoint_order'] and g['numerator_sha256']==h['numerator_sha256'])
   need(key+' endpoint integrable',isinstance(order,int) and order>=0 and e+order>-1 and rat(info['b'])==e+order)
   need(key+' exact decomposition',info['exact_reconstruction'] is True and priorinfo['exact_reconstruction'] is True and info['b']==priorinfo['b'] and info['factors']==priorinfo['factors'] and info['denominator_degree']==priorinfo['denominator_degree'] and info['polynomial_degree']==priorinfo['polynomial_degree'])
   need(key+' positive pole factors',all(rat(a) in [99,624,2499,9999] and isinstance(k,int) and k>0 for a,k in info['factors']))
   need(key+' containing finite values',value.is_finite() and oldvalue.contains(value) and value.rel_accuracy_bits()>150 and info['relative_accuracy_bits']>150)
   total+=value;radii+=value.rad();coarse+=oldvalue;total_groups+=1
   group_rows.append({'exponent':str(e),'order':order,'numerator_sha256':g['numerator_sha256'],'saved_absolute_radius':value.rad().str(15)})
  pairing=total*arb.pi()/2;full=arb(row['pairing_full_precision_ball']);saved=arb(row['pairing_replayed_ball']);original=arb(prior['pairing_ball' if kind=='dual' else 'b_ball'])
  need(label+' radius bound',radii.upper()<ar(Q(1,10**250)))
  need(label+' signed sum accuracy',pairing.rel_accuracy_bits()>700 and pairing.is_finite())
  need(label+' original strictly contains replay',inside(pairing,original))
  need(label+' replay contains new runtime final',pairing.contains(full))
  need(label+' source saved replay consistent',pairing.overlaps(saved) and total.overlaps(arb(row['sum_raw_ball'])) and radii.overlaps(arb(row['sum_group_absolute_radii_ball'])))
  need(label+' original input ball matches',row['original_pairing_ball']==prior['pairing_ball' if kind=='dual' else 'b_ball'])
  need(label+' certified sign',pairing.lower()>0 if kind=='dual' else pairing.upper()<0)
  val=abs(pairing)/(arb.pi()*ar(den)).sqrt() if kind=='dual' else pairing**2/(arb.pi()*ar(den))
  floor=rat(row['strict_floor_exact']);key='quotient_strict_lower_exact' if kind=='dual' else 'improvement_strict_lower_exact'
  need(label+' strict floor',floor>0 and floor==rat(prior[key])==rat(pars['floors'][str(n)][kind]) and ar(floor)<val.lower())
  need(label+' source quotient consistency',val.overlaps(arb(row['quotient_or_improvement_ball'])) and val.overlaps(arb(prior['quotient_ball' if kind=='dual' else 'b_squared_over_a_ball'])))
  need(label+' old precision limitation persists',coarse.rad()>1 and coarse.contains(0) and (coarse*arb.pi()/2).contains(pairing))
  if kind=='dual':lower2+=floor**2
  else:improvement+=floor
  rows.append({'n':n,'kind':kind,'coefficient_count':len(vector['x_rational']),'exact_energy_groups':len(agroups),'a_over_pi_sha256':hashlib.sha256(str(anum).encode()).hexdigest(),'d_over_pi_sha256':hashlib.sha256(str(dnum).encode()).hexdigest(),'exact_energy_checks':energies,'group_count':len(groups),'group_metadata':group_rows,'sum_absolute_radii':radii.str(50),'pairing_from_saved_groups':pairing.str(100),'replay_accuracy_bits':pairing.rel_accuracy_bits(),'quotient_or_improvement':val.str(100),'strict_floor':str(floor),'old_coarse_group_sum':(coarse*arb.pi()/2).str(30)})
need('all663 exact coefficients',total_coeff==663)
need('all262 group intervals',total_groups==262)
need('same H square floor',lower2==rat(dualprod['H_lower_square_exact'])==rat(old['H_lower_square_exact']))
Hfloor=rat(pars['H_lower']);need('strict H floor',Hfloor>0 and Hfloor**2<lower2 and Hfloor==rat(archive['H_strict_lower_exact']))
need('exact cross floor sum',improvement==rat(pars['improvement_sum'])==rat(prod['improvement_sum_strict_lower_exact'])==rat(archive['improvement_sum_strict_lower_exact']))
L={k:rat(components['norms'][k]['accepted_lower_exact']) for k in ['G0','G1','P2']};need('positive complete component floors',all(v>0 for v in L.values()))
E2=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*lower2
Elow=rat(pars['E2_lower']);Eup=rat(pars['007_upper']);gap=Elow-Eup
need('same E2 exact square',E2==rat(old['E2_lower_square_exact'])==rat(dualprod['E2_lower_square_exact']))
need('strict E2 lower',0<Elow and Elow**2<E2 and Elow==rat(archive['E2_strict_lower_exact']))
need('same007 complete upper',Eup==rat(old['007_E2_strict_upper_exact'])==rat(dualprod['baseline007_E2_strict_upper_exact']))
need('actual same E2 strict gap',gap>0 and gap==rat(pars['gap_lower'])==rat(old['strict_E2_gap']))
for row in manifest:need('unchanged '+row['local'],sha(B/row['local'])==row['sha256'])
for row in external:need('unchanged external '+row['source'],sha(row['source'])==row['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'rows':rows,'H_lower_square_exact':str(lower2),'H_strict_lower_exact':str(Hfloor),'improvement_sum_strict_lower_exact':str(improvement),'E2_lower_square_exact':str(E2),'E2_strict_lower_exact':str(Elow),'007_E2_strict_upper_exact':str(Eup),'strict_E2_gap':str(gap),'foreign_code_executed':False,'candidate_moment_integrals_repeated':False,'new650digit_groups_independently_resummed':True,'complete_H_upper':'OPEN pending full M2 upper and Opus review of469','verdict':'CONFIRMED exact beta cross energies, complete finite650digit group replay and scalar floors, retaining source-bound complete positive-pole moment certificates. Original200digit groups remain insufficient.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),out['utc'],out['elapsed_seconds'],sha(B/'verification/result.json'))
for r in rows:print('mode',r['n'],r['kind'],'groups',r['group_count'],'bits',r['replay_accuracy_bits'],'floor',r['strict_floor'])
print('IMPROVEMENT_SUM>',str(improvement),'E2_GAP>',str(gap))
