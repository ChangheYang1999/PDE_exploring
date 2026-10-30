"""Independent Cartesian residual, exact weighted energies and membership."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/weighted_full_norm'
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from radial import Radial,ar,U
from norms import endpoint,evaluate_derivative
ZERO=P([])
def digest(path):return sha256(path.read_bytes()).hexdigest()
def run():
 start=time.monotonic();ctx.prec=1536
 source=ROOT/'research/baseline/data/state131_independent.json'
 peerpath=BASE/'source/T4_state131_1024.json';peer=json.loads(peerpath.read_text())
 assert peer['source_sha256']==digest(BASE/'source/T4_state131.json')==digest(source)
 assert peer['proof_sha256']==digest(BASE/'source/T4_PROOF.md')
 assert peer['code_sha256']==digest(BASE/'source/T4_evaluate.py')
 model=Radial(source);F=model.residual_sine();delta=model.delta
 D={(h+1,'s',n):V for (h,n),V in F.items()};fields=[]
 for x,y in [('1/2','1/2'),('0','1'),('3','4'),('6','8')]:
  assembled=evaluate_derivative(D,0,model,x,y);direct=model.evaluate(x,y)['residual']
  assert assembled.overlaps(direct)
  fields.append({'x':x,'y':y,'overlap':True,'assembled':assembled.str(60)})
 modes={};leading={};orders=[]
 for (h,n),V in F.items():
  ell=h+1;v,W=endpoint(V);modes.setdefault(n,[]).append((ell,v,W));orders.append((ell,n,v))
  for j,b in enumerate(W):
   if b:
    z=ell*delta/2+v+j;key=(z,n);leading[key]=leading.get(key,Q(0))+b
 leading={k:v for k,v in leading.items() if v};qmin=min(z for z,n in leading)
 energy_leading=sum((b*b for (z,n),b in leading.items() if z==qmin),Q(0))
 assert qmin==delta and Q(peer['leading_q'])==qmin
 threshold=2-2*qmin;assert threshold==2/model.c==Q(peer['sharp_weight_membership_a_greater_than'])
 assert energy_leading==Q(peer['leading_angular_energy_over_pi'])>0
 groups={}
 for n,terms in modes.items():
  for i,(ell,v,W) in enumerate(terms):
   for j in range(i,len(terms)):
    ell2,v2,W2=terms[j];e=(ell+ell2)*delta/2+v+v2-3
    groups[e]=groups.get(e,ZERO)+(1 if i==j else 2)*U*W*W2
 print('assembled',len(F),'components',len(modes),'angular modes',len(groups),'groups',flush=True)
 rows=[]
 for prior in peer['weights']:
  a=Q(prior['a']);member=a>threshold;assert member==prior['member']
  row={'a':str(a),'member':member,'peer_membership_agrees':True}
  if member:
   assert all(a-3+ell*delta+2*v>-1 for ell,n,v in orders)
   E=Q(0)
   for e,V in groups.items():
    for j,b in enumerate(V):
     if b:
      assert a+e+j+1>0
      E+=b/(a+e+j+1)
   assert E==Q(prior['exact_energy_over_pi_half'])>0
   value=(arb.pi()/2*ar(E)).sqrt();assert value.overlaps(arb(prior['norm']))
   serialized=str(E).encode();row.update(exact_energy_equality=True,exact_energy_sha256=sha256(serialized).hexdigest(),norm=value.str(100),peer_norm_overlap=True)
   print(a,value.str(35),'exact energy agrees',flush=True)
  else:print(a,'diverges by exact leading sector',flush=True)
  rows.append(row)
 assert len(F)==peer['residual_components'] and len(modes)==peer['angular_modes']
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':digest(source),'peer_result_sha256':digest(peerpath),'proof_sha256':digest(BASE/'PROOF.md'),'code_sha256':digest(Path(__file__)),'radial_code_sha256':digest(ROOT/'research/radial_fourier/code/radial.py'),'precision_bits':ctx.prec,'residual_components':len(F),'angular_modes':len(modes),'leading_q':str(qmin),'sharp_membership_a_greater_than':str(threshold),'exact_leading_angular_energy_agrees':True,'field_checks':fields,'rows':rows,'elapsed_seconds':time.monotonic()-start}
 dest=BASE/'verification/state131.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
