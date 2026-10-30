from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from collections import defaultdict
import json,hashlib,time,sys
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=512
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def q(x):
 f=Fraction(str(x));return Q(f.numerator,f.denominator)
def ar(x):return arb(x.numerator)/x.denominator
def put(d,n,v):
 if n==0 or v==0:return
 if n<0:n,v=-n,-v
 d[n]=d.get(n,Q(0))+v
 if d[n]==0:del d[n]
def encode(d):return {str(n):str(v) for n,v in sorted(d.items())}
def norm(d):return (arb.pi()*ar(sum((v*v for v in d.values()),Q(0)))).sqrt()
def add_pair(out,P,T,ep,et):
 for m,A in P.items():
  for n,Bv in T.items():
   ab=A*Bv/2
   put(out,n+m,ab*(-et*m+(ep+1)*n))
   put(out,n-m,ab*(-et*m-(ep+1)*n))
start=time.monotonic();inputs=json.loads((B/'data/inputs.json').read_text())
peer=json.loads((B/'source/T2_result.json').read_text())['D'];results=[];allprofiles={}
for inp in inputs:
 localstart=time.monotonic();name=inp['candidate'];src=Path(inp['path']);assert sha(src)==inp['sha256']
 data=json.loads(src.read_text());c=q(data['cl']);assert c==Q(4076476460239181,2251799813685248)
 gamma=1/c;delta=1-gamma;amps=defaultdict(lambda:[Q(0),Q(0)])
 for (j,m,k),raw in zip(data['order'],data['coefficients']):
  v=q(raw);amps[j,2*m][0]+=v;amps[j,2*m][1]+=k*v
 Th={};Ps={}
 for (j,n),(A0,Ader) in amps.items():
  p=(3+gamma-j*delta)/2
  for L,A in enumerate([A0,p*A0-Ader]):
   key=(j+1,L);e=1-(j+1)*delta-2*L;d=e+3
   rr=Th.setdefault(key,{});ss=Ps.setdefault(key,{})
   put(rr,n+1,-A*(d*d-n*n)*(d-2-n)/2)
   put(rr,n-1,+A*(d*d-n*n)*(d-2+n)/2)
   put(ss,n+2,+A*(d-n)*(d-n-2)/4)
   put(ss,n-2,-A*(d+n)*(d+n-2)/4)
 keys=[(K,L) for K in range(1,10) for L in range(2)]
 def expo(key):return 1-key[0]*delta-2*key[1]
 assert len({expo(key) for key in keys})==len(keys)
 assert 1-10*delta<-3 and gamma-4<-3
 coefs={};poisson={}
 for key in keys:
  e=expo(key);rhs={}
  for n,A in Th.get(key,{}).items():
   put(rhs,n+1,(n-e)*A/2);put(rhs,n-1,-(n+e)*A/2)
  lhs={n:((e+1)**2-n*n)*v for n,v in Ps.get(key,{}).items()}
  lhs={n:v for n,v in lhs.items() if v};assert lhs==rhs,(name,key)
  poisson[str(key)]=True
  out={n:(c*e-1)*v for n,v in Th.get(key,{}).items() if (c*e-1)*v}
  K,L=key
  for K1 in range(1,K):
   for L1 in range(L+1):
    k1=(K1,L1);k2=(K-K1,L-L1)
    add_pair(out,Ps.get(k1,{}),Th.get(k2,{}),expo(k1),expo(k2))
  coefs[key]=out
 ordered=sorted(keys,key=expo,reverse=True);nz=[k for k in ordered if coefs[k]]
 first=nz[0];qs=expo(first);threshold=qs+1
 dnz=[k for k in ordered if k[1]==1 and Th.get(k)]
 norms={k:norm(coefs[k]) for k in nz}
 pname=name if name in ['state131','d2','Mpen2'] else 'C1-N1-'+name
 comparisons=[]
 if pname in peer:
  ref=peer[pname];assert first==tuple(ref['first']);assert qs==q(ref['qstar'])
  assert nz==[tuple(x[0]) for x in ref['sectors_nonzero']]
  assert dnz==[tuple(x) for x in ref['density_L1_nonzero']]
  for key,exp,nval in ref['sectors_nonzero']:
   key=tuple(key);rel=abs(float(norms[key])/nval-1);assert rel<1e-12,(name,key,rel)
   assert abs(float(expo(key))-exp)<1e-12
   comparisons.append({'sector':list(key),'peer_norm_float':nval,'own_norm':norms[key].str(80),'relative_float_difference':rel})
 profiles={str(K):encode(Th.get((K,0),{})) for K in range(1,5)};allprofiles[name]=profiles
 exact={'candidate':name,'source':inp,'c_exact':str(c),'delta_exact':str(delta),'sectors':[{'K':k[0],'L':k[1],'exponent_exact':str(expo(k)),'density':encode(Th.get(k,{})),'stream':encode(Ps.get(k,{})),'residual':encode(coefs[k])} for k in ordered]}
 dst=B/f'data/{name}_sectors.json';assert not dst.exists();dst.write_text(json.dumps(exact,indent=2)+'\n')
 row={'candidate':name,'source':inp,'all_18_poisson_equations_exact':True,'all_retained_exponents_distinct':True,'first_nonzero_sector':list(first),'first_exponent_exact':str(qs),'excluded_weight_upper_exact':str(threshold),'first_residual_angular_norm':norms[first].str(80),'nonzero_sector_set':[list(k) for k in nz],'nonzero_first_descendant_density_set':[list(k) for k in dnz],'peer_comparisons':comparisons,'exact_data_sha256':sha(dst),'seconds':time.monotonic()-localstart}
 results.append(row);print(name,first,'threshold',float(threshold),'norm',norms[first].str(20),'seconds',row['seconds'],flush=True)
common={name:pr==allprofiles['007'] for name,pr in allprofiles.items()}
for name in ['d2','Mpen2','005','007','013','014']:assert common[name],name
assert not common['state131']
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in [B/'PROOF.md',Path(__file__),B/'data/inputs.json',B/'source/T2_result.json',B/'source/T2_REVIEW_T4_249.md',B/'source/T2_REVIEW_T4_234.md']},'rows':results,'first_four_profiles_equal_to_007':common,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED five T2 candidate tail tests and common affine-class assertion; additional listed exact candidate computations require numerical peer acceptance'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('DONE',out['utc'],out['elapsed_seconds'],common,flush=True)
