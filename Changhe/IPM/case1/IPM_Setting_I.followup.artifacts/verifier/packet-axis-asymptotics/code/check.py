"""Own exact rescaling checks and Gaussian moment evaluations for displayed formulas."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math
import numpy as np
import sympy as s
from scipy.special import beta as beta_fn,gamma
R=Path(__file__).resolve().parents[1]
A,g,j,a,q,b,mu=s.symbols('A g j a q b mu',positive=True)
subs={q:2*(A-1),b:g/(2*(A-1)),mu:(1+g-j)/A}
checks=[]
def ck(name,expr):
 out=s.factor(expr.subs(subs));assert out==0,(name,out);checks.append({'name':name,'residual':str(out)})
ck('rescaled s exponent',g/A-(j-1)/A-mu)
ck('leading radial exponent',j-2-g-(-1-A*mu))
ck('leading t moment',mu-2*b-((1-j)*(A-1)-g)/(A*(A-1)))
ck('Taylor beta first radial exponent',(j-1+A*a)-1-(j-2+A*a))
ck('Taylor beta second parameter',b-(j-1+A*a)/q-(g-j+1-A*a)/q)
ck('first trace logarithmic coefficient',2*s.I*(-2/q)-(-4*s.I/q))
z=s.symbols('z',real=True)
for n in range(1,8):
 f=s.cos(z)-sum((-1)**k*z**(2*k)/s.factorial(2*k)for k in range(n+1));prev=s.cos(z)-sum((-1)**k*z**(2*k)/s.factorial(2*k)for k in range(n));assert s.simplify(s.diff(f,z,2)+prev)==0 and f.subs(z,0)==0 and s.diff(f,z).subs(z,0)==0
 checks.append({'name':f'cosine remainder recurrence n={n}','residual':'0'})
def moments(order,A,g,j):
 nodes,weights=np.polynomial.legendre.leggauss(order);v=(nodes+1)/2;weights=weights/2
 bump=np.exp(-1/(v*(1-v)));t1=1+v;t2=2+v;qq=2*(A-1);bb=g/qq;mm=(1+g-j)/A;cf=(2*math.pi)**-2
 moment=lambda power:2*float(weights@(bump*(t1**power-t2**power)))
 if j==1:center=4*cf/qq*2*float(weights@(bump*(np.log(t1)-np.log(t2))))
 else:center=float((2*(1j)**(j+1)*cf/(math.factorial(j)*qq)*beta_fn((j-1)/qq,(g-j+1)/qq)*moment(-2*(j-1)/qq)).real)
 reJ=gamma(-mm)*math.cos(math.pi*mm/2)
 leading=float((2*(1j)**(j+1)*cf/(math.factorial(j)*A)*reJ*moment(mm-2*bb)).real)
 return {'order':order,'A':A,'g':g,'j':j,'mu':mm,'G_j(0)':center,'C_even':leading,'zero_Phi_mass':0.0}
rows=[]
for aa,gg,jj in [(3.,3.5,3),(10.15,29.75,3),(10.150725,29.74949,3),(3.,3.5,1),(10.15,29.75,1)]:
 lo=moments(128,aa,gg,jj);hi=moments(256,aa,gg,jj)
 for name in ['G_j(0)','C_even']:assert abs(hi[name]-lo[name])<1e-13*max(abs(hi[name]),1e-10),(hi,lo)
 rows.append({'coarse':lo,'fine':hi,'absolute_changes':{name:abs(hi[name]-lo[name])for name in ['G_j(0)','C_even']}})
assert abs(rows[0]['fine']['G_j(0)']/3.1037e-5-1)<2e-5
assert abs(rows[1]['fine']['G_j(0)']/5.418995706e-6-1)<1e-9
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_checks':checks,'numerical_moments':rows,'scope':'Gaussian quadrature of the explicit bump moments and a standard Gamma evaluation of Re J for illustration. This is not direct residual evaluation, a rigorous quadrature enclosure, or an endpoint. The analytic proof establishes nonvanishing without Gamma.','pins':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [R/'PROOF.md',Path(__file__)]}}
(R/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'exact checks,',len(rows),'128/256 point comparisons');print(json.dumps(rows,indent=2))
