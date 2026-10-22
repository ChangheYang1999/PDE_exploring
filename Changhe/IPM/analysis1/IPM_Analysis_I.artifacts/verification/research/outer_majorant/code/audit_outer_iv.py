"""Independent exterior audit: Laurent/Cox reconstruction, recurrence, antiderivatives, iv."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,math,hashlib,time,resource,gzip
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import mpmath,flint
from mpmath import iv
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/outer_majorant/evidence';iv.dps=160
ZERO=(F(0),F(0))
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def hx(v):return F.from_float(float.fromhex(v))
def rf(v):
 sign,m,e,bc=v;assert bc>=0
 return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 assert not iv.isnan(x) and not iv.isinf(x)
 a,b=map(rf,x._mpi_);assert a<=b
 return a,b

def interval(a,b):assert a<=b;return iv.mpf([iq(a).a,iq(b).b])
def ib(d):
 assert d['schema']=='arb-dyadic-mid-radius-v1'
 m,e,r,f=[int(d[k]) for k in ('mid_m','mid_e','rad_m','rad_e')];assert r>=0
 return interval(F(m)*F(2)**e-F(r)*F(2)**f,F(m)*F(2)**e+F(r)*F(2)**f)
def enclosed(old,x,label):
 a,b=ends(x);lo,hi=F(old['lower_exact']),F(old['upper_exact']);assert lo<=hi
 if not lo<=a<=b<=hi:raise AssertionError((label,'primary does not contain independent interval',str(a-lo),str(hi-b)))
def out(x):a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':str(x)}
def ap(a,b):return a[0]+b[0],a[1]+b[1]
def sm(a,v):return a[0]*v,a[1]*v
def ev(a,z):return iq(a[0])+iq(a[1])*z

def padd(p,q):return [(p[j] if j<len(p) else F(0))+(q[j] if j<len(q) else F(0)) for j in range(max(len(p),len(q)))]
def linmul(p,a,b):
 r=[F(0)]*(len(p)+1)
 for j,v in enumerate(p):r[j]+=a*v;r[j+1]+=b*v
 return r

def cox_last(kn):
 kt=kn[-16:];a,b=kt[7],kt[8];mid=(a+b)/2;polys={7:[F(1)]}
 for d in range(1,8):
  nxt={}
  for j in range(7-d,8):
   p=[F(0)]
   if j in polys and kt[j+d]!=kt[j]:p=padd(p,linmul(polys[j],(mid-kt[j])/(kt[j+d]-kt[j]),1/(kt[j+d]-kt[j])))
   if j+1 in polys and kt[j+d+1]!=kt[j+1]:p=padd(p,linmul(polys[j+1],(kt[j+d+1]-mid)/(kt[j+d+1]-kt[j+1]),-1/(kt[j+d+1]-kt[j+1])))
   nxt[j]=p
  polys=nxt
 for q in range(8):assert sum((p[q] if q<len(p) else F(0) for p in polys.values()),F(0))==(1 if q==0 else 0)
 return [[polys[j][q] if q<len(polys[j]) else F(0) for q in range(8)] for j in range(8)]
def shift(p,d):return [sum((p[l]*math.comb(l,j)*d**(l-j) for l in range(j,len(p))),F(0)) for j in range(len(p))]
def polyval(p,x):
 r=iv.mpf(0)
 for c in reversed(p):r=r*x+iq(c)
 return r

def primitive(p,lam):
 assert lam
 q=[F(0)]*len(p)
 for j in reversed(range(len(p))):q[j]=(p[j]-(j+1)*(q[j+1] if j+1<len(p) else 0))/lam
 return q

def inverse_affine(p,lam):
 assert lam
 q=[ZERO]*len(p)
 for j in reversed(range(len(p))):q[j]=sm(ap(p[j],sm(q[j+1],-(j+1)) if j+1<len(p) else ZERO),1/lam)
 for j in range(len(p)):assert ap(sm(q[j],lam),sm(q[j+1],j+1) if j+1<len(p) else ZERO)==p[j]
 return q

def run():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));assert mpmath.__version__=='1.3.0' and flint.__version__=='0.9.0'
 rp=E/'outer_result.json';res=json.loads(rp.read_bytes());assert res['status']=='COMPUTED_REQUIRES_INDEPENDENT_AUDIT'
 assert sha(BASE/'research/outer_majorant/code/certify_outer.py')==res['source_sha256']
 assert sha(BASE/'research/outer_majorant/PROOF.md')==res['proof_sha256']
 inp=BASE/'data_exact/modal_v2.json';assert sha(inp)==res['dependency_pins']['input']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 assert sha(E/'final_span.json')==res['dependency_pins']['span']=='e8aa41cf0b0e19b0008c0c49ee105fb847e1a6cd7af39ea202b833e5cf1fb467'
 assert sha(E/'final_span_extract.json')==res['extract_sha256'];extract=json.loads((E/'final_span_extract.json').read_bytes())
 assert extract['status']=='PASS' and extract['full_gzip_footer_read'] and extract['archive_sha256']=='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
 assert sha(BASE/'research/outer_majorant/code/extract_final_span.py')==extract['source_sha256']
 audit=BASE/'research/middle_residual/evidence/knot_audit.json';assert sha(audit)==extract['archive_audit_sha256']=='decad65da9e0f347f63f2bd89f3317de2afc4a88500b6fb45b89b7a1869f5eeb'
 assert json.loads(audit.read_bytes())['status']=='PASS'
 archive=BASE/'research/middle_residual/evidence/original_knots.jsonl.gz';assert sha(archive)==extract['archive_sha256']
 with gzip.open(archive,'rb') as stream:
  header=json.loads(next(stream));last_span=None;footer=None;span_count=0
  for line in stream:
   assert line.endswith(b'\n');obj=json.loads(line)
   if obj['type']=='span':assert footer is None and obj['span']==span_count;last_span=line;span_count+=1
   else:assert obj['type']=='complete' and footer is None;footer=obj
 assert span_count==1558 and header==extract['header'] and footer==extract['footer'] and last_span==(E/'final_span.json').read_bytes()
 raw=json.loads(inp.read_bytes());ar=raw['arrays'];M,nb=ar['S']['shape'];kn=[hx(v) for v in ar['knots']['hex']];sc={k:hx(v) for k,v in raw['scalars_hex'].items()};k,L,bo=[sc[s] for s in ('k','L','bo')]
 assert M==260 and raw['degree']==7 and len(kn)==nb+8 and all(kn[i]<=kn[i+1] for i in range(len(kn)-1)) and kn[-8:]==[kn[-1]]*8 and 0<k<F(1,2) and L>0 and bo>120
 assert {key:F(value) for key,value in res['scalars_exact'].items()}==sc
 assert k==F(1615536043799051,9007199254740992) and F(res['c_l_exact'])==1/k
 jl=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)];assert raw['outer_jl']==[list(x) for x in jl]
 beta=[(j+1)*k-j-2*l for j,l in jl]+[3-bo];alpha=[v-3 for v in beta]
 basis=cox_last(kn);a,b=kn[-9],kn[-8];h=b-a;assert h>0 and b==kn[-1]==F(res['tb_exact'])
 span=json.loads((E/'final_span.json').read_bytes());assert span['span']==1557 and F(span['a_exact'])==a and F(span['b_exact'])==b and F(span['polynomial_mid_exact'])==(a+b)/2
 assert res['knot_interval_exact']==[str(a),str(b)] and len(span['density_polynomials'])==262 and len(span['i_left'])==261
 # Independent signed Laurent multiplication. The positive Fourier sine amplitude is read after multiplication.
 weights=[{} for _ in range(M+2)];sines={1:F(1,4),3:F(1,4),-1:-F(1,4),-3:-F(1,4)}
 for m in range(M):
  cs={0:F(1)} if m==0 else {2*m:F(1,2),-2*m:F(1,2)}
  for f,v in sines.items():
   for g,w in cs.items():
    freq=f+g
    if freq>0:
     j=(freq-1)//2;weights[j][m]=weights[j].get(m,F(0))+v*w
 def get(name,m,l):return hx(ar[name]['hex'][m*ar[name]['shape'][1]+l])
 nv=BASE/'research/modal_repair/evidence/audit_verdict.json';assert sha(nv)==res['dependency_pins']['normalization_verdict']=='c17c7f4dfbc86ac789838d59d846f5641cae59577dd8e62987edd31904dab6b8';nd=json.loads(nv.read_bytes());assert nd['verdict']=='CONFIRMED' and nd['source_and_evidence_sha256']['research/modal_repair/evidence/independent_gauss_iv.json']==res['dependency_pins']['normalization']
 zp=BASE/'research/modal_repair/evidence/independent_gauss_iv.json';assert sha(zp)==res['dependency_pins']['normalization']=='0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a'
 zraw=json.loads(zp.read_bytes());assert zraw['status']=='PASS independent arithmetic and formula reproduction; not a PDE residual certificate';zd=zraw['values']['A00_correction'];zlo,zhi=[F(zd[s]) for s in ('lower_exact_dyadic','upper_exact_dyadic')];z=interval(zlo,zhi);assert zlo<=zhi<0
 cp=E/'exact_outer_coefficients.json';assert sha(cp)==res['coefficient_sha256'];co=json.loads(cp.read_bytes());assert len(co['rows'])==262 and co['beta_exact']==[str(v) for v in beta] and co['tb_exact']==str(b) and co['correction_parameter_exact_interval']==[str(zlo),str(zhi)] and co['input_sha256']==res['dependency_pins']['input']
 coeff=[];polys=[];rjets=[];exactchecks=0;spanchecks=0;joins=0
 for j,ws in enumerate(weights):
  C=ws.get(0,F(0));assert C==(F(1,4) if j<2 else 0)
  S=[sum((w*get('S',m,l) for m,w in ws.items()),F(0)) for l in range(nb-8,nb)]
  poly=[sum((S[i]*basis[i][q] for i in range(8)),F(0)) for q in range(8)];polys.append(poly);right=shift(poly,h/2);rjets.append(right)
  for q,v in enumerate(poly):lo,hi=ends(ib(span['density_polynomials'][j][q]));assert lo<=v<=hi;spanchecks+=1
  A=[sum((w*get('Aout',m,l) for m,w in ws.items()),F(0)) for l in range(10)]
  # Endpoint Taylor coefficients of e^(bo*tau) times the join discrepancy.
  diff=[right[q]-sum((A[l]*alpha[l]**q/F(math.factorial(q)) for l in range(10)),F(0)) for q in range(7)]
  eo=[sum((diff[q]*bo**(l-q)/F(math.factorial(l-q)) for q in range(l+1)),F(0)) for l in range(7)]
  c=[[(A[l],C if l==0 else F(0))] for l in range(10)]+[[(eo[l],-C*(alpha[0]+bo)**l/F(math.factorial(l))) for l in range(7)]]
  stored=co['rows'][j];assert stored['j']==j and len(stored['basis'])==11
  for v in range(7):
   joined=ZERO
   for jbasis,cs in enumerate(c):
    for l in range(min(v,len(cs)-1)+1):joined=ap(joined,sm(cs[l],alpha[jbasis]**(v-l)/F(math.factorial(v-l))))
   assert joined==(right[v],F(0));joins+=1
  for exact,old in zip(c,stored['basis']):
   assert len(exact)==len(old)
   for value,ostr in zip(exact,old):assert value==tuple(F(t) for t in ostr);exactchecks+=2
  coeff.append(c)
 assert all(x==ZERO for cs in coeff[-1] for x in cs)
 ip=[];checks=0
 for n in range(1,262):
  lam=F(2*n+4);leftpoly=shift(polys[n-1],-h/2);q=primitive(leftpoly,lam)
  # Stable at this precision; polynomial antiderivative differs from the primary entire-series integration.
  ibound=iv.exp(iq(-lam*h))*(ib(span['i_left'][n-1])-iq(q[0]))+polyval(q,iq(h))
  old=res['green'][n-1];assert old['n']==n;enclosed(old['i_right'],ibound,('i',n));ip.append(ibound);checks+=1
 print(json.dumps({'utc':utc(),'stage':'independent_Cox_and_endpoint','checks':checks,'exact_checks':exactchecks,'seconds':time.monotonic()-start}),flush=True)
 ep2=iv.exp(iq(2*b));ep3=iv.exp(iq(3*b));P=[[iv.mpf(0)]*(1 if j<10 else 7) for j in range(11)];Q=[[iv.mpf(0)]*(1 if j<10 else 7) for j in range(11)];trans=[];polychecks=0;denoms=[]
 for n in range(1,262):
  m=2*n;H=(rjets[n-1][0]/2+rjets[n][0]/2,F(0));old=res['green'][n-1];assert len(old['plus_exact'])==len(old['minus_exact'])==11
  for bs,v in enumerate(beta):
   aa=v+1;assert aa+m!=0 and aa-m<0;denoms.append(abs(aa+m));c1,c2=coeff[n-1][bs],coeff[n][bs]
   forcing=[]
   for l in range(len(c1)):
    f=ap(sm(c1[l],(aa-m)/2),sm(c2[l],(aa+m)/2))
    if l+1<len(c1):f=ap(f,sm(ap(c1[l+1],c2[l+1]),F(l+1,2)))
    forcing.append(f)
   qp=inverse_affine(forcing,aa+m);qm=inverse_affine([sm(q,-1) for q in forcing],aa-m);H=ap(H,sm(qp[0],-1))
   for tag,ps in [('plus_exact',qp),('minus_exact',qm)]:
    assert len(old[tag][bs])==len(ps)
    for l,value in enumerate(ps):assert value==tuple(F(v) for v in old[tag][bs][l]);polychecks+=2
   for l in range(len(qp)):
    P[bs][l]+=ep2*abs(ev(ap(qp[l],qm[l]),z))/2;Q[bs][l]+=ep2*abs(ev(ap(qm[l],sm(qp[l],-1)),z))/2
  hv=ev(H,z)-m*ip[n-1];tr=ep2*abs(hv)/2;enclosed(old['H_over_R4'],hv,('H',n));enclosed(old['transient_velocity_coefficient'],tr,('trans',n));checks+=2;trans.append((F(-m-2),tr))
 D=[];Et=[];Lin=[];linzeros=0
 for bs,v in enumerate(beta):
  d=[];e=[];li=[]
  for l in range(1 if bs<10 else 7):
   di=iv.mpf(0);ei=iv.mpf(0);lli=iv.mpf(0)
   for j in range(262):
    cs=coeff[j][bs];der=sm(cs[l+1],l+1) if l+1<len(cs) else ZERO
    di+=abs(ev(ap(sm(cs[l],v),der),z));ei+=(2*j+1)*abs(ev(cs[l],z));val=ap(sm(cs[l],v/k-1),sm(der,1/k))
    if bs==0:assert val==ZERO;linzeros+=1
    lli+=abs(ev(val,z))
   d.append(ep3*di);e.append(ep3*ei);li.append(ep3*lli)
  D.append(d);Et.append(e);Lin.append(li);old=res['density_sums'][bs];assert old['beta_exact']==str(v)
  for tag,ps in [('P',P[bs]),('Q',Q[bs]),('D',d),('E',e),('L',li)]:
   assert len(old[tag])==len(ps)
   for l,value in enumerate(ps):enclosed(old[tag][l],value,(tag,bs,l));checks+=1
 C={}
 def add_monomial(g,l,v):
  assert g<=2*k-1<0
  if g not in C:C[g]={}
  C[g][l]=C[g].get(l,iv.mpf(0))+v
 for bs in range(1,11):
  for l,v in enumerate(Lin[bs]):add_monomial(beta[bs],l,v)
 products=0
 for bs in range(11):
  for cs in range(11):
   for i in range(len(P[bs])):
    for j in range(len(D[cs])):add_monomial(beta[bs]+beta[cs]-1,i+j,P[bs][i]*D[cs][j]+Q[bs][i]*Et[cs][j])
   products+=1
 for g,tr in trans:
  for cs in range(11):
   for j in range(len(D[cs])):add_monomial(g+beta[cs],j,tr*(D[cs][j]+Et[cs][j]))
   products+=1
 assert len(res['majorant'])==len(C) and products==2992 and linzeros==262
 for g,old in zip(sorted(C),res['majorant']):
  assert str(g)==old['gamma_exact'] and len(old['coefficients'])==len(C[g]) and sorted(C[g])==list(range(len(C[g])))
  for l,v in C[g].items():enclosed(old['coefficients'][l],v,('majorant',str(g),l));checks+=1
 expected={'exact_joins':joins,'archive_joins':joins,'polynomial_identities':polychecks//2,'denominator_pairs':len(denoms),'minimum_abs_lower_denominator_exact':str(min(denoms)),'leading_linear_zeros':linzeros,'product_blocks':products,'unique_exponents':len(C),'monomials':sum(map(len,C.values())),'weighted_rate_checks':12*sum(map(len,C.values()))};assert res['checks']==expected,(res['checks'],expected)
 print(json.dumps({'utc':utc(),'stage':'Green_and_majorant','enclosures':checks,'polynomial_checks':polychecks,'seconds':time.monotonic()-start}),flush=True)
 def maximum(rate,l,T):
  assert rate>0 and T>=0
  x=max(T,F(l)/rate);return iq(x**l)*iv.exp(iq(-rate*x))
 u=iv.exp(iq(b))/iq(L);cases=[];assert [F(x['T_exact']) for x in res['cases']]==[F(0),F(1),F(5),F(9)]
 for old in res['cases']:
  T=F(old['T_exact']);vals={'absolute_W':sum((cc*maximum(-g,l,T) for g,p in C.items() for l,cc in p.items()),iv.mpf(0))}
  for delta in (F(0),F(1,2),F(1,2)-k):
   K=iv.exp(iq(delta-k)*iv.log(u)+iq((3-k)/2)*iv.log(1+iv.exp(iq(-2*T))/(u*u))+iq(delta)*iv.log(1+iv.exp(iq(-T))/u))
   vals['weighted_delta_'+str(delta)]=K*sum((cc*maximum(k-delta-g,l,T) for g,p in C.items() for l,cc in p.items()),iv.mpf(0))
  assert set(vals)==set(old['values'])
  for tag,v in vals.items():enclosed(old['values'][tag],v,('case',str(T),tag));checks+=1
  cases.append({'T_exact':str(T),'values':{tag:out(v) for tag,v in vals.items()}})
 K0=iv.exp(-iq(k)*iv.log(u)+iq((3-k)/2)*iv.log(1+u**(-2)))
 l2=iv.sqrt(iv.pi)*iq(L)*K0*sum((cc*iv.sqrt(iq(F(math.factorial(2*l))/(2*(k-g))**(2*l+1))) for g,p in C.items() for l,cc in p.items()),iv.mpf(0))
 enclosed(res['exterior_L2_majorant'],l2,'L2');checks+=1;enclosed(res['R'],iv.exp(iq(b)),'R');checks+=1
 verdict={'utc':utc(),'status':'PASS','source_sha256':sha(__file__),'primary_source_sha256':res['source_sha256'],'primary_result_sha256':sha(rp),'proof_sha256':sha(BASE/'research/outer_majorant/PROOF.md'),'versions':{'python-flint':flint.__version__,'mpmath':mpmath.__version__},'iv_dps':iv.dps,'exact_coefficient_scalar_checks':exactchecks,'exact_C6_join_checks':joins,'exact_Cox_archive_checks':spanchecks,'exact_Green_polynomial_scalar_checks':polychecks,'enclosure_checks':checks,'cases':cases,'exterior_L2_majorant':out(l2),'seconds':time.monotonic()-start,'method':'Independent Laurent projection and exact Cox last-span polynomial, right Taylor coefficient joins, affine backward-recursion polynomial Green inverse, antiderivative canonical endpoint, direct iv coefficient convolutions and scalar maxima. All primary intervals contain independent intervals.','scope':'Shared independently audited exact input, scalar-correction interval and canonical left moments; does not reintegrate entire interior.'}
 dest=E/'outer_iv_audit.json';dest.write_text(json.dumps(verdict,indent=2)+'\n');print(json.dumps({'utc':utc(),'stage':'done','status':'PASS','checks':checks,'seconds':verdict['seconds']}),flush=True)
if __name__=='__main__':run()
