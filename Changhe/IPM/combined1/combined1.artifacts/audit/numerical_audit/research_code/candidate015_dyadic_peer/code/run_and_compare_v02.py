"""Source-bound own015 polynomial production and seven peer energy checks."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from types import ModuleType
import importlib.util,json,gzip,sys,time
from flint import arb,ctx,fmpq as Q
R=Path(__file__).resolve().parents[3];B=R/'research/candidate015_dyadic_peer';now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();sys.set_int_max_str_digits(0)
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def main():
 start=time.monotonic();ctx.prec=2048;target=B/'verification/result_v02.json';assert not target.exists();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or v==h,(str(p),v,h);inputs[str(p.relative_to(R))]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 m=read(B/'source/MANIFEST.json');bind(B/'PROOF.md',m['proof_sha256']);bind(Path(__file__));assert m['proof_written_before_code']
 for name,z in m['files'].items():
  p=bind(B/'source'/name,z['stored_sha256']);data=gzip.decompress(p.read_bytes()) if z['encoding']=='gzip' else p.read_bytes();assert sha256(data).hexdigest()==z['original_sha256']
 peer=json.loads(gzip.decompress((B/'source/N3_wlap_modes.json.gz').read_bytes()));assert peer['code_sha256']==m['files']['N3_wlap_modes.py']['original_sha256']
 name='C1-N1-015-pairQ-quot013';src=R/f'research/candidate_audits/data/{name}/canonical.json';audit=read(R/f'research/candidate_audits/verification/{name}.json');bind(src,audit['canonical_sha256']);assert peer['id']==name and peer['only_modes']==[1,3]
 bind(B/'SERIALIZATION_PROOF_v02.md');canonical=read(src);pairs=[(tuple(k),Q(v)) for k,v in zip(canonical['order'],canonical['coefficients'],strict=True)];assert len(set(k for k,v in pairs))==len(pairs) and all(v for k,v in pairs)
 serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(pairs))+'\n';sh=sha256(serial.encode()).hexdigest();assert sh==canonical['canonical_serialization_sha256']==peer['canonical_sha256'];checks['canonical_serialization_recomputed']=True
 entry=bind(R/m['own_entry'],m['own_entry_sha256']);spec=importlib.util.spec_from_file_location('own015_dyadic_entry',entry);C=importlib.util.module_from_spec(spec);spec.loader.exec_module(C)
 todo=[C]+list(sys.modules.values());seen=set();edges=[]
 while todo:
  mod=todo.pop()
  if not isinstance(mod,ModuleType) or id(mod) in seen:continue
  seen.add(id(mod));p=getattr(mod,'__file__',None)
  if not p:continue
  p=Path(p).resolve()
  if not p.is_relative_to(R) or p.suffix!='.py':continue
  bind(p)
  for key,value in vars(mod).items():
   if isinstance(value,ModuleType):
    todo.append(value);vp=getattr(value,'__file__',None)
    if vp and Path(vp).resolve().is_relative_to(R):edges.append({'from':str(p.relative_to(R)),'name':key,'to':str(Path(vp).resolve().relative_to(R))})
 expected=['research/successor_dyadic_probes/code/check.py','research/successor_weak_probes/code/check.py','research/whole_plane_norms/code/norms.py','research/radial_fourier/code/radial.py']
 assert all(p in inputs for p in expected)
 before={'utc':now(),'candidate':name,'inputs':dict(inputs),'module_edges':edges,'peer_code_executed':False,'production_arguments':[name,[1,3]],'before_integrations':True}
 save(B/'verification/BOUND_START_v02.json',before);print(now(),'BOUND_START',len(inputs),flush=True)
 ownbase=R/f'research/successor_dyadic_probes/verification/{name}'
 if not (ownbase/'result.json').exists():C.run(name,[1,3])
 own=read(ownbase/'result.json');manifest=read(ownbase/'manifest.json',own['manifest_sha256'])
 for p,h in manifest['inputs'].items():bind(R/p,h)
 assert own['candidate']==name and own['selected_modes']==[1,3] and own['all_seven_excluded'] and not own['complete_upper_norm']
 records={n:read(ownbase/f'mode_{n:03d}.json',own['mode_result_sha256'][str(n)]) for n in [1,3]}
 checks['own_exact_derivatives_and_endpoints']=all(z['exact_Cartesian_polar_trace_equal'] and z['exact_mixed_derivatives_equal'] and len(z['weights'])==8 for z in records.values())
 def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
 weights=[Q(k,4) for k in range(1,8)];assert set(peer['per_a'])==set(map(str,weights));rows=[]
 for a in weights:
  pr=peer['per_a'][str(a)];assert [z['mode'] for z in pr['modes']]==[1,3]
  exact=[Q(z['N_a_mode_sq_over_pi_exact']) for z in pr['modes']];total=Q(pr['sq_over_pi_exact']);assert sum(exact,Q(0))==total and all(z>0 for z in exact)
  sums=arb(0);modechecks=[]
  for n,z in zip([1,3],exact,strict=True):
   ownrow=next(v for v in records[n]['weights'] if Q(v['a'])==a);energy=arb(ownrow['energy']);pe=arb.pi()*ar(z)
   assert energy.overlaps(pe) and ownrow['relative_accuracy_bits']>150
   modechecks.append({'mode':n,'own_energy':ownrow['energy'],'peer_exact_energy':pe.str(100),'overlap':True});sums+=energy
  pn=(arb.pi()*ar(total)).sqrt();on=sums.sqrt();assert pn.overlaps(on)
  assert arb(pr['N_a_LB']).lower()<pn.lower() and pn.upper()<arb(pr['N_a_UB']).upper()
  rows.append({'a':str(a),'mode_energy_comparisons':modechecks,'peer_exact_sum_verified':True,'own_sum_norm':on.str(100),'peer_exact_norm':pn.str(100),'peer_directed_endpoint_displays_valid':True})
 checks['all14_mode_and7_total_energy_comparisons']=True
 c=Q(4076476460239181,2251799813685248);star,H=C.maximum(c);A=1+1/c;points=[Q(k,4) for k in range(7)]+[A];cells=[]
 for i,(lo,hi) in enumerate(zip(points[:-1],points[1:])):
  a=hi if i<6 else Q(7,4);assert a>=hi;row=next(z for z in rows if Q(z['a'])==a);norm=arb(row['own_sum_norm']);lower=arb(5)**ar((lo-2)/2)*norm;upper=H*ar((1+c-c*lo)/(1+lo));gap=lower-upper;ratio=lower/upper;old=own['seven_cells'][i]
  assert gap>0 and old['excluded'] and Q(old['left'])==lo and Q(old['right'])==hi and Q(old['norm_evaluation_at'])==a
  for key,value in [('lower',lower),('upper',upper),('gap',gap),('ratio',ratio)]:assert arb(old[key]).overlaps(value)
  floor=Q(int((ratio.lower()*10**12).floor().unique_fmpz())-1,10**12);assert ar(floor)<ratio and ar(Q(old['strict_ratio_floor']))<ratio
  cells.append({'left':str(lo),'right':str(hi),'norm_evaluation_at':str(a),'ratio':ratio.str(100),'strict_ratio_floor':str(floor),'gap':gap.str(100),'excluded':True})
 checks['all_seven_complete_cells']=True
 checks['origin_conditions']=Q(own['a0_exact'])>=5*c-4 and Q(manifest['strain_exact'])==1-c
 checks['all_before_hashes_unchanged']=all(sha(R/p)==h for p,h in before['inputs'].items())
 assert all(checks.values())
 for p,h in inputs.items():assert sha(R/p)==h
 out={'utc':now(),'elapsed_seconds':time.monotonic()-start,'candidate':name,'canonical_sha256':sha(src),'raw_sha256':audit['generator_sha256'],'precision_bits':ctx.prec,'inputs':inputs,'checks':checks,'check_count':len(checks),'before_binding_sha256':sha(B/'verification/BOUND_START_v02.json'),'peer_source_files':m['files'],'weights':rows,'cells':cells,'minimum_strict_ratio_floor':str(min(Q(z['strict_ratio_floor']) for z in cells)),'peer_historical_F_cache_available':False,'peer_historical_import_versions_observed':False,'foreign_code_executed':False,'whole_plane_no_quadrature':True,'projection_modes':[1,3],'complete_upper_norm':False,'verdict':'CONFIRMED own complete two-mode whole-plane energies and all seven N3 exact-rational energy comparisons; conditional registered seven-cell scheme exclusion only under the full stated framework hypotheses; no inverse or existence conclusion'}
 save(target,out);print(now(),'PASS',len(checks),'checks',len(inputs),'inputs','result',sha(target),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
