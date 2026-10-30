"""Full candidate007 weak norms with scalar, unexpanded large K."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, importlib.util, json, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, arb_poly, ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/large_index_weak'
NAME='C1-N1-007-d2w-j7-e2bal'
sys.set_int_max_str_digits(0)
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
F=module('n4_factored_largeK',ROOT/'research/factored_monomial_audit/code/check.py')
PAIR=module('n4_direct_largeK',ROOT/'research/far_pairing_audit/code/check_v2.py')
ENV=module('n4_envelope_largeK',ROOT/'research/localized_weak_probe/code/evaluate.py')
T,U,ap,ar,Radial=F.T,F.U,F.ap,F.ar,F.Radial
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def new(path,record):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('x') as out:json.dump(record,out,indent=2);out.write('\n')
def both_integrals(Pt,Pv,b,m):
 assert b>-1 and m>=0
 start=ar(b+1).gamma()*arb(m+1).gamma()/ar(b+m+2).gamma()
 vt=arb(0);tt=arb(0);vm=start;tm=start
 for j,p in enumerate(Pv):
  vt+=p*vm;vm*=ar((b+j+1)/(b+m+j+2))
 for j,p in enumerate(Pt):
  tt+=p*tm;tm*=ar(Q(m+j+1)/(b+m+j+2))
 assert vt.overlaps(tt)
 return vt,tt

def energy(fields,delta,K):
 groups={};pairs=0
 for field in fields:
  bymode={}
  for (ell,kind,n),P in field.items():
   assert n>0 and n%2
   bymode.setdefault((kind,n),[]).append((ell,ap(P),ap(P(U))))
  for rows in bymode.values():
   for i,(ell,Pt,Pv) in enumerate(rows):
    for j in range(i,len(rows)):
     ell2,Qt,Qv=rows[j];key=ell+ell2;mult=1 if i==j else 2
     At,Av=groups.get(key,(arb_poly([]),arb_poly([])))
     groups[key]=At+mult*Pt*Qt,Av+mult*Pv*Qv;pairs+=1
 vt=arb(0);tt=arb(0);checks=[]
 for ell,(Pt,Pv) in sorted(groups.items()):
  v,t=both_integrals(Pt,Pv,1+ell*delta/2,2*K+1)
  vt+=v;tt+=t
  checks.append({'ell_sum':ell,'degree':Pt.degree(),'endpoint_overlap':True})
 vt*=arb.pi()/2;tt*=arb.pi()/2
 assert vt>0 and tt>0 and vt.overlaps(tt)
 assert min(vt.rel_accuracy_bits(),tt.rel_accuracy_bits())>150
 return vt,tt,{'pairs':pairs,'groups':checks,'relative_accuracy_bits':[vt.rel_accuracy_bits(),tt.rel_accuracy_bits()]}

def maximum(K):
 assert K>=1
 v=Poly([0,1]);B=2*K+4
 P=v*v*(-3+B*v)
 critical=Poly([-6,9*K+18,-B*(K+3)])
 assert (1-v)*P.derivative()-K*P==v*critical
 disc=(9*K+18)**2-24*B*(K+3)
 assert disc==3*(K+2)*(11*K+6)>0
 root=arb(disc).sqrt()
 roots=[((9*K+18)-root)/(2*B*(K+3)),((9*K+18)+root)/(2*B*(K+3))]
 assert all(0<x and x<1 for x in roots)
 amplitudes=[abs(x*x*(1-x)**K*(-3+B*x)) for x in roots]
 x=ar(Q(2,K+2));amplitudes.append(x*x*(1-x)**K)
 bound=Q(2,K*K)
 assert all(value<ar(bound) for value in amplitudes)
 return bound,{'derivative_polynomial_exact':[str(x) for x in critical],
  'discriminant':disc,'v_roots':[x.str(100) for x in roots],
  'angular_critical_exact':str(Q(2,K+2)),
  'amplitude_caps':[x.str(100) for x in amplitudes],
  'endpoint_amplitudes_exact':['0','0'],'H_upper_exact':str(bound),
  'all_critical_amplitudes_strictly_below_H':True,'polynomial_identity_exact':True}

def envelopes(model,bg,cg,K):
 weight=arb_poly([5,2*K-4])
 B2=arb.pi()/2*sum((F.integral(P*weight*weight,b,2*K+1) for b,P in bg.items()),arb(0))
 C2=arb.pi()/2*sum((F.integral(P,b,2*K+1) for b,P in cg.items()),arb(0))
 a=Q(2*K+2);L0=3*model.c+1+2*model.c*K;L1=2*model.c*(K+2)
 rational=(L0*L0-2*L0*L1*a/(a+2)+L1*L1*a*(a+1)/((a+2)*(a+3)))/(a*(a+1))
 A2=arb.pi()/2*ar(rational)
 assert all(x>0 and x.rel_accuracy_bits()>150 for x in [A2,B2,C2])
 return {'A':A2.sqrt(),'Benv':B2.sqrt(),'Cenv':C2.sqrt(),
  'A2':A2,'Benv2':B2,'Cenv2':C2}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--K',type=int,nargs='+',default=[1024,100000,1000000,3000000,10000000,10000000000])
 args=parser.parse_args();ks=sorted(set(args.K));assert ks and min(ks)>=1024
 start=time.monotonic();ctx.prec=2048
 src=ROOT/f'research/candidate_audits/data/{NAME}/canonical.json'
 auditpath=ROOT/f'research/candidate_audits/verification/{NAME}.json'
 audit=json.loads(auditpath.read_text())
 assert H(src)==audit['canonical_sha256'] and audit['all_forbidden_zero'] and audit['B0n_exact'] and all(audit['snapshot_hashes_confirmed'].values())
 model=Radial(src);assert model.c>1 and model.state['source_sha256']==audit['generator_sha256']
 projection,metadata=PAIR.read_projection(NAME);ppath=PAIR.destination(NAME)
 previouspath=ROOT/'research/far_pairing_audit/verification/result.json'
 previous=json.loads(previouspath.read_text())
 assert previous['inputs'][str(ppath.relative_to(ROOT))]==H(ppath)
 assert previous['inputs'][str(src.relative_to(ROOT))]==H(src)
 assert previous['projection_full_comparison_report_bound'] and previous['complete_projected_branches']==len(projection)==16
 previousrows={r['K']:r for r in previous['rows']}
 prepared=[(ell,ell*model.delta/2,P,P(U)) for ell,P in sorted(projection.items())]
 smallpath=ROOT/f'research/projected_residual/verification/{NAME}_probe_2048.json'
 small=json.loads(smallpath.read_text());smallrows={r['k']:r for r in small['probes']}
 assert small['source_sha256']==H(src) and small['projection_sha256']==H(ppath)
 n1path=ROOT/'research/far_pairing_audit/source/N1_007_far_weak.json'
 n1=json.loads(n1path.read_text());assert n1['sha256']==audit['generator_sha256']
 n1rows={r['k']:r for r in n1['rows']}
 paths=[Path(__file__),BASE/'PROOF.md',BASE/'source/N1_weak_tests2.py',src,auditpath,ppath,previouspath,smallpath,n1path,
 ROOT/'research/factored_monomial_audit/code/check.py',ROOT/'research/factored_monomial_audit/PROOF.md',
 ROOT/'research/factored_monomial_audit/verification/result.json',ROOT/'research/far_pairing_audit/code/check_v2.py',
 ROOT/'research/successor_weak_probes/code/check.py',ROOT/'research/angular_probe_audit/code/check.py',
 ROOT/'research/optimized_probe_audit/code/check.py',ROOT/'research/localized_weak_probe/code/evaluate.py',
 ROOT/'research/localized_weak_probe/code/beta_scale.py',ROOT/'research/radial_fourier/code/radial.py',
 ROOT/'research/projected_residual/code/build.py',ROOT/'research/whole_plane_norms/code/pipeline.py']
 manifest={'candidate':NAME,'K_list':ks,'precision_bits':ctx.prec,'n':1,
 'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},'raw_sha256':audit['generator_sha256'],'canonical_sha256':H(src)}
 mp=BASE/'verification/manifest.json'
 if mp.exists():assert json.loads(mp.read_text())==manifest
 else:new(mp,manifest)
 mh=H(mp)
 smallfields=F.construct(model,1,3);ordinary=F.W.helper.construct(model,T**3,1)
 calibration=[{k:P*T**3 for k,P in field.items()}==other for field,other in zip(smallfields,ordinary,strict=True)]
 assert all(calibration)
 bg=ENV.groups(model,['u1','u2']);cg=ENV.groups(model,['rho_x','rho_y'])
 print('PREPARED','groups',len(bg),len(cg),'seconds',time.monotonic()-start,flush=True)
 records=[]
 for K in ks:
  dest=BASE/f'verification/K_{K:012d}.json'
  if dest.exists():
   saved=json.loads(dest.read_text());assert saved['manifest_sha256']==mh and saved['K']==K
   records.append({'K':K,'path':str(dest.relative_to(ROOT)),'sha256':H(dest)});continue
  tick=time.monotonic();fields=F.construct(model,1,K);points=F.point_checks(model,fields,1,K)
  M2,M2t,mc=energy(fields[:1],model.delta,K);C2,C2t,cc=energy(fields[1:],model.delta,K)
  Iparts,parts_count=F.parts(model,fields[0],K)
  I,It,branches=PAIR.whole(prepared,K)
  assert I.overlaps(Iparts) and Iparts.rel_accuracy_bits()>150
  refs={}
  if K in previousrows:
   old=previousrows[K];refs['far_pairing_v']=I.overlaps(arb(old['I_v_endpoint']));refs['far_pairing_t']=I.overlaps(arb(old['I_t_endpoint']))
  env=envelopes(model,bg,cg,K)
  if K in smallrows:
   old=smallrows[K]
   for key,previouskey in [('A','A'),('Benv','B_weighted'),('Cenv','C')]:refs['small_'+key]=env[key].overlaps(arb(old[previouskey]))
   refs['small_pairing']=I.overlaps(arb(old['pairing']))
  assert all(refs.values())
  M,C=M2.sqrt(),C2.sqrt();D=M+C;bound,sup=maximum(K)
  assert M<env['A']+env['Benv'] and C<env['Cenv']
  radius=2*abs(I)/(D+(D*D+4*ar(bound)*abs(I)).sqrt())
  floor=Q(int(float(radius)*10**18)-1,10**18);assert floor>0 and ar(floor)<radius
  comparisons={}
  if K in n1rows:
   old=n1rows[K]
   for key,peerkey in [('Benv','B_k_est'),('Cenv','C_k_est')]:
    fp=ar(Q(*float(old[peerkey]).as_integer_ratio()))
    comparisons[key]={'FLOAT_estimate':old[peerkey],
     'absolute_relative_error':(abs(fp-env[key])/env[key]).str(100),
     'estimate_over_full':(fp/env[key]).str(100)}
  vals={'pairing':I,'pairing_t_endpoint':It,'pairing_by_parts':Iparts,
   'M2':M2,'M2_t_endpoint':M2t,'C2':C2,'C2_t_endpoint':C2t,'M':M,'C':C,'D':D,'radius':radius,**env}
  out={'utc':now(),'candidate':NAME,'n':1,'K':K,'manifest_sha256':mh,'precision_bits':ctx.prec,
   'factored_K3_n1_exact_calibration':calibration,'point_checks':points,
   'field_sha256':[F.W.poly_hash(f) for f in fields],
   'energy_M_checks':mc,'energy_C_checks':cc,'direct_pairing_branches':branches,
   'parts_pairs':parts_count,'direct_parts_overlap':True,'prior_calibrations':refs,
   **{key:value.str(100) for key,value in vals.items()},'H_upper_exact':str(bound),
   'gradient_certificate':sup,'strict_lower_exact':str(floor),'strict_floor_verified':True,
   'envelope_M_and_C_inequalities_verified':True,'N1_matching_envelope_comparisons':comparisons,
   'elapsed_seconds':time.monotonic()-tick,'verdict':'OPEN independent candidate-level review; conditional necessary L2 distance only'}
  new(dest,out);records.append({'K':K,'path':str(dest.relative_to(ROOT)),'sha256':H(dest)})
  print('K',K,'I',I.str(20),'M',M.str(20),'C',C.str(20),'radius',radius.str(25),'seconds',out['elapsed_seconds'],flush=True)
 new(BASE/'verification/result.json',{'utc':now(),'candidate':NAME,'manifest_sha256':mh,'rows':records,'elapsed_seconds':time.monotonic()-start,'complete':True,'verdict':'OPEN independent peer'})
 print('DONE',now(),'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
