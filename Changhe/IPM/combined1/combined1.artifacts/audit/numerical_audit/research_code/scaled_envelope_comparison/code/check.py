"""Complete angular-envelope norms and matched frozen FLOAT comparisons."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, sys, time
from flint import arb, acb, fmpq as Q, ctx

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/scaled_envelope_comparison'
BACKEND=ROOT/'research/joint_scaled_factored_weak'
sys.path.insert(0,str(BACKEND/'code'))
from fields_joint import Rat, ScaledRadial, TR, ar, field_hash
import weak as W
sys.set_int_max_str_digits(0)
now=lambda:datetime.now(timezone.utc).isoformat()
def sha(p):
 h=sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def write(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def bind(d):
 for rel,digest in d.get('inputs',{}).items():assert sha(ROOT/rel)==digest,rel

def convert(model):
 return [(name,kind,{(j+1,n):A.divide_t(2) for (j,n),A in getattr(model,attr).items()})
         for name,kind,attr in [('u1','c','u1'),('u2','s','u2'),('rho_x','s','rx'),('rho_y','c','ry')]]

def square_groups(fields):
 groups={};count=0;zero_count=0
 for name,kind,field in fields:
  angular={}
  for (ell,n),A in field.items():
   assert n>=0 and not (n==0 and kind=='s')
   angular.setdefault(n,[]).append((ell,A))
  for n,terms in angular.items():
   weight=2 if n==0 else 1
   for i,(ell,A) in enumerate(terms):
    for j in range(i+1):
     ell2,B=terms[j];W.add(groups,ell+ell2,A*B*weight*(1 if i==j else 2))
     count+=1;zero_count+=int(n==0)
 return {k:A for k,A in groups.items() if A},count,zero_count

def fixtures():
 p,c,z=square_groups([('manufactured','c',{(1,0):Rat(2),(2,0):Rat(3)})])
 assert p=={2:Rat(8),3:Rat(24),4:Rat(18)} and c==3 and z==3
 rejected=False
 try:square_groups([('bad','s',{(1,0):Rat(1)})])
 except AssertionError:rejected=True
 assert rejected
 return {'constant_cosine_exact_weights':[8,24,18],'sine_zero_rejected':True}

def point_checks(model,fields):
 out=[]
 for xs,ys in [('1/10','73/100'),('3','4'),('60','80')]:
  x,y=ar(Q(xs)),ar(Q(ys));r=(x*x+y*y).sqrt();v=1/(1+r*r);t=1-v;z=acb(x/r,y/r)
  vals=model.evaluate(xs,ys);checks={}
  for name,kind,field in fields:
   total=sum((v**ar(ell*model.delta/2)*A.evaluate(t,v)*
     ((z**n).real if kind=='c' else (z**n).imag) for (ell,n),A in field.items()),arb(0))
   if name.startswith('u'):total*=r
   checks[name]=total.overlaps(vals[name]);assert checks[name],(name,xs,ys)
  out.append({'x':xs,'y':ys,'overlaps':checks})
 return out

def values(model,n,K,bg,cg):
 d=(2*K+1)-(2*K+4)*TR
 gg={ell:A*(d*d+n*n) for ell,A in bg.items()}
 b2,br=W.integrate_groups(gg,model.delta,Q(1),2*K+1,'B_envelope')
 c2,cr=W.integrate_groups(cg,model.delta,Q(1),2*K+1,'C_envelope')
 a=Q(2*K+2);l0=3*model.c+1+2*model.c*K;l1=2*model.c*(K+2)
 a2=arb.pi()/2*ar((l0*l0-2*l0*l1*a/(a+2)+l1*l1*a*(a+1)/((a+2)*(a+3)))/(a*(a+1)))
 assert all(x>0 and x.rel_accuracy_bits()>150 for x in [a2,b2,c2])
 A,B,C=a2.sqrt(),b2.sqrt(),c2.sqrt()
 return {'A':A,'Bbar':B,'Cbar':C,'Dbar':A+B+C},{'A2':a2.str(100),'Bbar2':b2.str(100),'Cbar2':c2.str(100),'B_moments':br,'C_moments':cr}

def common_inputs():
 ps=[Path(__file__),BASE/'PROOF.md',BASE/'source/MANIFEST.json',BACKEND/'PROOF.md',BACKEND/'code/fields_joint.py',BACKEND/'code/weak.py',
 ROOT/'research/factored_pole_moments/PROOF.md',ROOT/'research/factored_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/code/moments.py']
 for name in ['scalar_joint.json','fields.json','candidate013.json']:
  p=BACKEND/'verification'/name;d=json.loads(p.read_text());bind(d);ps.append(p)
 sources=json.loads((BASE/'source/MANIFEST.json').read_text())
 assert sources['proof_sha256']==sha(BASE/'PROOF.md') and sources['proof_checked_before_code']
 for name,entry in sources['sources'].items():
  p=BASE/'source'/name;assert sha(p)==entry['sha256'];ps.append(p)
 return ps

def calibrate(ps):
 start=time.monotonic();dest=BASE/'verification/calibration.json';assert not dest.exists()
 source=ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json'
 refp=ROOT/'research/angular_weak_probes/verification/n021_K00522.json';ref=json.loads(refp.read_text())
 mp=ROOT/'research/angular_weak_probes/verification/manifest.json';manifest=json.loads(mp.read_text())
 assert ref['manifest_sha256']==sha(mp);bind(manifest)
 model=ScaledRadial(source);fields=convert(model);pc=point_checks(model,fields)
 bg,bc,bz=square_groups(fields[:2]);cg,cc,cz=square_groups(fields[2:]);assert bz==0 and cz>0
 vals,records=values(model,21,522,bg,cg);checks={k:vals[k].overlaps(arb(ref[v])) for k,v in [('A','A'),('Bbar','B_upper'),('Cbar','C_upper'),('Dbar','D_upper')]};assert all(checks.values())
 K=522;h0=Q((2*K+1)*4*K**K,(K+2)**(K+2));assert h0==Q(ref['H_upper_exact'])
 I=arb(ref['pairing']);D=vals['Dbar'];radius=2*abs(I)/(D+(D*D+4*ar(h0)*abs(I)).sqrt());assert radius.overlaps(arb(ref['L2_radius_lower']))
 out={'utc':now(),'candidate':'C1-N1-007-d2w-j7-e2bal','n':21,'K':522,'fixtures':fixtures(),'point_checks':pc,'old_envelope_overlaps':checks,'old_radius_overlap':True,
 'values':{k:v.str(100) for k,v in vals.items()},'radius':radius.str(100),'groups':{'u':len(bg),'rho':len(cg)},'pair_counts':[bc,cc],'constant_cosine_pairs':cz,
 **records,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in ps+[source,refp,mp]},'elapsed_seconds':time.monotonic()-start,'status':'PASS own regression; scaled-candidate comparison remains OPEN'}
 write(dest,out);print('CALIBRATION_PASS',out['elapsed_seconds'],flush=True)
 return dest

def candidate(num,ps,cal):
 start=time.monotonic();name=f'C1-N1-{num:03d}-legqs{25 if num==16 else 50}-quot013'
 directory=ROOT/'research/candidate_audits/data'/name;mp=directory/'MANIFEST.json';manifest=json.loads(mp.read_text());assert manifest['id']==name
 entry=manifest['coefficient_files'][0];source=directory/entry['name'];assert sha(source)==entry['sha256']
 fp=BASE/f'source/candidate{num:03d}_float.json';floating=json.loads(fp.read_text());assert floating['sha256']==sha(source)
 model=ScaledRadial(source);fields=convert(model);pc=point_checks(model,fields)
 bg,bc,bz=square_groups(fields[:2]);cg,cc,cz=square_groups(fields[2:]);assert bz==0 and cz>0
 print('GROUPS_READY',name,len(bg),len(cg),bc,cc,'seconds',time.monotonic()-start,flush=True)
 for n,K in [(21,522),(23,2400),(19,1800)]:
  tick=time.monotonic();dest=BASE/f'verification/{name}_n{n:03d}_K{K:05d}.json';assert not dest.exists()
  folder='scaled_factored_weak' if num==16 else 'scaled50_factored_weak'
  fullp=ROOT/f'research/{folder}/verification/{name}_n{n:03d}_K{K:05d}.json'
  full=json.loads(fullp.read_text());assert full['candidate']==name and full['n']==n and full['K']==K and full['raw_sha256']==sha(source)
  bind(full);assert full['whole_plane'] and full['direct_parts_overlap'] and full['gradient_certificate']['strict_bound_all_critical_points']
  vals,records=values(model,n,K,bg,cg);I=arb(full['pairing']);assert I.overlaps(arb(full['pairing_by_parts']))
  H=ar(Q(full['H_upper_exact']));D=vals['Dbar'];radius=2*abs(I)/(D+(D*D+4*H*abs(I)).sqrt())
  floor=Q(int((radius.lower()*10**18).floor().unique_fmpz())-1,10**18);assert ar(floor)>0 and ar(floor)<radius
  M,C=arb(full['M']),arb(full['C']);checks={'M_below_A_plus_B':M<vals['A']+vals['Bbar'],'C_below_Cbar':C<vals['Cbar'],'radius_below_full_M_C':radius<arb(full['radius'])};assert all(checks.values())
  mesh=floating['probes'][f'{n}:{K}'];values_for_mesh={'I_signed_mesh':I,'A':vals['A'],'B_bound':vals['Bbar'],'C_bound':vals['Cbar'],'D':D}
  errors={key:{'mesh_decimal':str(mesh[key]),'exact':v.str(100),'mesh_minus_exact':(arb(str(mesh[key]))-v).str(100),'relative_error':((arb(str(mesh[key]))-v)/abs(v)).str(100)} for key,v in values_for_mesh.items()}
  Hmesh=arb(str(mesh['H_bound_mesh']));h_admitted=Hmesh>H
  meshHradius=2*abs(I)/(D+(D*D+4*Hmesh*abs(I)).sqrt())
  mesh_formula=2*abs(arb(str(mesh['I_signed_mesh'])))/(arb(str(mesh['D']))+(arb(str(mesh['D']))**2+4*Hmesh*abs(arb(str(mesh['I_signed_mesh'])))).sqrt())
  mesh_replay_error=(arb(str(mesh['m_lower_bound']))-mesh_formula)/abs(mesh_formula)
  assert abs(mesh_replay_error)<arb('1e-12')
  out={'utc':now(),'candidate':name,'raw_sha256':sha(source),'n':n,'K':K,'precision_bits':ctx.prec,'point_checks':pc,'groups':{'u':len(bg),'rho':len(cg)},'pair_counts':[bc,cc],'constant_cosine_pairs':cz,
   'u_group_sha256':field_hash(bg),'rho_group_sha256':field_hash(cg),'values':{k:v.str(100) for k,v in vals.items()},'pairing':I.str(100),'H_upper_exact':full['H_upper_exact'],'radius':radius.str(100),'strict_lower_exact':str(floor),'consistency':checks,
   'full_M_C_radius':full['radius'],'full_M_C_over_envelope_radius':(arb(full['radius'])/radius).str(100),'float_errors':errors,'saved_FLOAT_rule':floating['rule'],'saved_FLOAT_label':floating['label'],
   'mesh_H_above_global_certificate':h_admitted,'exact_envelope_radius_with_mesh_H':meshHradius.str(100),'mesh_radius_relative_error':((arb(str(mesh['m_lower_bound']))-meshHradius)/abs(meshHradius)).str(100),'mesh_formula_relative_replay_error':mesh_replay_error.str(100),
   **records,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in ps+[cal,source,mp,fp,fullp]},'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-tick,'total_elapsed_seconds':time.monotonic()-start,
   'status':'OPEN independent scaled-envelope reproduction; exact own computation compared with frozen FLOAT data'}
  write(dest,out);print('CANDIDATE_DONE',name,n,K,'envelope',radius.str(25),'FLOAT_rel_error',out['mesh_radius_relative_error'],'seconds',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
 ctx.prec=2048
 ps=common_inputs();cal=calibrate(ps)
 for num in [16,17]:candidate(num,ps,cal)
