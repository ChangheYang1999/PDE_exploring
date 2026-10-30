"""Independent finite composition, conditional on accepted exact moment certificates."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from collections import Counter, defaultdict
from math import comb
import gzip, hashlib, json, time
from flint import arb, ctx
B=Path(__file__).resolve().parents[1];ctx.prec=2048;started=time.monotonic()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
checks=[]
def need(name,value):
 assert bool(value),name
 checks.append(name)
def bounds(name,x,data):
 need(name+' overlaps saved ball',x.overlaps(arb(data['ball'])))
 need(name+' strict lower',ar(data['strict_lower_exact'])<x.lower())
 need(name+' strict upper',x.upper()<ar(data['strict_upper_exact']))
manifest=read('data/manifest.json')
for rec in manifest:
 need('frozen '+rec['local'],sha(B/rec['local'])==rec['sha256'])
 if 'decoded_sha256' in rec:need('decoded '+rec['local'],hashlib.sha256(gzip.decompress((B/rec['local']).read_bytes())).hexdigest()==rec['decoded_sha256'])
z=json.loads(gzip.decompress((B/'source/production.json.gz').read_bytes()));a=read('source/component_acceptance.json');f=read('source/forcing_result.json');bas=read('source/baseline007.json');be=read('source/baseline007_E2.json');pars=read('data/parameters.json');c=read('data/components.json');target=read('data/targets.json');ext=read('data/external_bindings.json')
need('accepted all-four',a['verdict'].startswith('CONFIRMED') and all(a['checks'].values()) and set(a['norms'])=={'G0','G1','rF','P2'})
need('component acceptance bound',sha(B/'source/component_acceptance.json')==c['acceptance_sha256'])
need('complete own production',z['status'].startswith('COMPLETE OWN') and set(z['norms'])==set(a['norms']) and z['no_spatial_quadrature'])
need('fixture provenance retained',z['frozen_peer_modules_imported_for_own_fixture_helpers'] and not z['peer_field_or_norm_routines_called'])
need('no source execution by assembly',f['foreign_code_executed'] is False and not f['integral_recomputed_here'])
for label,item in [('production',z),('component acceptance',a),('assembly',f),('parameters',pars),('component data',c)]:
 need(label+' immutable profile',item['candidate']=='C1-N1-016-legqs25-quot013' and item['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')
need('c and delta',Q(z['cl_exact'])==Q(4076476460239181,2251799813685248) and Q(z['delta_exact'])==Q(1824676646553933,4076476460239181));delta=Q(z['delta_exact'])
need('production bound from component graph',a['inputs']['research/candidate016_scaled_norm_peer/source/N4_norms_complete_v01.json']==hashlib.sha256(gzip.decompress((B/'source/production.json.gz').read_bytes())).hexdigest())
need('external rehash all true',ext['all_hashes_match'] and all(r['matches'] for r in ext['records']))
N=Path('RUN_ROOT/numerics_audit_N4')
for name,inputs,root in [('forcing62',f['inputs'],N),('components39',a['inputs'],N),('production25',z['inputs'],N),('baseline007_E2',be['inputs'],N),('baseline007_XSW',bas['inputs'],N/'research/registered_norm_assembly')]:
 rows={r['original']:r['sha256'] for r in ext['records'] if r['graph']==name}
 need(name+' complete recorded graph',rows=={str(root/p):h for p,h in inputs.items()})
need('assembly62 exact graph count',len(f['inputs'])==62)
need('139 external graph records',len(ext['records'])==139)
need('baseline007 raw',bas['generator_sha256']==be['source_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21')
need('baseline007 candidate',be['candidate']=='C1-N1-007-d2w-j7-e2bal')
field_counts={};ell_sums={};multiplicities={}
for d in [0,1,2]:
 pairs=0;sums=set();mults=[]
 for order in range(d+1):
  name=f'D{d}_{order}';field=z['fields'][name];records=field['components'];keys=[tuple(r['key']) for r in records]
  need(name+' complete metadata',len(keys)==field['component_count'] and len(set(keys))==len(keys) and keys==sorted(keys))
  h=hashlib.sha256()
  for row in records:h.update(json.dumps(row,sort_keys=True,separators=(',',':')).encode()+b'\n')
  need(name+' representation metadata hash',h.hexdigest()==field['representation_sha256'])
  modes=defaultdict(list)
  for ell,kind,n in keys:
   need(name+' valid angular key '+str((ell,kind,n)),kind in ['c','s'] and n>=0 and (kind!='s' or n>0) and ell>0)
   modes[kind,n].append(ell)
  for mode,branches in modes.items():
   pairs+=len(branches)**2
   sums.update(x+y for x in branches for y in branches)
  mults.append(comb(d,order))
 field_counts[d]=pairs;ell_sums[d]=sums;multiplicities[d]=mults
need('1360 residual components',z['fields']['D0_0']['component_count']==1360)
need('all residual angular modes odd sine',all(r['key'][1]=='s' and r['key'][2]%2==1 for r in z['fields']['D0_0']['components']))
need('Hessian ordered tensor multiplicities',multiplicities[2]==[1,2,1])
coeff=Q(1)
for k in range(1,58):coeff*= (Q(4,5)-(k-1))/k
eps=abs(coeff)*Q(3,5)**57/Q(2,5)
comp={};component_audit={}
for label,d,extra,required_bits in [('G0',0,Q(0),1739),('rF',0,Q(-1),1740),('G1',1,Q(0),1730),('P2',2,Q(-4,5),1690)]:
 n=z['norms'][label];accepted=a['norms'][label];groups=n['groups'];lo=Q(c['norms'][label]['lower_exact']);hi=Q(c['norms'][label]['upper_exact']);comp[label]=(lo,hi)
 need(label+' exact outward source',0<lo==Q(accepted['accepted_lower_exact'])<hi==Q(accepted['accepted_upper_exact']))
 need(label+' all31 groups',len(groups)==n['complete_group_count']==accepted['own_groups']==31 and len({g['ell_sum'] for g in groups})==31)
 need(label+' complete branch sums',{g['ell_sum'] for g in groups}==ell_sums[d])
 need(label+' all ordered pairs',field_counts[d]==n['ordered_pair_count']==accepted['ordered_pair_count']==target['expected_pair_counts'][label])
 bits=[]
 for i,g in enumerate(groups):
  tag=label+' group'+str(i);b=Q(d-3)+Q(g['ell_sum'])*delta/2+extra+g['endpoint_v_order']
  need(tag+' exponent and integrability',b==Q(g['b']) and b>-1)
  need(tag+' exact reconstruction',g['decomposition']['exact_reconstruction'] and Q(g['decomposition']['b'])==b)
  bits.append(g['integral_accuracy_bits'])
  if label=='P2':
   need(tag+' weighted exact reconstruction',g['weighted_decomposition']['exact_reconstruction'] and Q(g['weighted_decomposition']['b'])==b)
   bits.append(g['weighted_integral_accuracy_bits'])
 need(label+' minimum recorded bits',min(bits)==required_bits==accepted['minimum_integral_accuracy_bits'])
 S=sum((arb(g['integral_ball']) for g in groups),arb(0));need(label+' saved S sum',S.overlaps(arb(n['S_ball'])));need(label+' positive total S',S>0)
 if label=='P2':
  need('P2 exact binomial error',Q(n['series_absolute_error'])==eps)
  T=sum((arb(g['weighted_integral_ball']) for g in groups),arb(0));need('P2 saved T sum',T.overlaps(arb(n['T_ball'])))
  constant=arb.pi()/2*ar(Q(5,2))**ar(Q(4,5));squares=(constant*(T-ar(eps)*S),constant*(T+ar(eps)*S))
 else:squares=(arb.pi()*S/2,)*2
 new=[]
 for i,side in enumerate(['lower','upper']):
  need(label+' square '+side,squares[i]>0 and squares[i].overlaps(arb(n['square_'+side+'_ball'])))
  value=squares[i].sqrt();new.append(value)
  need(label+' reconstructed norm '+side,value.overlaps(arb(n['norm_'+side+'_ball'])))
  need(label+' new strict rational bounds '+side,ar(lo)<value.lower() and value.upper()<ar(hi))
  need(label+' corresponding peer40 containing ball '+side,arb(accepted['peer_'+side+'_ball']).contains(arb(n['norm_'+side+'_ball'])))
  need(label+' acceptance own saved ball '+side,arb(accepted['own_'+side+'_ball']).overlaps(arb(n['norm_'+side+'_ball'])))
 need(label+' wholeplane/no full1024bit reproduction',accepted['whole_plane_no_quadrature'] and accepted['full1024bit_peer_endpoint_reproduction'].startswith('OPEN'))
 component_audit[label]={'lower_recomputed':new[0].str(100),'upper_recomputed':new[1].str(100),'strict_lower_exact':str(lo),'strict_upper_exact':str(hi),'groups':31,'ordered_pair_count':field_counts[d],'minimum_recorded_bits':min(bits)}
point_count=0
for point in z['point_checks']['records']:
 for key,v in point['values'].items():
  need('saved Cartesian/polar '+point['x']+','+point['y']+' '+key,v['overlap'] and arb(v['own']).overlaps(arb(v['Cartesian'])));point_count+=1
need('33 saved point comparisons',point_count==33)
def energy(w1,w2):
 return tuple(ar(comp['P2'][i]**2+w1*comp['G1'][i]**2+w2*comp['G0'][i]**2).sqrt() for i in [0,1])
star=energy(16384,262144);e2=(star[0],(star[1]**2+ar(Q(262144*20,21)*comp['rF'][1]**2)).sqrt())
for i,key in enumerate(['lower','upper']):
 bounds('E_star '+key,star[i],f['E_star'][key]);bounds('E2 Hardy proxy '+key,e2[i],f['E2_with_Hardy_proxy'][key])
need('Hardy proxy marked as such',f['E2_with_Hardy_proxy']['actual_H_computed'] is False)
rows=[];pairwise=[];mapping={r['framework']:r for r in f['instances']}
specs=[(name,'Ns',s,16384,262144,t,None) for name,s,t,_ in pars['Ns']]
name,s,t,_=pars['legacy_X3'];specs.append((name,'X3',s,16384,262144,t,None))
specs.extend((name,'XSW',s,w1,w2,t,cw) for name,s,w1,w2,cw,t in pars['XSW'])
need('ten distinct framework rows',len(specs)==len(mapping)==10)
for name,kind,ss,w1,w2,tt,cw in specs:
 s,t=Q(ss),Q(tt);row=mapping[name];constant=Q(48,25) if kind=='XSW' else Q(34)
 need(name+' domain and positive thresholds',0<s<Q(1,1024) and 1-constant*s>0 and t>0)
 need(name+' same kind s threshold',(row['kind'],Q(row['s_exact']),Q(row['threshold_exact']))==(kind,s,t))
 e=energy(w1,w2);lower=(1-ar(constant*s))*e[0];ratio=lower/ar(t)
 bounds(name+' lower',lower,row['forcing_lower_comparison']);bounds(name+' ratio',ratio,row['ratio_lower_comparison'])
 need(name+' sufficient condition fails',lower>ar(t) and ratio>1 and row['sufficient_test_fails'])
 need(name+' no fractional upper claimed',row['fractional_upper'].startswith('OPEN'))
 if kind=='XSW':
  need(name+' exact weights Cw',row['weights']==[w1,w2] and Q(row['Cw_exact'])==Q(cw))
  bounds(name+' energy lower',e[0],row['E_lower']);bounds(name+' energy upper',e[1],row['E_upper'])
 rows.append({'framework':name,'kind':kind,'lower_ball':lower.str(100),'strict_lower_exact':row['forcing_lower_comparison']['strict_lower_exact'],'factor_ball':ratio.str(100),'strict_factor_exact':row['ratio_lower_comparison']['strict_lower_exact']})
for spec,label,peer_order,gapfloor in zip(pars['XSW'],['sharp','sharpw','bL7_5','bL1','trans'],f['XSW_pair_ordering'],target['gap_floors'],strict=True):
 name,ss,w1,w2,cw,tt=spec;base=next(r for r in bas['instances'] if r['label']==label);row=mapping[name]
 need(name+' identical007 parameters',Q(base['s_exact'])==Q(ss) and (base['w1'],base['w2'])==(w1,w2) and Q(base['Cw_exact'])==Q(cw) and Q(base['threshold_exact'])==Q(tt))
 upper=Q(base['upper_comparison']['strict_upper_exact']);lower=Q(row['forcing_lower_comparison']['strict_lower_exact']);gap=lower-upper
 need(name+' baseline strict endpoint',arb(base['upper_comparison']['ball']).upper()<ar(upper))
 need(name+' matching peer pair endpoints',peer_order['framework']==name and Q(peer_order['baseline007_upper_exact'])==upper and Q(peer_order['candidate016_lower_exact'])==lower)
 need(name+' strict actual gap',gap>0 and gap==Q(gapfloor) and peer_order['strict_007_less_than_016'])
 bounds(name+' displayed gap enclosure',ar(gap),peer_order['lower_minus_upper'])
 pairwise.append({'framework':name,'baseline007_upper_exact':str(upper),'candidate016_lower_exact':str(lower),'exact_gap':str(gap),'gap_decimal':gapfloor,'verdict':'CONFIRMED actual same-parameter XSW007<XSW016'})
need('all five actual comparisons',len(pairwise)==5 and f['all_five_pair_orderings_strict'])
estar=Q(target['conditional_Estar_floor']);base_e2=Q(target['conditional007_E2_upper']);sqsum=sum((Q(v)**2 for v in target['conditional_dual_modes'].values()),Q(0))
need('conditional distinct dual modes',set(target['conditional_dual_modes'])=={'1','3'} and all(Q(v)>0 for v in target['conditional_dual_modes'].values()))
need('conditional accepted Estar floor',star[0]>ar(estar))
need('conditional baseline E2 upper',base_e2==Q(be['E_upper']['strict_upper_exact']) and arb(be['E_upper']['ball']).upper()<ar(base_e2) and all(be['checks'].values()))
conditional_gap=estar**2+Q(262144*20,21)*sqsum-base_e2**2
need('conditional E2 squared gap positive',conditional_gap>0)
for rec in manifest:need('unchanged '+rec['local'],sha(B/rec['local'])==rec['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'N4_393_sha256':sha(B/'source/forcing_result.json'),'components':component_audit,'complete_hessian_multiplicities':multiplicities[2],'exact_binomial_error':str(eps),'saved_Cartesian_checks':point_count,'E_star_lower':star[0].str(100),'E_star_upper':star[1].str(100),'E2_Hardy_proxy_upper':e2[1].str(100),'instances':rows,'actual_XSW_orderings':pairwise,'conditional_dual_target':{'mode_floors':target['conditional_dual_modes'],'H_square_floor_exact':str(sqsum),'E2_square_gap_exact':str(conditional_gap),'E2_floor_if_certified':ar(estar**2+Q(262144*20,21)*sqsum).sqrt().str(100),'status':'CONDITIONAL; new016 dual quotient certificates remain OPEN'},'integrals_repeated':False,'foreign_code_executed':False,'verdict':'CONFIRMED complete component finite assembly, all ten sufficient forcing failures and five actual same-parameter XSW007<XSW016 comparisons, under accepted moment premises; no actual E2 or correction-distance ordering, inverse or existence conclusion'}
with (B/'verification/result.json').open('x') as stream:json.dump(out,stream,indent=2);stream.write('\n')
print('PASS',len(checks),'checks',out['utc'],out['elapsed_seconds'],sha(B/'verification/result.json'))
print('E_STAR',out['E_star_lower'],out['E_star_upper'])
for p in pairwise:print(p['framework'],'gap',p['gap_decimal'])
print('CONDITIONAL_DUAL',out['conditional_dual_target'])
