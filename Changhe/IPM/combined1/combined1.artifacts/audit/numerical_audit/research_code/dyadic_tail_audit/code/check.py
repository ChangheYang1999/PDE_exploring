"""Independent Cartesian Laplacian, full finite tail, and scalar interval cover."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/dyadic_tail_audit'
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from radial import Radial,ar,T,U
from norms import construct
Z=P([])
def digest(path):return sha256(path.read_bytes()).hexdigest()
def run():
 start=time.monotonic();ctx.prec=1536
 source=ROOT/'research/baseline/data/state131_independent.json'
 peerpath=BASE/'source/T4_tail_results.json';peer=json.loads(peerpath.read_text())
 coverpath=BASE/'source/T4_cover_results.json';cover=json.loads(coverpath.read_text())
 assert peer['source_sha256']==digest(source)==digest(BASE/'source/T4_state131.json')
 assert peer['code_sha256']==digest(BASE/'source/T4_check.py')
 assert peer['helper_sha256']==digest(BASE/'source/T4_reproduce.py')
 assert cover['source_sha256']==digest(peerpath)
 assert cover['code_sha256']==digest(BASE/'source/T4_cover.py')
 assert cover['proof_sha256']==digest(BASE/'source/T4_PROOF.md')
 model=Radial(source);c,delta=model.c,model.delta;b=1-2*delta;D=construct(model,2)
 lap={key:V+D[2,2].get(key,Z) for key,V in D[2,0].items()}
 for key,V in D[2,2].items():
  if key not in D[2,0]:lap[key]=V
 lap={key:V for key,V in lap.items() if V}
 # The polar identity is a separate algebraic check of the Cartesian trace.
 td=lambda V,d:(1-2*d*T)*V+2*T*U*V.derivative()
 polar={key:td(td(V,key[0]*delta/2),key[0]*delta/2)-key[2]**2*V for key,V in D[0,0].items()}
 polar={key:V for key,V in polar.items() if V}
 assert set(lap)==set(polar)
 assert all(T*V==polar[key] for key,V in lap.items())
 coeff={}
 for (ell,kind,n),V in lap.items():
  assert kind=='s' and n>0
  W=(T*V)(U)
  for k,v in enumerate(W):
   if not v:continue
   e=ell*delta/2-delta+k
   assert e>=0
   row=coeff.setdefault(e,{})
   row[n]=row.get(n,Q(0))+v
 coeff={e:{n:v for n,v in row.items() if v} for e,row in coeff.items()}
 coeff={e:row for e,row in coeff.items() if row}
 energies={e:sum((v*v for v in row.values()),Q(0)) for e,row in coeff.items()}
 peerenergies={Q(k):Q(v) for k,v in peer['angular_squared_norms_over_pi'].items()}
 assert energies==peerenergies
 assert len(coeff)==peer['coefficient_groups']
 assert len(D[0,0])==peer['residual_components']
 leading=(arb.pi()*ar(energies[Q(0)])).sqrt()
 assert leading.overlaps(arb(peer['leading_laplacian_norm']))
 rows=[]
 for ref in peer['tail_tests']:
  J=ref['J'];v=Q(1,1+2**(2*J));t=1-v
  ratio=1-ar(t)**ar(delta)+sum((ar(v)**ar(e)*(ar(E/energies[Q(0)])).sqrt() for e,E in energies.items() if e>0),arb(0))
  assert ratio.overlaps(arb(ref['relative_remainder_upper']))
  assert bool(ratio<arb(1)/2)==ref['below_half']
  assert bool(ratio<arb(1)/4)==ref['below_quarter']
  rows.append({'J':J,'relative_remainder_upper':ratio.str(100),'peer_overlap':True,'below_half':bool(ratio<arb(1)/2),'below_quarter':bool(ratio<arb(1)/4)})
  print('J',J,'ratio',ratio.str(30),flush=True)
 J=13;assert next(r for r in rows if r['J']==J)['below_half']
 K=(1-arb(2)**ar(2*b-2))/ar(2-2*b)
 cells=[];N=256
 for j,ref in enumerate(cover['cells']):
  l,h=Q(j,N),Q(j+1,N)
  assert Q(ref['left'])==l and Q(ref['right'])==h
  left=ar(energies[Q(0)]/4)*K*ar(1+2/c+delta*l)**2
  right=ar(8*(c-1)**4*(1-l)**4)*(1-arb(2)**ar(-2*delta*h))*arb(2)**ar(2*J*delta*h)
  gap=left-right;ratio=left/right
  assert gap>0 and ratio>1
  values={'LHS_lower_ball':left,'RHS_upper_ball':right,'positive_gap_ball':gap,'squared_ratio_lower_ball':ratio}
  assert all(v.overlaps(arb(ref[key])) for key,v in values.items())
  cells.append({'left':str(l),'right':str(h),**{key:v.str(100) for key,v in values.items()},'peer_comparisons':4})
 assert len(cells)==N==cover['cover_cells']
 mingap=min(arb(r['positive_gap_ball']).lower() for r in cells)
 minratio=min(arb(r['squared_ratio_lower_ball']).lower() for r in cells)
 # Peer's printed lower endpoints need not overlap higher-precision endpoints;
 # compare their enclosing full cell quantities above, not those endpoints.
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':digest(source),
      'peer_tail_sha256':digest(peerpath),'peer_cover_sha256':digest(coverpath),'proof_sha256':digest(BASE/'PROOF.md'),
      'code_sha256':digest(Path(__file__)),'radial_code_sha256':digest(ROOT/'research/radial_fourier/code/radial.py'),
      'derivative_code_sha256':digest(ROOT/'research/whole_plane_norms/code/norms.py'),
      'historical_tail_proof_hash_matches_current':peer['proof_sha256']==digest(BASE/'source/T4_PROOF.md'),
      'historical_tail_proof_sha256':peer['proof_sha256'],'current_peer_proof_sha256':digest(BASE/'source/T4_PROOF.md'),
      'precision_bits':ctx.prec,'c':str(c),'delta':str(delta),'b':str(b),
      'residual_components':len(D[0,0]),'cartesian_laplacian_components':len(lap),
      'cartesian_polar_exact_agreements':len(lap),'coefficient_groups':len(coeff),
      'exact_angular_squared_norm_comparisons':len(energies),'leading_laplacian_norm':leading.str(100),
      'angular_squared_norm_hashes':{str(e):sha256(str(E).encode()).hexdigest() for e,E in sorted(energies.items())},
      'tail_tests':rows,'cover_cells':cells,'minimum_positive_gap_lower':mingap.str(95),
      'minimum_squared_ratio_lower':minratio.str(95),'elapsed_seconds':time.monotonic()-start,
      'scope':'Finite tail and conditional scalar contradiction independently verified. Analytic high-inverse and radius-ceiling hypotheses require separate review.'}
 dest=BASE/'verification/state131.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
 print('groups',len(coeff),'D',leading.str(35),'cells',len(cells),'minratio',minratio.str(35),'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':run()
