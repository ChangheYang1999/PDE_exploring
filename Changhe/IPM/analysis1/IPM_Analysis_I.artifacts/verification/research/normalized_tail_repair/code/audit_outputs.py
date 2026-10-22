"""Independent exact rational source, quotient, moments and directed output audit.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,math,time
from decimal import Decimal,localcontext
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
from mpmath import iv
import engine_arb as A,engine_iv as I
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/normalized_tail_repair';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def ends(b):lo,hi=F(b['lower_exact']),F(b['upper_exact']);assert lo<=hi;return lo,hi
def dec(s):
 neg=s.startswith('-');man,e=s.lstrip('+-').split('p');w,f=man[2:].split('.');z=F(int(w+f,16),16**len(f))*F(2)**int(e);return -z if neg else z
files={};counts={}
def pin(p,h=None):
 z=sha(p)
 if h is not None:assert z==h,str(p)
 files[str(p.relative_to(B))]=z

def main():
 start=time.monotonic();o=load(E/'checks.json');pf=load(E/'proof_first.json');assert o['status']=='COMPUTED_TWO_METHOD_NORMS_REQUIRES_EXACT_OUTPUT_AUDIT'
 assert pf['sha256']==sha(D/'PROOF.md') and datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(o['utc'])
 for p,h in o['files'].items():pin(B/p,h)
 for p in [E/'checks.json',Path(__file__)]:pin(p)
 public=load(D/'source/public_bounds.json');trans=load(D/'source/transition.json')
 data=load(B/'data_exact/modal_v2.json');ar=data['arrays'];archive=Path(o['outputs']['iv180']['source_archive']['path']);assert sha(archive)==o['outputs']['iv180']['source_archive']['sha256']
 with np.load(archive,allow_pickle=False) as z:
  for key,num in [('Aout',2600),('knots',1573)]:
   assert len(ar[key]['hex'])==num==z[key].size
   assert all(F(float(v))==dec(h) for v,h in zip(z[key].flat,ar[key]['hex'],strict=True));counts['original_'+key+'_entries']=num
  k=F(float(z['k']));L=F(float(z['L']));t=F(float(z['knots'][-1]));bo=F(float(z['bo']))
 assert 0<k<F(1,3);beta=2*k-1;b2=3*k-2;alpha=(3-k)/2
 assert -1<beta<-F(1,3) and b2<-1 and 2*beta-1<b2 and beta+1==2*k
 for eng in o['outputs'].values():assert eng['scalars']==dict(k=str(k),L=str(L),tplus=str(t),beta=str(beta),alpha=str(alpha))
 pairs=data['outer_jl'];assert pairs==[[j,0] for j in range(6)]+[[0,1],[1,1],[2,1],[0,2]]
 exps=[k-j*(1-k)-2*l for j,l in pairs]+[3-bo]
 assert exps[:2]==[k,beta] and all(v<=b2 for v in exps[2:])
 assert all((i==j==0 and v+w-1==beta) or ((i,j)!=(0,0) and v+w-1<=b2) for i,v in enumerate(exps) for j,w in enumerate(exps))
 assert all(v-2*n-2<b2 for v in exps for n in range(1,262))
 assert all((2*n)**2-4*k*k>0 and beta-2*n<-1 for n in range(1,523))
 counts['exterior_exponent_and_denominator_checks']=9+121+2871+1044
 # Independently construct each linear form by symbolic integer recurrence.
 # Vectors carry exact dependence on the 522 sine coefficients.
 M=520;mat=[[0]*522 for _ in range(M+3)];mat[M][M+1]=8
 for j in range(M,1,-1):
  mat[j-1]=[-x+y+z for x,y,z in zip(mat[j],mat[j+1],mat[j+2],strict=True)];mat[j-1][j]+=8
 mat[0]=[-x+y+z for x,y,z in zip(mat[1],mat[2],mat[3],strict=True)];mat[0][1]+=8
 assert all(x%2==0 for x in mat[0]);mat[0]=[x//2 for x in mat[0]];mat=mat[:M+1]
 symbolic=0
 for m,row in enumerate(mat):
  for j,weight in enumerate(row):
   d=j-m-1;want=(4 if m==0 else 8)*(-1 if d%2 else 1)*(d//2+1) if d>=0 else 0
   assert weight==want,(m,j);symbolic+=1
 counts['symbolic_recurrence_matrix_entries']=symbolic
 # One common dyadic denominator permits exact integer interval sums.
 runtime={};exact_q={};widths={}
 for name,mod in [('arb512',A),('iv180',I)]:
  run,qs=mod.evaluate();saved=o['outputs'][name]
  assert run==saved,'Deterministic replay differs from saved output'
  bs=[mod.box(x) for x in qs];assert hashlib.sha256(json.dumps(bs,sort_keys=True).encode()).hexdigest()==saved['raw_quotient_sha256']
  prior=load(B/saved['source']['path'])['residual_coefficients'];inputs=[ends(x['value']) for x in prior]
  den=max(x.denominator for pair in inputs for x in pair);assert den&(den-1)==0
  integer=[(int(lo*den),int(hi*den)) for lo,hi in inputs];assert all(F(x,den)==v for pair,pair2 in zip(integer,inputs,strict=True) for x,v in zip(pair,pair2,strict=True))
  exact=[]
  for m,row in enumerate(mat):
   lo=hi=0
   for w,(x,y) in zip(row,integer,strict=True):
    if w>=0:lo+=w*x;hi+=w*y
    else:lo+=w*y;hi+=w*x
   le,he=F(lo,den),F(hi,den);lb,hb=ends(bs[m]);assert lb<=le<=he<=hb,(name,m);exact.append((le,he))
  nlo=sum(F(0) if lo<=0<=hi else min(abs(lo),abs(hi)) for lo,hi in exact);nhi=sum(max(abs(lo),abs(hi)) for lo,hi in exact)
  lb,hb=ends(saved['values']['raw_N']);assert lb<=nlo<=nhi<=hb,(name,'raw_N')
  # Exact sin3 coefficient reconstruction from independently derived quotient.
  for w in saved['witnesses']:assert w['q_raw']==bs[w['m']]
  runtime[name]=saved;exact_q[name]=exact;counts[name+'_exact_quotient_enclosures']=len(exact)
  counts[name+'_exact_norm_enclosures']=1;counts[name+'_witnesses']=len(saved['witnesses'])
  widths[name]={key:str(ends(saved['values'][key])[1]-ends(saved['values'][key])[0]) for key in ('raw_N','N','I_H','C')}
  for key,(lo,hi) in public['strict_intervals'].items():
   x,y=ends(saved['values'][key]);assert F(lo)<x<=y<F(hi),(name,key)
  assert ends(saved['values']['N'])[1]<F(public['N_upper'])
  assert max(map(abs,ends(saved['values']['I_H'])))<F(public['I_abs_upper'])
  assert 0<ends(saved['values']['C_from_public_N_I'])[0]<=ends(saved['values']['C_from_public_N_I'])[1]<F(public['C_upper'])
 counts['strict_public_claims']=16
 # Independent expansion by repeated exact convolution, not binomial coefficients.
 co=[1]
 for _ in range(8):
  nxt=[0]*(len(co)+2)
  for j,x in enumerate(co):nxt[j]+=-2*x;nxt[j+1]+=3*x;nxt[j+2]-=x
  co=nxt
 assert list(map(int,trans['coefficients_low_to_high']))==co
 def at(coeff,x):return sum(F(c)*x**j for j,c in enumerate(coeff))
 der=co[:]
 for order in range(8):
  assert at(der,F(1))==at(der,F(2))==0;der=[j*x for j,x in enumerate(der)][1:]
 def moment(n):return sum(F(c,j+n+1)*(2**(j+n+1)-1) for j,c in enumerate(co))
 BB=moment(0);JB=moment(1);assert BB==F(trans['B'])==F(math.factorial(8)**2,math.factorial(17))>0
 assert JB==F(trans['J_b'])==3*BB/2 and at(co,F(3,2))==F(trans['bmax'])==F(1,2**16)
 # Symmetry coefficients under s -> 3-s, independent exact binomial transform.
 sym=[sum(co[j]*math.comb(j,i)*3**(j-i)*(-1)**i for j in range(i,17)) for i in range(17)]
 assert sym==co
 assert all(j+beta!=0 for j in range(17))
 counts['transition_exact_checks']=17+16+3+17+17
 # Independent moment kernel angular factor via a rational recurrence for
 # normalized even sine/cosine moments, with total mass2.
 def ang(a,b):
  v=F(2)
  for j in range(1,a+1):v*=F(2*j-1,2*j)
  for j in range(1,b+1):v*=F(2*j-1,2*(a+j))
  return v
 assert 3*ang(2,1)-ang(1,2)==F(1,4)
 counts['exact_strain_angular_factor']=1
 # Evaluate only the certified C ceiling in the displayed T-cost examples.
 ctx.prec=768;ctx.threads=1;iv.dps=200;rows=[]
 assert public['T_powers']==trans['example_T_powers_of_10']
 def ra(v):v=F(v);return arb(v.numerator)/v.denominator
 def ri(v):v=F(v);return iv.mpf(v.numerator)/v.denominator
 for p in public['T_powers']:
  T=10**p;assert T>=max(L,1);assert ra(t).exp()<ra(T)
  ca=ra(public['C_upper'])*(ra(k-1)*ra(T).log()).exp();ci=ri(public['C_upper'])/iv.power(ri(T),ri(1-k))
  ba,bi=A.box(ca),I.box(ci);la,ha=ends(ba);li,hi=ends(bi);assert max(la,li)<=min(ha,hi)
  scale=10**(p+8);up=F(max(ha,hi).numerator*scale//max(ha,hi).denominator+1,scale);assert ha<up and hi<up
  with localcontext() as dc:
   dc.prec=100;updecimal=str(Decimal(up.numerator)/Decimal(up.denominator))
  assert F(updecimal)==up
  rows.append({'T':str(T),'arb768':ba,'iv200':bi,'cost_strict_upper_exact':str(up),'cost_strict_upper_decimal':updecimal})
 counts['two_method_cost_examples']=len(rows)
 for p in [D/'source/transition.json',D/'source/public_bounds.json']:pin(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_RATIONAL_QUOTIENT_SOURCE_MOMENTS_AND_OUTPUT_AUDIT','counts':counts,'files':dict(sorted(files.items())),'source_archive':o['outputs']['iv180']['source_archive'],'public_bounds':public,'cost_examples':rows,'widths_exact':widths,'seconds':time.monotonic()-start,'scope':'Collected quotient and Laurent division independently enclose all521 coefficients. Exact symbolic map/source/moment audit and two directed public cost bounds. Overlaps/remainders are diagnostics. No residual norm ceiling, source control, stationarity or decisive endpoint.'}
 (E/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','counts','seconds')}));print(json.dumps([{'T':r['T'],'cost_strict_upper_exact':r['cost_strict_upper_exact']} for r in rows]))
if __name__=='__main__':main()
