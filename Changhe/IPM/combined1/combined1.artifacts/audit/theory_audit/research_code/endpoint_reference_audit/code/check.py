"""Independent audit of the endpoint extensions in the Opus review."""
from pathlib import Path
from datetime import datetime,timezone
import importlib.util,json,hashlib,time
from flint import fmpq as Q,arb,ctx
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
spec=importlib.util.spec_from_file_location('finite_tail_audit',BASE.parent/'finite_tail_surgery/code/check.py');f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dot(a,b):return sum((v*b.get(n,Q(0)) for n,v in a.items()),Q(0))
def projected(a,p):
 z=dot(a,p)/dot(p,p);return {n:a.get(n,Q(0))-z*p.get(n,Q(0)) for n in set(a)|set(p)}
def main():
 tick=time.monotonic();ctx.prec=768;m=json.loads((BASE/'data/manifest.json').read_text());assert sha(BASE/'PROOF.md')==m['proof_sha256']
 for rel,h in m['files'].items():assert sha(ROOT/rel)==h
 opus=json.loads((BASE/'source/Opus_results.json').read_text());results=[]
 c=Q('4076476460239181/2251799813685248');delta=1-1/c;expo=lambda pair:1-pair[0]*delta-2*pair[1]
 q,p,e61=expo((1,2)),expo((10,0)),expo((6,1));eps,epsprime=q-p,q-e61
 assert 0<eps<epsprime<delta and q+3==-delta and -2<q+3<0
 for num in ('007','013','014'):
  src=json.loads((BASE/'source'/f'{num}_sectors.json').read_text());end=json.loads((BASE/'source'/f'{num}_endpoint.json').read_text())
  th={(r['K'],r['L']):f.decode(r['density']) for r in src['sectors']};ps={(r['K'],r['L']):f.decode(r['stream']) for r in src['sectors']}
  A=f.decode(end['F12']);P=f.decode(end['P']);assert dot(P,P)>0
  th[(4,1)],ps[(4,1)]={},{}
  a2=f.residual((9,0),th,ps,expo,c);q2=expo((9,0));b2={n:z/(1-c*q2) for n,z in a2.items()}
  potential2=f.potential(q2+3,b2);d2,s2=f.fields(q2+3,potential2);assert d2==b2
  th.setdefault((9,0),{});ps.setdefault((9,0),{})
  for n,v in d2.items():f.put(th[(9,0)],n,v)
  for n,v in s2.items():f.put(ps[(9,0)],n,v)
  B=f.residual((10,0),th,ps,expo,c);assert B
  pa=projected(A,P);pb=projected(B,P)
  aa={n:z/(4*c) for n,z in pa.items()};bb={n:z/(1-c*p) for n,z in pb.items()}
  ab=dot(aa,bb);a2norm=dot(aa,aa);b2norm=dot(bb,bb);assert ab>0
  cosine=arb(ab)/(arb(a2norm*b2norm).sqrt());assert cosine.overlaps(arb(opus['B'][num]['D']['cosine_a_b']))
  d=(arb.pi()*arb(a2norm)).sqrt();bn=(arb.pi()*arb(b2norm)).sqrt()
  assert d.overlaps(arb(opus['B'][num]['D']['d_over_4c'])) and bn.overlaps(arb(opus['B'][num]['D']['perp_F100_over_De']))
  density4={n:z/(4*c) for n,z in A.items()};pot4=f.potential(q+3,density4);rho4,stream4=f.fields(q+3,pot4);assert rho4==density4
  assert all((c*q-1)*rho4.get(n,Q(0))+A.get(n,Q(0))==0 for n in set(rho4)|set(A))
  data={'candidate':num,'A':f.encode(A),'P':f.encode(P),'B10_after_repairs':f.encode(B),'projection_inner_product_div_pi':str(ab),'projection_a_squared_div_pi':str(a2norm),'projection_b_squared_div_pi':str(b2norm),'fourth_density':f.encode(rho4),'fourth_potential':f.encode(pot4),'fourth_stream':f.encode(stream4)}
  out=BASE/'data'/f'{num}_fourth.json'
  with out.open('x') as fd:json.dump(data,fd,indent=2);fd.write('\n')
  results.append({'candidate':num,'positive_projection_inner_product':True,'cosine':cosine.str(85),'endpoint_perpendicular_norm':d.str(85),'next_perpendicular_norm':bn.str(85),'fourth_density_exact':True,'linear_endpoint_cancellation':True,'data_sha256':sha(out)})
 result={'utc':datetime.now(timezone.utc).isoformat(),'c':str(c),'q':str(q),'p':str(p),'epsilon':str(eps),'epsilon_prime':str(epsprime),'results':results,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in [BASE/'PROOF.md',BASE/'data/manifest.json',Path(__file__),BASE.parent/'finite_tail_surgery/code/check.py']},'elapsed_seconds':time.monotonic()-tick}
 with (BASE/'verification/result.json').open('x') as fd:json.dump(result,fd,indent=2);fd.write('\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
