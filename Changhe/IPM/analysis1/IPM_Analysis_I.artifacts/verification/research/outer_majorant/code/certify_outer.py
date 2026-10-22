"""Entire exterior residual: exact affine coefficients, Arb Green polynomials and maxima."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,time,hashlib,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint,mpmath
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/outer_majorant/evidence'
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import import_ball,export_ball
PINS={'input':'57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6','normalization':'0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a','span':'e8aa41cf0b0e19b0008c0c49ee105fb847e1a6cd7af39ea202b833e5cf1fb467','archive':'c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648','archive_audit':'decad65da9e0f347f63f2bd89f3317de2afc4a88500b6fb45b89b7a1869f5eeb','transport':'6525060f436bf553f3b4a42e403ad2c27dc69d6a82a1460634995f95e755e3c3','normalization_verdict':'c17c7f4dfbc86ac789838d59d846f5641cae59577dd8e62987edd31904dab6b8'}
ZERO=(F(0),F(0))
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def hx(x):return F.from_float(float.fromhex(x))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,x):return a[0]*x,a[1]*x
def ev(a,z):return aa(a[0])+aa(a[1])*z

def out(x):
 assert x.is_finite()
 def dy(y):m,e=y.man_exp();return F(int(m))*F(2)**int(e)
 return {'ball':export_ball(x),'lower_exact':str(dy(x.lower())),'upper_exact':str(dy(x.upper())),'display':x.str(28)}
def inv_poly(p,lam):
 assert lam
 q=[]
 for l in range(len(p)):
  v=ZERO
  for j in range(l,len(p)):v=add(v,mul(p[j],F((-1)**(j-l)*math.factorial(j),math.factorial(l))/lam**(j-l+1)))
  q.append(v)
 for l in range(len(p)):assert add(mul(q[l],lam),mul(q[l+1],l+1) if l+1<len(q) else ZERO)==p[l]
 return q

def setup():
 inp=BASE/'data_exact/modal_v2.json';assert sha(inp)==PINS['input']
 raw=json.loads(inp.read_bytes());ar=raw['arrays'];M,nb=ar['S']['shape'];kn=[hx(v) for v in ar['knots']['hex']];sc={k:hx(v) for k,v in raw['scalars_hex'].items()}
 assert M==260 and raw['degree']==7 and len(kn)==nb+8 and kn[-8:]==[kn[-1]]*8 and all(kn[i]<kn[i+1] for i in range(7,nb))
 jl=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)];assert raw['outer_jl']==[list(v) for v in jl]
 k,bo=sc['k'],sc['bo'];assert k==F(1615536043799051,9007199254740992) and 0<k<F(1,2) and bo>120 and sc['L']>0
 beta=[k-j*(1-k)-2*l for j,l in jl]+[3-bo];alpha=[v-3 for v in beta[:10]]
 weights=[{} for _ in range(M+2)]
 for m in range(M):
  for freq in (1+2*m,1-2*m,3+2*m,3-2*m):
   j=(abs(freq)-1)//2;weights[j][m]=weights[j].get(m,F(0))+F(1 if freq>0 else -1,8)
 weights=[{m:w for m,w in row.items() if w} for row in weights]
 def get(name,m,l):return hx(ar[name]['hex'][m*ar[name]['shape'][1]+l])
 def jets_right(co,kt):
  vals=[]
  for p in range(7,0,-1):
   vals.append(co[-1]);co=[p*(co[i+1]-co[i])/(kt[i+p+1]-kt[i+1]) for i in range(len(co)-1)];kt=kt[1:-1]
  return vals
 coeff=[];jets=[];joins=0
 for j,ws in enumerate(weights):
  C=ws.get(0,F(0));assert C==(F(1,4) if j<2 else 0)
  A=[sum((w*get('Aout',m,l) for m,w in ws.items()),F(0)) for l in range(10)]
  S=[sum((w*get('S',m,l) for m,w in ws.items()),F(0)) for l in range(nb-8,nb)]
  J=jets_right(S,kn[-16:]);jets.append(J)
  P=[sum((A[l]*alpha[l]**v for l in range(10)),F(0)) for v in range(7)]
  eo=[sum((bo**(l-v)*(J[v]-P[v])/F(math.factorial(v)*math.factorial(l-v)) for v in range(l+1)),F(0)) for l in range(7)]
  c=[[(A[b],C if b==0 else F(0))] for b in range(10)]+[[(eo[l],-C*(alpha[0]+bo)**l/F(math.factorial(l))) for l in range(7)]]
  for v in range(7):
   got=ZERO
   for b,cs in enumerate(c):
    for l in range(min(v,len(cs)-1)+1):got=add(got,mul(cs[l],F(math.comb(v,l)*math.factorial(l))*(beta[b]-3)**(v-l)))
   assert got==(J[v],F(0)),(j,v,'exact C6 join');joins+=1
  coeff.append(c)
 assert all(v==ZERO for cs in coeff[-1] for v in cs)
 return sc,kn,beta,coeff,jets,joins

def shift_ball(p,d):return [sum((p[l]*aa(F(math.comb(l,j))*d**(l-j)) for l in range(j,len(p))),arb(0)) for j in range(len(p))]
def lower_endpoint(p,left,h,lam):
 # Reverse v=t_b-t: integral_0^h exp(-lam*v) p(h/2-v)dv.
 rev=[v*(-1)**j for j,v in enumerate(shift_ball(p,h/2))];zq=-lam*h;assert abs(zq)<5
 K=180;z=aa(zq);terms=[arb(1)]
 for q in range(1,K+1):terms.append(terms[-1]*z/q)
 hs=aa(h);integ=arb(0)
 for j,c in enumerate(rev):
  tail=aa(abs(zq))**(K+1)/math.factorial(K+1)/(K+j+2)/(1-aa(abs(zq))/(K+2))
  ph=sum((terms[q]/(q+j+1) for q in range(K+1)),arb(0))+arb(0,tail.upper())
  assert ph>0
  integ+=c*hs**(j+1)*ph
 return z.exp()*left+integ

def run():
 start=time.monotonic();ctx.prec=384;ctx.threads=1;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 assert sha(BASE/'research/ball_transport/code/dyadic_ball.py')==PINS['transport']
 sc,kn,beta,coeff,jets,joins=setup();k,L,bo=[sc[s] for s in ('k','L','bo')];tb=kn[-1];N=261
 ex=json.loads((E/'final_span_extract.json').read_bytes());assert ex['status']=='PASS' and ex['archive_sha256']==PINS['archive'] and ex['archive_audit_sha256']==PINS['archive_audit'] and ex['full_gzip_footer_read']
 assert ex['source_sha256']==sha(BASE/'research/outer_majorant/code/extract_final_span.py') and sha(E/'final_span.json')==ex['final_span_sha256']==PINS['span']
 sp=json.loads((E/'final_span.json').read_bytes());a=F(sp['a_exact']);b=F(sp['b_exact']);h=b-a;assert b==tb and a==kn[-9] and F(sp['polynomial_mid_exact'])==(a+b)/2
 assert len(sp['density_polynomials'])==N+1 and len(sp['i_left'])==N
 nv=BASE/'research/modal_repair/evidence/audit_verdict.json';assert sha(nv)==PINS['normalization_verdict'];nd=json.loads(nv.read_bytes());assert nd['verdict']=='CONFIRMED' and nd['source_and_evidence_sha256']['research/modal_repair/evidence/independent_gauss_iv.json']==PINS['normalization']
 zp=BASE/'research/modal_repair/evidence/independent_gauss_iv.json';assert sha(zp)==PINS['normalization'];zr=json.loads(zp.read_bytes());assert zr['status']=='PASS independent arithmetic and formula reproduction; not a PDE residual certificate'
 zz=zr['values']['A00_correction'];zlo,zhi=[F(zz[v]) for v in ('lower_exact_dyadic','upper_exact_dyadic')];assert zlo<=zhi<0;z=aa(zlo).union(aa(zhi))
 archive_joins=0
 for j,p in enumerate(sp['density_polynomials']):
  ps=shift_ball([import_ball(v) for v in p],h/2)
  for q in range(7):
   enclosure=out(math.factorial(q)*ps[q]);assert F(enclosure['lower_exact'])<=jets[j][q]<=F(enclosure['upper_exact']),(j,q,'archive join');archive_joins+=1
 ip=[]
 for n in range(1,N+1):ip.append(lower_endpoint([import_ball(v) for v in sp['density_polynomials'][n-1]],import_ball(sp['i_left'][n-1]),h,F(2*n+4)))
 print(json.dumps({'utc':utc(),'stage':'canonical_endpoint','seconds':time.monotonic()-start}),flush=True)
 ep2=aa(2*tb).exp();ep3=aa(3*tb).exp();P=[[arb(0)]*(1 if j<10 else 7) for j in range(11)];Q=[[arb(0)]*(1 if j<10 else 7) for j in range(11)]
 green=[];trans=[];denom=[];pchecks=0
 for n in range(1,N+1):
  m=2*n;qplus=[];qminus=[];fpolys=[];H=(jets[n-1][0]/2+jets[n][0]/2,F(0))
  for b,beta_b in enumerate(beta):
   aa_b=beta_b+1;assert aa_b+m!=0 and aa_b-m<0;denom.append(abs(aa_b+m))
   c1,c2=coeff[n-1][b],coeff[n][b];forcing=[]
   for l in range(len(c1)):
    f=add(mul(c1[l],aa_b-m),mul(c2[l],aa_b+m))
    if l+1<len(c1):f=add(f,mul(add(c1[l+1],c2[l+1]),l+1))
    forcing.append(mul(f,F(1,2)))
   qp=inv_poly(forcing,aa_b+m);qm=[mul(q,-1) for q in inv_poly(forcing,aa_b-m)];pchecks+=2*len(forcing)
   H=add(H,mul(qp[0],-1))
   for l in range(len(qp)):
    P[b][l]+=ep2*abs(ev(add(qp[l],qm[l]),z))/2
    Q[b][l]+=ep2*abs(ev(add(qm[l],mul(qp[l],-1)),z))/2
   qplus.append(qp);qminus.append(qm);fpolys.append(forcing)
  Hval=ev(H,z)-m*ip[n-1];tr=ep2*abs(Hval)/2;trans.append((F(-m-2),[tr]))
  green.append({'n':n,'i_right':out(ip[n-1]),'H_over_R4':out(Hval),'transient_velocity_coefficient':out(tr),'plus_exact':[[[str(a),str(b)] for a,b in cs] for cs in qplus],'minus_exact':[[[str(a),str(b)] for a,b in cs] for cs in qminus]})
 D=[];Et=[];Lin=[];linear_zero=0
 for b,beta_b in enumerate(beta):
  ds=[];es=[];ls=[]
  for l in range(1 if b<10 else 7):
   ds.append(arb(0));es.append(arb(0));ls.append(arb(0))
   for j in range(N+1):
    cs=coeff[j][b];nextc=mul(cs[l+1],l+1) if l+1<len(cs) else ZERO
    dc=add(mul(cs[l],beta_b),nextc);lc=add(mul(cs[l],beta_b/k-1),mul(nextc,1/k))
    if b==0:assert lc==ZERO;linear_zero+=1
    ds[-1]+=ep3*abs(ev(dc,z));es[-1]+=ep3*(2*j+1)*abs(ev(cs[l],z));ls[-1]+=ep3*abs(ev(lc,z))
  D.append(ds);Et.append(es);Lin.append(ls)
 C={}
 def accumulate(g,p):
  assert g<=2*k-1 and g<0
  if g not in C:C[g]=[arb(0)]*len(p)
  if len(C[g])<len(p):C[g].extend([arb(0)]*(len(p)-len(C[g])))
  for l,v in enumerate(p):assert v.is_finite();C[g][l]+=v
 def prod(u,v):
  r=[arb(0)]*(len(u)+len(v)-1)
  for i,x in enumerate(u):
   for j,y in enumerate(v):r[i+j]+=x*y
  return r
 for b in range(1,11):accumulate(beta[b],Lin[b])
 products=0
 for b in range(11):
  for c in range(11):
   pd=prod(P[b],D[c]);qe=prod(Q[b],Et[c]);assert len(pd)==len(qe)
   accumulate(beta[b]+beta[c]-1,[x+y for x,y in zip(pd,qe)]);products+=1
 for g,ts in trans:
  for c in range(11):accumulate(g+beta[c],[ts[0]*(x+y) for x,y in zip(D[c],Et[c])]);products+=1
 assert products==2992 and max(len(p) for p in C.values())==13 and len(green)==261 and linear_zero==262
 print(json.dumps({'utc':utc(),'stage':'majorant','unique_exponents':len(C),'monomials':sum(map(len,C.values())),'seconds':time.monotonic()-start}),flush=True)
 # Bounds are sums of exact scalar maxima; no assumed monotonicity of a polynomial sum.
 def maximum(rate,l,T):
  assert rate>0 and l>=0 and T>=0
  x=max(T,F(l)/rate);return aa(x**l)*aa(-rate*x).exp()
 u0=aa(tb).exp()/aa(L);cases=[];rate_checks=0
 for T in (F(0),F(1),F(5),F(9)):
  absolute=sum((cc*maximum(-g,l,T) for g,p in C.items() for l,cc in enumerate(p)),arb(0));vals={'absolute_W':absolute}
  for delta in (F(0),F(1,2),F(1,2)-k):
   K=u0**aa(delta-k)*(1+u0**(-2)*aa(-2*T).exp())**aa((3-k)/2)*(1+u0**(-1)*aa(-T).exp())**aa(delta)
   bound=arb(0)
   for g,p in C.items():
    for l,cc in enumerate(p):assert k-delta-g>0;rate_checks+=1;bound+=cc*maximum(k-delta-g,l,T)
   vals['weighted_delta_'+str(delta)]=K*bound
  cases.append({'T_exact':str(T),'values':{key:out(v) for key,v in vals.items()}})
  print(json.dumps({'utc':utc(),'stage':'case','T':str(T),'values':{key:v.str(14) for key,v in vals.items()},'seconds':time.monotonic()-start}),flush=True)
 K0=u0**aa(-k)*(1+u0**(-2))**aa((3-k)/2)
 l2=arb.pi().sqrt()*aa(L)*K0*sum((cc*(aa(math.factorial(2*l))/aa(2*(k-g))**(2*l+1)).sqrt() for g,p in C.items() for l,cc in enumerate(p)),arb(0))
 cp=E/'exact_outer_coefficients.json';cp.write_text(json.dumps({'schema':'ipm-exterior-affine-coefficients-v1','input_sha256':PINS['input'],'tb_exact':str(tb),'beta_exact':[str(v) for v in beta],'correction_parameter_exact_interval':[str(zlo),str(zhi)],'rows':[{'j':j,'basis':[[[str(a),str(b)] for a,b in cs] for cs in row]} for j,row in enumerate(coeff)]},indent=2)+'\n')
 r={'utc':utc(),'status':'COMPUTED_REQUIRES_INDEPENDENT_AUDIT','source_sha256':sha(__file__),'proof_sha256':sha(BASE/'research/outer_majorant/PROOF.md'),'dependency_pins':PINS,'extract_sha256':sha(E/'final_span_extract.json'),'coefficient_sha256':sha(cp),'precision_bits':ctx.prec,'versions':{'python-flint':flint.__version__,'mpmath':mpmath.__version__},'scalars_exact':{key:str(v) for key,v in sc.items()},'c_l_exact':str(1/k),'tb_exact':str(tb),'R':out(aa(tb).exp()),'knot_interval_exact':[sp['a_exact'],sp['b_exact']],'checks':{'exact_joins':joins,'archive_joins':archive_joins,'polynomial_identities':pchecks,'denominator_pairs':len(denom),'minimum_abs_lower_denominator_exact':str(min(denom)),'leading_linear_zeros':linear_zero,'product_blocks':products,'unique_exponents':len(C),'monomials':sum(map(len,C.values())),'weighted_rate_checks':rate_checks},'green':green,'density_sums':[{'beta_exact':str(beta[b]),'D':[out(v) for v in D[b]],'E':[out(v) for v in Et[b]],'L':[out(v) for v in Lin[b]],'P':[out(v) for v in P[b]],'Q':[out(v) for v in Q[b]]} for b in range(11)],'majorant':[{'gamma_exact':str(g),'coefficients':[out(v) for v in C[g]]} for g in sorted(C)],'cases':cases,'exterior_L2_majorant':out(l2),'seconds':time.monotonic()-start,'method':'Exact rational affine jets and closed finite Green inverse; Arb384 entire-series canonical endpoint; all monomial maxima and positive Minkowski sum.','scope':'Entire exterior zeroth residual only, no derivative norm or endpoint.'}
 dest=E/'outer_result.json';dest.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'utc':utc(),'stage':'done','result_sha256':sha(dest),'L2':l2.str(18),'seconds':r['seconds']}),flush=True)
if __name__=='__main__':run()
