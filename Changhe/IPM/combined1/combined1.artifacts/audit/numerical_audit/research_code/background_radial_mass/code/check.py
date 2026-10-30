"""Exact radial background energies and finite-domain diagnostic comparison."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
import json,sys,time
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/background_radial_mass'
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from radial import Radial,ar,pshift,U
from norms import derivative,endpoint
Z=P([])
def digest(path):return sha256(path.read_bytes()).hexdigest()
def groups(A,delta):
 angular={};out={}
 for (ell,kind,n),V in A.items():
  q,W=endpoint(V);assert -1+ell*delta+2*q>-1
  angular.setdefault((kind,n),[]).append((ell,q,W))
 for (kind,n),terms in angular.items():
  for i,(ell,q,W) in enumerate(terms):
   for j in range(i,len(terms)):
    ell2,q2,W2=terms[j];e=-1+(ell+ell2)*delta/2+q+q2
    factor=(2 if kind=='c' and n==0 else 1)*(1 if i==j else 2)
    out[e]=out.get(e,Z)+factor*U*W*W2
 return out
def addgroups(a,b):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Z)+v
 return {k:v for k,v in out.items() if v}
def tail(a,r):
 v=1/(1+r*r);result=arb(0)
 for e,V in a.items():
  p=ar(v)**ar(e+1)
  for k,b in enumerate(V):
   if b:result+=ar(b)*p/ar(e+k+1)
   p*=ar(v)
 return arb.pi()/2*result
def whole(a):return sum((b/(e+k+1) for e,V in a.items() for k,b in enumerate(V) if b),Q(0))
def run(name):
 start=time.monotonic();ctx.prec=1536
 source=ROOT/f'research/candidate_audits/data/{name}/canonical.json'
 peerpath=ROOT/f'research/background_sobolev/verification/{name}.json';prior=json.loads(peerpath.read_text())
 assert prior['source_sha256']==digest(source)
 model=Radial(source);D={(0,0):{(j+1,'s',n):pshift(V,2) for (j,n),V in model.rho.items()}}
 for d in range(2):
  for nx in range(d+2):D[d+1,nx]=derivative(D[d,0],d,'y',model.delta) if nx==0 else derivative(D[d,nx-1],d,'x',model.delta)
  for nx in range(1,d+1):assert D[d+1,nx]==derivative(D[d,nx],d,'y',model.delta)
 terms=[groups(D[2,nx],model.delta) for nx in range(3)]
 gx=addgroups(terms[1],terms[2]);gy=addgroups(terms[0],terms[1])
 r0=Q(1,50);R=Q(str(Fraction(float('8356.474846731926'))))
 diagpath=next((ROOT/f'research/candidate_audits/data/{name}').glob('*diag*.json'));diag=json.loads(diagpath.read_text())
 energies={};equality={}
 for label,G in [('D_rho_x',gx),('D_rho_y',gy)]:
  exact=whole(G);assert exact==Q(prior['norms'][label]['unweighted_rational_sum']);equality[label]=True
  full=arb.pi()/2*ar(exact);fromr0=tail(G,r0);outer=tail(G,R)
  regions={'full':full,'origin':full-fromr0,'middle':fromr0-outer,'exterior':outer}
  assert all(v>0 for v in regions.values())
  assert (regions['origin']+regions['middle']+regions['exterior']).overlaps(full)
  energies[label]=regions
  print(label,{k:v.str(30) for k,v in regions.items()},flush=True)
 regions={}
 for region in ['full','origin','middle','exterior']:
  k=((arb(2).log()-arb(1)/2)*energies['D_rho_x'][region]+(3*arb(2).log()-2)*energies['D_rho_y'][region])/(16*arb.pi())
  regions[region]=k
 assert regions['full'].sqrt().overlaps(arb(prior['gradient_identity_conditional_HS_upper']))
 reported=ar(Q(str(Fraction(diag['BL2']['kappa_inner']))))
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'source_sha256':digest(source),
      'prior_background_sha256':digest(peerpath),'diagnostic_sha256':digest(diagpath),'launch_source_sha256':digest(BASE/'source/N1_chain8_core52.sh'),
      'proof_sha256':digest(BASE/'PROOF.md'),'code_sha256':digest(Path(__file__)),'precision_bits':ctx.prec,
      'inner_radius':str(r0),'outer_radius_exact_binary64':str(R),'full_exact_energy_comparisons':equality,
      'derivative_squared_masses':{label:{k:v.str(95) for k,v in a.items()} for label,a in energies.items()},
      'kappa_squared_masses':{k:v.str(95) for k,v in regions.items()},
      'kappa_full':regions['full'].sqrt().str(95),'kappa_exact_middle':regions['middle'].sqrt().str(95),
      'reported_floating_kappa':diag['BL2']['kappa_inner'],
      'reported_minus_exact_middle':(reported-regions['middle'].sqrt()).str(95),
      'missing_origin_fraction_of_kappa_squared':(regions['origin']/regions['full']).str(95),
      'missing_exterior_fraction_of_kappa_squared':(regions['exterior']/regions['full']).str(95),
      'elapsed_seconds':time.monotonic()-start,'scope':'Exact rational candidate. New radial localization pending independent reproduction; finite-domain floating comparison is descriptive.'}
 dest=BASE/f'verification/{name}.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
 print('kappa full',out['kappa_full'],'middle',out['kappa_exact_middle'],'reported difference',out['reported_minus_exact_middle'],'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run(sys.argv[1])
