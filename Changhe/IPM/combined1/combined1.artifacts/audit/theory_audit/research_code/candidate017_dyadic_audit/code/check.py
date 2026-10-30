"""Own exact local jet and finite two-endpoint energy/cell replay."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import json,gzip,sys,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(1000000)
B=Path(__file__).resolve().parents[1];ctx.prec=1024
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def A(q):q=Q(q);return arb(q.numerator)/arb(q.denominator)
def read(rel):
 p=B/rel;b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def binom(a,n):
 z=Q(1)
 for k in range(n):z*=Q(a-k)/(k+1)
 return z
def main():
 tick=time.monotonic();checks={}
 def ck(label,test):
  assert label not in checks,label
  assert test,label
  checks[label]=True
 manifest=read('data/manifest.json')
 for z in manifest:
  p=B/z['local'];ck('binding:'+z['local'],sha(p)==z['sha256'])
  if z.get('decoded_sha256'):ck('decoded:'+z['local'],sha256(gzip.decompress(p.read_bytes())).hexdigest()==z['decoded_sha256'])
 pars=read('data/parameters.json');raw=read('data/candidate017.json.gz');out=read('source/N4_production.json');start=read('source/N4_start.json');bound=read('source/N4_bound.json');acc=read('source/N4_acceptance.json');peer=read('source/N3_cells.json');origin=read('source/origin_comparison.json');ext=read('data/external_bindings.json')
 ck('47_external_source_observation',len(ext['bindings'])==47==acc['source_count'] and ext['all_matched'] and all(z['expected']==z['observed'] for z in ext['bindings']))
 ck('acceptance_hash',sha(B/'source/N4_acceptance.json')==pars['N4_acceptance_sha256'])
 ck('production_wrapper_bindings',bound['result_sha256']==sha(B/'source/N4_production.json') and bound['start_sha256']==sha(B/'source/N4_start.json') and bound['all_before_hashes_unchanged'])
 ck('fresh_dynamic_source_closure',len(start['sources'])==bound['source_count']==21 and len(start['module_edges'])==8 and start['earlier_mode_records']=={})
 ck('two_positive_weights_only',out['two_weights_only'] and not out['foreign_code_executed'])
 ck('N3_source_code',peer['code_sha256']==sha(B/'source/N3_legqs_cells.py'))
 ck('raw_candidate_binding',sha256(gzip.decompress((B/'data/candidate017.json.gz').read_bytes())).hexdigest()==pars['raw_sha256']==peer['source_sha256']==origin['generator_sha256'])
 ck('candidate_id',pars['candidate']==peer['id']==origin['candidate'])
 c=Q(pars['c']);ck('same_c',c==Q(raw['cl_exact'])==Q(origin['c_exact']));gamma=1/c;delta=1-gamma;prod=out['results'][pars['candidate']]
 sums=[Q(0),Q(0),Q(0)];touched=terms=0;scales=set()
 for g in raw['generators']:
  m=int(g['m']);w=int(g['spec'][1]);kind=g['spec'][0]
  assert m>=0 and w>=0 and kind in ['mono','leg','legq','legqs']
  N=0 if kind=='mono' else int(g['spec'][2]);q=int(g['spec'][3]) if kind in ['legq','legqs'] else 0;R=Q(g['spec'][4]) if kind=='legqs' else Q(1)
  assert N>=0 and q>=0 and R>0;scales.add(str(R))
  if m+w>2:continue
  touched+=1;p=(3+gamma-int(g['j'])*delta)/2
  for k in range(min(N,2-m-w)+1):
   nn=2-m-w-k;d=w+q+k
   series=sum((binom(p-m,i)*binom(-d,nn-i)/R**(2*(nn-i)) for i in range(nn+1)),Q(0))
   sums[m]+=Q(g['coef'])*(-1)**(N+k)*comb(N,k)*comb(N+k,k)/R**(2*(w+k))*series;terms+=1
 a22=2*sums[0]-6*sums[2];a04=sums[0]-sums[1]+sums[2];strain=4*a22;a0=-strain-24*a04
 ck('only_scales_1_50',scales=={'1','50'})
 ck('exact_origin_strain',strain==1-c==Q(prod['strain_exact'])==Q(origin['origin']['strain']))
 ck('exact_origin_a0',a0==Q(prod['a0_exact'])==Q(origin['origin']['a0']))
 ck('origin_quartic_coefficients',a22==Q(origin['origin']['x2y2_coefficient']) and a04==Q(origin['origin']['y4_coefficient']))
 ck('origin_hypotheses',1<c<2 and a0>=5*c-4)
 ck('origin_display',A(a0).overlaps(arb(origin['a0_arb'])))
 norms={};energyrows=[]
 for suffix in ['007-d2w-j7-e2bal','017-legqs50-quot013']:
  candidate='C1-N1-'+suffix;short=suffix[:3];total={str(a):arb(0) for a in [Q(1,4),Q(7,4)]}
  for n in [1,3]:
   rel=f'source/mode_{short}_{n}.json';z=read(rel);key=f'{short}:mode{n}:'
   original=f'research/candidate017_dyadic_preparation/verification/{candidate}/mode_{n:03d}.json'
   ck(key+'mode_hash',sha(B/rel)==bound['final_modes'][original])
   ck(key+'candidate_source_code',z['candidate']==candidate and z['mode']==n and z['code_sha256']==sha(B/'source/N4_check.py'))
   ck(key+'raw_hash',z['raw_sha256']==(pars['raw_sha256'] if short=='017' else '153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'))
   ck(key+'derivative_identity_assertions',z['Cartesian_polar_equal'] and z['mixed_derivatives_equal'])
   ends=z['endpoints'];ck(key+'16_branches',[e['ell'] for e in ends]==list(range(1,17)))
   for e in ends:
    margin=e['ell']*delta+2*e['endpoint_order']-2
    ck(key+f"endpoint{e['ell']}",margin>0 and margin==Q(e['diagonal_integrability_margin']))
    ck(key+f"powers{e['ell']}",len(e['powers'])==4 and all(isinstance(k,int) and k>=0 for k in e['powers']) and all(k==0 for i,k in enumerate(e['powers']) if short=='007' or i!=2))
   exponents=set();paircount=0
   for i,e in enumerate(ends):
    for f in ends[i:]:
     b=(e['ell']+f['ell'])*delta/2+e['endpoint_order']+f['endpoint_order']-3
     ck(key+f"cross{e['ell']}_{f['ell']}",b>-1);exponents.add(b);paircount+=1
   ck(key+'crosspair_group_counts',paircount==z['pairs']==136 and len(exponents)==z['group_count']==len(z['decompositions'])==51)
   ck(key+'decomposition_exponents',{Q(d['b_without_a']) for d in z['decompositions']}==exponents)
   for i,d in enumerate(z['decompositions']):
    ck(key+f'decomposition_assertion{i}',d['exact_reconstruction'] and d['denominator_degree']==sum(k for a,k in d['factors']) and all(Q(a)==2499 and k>0 for a,k in d['factors']) and (short!='007' or d['factors']==[]))
   ck(key+'two_weights',[Q(w['a']) for w in z['weights']]==[Q(1,4),Q(7,4)])
   if short=='007':
    ck(key+'six_polynomial_calibrations',set(z['polynomial_calibration'])=={'projection','dx','dy','xx','yy','xy'} and all(z['polynomial_calibration'].values()));old=read(f'source/prior_007_{n}.json')
   for w in z['weights']:
    a=Q(w['a']);wk=key+'a'+str(a)+':'
    ck(wk+'51_group_exponents',len(w['groups'])==51 and [Q(g['b']) for g in w['groups']]==sorted(b+a for b in exponents))
    en=arb.pi()/2*sum((arb(g['integral']) for g in w['groups']),arb(0));saved=arb(w['energy'])
    ck(wk+'complete_group_sum',en>0 and en.overlaps(saved) and en.sqrt().overlaps(arb(w['norm'])))
    ck(wk+'production_accuracy_assertions',w['accuracy_bits']>150 and all(g['accuracy_bits']>150 for g in w['groups']))
    if short=='007':
     prev=next(x for x in old['weights'] if Q(x['a'])==a)
     ck(wk+'prior_007_energy',w['accepted007_energy_overlap'] and en.overlaps(arb(prev['energy'])) and saved.overlaps(arb(prev['energy'])))
    total[str(a)]+=en
  for a,en in total.items():
   norm=en.sqrt();saved=out['results'][candidate]
   ck(short+':sum_energy'+a,en.overlaps(arb(saved['square_norms'][a])) and norm.overlaps(arb(saved['norms'][a])))
   energyrows.append({'candidate':candidate,'a':a,'group_sum_energy':en.str(100),'group_sum_norm':norm.str(100)})
   if short=='017':
    index=0 if a=='1/4' else 6;p=peer['cells'][index];display=arb(p['N_h_modes13_sq_ball'])
    ck('017:N3_containing_square'+a,display.contains(en) and Q(p['cell'][1])==Q(a))
    ck('017:N4_peer_containing_assertion'+a,prod['peer_comparisons'][a]['containing_display'] and en.overlaps(arb(prod['peer_comparisons'][a]['own_square'])))
    norms[a]=norm
 d=c-1;star=(A(2*d-3)+A((2*d-3)**2+16*d).sqrt())/8;H=(A(d)-star)*(4*arb.pi()*star*(1+star)).sqrt()
 ck('H_maximum_domain_and_value',0<star<A(d) and H>0 and star.overlaps(arb(prod['smax'])) and H.overlaps(arb(prod['Hmax'])))
 cap=1+1/c;ck('last_cell_endpoint',Q(3,2)<cap<Q(7,4)<2);points=[Q(k,4) for k in range(7)]+[cap];cells=[]
 ck('seven_production_cells',len(prod['seven_cells'])==7 and prod['conditional_all_seven_excluded'])
 for i,(lo,hi) in enumerate(zip(points[:-1],points[1:],strict=True)):
  e=Q(1,4) if i==0 else Q(7,4);r=prod['seven_cells'][i];key=f'cell{i}:'
  ck(key+'monotonicity_endpoints',e>=hi and Q(r['left'])==lo and Q(r['right'])==hi and Q(r['norm_evaluation_at'])==e)
  lhs=arb(5)**A((lo-2)/2)*norms[str(e)];rhs=H*A((1+c-c*lo)/(1+lo));ratio=lhs/rhs;gap=lhs-rhs;floor=Q(r['strict_ratio_floor'])
  ck(key+'strict_ratio_and_gap',rhs>0 and gap>0 and ratio>A(floor)>1 and r['excluded'])
  for name,value in [('projected_norm',norms[str(e)]),('lower',lhs),('upper',rhs),('gap',gap),('ratio',ratio)]:ck(key+name,value.overlaps(arb(r[name])))
  cells.append({'left':str(lo),'right':str(hi),'evaluation_at':str(e),'ratio':ratio.str(100),'strict_floor':str(floor),'gap':gap.str(100)})
 floor=min(Q(z['strict_floor']) for z in cells)
 ck('minimum_floor_on_second_cell',floor==Q(pars['minimum_ratio_floor'])==Q(acc['minimum_strict_ratio_floor'])==Q(cells[1]['strict_floor']))
 ck('complete_cell_union',cells[0]['left']=='0' and Q(cells[-1]['right'])==cap and all(cells[i]['right']==cells[i+1]['left'] for i in range(6)))
 for z in manifest:ck('unchanged:'+z['local'],sha(B/z['local'])==z['sha256'])
 result={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'candidate':pars['candidate'],'raw_generators':len(raw['generators']),'origin_contributors':touched,'origin_summands':terms,'strain_exact':str(strain),'a0_exact':str(a0),'a0_margin_exact':str(a0-(5*c-4)),'a0_ball':A(a0).str(100),'smax':star.str(100),'Hmax':H.str(100),'energy_rows':energyrows,'cells':cells,'minimum_strict_ratio_floor':str(floor),'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'elapsed_seconds':time.monotonic()-tick,'field_integrations_repeated':False,'foreign_code_executed':False,'L2_distance_used':False,'complete_upper_norm':False,'verdict':'CONFIRMED conditional candidate017 two-endpoint seven-cell exclusion in FW-T-DYADIC-Y-v1, with all exact inverse, origin, realization, input hyperplane, canonical velocity, partition, plateau and absorption hypotheses retained. Independent exact raw origin and finite energy/cell replay; no full upper norm, profile nonexistence or existence closure.'}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],'CHECKS',len(checks),'SECONDS',result['elapsed_seconds'],'SHA',sha(B/'verification/result.json'))
 print('origin',result['a0_ball'],'contributors',touched,terms,'minimum ratio',floor)
if __name__=='__main__':main()
