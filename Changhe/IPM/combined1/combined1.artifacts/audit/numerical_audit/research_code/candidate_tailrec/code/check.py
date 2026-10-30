"""Full nonintegrable profile and triangular recurrence audit from raw generators."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,importlib.util,json,sys,time
from flint import fmpq as Q
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/candidate_tailrec'
sys.set_int_max_str_digits(0)
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out
L=module('n4_candidate_laurent_tail',ROOT/'research/triangular_tail_audit/code/check.py')
A=module('n4_candidate_freeze_tail',ROOT/'research/generator_sector_audit/code/audit_candidate.py')
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def hashobject(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main(names):
 start=time.monotonic();profiles_path=ROOT/'research/triangular_tail_audit/verification/exact_profiles.json';profiles=json.loads(profiles_path.read_text())
 baseline_path=ROOT/'research/triangular_tail_audit/verification/result.json';baseline=json.loads(baseline_path.read_text());assert sha(profiles_path)==baseline['exact_profiles_sha256']
 for rel,digest in baseline['inputs'].items():assert sha(ROOT/rel)==digest
 expected_c=Q(profiles['c']);expected_gamma=Q(profiles['gamma']);assert Q(1,2)<expected_gamma<Q(3,5)
 cos={1:(Q(1,2),Q(0)),-1:(Q(1,2),Q(0))};sin={1:(Q(0),Q(-1,2)),-1:(Q(0),Q(1,2))}
 rows=[];allinputs={};referencepotential=None
 for name in names:
  tick=time.monotonic();directory,snapshots=A.copy_snapshot(name);manifest_path=directory/'MANIFEST.json';manifest=json.loads(manifest_path.read_text())
  assert manifest['id']==name and len(manifest['coefficient_files'])==1;entry=manifest['coefficient_files'][0];source=directory/entry['name'];assert sha(source)==entry['sha256']
  data=json.loads(source.read_text());c=A.rational(data.get('cl',data.get('cl_exact')));assert c==expected_c==Q(manifest['c_l_exact'])
  gamma,delta=1/c,1-1/c;exponents={j:gamma-j*delta for j in range(5)};assert exponents[3]>-1>exponents[4] and gamma-2<-1
  potential={};dropped=0;scales=set()
  for g in data['generators']:
   j,m=int(g['j']),int(g['m']);assert g['j']==j and g['m']==m and min(j,m)>=0
   w,n,q,R=A.spec_parts(g['spec']);assert min(w,n,q)>=0 and R>0;scales.add(str(R));coefficient=A.rational(g['coef'])
   if j<=3 and q==0:potential[j,m]=potential.get((j,m),Q(0))+coefficient
   else:dropped+=1
  potential={k:q for k,q in potential.items() if q};ordered=sorted(potential)
  state={'cl':str(c),'order':[[j,m,m] for j,m in ordered],'coefficients':[str(potential[k]) for k in ordered]}
  model=L.Radial(state);fields={};branches=[];same_all=True;differences={}
  for j in range(4):
   e=exponents[j];rho=L.endpoint(model.rho,j,'s');psi=L.endpoint(model.deriv(1,1),j,'s')
   u1,u2=L.endpoint(model.u1,j,'c'),L.endpoint(model.u2,j,'s');rx,ry=L.endpoint(model.rx,j,'s'),L.endpoint(model.ry,j,'c')
   radial=L.add(L.multiply(cos,u1),L.multiply(sin,u2));angular=L.add(L.scale(L.multiply(sin,u1),-1),L.multiply(cos,u2))
   assert radial==L.scale(L.derivative(psi),-1) and angular==L.scale(psi,e+1)
   assert rx==L.add(L.scale(L.multiply(cos,rho),e),L.scale(L.multiply(sin,L.derivative(rho)),-1))
   assert ry==L.add(L.scale(L.multiply(sin,rho),e),L.multiply(cos,L.derivative(rho)))
   lap={n:(x*((e+1)**2-n*n),y*((e+1)**2-n*n)) for n,(x,y) in psi.items()};lap={n:z for n,z in lap.items() if z!=L.ZERO};assert lap==L.scale(rx,-1)
   ownrho,ownpsi=L.sine_map(rho),L.sine_map(psi);sameR=ownrho==profiles['density_profiles'][str(j)];sameS=ownpsi==profiles['stream_profiles'][str(j)]
   endpoints={k:L.emit(v) for k,v in dict(u1=u1,u2=u2,rx=rx,ry=ry).items()};sameE=endpoints==profiles['Cartesian_endpoint_profiles'][str(j)]
   if not (sameR and sameS and sameE):differences[str(j)]={'density':ownrho,'stream':ownpsi,'Cartesian_endpoint_profiles':endpoints}
   same_all &= sameR and sameS and sameE
   fields[j]=dict(rho=rho,psi=psi,u1=u1,u2=u2,rx=rx,ry=ry,radial=radial,angular=angular)
   branches.append({'j':j,'e':str(e),'all_polar_Cartesian_and_Poisson_identities':True,'density_modes':len(ownrho),'stream_modes':len(ownpsi),'density_equal007':sameR,'stream_equal007':sameS,'all_four_Cartesian_profiles_equal007':sameE,'density_sha256':hashobject(ownrho),'stream_sha256':hashobject(ownpsi)})
  recurrences=[];zero=True
  for j in range(1,4):
   direct,polar={},{}
   for ell in range(j):
    m=j-1-ell;a,b=fields[ell],fields[m]
    direct=L.add(direct,L.multiply(a['u1'],b['rx']),L.multiply(a['u2'],b['ry']))
    polar=L.add(polar,L.scale(L.multiply(a['radial'],b['rho']),exponents[m]),L.multiply(a['angular'],L.derivative(b['rho'])))
   assert direct==polar;residual=L.add(direct,L.scale(fields[j]['rho'],-j*(c-1)));zero &= not residual
   frequencies=sorted(n for n in set(direct)|set(fields[j]['rho']) if n>0)
   if same_all:assert frequencies==list(range(1,20*(j+1),2))
   recurrences.append({'j':j,'all_Cartesian_polar_products_equal':True,'coefficient_count':len(frequencies),'maximum_frequency':max(frequencies,default=0),'all_exact_zero':not residual,'nonzero_residual_Laurent_coefficients':L.emit(residual)})
  if name=='C1-N1-007-d2w-j7-e2bal':assert same_all and zero;referencepotential=hashobject(state)
  paths=[source,manifest_path,directory/'SHA256SUMS']
  allinputs.update({str(p.relative_to(ROOT)):sha(p) for p in paths})
  row={'candidate':name,'raw_sha256':sha(source),'manifest_sha256':sha(manifest_path),'snapshot_hashes':snapshots,'chart':manifest.get('chart'),'scales':sorted(scales),'source_generator_count':len(data['generators']),'discarded_from_nonintegrable_prefix':dropped,'exact_leading_potential_surrogate_sha256':hashobject(state),'surrogate_term_count':len(ordered),'branches':branches,'recurrences':recurrences,'complete_Theta0_to3_Psi0_to3_equal007':same_all,'all_triangular_recurrence_coefficients_zero':zero,'total_recurrence_coefficient_count':sum(r['coefficient_count'] for r in recurrences),'differing_profiles':differences,'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED exact NC-T-TAILREC algebra and full-profile agreement with007' if same_all and zero else 'REFUTED agreement or recurrence; inspect complete exact difference maps'}
  rows.append(row);print(name,'MATCH007',same_all,'TAILREC',zero,'COUNT',row['total_recurrence_coefficient_count'],'SECONDS',row['elapsed_seconds'],flush=True)
 inputs=[Path(__file__),BASE/'PROOF.md',profiles_path,baseline_path,ROOT/'research/triangular_tail_audit/PROOF.md',ROOT/'research/triangular_tail_audit/code/check.py',ROOT/'research/radial_fourier/code/radial.py',ROOT/'research/generator_sector_audit/code/audit_candidate.py',ROOT/'research/generator_sector_audit/code/direct.py',ROOT/'research/multiscale_generators/code/cartesian.py']
 allinputs.update({str(p.relative_to(ROOT)):sha(p) for p in inputs})
 theory=ROOT.parent/'c1-shared/theory_requirements/theory_v04.md';assert sha(theory)=='7638b0dae2e1cd03bd307fec28143ce84ae37b5a42a0d882d64e879094fcca93'
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':allinputs,'theory_v04_sha256':sha(theory),'c_exact':str(expected_c),'leading_profile_source_sha256':sha(profiles_path),'rows':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Independent exact finite nonintegrable prefix only; no remainder, inverse, or existence; passing rows prove NC-T-TAILREC algebra under the separate theory chart interpretation.'}
 with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',out['utc'],'SECONDS',out['elapsed_seconds'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidate',nargs='+');main(p.parse_args().candidate)
