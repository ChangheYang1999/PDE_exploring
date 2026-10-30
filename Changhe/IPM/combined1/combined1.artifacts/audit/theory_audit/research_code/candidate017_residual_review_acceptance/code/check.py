"""Independent finite monomial integration and review acceptance. No peer code executes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import factorial,comb
import hashlib,json,gzip,time
B=Path(__file__).resolve().parents[1];tick=time.monotonic();checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(c,msg):
 if not c:raise AssertionError(msg)
 checks.append(msg)
def load(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_text())
m=load(B/'data/manifest.json')
for r in m:ck(sha(B/r['local'])==r['sha256'],'input '+r['local'])
ck(load(B/'data/PROOF_FIRST.json')['proof_sha256']==sha(B/'PROOF.md'),'proof first')
P=load(B/'data/parameters.json');T2=load(B/'source/T2_result.json');X=load(B/'source/T1_extract.json')
ck(T2['checks']==18 and T2['fails']==[],'T2 final18checks');ck('checks 79 failures 0\nRESULT PASS' in (B/'source/T1_log.txt').read_text(),'T1 final79checks')
def add(a,b,k=F(1)):
 out=dict(a)
 for key,c in b.items():out[key]=out.get(key,F(0))+k*c
 return {key:c for key,c in out.items() if c}
def mul(a,b):
 out={}
 for (m,s),c in a.items():
  for (j,t),d in b.items():out[(m+j,s+t)]=out.get((m+j,s+t),F(0))+c*d
 return {key:c for key,c in out.items() if c}
def shift(a,k):return {(m+k,s):c for (m,s),c in a.items()}
def scale(a,c):return {k:c*v for k,v in a.items() if c*v}
def deriv(a):
 out={}
 for (m,s),c in a.items():
  out=add(out,{(m-1,s):m*c,(m+1,s+1):-2*s*c})
 return out
def source(a):return {(m,F(s)):F(num,den) for num,den,m,s in a}
def integrate(a):
 val=F(0)
 for (m,s),c in a.items():
  q=F(m+1,2);z=s-q;ck(q.denominator==1 and q>0 and z>0,'convergent monomial '+str((m,s)))
  j=int(q);prod=F(1)
  for k in range(j):prod*=z+k
  val+=c*F(factorial(j-1),2)/prod
 return val
def lap(n,u):return add(add(deriv(deriv(u)),shift(deriv(u),-1)),shift(u,-2),-n*n)
def normgrad(n,u):return integrate(add(shift(mul(deriv(u),deriv(u)),1),shift(mul(u,u),-1),n*n))
def parts(n,u,f):
 up=deriv(u);yp=add(shift(deriv(up),1),up);lp=lap(n,u)
 return {'d':normgrad(n,u),'a':integrate(add(shift(mul(up,up),1),shift(mul(yp,yp),1),F(1,n*n))),'p':integrate(shift(mul(f,u),1)),'b':integrate(shift(mul(f,yp),2))/n**2,'Q':integrate(shift(mul(f,f),3)),'R2':integrate(shift(mul(add(f,lp),add(f,lp)),3)),'lap2':integrate(shift(mul(lp,lp),3)),'cross':integrate(shift(mul(f,lp),3))}
def validate(a,n,name):
 ck(a['lap2']==n*n*(a['a']+a['d']),name+' Laplacian square')
 ck(a['cross']==n*n*(a['b']-a['p']),name+' cross')
 ck(a['R2']==a['Q']+2*n*n*(a['b']-a['p'])+n*n*(a['a']+a['d']),name+' residual identity')
 ck(a['b']**2<=a['Q']*a['a']/n**2,name+' Cauchy b')
 ck(a['p']**2<=a['Q']*a['d']/n**2,name+' Cauchy p')
 ck(a['cross']**2<=n*n*a['Q']*(a['a']+a['d']),name+' corrected Cauchy cross')
examples={}
for row in P['fixtures']:
 n=row['n'];a=parts(n,source(row['u']),source(row['f']));validate(a,n,row['name'])
 for key,val in T2['examples'][row['name']].items():ck(a[key]==F(val),row['name']+' exact '+key)
 examples[row['name']]={k:str(v) for k,v in a.items()}
c=P['counterexample'];n=c['n'];u=source(c['u']);f=source(c['f']);a=parts(n,u,f);validate(a,n,'counterexample')
# Functional equality of the independently differentiated Laplacian and saved f, after S=1+r2.
diff=add(lap(n,u),f,-1);top=max(s for m,s in diff);out={}
for (power,s),coef in diff.items():
 k=top-s;ck(k.denominator==1 and k>=0,'common denominator exponent')
 for j in range(int(k)+1):out[power+2*j]=out.get(power+2*j,F(0))+coef*comb(int(k),j)
ck(all(x==0 for x in out.values()),'counterexample F exactly Delta psi')
expected={'d':'6/35','a':'2/63','p':'-6/35','b':'2/63','Q':'64/35','cross':'64/35','R2':'256/35'}
for key,val in expected.items():ck(a[key]==F(val),'counterexample '+key)
ck(a['a']+a['d']==F(64,315),'counterexample energy sum')
ck(F(64,105)**2==a['Q']*(a['a']+a['d']),'omitted-n RHS exact square')
ck(a['cross']==3*F(64,105) and a['cross']>F(64,105),'omitted-n counterexample factor3')
K=P['known_riesz'];u=source(K['u']);w=source(K['w']);f=scale(lap(1,w),-1);z=parts(1,u,f);validate(z,1,'known Riesz');H2=normgrad(1,w);res2=normgrad(1,add(w,u,-1))
for key,val in T2['riesz_example'].items():
 actual={'H2_over_pi':H2,'residual_H2_over_pi':res2}.get(key,z.get(key));ck(actual==F(val),'known Riesz '+key)
le=lambda x,y,z:x<=y+z or (x-y-z)**2<=4*y*z
ck(le(H2,z['d'],z['R2']) and le(z['d'],H2,z['R2']),'known Riesz triangles')
ck(res2<=z['R2'] and z['p']**2<=z['d']*H2,'known Riesz Hardy dual')
for row in T2['trial_family_orders']:
 n=row['n'];k=row['k'];beta=F(row['beta']);alpha=3-2*beta
 ck(beta>F(3,2) and k>=-1 and (3+2*k-n)>=0 and (3+2*k-n)%2==0,'admissible endpoint fixture '+str(n,k) if False else 'admissible endpoint fixture '+str((n,k,beta)))
 vals=[alpha**2+n*n,alpha**2+alpha**4/F(n*n),(alpha**2-n*n)**2]
 ck(vals==list(map(F,row['lead_inf'])),'three exact leading coefficients '+str((n,k,beta)))
 ck(6-4*beta<0 and 5-4*beta<-1,'decay and integrability '+str((n,k,beta)))
ck((3-2*F(3,2))==0 and (3-2*F(3,2))**2+1==1,'beta endpoint cancellation with angular energy1')
A=B/'../candidate017_partial_replay_audit';R=load(A/'source/N4_result.json.gz');O=load(A/'verification/result.json')
ck(hashlib.sha256(gzip.decompress((A/'source/N4_result.json.gz').read_bytes())).hexdigest()==X['result_sha256'],'T1 extract original result hash')
for key in ['raw_sha256','H_lower_square_exact','H_strict_lower_exact']:
 ck(R[key]==X[key] and O[key]==X[key],'accepted source '+key)
ck([q['n'] for q in X['modes']]==list(range(1,32,2)),'sixteen distinct frequencies')
for x,r in zip(X['modes'],R['modes']):
 for key in ['n','sha256','quotient_strict_lower_exact','independent_hres']:ck(x[key]==r[key],'T1 extracted mode '+str(x['n'])+' '+key)
 ck(F(x['quotient_strict_lower_exact'])>0,'positive floor '+str(x['n']))
S=sum((F(x['quotient_strict_lower_exact'])**2 for x in X['modes']),F(0));HL=F(X['H_strict_lower_exact'])
ck(S==F(X['H_lower_square_exact']) and HL**2<S,'accepted dual lower sum')
ck(F('.377511443340457')<S<F('.377511443340458'),'T1 squared interval')
ck(F('.614419598760')<HL<F('.614419598761'),'T1 H lower display')
ck(F('.6144195987')<HL<F('.6165956396'),'conditional interval consistency only')
mode_checks=[]
for ns in ['1','3']:
 n=int(ns);raw=gzip.decompress((A/f'source/mode_{n:03d}.json.gz').read_bytes());M=json.loads(raw);e=X['residual'][ns];rr=M['residual_trial']
 ck(hashlib.sha256(raw).hexdigest()==e['record_sha256'],'mode source hash '+ns)
 for k in ['H_mode_strict_lower_exact','H_mode_strict_upper_exact']:ck(e[k]==rr[k],'T1 residual endpoint '+ns+' '+k)
 ck(e['dual_quotient_strict_lower_exact']==M['dual_quotient_strict_lower_exact'],'T1 dual floor '+ns)
 ck(rr['gradient_ball'].startswith(e['gradient_ball_head']) and rr['residual_ball']==e['residual_ball_text'],'T1 diagnostic ball excerpts '+ns)
 lo,hi,q=map(F,[e['H_mode_strict_lower_exact'],e['H_mode_strict_upper_exact'],e['dual_quotient_strict_lower_exact']]);ck(0<lo<q<hi,'same-mode lower comparison '+ns)
 display={1:('.3759840488468','.3759983211623','1.4272316e-5'),3:('.3718015564841','.3718071978901','5.641406e-6')}[n]
 ck(F(display[0])<lo<hi<F(display[1]),'T1 outward mode display '+ns);ck(hi-lo<F(display[2]),'T1 width '+ns)
 if n==1:ck((hi-lo)/lo<F('3.8e-5'),'T1 relative width')
 target=F('4.7e-14' if n==1 else '9.0e-14');ck(abs(q-lo-target)<F('0.05e-14'),'T1 approximate dual difference '+ns)
 mode_checks.append({'n':n,'width_exact':str(hi-lo),'relative_width_exact':str((hi-lo)/lo),'dual_minus_residual_lower_exact':str(q-lo)})
ck(R['complete_H_upper'].startswith('OPEN') and R['complete_E2_and_017_less_than007'].startswith('OPEN'),'candidate upper scope OPEN')
ck('sqrt(Qn (a + d))' in (B/'source/T2_review.md').read_text(),'frozen missing-n text recorded')
for r in m:ck(sha(B/r['local'])==r['sha256'],'unchanged '+r['local'])
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'examples':examples,'counterexample':{k:str(v) for k,v in a.items()},'known_riesz':{'H2_over_pi':str(H2),'residual_H2_over_pi':str(res2),**{k:str(v) for k,v in z.items()}},'mode_comparisons':mode_checks,'H_lower_square_exact':str(S),'H_strict_lower_exact':str(HL),'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED both Opus identities, cutoff/duality and T1 exact composition; REFUTED missing n in frozen T2 R2. General local integrability required and supplied by accepted017 smooth structure. Full candidate upper/E2 OPEN.'}
(B/'verification/result.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS',len(checks),result['elapsed_seconds'],sha(B/'verification/result.json'))
