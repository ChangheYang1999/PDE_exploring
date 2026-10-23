"""Result282: independent exact III/IV algebra, branch and determinant check.
Only our own polynomial/rational libraries, no Sympy or producer code.
"""
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import json,hashlib,time,resource,traceback
from exact_polynomial_275 import P,F,mul,peval,sylvester,bareiss,gaussian
import exact_rational_282 as Q
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
R=Path('research/degree19_grouped_moment_obstruction');V=R/'verification';Rat=Q.Rat;ps=Q.ps;checks=[];details={}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,value,evidence=None):
 checks.append(dict(name=name,passed=bool(value),evidence=evidence))
 if not value:raise AssertionError(name)
def readp(rows,dim=None):
 if dim is None:dim=len(rows[0]['powers'])
 return P({tuple(t['powers']):F(t['coefficient'])for t in rows},dim)
def eqcheck(name,eq,data):
 num=readp(data['numerator_terms']);den=readp(data['denominator_terms']);prim=readp(data['primitive_terms']);c=F(data['primitive_content']);own=eq.denominator();quot,rem=Q.divpoly(own,den)
 ck(name+' exact rational identity',eq.num*den==num*own)
 ck(name+' denominator divides allowed product',not rem.a and bool(quot.a),eq.den)
 ck(name+' scalar-only primitive content',c!=0 and num==c*prim and prim.primitive()==(prim,F(1)))
 return prim

def signcheck(name,sc):
 product=[F(sc['constant'])];ck(name+' nonzero constant',product[0]!=0)
 for j,f in enumerate(sc['factors']):
  co=[F(c)for c in f['coefficients_ascending']];shift=[sum(co[i]*comb(i,k)for i in range(k,len(co)))for k in range(len(co))]
  ck(name+' shift identity '+str(j),shift==[F(x)for x in f['shifted_coefficients_ascending']])
  ck(name+' strict positive shift '+str(j),all(c>0 for c in shift))
  ck(name+' positive exponent '+str(j),isinstance(f['power'],int)and f['power']>0)
  for _ in range(f['power']):product=mul(product,co)
 ck(name+' exact factor convolution',product==[F(c)for c in sc['coefficients_ascending']]);return product

def determinant(name,polys,data):
 A,B=polys;da,db=A.degree(0),B.degree(0);bound=db*A.degree(1)+da*B.degree(1)
 ck(name+' saved degrees',[[p.degree(0),p.degree(1)]for p in polys]==data['degrees'])
 ck(name+' resultant degree bound',bound==data['degree_bound'])
 co=signcheck(name,data['resultant']);ck(name+' coefficient degree within bound',co[-1]!=0 and len(co)-1<=bound)
 ck(name+' integer resultant coefficients',all(c.denominator==1 for c in co))
 for v in range(1,bound+3):
  mat=sylvester(A.specialize(v,da),B.specialize(v,db));det,nd,ns=bareiss(mat)
  ck(name+' exact determinant n='+str(v),det==peval(co,v),dict(divisions=nd,swaps=ns,determinant=str(det)))
 for v in [F(1),F(2),F(3,2)]:ck(name+' Gaussian n='+str(v),gaussian(sylvester(A.specialize(v,da),B.specialize(v,db)))==peval(co,v))
 details[name]=dict(degree_bound=bound,degree=len(co)-1,finite_parameter_values_checked=bound+2,meaning='Exact polynomial identity by degree bound, then global factor sign proof.')
 print('DETERMINANT DONE',name,len(checks),datetime.now(timezone.utc).isoformat(),flush=True)

def progress(stage):
 (V/'TYPES34_PROGRESS.json').write_text(json.dumps(dict(stage=stage,utc=datetime.now(timezone.utc).isoformat(),checks=checks,details=details),indent=2)+'\n');print('PROGRESS',stage,len(checks),flush=True)

def cubic_moments(x,y,n,tau,invn):
 u3=((n+3)-(n+2)*x+(n+1)*y)*invn;uc=[Rat(1),-x,y,-u3];pu=ps(uc,5)
 w1=-(tau+4*pu[1])*F(1,2);c1=-w1;w2=-(tau**2+4*pu[2])*F(1,2);c2=-(w2+c1*w1)*F(1,2);c3=(3+2*c1+c2)*invn-1-c1-c2;wc=[Rat(1),c1,c2,c3];pw=ps(wc,5)
 mm=[tau**j+4*pu[j]+2*pw[j]for j in range(1,6)]
 return mm,uc,wc

def monic_log(co):
 L=len(co)-1;return sum((L-j)*co[j]for j in range(L)),sum(co)

start=datetime.now(timezone.utc).isoformat();out=dict(status='RUNNING',started_utc=start)
try:
 cert=json.loads((V/'types_III_IV_certificate.json').read_text());ck('initial proof binding',sha(R/'INITIAL_REDUCTION.md')==cert['initial_proof_sha256']);ck('discovery binding',sha('independent_code/derive_degree19_types34.py')==cert['driver_sha256'])
 for p in json.loads((V/'TYPES34_BINDINGS.json').read_text())['files']:ck('library/proof binding '+Path(p['path']).name,sha(p['path'])==p['sha256'])
 # New necessary-elimination identity over five formal variables.
 xx,bb,cc,rr,ss=[P.var(i,5)for i in range(5)]
 ck('universal quadratic-linear resultant identity',rr**2*(12*xx**2+bb*xx+cc)-(rr*xx+ss)*(12*rr*xx+bb*rr-12*ss)==12*ss**2-bb*ss*rr+cc*rr**2)
 ck('universal first remainder elimination',P.var(0,4)*P.var(3,4)-P.var(1,4)*P.var(2,4)==P.var(3,4)*P.var(0,4)-P.var(2,4)*P.var(1,4))
 data=cert['cases']['III'];px,py,pn=[P.var(i,3)for i in range(3)];DD=19+2*pn;Q.configure([DD,pn],3);x,y,n=Rat(px),Rat(py),Rat(pn);tau=Rat(DD-1,{0:1});mm,uc,wc=cubic_moments(x,y,n,tau,Rat(1,{1:1}))
 ck('III first moment zero',not mm[0].num.a);ck('III second moment zero',not mm[1].num.a)
 du,u=monic_log(uc);dw,w=monic_log(wc);ck('III U logarithm',not(du+n*u).num.a);ck('III W logarithm',not(dw-n*w).num.a)
 pm=eqcheck('III moment3',mm[2],data['moment3']);ck('III moment3 linear y',pm.degree(1)==1)
 C1=P({(i,k):c for(i,j,k),c in pm.a.items()if j==1});C0=P({(i,k):c for(i,j,k),c in pm.a.items()if j==0});ck('III exact C1',C1==readp(data['C1_terms']));ck('III exact C0',C0==readp(data['C0_terms']))
 px,pn=P.var(0),P.var(1);DD=19+2*pn;Q.configure([DD,pn],2)
 polys=[eqcheck('III pivot '+str(i),Rat(p),r)for i,(p,r)in enumerate(zip([C1,C0],data['pivot_branch']['equations']))]
 determinant('III pivot',polys,data['pivot_branch']);progress('III pivot complete')
 Q.configure([DD,pn,C1],2);x,n=Rat(px),Rat(pn);y=Rat(-C0,{2:1});tau=Rat(DD-1,{0:1});mm,uc,wc=cubic_moments(x,y,n,tau,Rat(1,{1:1}));ck('III eliminated moment3 identically zero',not mm[2].num.a)
 polys=[eqcheck('III generic moment'+str(j+4),e,r)for j,(e,r)in enumerate(zip(mm[3:],data['generic']['equations']))]
 determinant('III generic',polys,data['generic']);progress('III complete')
 # Three-variable original IV moment polynomials, before division in x.
 data=cert['cases']['IV'];px,pt,pn=[P.var(i,3)for i in range(3)];DD=19+2*pn;L1=-pn-2*pt;L2=pn+pt;Q.configure([DD,pt,L1,L2],3);x,t,n=Rat(px),Rat(pt),Rat(pn);tau=Rat(DD-1,{0:1});alpha=1-Rat(1,{1:1});v=-(tau+6*alpha+4*x)*F(1,2);c=(2-x)*Rat(1,{2:1})-1+x;k=(2-v)*Rat(1,{3:1})-1+v;uc=[Rat(1),-x,c];wc=[Rat(1),-v,k];pu=ps(uc,4);pw=ps(wc,4);mm=[tau**j+6*alpha**j+4*pu[j]+2*pw[j]for j in range(1,5)]
 ck('IV first moment zero',not mm[0].num.a);du,u=monic_log(uc);dw,w=monic_log(wc);ck('IV U logarithm',not(du-Rat(L1)*u).num.a);ck('IV W logarithm',not(dw-Rat(L2)*w).num.a)
 for j,(m,r)in enumerate(zip(mm[1:],data['moments'])):eqcheck('IV original moment'+str(j+2),m,r)
 raw=[(m.num,m.den.copy())for m in mm[1:]]
 for j,m in enumerate(mm[1:]):ck('IV denominator independent of x '+str(j),m.denominator().degree(0)==0)
 pt,pn=P.var(0),P.var(1);DD=19+2*pn;L1=-pn-2*pt;L2=pn+pt;Q.configure([DD,pt,L1,L2],2)
 def coeffs(record):
  p,de=record;return [Rat(P({(j,k):v for(i,j,k),v in p.a.items()if i==power}),de)for power in range(p.degree(0)+1)]
 mc=[coeffs(r)for r in raw];ck('IV quadratic degree',len(mc[0])==3);C,B,A=mc[0];ck('IV quadratic leading constant12',A.num==12*A.denominator());eqcheck('IV B',B,data['B']);eqcheck('IV C',C,data['C'])
 def rem(poly):
  r0=Rat(0);r1=Rat(0);power=[Rat(1),Rat(0)]
  for c in poly:
   r0=r0+c*power[0];r1=r1+c*power[1];power=[-C*power[1]*F(1,12),power[0]-B*power[1]*F(1,12)]
  return r1,r0
 r1,r0=rem(mc[1]);r3,r2=rem(mc[2])
 for j,(e,r)in enumerate(zip([r1,r0,r3,r2],data['remainders'])):eqcheck('IV remainder '+str(j),e,r)
 N1=r1*r2-r0*r3;N2=12*r0**2-B*r0*r1+C*r1**2
 polys=[eqcheck('IV generic necessary '+str(j),e,r)for j,(e,r)in enumerate(zip([N1,N2],data['generic']['equations']))];progress('IV algebra complete')
 determinant('IV generic',polys,data['generic']);progress('IV generic complete')
 # Reconstruct exceptional branches afresh; never substitute into singular formulas.
 for branch in ['L1zero','L2zero']:
  pn=P.var(0,1);DD=19+2*pn;Q.configure([DD,pn],1);n=Rat(pn);tau=Rat(DD-1,{0:1});ni=Rat(1,{1:1})
  if branch=='L1zero':
   t=-n*F(1,2);alpha=1+2*ni;x=Rat(2);v=-(tau+6*alpha+4*x)*F(1,2);k=(2-v)*2*ni-1+v;c=(tau**2+6*alpha**2+4*x**2+2*v**2-4*k)*F(1,8)
  else:
   t=-n;alpha=1+ni;v=Rat(2);x=-(tau+6*alpha+2*v)*F(1,4);c=(2-x)*ni-1+x;k=(tau**2+6*alpha**2+4*x**2-8*c+2*v**2)*F(1,4)
  db=data['branches'][branch]
  for name,val in [('t',t),('alpha',alpha),('x',x),('v',v),('c',c),('k',k)]:eqcheck('IV '+branch+' value '+name,val,db['values'][name])
  ck('IV '+branch+' reciprocal node',(1-alpha).num*t.num==(1-alpha).denominator()*t.denominator())
  uc=[Rat(1),-x,c];wc=[Rat(1),-v,k];du,u=monic_log(uc);dw,w=monic_log(wc);ck('IV '+branch+' logarithm U',not(du-(-n-2*t)*u).num.a);ck('IV '+branch+' logarithm W',not(dw-(n+t)*w).num.a)
  up,wp=ps(uc,4),ps(wc,4);mom=[tau**j+6*alpha**j+4*up[j]+2*wp[j]for j in range(1,5)]
  ck('IV '+branch+' moment1 zero',not mom[0].num.a);ck('IV '+branch+' moment2 zero',not mom[1].num.a)
  for j,(m,r,sc)in enumerate(zip(mom[2:],db['moments'],db['sign_certificates'])):
   prim=eqcheck('IV '+branch+' moment'+str(j+3),m,r);co=signcheck('IV '+branch+' primitive sign'+str(j+3),sc);ck('IV '+branch+' primitive sign polynomial'+str(j+3),prim==P({(i,):c for i,c in enumerate(co)},1))
  progress('IV '+branch+' complete')
 # Two admissible integers in the three-node singleton branch.
 for row in cert['special_e2']:
  nn=row['n'];ck('special allowed integer '+str(nn),nn in(1,2));z=F(19+2*nn,18+2*nn);v1=z*(1-F(3,nn));b1=-(1+2*v1)/8;b2=(1+2*v1**2+8*b1**2)/16;der=z*z-b1*z+b2+(z-v1)*(2*z-b1)
  own=dict(z=z,v1=v1,pair_sum=b1,pair_product=b2,pi_prime=der)
  for key,val in own.items():ck('special exact '+str(nn)+' '+key,val==F(row[key]))
  ck('special derivative nonzero '+str(nn),der!=0);ck('special moments '+str(nn),1+2*v1+8*b1==0 and 1+2*v1*v1+8*(b1*b1-2*b2)==0)
 ck('special covers exactly1and2',[r['n']for r in cert['special_e2']]==[1,2])
 out.update(status='PASS')
except Exception:
 out.update(status='FAIL',error=traceback.format_exc());raise
finally:
 out.update(finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,details=details,driver_sha256=sha(__file__),proof_sha256=sha(R/'TYPES34_PROOF.md'),certificate_sha256=sha(V/'types_III_IV_certificate.json'),rational_library_sha256=sha('independent_code/exact_rational_282.py'),scope='Only III,IV and special integer branch; complete degree19 also needs13cases and exact partition enumeration.')
 (V/'TYPES34_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),out['finished_utc'],flush=True)
