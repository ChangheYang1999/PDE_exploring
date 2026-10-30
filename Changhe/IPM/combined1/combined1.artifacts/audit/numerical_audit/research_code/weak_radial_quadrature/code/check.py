"""Independent exact-field quadrature of the candidate007 first sine pairing."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time,math
import numpy as np
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_poly,ctx
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];D=R/'research/weak_radial_quadrature';NAME='C1-N1-007-d2w-j7-e2bal';KS=[0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096]
sys.path.insert(0,str(R/'research/projected_residual/code'))
from build import candidate_source,read_projection,destination
sys.path.insert(0,str(R/'research/localized_weak_probe/code'))
from beta_scale import integral,ar,ap,U
ctx.prec=2048

def H(p):return sha256(Path(p).read_bytes()).hexdigest()
def new(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def rational_float(x):
 a,b=float(x).as_integer_ratio();return Q(a,b)
def prim(P,b,x):
 if not x:return arb(0)
 xx=ar(x);out=arb(0)
 for j in reversed(range(len(P))):out=out*xx+P[j]/ar(b+j+1)
 return xx**ar(b+1)*out

def main():
 start=time.monotonic();src=candidate_source(NAME);assert H(src)=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316';c=Q(json.loads(src.read_text())['cl']);delta=1-1/c
 proj,meta=read_projection(NAME);parts=[(ell,ap(P),ap(P(U))) for ell,P in proj.items()];assert all(ell*delta/2-1>-1 for ell,_,_ in parts)
 exact={k:arb.pi()/2*sum((integral(V,ell*delta/2-1,k+1) for ell,P,V in parts),arb(0)) for k in KS}
 reference=R/'research/weak_mesh_comparison/verification/candidate007.json';ref={row['k']:row['exact_balls']['pairing'] for row in json.loads(reference.read_text())['rows']};previous=R/f'research/projected_residual/verification/{NAME}_probe_2048.json';ref.update({row['k']:row['pairing'] for row in json.loads(previous.read_text())['probes']})
 referencechecks={str(k):bool(z.overlaps(arb(ref[k]))) for k,z in exact.items() if k in ref};assert all(referencechecks.values())
 split={};unit=arb_poly([1,-1])
 for k in (0,1,2,4,8):
  end=[]
  for radius in [Q(1,50),Q(10000)]:
   x=1/(1+radius*radius);end.append(arb.pi()/2*sum((prim(V*unit**(k+1),ell*delta/2-1,x) for ell,P,V in parts),arb(0)))
  inside=exact[k]-end[0];outside=end[1];middle=end[0]-end[1]
  assert (inside+middle+outside).overlaps(exact[k]);split[k]={'inside':inside,'middle':middle,'outside':outside}
 rows=[];nodefiles=[]
 for order in [8,12,16,24,32]:
  tick=time.monotonic();lo=math.log(.02);upper=16.;edges=np.linspace(lo,upper,math.ceil(upper-lo)+1);z,w=np.polynomial.legendre.leggauss(order)
  s=np.concatenate([.5*(a+b+(b-a)*z) for a,b in zip(edges[:-1],edges[1:])]);ws=np.concatenate([.5*(b-a)*w for a,b in zip(edges[:-1],edges[1:])]);rr=np.exp(s);sel=(rr>=.02)&(rr<=1e4);rr=rr[sel];ws=ws[sel]
  nodes=[(rational_float(r),rational_float(weight)) for r,weight in zip(rr,ws)]
  npth=D/f'verification/nodes_mid{order}.json';new(npth,{'order':order,'rational_radii_weights':[[str(r),str(w)] for r,w in nodes]});nodefiles.append(npth)
  sums={k:arb(0) for k in KS};comparisons=0
  for r,w in nodes:
   v=ar(1/(1+r*r));t=ar(r*r/(1+r*r));val=arb(0)
   for ell,P,V in parts:
    a=P(t);b=V(v);assert a.overlaps(b);comparisons+=1;val+=v**ar(ell*delta/2)*b
   assert val.rel_accuracy_bits()>100
   for k in KS:sums[k]+=ar(w)*t**(k+2)*val
  sums={k:arb.pi()*z for k,z in sums.items()};data=[]
  for k in KS:
   error=sums[k]-exact[k]
   data.append({'k':k,'quadrature_ball':sums[k].str(65),'whole_plane_ball':exact[k].str(65),'error_vs_whole_plane':error.str(65),'relative_error':(error/abs(exact[k])).str(40),'error_vs_exact_middle':(sums[k]-split[k]['middle']).str(65) if k in split else None})
  rows.append({'middle_order':order,'nodes':len(nodes),'composition_overlap_checks':comparisons,'values':data,'elapsed_seconds':time.monotonic()-tick})
  print('MID',order,'nodes',len(nodes),'I0',sums[0].str(24),'error', (sums[0]-exact[0]).str(24),'seconds',time.monotonic()-tick,flush=True)
 paths=[src,destination(NAME),reference,previous,Path(__file__),D/'PROOF.md',R/'research/projected_residual/code/build.py',R/'research/localized_weak_probe/code/beta_scale.py',R/'research/localized_weak_probe/code/evaluate.py',R/'research/radial_fourier/code/radial.py']+nodefiles
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':NAME,'precision_bits':ctx.prec,'full_pairing_previous_checks':referencechecks,'radius_split':['1/50','10000'],'exact_splits':{str(k):{name:z.str(65) for name,z in row.items()} for k,row in split.items()},'rules':rows,'inputs':{str(p.relative_to(R)):H(p) for p in paths},'elapsed_seconds':time.monotonic()-start,'status':'Independent exact-field finite-sum error diagnostic; new whole-plane k values OPEN where no peer exists'}
 new(D/'verification/candidate007.json',out);print('DONE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
