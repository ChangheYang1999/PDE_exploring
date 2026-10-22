"""Independent whole-inner-disk B5 enclosure from exact JSON and canonical moments."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,gzip,math,time,hashlib,resource,argparse
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3]
E=BASE/'research/inner_majorant/evidence'
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import import_ball,export_ball
PINS={'input':'57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6','archive':'c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648','manifest':'dcab8364db8cb915412063fa8c1d3c6056ea4dd74cec218be04692a5d5ab474d','transport':'6525060f436bf553f3b4a42e403ad2c27dc69d6a82a1460634995f95e755e3c3'}
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def frac(v):return F.from_float(float.fromhex(v))
def dyadic(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def out(x):
 assert x.is_finite()
 return {'ball':export_ball(x),'lower_exact':str(dyadic(x.lower())),'upper_exact':str(dyadic(x.upper())),'display':x.str(32)}
def shift(p,d):
 d=aa(d)
 return [sum((p[l]*math.comb(l,j)*d**(l-j) for l in range(j,len(p))),arb(0)) for j in range(len(p))]
def phi(zq,degree):
 zq=F(zq)
 if zq==0:return [aa(F(1,j+1)) for j in range(degree+1)]
 z=aa(zq)
 if abs(zq)<=F(1,2):
  # Entire series. The first omitted term bounds a geometric tail.
  K=120;terms=[arb(1)]
  for q in range(1,K+1):terms.append(terms[-1]*z/q)
  vals=[];qabs=aa(abs(zq))
  for j in range(degree+1):
   tail=qabs**(K+1)/math.factorial(K+1)/(K+j+2)/(1-qabs/(K+2))
   vals.append(sum((terms[q]/(q+j+1) for q in range(K+1)),arb(0))+arb(0,tail.upper()))
 else:
  ez=z.exp();vals=[z.expm1()/z]
  for j in range(1,degree+1):vals.append((ez-j*vals[-1])/z)
 assert all(v>0 and v.rel_accuracy_bits()>160 for v in vals)
 return vals
def integ(p,offset,length,rate):
 if length==0:return arb(0)
 ps=shift(p,offset);ph=phi(rate*length,len(p)-1);h=aa(length)
 return h*sum((c*h**j*ph[j] for j,c in enumerate(ps)),arb(0))
def jets_left(c,kn):
 ans=[]
 for p in range(7,0,-1):
  ans.append(c[0]);c=[p*(c[i+1]-c[i])/(kn[i+p+1]-kn[i+1]) for i in range(len(c)-1)];kn=kn[1:-1]
 return ans

def setup():
 inp=BASE/'data_exact/modal_v2.json';assert sha(inp)==PINS['input']
 raw=json.loads(inp.read_bytes());a=raw['arrays'];M,nb=a['S']['shape'];kn=[frac(x) for x in a['knots']['hex']];sc={k:frac(v) for k,v in raw['scalars_hex'].items()}
 assert raw['degree']==7 and len(kn)==nb+8 and kn[:8]==[kn[0]]*8
 assert M==260 and sc['bi']>=49 and 0<sc['k']<F(1,2)
 def get(name,m,j):return frac(a[name]['hex'][m*a[name]['shape'][1]+j])
 weights=[{} for _ in range(M+2)]
 for m in range(M):
  for nu in (1+2*m,1-2*m,3+2*m,3-2*m):
   j=(abs(nu)-1)//2;weights[j][m]=weights[j].get(m,F(0))+F(1 if nu>0 else -1,8)
 weights=[{m:w for m,w in row.items() if w} for row in weights]
 inn=[];bi=sc['bi']
 for j,ws in enumerate(weights):
  C=ws.get(0,F(0));assert C==(F(1,4) if j in (0,1) else 0)
  D=[sum((w*get('D',m,l) for m,w in ws.items()),F(0)) for l in range(7)]
  co=[sum((w*get('S',m,l) for m,w in ws.items()),F(0)) for l in range(8)]
  J=jets_left(co,kn[:16]);P=[sum((D[l]*(2*l+2)**v for l in range(7)),C if v==0 else F(0)) for v in range(7)]
  ei=[sum(((-bi)**(i-l)*(J[l]-P[l])/math.factorial(l)/math.factorial(i-l) for l in range(i+1)),F(0)) for i in range(7)]
  for v in range(7):
   joined=P[v]+sum((math.comb(v,l)*bi**(v-l)*math.factorial(l)*ei[l] for l in range(v+1)),F(0))
   assert joined==J[v],(j,v,'inner join')
  inn.append((C,D,ei))
 assert inn[-1]==(F(0),[F(0)]*7,[F(0)]*7)
 return raw,sc,kn,inn

def run():
 start=time.monotonic();ctx.prec=384;ctx.threads=1;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 raw,sc,kn,inn=setup();M=260;N=M+1;k,L,bi=[sc[x] for x in ('k','L','bi')];ta=kn[0];tb=kn[8]
 archive=BASE/'research/middle_residual/evidence/original_knots.jsonl.gz';manifest=archive.parent/'knot_manifest.json';audit=archive.parent/'knot_audit.json'
 assert sha(archive)==PINS['archive'] and sha(manifest)==PINS['manifest'] and sha(BASE/'research/ball_transport/code/dyadic_ball.py')==PINS['transport']
 au=json.loads(audit.read_bytes());assert au['status']=='PASS' and au['archive_sha256']==PINS['archive'] and au['manifest_sha256']==PINS['manifest'] and au['footer_read']
 with gzip.open(archive,'rt') as f:header=json.loads(f.readline());row=json.loads(f.readline())
 assert row['span']==0 and F(row['a_exact'])==ta and F(row['b_exact'])==tb and F(row['polynomial_mid_exact'])==(ta+tb)/2
 assert len(row['j_right'])==N and len(row['density_polynomials'])==N+1
 join_checks=0
 for j,(C,D,ei) in enumerate(inn):
  shifted=shift([import_ball(v) for v in row['density_polynomials'][j]],-(tb-ta)/2)
  for v in range(7):
   exactjet=(C if v==0 else 0)+sum((D[l]*(2*l+2)**v for l in range(7)),F(0))+sum((math.comb(v,l)*bi**(v-l)*math.factorial(l)*ei[l] for l in range(v+1)),F(0))
   assert (math.factorial(v)*shifted[v]).contains(aa(exactjet)),(j,v,'archive join')
   join_checks+=1
 assert arb(0)**0==1
 j_a=[]
 for n in range(1,N+1):
  rate=F(4-2*n);p=[import_ball(v) for v in row['density_polynomials'][n]]
  j_a.append(aa(rate*(tb-ta)).exp()*import_ball(row['j_right'][n-1])+integ(p,-(tb-ta)/2,tb-ta,rate))
 C,D,ei=inn[1]
 inner_strain=aa(C/2+sum((D[l]/(2*l+4) for l in range(7)),F(0))+sum((ei[l]*(-1)**l*math.factorial(l)/(2+bi)**(l+1) for l in range(7)),F(0)))
 canonical_c=aa(2*ta).exp()*(j_a[0]+inner_strain);assert canonical_c.contains(aa(3/k-1))
 print(json.dumps({'utc':utc(),'stage':'first_boundary','canonical_c_consistency':canonical_c.str(18),'seconds':time.monotonic()-start}),flush=True)
 cases=[]
 for T in (F(0),F(1,8),F(5,2)):
  R=aa(ta-T).exp();R2=R*R;ea=aa(-2*ta).exp();d=[];e=[];rv=[];details=[]
  for j,(C,D,ei) in enumerate(inn):
   terms=[(F(2*l+2),[c]) for l,c in enumerate(D)]+[(bi,ei)]
   dj=arb(0);ej=arb(0);rj=aa(C)
   for alpha,cs in terms:
    beta=alpha-2
    dc=[(3+alpha)*cs[l]+((l+1)*cs[l+1] if l+1<len(cs) else 0) for l in range(len(cs))]
    assert beta>=0 and (beta>0 or len(cs)==1)
    for l,(c,cc) in enumerate(zip(cs,dc)):
     x=max(T,F(l)/beta) if beta>0 else T
     maximum=(arb(1) if l==0 else aa(x)**l)*aa(-beta*x).exp()
     dj+=aa(abs(c))*maximum;ej+=aa(abs(cc))*maximum
    rj+=aa(-alpha*T).exp()*sum((aa(c)*(arb(1) if l==0 else aa(-T)**l) for l,c in enumerate(cs)),arb(0))
   d.append(ea*dj);e.append(ea*ej);rv.append(rj)
   details.append({'j':j,'d':out(d[-1]),'e':out(e[-1]),'Rhat_boundary':out(rj)})
  Dtot=sum(d,arb(0));Etot=sum(e,arb(0));Qtot=sum(((2*j+1)*v for j,v in enumerate(d)),arb(0));forcing=[];B=[]
  for n in range(1,N+1):forcing.append((e[n-1]+(2*n-1)*d[n-1]+e[n]+(2*n+1)*d[n])/2)
  H=3*forcing[0]*R2/16
  for n in range(2,N+1):
   rate=F(4-2*n);C,Ds,ei=inn[n];jn=aa(rate*T).exp()*j_a[n-1]
   if T:
    terms=[(F(0),[C])]+[(F(2*l+2),[c]) for l,c in enumerate(Ds)]+[(bi,ei)]
    for alpha,cs in terms:
     if not any(cs):continue
     jn+=aa(-alpha*T).exp()*integ([aa(c) for c in cs],-T,T,rate+alpha)
   bn=2*n*jn-(rv[n-1]+rv[n])/2
   cm=F(1,2) if n==2 else F(1,2*n-4)
   H+=(abs(bn)+forcing[n-1]*R2*aa(F(1,2*n+6)+cm))/2
   B.append({'n':n,'j_boundary':out(jn),'B_over_R4':out(bn)})
  Cr=arb(1)/6+H;Ct=arb(1)/3+H;cl=1/aa(k);c=3/aa(k)-1
  b5=abs(cl)*Etot+Dtot+abs(c)*(Etot+Qtot)+3*Cr/2+Ct+R2*(Cr*Etot+Ct*Qtot)
  u=R/aa(L);m=u**3*(1+u*u)**aa((k-3)/2);wm=b5*R**5/m
  vals={'R':R,'D':Dtot,'E':Etot,'Q':Qtot,'H':H,'C_r':Cr,'C_theta':Ct,'B5':b5,'W_boundary_majorant':b5*R**5,'W_over_m':wm,'Wm_times_one_plus_u_power_half':wm*(1+u)**aa(F(1,2)),'Wm_times_one_plus_u_power_half_minus_k':wm*(1+u)**aa(F(1,2)-k)}
  case={'T_exact':str(T),'values':{key:out(v) for key,v in vals.items()},'mode_bounds':details,'upper_Green':B}
  assert all(v.is_finite() for v in vals.values()) and b5>0
  cases.append(case);print(json.dumps({'utc':utc(),'stage':'case','T':str(T),'B5':b5.str(12),'Wm':wm.str(12),'seconds':time.monotonic()-start}),flush=True)
 coeff={'schema':'ipm-inner-exact-density-coefficients-v1','input_sha256':PINS['input'],'ta_exact':str(ta),'bi_exact':str(bi),'rows':[{'j':j,'C':str(C),'D':[str(v) for v in D],'Ei':[str(v) for v in ei]} for j,(C,D,ei) in enumerate(inn)]}
 cp=E/'exact_inner_coefficients.json';cp.write_text(json.dumps(coeff,indent=2)+'\n')
 result={'utc':utc(),'status':'COMPUTED_REQUIRES_INDEPENDENT_AUDIT','method':'Exact dyadic input and derivative jets; exact monomial maxima; Arb384 stable exponential moments and canonical first-span upper moments; positive B5 theorem','source_sha256':sha(__file__),'proof_sha256':sha(BASE/'research/inner_majorant/PROOF.md'),'dependency_pins':PINS,'knot_audit_sha256':sha(audit),'coefficient_sha256':sha(cp),'archive_join_checks':join_checks,'canonical_c_consistency':out(canonical_c),'precision_bits':ctx.prec,'k_exact':str(k),'L_exact':str(L),'ta_exact':str(ta),'cases':cases,'seconds':time.monotonic()-start,'scope':'Zeroth residual only, exact repaired modal trial. T=0 covers whole inner disk. No target derivative norm, X3-distance theorem, inverse or decisive endpoint.'}
 dest=E/'inner_result.json';dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':utc(),'stage':'done','seconds':result['seconds'],'result_sha256':sha(dest)}),flush=True)
if __name__=='__main__':run()
