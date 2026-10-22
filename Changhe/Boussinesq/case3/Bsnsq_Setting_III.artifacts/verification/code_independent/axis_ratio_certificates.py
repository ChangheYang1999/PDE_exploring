"""P242 exact elimination certificates from this lane's physical-x equations.
Large lead resultant arrays are untrusted integer claims, checked against our
polynomials at a degree-complete set of points over enough independent primes.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,resource,time,traceback
os.environ.setdefault('SYMPY_GROUND_TYPES','flint')
import sympy as s
from flint import nmod_poly,nmod_mat,fmpz_poly
from axis_ratio_compatibility import ROOT,restore,polydata,rationaldata
beta,t,u=s.symbols('beta t u');delta=3*beta+2-4*t
utc=lambda:datetime.now(timezone.utc).isoformat()
checks=[];started=utc();tick=time.monotonic()
def save(name,data):(ROOT/name).write_text(json.dumps(data,indent=2)+'\n')
def ck(name,truth,**data):
 row={'name':name,'pass':bool(truth),**data};checks.append(row)
 if not truth:
  save('certificate_failure.json',{'utc':utc(),'checks':checks});raise AssertionError(name)
def positive_beta_factor(f,name):
 """Exact nonvanishing certificate: f(2+z) has one sign for every z>0."""
 ck(name+' only beta',not(f.free_symbols-{beta}))
 p=s.Poly(f,beta,domain=s.QQ)
 if p.LC()<0:p=-p
 z=s.Symbol('z');q=s.Poly(p.as_expr().subs(beta,2+z),z)
 coeff=[s.Rational(c)for c in q.all_coeffs()]
 ck(name+' shifted coefficients nonnegative',all(c>=0 for c in coeff)and any(c>0 for c in coeff),factor=str(f),shifted=str(q.as_expr()))
 return {'factor':polydata(f,(beta,)),'positive_shift_coefficients':[str(c)for c in coeff]}
def classify_removed(f,name,allow_delta=True):
 if not(f.free_symbols-{beta}):return {'kind':'beta_nonzero',**positive_beta_factor(f,name)}
 if allow_delta and s.cancel(f/delta).is_number:return {'kind':'nonzero_A0','factor':polydata(f,(beta,t))}
 raise AssertionError(name+' unexpected removable factor '+str(f))
def read_reduced(chart):
 d=json.loads((ROOT/f'chart{chart}_reduced.json').read_text());out=[];denlog=[]
 for i,r in enumerate(d['reduced']):
  num=restore(r['numerator']);den=restore(r['denominator']);fl=s.factor_list(den)
  rows=[]
  for f,m in fl[1]:rows.append({'multiplicity':int(m),**classify_removed(f,f'chart{chart} y{i+2} denominator')})
  denlog.append({'degree_y':i+2,'content':str(fl[0]),'factors':rows});out.append(num)
 for i,v in enumerate(d['divisors']):
  expr=s.sympify(v,locals={'beta':beta,'t':t,'u':u});n,den=s.fraction(s.cancel(expr))
  for kind,p in [('numerator',n),('denominator',den)]:
   for f,m in s.factor_list(p)[1]:classify_removed(f,f'chart{chart} division{i} {kind}')
 save(f'chart{chart}_denominator_certificate.json',{'polynomial_denominators':denlog,'elimination_divisors':d['divisors']})
 return out

def extract_chart(chart):
 polys=read_reduced(chart);F=[];logs=[]
 for i,p in enumerate(polys):
  content,factors=s.factor_list(p);keep=s.Integer(1);rows=[];removed_u=0
  for f,m in factors:
   if f==u and chart==0:
    removed_u=m;rows.append({'kind':'u_zero_branch_retained','multiplicity':int(m)});continue
   if s.Poly(f,u,t,beta).degree(u)>0:
    keep*=f**m;rows.append({'kind':'retained','multiplicity':int(m),'factor':polydata(f,(beta,t,u))});continue
   rows.append({'multiplicity':int(m),**classify_removed(f,f'chart{chart} numerator y{i+2}')})
  ck(f'chart{chart} y{i+2} nonconstant u polynomial',s.Poly(keep,u).degree()>0)
  if chart==0:ck(f'chart0 y{i+2} exact u factor',removed_u==1)
  F.append(s.expand(keep));logs.append({'degree_y':i+2,'content':str(content),'factors':rows})
  print('EXTRACT',chart,i+2,'degrees',s.Poly(keep,u,t,beta).degree_list(),'seconds',round(time.monotonic()-tick,2),utc(),flush=True)
 save(f'chart{chart}_factor_certificate.json',logs)
 save(f'chart{chart}_F.json',{'polynomials':[polydata(f,(beta,t,u))for f in F]})
 return F

def small_exclusion(F,label):
 p=s.Poly(F[0],u);ck(label+' first linear in u',p.degree()==1)
 c1,c0=p.all_coeffs();g=s.gcd(s.Poly(c1,beta),s.Poly(c0,beta))
 ck(label+' linear polynomial never identically zero',g.degree()==0)
 results=[s.Poly(s.resultant(F[0],f,u),beta)for f in F[1:3]]
 gg=s.gcd(*results);rows=[]
 for f,m in s.factor_list(gg.as_expr())[1]:rows.append({'multiplicity':int(m),**positive_beta_factor(f,label+' resultant gcd')})
 ck(label+' resultant gcd not zero',not gg.is_zero)
 save(label+'_exclusion.json',{'linear_coefficients':[polydata(c,(beta,))for c in [c1,c0]],'linear_coefficient_gcd':str(g.as_expr()),'resultants':[polydata(r.as_expr(),(beta,))for r in results],'gcd':polydata(gg.as_expr(),(beta,)),'nonvanishing_factors':rows})

def chart0():
 F=extract_chart(0);small_exclusion(F,'chart0_nonzero_u')

def chart1():
 F=extract_chart(1);G={};factor_rows=[]
 for j in [3,4,5]:
  r=s.resultant(F[0],F[j-2],u);content,factors=s.factor_list(r)
  main=s.Integer(1);rows=[];nt=0;nd=0
  for f,m in factors:
   if f==t:
    nt=m;rows.append({'kind':'t_zero_branch_retained','multiplicity':int(m)});continue
   if s.cancel(f/delta).is_number:
    nd=m;rows.append({'kind':'nonzero_A0','multiplicity':int(m),'factor':polydata(f,(beta,t))});continue
   if s.Poly(f,t).degree()>0:
    main*=f**m;rows.append({'kind':'retained','multiplicity':int(m),'factor':polydata(f,(beta,t))});continue
   rows.append({'multiplicity':int(m),**positive_beta_factor(f,f'chart1 Res_u 2{j}')})
  ck(f'chart1 Res_u 2{j} t branch present',nt>=1)
  ck(f'chart1 Res_u 2{j} retained polynomial',s.Poly(main,t).degree()>0)
  G[j]=s.expand(main);factor_rows.append({'pair':[2,j],'content':str(content),'factors':rows,'full_resultant':polydata(r,(beta,t))})
  print('RESU',j,'degrees',s.Poly(main,t,beta).degree_list(),'seconds',round(time.monotonic()-tick,2),utc(),flush=True)
 save('chart1_u_resultant_factors.json',factor_rows);save('chart1_G.json',{'polynomials':{str(j):polydata(g,(beta,t))for j,g in G.items()}})
 H=[];logs=[]
 for j,f in enumerate(F[:3],2):
  p=s.expand(f.subs(t,0));content,factors=s.factor_list(p);h=s.Integer(1);hasu=0;rows=[]
  for ff,m in factors:
   if ff==u:hasu=m;rows.append({'kind':'u_zero_branch_retained','multiplicity':int(m)});continue
   if s.Poly(ff,u).degree()>0:h*=ff**m;rows.append({'kind':'retained','multiplicity':int(m),'factor':polydata(ff,(beta,u))});continue
   rows.append({'multiplicity':int(m),**positive_beta_factor(ff,f'chart1 t0 y{j}')})
  ck(f'chart1 t0 y{j} exact u factor',hasu==1);H.append(s.expand(h));logs.append({'degree_y':j,'content':str(content),'factors':rows})
 save('chart1_t0_factor_certificate.json',logs);small_exclusion(H,'chart1_t0_nonzero_u')

# Modular verification is deliberately different from lead CRT reconstruction:
# direct library polynomial resultants, shifted nonconsecutive evaluation nodes,
# 61-bit primes, exact integer stopping bound, no interpolation and no CRT.
def sylvester_fixed(a,b,p):
 m=len(a)-1;n=len(b)-1;N=m+n;rows=[]
 for k in range(n):rows.append([0]*k+a[::-1]+[0]*(n-1-k))
 for k in range(m):rows.append([0]*k+b[::-1]+[0]*(m-1-k))
 return int(nmod_mat(rows,p).det())
def resultant_formal(a,b,p):
 if a[-1]and b[-1]:return int(nmod_poly(a,p).resultant(nmod_poly(b,p)))
 return sylvester_fixed(a,b,p)
def input_coeffs(expr):
 P=s.Poly(expr,t,beta);dt,db=P.degree_list();a=[[0]*(db+1)for i in range(dt+1)]
 for (i,j),c in P.terms():a[i][j]=int(c)
 return a,dt,db,sum(abs(int(c))for c in P.coeffs())
def modular_pair(i,j,gi,gj,claim):
 ai,mi,di,li=input_coeffs(gi);aj,mj,dj,lj=input_coeffs(gj)
 D=mj*di+mi*dj;H=li**mj*lj**mi;Hclaim=max(abs(x)for x in claim)
 ck(f'R{i}{j} claimed degree within formal bound',len(claim)-1<=D)
 product=1;primes=[];q=2**61-1000033;failures=[];modrows=[]
 start=time.monotonic();save(f'R{i}{j}_bound.json',{'formal_degree_bound':D,'input_t_degrees':[mi,mj],'input_beta_degrees':[di,dj],'l1_norms':[str(li),str(lj)],'true_coefficient_bound':str(H),'claimed_coefficient_bound':str(Hclaim),'required_modulus_exceeds':str(H+Hclaim),'nodes':'x_k=100003+17*k, k=0..D; degree-complete with fixed formal Sylvester dimensions at degree drops'})
 while product<=H+Hclaim:
  q=int(s.prevprime(q));p=q;primes.append(p);ck(f'R{i}{j} prime{len(primes)} exact primality',s.isprime(p))
  ci=[nmod_poly(c,p)for c in ai];cj=[nmod_poly(c,p)for c in aj];C=nmod_poly(claim,p);drops=0
  for k in range(D+1):
   x=100003+17*k;a=[int(c(x))for c in ci];b=[int(c(x))for c in cj]
   drops+=not(a[-1]and b[-1]);actual=resultant_formal(a,b,p);expected=int(C(x))
   if actual!=expected:
    failures.append({'prime':p,'node':x,'actual':actual,'claim':expected});save(f'R{i}{j}_failure.json',failures);raise AssertionError(f'R{i}{j} modular mismatch')
  product*=p;modrows.append({'prime':p,'degree_complete_points':D+1,'formal_degree_drops':drops,'all_equal':True})
  if len(primes)%5==0:print('MODVERIFY',i,j,'primes',len(primes),'bits',product.bit_length(),'needbits',(H+Hclaim).bit_length(),'elapsed',round(time.monotonic()-start,2),utc(),flush=True)
 ck(f'R{i}{j} all degree-complete modular checks',not failures)
 ck(f'R{i}{j} exact coefficient uniqueness bound',product>H+Hclaim)
 save(f'R{i}{j}_modular_certificate.json',{'started_utc':started,'ended_utc':utc(),'elapsed_seconds':time.monotonic()-start,'formal_degree_bound':D,'claimed_degree':len(claim)-1,'modulus':str(product),'bound_sum':str(H+Hclaim),'rows':modrows,'equality_over_Z':True})

def modular():
 d=json.loads((ROOT/'chart1_G.json').read_text());G={int(k):restore(v)for k,v in d['polynomials'].items()}
 c=json.loads((ROOT/'lead_resultant_claims.json').read_text());claims={k:[int(z)for z in v]for k,v in c['coefficients_ascending'].items()}
 for i,j in [(3,4),(3,5)]:modular_pair(i,j,G[i],G[j],claims[f'{i}{j}'])
 # Exact divisibility plus a good-prime coprimality test certifies a common
 # divisor is maximal over Q. This is an independent check on the integer gcd.
 R=fmpz_poly(claims['34']);S=fmpz_poly(claims['35']);g=R.gcd(S)
 q1,r1=divmod(R,g);q2,r2=divmod(S,g)
 ck('large gcd exactly divides both resultants',not r1 and not r2)
 q=2147483647
 while int(q1.leading_coefficient())%q==0 or int(q2.leading_coefficient())%q==0:q=int(s.prevprime(q))
 ck('coprimality prime exact',s.isprime(q))
 h=nmod_poly([int(c)%q for c in q1],q).gcd(nmod_poly([int(c)%q for c in q2],q))
 ck('large gcd maximal over Q by good-prime quotient gcd',h.degree()==0)
 content,factors=g.factor();rows=[]
 for k,(f,m)in enumerate(factors):
  expr=sum(s.Integer(int(c))*beta**i for i,c in enumerate(f));rows.append({'multiplicity':int(m),**positive_beta_factor(expr,'large resultant gcd factor'+str(k))})
 ck('large resultant gcd nonzero',g.degree()>=0)
 save('large_gcd_certificate.json',{'gcd_coefficients_ascending':[str(c)for c in g],'degree':g.degree(),'content':str(content),'factors':rows,'quotient_good_prime':q,'quotient_gcd_degree':h.degree(),'claim_source_sha256':c['source_sha256']})

def manufactured():
 for p in [101,1009]:
  for a,b in [([1,2],[3,4]),([0,0,1],[1,0,1]),([2,1,0],[3,0,1]),([0,0,0],[1,2,0]),([2,0,0],[1,0,3])]:
   actual=resultant_formal(a,b,p);x=s.Symbol('x');N=len(a)+len(b)-2;rows=[]
   for k in range(len(b)-1):rows.append([0]*k+a[::-1]+[0]*(len(b)-2-k))
   for k in range(len(a)-1):rows.append([0]*k+b[::-1]+[0]*(len(a)-2-k))
   exact=int(s.det(s.Matrix(rows)))%p
   ck('manufactured formal Sylvester '+str((p,a,b)),actual==exact)
 # A degree-complete check detects a hidden high degree factor missed by sparse
 # integer samples. The bound is a rigorous worst-case coefficient bound.
 x=s.Symbol('x');P=t**2+x*t+1;Q=t+2*x;R=s.Poly(s.resultant(P,Q,t),x)
 ck('manufactured exact polynomial resultant',s.expand(R.as_expr()-(2*x*x+1))==0)
 p=101;values=[resultant_formal([1,k,1],[2*k,1],p)for k in range(4)]
 ck('manufactured degree-complete evaluations',values==[(2*k*k+1)%p for k in range(4)])
 a=fmpz_poly([2,3,1]);b=fmpz_poly([3,4,1]);g=a.gcd(b);q1,r1=divmod(a,g);q2,r2=divmod(b,g)
 ck('manufactured exact gcd division',not r1 and not r2 and g==fmpz_poly([1,1]))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--stage',choices=['controls','chart0','chart1','modular','all'],required=True);args=ap.parse_args()
 if args.stage in ['controls','all']:manufactured()
 if args.stage in ['chart0','all']:chart0()
 if args.stage in ['chart1','all']:chart1()
 if args.stage in ['modular','all']:modular()
 save('certificate_checks_'+args.stage+'.json',{'started_utc':started,'ended_utc':utc(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['pass']for c in checks),'total':len(checks),'checks':checks,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'peak_RSS_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
 print('COMPLETE',args.stage,len(checks),round(time.monotonic()-tick,2),utc(),flush=True)
if __name__=='__main__':
 resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
 try:main()
 except Exception:
  save('certificate_exception.json',{'utc':utc(),'traceback':traceback.format_exc(),'checks':checks});raise
