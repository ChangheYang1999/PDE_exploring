"""Result211 v2: source delta and the additional exact moment implication."""
from pathlib import Path
import json,hashlib,datetime,difflib
import sympy as S
r=Path('research/hydrostatic_line_core_audit');v=r/'verification';rows=[]
def check(name,value):
 rows.append(dict(name=name,passed=bool(value)));assert value,name
for z in json.loads((v/'V2_INPUTS.json').read_text()):check('source '+z['copy'],hashlib.sha256(Path(z['copy']).read_bytes()).hexdigest()==z['sha256'])
a=(r/'sources/questions__sec377v1__app.txt').read_text();b=(r/'sources/questions__sec377v2__app.txt').read_text();check('appendix byte exact',a==b)
a=(r/'sources/questions__sec377v1__body.txt').read_text();b=(r/'sources/questions__sec377v2__body.txt').read_text()
check('parts a through c byte exact',a.split('(d) c = 2')[0]==b.split('(d) c = 2')[0])
check('all displayed equations exact',[x for x in a.splitlines()if x.startswith('    ')]==[x for x in b.splitlines()if x.startswith('    ')])
w=' '.join(b.split());check('absolute moment clause explicit',"the moment hypothesis of 3.74(d) holds on the axis with Q = p K + Theta''(pi/2) and m_0 = C_0(f_0)"in w)
check('scope distinguishes conditional moments','The moment comparison in (a) uses the two stated moment hypotheses.'in w)
y,p,A,K=S.symbols('y p A K',positive=True);z=S.symbols('z')
H=K*y**p*(1+A*p*y**(p-1))**(p/(1-p));vel=y/p+A*y**p
check('aud25 exact axis solution',S.simplify(S.diff(S.log(H),y)-1/vel)==0)
series=S.series((1+A*p*z)**(p/(1-p)),z,0,3).removeO()
Q=S.symbols('Q');Aq=Q/(p*(1-p))
check('aud25 first correction',S.simplify(series.coeff(z,1).subs(A,Aq)-Q*p/(1-p)**2)==0)
check('aud25 second correction',S.simplify(series.coeff(z,2).subs(A,Aq)-Q**2*p*(2*p-1)/(2*(1-p)**4))==0)
e=S.symbols('e',negative=True)
check('moment tail integrable',S.integrate(y**(e-1),(y,1,S.oo))==-1/e)
check('subtracted origin power integrable',S.integrate(y**(S.Rational(1,2)-1),(y,0,1))==2)
check('v1 manufacture remains PASS',json.loads((v/'CHECKS.json').read_text())['status']=='PASS')
check('v2 frozen exact body identity',hashlib.sha256((r/'sources/questions__sec377v2__body.txt').read_bytes()).hexdigest()=='13ebda43205b1be3aa8bfb75e3d6981f24735536e5b83ee9cc83ebfbce46b25d')
report=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS',count=len(rows),checks=rows,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256((r/'V2_PROOF.md').read_bytes()).hexdigest())
(v/'V2_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n');print(report['utc'],report['status'],report['count'])
