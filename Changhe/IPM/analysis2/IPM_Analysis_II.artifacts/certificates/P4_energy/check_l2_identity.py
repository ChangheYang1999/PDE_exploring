"""Independent exact Gaussian-moment check of the L2 coupling identity."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json
x,y=s.symbols('x y',real=True)
a,b,c,d,e,f=s.symbols('a b c d e f')
rho=a*y+b*y**3+c*x*x*y+d*y**5+e*x*x*y**3+f*x**4*y
rx=s.diff(rho,x);ry=s.diff(rho,y)
A=s.Matrix([[ry,-rx/2],[-rx/2,0]])
N=s.Matrix([[s.diff(rho,y,3),-s.diff(rho,x,y,2)],[-s.diff(rho,x,y,2),s.diff(rho,x,2,y)]])/2
q=x*x+y*y

def gauss_moment(n):
    if n%2:return s.S(0)
    m=n//2
    return s.factorial2(2*m-1)*s.sqrt(s.pi)/(2**(2*m)*s.sqrt(2))

def integral(poly):
    total=0
    for (i,j),co in s.Poly(s.expand(poly),x,y).terms():total+=co*gauss_moment(i)*gauss_moment(j)
    return s.simplify(total)

def D(p,axis):return s.diff(p,axis)-2*axis*p

rows=[]
for name,P in [('y',y),('x2y',x*x*y),('mixed',y+x*x*y-y**3)]:
    px=D(P,x);py=D(P,y);pxx=D(px,x);pxy=D(px,y);pyy=D(py,y)
    h=-pxx-pyy
    left=(-rx*pxy+ry*pxx)*h
    Gx=s.Matrix([pxx,pxy]);Gy=s.Matrix([pxy,pyy]);G=s.Matrix([px,py])
    right=-(Gx.T*A*Gx)[0]-(Gy.T*A*Gy)[0]+(G.T*N*G)[0]
    defect=integral(left-right);assert defect==0
    rows.append({'potential_polynomial':name,'rho':'a*y+b*y^3+c*x^2*y+d*y^5+e*x^2*y^3+f*x^4*y','exact_integrated_defect':str(defect)})
    print(name,'exact identity defect',defect)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'Symbolic differentiation and exact moments of exp(-2(x²+y²)); generic parity polynomial background through degree5.','checks':rows}
Path(__file__).with_name('l2_identity_checks.json').write_text(json.dumps(out,indent=2)+'\n')
