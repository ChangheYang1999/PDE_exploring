"""Independent symbolic jet check and ordinary quadrature of the resonant moment."""
import sys,json
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.special import roots_legendre
import sympy as sp
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'inverse'/'code'))
from collocation import NodalDensity

t=sp.symbols('t');D0,D2,D4,D6=sp.symbols('D0 D2 D4 D6')
z=sp.atan(t);series=sp.series((1+t*t)*(D0+D2*z**2/2+D4*z**4/24+D6*z**6/720),t,0,8).removeO().expand()
assert sp.simplify(series.coeff(t,4)-(D4+4*D2)/24)==0
assert sp.simplify(series.coeff(t,6)-(D6-10*D4-56*D2)/720)==0
r,theta=sp.symbols('r theta',positive=True)
psi=-sp.Rational(1,2)*r**6*sp.log(r)*sp.sin(6*theta)
lap=sp.diff(psi,r,2)+sp.diff(psi,r)/r+sp.diff(psi,theta,2)/r**2
assert sp.simplify(lap+6*r**4*sp.sin(6*theta))==0
u1=-(sp.sin(theta)*sp.diff(psi,r)+sp.cos(theta)*sp.diff(psi,theta)/r)
assert sp.simplify(u1.subs(theta,0)-3*r**5*sp.log(r))==0
# Fourier action on individual sine modes, checked without the coefficient formula.
cl,c=sp.symbols('cl c');theta=sp.symbols('theta',real=True)
for mode in [3,5,7,9,11,13]:
 P=sp.sin(mode*theta)
 actual=(5*cl-1-5*c*sp.cos(2*theta))*P+c*sp.sin(2*theta)*sp.diff(P,theta)
 expected=(5*cl-1)*P+c*sp.Rational(mode-5,2)*sp.sin((mode+2)*theta)-c*sp.Rational(mode+5,2)*sp.sin((mode-2)*theta)
 assert sp.expand((actual-expected).rewrite(sp.exp))==0
rows=[]
for filename in sys.argv[1:]:
 f=NodalDensity(filename);rec={'source':filename,'md5':f.md5,'quadrature':[]}
 for n in [128,256,512,1024]:
  x,w=roots_legendre(n);ang=(x+1)*np.pi/4
  A=f.center_a_quadratic(ang)
  p7=float(np.sum(w*np.cos(ang)**2*np.sin(ang)*A*np.sin(7*ang)))
  # 4/pi reflection factor times pi/4 mapped quadrature weight.
  pn={m:float(np.sum(w*np.cos(ang)**2*np.sin(ang)*A*np.sin(m*ang))) for m in [7,9,11]}
  rec['quadrature'].append({'n':n,'p7':p7,'w_x5_logx':3*p7,
    'p9':pn[9],'p11':pn[11],
    'balance_determinant':7*pn[9]**2+pn[7]**2-8*pn[7]*pn[11]})
 rows.append(rec)
out={'date':datetime.now(timezone.utc).isoformat(),'symbolic_checks':'four jet/Poisson identities and six Fourier-mode identities, all exact zero','rows':rows}
Path('verifier/center-regularity/verification/axis_formula_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
