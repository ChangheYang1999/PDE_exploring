"""Bind independent polar reconstruction and all40082 coefficient digests."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
import gzip,json,sys,time,importlib.util
R=Path(__file__).resolve().parents[3];B=R/'research/scaled_reconstruction_peer';P=R.parent/'c1-t4';sys.set_int_max_str_digits(0);ctx.prec=2048
spec=importlib.util.spec_from_file_location('own_binding303',R/'research/scaled_hessian_peer/code/check.py');H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();op=R/'research/scaled_background_cover/verification/C1-N1-017-legqs50-quot013_reconstruction.json';own=json.loads(op.read_text());poly=R/own['storage_path'];ap=R/'research/scaled_hessian_peer/verification/result.json';accepted=json.loads(ap.read_text());raw=R/'research/candidate_audits/data/C1-N1-017-legqs50-quot013/quot013_legqs50_m9to15_cpu_m16_exact.json';dp=R/'research/generator_sector_audit/verification/C1-N1-017-legqs50-quot013_direct.json';direct=json.loads(dp.read_text());paths=[B/'PROOF.md',Path(__file__),op,poly,ap,raw,dp,R/'research/scaled_hessian_peer/code/check.py']+[R/rel for rel in own['inputs']]+[R/rel for rel in accepted['own_inputs']]
 bind=H.Binding(B,paths)
 for rel,h in own['inputs'].items():bind.ownfile(R/rel,h)
 for rel,h in accepted['own_inputs'].items():bind.ownfile(R/rel,h)
 for rel,info in accepted['frozen_or_retained_sources'].items():bind.ownfile(R/rel,info['stored_sha256'])
 peer=bind.freeze(P/'research/scaled_background_reconstruction/verification/result.json','7c72008a0f4a67b9afd4764262055cfedb116b5e98bb818af5f60fc825e9ac03')
 for rel,h in peer['inputs'].items():bind.freeze(P/rel,h)
 checks={};checks['identity']=peer['raw_sha256']==sha(raw)==own['raw_sha256'] and peer['peer_polynomial_sha256']==sha(poly)==own['polynomial_sha256']
 checks['independent_comparison']=peer['all_exact_coefficients_equal'] and not peer['foreign_code_executed'] and not peer['complete_cover_claimed']
 checks['clearing_counts']=peer['exact_clearing_checks']==own['exact_clearing_checks']==728 and peer['polar_group_counts']=={'rx':360,'ry':368}
 checks['recurrence_counts']=peer['closed_chebyshev_recurrence_checks']==158
 checks['denominator_powers']=peer['denominator_powers']==[0,19] and own['denominator_powers']==[0,0,19,0] and peer['denominator_degree']==19
 with gzip.open(poly,'rt') as f:target=json.load(f)
 t=Poly([0,1]);D=(1+2499*(1-t))**19;checks['exact_denominator']=D==Poly([Q(x) for x in target['denominator']]) and D(1)==1
 checks['exact_parameters']=Q(target['c_exact'])==Q(own['c_exact'])==Q(4076476460239181,2251799813685248) and Q(target['delta'])==Q(own['delta'])==1-1/Q(own['c_exact'])
 counts={};digests={};origin={'rx':{},'ry':{}};maxi=0;maxk=0
 for key,rows in target['polynomials'].items():
  vals={(i,k):Q(v) for i,k,v in rows};assert len(vals)==len(rows) and all(vals.values());h=sha256()
  for (i,k),q in sorted(vals.items()):
   h.update(f'{i},{k}:{q}\n'.encode());maxi=max(maxi,i);maxk=max(maxk,k)
   if i==0:origin[key[:2]][k]=origin[key[:2]].get(k,Q(0))+q
  counts[key]=len(vals);digests[key]=h.hexdigest();checks[key+'_count']=counts[key]==peer['coefficient_counts'][key];checks[key+'_digest']=digests[key]==peer['coefficient_sha256'][key]
 checks['all_coefficient_maps']=set(counts)==set(peer['coefficient_counts'])==set(peer['coefficient_sha256']) and sum(counts.values())==40082==peer['nonzero_coefficients']==own['nonzero_coefficients']
 checks['degrees']=(maxi,maxk)==(103,80)==(peer['degree_t'],peer['degree_z'])==(own['degree_t'],own['degree_z'])
 for k,v in peer['origin'].items():checks['origin_'+k]=Q(v)==Q(direct['origin'][k]) and peer['origin_N4_checks'][k]
 checks['origin_normalization']=Q(peer['origin']['strain'])+Q(own['c_exact'])==1 and Q(peer['origin']['a0'])>0
 origin={key:{k:v for k,v in vals.items() if v} for key,vals in origin.items()};checks['origin_polynomial']=not origin['rx'] and origin['ry']=={0:Q(peer['origin']['a0'])*D(0)} and peer['origin_polynomial_checks'] and own['origin_checks']
 points=[];minimum=1000000
 for i,(pp,oo) in enumerate(zip(peer['point_checks'],own['point_checks'],strict=True)):
  checks[f'point{i}_coordinates']=Q(pp['x'])==Q(oo['x']) and Q(pp['y'])==Q(oo['y'])
  for label in ['rx','ry']:
   pr=pp['fields'][label];orr=oo['fields'][label];minimum=min(minimum,pr['bits']);checks[f'point{i}_{label}']=pr['peer_overlap'] and pr['bits']>150 and arb(pr['value']).overlaps(arb(orr['value']))
  points.append({'x':pp['x'],'y':pp['y'],'fields':pp['fields']})
 checks['point_count']=len(points)==3
 assert all(checks.values()),{k:v for k,v in checks.items() if not v};bind.finish()
 rec={'utc':datetime.now(timezone.utc).isoformat(),'candidate':own['candidate'],'raw_sha256':sha(raw),'checks':checks,'check_count':len(checks),'own_inputs':bind.own,'peer_bindings':bind.bindings,'retained_or_frozen':bind.frozen,'coefficient_counts':counts,'coefficient_sha256':digests,'nonzero_coefficient_count':sum(counts.values()),'point_checks':points,'minimum_peer_point_accuracy_bits':minimum,'peer_elapsed_seconds':peer['elapsed_seconds'],'foreign_code_executed':False,'verdict':'CONFIRMED N4-284 through independent T4-378; actual complete cover remains separate','elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(rec,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bind.bindings),'bindings',sum(counts.values()),'coefficients',sha(out),rec['utc'],'seconds',rec['elapsed_seconds'])
if __name__=='__main__':main()
