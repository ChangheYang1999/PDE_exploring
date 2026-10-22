"""Corner constants: Arb vectors versus rational block forms and iv integration."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,hashlib,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];E=B/'research/corner_coupling/evidence'
CASES=['SS','SL','LS','LL','SC','LC','CS','CL','CC'];WEIGHTS=[(F(129,20),F(307,100)),(F(1299,200),F(3403,1000))];GAMMA=F(1129,1000);D=F(1,2)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def ii(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def ae(x):
 assert x.is_finite()
 def f(y):
  assert y.rad()==0;m,e=y.man_exp();return F(int(m))*F(2)**int(e)
 return f(x.lower()),f(x.upper())
def ie(x):
 out=[]
 for s,m,e,b in x._mpi_:assert b>=0;out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 assert out[0]<=out[1];return tuple(out)
def pack(x,method):l,h=ae(x) if method=='arb' else ie(x);return {'lower_exact':str(l),'upper_exact':str(h),'display':str(x)}
def apow(base,p):return (aa(base).log()*aa(p)).exp()
def ipow(base,p):return iv.exp(iv.ln(ii(base))*ii(p))
def maximum(values,method):
 lohi=[ae(x) if method=='arb' else ie(x) for x in values];l=max(x[0] for x in lohi);h=max(x[1] for x in lohi)
 return aa(l).union(aa(h)) if method=='arb' else iv.mpf([ii(l).a,ii(h).b])
def public_ceil(x):
 assert x>0;e=0
 while F(10)**e<=x:e+=1
 while F(10)**(e-1)>x:e-=1
 step=F(10)**(e-4);return (x//step+1)*step

def arb_blocks(n,m):
 def v(k,c):
  if c=='S':return {k:aa(2**(k+1)*F(4,3)**(k+1)/math.factorial(k))}
  if c=='C':return {j:aa(F(4*8**j,math.factorial(j))) for j in range(k)}
  out=v(k,'C') if c=='J' else {j:aa(F(2**(j+1),math.factorial(j))) for j in range(k)}
  out[0]=out.get(0,arb(0))+(arb.pi() if c=='J' else aa(F(8,3)));return out
 def ker(p,q):return arb(math.factorial(p+q+1))/(2*arb.pi())
 def dot(x,y):return sum((vx*vy*ker(p,q) for p,vx in x.items() for q,vy in y.items()),arb(0))
 out={c:dot(v(n,'J' if c[0]=='C' else c[0]),v(m,'J' if c[1]=='C' else c[1])) for c in CASES[:-1]}
 cn,cm=v(n,'C'),v(m,'C');out['CC']=1+arb.pi()*sum((z*ker(p,0) for p,z in cn.items()),arb(0))+arb.pi()*sum((z*ker(0,q) for q,z in cm.items()),arb(0))+dot(cn,cm)
 return out

def rational_blocks(n,m):
 # Each case is exactly r+s/pi. Directly enumerate the one-coordinate estimates.
 def fact(k):
  z=1
  for j in range(2,k+1):z*=j
  return z
 def k(p,q):return F(fact(p+q+1),2)
 def small(j):return F(2**(j+1))*F(4,3)**(j+1)/fact(j)
 def large(j):return F(2**(j+1),fact(j))
 def corr(j):return F(4*8**j,fact(j))
 z=F(0);v=F(8,3);sn,sm=small(n),small(m)
 out={'SS':(z,sn*sm*k(n,m)),
 'SL':(z,sn*(v*k(n,0)+sum(large(q)*k(n,q) for q in range(m)))),
 'LS':(z,sm*(v*k(0,m)+sum(large(p)*k(p,m) for p in range(n)))),
 'SC':(sn*k(n,0),sn*sum(corr(q)*k(n,q) for q in range(m))),
 'CS':(sm*k(0,m),sm*sum(corr(p)*k(p,m) for p in range(n)))}
 out['LL']=(z,v*v*k(0,0)+v*sum(large(p)*k(p,0) for p in range(n))+v*sum(large(q)*k(0,q) for q in range(m))+sum(large(p)*large(q)*k(p,q) for p in range(n) for q in range(m)))
 out['LC']=(v*k(0,0)+sum(large(p)*k(p,0) for p in range(n)),v*sum(corr(q)*k(0,q) for q in range(m))+sum(large(p)*corr(q)*k(p,q) for p in range(n) for q in range(m)))
 out['CL']=(v*k(0,0)+sum(large(q)*k(0,q) for q in range(m)),v*sum(corr(p)*k(p,0) for p in range(n))+sum(corr(p)*large(q)*k(p,q) for p in range(n) for q in range(m)))
 out['CC']=(1+sum(corr(p)*k(p,0) for p in range(n))+sum(corr(q)*k(0,q) for q in range(m)),sum(corr(p)*corr(q)*k(p,q) for p in range(n) for q in range(m)))
 return out

def arb_L(n,u):
 x=F(n)+F(1,2)-u;y=u-F(n)+F(1,2);assert x>0 and y>0
 return sum((apow(2,-u*j) for j in range(-2,3)),arb(0))+apow(2,-3*x)/(1-apow(2,-x))+apow(2,-3*y)/(1-apow(2,-y))
def iv_L(n,u):
 gaps=[F(n)+F(1,2)-u,u-F(n)+F(1,2)];assert min(gaps)>0
 z=sum((ipow(2,-u*j) for j in [-2,-1,0,1,2]),iv.mpf(0));tails=[]
 for delta in gaps:
  ratio=ipow(2,-delta);assert ie(ratio)[1]<1;term=ratio**3;s=iv.mpf(0)
  for unused in range(128):s+=term;term*=ratio
  rem=term/(1-ratio);z+=s+rem;tails.append({'gap_exact':str(delta),'terms':128,'remainder_first_power':131,'ratio':pack(ratio,'iv'),'remainder':pack(rem,'iv')})
 return z,tails

def beta_integral(p,q,cells=4096):
 assert p>1 and q>1 and cells>0
 peak=(p-1)/(p+q-2)
 def value(t):
  if t==0 or t==1:return iv.mpf(0)
  return iv.exp(ii(p-1)*iv.ln(ii(t))+ii(q-1)*iv.ln(ii(1-t)))
 prev=ie(value(F(0)));total_lo=F(0);total_hi=F(0);peakball=ie(value(peak));critical=0
 for j in range(cells):
  a,b=F(j,cells),F(j+1,cells);nxt=ie(value(b));l=min(prev[0],nxt[0]);h=max(prev[1],nxt[1])
  if a<=peak<=b:h=max(h,peakball[1]);critical+=1
  total_lo+=l/cells;total_hi+=h/cells;prev=nxt
 assert 0<total_lo<total_hi and critical in [1,2]
 out=iv.mpf([ii(total_lo).a,ii(total_hi).b]);lo,hi=ie(out);assert lo<=total_lo<=total_hi<=hi
 return out,{'p_exact':str(p),'q_exact':str(q),'cells':cells,'peak_exact':str(peak),'critical_cells':critical,'sum_lower_exact':str(total_lo),'sum_upper_exact':str(total_hi),'enclosure':pack(out,'iv'),'method':'Unimodal endpoint/peak Riemann bounds; all mesh and accumulation exact rational.'}

def grouped_coefficients(d):
 out={}
 for n in range(6):
  for m in range(4):
   coeff=F(0)
   if m<=2:coeff+=(7-n+d)/(math.factorial(5-n)*math.factorial(2-m))
   if n<=4:coeff+=(4-m+d)/(math.factorial(4-n)*math.factorial(3-m))
   if coeff:out[(n,m)]=coeff
 return out

def constants(a,b,gamma):
 assert F(11,2)<a<F(13,2) and F(5,2)<b<F(7,2) and 1<gamma<2
 A=a+b;d=D;rows=[];arbs={};ivs={};overlaps=0;coef=grouped_coefficients(d)
 for (n,m),co in coef.items():
  u,v=a-6+n,b-3+m;ab=arb_blocks(n,m);forms=rational_blocks(n,m);ib={c:ii(r)+ii(s)/iv.pi for c,(r,s) in forms.items()}
  pairs={};
  for c in CASES:
   al,ah=ae(ab[c]);il,ih=ie(ib[c]);assert max(al,il)<=min(ah,ih);overlaps+=1;pairs[c]={'arb':pack(ab[c],'arb'),'iv':pack(ib[c],'iv'),'rational_plus_inverse_pi':[str(x) for x in forms[c]]}
  ba=maximum(ab.values(),'arb');bi=maximum(ib.values(),'iv');la,ma=arb_L(n,u),arb_L(m,v);li,lt=iv_L(n,u);mi,mt=iv_L(m,v)
  ca=apow(2,abs(u)+abs(v))*ba*la*ma;ci=ipow(2,abs(u)+abs(v))*bi*li*mi
  for x,y in [(ba,bi),(la,li),(ma,mi),(ca,ci)]:
   al,ah=ae(x);il,ih=ie(y);assert max(al,il)<=min(ah,ih);overlaps+=1
  arbs[n,m]=ca;ivs[n,m]=ci
  rows.append({'N':n,'M':m,'u_exact':str(u),'v_exact':str(v),'coefficient_exact':str(co),'cases':pairs,'B':{'arb':pack(ba,'arb'),'iv':pack(bi,'iv')},'Lx':{'arb':pack(la,'arb'),'iv':pack(li,'iv')},'Ly':{'arb':pack(ma,'arb'),'iv':pack(mi,'iv')},'C':{'arb':pack(ca,'arb'),'iv':pack(ci,'iv')},'geometric_tails':[lt,mt]})
 betaA=aa(a+F(1,2)).gamma()*aa(b+F(1,2)).gamma()/aa(A+1).gamma();betaI,integral=beta_integral(a+F(1,2),b+F(1,2));bl,bh=ae(betaA);il,ih=ie(betaI);assert il<=bl<=bh<=ih
 velA=sum((aa((2+i+d)/(math.factorial(i)*math.factorial(j)))*arbs[5-i,2-j] for i in range(6) for j in range(3)),arb(0))+sum((aa((1+j+d)/(math.factorial(i)*math.factorial(j)))*arbs[4-i,3-j] for i in range(5) for j in range(4)),arb(0))
 velI=sum((ii(co)*ivs[n,m] for (n,m),co in coef.items()),iv.mpf(0));h0=(9+2*d)/(3*math.factorial(4)*math.factorial(2))
 ma=(aa(4)*apow(d,20-2*A)/(aa(13-2*a)*aa(7-2*b))).sqrt();mi=iv.sqrt(ii(2)*ipow(d,13-2*a)/ii(13-2*a))*iv.sqrt(ii(2)*ipow(d,7-2*b)/ii(7-2*b))
 strA=(betaA*apow(2,A-2)/aa(A-2)).sqrt()/arb.pi();strI=iv.sqrt(betaI*ipow(2,A-2)/ii(A-2))/iv.pi
 ta=(2*betaA/aa(4-2*gamma)).sqrt();ti=iv.sqrt(2*betaI/ii(4-2*gamma))
 fa={0:aa(d)/(arb.pi()*apow(1-d,3))};fr={0:d/(1-d)**3}
 for j in range(1,8):fa[j]=arb(math.factorial(j+1))/(2*arb.pi()*apow(1-d,j+2));fr[j]=F(math.factorial(j+1),2)/(1-d)**(j+2)
 s1a=sum((aa(F(math.comb(5,p)*math.comb(2,q),math.factorial(5)*math.factorial(2))*(2+p+d))*fa[7-p-q] for p in range(6) for q in range(3)),arb(0))
 s2a=sum((aa(F(math.comb(4,p)*math.comb(3,q),math.factorial(4)*math.factorial(3))*(1+q+d))*fa[7-p-q] for p in range(5) for q in range(4)),arb(0))
 # Factorials cancel before independent exact finite summation.
 s1r=sum((2+p+d)*fr[7-p-q]/(math.factorial(p)*math.factorial(5-p)*math.factorial(q)*math.factorial(2-q)) for p in range(6) for q in range(3))
 s2r=sum((1+q+d)*fr[7-p-q]/(math.factorial(p)*math.factorial(4-p)*math.factorial(q)*math.factorial(3-q)) for p in range(5) for q in range(4))
 unitA=velA+aa(h0)*strA*ma;unitI=velI+ii(h0)*strI*mi
 farA=ma*ta*(s1a+s2a+aa(h0)/arb.pi());farI=mi*ti*ii(s1r+s2r+h0)/iv.pi
 compA=(unitA**2+farA**2).sqrt();compI=iv.sqrt(unitI**2+farI**2)
 names=['beta','M_d','C_str','T_gamma','S1','S2','C_vel','C_unit','C_far','C_comp'];av=[betaA,ma,strA,ta,s1a,s2a,velA,unitA,farA,compA];ivv=[betaI,mi,strI,ti,ii(s1r)/iv.pi,ii(s2r)/iv.pi,velI,unitI,farI,compI];summary={}
 for name,x,y in zip(names,av,ivv):
  al,ah=ae(x);il,ih=ie(y);assert 0<max(al,il)<=min(ah,ih);overlaps+=1;up=max(ah,ih);pub=public_ceil(up);assert up<pub
  summary[name]={'arb':pack(x,'arb'),'iv':pack(y,'iv'),'joint_upper_exact':str(up),'public_strict_upper_exact':str(pub)}
 return {'a_exact':str(a),'b_exact':str(b),'gamma_exact':str(gamma),'d_exact':str(d),'H0_exact':str(h0),'S1_times_pi_exact':str(s1r),'S2_times_pi_exact':str(s2r),'shifted_rows':rows,'positive_beta_integral':integral,'constants':summary,'overlaps':overlaps}

def main():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));contracts=0;rejects=0
 for q in [F(0),F(-1,3),F(7,8),F(1299,200),F(1129,1000)]:
  for lo,hi in [ae(aa(q)),ie(ii(q))]:assert lo<=q<=hi;contracts+=1
 for x in [iv.mpf('inf'),iv.mpf('-inf'),iv.mpf('nan')]:
  try:ie(x)
  except AssertionError:rejects+=1
  else:raise AssertionError('nonfinite accepted')
 rows=[constants(a,b,GAMMA) for a,b in WEIGHTS]
 dep=B/'research/double_remainder/evidence/verdict.json';assert sha(dep)=='a25eec10e3cdec6bc94fbd46df0e5413c68160ec0a7df2b13eff9ca408be991e'
 # Dependency source pins are all immutable and are rehashed here.
 manifest=json.loads(dep.read_text())
 for rel,h in manifest['files'].items():assert sha(B/rel)==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_METHOD_CONSTANTS','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/corner_coupling/PROOF.md'),'dependency_verdict_sha256':sha(dep),'runtime':{'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_decimal_digits':iv.dps},'checks':{'rows':2,'shifted_rows':sum(len(x['shifted_rows']) for x in rows),'overlaps':sum(x['overlaps'] for x in rows),'beta_containments':2,'endpoint_containments':contracts,'nonfinite_rejections':rejects},'rows':rows,'seconds':time.monotonic()-start,'scope':'Conditional local C8-factor zeroth coupling remainder only. No current-trial application, derivative estimates or inverse.'}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='rows'}));print(json.dumps([{'a':x['a_exact'],'b':x['b_exact'],'bounds':{name:v['public_strict_upper_exact'] for name,v in x['constants'].items()}} for x in rows]))
if __name__=='__main__':main()
