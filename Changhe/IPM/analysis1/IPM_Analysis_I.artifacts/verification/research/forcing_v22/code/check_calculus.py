"""Independent closed coefficient formula and exact Leibniz enumeration."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,ast,math,time,sys,copy
import sympy as s
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];start=time.monotonic();src=D/'source/src/cert_forcing2.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((D/'evidence/snapshot_manifest.json').read_text());assert sha(src)==manifest['files']['src/cert_forcing2.py']['source_sha256']
assert json.loads((D/'evidence/proof_first.json').read_text())['sha256']==sha(D/'PROOF.md')
tree=ast.parse(src.read_text());fd=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='faa_di_bruno_tables')
ns={};exec(compile(ast.Module(body=[fd],type_ignores=[]),'frozen_integer_composition_table','exec'),ns);actual=ns['faa_di_bruno_tables'](4)
expected={};entries=0
for a in range(5):
 for b in range(5-a):
  table={}
  for j in range(a//2+1):
   for l in range(b//2+1):
    nu=a+b-j-l;mono=(a-2*j,b-2*l)
    c=F(math.factorial(a)*math.factorial(b)*2**sum(mono),math.factorial(mono[0])*math.factorial(mono[1])*math.factorial(j)*math.factorial(l));assert c.denominator==1
    table.setdefault(nu,{})[mono]=c.numerator;entries+=1
  expected[(a,b)]=table
assert actual==expected and len(actual)==15
u,v,q,delta=s.symbols('u v q delta',positive=True);z=s.Symbol('z');S=1-126*z**5+420*z**6-540*z**7+315*z**8-70*z**9
assert s.expand(s.diff(S,z)+630*z**4*(1-z)**4)==0
assert S.subs(z,0)==1 and S.subs(z,1)==0
for j in range(1,5):assert s.diff(S,z,j).subs(z,0)==s.diff(S,z,j).subs(z,1)==0
zeta=2*s.sqrt(q)/delta-s.Rational(7,2);W=q**s.Rational(-1,2)
derivatives=[None,W/delta,-W**3/(2*delta),3*W**5/(4*delta),-15*W**7/(8*delta)]
for j in range(1,5):assert s.simplify(s.diff(zeta,q,j)-derivatives[j])==0
class Expr:
 def __init__(self,x):self.x=s.sympify(x)
 def __add__(self,o):return Expr(self.x+o.x)
 def __mul__(self,o):return Expr(self.x*o.x)
 def scale(self,x):return Expr(self.x*x)
class MR:
 @staticmethod
 def exact(x):return s.Rational(F.from_float(float(x)).numerator,F.from_float(float(x)).denominator)
main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main');records=[]
def assignment(name):
 nodes=[n for n in ast.walk(main) if isinstance(n,ast.Assign) and any(ast.unparse(t)==name for t in n.targets)];assert len(nodes)==1,(name,len(nodes))
 records.append({'target':name,'expression':ast.unparse(nodes[0].value),'line':nodes[0].lineno});return nodes[0].value
def evaluate(node,ns):return eval(compile(ast.Expression(body=copy.deepcopy(node)),'selected_source_symbolic_expression','eval'),ns)
# Evaluate the source composition expression as formal scalar algebra, then
# compare to four direct differentiations of the exact degree-nine polynomial.
sv=[Expr(s.diff(S,z,j).subs(z,zeta)) for j in range(5)]
s1,s2,s3,s4=[Expr(derivatives[j]) for j in range(1,5)]
fns={'Sv':sv,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s1_2':s1*s1,'s1_3':s1*s1*s1,'s1_4':s1*s1*s1*s1,'s1s2':s1*s2,'s1_2s2':s1*s1*s2,'s2_2':s2*s2,'s1s3':s1*s3,'MR':MR}
comp=evaluate(assignment('Shat'),fns)
for j in range(5):assert s.expand(comp[j].x-s.diff(S.subs(z,zeta),q,j))==0,j
# Each tau/g derivative is an independent symbol. Enumerate Leibniz terms
# directly by alpha, not by the producer's Laplacian product identities.
keys=list(expected);ts={k:s.Symbol('t%d%d'%k) for k in keys};gs={k:s.Symbol('g%d%d'%k) for k in keys}
Db={k:Expr(gs[k]) for k in keys};Dtau={k:Expr(ts[k]) for k in keys}
lns={'MR':MR,'Db':Db,'Dtau':Dtau,'g':Db[0,0],'gx':Db[1,0],'gy':Db[0,1],'tau':Dtau[0,0],'tx':Dtau[1,0],'ty':Dtau[0,1]}
for prefix,tab in [('lapg',Db),('lapt',Dtau)]:
 lns[prefix]=tab[2,0]+tab[0,2];lns[prefix+'x']=tab[3,0]+tab[1,2];lns[prefix+'y']=tab[2,1]+tab[0,3]
lns['lap2g']=Db[4,0]+Db[2,2].scale(s.Integer(2))+Db[0,4];lns['lap2t']=Dtau[4,0]+Dtau[2,2].scale(s.Integer(2))+Dtau[0,4]
def leib(a,b):return s.expand(sum(math.comb(a,i)*math.comb(b,j)*ts[i,j]*gs[a-i,b-j] for i in range(a+1) for j in range(b+1)))
expected_products={'f':leib(0,0),'fx':leib(1,0),'fy':leib(0,1),'lapf':leib(2,0)+leib(0,2),'lapfx':leib(3,0)+leib(1,2),'lapfy':leib(2,1)+leib(0,3),'lap2f':leib(4,0)+2*leib(2,2)+leib(0,4)}
product_terms={}
for name,target in expected_products.items():
 val=evaluate(assignment(name),lns).x;assert s.expand(val-target)==0,name
 product_terms[name]=len(s.Poly(s.expand(target),list(ts.values())+list(gs.values())).terms())
# Exact coefficient and recentering combinatorics, independent of floats.
coeffs=[F((-1)**k*math.comb(2*k,k),4**k) for k in range(17)]
for k in range(16):assert abs(coeffs[k+1]/coeffs[k])==F(2*k+1,2*k+2)<1
shiftchecks=0
h=s.Symbol('h');x=s.Symbol('x')
for n in range(13):
 poly=s.Poly(s.expand((x+h)**n),x)
 for j in range(n+1):assert poly.coeff_monomial(x**j)==math.comb(n,j)*h**(n-j);shiftchecks+=1
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_CONDITIONAL_EXACT_CALCULUS','source_sha256':sha(src),'cartesian_multiindices':len(expected),'cartesian_table_entries':entries,'zeta_derivatives':4,'scalar_composition_orders':5,'leibniz_expressions':7,'leibniz_term_counts':product_terms,'binomial_coefficients':list(map(str,coeffs)),'binomial_ratio_checks':16,'centering_binomial_checks':shiftchecks,'source_assignments':records,'composition_tables':{str(k):{str(n):{str(m):c for m,c in p.items()} for n,p in t.items()} for k,t in expected.items()},'scope':'Exact symbolic calculus of the current frozen source. No interval-model implementation or historical pipeline execution accepted.'}
(D/'evidence/calculus.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],'seconds',entries,'table entries',product_terms)
