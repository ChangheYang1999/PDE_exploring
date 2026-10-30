"""Candidate014 complete Cartesian M/C weak test with factored K."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,sys,time
from flint import arb,ctx,fmpq as Q
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/successor_factored_weak'
NAME='C1-N1-014-pairB-from007';RAW='8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746'
sys.set_int_max_str_digits(0)
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
L=module('n4_successor_two_endpoints',ROOT/'research/large_index_weak/code/check.py')
F=L.F;W=F.W;T,U,ar,ap,Radial=F.T,F.U,F.ar,F.ap,F.Radial
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();ctx.prec=2048;n,K=21,522
 src=ROOT/f'research/candidate_audits/data/{NAME}/canonical.json'
 auditpath=ROOT/f'research/candidate_audits/verification/{NAME}.json';audit=json.loads(auditpath.read_text())
 assert audit['generator_sha256']==RAW and H(src)==audit['canonical_sha256']
 assert audit['all_forbidden_zero'] and audit['B0n_exact'] and all(audit['snapshot_hashes_confirmed'].values())
 assert audit['c_equal_state131'] and audit['leading_density_equal_state131']
 model=Radial(src);assert model.state['source_sha256']==RAW and model.c==Q('4076476460239181/2251799813685248')
 oldpath=ROOT/'research/factored_monomial_audit/verification/result.json';old=json.loads(oldpath.read_text())
 fixture=ROOT/'research/factored_monomial_audit/source/T4_result.json';peer=json.loads(fixture.read_text())
 assert old['inputs'][str(fixture.relative_to(ROOT))]==H(fixture)
 assert old['n']==peer['angular_mode']==n and old['K']==peer['radial_power']==K
 assert all(old['peer_comparisons'].values()) and old['both_strict_floors_verified']
 bound,sup=F.supremum(K,n,peer['sup_certificate'])
 assert bound==Q('4156114212970569/100000000000000000000')
 small=F.construct(model,7,3);ordinary=W.helper.construct(model,T**3,7)
 calibration=[{key:P*T**3 for key,P in field.items()}==other for field,other in zip(small,ordinary,strict=True)]
 assert all(calibration)
 fields=F.construct(model,n,K);points=F.point_checks(model,fields,n,K)
 print('FIELDS',NAME,len(fields[0]),'seconds',time.monotonic()-start,flush=True)
 M2,M2t,mc=L.energy(fields[:1],model.delta,K)
 C2,C2t,cc=L.energy(fields[1:],model.delta,K)
 print('ENERGIES',M2.str(24),C2.str(24),'seconds',time.monotonic()-start,flush=True)
 Ip,parts_pairs=F.parts(model,fields[0],K);projection,counts=W.project(model,n)
 prepared=[(ell,ell*model.delta/2,P,P(U)) for ell,P in sorted(projection.items())]
 I,It,branches=L.PAIR.whole(prepared,K)
 assert I.overlaps(Ip) and min(I.rel_accuracy_bits(),It.rel_accuracy_bits(),Ip.rel_accuracy_bits())>150
 M,C=M2.sqrt(),C2.sqrt();D=M+C;radius=2*abs(I)/(D+(D*D+4*ar(bound)*abs(I)).sqrt())
 floor=Q(int(float(radius)*10**15)-1,10**15);assert floor>0 and ar(floor)<radius
 vals={'pairing':I,'pairing_t_endpoint':It,'pairing_by_parts':Ip,'M2':M2,'M2_t_endpoint':M2t,'C2':C2,'C2_t_endpoint':C2t,'M':M,'C':C,'D':D,'radius':radius}
 paths=[src,auditpath,Path(__file__),BASE/'PROOF.md',oldpath,fixture,
 ROOT/'research/factored_monomial_audit/code/check.py',ROOT/'research/factored_monomial_audit/PROOF.md',
 ROOT/'research/large_index_weak/code/check.py',ROOT/'research/large_index_weak/PROOF.md',
 ROOT/'research/far_pairing_audit/code/check_v2.py',ROOT/'research/successor_weak_probes/code/check.py',
 ROOT/'research/angular_probe_audit/code/check.py',ROOT/'research/optimized_probe_audit/code/check.py',
 ROOT/'research/localized_weak_probe/code/evaluate.py',ROOT/'research/localized_weak_probe/code/beta_scale.py',
 ROOT/'research/radial_fourier/code/radial.py',ROOT/'research/projected_residual/code/build.py',
 ROOT/'research/whole_plane_norms/code/pipeline.py']
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':NAME,'n':n,'K':K,'precision_bits':ctx.prec,
 'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},'raw_sha256':RAW,'canonical_sha256':H(src),
 'factored_K3_n7_exact_calibration':calibration,'point_checks':points,
 'field_sha256':[W.poly_hash(f) for f in fields],'energy_M_checks':mc,'energy_C_checks':cc,
 'projection_sha256':W.poly_hash(projection),'projection_pairs':counts,'parts_pairs':parts_pairs,
 'direct_pairing_branches':branches,'direct_parts_overlap':True,**{k:v.str(100) for k,v in vals.items()},
 'H_upper_exact':str(bound),'gradient_certificate':sup,'strict_lower_exact':str(floor),'strict_floor_verified':True,
 'probe_was_in_candidate014_optimization':True,'whole_plane':True,'all_background_modes_retained':True,
 'elapsed_seconds':time.monotonic()-start,'verdict':'OPEN independent candidate-level review; necessary distance under PROOF hypotheses'}
 with (BASE/f'verification/{NAME}_n021_K00522.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',NAME,'radius',radius.str(35),'floor',floor,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
