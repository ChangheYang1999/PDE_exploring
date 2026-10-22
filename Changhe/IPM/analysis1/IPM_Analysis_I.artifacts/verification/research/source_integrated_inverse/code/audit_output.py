"""Third exact integration and independent factorized fresh scalar audit."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
import hashlib,json,math,sys
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_integrated_inverse';E=D/'evidence';ctx.prec=1536;iv.dps=250

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def multiply(p,q):
 v=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):v[i+j]+=a*b
 return v
def ev(p,x):return sum((a*x**j for j,a in enumerate(p)),F())
def derivative(p):return [F(j)*p[j] for j in range(1,len(p))] or [F(0)]
def compose(p,offset,slope):
 v=[F(0)]*len(p)
 for j,a in enumerate(p):
  for k in range(j+1):v[k]+=a*math.comb(j,k)*offset**(j-k)*slope**k
 return v
def clean(p):
 while len(p)>1 and not p[-1]:p.pop()
 return p

def third_geometry(data,counts):
 nodes=[F(j,18) for j in range(19)];weights=[]
 for i,t in enumerate(nodes):
  p=[F(1)];den=F(1)
  for j,u in enumerate(nodes):
   if i!=j:p=multiply(p,[-u,F(1)]);den*=t-u
  weights.append(sum((v/F(k+1) for k,v in enumerate(p)),F())/den)
 for j in range(19):assert sum((w*t**j for w,t in zip(weights,nodes)),F())==F(1,j+1);counts['exact_quadrature_moment_checks']+=1
 def tensor(q,j,v):
  total=F(0);parity=j%2
  for by in range(0,j+1,2):
   value=F(0)
   for n,c in enumerate(q):
    if n<by//2 or 2*n<j:continue
    factor=F(math.comb(n,by//2)*math.factorial(by)*math.factorial(2*n-by),math.factorial(2*n-j))
    value+=c*factor*v**(n-(j+parity)//2)
   total+=math.comb(j,by)*v**parity*value*value
  return total
 C=[[F(0)]*3 for _ in range(5)];a=F(273,64);S=[F(0)]*4+[F(35),F(-84),F(70),F(-20)]
 qtau=[]
 for piece in data['pieces']:
  lo,hi=F(piece['left']),F(piece['right']);q=list(map(F,piece['Q_coefficients']));qtau.append(compose(q,4,a))
  assert len(q)<=9 and hi>lo
  for j in range(5):
   for d in range(3):
    assert 2*(len(q)-1)-j+d<=18
    val=(hi-lo)*sum((w*(lo+(hi-lo)*t)**d*tensor(q,j,lo+(hi-lo)*t) for w,t in zip(weights,nodes)),F())
    assert val==F(piece['integrals'][j][d]) and val>=0;C[j][d]+=val;counts['third_exact_piece_integrals']+=1
 # Derivatives in tau reproduce exactly the old cutoff's -b on all pieces.
 minusb=[[F(0)],[-F(4,3)*x for x in compose(S,0,4)],[-F(4,3)],[-F(4,3)*x for x in compose(S,4,-4)]]
 for q,b in zip(qtau,minusb):assert clean(derivative(q))==clean(b);counts['same_cutoff_derivative_identities']+=1
 assert C==[[F(v) for v in row] for row in data['radial_moments_exact']];counts['whole_radial_moment_equalities']=15
 return C

def fa(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def fi(t):s,m,e,_=t;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 if isinstance(x,arb):assert x.is_finite();return fa(x.lower()),fa(x.upper())
 return fi(x._mpi_[0]),fi(x._mpi_[1])
def qa(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def qi(v):v=F(v);return iv.mpf(v.numerator)/v.denominator

def fresh(C,data,eng,counts):
 Q=qa if eng=='arb' else qi;pi=arb.pi() if eng=='arb' else iv.pi
 sqrt=(lambda z:z.sqrt()) if eng=='arb' else iv.sqrt
 log=(lambda z:z.log()) if eng=='arb' else iv.ln
 exp=(lambda z:z.exp()) if eng=='arb' else iv.exp
 delta=F(33,2000);MV=F(743,2500);MR=F(5059,10000)
 bases=[[(MV/2,2),(MV,1),(MV,0),(F(6376),0),(F(87933),0)],[(MR,1),(MR,0),(F(505),0),(F(24381),0),(F(3758450),0)]]
 ss=[]
 for base in bases:
  ss.append([sum((Q(math.comb(j,k)*b*delta**(d+k))*sqrt(Q(C[j-k][d])) for k,(b,d) in enumerate(base[:j+1])),Q(0)) for j in range(5)])
 def inside(v,old):
  l,h=ends(v);a,b=map(F,old);assert 0<a<=l<=h<=b,(eng,float(l),float(a),float(h),float(b));counts[eng+'_fresh_scalar_containments']+=1
 for i in range(2):
  for j in range(5):inside(sqrt(pi)*Q(delta**(1-j))*ss[i][j],data['results'][eng]['physical_L2_derivative_bounds'][i][j])
 aa=lambda s:1/(2*sqrt(pi*Q(s-1)))
 bb=lambda s:1/(2*sqrt(pi*Q((s-1)*(s-2))))
 pow2=lambda x:exp(Q(x)*log(Q(2)))
 def margins(s):return F(1301,200)-F(101,100)*s-delta*((12*s+F(9,2))*MV+3*MR),(101*s-1)/100
 cache={}
 for ell in map(F,data['scales_exact']):
  uv=[]
  for i in range(2):
   uv.append([sqrt(pi)*Q(delta/ell**(2 if i==0 else 1))*sqrt(sum((Q(math.comb(m,j)*(ell/delta)**(2*j))*ss[i][j]*ss[i][j] for j in range(m+1)),Q(0))) for m in (3,4)])
  cache[ell]=uv
 def row(s,ell,uniform=False):
  (w3,w4),(q3,q4)=cache[ell];sp=F(31,10);sm=F(61,20);order=sp if uniform else s
  wi=exp(Q(4-order)*log(w3)+Q(order-3)*log(w4));qi0=exp(Q(4-order)*log(q3)+Q(order-3)*log(q4))
  corder=sm if uniform else s
  rr=sqrt(Q(2))*Q(order*(order-1))*pow2(order-4)*(aa(F(2))*w4+bb(corder-1)*wi)+sqrt(Q(2))*Q(order)*pow2(order-2)*(aa(F(2))*q3+aa(corder-1)*qi0)
  am,dm=(margins(sp)[0],margins(sm)[1]) if uniform else margins(s)
  nn=exp(Q(order)*log(1+rr/Q(dm)))/Q(am);hh=exp(-Q(order)*log(Q(ell)))*nn
  return {'W3':w3,'W4':w4,'Q3':q3,'Q4':q4,'Ws':wi,'Qs':qi0,'R':rr,'N_inverse':nn,'H_inverse':hh},am,dm
 assert len(data['results'][eng]['rows'])==243 and len(data['results'][eng]['uniform'])==81
 seen=set()
 for old in data['results'][eng]['rows']:
  s,ell=F(old['s']),F(old['ell']);assert (s,ell) not in seen;seen.add((s,ell));vals,am,dm=row(s,ell)
  assert am==F(old['a_lower']) and dm==F(old['d_lower']) and min(am,dm)>0
  for k,v in vals.items():inside(v,old['bounds'][k])
 assert seen=={(s,e) for s in map(F,('61/20','153/50','31/10')) for e in cache}
 for old in data['results'][eng]['uniform']:
  vals,am,dm=row(F(31,10),F(old['ell']),True);assert am==F(old['a_lower']) and dm==F(old['d_lower']) and min(am,dm)>0
  for key in ('R','N_inverse','H_inverse'):inside(vals[key],old['bounds'][key])

def main():
 data=json.loads((E/'checks.json').read_text());assert data['status']=='PASS_INTEGRATED_CUTOFF_AUXILIARY_INVERSE';counts=Counter();files={}
 for f,h in data['files'].items():assert sha(B/f)==h,f;files[f]=h;counts['producer_pin_checks']+=1
 assert data['scales_exact']==list(map(str,sorted(set([F(1)]+[F(j,4000) for j in range(1,81)]))))
 C=third_geometry(data,counts)
 for eng in ('arb','iv'):fresh(C,data,eng,counts)
 # Strict ceilings for the full publication, checked on exact stored upper endpoints.
 named=[('61/20','1/500','N_inverse','608'),('153/50','1/500','N_inverse','554'),('31/10','1/500','N_inverse','473'),('153/50','3/1000','H_inverse','5.743e10'),('31/10','11/4000','H_inverse','6.968e10'),('31/10','33/2000','R','679.382'),('31/10','33/2000','N_inverse','5.7e6'),('31/10','7/2000','R','48.225'),('31/10','7/2000','N_inverse','1874'),('31/10','1/500','R','29.812')]
 for eng in ('arb','iv'):
  for s,e,k,cap in named:
   row=next(r for r in data['results'][eng]['rows'] if r['s']==s and r['ell']==e);assert F(row['bounds'][k][1])<F(cap);counts['published_named_strict_ceilings']+=1
  for e,k,cap in [('1/500','N_inverse','922'),('3/1000','H_inverse','1.223e11')]:
   row=next(r for r in data['results'][eng]['uniform'] if r['ell']==e);assert F(row['bounds'][k][1])<F(cap);counts['published_uniform_strict_ceilings']+=1
 for s,best in data['best_of_81_scales'].items():
  for key,row in best.items():
   values={}
   for eng in ('arb','iv'):
    for r in (data['results'][eng]['uniform'] if s=='uniform' else [z for z in data['results'][eng]['rows'] if z['s']==s]):values[r['ell']]=max(values.get(r['ell'],F(0)),F(r['bounds'][key][1]))
   assert values[row['ell']]==min(values.values())==F(row['upper_exact'])<F(row['integer_strict_ceiling']);counts['best_upper_bound_checks']+=1
 for p in [E/'checks.json',E/'review_summary.json',D/'ADDENDUM.md',D/'AUDIT_METHOD.md',D/'PUBLICATION.md',Path(__file__)]:files[str(p.relative_to(B))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_THIRD_EXACT_QUADRATURE_AND_FRESH_OUTPUT_AUDIT','counts':dict(counts),'files':files,'scope':'Complete exact integration and scalar output audit for same95cutoff. No new canonical Green integration or physical rank-one inverse.'}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
if __name__=='__main__':main()
