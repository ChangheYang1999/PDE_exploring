from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
sys.dont_write_bytecode=True
import sympy as s
R=Path(__file__).resolve().parents[3];D=R/'research/annular_degree_five_leakage';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def parse_poly(d,x,y):return sum(s.Rational(q)*x**int(k.split(',')[0])*y**int(k.split(',')[1]) for k,q in d.items())
start=datetime.now(timezone.utc).isoformat();A=load(E/'fraction.json');assert sha(D/'code/fraction_check.py')==A['code_sha256'];assert sha(D/'PROOF.md')==A['proof_sha256'];v=load(R/A['parent_path']);assert sha(R/A['parent_path'])==A['parent_sha256'] and v['files']==A['parent_files']
for p,h in v['files'].items():assert sha(R/p)==h
x,y,n,m,k=s.symbols('x y n m k',real=True);z=x+s.I*y
s5=s.expand(s.im(s.expand(z**5)));s7=s.expand(s.im(s.expand(z**7)));s4=s.expand(s.im(s.expand(z**4)))
factor=s.factor(s5*(x*x+y*y)+s7);assert s.expand(factor-4*x*x*y*(3*x**4-10*x*x*y*y+3*y**4))==0;assert s.expand(factor-parse_poly(A['factor_numerator'],x,y))==0
psi=s4/2;u=s.Matrix([-s.diff(psi,y),s.diff(psi,x)]);grad=s.Matrix([s.diff(x*x*y,x),s.diff(x*x*y,y)]);image=s.expand(u.dot(grad));assert image==2*x**4*y+10*x*x*y**3;assert s.expand(image-parse_poly(A['image_degree_five'],x,y))==0
for i in range(2):assert s.expand(u[i]-parse_poly(A['velocity_cubic'][i],x,y))==0
lo=s.simplify(((n-1)-(n-1))/(4*n));hi=s.simplify(((n-1)+(n+1))/(4*n));assert lo==0 and hi==s.Rational(1,2)
center=s.expand(10-(2*m+2)+1);far=s.expand(2*(k-3)+(-2*k-3)+1);assert center==9-2*m and far==-8
assert s.simplify(4*s.Rational(A['polar_quartic_coefficient'])-s.Rational(A['cartesian_quartic_coefficient']))==0
for row in A['center_exponents']:assert center.subs(m,row['m'])==row['center_radial_exponent'];assert bool(center.subs(m,row['m'])<=-1)==row['diverges']
# Regular degree-six harmonic produces a velocity of degree five and an image of degree seven.
p6=s.expand(s.im(s.expand(z**6)));u6=s.Matrix([-s.diff(p6,y),s.diff(p6,x)]);im7=s.expand(u6.dot(grad));assert s.Poly(im7,x,y).total_degree()==7
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_SYMPY_ANGULAR_GREEN_COEFFICIENT_AND_WEIGHT_CHECKS_REQUIRES_ACTUAL_REVIEW','code_sha256':sha(Path(__file__)),'fraction_json_sha256':sha(E/'fraction.json'),'parent_pin_count':len(v['files']),'factor_identity':str(factor),'quartic_stream':str(psi),'image_degree_five':str(image),'sixth_harmonic_image_degree':7,'moment_lower_symbolic':str(lo),'moment_upper_symbolic':str(hi),'center_exponent_symbolic':str(center),'far_exponent_symbolic':str(far),'scope':'Exact symbolic reconstruction and fresh parent pin verification; no numerical bump integration used or claimed.'}
with (E/'symbolic.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out))
