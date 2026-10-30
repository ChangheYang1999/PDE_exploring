"""Independent exact acceptance of the Opus upper-bound review; no peer execution."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import factorial
import hashlib, json, time
from flint import fmpq, fmpq_poly as Poly, arb, ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=512
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads((B/p).read_text())
checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):
 need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');review=read('source/T2_result.json')
need('review completed59 checks',review['checks']==59 and review['fails']==[])
for rel,h in review['A']['inputs'].items():
 local='../'+rel.split('/research/',1)[1]
 need('review original binding '+rel,sha(B/local)==h)
need('review positive-pole observation explicitly FLOAT','FLOAT' in (B/'source/T2_review.md').read_text())
need('review wording actually present','exactly when' in (B/'source/T2_review.md').read_text())
x=Poly([0,1]);w=1-x
F=lambda z:fmpq(str(z))
def Dop(b,P):return (1-2*F(b)*x)*P+2*x*w*P.derivative()
def integ(P,q):
 q=Q(str(q));assert q>-1
 total=Q(0)
 for j,c in enumerate(P.coeffs()):
  v=Q(factorial(j))
  for i in range(1,j+2):v/=q+i
  total+=Q(str(c))*v
 return total
def decode(row):return row['n'],[(Q(t['b']),Poly([F(c) for c in t['P']])) for t in row['terms']]
profiles={k:decode(v) for k,v in p['profiles'].items()}
def pair(kind,U,V):
 n,terms=U;m,other=V
 if n!=m:return Q(0)
 out=Q(0)
 for b,P in terms:
  dP=Dop(b,P);d2P=Dop(b,dP);LP=n*n*P-d2P
  for c,T in other:
   dT=Dop(c,T);d2T=Dop(c,dT);LT=n*n*T-d2T
   forms={'d':dP*dT+n*n*P*T,'a':dP*dT+d2P*d2T/(n*n),'M':LP*LT/(n*n),'b':LP*d2T/(n*n),'p':LP*T}
   out+=integ(forms[kind],b+c-2)/2
 return out
def lin(U,V,q):
 assert U[0]==V[0]
 return U[0],U[1]+[(b,F(q)*P) for b,P in V[1]]
for key,U in profiles.items():
 n,terms=U
 need(key+' sufficient grouped decay',all(b>Q(1,2) for b,P in terms))
 need(key+' smooth angular origin',all(1+2*j>=n and (1+2*j-n)%2==0 for b,P in terms for j,c in enumerate(P.coeffs()) if c))
 need(key+' positive exact gradient and cross energy',pair('d',U,U)>0 and pair('a',U,U)>0)
 for key2,V in profiles.items():
  if U[0]!=V[0]:continue
  need(key+'/'+key2+' orthogonal energy',pair('M',U,V)==pair('d',U,V)+pair('a',U,V))
  need(key+'/'+key2+' signed cross',pair('b',U,V)==-pair('a',U,V))
  need(key+'/'+key2+' source pairing',pair('p',U,V)==pair('d',U,V))
fx={}
for key,expected in [('psi1','mode1'),('psi3','mode3')]:
 U=profiles[key];d=pair('d',U,U);a=pair('a',U,U);M=pair('M',U,U);b=pair('b',U,U);pv=pair('p',U,U)
 vals={'d':d,'a':a,'a6':M-d,'M2':M,'b':b,'b6':b,'p':pv}
 for k,v in vals.items():need(expected+'/'+k,v==Q(review['C'][expected][k]))
 need(expected+' exact H2 optimized',M-b*b/a==d)
 fx[key]=vals
x1=fx['psi1'];x3=fx['psi3'];H=x1['d']+x3['d'];M=x1['M2']+x3['M2'];am=x1['a']+4*x3['a'];bm=x1['b']+2*x3['b'];one=M-x1['b']**2/x1['a']
combined={'H2':H,'one_test':one,'gap':one-H,'mixed_a':am,'mixed_b':bm,'mixed_opt':M-bm*bm/am}
for k,v in combined.items():need('combined/'+k,v==Q(review['C']['combined'][k]))
need('both tests known complete H2',M-x1['b']**2/x1['a']-x3['b']**2/x3['a']==H)
q=Q(3,4)
need('mixed quadratic complete positive loss',M+2*q*bm+q*q*am-H==(1-q)**2*x1['a']+(1-2*q)**2*x3['a'])
u2=profiles['two_exponent'];a2=pair('a',u2,u2)
need('two exponent value',a2==Q(review['C']['two_exponent_a_over_pi']))
R=profiles['R1'];U=profiles['psi1'];H=pair('d',R,R);M=pair('M',R,R);b=pair('b',R,U);a=pair('a',U,U);pv=pair('p',R,U);d=pair('d',U,U);g=lin(R,U,-1);Hg=pair('d',g,g);Mg=pair('M',g,g);opt=M-b*b/a
single={'H2':H,'M2':M,'b':b,'a':a,'bound4':opt,'p':pv,'Hg2':Hg,'Ag2':Mg,'t1_value':M+2*b+a}
for k,v in single.items():need('single/'+k,v==Q(review['D']['single'][k]))
need('strict known H2 and upper',H<opt<M)
for q in [Q(z) for z in p['quadratic_tests']]+[-b/a]:
 value=M+2*q*b+q*q*a
 need('quadratic square '+str(q),value-opt==a*(q+b/a)**2 and value>=opt>H)
need('residual energy identity',H==2*pv-d+Hg)
need('residual vector identity',M+2*b+a==2*pv-d+Mg)
need('residual upper',Mg>=Hg)
uh=(U[0],[(b0,P/2) for b0,P in U[1]]);gh=lin(R,uh,-1);ph=pair('p',R,uh);dh=pair('d',uh,uh);ah=pair('a',uh,uh);bh=pair('b',R,uh);Mgh=pair('M',gh,gh);Hgh=pair('d',gh,gh)
need('half nontrivial positive difference',ph-dh==Q(p['half_test_p_minus_d'])>0)
need('half energy identity',H==2*ph-dh+Hgh)
need('half vector identity',M+2*bh+ah==2*ph-dh+Mgh)
need('half triangle exact square',dh*Mgh>=(ph-dh)**2)
Udir,Adir,Bdir=(Q(p['directed'][k]) for k in ['U','A','B'])
need('directed upper inputs',Udir>=M and Adir>=a>0 and 0<=Bdir<=abs(b))
need('directed scalar composition',Udir-Bdir*Bdir/Adir>=opt>H)
V=profiles['extra1'];R3=profiles['R3'];V3=profiles['psi3'];g11=a;g12=pair('a',U,V);g22=pair('a',V,V);s1=b;s2=pair('b',R,V);det=g11*g22-g12*g12;corr=(g22*s1*s1-2*g12*s1*s2+g11*s2*s2)/det
need('positive Gram',g11>0 and det>0)
Mtwo=M+pair('M',R3,R3);Htwo=H+pair('d',R3,R3);b3=pair('b',R3,V3);a3=pair('a',V3,V3);upper=Mtwo-corr-b3*b3/a3
vals={'H2':Htwo,'bound_gram':upper,'M2':Mtwo,'gram_det':det}
for k,v in vals.items():need('two mode/'+k,v==Q(review['D']['two_mode'][k]))
need('strict full Gram improvement',Htwo<upper<Mtwo-b*b/a-b3*b3/a3<Mtwo)
# The ungrouped beta_min is exactly3/2; one exact polynomial cancellation gains one w factor.
raw=p['cancellation_raw'];need('raw beta minimum at boundary',min(Q(t['beta']) for t in raw)==Q(3,2))
rawpoly=sum((F(t['x'])*x**t['k'] for t in raw),Poly([]))
need('raw leading cancellation',rawpoly==w)
need('effective grouped polynomial',x*rawpoly==x*w)
ce=profiles['cancellation'];cevals={k:pair(k,ce,ce) for k in ['d','a','M']}
need('admissible cancelled energies positive finite',all(v>0 for v in cevals.values()))
need('counterexample complete identity',cevals['M']==cevals['d']+cevals['a'])
# Independent exact antiderivative after w=z^2; x now denotes z.
z=x;t=1-z*z;q=F(p['pole']['q']);den=1+q*z*z
num=z**4*t**3*(2*z*z-1)*(9-48*t+48*t*t)/9
quot,rem=divmod(num,den*den)
need('polynomial division exact',num==quot*den*den+rem)
need('remainder even degree2',rem.degree()<=2 and rem[1]==0)
A=(rem[0]-rem[2]/q)/2;Bb=(rem[0]+rem[2]/q)/2
need('rational primitive derivative',rem==A*(1-q*z*z)+Bb*den)
constant=sum((Q(str(v))/Q(j+1) for j,v in enumerate(quot.coeffs())),Q(0))+Q(str(A))/4
coef=Q(str(Bb))/9
need('closed form constant',constant==Q(p['pole']['constant']))
need('closed form sqrt3 pi coefficient',coef==Q(p['pole']['sqrt3_pi_coefficient']))
value=arb(str(constant))+arb(str(coef))*arb(3).sqrt()*arb.pi()
need('closed form negative',value<0)
float_source=arb(p['pole']['float_prefix']);tolerance=arb(p['pole']['float_tolerance'])
need('float source agrees within explicit tolerance',abs(value-float_source)<tolerance)
for key in ['b_over_pi_11','b_over_pi_8']:need('same frozen float observation '+key,review['E'][key]==p['pole']['float_prefix'])
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'fixtures':{k:{j:str(v) for j,v in values.items()} for k,values in fx.items()},'combined':{k:str(v) for k,v in combined.items()},'single':{k:str(v) for k,v in single.items()},'two_mode':{k:str(v) for k,v in vals.items()},'counterexample_energies_over_pi':{k:str(v) for k,v in cevals.items()},'two_exponent_a_over_pi':str(a2),'positive_pole_closed_form':{'constant':str(constant),'sqrt3_pi_coefficient':str(coef),'ball512':value.str(145)},'peer_checks':review['checks'],'foreign_code_executed':False,'candidate_integrals_evaluated':False,'candidate_H_upper_asserted':False,'verdict':'CONFIRMED T2 analytic review acceptance of469 and independent exact rational fixtures. REFUTED necessity wording for ungrouped beta_min by exact cancellation. Candidate Hardy upper still requires complete source inputs. T1 reciprocal review remains separate.'}
with (B/'verification/result.json').open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
print('PASS',len(checks),'checks',result['elapsed_seconds'],'seconds')
print('counterexample',result['counterexample_energies_over_pi'])
print('positive pole',value.str(50))
