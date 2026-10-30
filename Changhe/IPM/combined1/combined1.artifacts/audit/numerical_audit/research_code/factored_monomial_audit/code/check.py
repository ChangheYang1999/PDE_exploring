"""Independent Cartesian factored high-angular whole-plane weak audit."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_poly,acb,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/factored_monomial_audit';SRC=BASE/'source'
sys.set_int_max_str_digits(0)
spec=importlib.util.spec_from_file_location('n4_successor_factored',ROOT/'research/successor_weak_probes/code/check.py')
W=importlib.util.module_from_spec(spec);spec.loader.exec_module(W)
T,U,ap,ar,Radial,pshift,integral=W.T,W.U,W.ap,W.ar,W.Radial,W.pshift,W.integral
put=W.helper.put
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
NAME='C1-N1-013-pairU-from007'

def construct(model,n,K):
 radial=(2*K+1)-(2*K+4)*T
 px=[(n+1,(radial-n)/2),(n-1,(radial+n)/2)]
 py=[(n-1,(radial+n)/2),(n+1,(n-radial)/2)]
 M,Cx,Cy={},{},{};put(M,0,'s',n,(2*model.c+1)+model.c*radial)
 for (j,l),A in model.u1.items():
  for freq,B in px:
   G=pshift(A,2)*B/2;put(M,j+1,'s',freq+l,G);put(M,j+1,'s',freq-l,G)
 for (j,l),A in model.u2.items():
  for freq,B in py:
   G=pshift(A,2)*B/2;put(M,j+1,'s',l+freq,G);put(M,j+1,'s',l-freq,G)
 for (j,l),A in model.rx.items():
  G=pshift(A,2)/2;put(Cx,j+1,'c',n-l,G);put(Cx,j+1,'c',n+l,-G)
 for (j,l),A in model.ry.items():
  G=pshift(A,2)/2;put(Cy,j+1,'s',n+l,G);put(Cy,j+1,'s',n-l,G)
 return [{k:p for k,p in f.items() if p} for f in [M,Cx,Cy]]

def energy(fields,delta,K):
 groups={};count=0
 for field in fields:
  bymode={}
  for (ell,kind,n),P in field.items():
   assert n>0 and n%2
   bymode.setdefault((kind,n),[]).append((ell,ap(P(U))))
  for rows in bymode.values():
   for i,(ell,P) in enumerate(rows):
    for j in range(i,len(rows)):
     ell2,Qp=rows[j];key=ell+ell2
     groups[key]=groups.get(key,arb_poly([]))+P*Qp*(1 if i==j else 2);count+=1
 vals=[integral(P,1+ell*delta/2,2*K+1) for ell,P in sorted(groups.items())]
 answer=arb.pi()/2*sum(vals,arb(0));assert answer>0 and answer.rel_accuracy_bits()>150
 return answer,count,len(groups)

def parts(model,Mfield,K):
 rho={}
 for (j,n),P in model.rho.items():rho.setdefault(n,[]).append((j+1,ap(pshift(P,2)(U))))
 groups={};count=0
 for (ell,kind,n),P in Mfield.items():
  assert kind=='s';PP=ap(P(U))
  for ell2,R in rho.get(n,[]):
   key=ell+ell2;groups[key]=groups.get(key,arb_poly([]))+PP*R;count+=1
 return -arb.pi()/2*sum((integral(P,ell*model.delta/2-1,K+1) for ell,P in groups.items()),arb(0)),count

def point_checks(model,fields,n,K):
 out=[]
 for xs,ys in [('1/2','1/2'),('3','4'),('60','80')]:
  x,y=ar(Q(xs)),ar(Q(ys));r2=x*x+y*y;r=r2.sqrt();t=r2/(1+r2);v=1/(1+r2);z=acb(x/r,y/r)**n
  vals=model.evaluate(xs,ys);factor=t**K
  radial=(2*K+1)-(2*K+4)*t;pr=v*v*factor*radial*z.imag;pt=n*v*v*factor*z.real
  px,py=x/r*pr-y/r*pt,y/r*pr+x/r*pt;phi=r*v*v*factor*z.imag
  expected=[(2*ar(model.c)+1)*phi+(ar(model.c)*x+vals['u1'])*px+(ar(model.c)*y+vals['u2'])*py,phi*vals['rho_x'],phi*vals['rho_y']]
  checks=[(W.helper.evaluate(f,model,x,y)*factor).overlaps(e) for f,e in zip(fields,expected,strict=True)]
  assert all(checks);out.append({'x':xs,'y':ys,'M_Cx_Cy':checks})
 return out

def supremum(K,n,peer):
 v=Poly([0,1]);B=2*K+4;q=v*v*(-3+B*v)
 equation=(1-v)*q.derivative()-K*q
 numerator=Poly([-6,9*K+18,-B*(K+3)])
 assert equation==v*numerator
 disc=(9*K+18)**2-24*B*(K+3);assert disc>0
 root=arb(disc).sqrt();rr=[((9*K+18)-root)/(2*B*(K+3)),((9*K+18)+root)/(2*B*(K+3))]
 assert all(0<x and x<1 for x in rr)
 radial=[abs(x*x*(1-x)**K*(-3+B*x)) for x in rr]
 x=ar(Q(2,K+2));angular=n*x*x*(1-x)**K
 caps=radial+[angular];bound=Q(peer['H_upper_exact'])
 assert all(x<ar(bound) for x in caps)
 assert all(rr[i].overlaps(1-arb(peer['roots'][1-i])) for i in range(2))
 assert all(radial[i].overlaps(arb(peer['amplitude_caps'][1-i])) for i in range(2))
 assert angular.overlaps(arb(peer['amplitude_caps'][2]))
 return bound,{'derivative_polynomial_exact':[str(x) for x in numerator],'discriminant':disc,'v_roots':[x.str(100) for x in rr],'amplitudes':[x.str(100) for x in caps],'exact_polynomial_identity':True,'peer_roots_and_amplitudes_overlap':True,'strict_H_verified':True}

def main():
 start=time.monotonic();ctx.prec=2048;n,K=21,522
 p=SRC/'T4_result.json';peer=json.loads(p.read_text());manifest=json.loads((SRC/'MANIFEST.json').read_text())
 assert all(H(SRC/name)==d['sha256'] for name,d in manifest['files'].items())
 for key,name in [('source_sha256','T4_canonical.json'),('build_sha256','T4_build.json'),('proof_sha256','T4_PROOF.md'),('code_sha256','T4_check.py'),('helper_sha256','T4_polar_helper.py'),('probe_sha256','T4_probe.json')]:assert peer[key]==H(SRC/name)
 assert peer['angular_mode']==n and peer['radial_power']==K and peer['direct_parts_overlap']
 canonical=ROOT/f'research/candidate_audits/data/{NAME}/canonical.json';auditpath=ROOT/f'research/candidate_audits/verification/{NAME}.json';audit=json.loads(auditpath.read_text());ours=json.loads(canonical.read_text());other=json.loads((SRC/'T4_canonical.json').read_text());build=json.loads((SRC/'T4_build.json').read_text())
 assert H(canonical)==audit['canonical_sha256'] and audit['all_forbidden_zero'] and audit['B0n_exact'] and all(audit['snapshot_hashes_confirmed'].values())
 assert other['source_sha256']==ours['source_sha256']==audit['generator_sha256']==build['source_sha256']
 maps=[{tuple(k):Q(a) for k,a in zip(d['order'],d['coefficients'],strict=True)} for d in [ours,other]]
 assert len(maps[0])==len(maps[1])==1922 and maps[0]==maps[1]
 assert Q(ours['cl'])==Q(other['cl']) and Q(ours['a0'])==Q(other['a0']) and Q(ours['strain'])==Q(other['strain'])
 bound,sup=supremum(K,n,peer['sup_certificate']);model=Radial(canonical)
 small=construct(model,7,3);ordinary=W.helper.construct(model,T**3,7)
 calibration=[{k:P*T**3 for k,P in f.items()}==g for f,g in zip(small,ordinary,strict=True)];assert all(calibration)
 fields=construct(model,n,K);points=point_checks(model,fields,n,K)
 print('FIELDS',len(fields[0]),'seconds',time.monotonic()-start,flush=True)
 M2,mpairs,mgroups=energy(fields[:1],model.delta,K);print('M complete',M2.str(24),'seconds',time.monotonic()-start,flush=True)
 C2,cpairs,cgroups=energy(fields[1:],model.delta,K);print('C complete',C2.str(24),'seconds',time.monotonic()-start,flush=True)
 Iparts,pcount=parts(model,fields[0],K);projection,counts=W.project(model,n)
 I=arb.pi()/2*sum((integral(ap(P(U)),ell*model.delta/2-1,K+1) for ell,P in projection.items()),arb(0))
 assert I.overlaps(Iparts) and min(I.rel_accuracy_bits(),Iparts.rel_accuracy_bits())>150
 M,C=M2.sqrt(),C2.sqrt();D=M+C;radius=2*abs(I)/(D+(D*D+4*ar(bound)*abs(I)).sqrt())
 vals={'pairing':I,'pairing_by_parts':Iparts,'normM2':M2,'normC2':C2,'M':M,'C':C,'D':D,'radius':radius}
 comparisons={key:val.overlaps(arb(peer[key])) for key,val in vals.items()};assert all(comparisons.values()),comparisons
 floor=Q(peer['strict_lower_exact']);assert ar(floor)<radius and ar(floor)<arb(peer['radius'])
 oldpath=ROOT/f'research/successor_monomial_probes/verification/{NAME}_n021_K00522.json';old=json.loads(oldpath.read_text())
 assert I.overlaps(arb(old['pairing'])) and D<arb(old['D_upper']) and bound<Q(old['H_upper_exact']) and radius>arb(old['L2_radius_lower'])
 paths=[Path(__file__),BASE/'PROOF.md',SRC/'MANIFEST.json',p,canonical,auditpath,oldpath,ROOT/'research/successor_weak_probes/code/check.py',ROOT/'research/angular_probe_audit/code/check.py',ROOT/'research/optimized_probe_audit/code/check.py',ROOT/'research/localized_weak_probe/code/beta_scale.py',ROOT/'research/radial_fourier/code/radial.py']
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':NAME,'n':n,'K':K,'bits':ctx.prec,'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},'raw_sha256':audit['generator_sha256'],'canonical_sha256':H(canonical),'independent_canonical_term_count':1922,'all_canonical_terms_equal':True,'factored_K3_n7_field_calibration':calibration,'point_checks':points,'field_hashes':[W.poly_hash(f) for f in fields],'M_pairs':mpairs,'C_pairs':cpairs,'M_groups':mgroups,'C_groups':cgroups,'parts_pairs':pcount,'projection_pairs':counts,'projection_sha256':W.poly_hash(projection),**{key:value.str(100) for key,value in vals.items()},'H_upper_exact':str(bound),'gradient_certificate':sup,'peer_comparisons':comparisons,'strict_lower_exact':str(floor),'both_strict_floors_verified':True,'weaker_N4_200_consistent':True,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED independent necessary L2 distance; exact framework hypotheses apply'}
 with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',out['utc'],'radius',radius.str(35),'floor',floor,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
