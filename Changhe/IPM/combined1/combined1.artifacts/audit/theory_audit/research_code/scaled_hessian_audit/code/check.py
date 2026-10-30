"""Independent polar Hessians, complete CRT integrals, and peer comparisons."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,sys,time
from flint import fmpq as Q, arb,acb,ctx
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
spec=importlib.util.spec_from_file_location('hessian_polar',BASE/'code/polar.py');f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
Rat=f.Rat;ar=f.ar
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def derive(field,d,kind,axis,delta):
 out={};target=('c' if kind=='s' else 's') if axis=='y' else kind
 for (j,n),A in field.items():
  B=f.td(A,(j+1)*delta/2,d)
  plus=(B-n*A)/2;minus=(B+n*A)/2
  if axis=='y':
   if kind=='s':plus=-plus
   else:minus=-minus
  f.F.fold(out,j,n+1,plus,target);f.F.fold(out,j,n-1,minus,target)
 return {k:A for k,A in out.items() if A},target

def build(data):
 c,delta,rho,stream=f.fields(data)
 rx,kx=derive(rho,1,'s','x',delta);ry,ky=derive(rho,1,'s','y',delta)
 xx,kindxx=derive(rx,0,kx,'x',delta);xy,kindxy=derive(rx,0,kx,'y',delta)
 yx,_=derive(ry,0,ky,'x',delta);yy,kindyy=derive(ry,0,ky,'y',delta)
 assert xy==yx,'mixed derivatives'
 fields={label:(kind,{key:A.divide_t(1) for key,A in field.items()}) for label,kind,field in [('xx',kindxx,xx),('xy',kindxy,xy),('yy',kindyy,yy)]}
 assert all(n>0 and n%2 for kind,field in fields.values() for j,n in field)
 return c,delta,fields

def evaluate(field,kind,delta,xs,ys):
 x,y=ar(Q(xs)),ar(Q(ys));r2=x*x+y*y;r=r2.sqrt();v=1/(1+r2);t=1-v;z=acb(x/r,y/r)
 return r*sum((v**ar(1+(j+1)*delta/2)*A.evaluate(t,v)*((z**n).real if kind=='c' else (z**n).imag) for (j,n),A in field.items()),arb(0))

def groups(field):
 angular={};out={};count=0
 for (j,n),A in field.items():angular.setdefault(n,[]).append((j,A))
 for n,terms in angular.items():
  for i,(j,A) in enumerate(terms):
   for k,(jj,B) in enumerate(terms[:i+1]):
    f.add(out,j+jj+2,A*B*(1 if i==k else 2));count+=1
 return {ell:A for ell,A in out.items() if A},count

def one(num,manifest):
 start=time.monotonic();m=manifest['candidates'][str(num)];raw=ROOT/m['raw'];peerpath=ROOT/m['peer']
 assert sha(raw)==m['raw_sha256'] and sha(peerpath)==m['peer_sha256']
 peer=json.loads(peerpath.read_text());assert peer['raw_sha256']==sha(raw)
 c,delta,fields=build(json.loads(raw.read_text()));pointchecks=[]
 for point in peer['point_checks']:
  vals={};checks={}
  for label,(kind,field) in fields.items():
   value=evaluate(field,kind,delta,point['x'],point['y']);checks[label]=value.overlaps(arb(point['values'][label]));assert checks[label],(num,label,point['x'],value)
   vals[label]=value.str(100)
  pointchecks.append({'x':point['x'],'y':point['y'],'values':vals,'peer_overlaps':checks})
 print('FIELDS',num,'seconds',time.monotonic()-start,flush=True)
 details={};E={}
 for label,(kind,field) in fields.items():
  gs,count=groups(field);ps=peer['component_energies'][label];pm={row['ell']:row for row in ps['moments']};assert set(gs)==set(pm)
  rows=[];total=arb(0)
  for ell,A in sorted(gs.items()):
   b=ell*delta/2-1;assert b==Q(pm[ell]['b'])
   val,record=f.integrate(A,b,f'{num}:{label}:{ell}')
   record['ell']=ell;record['peer_moment_overlap']=val.overlaps(arb(pm[ell]['integral']));assert record['peer_moment_overlap']
   rows.append(record);total+=val
  value=arb.pi()/2*total;assert value>0 and value.rel_accuracy_bits()>150
  assert value.overlaps(arb(ps['energy']))
  E[label]=value;details[label]={'field_hash':f.F.field_hash(field),'pair_count':count,'group_count':len(gs),'moments':rows,'energy':value.str(100),'peer_energy_overlap':True}
 X2=E['xx']+E['xy'];Y2=E['xy']+E['yy'];H2=X2+Y2
 K2=((arb(2).log()-arb(1)/2)*X2+(3*arb(2).log()-2)*Y2)/(16*arb.pi())
 vals={'X':X2.sqrt(),'Y':Y2.sqrt(),'D2rho':H2.sqrt(),'kappa':K2.sqrt()}
 squares={'X2':X2,'Y2':Y2,'D2rho_squared':H2,'kappa_squared':K2}
 comparisons={k:v.overlaps(arb(peer['values'][k])) for k,v in vals.items()};assert all(comparisons.values())
 squarechecks={k:v.overlaps(arb(peer[k])) for k,v in squares.items()};assert all(squarechecks.values())
 calibration={}
 if num==7:
  old=json.loads((BASE/'source/accepted007.json').read_text())
  for label,key,value in [('X','D_rho_x',X2),('Y','D_rho_y',Y2),('D2rho','D2rho',H2)]:
   entry=old['norms'][key];assert Q(entry['weight_error_rational'])==0
   exact=arb.pi()/2*ar(Q(entry['unweighted_rational_sum']));assert value.overlaps(exact)
   assert vals[label].overlaps(arb(entry['norm_upper_ball']))
   calibration[label]={'exact_energy_overlap':True,'containing_norm_ball_overlap':True,'endpoint_ball_overlap_not_required':vals[label].overlaps(arb(entry['norm_upper']))}
 result={'utc':now(),'candidate':num,'raw_sha256':sha(raw),'peer_sha256':sha(peerpath),'precision_bits':ctx.prec,'mixed_derivative_exact_equality':True,'point_checks':pointchecks,'components':details,'values':{k:v.str(100) for k,v in vals.items()},'squares':{k:v.str(100) for k,v in squares.items()},'peer_norm_overlaps':comparisons,'peer_square_overlaps':squarechecks,'007_calibration':calibration,'whole_plane':True,'no_global_theta_or_inverse_claim':True,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in [BASE/'PROOF.md',BASE/'data/manifest.json',BASE/'code/check.py',BASE/'code/polar.py',BASE/'code/rational.py',BASE.parent/'weak_probe_audit/code/reproduce.py',BASE.parent/'new_successor_weak/code/check.py']},'elapsed_seconds':time.monotonic()-start}
 out=BASE/'verification'/f'{num:03d}.json'
 with out.open('x') as fd:json.dump(result,fd,indent=2);fd.write('\n')
 print('DONE',num,vals['kappa'].str(50),'seconds',result['elapsed_seconds'],flush=True)

if __name__=='__main__':
 ctx.prec=2048;manifest=json.loads((BASE/'data/manifest.json').read_text())
 assert sha(BASE/'PROOF.md')==manifest['proof_sha256']
 for rel,h in manifest['files'].items():assert sha(ROOT/rel)==h
 for num in [7,16,17]:one(num,manifest)
