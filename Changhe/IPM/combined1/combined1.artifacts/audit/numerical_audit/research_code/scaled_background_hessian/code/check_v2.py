"""Full-plane background Hessian and structured commutator norm."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,sys,time
from flint import arb,acb,fmpq as Q,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/scaled_background_hessian';BACK=ROOT/'research/joint_scaled_factored_weak'
sys.path.insert(0,str(BACK/'code'))
from fields_joint import Rat,ScaledRadial,combine,ar,field_hash
import weak as W
sys.set_int_max_str_digits(0)
now=lambda:datetime.now(timezone.utc).isoformat()
def sha(p):
 h=sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def write(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def module(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
JET=module('n4_hessian_taylor',ROOT/'research/multiscale_generators/code/cartesian.py')
def bind(d):
 for rel,h in d.get('inputs',{}).items():assert sha(ROOT/rel)==h,rel

def build(model):
 checks=[]
 for total in range(1,6):
  for x in range(total+1):model.deriv(x,total-x)
  for x in range(1,total):
   y=total-x;kind='s' if y%2 else 'c'
   d=model.differentiate(model.deriv(x-1,y),total-1,kind,'x')
   same=d==model.deriv(x,y);assert same;checks.append({'x':x,'y':y,'equal':same})
 specs=[('xx','s',(4,1),(2,3)),('xy','c',(3,2),(1,4)),('yy','s',(2,3),(0,5))]
 fields={}
 for label,kind,left,right in specs:
  coeffs=combine(model.deriv(*left),model.deriv(*right))
  field={(j+1,n):-A.divide_t(3) for (j,n),A in coeffs.items()}
  assert all(n>0 and n%2==1 for ell,n in field)
  fields[label]=(kind,field)
 return fields,checks

def point_checks(model,fields,source):
 records=[]
 for xs,ys in [('1/10','73/100'),('3','4'),('60','80')]:
  x,y=ar(Q(xs)),ar(Q(ys));r=(x*x+y*y).sqrt();v=1/(1+r*r);t=1-v;z=acb(x/r,y/r)
  jet=JET.GeneratorJet(source,xs,ys,5)
  target={'xx':-jet.chi(4,1)-jet.chi(2,3),'xy':-jet.chi(3,2)-jet.chi(1,4),'yy':-jet.chi(2,3)-jet.chi(0,5)}
  checks={};vals={}
  for label,(kind,field) in fields.items():
   value=r*sum((v**ar(1+ell*model.delta/2)*A.evaluate(t,v)*((z**n).real if kind=='c' else (z**n).imag) for (ell,n),A in field.items()),arb(0))
   checks[label]=value.overlaps(target[label]);assert checks[label],(label,xs,ys)
   vals[label]=value.str(80)
  records.append({'x':xs,'y':ys,'Cartesian_jet_overlaps':checks,'values':vals})
 return records

def energy(field,model,label):
 angular={};groups={};count=0
 for (ell,n),A in field.items():angular.setdefault(n,[]).append((ell,A))
 for n,terms in angular.items():
  assert n>0 and n%2
  for i,(ell,A) in enumerate(terms):
   for j in range(i+1):
    ell2,B=terms[j];W.add(groups,ell+ell2,A*B*(1 if i==j else 2));count+=1
 groups={k:A for k,A in groups.items() if A};assert min(groups)>=2
 value,rows=W.integrate_groups(groups,model.delta,Q(-1),1,label)
 assert value>0 and value.rel_accuracy_bits()>150
 return value,{'group_sha256':field_hash(groups),'pair_count':count,'group_count':len(groups),'moments':rows,'energy':value.str(100)}

def common():
 ps=[Path(__file__),BASE/'CALIBRATION_CORRECTION.md',BASE/'PROOF.md',BASE/'verification/PREPARE.json',BACK/'PROOF.md',BACK/'code/fields_joint.py',BACK/'code/weak.py',ROOT/'research/factored_pole_moments/PROOF.md',ROOT/'research/factored_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/gradient_commutator/PROOF.md',ROOT/'research/multiscale_generators/code/cartesian.py']
 prep=json.loads((BASE/'verification/PREPARE.json').read_text());assert prep['proof_sha256']==sha(BASE/'PROOF.md')
 for name in ['scalar_joint.json','fields.json','candidate013.json']:
  p=BACK/'verification'/name;bind(json.loads(p.read_text()));ps.append(p)
 return ps

def run(num,ps,cal=None):
 start=time.monotonic()
 name='C1-N1-007-d2w-j7-e2bal' if num==7 else f'C1-N1-{num:03d}-legqs{25 if num==16 else 50}-quot013'
 directory=ROOT/'research/candidate_audits/data'/name;mp=directory/'MANIFEST.json';manifest=json.loads(mp.read_text());assert manifest['id']==name
 entry=manifest['coefficient_files'][0];source=directory/entry['name'];assert sha(source)==entry['sha256']
 output=BASE/f'verification/{name}.json';assert not output.exists()
 auditp=ROOT/f'research/generator_sector_audit/verification/{name}_direct.json'
 if not auditp.exists():auditp=ROOT/f'research/candidate_audits/verification/{name}.json'
 audit=json.loads(auditp.read_text())
 assert audit['generator_sha256']==sha(source) and audit['B0n_exact'] and audit['leading_density_equal_state131']
 model=ScaledRadial(source);fields,mixed=build(model);points=point_checks(model,fields,source)
 print('HESSIAN_FIELDS',name,'seconds',time.monotonic()-start,flush=True)
 energies={};details={}
 for label,(_,field) in fields.items():energies[label],details[label]=energy(field,model,label)
 X2=energies['xx']+energies['xy'];Y2=energies['xy']+energies['yy'];D2=X2+Y2
 k2=((arb(2).log()-arb(1)/2)*X2+(3*arb(2).log()-2)*Y2)/(16*arb.pi())
 vals={'X':X2.sqrt(),'Y':Y2.sqrt(),'D2rho':D2.sqrt(),'kappa':k2.sqrt()}
 additional=[];old={};comparison={};endpoint_checks={};exact_energy_checks={}
 if num==7:
  p=ROOT/f'research/background_sobolev/verification/{name}.json';d=json.loads(p.read_text());additional.append(p)
  additional.append(ROOT/'research/whole_plane_norms/code/norms.py')
  for key,oldkey,E in [('X','D_rho_x',X2),('Y','D_rho_y',Y2),('D2rho','D2rho',D2)]:
   previous=d['norms'][oldkey];assert Q(previous['weight_error_rational'])==0
   exact=arb.pi()/2*ar(Q(previous['unweighted_rational_sum']))
   exact_energy_checks[key]=E.overlaps(exact);assert exact_energy_checks[key],(key,E.str(60),exact.str(60))
   old[key]=vals[key].overlaps(arb(previous['norm_upper_ball']));assert old[key]
   endpoint_checks[key]=vals[key].overlaps(arb(previous['norm_upper']))
  old['kappa']=vals['kappa'].overlaps(arb(d['gradient_identity_conditional_HS_upper']));assert old['kappa']
 else:
  assert cal and json.loads(cal.read_text())['old007_norm_overlaps']=={'X':True,'Y':True,'D2rho':True,'kappa':True};additional.append(cal)
  fp=next(directory.glob('*diag2.json'));d=json.loads(fp.read_text());assert d['sha256']==sha(source);additional.append(fp)
  for key,oldkey in [('X','D_rho_x_L2_inner'),('Y','D_rho_y_L2_inner'),('kappa','kappa_inner')]:
   approx=arb(str(d['BL2'][oldkey]));value=vals[key]
   comparison[key]={'saved_FLOAT':str(d['BL2'][oldkey]),'whole_minus_FLOAT':(value-approx).str(100),'relative_difference':((value-approx)/value).str(100)}
  comparison['FLOAT_scope']=d['BL2']['note'];comparison['saved_theta_mesh_only']=d['BL2']['theta_inner_sup']
 out={'utc':now(),'candidate':name,'raw_sha256':sha(source),'precision_bits':ctx.prec,'mixed_derivative_checks':mixed,'point_checks':points,'component_field_sha256':{k:field_hash(f) for k,(_,f) in fields.items()},'component_energies':details,
 'X2':X2.str(100),'Y2':Y2.str(100),'D2rho_squared':D2.str(100),'kappa_squared':k2.str(100),'values':{k:v.str(100) for k,v in vals.items()},'old007_norm_overlaps':old,'old007_exact_energy_overlaps':exact_energy_checks,'old007_endpoint_ball_overlaps_diagnostic':endpoint_checks,'FLOAT_comparison':comparison,
 'tensor_identity_verified':D2.overlaps(energies['xx']+2*energies['xy']+energies['yy']),'whole_plane':True,'no_global_theta_claim':True,'foreign_code_executed':False,
 'inputs':{str(p.relative_to(ROOT)):sha(p) for p in ps+[source,mp,auditp]+additional},'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent scaled-background review; complete own Hessian and structured Hilbert-Schmidt norm'}
 assert out['tensor_identity_verified'];write(output,out);print('HESSIAN_DONE',name,'kappa',vals['kappa'].str(35),'seconds',out['elapsed_seconds'],flush=True)
 return output

if __name__=='__main__':
 ctx.prec=2048;ps=common();cal=run(7,ps)
 for num in [16,17]:run(num,ps,cal)
