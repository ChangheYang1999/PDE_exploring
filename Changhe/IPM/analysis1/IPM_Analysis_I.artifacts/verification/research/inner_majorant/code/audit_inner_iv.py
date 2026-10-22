"""Independent mpmath.iv audit using Cox polynomials and antiderivative integrals."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,gzip,hashlib,math,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/inner_majorant/evidence';iv.dps=160
PRIMARY_SHA='dc15bc9c1ee592dbfda9ec05fa5b7c4301622594395439d917e3288eb3f367b5'

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def fhex(v):return F.from_float(float.fromhex(v))
def rawfrac(v):s,m,e,b=v;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def endpoints(x):return tuple(rawfrac(v) for v in x._mpi_)
def ib(data):
 assert data['schema']=='arb-dyadic-mid-radius-v1'
 m,e,r,f=[int(data[k]) for k in ('mid_m','mid_e','rad_m','rad_e')];assert r>=0
 c=F(m)*F(2)**e;rad=F(r)*F(2)**f
 return iv.mpf([iq(c-rad).a,iq(c+rad).b])
def encloses(old,new):
 a,b=endpoints(new)
 return F(old['lower_exact'])<=a<=b<=F(old['upper_exact'])
def encode(x):a,b=endpoints(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':str(x)}
def polyadd(p,q):return [(p[j] if j<len(p) else F(0))+(q[j] if j<len(q) else F(0)) for j in range(max(len(p),len(q)))]
def linmul(p,a,b):
 out=[F(0)]*(len(p)+1)
 for j,v in enumerate(p):out[j]+=a*v;out[j+1]+=b*v
 return out

def cox_first(kn):
 a,b=kn[7],kn[8];mid=(a+b)/2;polys={7:[F(1)]}
 for d in range(1,8):
  nxt={}
  for j in range(7-d,8):
   p=[F(0)]
   if j in polys and kn[j+d]!=kn[j]:p=polyadd(p,linmul(polys[j],(mid-kn[j])/(kn[j+d]-kn[j]),1/(kn[j+d]-kn[j])))
   if j+1 in polys and kn[j+d+1]!=kn[j+1]:p=polyadd(p,linmul(polys[j+1],(kn[j+d+1]-mid)/(kn[j+d+1]-kn[j+1]),-1/(kn[j+d+1]-kn[j+1])))
   nxt[j]=p
  polys=nxt
 for degree in range(8):assert sum((p[degree] if degree<len(p) else F(0) for p in polys.values()),F(0))==(1 if degree==0 else 0)
 return [[polys[j][l] if l<len(polys[j]) else F(0) for l in range(8)] for j in range(8)]
def translate(p,d):return [sum((p[l]*math.comb(l,j)*d**(l-j) for l in range(j,len(p))),F(0)) for j in range(len(p))]
def eval_iv(p,x):
 v=iv.mpf(0)
 for c in reversed(p):v=v*x+iq(c)
 return v

def integrate(p,offset,h,rate):
 """Exact polynomial antiderivative at endpoints, or exponential-Taylor integral."""
 assert h>=0
 if h==0:return iv.mpf(0)
 p=translate(p,offset)
 if rate==0:return iq(sum((c*h**(j+1)/F(j+1) for j,c in enumerate(p)),F(0)))
 z=rate*h
 if abs(z)>F(1,2):
  prim=[F(0)]*len(p)
  for j in range(len(p)-1,-1,-1):prim[j]=(p[j]-(j+1)*(prim[j+1] if j+1<len(p) else 0))/rate
  return iv.exp(iq(z))*eval_iv(prim,iq(h))-iq(prim[0])
 # Integrate the product of an exact exponential Taylor polynomial and p.
 Q=140;total=F(0);rq=F(1)
 for q in range(Q+1):
  total+=rq*sum((c*h**(q+j+1)/F(q+j+1) for j,c in enumerate(p)),F(0))
  rq*=rate/F(q+1)
 sup=sum((abs(c)*h**j for j,c in enumerate(p)),F(0))
 remainder=iq(h*sup*abs(z)**(Q+1)/math.factorial(Q+1))*iv.exp(iq(abs(z)))
 return iq(total)+iv.mpf([-remainder.b,remainder.b])

def run():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 rp=E/'inner_result.json';res=json.loads(rp.read_bytes());assert sha(BASE/'research/inner_majorant/code/certify_inner.py')==res['source_sha256']==PRIMARY_SHA
 inp=BASE/'data_exact/modal_v2.json';assert sha(inp)==res['dependency_pins']['input']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 raw=json.loads(inp.read_bytes());ar=raw['arrays'];M,nb=ar['S']['shape'];assert M==260 and raw['degree']==7
 kn=[fhex(v) for v in ar['knots']['hex']];sc={k:fhex(v) for k,v in raw['scalars_hex'].items()};a,b=kn[7],kn[8];mid=(a+b)/2;k,L,bi=[sc[s] for s in ('k','L','bi')]
 assert nb>=8 and len(kn)==nb+8 and kn[:8]==[a]*8 and a<b and all(kn[j]<=kn[j+1] for j in range(len(kn)-1))
 assert 0<k<F(1,2) and L>0 and bi>=49
 basis=cox_first(kn);assert a==kn[0]
 def get(name,m,j):return fhex(ar[name]['hex'][m*ar[name]['shape'][1]+j])
 # Laurent multiplication: the signed sine coefficients of (sin theta+sin3theta)/4 times cos2mtheta.
 ws=[{} for _ in range(M+2)];base={1:F(1,4),3:F(1,4),-1:-F(1,4),-3:-F(1,4)}
 for m in range(M):
  cos={0:F(1)} if m==0 else {2*m:F(1,2),-2*m:F(1,2)}
  for f,v in base.items():
   for g,w in cos.items():
    freq=f+g
    if freq>0:
     j=(freq-1)//2;ws[j][m]=ws[j].get(m,F(0))+v*w
 cp=E/'exact_inner_coefficients.json';assert sha(cp)==res['coefficient_sha256'];stored=json.loads(cp.read_bytes());assert len(stored['rows'])==M+2
 coeff=[];polys=[];checks=0
 for j,row in enumerate(ws):
  C=row.get(0,F(0));assert C==(F(1,4) if j<2 else 0)
  D=[sum((w*get('D',m,l) for m,w in row.items()),F(0)) for l in range(7)]
  S=[sum((w*get('S',m,l) for m,w in row.items()),F(0)) for l in range(8)]
  p=[sum((basis[l][q]*S[l] for l in range(8)),F(0)) for q in range(8)];polys.append(p);pleft=translate(p,-(b-a)/2)
  diff=[pleft[q]-sum((D[l]*(2*l+2)**q/F(math.factorial(q)) for l in range(7)),C if q==0 else F(0)) for q in range(7)]
  Ei=[sum((diff[q]*(-bi)**(l-q)/F(math.factorial(l-q)) for q in range(l+1)),F(0)) for l in range(7)]
  old=stored['rows'][j];assert old['j']==j and F(old['C'])==C and [F(x) for x in old['D']]==D and [F(x) for x in old['Ei']]==Ei
  checks+=15;coeff.append((C,D,Ei))
  for v in range(7):
   got=(C if v==0 else 0)+sum((D[l]*(2*l+2)**v for l in range(7)),F(0))+sum((math.comb(v,l)*bi**(v-l)*math.factorial(l)*Ei[l] for l in range(v+1)),F(0))
   assert got==math.factorial(v)*pleft[v];checks+=1
 archive=BASE/'research/middle_residual/evidence/original_knots.jsonl.gz';assert sha(archive)==res['dependency_pins']['archive']=='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
 with gzip.open(archive,'rt') as f:header=json.loads(f.readline());span=json.loads(f.readline())
 assert span['span']==0 and F(span['a_exact'])==a and F(span['b_exact'])==b
 for j in range(M+2):
  for q,c in enumerate(polys[j]):
   lo,hi=endpoints(ib(span['density_polynomials'][j][q]));assert lo<=c<=hi;checks+=1
 jleft=[]
 for n in range(1,M+2):
  rate=F(4-2*n);jleft.append(iv.exp(iq(rate*(b-a)))*ib(span['j_right'][n-1])+integrate(polys[n],-(b-a)/2,b-a,rate))
 print(json.dumps({'utc':utc(),'stage':'exact_coefficients_and_first_boundary','checks':checks,'seconds':time.monotonic()-start}),flush=True)
 C,D,Ei=coeff[1]
 cinner=C/2+sum((D[l]/(2*l+4) for l in range(7)),F(0))+sum((Ei[l]*(-1)**l*math.factorial(l)/(bi+2)**(l+1) for l in range(7)),F(0))
 ccheck=iv.exp(iq(2*a))*(jleft[0]+iq(cinner));assert encloses(res['canonical_c_consistency'],ccheck)
 assert endpoints(ccheck)[0]<=3/k-1<=endpoints(ccheck)[1]
 assert [F(c['T_exact']) for c in res['cases']]==[F(0),F(1,8),F(5,2)]
 outputs=[]
 for oldcase in res['cases']:
  T=F(oldcase['T_exact']);assert T>=0
  R=iv.exp(iq(a-T));u=R/iq(L);R2=R*R;Dvec=[];Evec=[];rhat=[];caseschecked=0
  for j,(C,D,Ei) in enumerate(coeff):
   d=iv.mpf(0);e=iv.mpf(0);rho=iq(C)
   for alpha,cs in [(F(2*l+2),[c]) for l,c in enumerate(D)]+[(bi,Ei)]:
    deriv=[(3+alpha)*cs[l]+((l+1)*cs[l+1] if l+1<len(cs) else 0) for l in range(len(cs))]
    for l,c in enumerate(cs):
     beta=alpha-2;assert beta>=0 and (beta>0 or l==0)
     x=max(T,F(l)/beta) if beta else T
     v=iq(x**l)*iv.exp(iq(-beta*x));d+=iq(abs(c))*v;e+=iq(abs(deriv[l]))*v
    rho+=iv.exp(iq(-alpha*T))*eval_iv(cs,iq(-T))
   scale=iv.exp(iq(-2*a));d*=scale;e*=scale;Dvec.append(d);Evec.append(e);rhat.append(rho)
   old=oldcase['mode_bounds'][j]
   for name,value in [('d',d),('e',e),('Rhat_boundary',rho)]:assert encloses(old[name],value),(str(T),j,name);caseschecked+=1
  Dt=sum(Dvec,iv.mpf(0));Et=sum(Evec,iv.mpf(0));Qt=sum(((2*j+1)*v for j,v in enumerate(Dvec)),iv.mpf(0))
  f=[(Evec[n-1]+(2*n-1)*Dvec[n-1]+Evec[n]+(2*n+1)*Dvec[n])/2 for n in range(1,M+2)]
  H=3*f[0]*R2/16
  for n in range(2,M+2):
   rate=F(4-2*n);jn=iv.exp(iq(rate*T))*jleft[n-1];C,D,Ei=coeff[n]
   for alpha,p in [(F(0),[C])]+[(F(2*l+2),[c]) for l,c in enumerate(D)]+[(bi,Ei)]:
    if any(p):jn+=iv.exp(iq(-alpha*T))*integrate(p,-T,T,rate+alpha)
   bn=2*n*jn-(rhat[n-1]+rhat[n])/2;old=oldcase['upper_Green'][n-2];assert old['n']==n
   assert encloses(old['j_boundary'],jn),(str(T),n,'j');assert encloses(old['B_over_R4'],bn),(str(T),n,'B');caseschecked+=2
   cm=F(1,2) if n==2 else F(1,2*n-4);H+=(abs(bn)+f[n-1]*R2*iq(F(1,2*n+6)+cm))/2
  Cr=iq(F(1,6))+H;Ct=iq(F(1,3))+H;c=iq(3/k-1);cl=iq(1/k)
  b5=abs(cl)*Et+Dt+abs(c)*(Et+Qt)+3*Cr/2+Ct+R2*(Cr*Et+Ct*Qt)
  m=u**3*iv.exp(iq((k-3)/2)*iv.log(1+u*u));wm=b5*R**5/m
  vals={'R':R,'D':Dt,'E':Et,'Q':Qt,'H':H,'C_r':Cr,'C_theta':Ct,'B5':b5,'W_boundary_majorant':b5*R**5,'W_over_m':wm,'Wm_times_one_plus_u_power_half':wm*iv.exp(iq(F(1,2))*iv.log(1+u)),'Wm_times_one_plus_u_power_half_minus_k':wm*iv.exp(iq(F(1,2)-k)*iv.log(1+u))}
  for name,val in vals.items():assert encloses(oldcase['values'][name],val),(str(T),name);caseschecked+=1
  outputs.append({'T_exact':str(T),'enclosure_checks':caseschecked,'values':{name:encode(v) for name,v in vals.items()}})
  print(json.dumps({'utc':utc(),'stage':'case_pass','T':str(T),'checks':caseschecked,'seconds':time.monotonic()-start}),flush=True)
 out={'utc':utc(),'status':'PASS','source_sha256':sha(__file__),'primary_result_sha256':sha(rp),'primary_source_sha256':res['source_sha256'],'proof_sha256_at_audit':sha(BASE/'research/inner_majorant/PROOF.md'),'exact_coefficient_and_Cox_checks':checks,'method':'Independent Laurent angular transform, exact Cox polynomials and endpoint Taylor coefficients, exact antiderivative endpoint integrals or integrated exponential Taylor series, and mpmath.iv160 positive majorant. Every primary mode/Green/scalar enclosure contains the independent interval.','cases':outputs,'seconds':time.monotonic()-start,'scope':'Same canonical upper-boundary moment archive; archive itself independently audited. No new independently integrated exterior beyond that dependency.'}
 op=E/'inner_iv_audit.json';op.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':utc(),'stage':'done','status':'PASS','seconds':out['seconds']}),flush=True)
if __name__=='__main__':run()
