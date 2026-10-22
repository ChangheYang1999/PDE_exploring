"""Exact endpoint regularity audit, independent implementations and input decoders."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
import json,hashlib,math,sys,bisect
from flint import fmpq as Q,fmpq_poly as Poly,fmpq_mat as Mat,ctx
assert not sys.flags.optimize
ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/modal_annular_regularity';E=D/'evidence'
now=lambda:datetime.now(timezone.utc).isoformat()
start=now();counts=Counter();pins={};digest=hashlib.sha256();records=[]
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def pin(p,h=None):
 p=Path(p);p=p if p.is_absolute() else B/p;n=str(p.relative_to(B)) if p.is_relative_to(B) else str(p);a=sha(p)
 assert h is None or a==h,n
 assert n not in pins or pins[n]==a,n
 pins[n]=a

def manual(s):
 sign=-1 if s.startswith('-') else 1;s=s.lstrip('+-');mant,exp=s.split('p');assert mant.startswith('0x');parts=mant[2:].split('.')
 assert len(parts)==2;num=int(parts[0]+parts[1],16);power=int(exp)-4*len(parts[1])
 return Q(sign*num)*Q(2)**power

def af(s):return F.from_float(float.fromhex(s))
def aq(f):return Q(f.numerator,f.denominator)
def equal(f,q,label):
 assert aq(f)==q,label
 digest.update((str(label)+'='+str(f)+'\n').encode())
 counts['exact_cross_method_equalities']+=1

inp=B/'data_exact/modal_v2.json';pin(inp,'57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6')
x=json.loads(inp.read_text());ar=x['arrays'];p=x['degree'];M,nb=ar['S']['shape'];assert p==7 and M==260 and nb==1565
assert ar['knots']['shape']==[nb+8]
for name,shape in [('S',[M,nb]),('D',[M,7]),('Ei',[M,7]),('Eo',[M,7]),('Aout',[M,10])]:
 assert ar[name]['shape']==shape and len(ar[name]['hex'])==math.prod(shape)
 counts['array_shape_checks']+=1
T=[af(v) for v in ar['knots']['hex']];K=[manual(v) for v in ar['knots']['hex']]
for i,(t,k) in enumerate(zip(T,K)):equal(t,k,('knot',i))
assert len(T)==1573 and T[:8]==[T[0]]*8 and T[-8:]==[T[-1]]*8
assert K[:8]==[K[0]]*8 and K[-8:]==[K[-1]]*8
assert all(T[i]<T[i+1] and K[i]<K[i+1] for i in range(7,nb))
counts['distinct_nonempty_spans']=len(set(T))-1;counts['simple_interior_knots']=len(set(T))-2
assert counts['distinct_nonempty_spans']==1558 and counts['simple_interior_knots']==1557
s={k:af(v) for k,v in x['scalars_hex'].items()};q={k:manual(v) for k,v in x['scalars_hex'].items()}
for k in s:equal(s[k],q[k],('scalar',k))
assert 0<s['k']<F(1,2) and s['bi']>4 and s['bo']>4-2*s['k']
assert q['k']>0 and q['k']<Q(1,2) and q['bi']>4 and q['bo']>4-2*q['k']
pairs=x['outer_jl'];assert pairs[0]==[0,0] and len(pairs)==10 and len(set(map(tuple,pairs)))==10
assert all(type(j) is int and type(l) is int and j>=0 and l>=0 for j,l in pairs)
a=[s['k']-3-j*(1-s['k'])-2*l for j,l in pairs];b=[q['k']-3-j*(1-q['k'])-2*l for j,l in pairs]
for j in range(10):equal(a[j],b[j],('alpha',j));assert a[j]<-2 and b[j]<-2
for n in range(1,262):
 m=2*n
 assert m+4>0 and m+4+s['bi']>0 and all(m-4-z>0 for z in a) and m-4+s['bo']>0
 assert Q(m+4)+q['bi']>0 and all(Q(m-4)-z>0 for z in b) and Q(m-4)+q['bo']>0
 counts['all_mode_tail_rate_checks']+=1

def getA(name,m,i):return af(ar[name]['hex'][m*ar[name]['shape'][1]+i])
def getB(name,m,i):return manual(ar[name]['hex'][m*ar[name]['shape'][1]+i])

def endpointA(c,t,right):
 out=[]
 for degree in range(7,0,-1):
  out.append(c[-1] if right else c[0])
  ds=[t[i+degree+1]-t[i+1] for i in range(len(c)-1)];assert all(v>0 for v in ds)
  c=[degree*(c[i+1]-c[i])/ds[i] for i in range(len(c)-1)];t=t[1:-1]
 return out

def basisB(span,anchor):
 # Polynomial Cox recurrence in the signed coordinate t-anchor.
 polys={span:Poly([1])}
 for degree in range(1,8):
  nxt={}
  for i in range(span-degree,span+1):
   z=Poly()
   den=K[i+degree]-K[i]
   if den and i in polys:z+=Poly([anchor-K[i],1])*polys[i]/den
   den=K[i+degree+1]-K[i+1]
   if den and i+1 in polys:z+=Poly([K[i+degree+1]-anchor,-1])*polys[i+1]/den
   nxt[i]=z
  polys=nxt
 assert sum(polys.values(),Poly())==Poly([1])
 return Mat([[polys[i][j] for i in range(span-7,span+1)] for j in range(8)])

for right in [False,True]:
 span=nb-1 if right else 7;anchor=K[-1] if right else K[0]
 source=Mat([[getB('S',m,i) for m in range(M)] for i in range(span-7,span+1)])
 pol=basisB(span,anchor)*source
 beta=s['bo']*-1 if right else s['bi'];betab=q['bo']*-1 if right else q['bi']
 for m in range(M):
  co=[getA('S',m,i) for i in range(span-7,span+1)]
  for i in range(8):equal(co[i],source[i,m],('source',right,m,i))
  jets=endpointA(co,T[-16:] if right else T[:16],right)
  jetsb=[pol[n,m]*math.factorial(n) for n in range(7)]
  for n in range(7):equal(jets[n],jetsb[n],('endpoint',right,m,n))
  power=[];powerb=[]
  for n in range(7):
   if right:
    power.append(sum((getA('Aout',m,j)*a[j]**n for j in range(10)),F(0)))
    powerb.append(sum((getB('Aout',m,j)*b[j]**n for j in range(10)),Q(0)))
   else:
    power.append(sum((getA('D',m,j)*(2*j+2)**n for j in range(7)),F(int(m==0 and n==0))))
    powerb.append(sum((getB('D',m,j)*Q(2*j+2)**n for j in range(7)),Q(int(m==0 and n==0))))
   equal(power[-1],powerb[-1],('uncorrected',right,m,n))
  cor=[];corb=[]
  for n in range(7):
   v=sum(((-beta)**(n-j)*(jets[j]-power[j])/math.factorial(n-j)/math.factorial(j) for j in range(n+1)),F(0));cor.append(v)
   z=(jetsb[n]-powerb[n]-sum((Q(math.factorial(n),math.factorial(n-i))*betab**(n-i)*corb[i] for i in range(n)),Q(0)))/math.factorial(n);corb.append(z)
   equal(v,z,('correction',right,m,n))
  for n in range(7):
   recovered=power[n]+sum((F(math.factorial(n),math.factorial(n-i))*beta**(n-i)*cor[i] for i in range(n+1)),F(0))
   recoveredb=powerb[n]+sum((Q(math.factorial(n),math.factorial(n-i))*betab**(n-i)*corb[i] for i in range(n+1)),Q(0))
   assert recovered==jets[n] and recoveredb==jetsb[n];equal(recovered,recoveredb,('recovered',right,m,n));counts['exact_matching_equations_per_method']+=1
  if m in [0,1,2,129,259]:records.append({'side':'outer' if right else 'inner','mode':m,'jets':[str(z) for z in jets],'corrections':[str(z) for z in cor]})

# All seven zero jets of the exact normalization correction, independent finite sums.
for n in range(7):
 z=a[0]**n-sum((F(math.comb(n,j))*(-s['bo'])**(n-j)*(a[0]+s['bo'])**j for j in range(n+1)),F(0))
 poly=Poly([b[0]**i/math.factorial(i) for i in range(7)])
 expminus=Poly([(-q['bo'])**i/math.factorial(i) for i in range(7)])
 trunc=Poly([(b[0]+q['bo'])**i/math.factorial(i) for i in range(7)])
 zz=(poly-expminus*trunc)[n]*math.factorial(n)
 assert z==0 and zz==0;equal(z,zz,('normalization_zero_jet',n));counts['normalization_zero_jets']=n+1

# Signed sine product versus the collected sparse density conversion for each input basis mode.
for mode in range(M):
 scatter=[F(0)]*262
 for freq in [1+2*mode,1-2*mode,3+2*mode,3-2*mode]:scatter[(abs(freq)-1)//2]+=F(1 if freq>0 else -1,8)
 def v(i):return Q(int(i==mode)) if 0<=i<M else Q(0)
 collected=[(2*v(0)-v(2))/8,(2*v(0)+v(1)-v(2)-v(3))/8]+[(v(j-1)+v(j)-v(j+1)-v(j+2))/8 for j in range(2,262)]
 for j in range(262):equal(scatter[j],collected[j],('angular',mode,j))
 assert scatter[261]==0 and collected[261]==0
 counts['angular_basis_modes']=mode+1

prior=json.loads((B/'research/modal_repair/evidence/audit_verdict.json').read_text());assert prior['verdict']=='CONFIRMED'
for n,h in prior['source_and_evidence_sha256'].items():pin(n,h)
pin(B/'research/modal_repair/evidence/audit_verdict.json')
comp=json.loads((B/'research/coherent_derivative_norm_composition/evidence/verdict.json').read_text())
for n,h in comp['files'].items():pin(n,h)
pin(B/'research/coherent_derivative_norm_composition/evidence/verdict.json')
for p in [D/'PROOF.md',D/'SPLINE_DERIVATIVE_DETAILS.md',E/'proof_first.json',Path(__file__)]:pin(p)
out={'start_utc':start,'utc':now(),'status':'PASS_EXACT_MODAL_ENDPOINTS_AND_ANNULAR_REGULARITY_PREMISES','counts':dict(counts),'comparison_stream_sha256':digest.hexdigest(),'selected_endpoint_records':records,'scope':'Exact repaired trial joins and finite annular regularity only. No I/J archive values, physical W bounds, norm size, centre upgrade, inverse or IPM endpoint.','files':pins}
with (E/'checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['start_utc','utc','status','counts']}),flush=True)
