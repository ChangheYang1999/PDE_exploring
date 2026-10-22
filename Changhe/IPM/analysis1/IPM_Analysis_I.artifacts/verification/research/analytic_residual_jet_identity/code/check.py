from pathlib import Path
from datetime import datetime,timezone
from types import SimpleNamespace
from math import comb
from flint import fmpq
import ast,hashlib,json,numpy as np,random,struct,time
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'sources/xnorm_jets.py').read_text();tree=ast.parse(text)
node=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='eps_mode_jets'];assert len(node)==1
namespace={'np':np,'comb':comb};exec(compile(ast.Module(body=node,type_ignores=[]),'<pinned eps_mode_jets>','exec'),namespace)
producer=namespace['eps_mode_jets']
def exact_float(x):
 bits=int.from_bytes(struct.pack('>d',float(x)),'big');s=bits>>63;e=(bits>>52)&2047;m=bits&((1<<52)-1);assert e<2047
 v=m if e==0 else m+(1<<52);q=-1074 if e==0 else e-1075;v=-v if s else v
 return fmpq(v<<max(q,0),1<<max(-q,0))
def laurent(R,S,c):
 # R and S contain integer derivative data; twice the imaginary Laurent
 # coefficient of a positive sine mode is minus its real amplitude.
 M=len(R[0])-1;out=[];P=[];nprod=0;largest=0
 for order in range(3):
  dic={}
  for a in range(order+1):
   b=order-a;choose=comb(order,a)
   for n in range(1,M+2):
    for j in range(M+1):
     x=int(S[a][n-1])*int(R[b+1][j]);y=int(S[a+1][n-1])*int(R[b][j])
     if not x and not y:continue
     for sp in (-1,1):
      p=sp*2*n
      for sq in (-1,1):
       q=sq*(2*j+1);k=p+q
       # Four times the imaginary product coefficient.
       value=choose*sp*sq*(p*x-q*y)
       dic[k]=dic.get(k,0)+value;nprod+=1;largest=max(largest,abs(dic[k]))
  assert all(dic.get(-k,0)==-v for k,v in dic.items())
  P.append([fmpq(-dic.get(2*j+1,0),2) for j in range(2*M+3)])
 for i in range(3):
  v=[sum((fmpq(comb(i,l)*(-2)**(i-l))*P[l][j] for l in range(i+1)),fmpq(0)) for j in range(2*M+3)]
  for j in range(M+1):v[j]+=c*int(R[i+1][j])-int(R[i][j])
  out.append(v)
 return out,nprod,largest
rng=random.Random(2026102119);records=[];comparisons=0;products=0;max_integer=0
start=time.monotonic()
input_records=[]
for M in [0,1,3,16,260]:
 R=np.array([[[rng.randrange(-5,6) for j in range(M+1)] for t in range(3)] for a in range(4)],dtype=np.int64)
 S=np.array([[[2*rng.randrange(-5,6) for j in range(M+1)] for t in range(3)] for a in range(4)],dtype=np.int64)
 input_records.append({'M':M,'R':R.tolist(),'PSI':S.tolist(),'t':['0','0','0'],'c':'3/4'})
 G=SimpleNamespace(M=M,n=np.arange(1,M+2),Nf=M+1,c_l=0.75)
 exact=[]
 for t in range(3):
  v,n,b=laurent(R[:,t,:],S[:,t,:],fmpq(3,4));exact.append(v);products+=n;max_integer=max(max_integer,b)
 for K in range(3):
  actual=producer(G,{'t':np.zeros(3),'R':list(R),'PSI':list(S)},K)
  assert actual.shape==(K+1,3,2*M+3)
  for i in range(K+1):
   for t in range(3):
    for j in range(2*M+3):assert exact_float(actual[i,t,j])==exact[t][i][j];comparisons+=1
  assert np.all(actual[:,:,-1]==0)
 records.append({'M':M,'radii':3,'orders':[0,1,2]})
# Complete bilinear basis-pair comparisons at M0 and M1, including derivative
# slots that cannot enter a derivative of order <=2.
basis_pairs=0;basis_entries=0
for M in [0,1]:
 for ar in range(4):
  for jr in range(M+1):
   for ap in range(4):
    for npidx in range(M+1):
     R=np.zeros((4,1,M+1),dtype=np.int64);S=np.zeros_like(R);R[ar,0,jr]=1;S[ap,0,npidx]=2
     G=SimpleNamespace(M=M,n=np.arange(1,M+2),Nf=M+1,c_l=0.)
     exact,n,b=laurent(R[:,0,:],S[:,0,:],fmpq(0));actual=producer(G,{'t':np.zeros(1),'R':list(R),'PSI':list(S)},2)
     for i in range(3):
      for j in range(2*M+3):assert exact_float(actual[i,0,j])==exact[i][j];basis_entries+=1
     basis_pairs+=1
# Coarse a priori dyadic bound for the synthetic source computations:
# |R|<=5, |psi|<=10, |n|<=261, |q|<=521, l<=2, sum binom<=4.
# At most 2*261 contributions per output bin in each A or B scatter.
# This generous bound includes c rho'-rho and exponential product rule.
coarse_bound=4*8*522*4*(261*10*5+521*10*5)+10
assert coarse_bound<2**40 and max_integer<coarse_bound
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_LAURENT_VERSUS_SOURCE_JETS','synthetic_cases':records,'dense_comparisons':comparisons,'laurent_product_contributions':products,'largest_dense_laurent_accumulator':max_integer,'coarse_source_absolute_bound':coarse_bound,'basis_pairs':basis_pairs,'basis_entries':basis_entries,'no_tolerance':True,'source_sha256':hashlib.sha256(text.encode()).hexdigest(),'seconds':time.monotonic()-start,'scope':'Algebra tests with exact synthetic jets only, no trial or quadrature computation.'}
(ROOT/'data_exact/synthetic_jets.json').write_text(json.dumps({'seed':2026102119,'records':input_records},indent=2)+'\n')
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
