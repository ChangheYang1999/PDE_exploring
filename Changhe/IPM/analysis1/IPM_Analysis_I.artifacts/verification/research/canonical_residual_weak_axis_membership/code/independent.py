from pathlib import Path
from fractions import Fraction as F
import sys,os,time,json
sys.dont_write_bytecode=True
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from flint import fmpq
from mpmath import iv
iv.dps=150
R=Path(__file__).resolve().parents[3];D=R/'research/canonical_residual_weak_axis_membership';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();clock=time.monotonic();A=p.load(E/'check.json');assert A['proof_sha256']==p.sha(D/'PROOF.md')=='b13a5c23f5deb1779caaca192324f98f3565627aa86fe29ba08a7a547a2f33d3';assert A['code_sha256']==p.sha(D/'code/check.py');p.rehash(A['parent_files'])
path=R/'data_exact/modal_v2.json';assert p.sha(path)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';raw=p.load(path)
def hx(t):
 sign=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,e=t.split('p');a,b=m[2:].split('.');return fmpq(sign*int(a+b,16))*fmpq(2)**(int(e)-4*len(b))
k,bi,bo=[hx(raw['scalars_hex'][n]) for n in ['k','bi','bo']];tb=hx(raw['arrays']['knots']['hex'][-1]);gamma=k-(1-k);ae=1+k
assert raw['arrays']['Aout']['shape']==[260,10] and raw['outer_jl']==[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[0,1],[1,1],[2,1],[0,2]]
beta=[]
for j,l in raw['outer_jl']:
 v=k
 for _ in range(j):v-=1-k
 for _ in range(l):v-=2
 beta.append(v)
beta.append(3-bo);assert list(map(str,beta))==A['beta'] and 0<k<fmpq(1,2) and bi>50 and bo>120
lg=[];pg=[];tg=[];linear_sources=[];product_sources=[]
for i,b in enumerate(beta):
 if b==gamma:linear_sources.append(i)
 if i not in [0,1]:lg.append(gamma-b)
 for j,c in enumerate(beta):
  gap=gamma+1-b-c
  if gap==0:product_sources.append([i,j])
  else:assert gap>0;pg.append(gap)
 for n in range(1,262):tg.append(gamma-b+2*n+2)
assert linear_sources==[1] and product_sources==[[0,0]] and min(lg)>0 and min(tg)>0
# Direct reconstruction from the hexadecimal raw cosine vectors.
d=[[fmpq(0),fmpq(0)] for _ in range(262)];d1=[[fmpq(0),fmpq(0)] for _ in range(262)]
for mode in range(260):
 a0=hx(raw['arrays']['Aout']['hex'][10*mode]);a1=hx(raw['arrays']['Aout']['hex'][10*mode+1])
 # Product sin1+sin3 with cos(2 mode), divided by4, then product-to-sum.
 for base in [1,3]:
  for direction in [-1,1]:
   freq=base+direction*2*mode;sg=1 if freq>0 else -1;j=(abs(freq)-1)//2;w=fmpq(sg,8)
   d[j][0]+=w*a0;d[j][1]+=w*(mode==0);d1[j][0]+=w*a1
assert [[str(v) for v in row] for row in d]==A['projection_d'];assert [[str(v) for v in row] for row in d1]==A['projection_d1'];assert d[-1]==d1[-1]==[0,0]
zpath=R/'research/modal_repair/evidence/independent_gauss_iv.json';assert p.sha(zpath)=='0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a';zz=p.load(zpath)['values']['A00_correction'];zlo,zhi=[fmpq(zz[n]) for n in ['lower_exact_dyadic','upper_exact_dyadic']];assert list(map(str,[zlo,zhi]))==A['normalization_interval']
def V(q):q=fmpq(q);return iv.mpf(int(q.p))/int(q.q)
z=iv.mpf([V(zlo).a,V(zhi).b]);ev=lambda pair:V(pair[0])+V(pair[1])*z
# Solve the radial Poisson coefficient as an affine exact rational pair first.
vel=[];den=[]
for n in range(1,262):
 m=2*n;dd=m*m-ae*ae;assert dd>0;den.append(dd);fn=[((ae-m)*d[n-1][i]+(ae+m)*d[n][i])/2 for i in range(2)];vel.append((ev([-m*x/dd for x in fn]),ev([ae*x/dd for x in fn])))
ds=[ev(row) for row in d];product=iv.mpf(0);pairs_seen=0;pairs_used=0;freq_contributions=0
for n,(v,w) in enumerate(vel,1):
 m=2*n
 for j in range(261):
  nu=2*j+1;cr=fmpq(0);ca=fmpq(0);pairs_seen+=1
  for freq in [nu+m,nu-m]:
   if abs(freq)==3:cr+=fmpq(1 if freq>0 else -1,2);freq_contributions+=1
  for freq in [m+nu,m-nu]:
   if abs(freq)==3:ca+=fmpq(1 if freq>0 else -1,2);freq_contributions+=1
  if cr or ca:product+=v*V(k)*ds[j]*V(cr)+w*nu*ds[j]*V(ca);pairs_used+=1
rr=iv.exp(V(tb));linear=rr**3*V((k-1)/k)*ev(d1[1]);nonlinear=rr**5*product;e1=linear+nonlinear
# Separate sparse polynomial verification: variables x,y,l,c,a,a_x,a_y,v1,v2.
N=9
def const(c):return {(0,)*N:fmpq(c)} if c else {}
def var(i):q=[0]*N;q[i]=1;return {tuple(q):fmpq(1)}
def add(*rows):
 out={}
 for row in rows:
  for key,value in row.items():out[key]=out.get(key,fmpq(0))+value
 return {key:value for key,value in out.items() if value}
def neg(row):return {key:-value for key,value in row.items()}
def mul(a,b):
 out={}
 for i,x in a.items():
  for j,y in b.items():
   key=tuple(ii+jj for ii,jj in zip(i,j));out[key]=out.get(key,fmpq(0))+x*y
 return {key:value for key,value in out.items() if value}
def prod(*factors):
 ans=const(1)
 for f in factors:ans=mul(ans,f)
 return ans
def deriv(row,axis):
 out={}
 for key,c in row.items():
  if key[axis]:
   v=list(key);v[axis]-=1;out=add(out,{tuple(v):c*key[axis]})
  if key[4]:
   v=list(key);v[4]-=1;v[5+axis]+=1;out=add(out,{tuple(v):c*key[4]})
 return out
x,y,ell,cs,a,ax,ay,v1,v2=[var(i) for i in range(N)];rho=prod(x,x,y,a);vx=mul(x,add(ell,neg(cs),v1));vy=mul(y,add(ell,cs,v2));res=add(mul(vx,deriv(rho,0)),mul(vy,deriv(rho,1)),neg(rho));factor=add(mul(add(prod(const(3),ell),neg(cs),const(-1)),a),prod(add(ell,neg(cs)),x,ax),prod(add(ell,cs),y,ay),prod(v1,add(mul(const(2),a),mul(x,ax))),prod(v2,add(a,mul(y,ay))));assert res==prod(x,x,y,factor)
# Independent scalar substitutions of c=3ell-1, far homogeneity, shell measure.
assert 3/k-(3/k-1)-1==0 and (3/k-1)+(k-3)/k==0
assert tuple(fmpq(c,2) for c in [0,-2,-2,4])==(0,-1,-1,2) # Far shell (constant,b,q,k).
assert tuple([2*(-1)+1,-2,4])==(-1,-2,4) # Far lower radial integral exponent.
actual={'k':k,'bi':bi,'bo':bo,'tb':tb,'s':fmpq(153,50),'gamma':gamma,'minimum_weight':2*k,'maximum_weight':fmpq(5,2),'center_rate_infimum':6-fmpq(5,2)-fmpq(153,50),'minimum_stream_denominator':min(den),'minimum_other_linear_gap':min(lg),'minimum_other_particular_gap':min(pg),'minimum_transient_gap':min(tg)};assert {n:str(v) for n,v in actual.items()}==A['actual']
def end(t):sg,m,e,bc=t;assert bc>=0;return F((-1 if sg else 1)*int(m))*F(2)**int(e)
def out(v):
 lo,hi=map(end,v._mpi_);assert lo<=hi;return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(v)}
values={'leading_linear':out(linear),'leading_product':out(nonlinear),'e1':out(e1)};comparisons={}
for n,v in values.items():
 lo,hi=F(v['lower_exact']),F(v['upper_exact']);al,au=F(A[n]['lower_exact']),F(A[n]['upper_exact']);assert al<=lo<=hi<=au,n;comparisons[n]='INDEPENDENT_INTERVAL_FULLY_INSIDE_PRIMARY'
lo,hi=F(values['e1']['lower_exact']),F(values['e1']['upper_exact']);wl,wu=map(F,A['strict_window']);assert wl<lo<=hi<wu<0
result={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_HEX_FMPQ_DIRECT_POISSON_IV_TARGET_PROJECTION','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(A['parent_files']),'exact_parameters_compared':len(actual),'exact_projection_scalars_compared':1048,'exponents_compared':11,'candidate_pairs_scanned':pairs_seen,'contributing_pairs':pairs_used,'signed_frequency_contributions':freq_contributions,'iv_dps':iv.dps,'values':values,'comparisons':comparisons,'strict_window':A['strict_window'],'sparse_polynomial_factor_identity':True,'seconds':time.monotonic()-clock,'scope':'Raw exact data and one nonzero leading coefficient independently reconstructed. Shared analytic normalization enclosure and existing axis-Q theorem are dependencies. Sparse polynomial checks do not prove functional analysis.'};p.write(E/'independent.json',result);print(json.dumps(result))
