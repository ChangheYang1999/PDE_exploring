from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as S
z,p=S.symbols('z p');root=Path(__file__).resolve().parents[1];checks={};rows=[]
for name,A,g,d,mode,expected in [('V',S.Rational(5,2),S.Rational(21,4),S.Rational(5,2),'V',(S.Rational(8,63),S.Rational(1,70))),('Q175',S.Rational(7,4),S.Rational(27,8),S.Rational(5,2),'Q',(S.Rational(32,405),-S.Rational(11,405))),('Q2',S.Integer(2),S.Integer(5),S.Integer(3),'Q',(S.Rational(1,10),-S.Rational(1,48)))]:
 exponent=(d-1)/2 if mode=='V' else (d-2)/2;sign=1 if mode=='V' else -1
 phi=sum(sign*S.binomial(exponent,n)*z**(2*n+1)/(2*n+1) for n in range(9))
 if mode=='V':alpha=-(1+z*z)**exponent/(A+1);beta=-((d+1)*phi-z*S.diff(phi,z))/(A+1)
 else:alpha=((d+1)+z*z)*(1+z*z)**exponent/(d*(d+2));beta=-phi+z*S.diff(phi,z)/(d+2)
 h=S.series(alpha*(d*phi-z*S.diff(phi,z))-beta*S.diff(phi,z),z,0,12).removeO().expand()
 hc={j:h.coeff(z,j) for j in range(1,12,2)};beta_c={1:hc[1]/g};phi_c={1:S.Integer(0)}
 for j in range(1,12,2):
  if j!=1:phi_c[j]=S.factor((hc[j]-g*beta_c[j])/(A*p-1-(A-1)*j))
  beta_c[j+2]=S.factor(-(p-j)*(p-j-1)*(beta_c[j]+phi_c[j])/((j+1)*(j+2)))
 pn=2*d-1;values=[S.limit(phi_c[j],p,pn) for j in [3,5]]
 checks[name+'_first_coefficients']=values==list(expected)
 phip=sum(phi_c[j]*z**j for j in range(1,12,2));bp=sum(beta_c[j]*z**j for j in range(1,14,2));ap=beta_c[1]/p+sum((j-p)*(beta_c[j]+phi_c[j])*z**(j+1)/(j+1) for j in range(1,12,2))
 eq=[(A*p-1)*phip+(1-A)*z*S.diff(phip,z)+g*bp-h,S.diff(bp,z)-p*ap+z*S.diff(ap,z),-p*bp+z*S.diff(bp,z)-S.diff(ap,z)-p*phip+z*S.diff(phip,z)]
 # Verify every coefficient below the truncation error, at a generic rational degree.
 for i,e in enumerate(eq):checks[name+'_equation_'+str(i)]=all(S.simplify(S.expand(e.subs(p,S.Rational(37,7))).coeff(z,j))==0 for j in range(0,10))
 row={'mode':name,'A':str(A),'g':str(g),'d':str(d),'forcing':{str(k):str(v) for k,v in hc.items()},'first_phi3_phi5':list(map(str,values))}
 if name=='Q2':
  defect=S.simplify(hc[9]-g*S.limit(beta_c[9],p,5));res=S.limit((p-5)*phi_c[9],p,5)
  checks['Q2_compatibility']=defect==-S.Rational(1,120);checks['Q2_log_coefficient']=res==-S.Rational(1,240);row.update(defect=str(defect),log_coefficient=str(res))
  free=S.symbols('phi1');bc={1:(hc[1]-8*free)/5};pc={1:free}
  for j in range(1,10,2):
   if j!=1 and j!=9:pc[j]=S.factor((hc[j]-5*bc[j])/(9-j))
   if j!=9:bc[j+2]=S.factor(-(5-j)*(4-j)*(bc[j]+pc[j])/((j+1)*(j+2)))
  checks['Q2_beta5_free']=S.simplify(bc[5]-(S.Rational(1,1500)-free/50))==0
  checks['Q2_beta7_free']=bc[7]==0
  checks['Q2_defect_free']=S.simplify(hc[9]-5*bc[9]+S.Rational(1,120))==0
  row.update(beta5_free=str(bc[5]),beta7_free=str(bc[7]),defect_free=str(S.simplify(hc[9]-5*bc[9])))
 rows.append(row)
s,y=S.symbols('s y',positive=True);I=2*y*((s*s+y*y)**S.Rational(5,2)-y**5)/(15*s*s);force=y*(s*s+y*y)**S.Rational(3,2)
checks['scalar_inverse_equation']=S.simplify(S.Rational(5,2)*s*S.diff(I,s)+y*S.diff(I,y)-I-force)==0
for A,d,expected in [(S.Rational(5,2),S.Rational(5,2),S.Rational(3,5)),(S.Rational(7,4),S.Rational(5,2),S.Rational(9,7)),(S.Integer(2),S.Integer(3),S.Integer(2))]:checks['endpoint_exponent_'+str(A)]=2*d-1-5+4/A==expected
out={'date':datetime.now(timezone.utc).isoformat(),'checks':checks,'rows':rows,'all_pass':all(checks.values())};(root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True);assert out['all_pass']
